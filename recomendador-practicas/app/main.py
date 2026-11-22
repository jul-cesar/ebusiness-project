"""API REST del recomendador y servidor del frontend.

Ejecutar:  uv run uvicorn app.main:app --reload
Documentación interactiva: http://127.0.0.1:8000/docs
"""

from __future__ import annotations

import os
from dataclasses import asdict, replace
from functools import lru_cache
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.assignment import CohortResult, assign_greedy, assign_hungarian
from app.db import DEFAULT_DB, load_dataset, save_dataset
from app.evaluation import evaluate
from app.models import AREAS, Dataset, Student
from app.rules import RULE_IDS
from app.scoring import (
    DEFAULT_WEIGHTS,
    FACTOR_LABELS,
    FACTORS,
    Params,
    Recommender,
    ScoredPlacement,
    rules_catalog,
)
from app.seed import build_world

STATIC_DIR = Path(__file__).resolve().parent / "static"


class StudentPatch(BaseModel):
    """Cambios hipotéticos sobre un estudiante ("¿qué pasa si…?"). No se guardan."""

    municipality: str | None = None
    modality_pref: str | None = Field(None, pattern="^(presencial|remota|cualquiera)$")
    area_prefs: list[str] | None = Field(None, min_length=1, max_length=3)
    competencies: dict[str, float] | None = None
    relatives_at: list[str] | None = None
    works_at: str | None = None
    job_matches_profile: bool | None = None
    m: float = Field(3.0, gt=0, le=100)
    intl_insurance: bool | None = None


class ParamsIn(BaseModel):
    weights: dict[str, float] = Field(default_factory=lambda: dict(DEFAULT_WEIGHTS))
    k: int = Field(5, ge=1, le=50)
    m: float = Field(3.0, ge=0, le=100)
    top_n: int = Field(5, ge=1, le=50)
    disabled_rules: list[str] = Field(default_factory=list)

    def to_params(self) -> Params:
        unknown = set(self.disabled_rules) - set(RULE_IDS)
        if unknown:
            raise HTTPException(422, f"Reglas desconocidas: {sorted(unknown)}")
        params = Params(dict(self.weights), self.k, self.m, self.top_n, frozenset(self.disabled_rules))
        try:
            params.normalized_weights()
        except ValueError as e:
            raise HTTPException(422, str(e)) from e
        return params


class RecommendIn(ParamsIn):
    student_id: str
    overrides: StudentPatch | None = None


def student_out(s: Student) -> dict:
    return asdict(s)


def scored_out(sp: ScoredPlacement, rank: int) -> dict:
    p = sp.placement
    return {
        "rank": rank,
        "placement_id": p.id,
        "organization": sp.org.name,
        "sector": sp.org.sector,
        "municipality": sp.org.municipality,
        "area": p.area,
        "modality": p.modality,
        "available": p.available,
        "score": round(sp.score, 4),
        "cold_start": sp.cold_start,
        "factors": {
            f: {"label": FACTOR_LABELS[f], "value": round(d.value, 4), "weight": round(d.weight, 4),
                "contribution": round(d.contribution, 4), "text": d.text}
            for f, d in sp.factors.items()
        },
    }


def cohort_out(r: CohortResult, ds: Dataset) -> dict:
    names = {s.id: s.name for s in ds.students}
    return {
        "method": r.method,
        "assigned": len(r.assignments),
        "unassigned": [{"student_id": sid, "name": names[sid]} for sid in r.unassigned],
        "total_score": round(r.total_score, 4),
        "mean_score": round(r.mean_score, 4),
        "assignments": [
            {"student_id": a.student_id, "name": names[a.student_id], "placement_id": a.placement_id,
             "organization": ds.organizations[ds.placement(a.placement_id).org_id].name,
             "area": ds.placement(a.placement_id).area, "score": round(a.score, 4)}
            for a in sorted(r.assignments, key=lambda a: a.student_id)
        ],
    }


def create_app(dataset: Dataset) -> FastAPI:
    app = FastAPI(title="Recomendador de escenarios de práctica profesional", version="1.0.0")
    rec = Recommender(dataset)

    @app.get("/api/meta")
    def meta() -> dict:
        return {
            "areas": AREAS,
            "factors": [{"id": f, "label": FACTOR_LABELS[f], "default_weight": DEFAULT_WEIGHTS[f]} for f in FACTORS],
            "rules": rules_catalog(),
            "defaults": {"k": 5, "m": 3.0, "top_n": 5},
            "cohort_start": dataset.cohort_start.isoformat(),
            "organizations": [{"id": o.id, "name": o.name} for o in dataset.organizations.values()],
        }

    @app.get("/api/students")
    def students() -> list[dict]:
        return [student_out(s) for s in dataset.students]

    @app.get("/api/placements")
    def placements() -> list[dict]:
        out = []
        for p in dataset.placements:
            o = dataset.organizations[p.org_id]
            hist = rec.history[p.id]
            out.append({
                **asdict(p), "available": p.available, "organization": o.name, "sector": o.sector,
                "municipality": o.municipality, "country": o.country,
                "agreement_until": o.agreement_until.isoformat(), "history_count": len(hist),
                "mean_rating": round(sum(h.rating for h in hist) / len(hist), 2) if hist else None,
            })
        return out

    @app.post("/api/recommend")
    def recommend(body: RecommendIn) -> dict:
        try:
            student = dataset.student(body.student_id)
        except KeyError:
            raise HTTPException(404, f"Estudiante {body.student_id} no existe") from None
        if body.overrides:
            changes = body.overrides.model_dump(exclude_unset=True)
            bad = [a for a in changes.get("area_prefs") or [] if a not in AREAS]
            bad += [a for a in changes.get("competencies") or {} if a not in AREAS]
            if bad:
                raise HTTPException(422, f"Áreas desconocidas: {bad}")
            student = replace(student, **changes)
        result = rec.recommend(student, body.to_params())
        return {
            "student": student_out(student),
            "eligible_count": result.eligible_count,
            "message": result.message,
            "ranking": [scored_out(sp, i + 1) for i, sp in enumerate(result.ranking)],
            "excluded": [
                {"placement_id": e.placement.id, "organization": e.org.name, "area": e.placement.area,
                 "violations": [asdict(v) for v in e.violations]}
                for e in result.excluded
            ],
        }

    @app.post("/api/cohort")
    def cohort(body: ParamsIn) -> dict:
        params = body.to_params()
        hung = assign_hungarian(rec, dataset.students, params)
        greedy = assign_greedy(rec, dataset.students, params)
        return {"hungaro": cohort_out(hung, dataset), "greedy": cohort_out(greedy, dataset)}

    @app.get("/api/evaluation")
    def evaluation() -> dict:
        return _cached_evaluation()

    if STATIC_DIR.exists():
        app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
    return app


@lru_cache(maxsize=1)
def _cached_evaluation() -> dict:
    return evaluate()


def _load_default() -> Dataset:
    if not os.path.exists(DEFAULT_DB):
        Path(DEFAULT_DB).parent.mkdir(parents=True, exist_ok=True)
        save_dataset(build_world().dataset, DEFAULT_DB)
    return load_dataset(DEFAULT_DB)


app = create_app(_load_default())
