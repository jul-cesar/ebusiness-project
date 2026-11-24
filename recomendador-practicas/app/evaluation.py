"""Evaluación offline del recomendador sobre el mundo simulado.

Para estudiantes de prueba que el sistema nunca vio, el mundo simulado conoce el
desempeño esperado real de cada plaza (usa la calidad oculta). Con eso se mide
qué tan bien ordena cada método las plazas elegibles:

  NDCG@5        calidad del orden de las 5 primeras (1 = orden ideal)
  Precision@5   cuántas de las 5 recomendadas están entre las 5 mejores reales
  Nota top-1    desempeño esperado (1..5) en la plaza recomendada en 1.er lugar

Métodos comparados:
  híbrido          el recomendador completo
  solo contenido   el mismo, sin factores de historial (calidad = similares = 0)
  popularidad      ordena por número de practicantes anteriores y su evaluación
  aleatorio        orden al azar (promedio de 20 repeticiones)

Limitación: el mundo lo generamos nosotros. La evaluación prueba que el método
recupera relaciones cuando existen; no prueba que existan en CECAR.
"""

from __future__ import annotations

import math
import random
from collections import Counter
from dataclasses import replace

from app.models import Student
from app.scoring import Params, Recommender
from app.seed import SEED, build_world, generate_students, world_utility

K = 5


def dcg(gains: list[float]) -> float:
    return sum(g / math.log2(i + 2) for i, g in enumerate(gains))


def ndcg_at_k(ranked: list[str], truth: dict[str, float], k: int = K) -> float:
    ideal = sorted(truth.values(), reverse=True)[:k]
    idcg = dcg(ideal)
    return dcg([truth[p] for p in ranked[:k]]) / idcg if idcg > 0 else 0.0


def precision_at_k(ranked: list[str], truth: dict[str, float], k: int = K) -> float:
    best = set(sorted(truth, key=lambda p: (-truth[p], p))[:k])
    return len(best & set(ranked[:k])) / k


def _hybrid_ranking(rec: Recommender, s: Student, params: Params) -> list[str]:
    full = replace(params, top_n=len(rec.ds.placements))
    return [sp.placement.id for sp in rec.recommend(s, full).ranking]


def _popularity_ranking(rec: Recommender, eligible: list[str]) -> list[str]:
    def key(pid: str) -> tuple[float, float, str]:
        hist = rec.history[pid]
        mean = sum(h.rating for h in hist) / len(hist) if hist else 0.0
        return (-len(hist), -mean, pid)

    return sorted(eligible, key=key)


def evaluate(params: Params | None = None, n_test: int = 200, seed: int = SEED) -> dict:
    params = params or Params()
    world = build_world(seed)
    ds = world.dataset
    rec = Recommender(ds)
    rng = random.Random(seed + 1000)
    test_students = generate_students(rng, n_test, "T")

    content_only = replace(params, weights={**params.weights, "calidad": 0.0, "similares": 0.0})
    metrics: dict[str, dict[str, list[float]]] = {
        m: {"ndcg": [], "precision": [], "top1": []}
        for m in ("hibrido", "solo_contenido", "popularidad", "aleatorio")
    }
    evaluated = 0
    for s in test_students:
        eligible = [p.id for p in ds.placements if not rec.exclusions(s, p, params)]
        if len(eligible) < K:
            continue
        evaluated += 1
        truth = {
            pid: world_utility(s, ds.placement(pid), ds.organizations[ds.placement(pid).org_id], world.latent_quality[pid])
            for pid in eligible
        }
        rankings = {
            "hibrido": _hybrid_ranking(rec, s, params),
            "solo_contenido": _hybrid_ranking(rec, s, content_only),
            "popularidad": _popularity_ranking(rec, eligible),
        }
        for name, ranked in rankings.items():
            metrics[name]["ndcg"].append(ndcg_at_k(ranked, truth))
            metrics[name]["precision"].append(precision_at_k(ranked, truth))
            metrics[name]["top1"].append(1 + 4 * truth[ranked[0]])
        for _ in range(20):
            shuffled = eligible[:]
            rng.shuffle(shuffled)
            metrics["aleatorio"]["ndcg"].append(ndcg_at_k(shuffled, truth))
            metrics["aleatorio"]["precision"].append(precision_at_k(shuffled, truth))
            metrics["aleatorio"]["top1"].append(1 + 4 * truth[shuffled[0]])

    def mean(xs: list[float]) -> float:
        return round(sum(xs) / len(xs), 4) if xs else 0.0

    return {
        "estudiantes_prueba": evaluated,
        "k": K,
        "metodos": {
            name: {"ndcg_at_5": mean(v["ndcg"]), "precision_at_5": mean(v["precision"]), "nota_top1": mean(v["top1"])}
            for name, v in metrics.items()
        },
        "sesgo_popularidad": popularity_bias(rec, ds.students, params),
    }


def popularity_bias(rec: Recommender, students: list[Student], params: Params) -> dict:
    """¿Las recomendaciones se concentran en las plazas con más historial?

    cobertura: % de plazas elegibles que aparecen en algún top-5.
    concentracion_top20: % de recomendaciones que van al 20 % de plazas con más historial.
    """
    placements = [p.id for p in rec.ds.placements]
    by_history = sorted(placements, key=lambda pid: (-len(rec.history[pid]), pid))
    popular = set(by_history[: max(1, len(placements) // 5)])
    out = {}
    for name in ("hibrido", "popularidad"):
        counts: Counter[str] = Counter()
        eligible_any: set[str] = set()
        for s in students:
            eligible = [p.id for p in rec.ds.placements if not rec.exclusions(s, p, params)]
            if not eligible:
                continue
            eligible_any.update(eligible)
            ranked = _hybrid_ranking(rec, s, params) if name == "hibrido" else _popularity_ranking(rec, eligible)
            counts.update(ranked[:K])
        total = sum(counts.values())
        out[name] = {
            "cobertura": round(len(counts) / len(eligible_any), 4) if eligible_any else 0.0,
            "concentracion_top20": round(sum(counts[p] for p in popular) / total, 4) if total else 0.0,
        }
    out["plazas_populares"] = sorted(popular)
    return out


if __name__ == "__main__":
    import json
    from pathlib import Path

    result = evaluate()
    out = Path(__file__).resolve().parent.parent / "evidencias" / "resultados_evaluacion.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nGuardado en {out}")
