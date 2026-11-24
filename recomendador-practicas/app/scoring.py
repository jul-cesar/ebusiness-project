"""Etapa 2: puntaje híbrido y explicable de cada plaza elegible.

    S = Σ wᵢ · fᵢ / Σ wᵢ          con fᵢ ∈ [0, 1]

Factores:
  area          contenido     afinidad entre el área de la plaza y las preferencias del estudiante
  competencias  contenido     fracción de las competencias requeridas que el estudiante cubre
  calidad       historial     evaluación del escenario por estudiantes anteriores (promedio bayesiano)
  similares     colaborativo  nota obtenida por practicantes de perfil parecido (kNN + prior)
  logistica     contenido     mismo municipio (o plaza remota) y modalidad preferida

La contribución de cada factor es wᵢ·fᵢ/Σw; por construcción su suma es exactamente S.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass, field

from app.models import AREAS, Dataset, HistoryRecord, Organization, Placement, Student
from app.rules import RULES, Violation, violations

FACTORS: tuple[str, ...] = ("area", "competencias", "calidad", "similares", "logistica")

FACTOR_LABELS = {
    "area": "Afinidad de área",
    "competencias": "Ajuste de competencias",
    "calidad": "Calidad del escenario",
    "similares": "Éxito de perfiles similares",
    "logistica": "Logística",
}

DEFAULT_WEIGHTS = {"area": 0.30, "competencias": 0.25, "calidad": 0.15, "similares": 0.20, "logistica": 0.10}

PREF_SCORES = (1.0, 0.6, 0.3)  # 1.ª, 2.ª y 3.ª preferencia
MAX_DISTANCE = 5.0 * math.sqrt(len(AREAS))  # distancia máxima entre dos perfiles 0..5


@dataclass(frozen=True)
class Params:
    weights: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_WEIGHTS))
    k: int = 5  # vecinos del kNN
    m: float = 3.0  # fuerza del prior (evaluaciones "virtuales" con el promedio general)
    top_n: int = 5
    disabled_rules: frozenset[str] = frozenset()

    def normalized_weights(self) -> dict[str, float]:
        unknown = set(self.weights) - set(FACTORS)
        if unknown:
            raise ValueError(f"Factores desconocidos: {sorted(unknown)}")
        w = {f: float(self.weights.get(f, 0.0)) for f in FACTORS}
        if any(v < 0 for v in w.values()):
            raise ValueError("Los pesos no pueden ser negativos")
        total = sum(w.values())
        if total == 0:
            raise ValueError("Al menos un peso debe ser mayor que cero")
        return {f: v / total for f, v in w.items()}


@dataclass
class FactorDetail:
    value: float  # fᵢ en [0, 1]
    weight: float  # peso normalizado
    contribution: float  # weight * value
    text: str  # explicación en lenguaje natural


@dataclass
class ScoredPlacement:
    placement: Placement
    org: Organization
    score: float
    factors: dict[str, FactorDetail]
    cold_start: bool  # la plaza no tiene historial: calidad y similares usan el prior


@dataclass
class Exclusion:
    placement: Placement
    org: Organization
    violations: list[Violation]


@dataclass
class Recommendation:
    student: Student
    ranking: list[ScoredPlacement]  # top-N elegibles
    eligible_count: int
    excluded: list[Exclusion]
    message: str | None  # aviso cuando no hay plazas elegibles


def _fmt(x: float, d: int = 1) -> str:
    return f"{x:.{d}f}".replace(".", ",")


def to_unit(grade: float) -> float:
    """Escala 1..5 -> 0..1."""
    return (grade - 1.0) / 4.0


def area_affinity(student: Student, placement: Placement) -> tuple[float, str]:
    if placement.area in student.area_prefs[:3]:
        pos = student.area_prefs.index(placement.area)
        return PREF_SCORES[pos], f"{placement.area} es su {pos + 1}.ª preferencia"
    return 0.0, f"{placement.area} no está entre sus áreas preferidas"


def competency_fit(student: Student, placement: Placement) -> tuple[float, str]:
    total = sum(placement.required.values())
    if total == 0:
        return 1.0, "La plaza no declara competencias requeridas"
    covered = sum(min(student.competencies.get(a, 0.0), lvl) for a, lvl in placement.required.items())
    gaps = sorted(
        ((a, lvl - student.competencies.get(a, 0.0)) for a, lvl in placement.required.items()
         if student.competencies.get(a, 0.0) < lvl),
        key=lambda g: -g[1],
    )
    fit = covered / total
    text = f"Cubre el {_fmt(100 * fit, 0)} % de lo requerido"
    if gaps:
        a, gap = gaps[0]
        text += f"; mayor brecha en {a} (requiere {_fmt(placement.required[a])}, tiene {_fmt(student.competencies.get(a, 0.0))})"
    return fit, text


def similarity(a: dict[str, float], b: dict[str, float]) -> float:
    """1 = perfiles idénticos; 0 = máxima distancia posible."""
    dist = math.sqrt(sum((a.get(x, 0.0) - b.get(x, 0.0)) ** 2 for x in AREAS))
    return 1.0 - dist / MAX_DISTANCE


def logistics(student: Student, placement: Placement, org: Organization) -> tuple[float, str]:
    if placement.modality == "remota":
        loc, loc_txt = 1.0, "plaza remota (no requiere traslado)"
    elif org.municipality == student.municipality:
        loc, loc_txt = 1.0, f"mismo municipio ({org.municipality})"
    else:
        loc, loc_txt = 0.0, f"requiere traslado a {org.municipality}"
    mod_ok = student.modality_pref == "cualquiera" or student.modality_pref == placement.modality
    mod_txt = f"modalidad {placement.modality} {'acorde' if mod_ok else 'distinta'} a su preferencia"
    return 0.5 * loc + 0.5 * float(mod_ok), f"{loc_txt.capitalize()}; {mod_txt}"


class Recommender:
    def __init__(self, dataset: Dataset):
        self.ds = dataset
        self.history: dict[str, list[HistoryRecord]] = defaultdict(list)
        for h in dataset.history:
            self.history[h.placement_id].append(h)
        n = len(dataset.history)
        # Promedios globales: el prior para plazas con poco o ningún historial.
        self.global_rating = sum(h.rating for h in dataset.history) / n if n else 3.0
        self.global_performance = sum(h.performance for h in dataset.history) / n if n else 3.0

    # -- factores que usan historial --------------------------------------
    def quality(self, placement: Placement, m: float) -> tuple[float, str]:
        ratings = [h.rating for h in self.history[placement.id]]
        n = len(ratings)
        bayes = (m * self.global_rating + sum(ratings)) / (m + n) if n else self.global_rating
        if n == 0:
            return to_unit(bayes), f"Sin evaluaciones previas: se usa el promedio general {_fmt(self.global_rating, 2)}/5 (arranque en frío)"
        raw = sum(ratings) / n
        return to_unit(bayes), f"Evaluada {_fmt(raw, 2)}/5 por {n} estudiantes; ajustada a {_fmt(bayes, 2)}/5 con el promedio bayesiano"

    def similar_success(self, student: Student, placement: Placement, k: int, m: float) -> tuple[float, str]:
        records = self.history[placement.id]
        if not records:
            return to_unit(self.global_performance), f"Sin practicantes anteriores: se usa la nota general {_fmt(self.global_performance, 2)}/5 (arranque en frío)"
        neigh = sorted(((similarity(student.competencies, r.competencies), r.performance) for r in records),
                       key=lambda t: -t[0])[: max(1, k)]
        wsum = sum(s for s, _ in neigh)
        raw = sum(s * perf for s, perf in neigh) / wsum if wsum else self.global_performance
        est = (raw * wsum + m * self.global_performance) / (wsum + m) if wsum else self.global_performance
        avg_sim = wsum / len(neigh)
        return to_unit(est), (f"Los {len(neigh)} practicantes más parecidos (similitud media {_fmt(avg_sim, 2)}) "
                              f"obtuvieron {_fmt(raw, 2)}/5; estimado {_fmt(est, 2)}/5")

    # -- puntaje -----------------------------------------------------------
    def score(self, student: Student, placement: Placement, params: Params) -> ScoredPlacement:
        weights = params.normalized_weights()
        org = self.ds.organizations[placement.org_id]
        raw = {
            "area": area_affinity(student, placement),
            "competencias": competency_fit(student, placement),
            "calidad": self.quality(placement, params.m),
            "similares": self.similar_success(student, placement, params.k, params.m),
            "logistica": logistics(student, placement, org),
        }
        factors = {
            f: FactorDetail(value=v, weight=weights[f], contribution=weights[f] * v, text=t)
            for f, (v, t) in raw.items()
        }
        score = sum(d.contribution for d in factors.values())
        return ScoredPlacement(placement, org, score, factors, cold_start=not self.history[placement.id])

    def exclusions(self, student: Student, placement: Placement, params: Params) -> list[Violation]:
        org = self.ds.organizations[placement.org_id]
        return violations(student, placement, org, self.ds.cohort_start, params.disabled_rules)

    def recommend(self, student: Student, params: Params | None = None) -> Recommendation:
        params = params or Params()
        scored, excluded = [], []
        for p in self.ds.placements:
            v = self.exclusions(student, p, params)
            if v:
                excluded.append(Exclusion(p, self.ds.organizations[p.org_id], v))
            else:
                scored.append(self.score(student, p, params))
        scored.sort(key=lambda s: (-s.score, s.placement.id))  # desempate determinista
        message = None
        if not scored:
            message = ("No hay plazas elegibles para este estudiante con las reglas activas. "
                       "La Coordinación de Prácticas debe gestionar un nuevo escenario o revisar su caso.")
        return Recommendation(student, scored[: params.top_n], len(scored), excluded, message)


def rules_catalog() -> list[dict[str, str]]:
    return [{"id": r.id, "name": r.name, "reference": r.reference} for r in RULES]
