"""Etapa 3 (opcional): propuesta de asignación para toda la cohorte.

Cada plaza se replica tantas veces como cupos disponibles tenga. Se resuelve un
problema de asignación (algoritmo húngaro, scipy.optimize.linear_sum_assignment):

  1.º maximiza el número de estudiantes asignados a una plaza elegible;
  2.º entre esas soluciones, maximiza la suma de puntajes.

Se compara con una línea base voraz (greedy): recorre los pares estudiante-plaza
de mayor a menor puntaje y asigna si ambos siguen libres.
La propuesta es un insumo para la Coordinación de Prácticas, no una decisión.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np
from scipy.optimize import linear_sum_assignment

from app.models import Student
from app.scoring import Params, Recommender

INFEASIBLE = 1e6  # costo de un par no elegible; domina cualquier suma de puntajes


@dataclass
class Assignment:
    student_id: str
    placement_id: str
    score: float


@dataclass
class CohortResult:
    method: str
    assignments: list[Assignment]
    unassigned: list[str]

    @property
    def total_score(self) -> float:
        return sum(a.score for a in self.assignments)

    @property
    def mean_score(self) -> float:
        return self.total_score / len(self.assignments) if self.assignments else 0.0


def eligible_scores(rec: Recommender, students: list[Student], params: Params) -> dict[tuple[str, str], float]:
    """Puntaje de cada par elegible. El cupo (R3) lo administra la asignación, no el filtro."""
    p = replace(params, disabled_rules=params.disabled_rules | {"R3"})
    scores = {}
    for s in students:
        for pl in rec.ds.placements:
            if pl.available > 0 and not rec.exclusions(s, pl, p):
                scores[(s.id, pl.id)] = rec.score(s, pl, p).score
    return scores


def assign_hungarian(rec: Recommender, students: list[Student], params: Params) -> CohortResult:
    scores = eligible_scores(rec, students, params)
    seats = [pl.id for pl in rec.ds.placements for _ in range(max(0, pl.available))]
    if not students or not seats:
        return CohortResult("hungaro", [], [s.id for s in students])
    cost = np.full((len(students), len(seats)), INFEASIBLE)
    for i, s in enumerate(students):
        for j, pid in enumerate(seats):
            if (s.id, pid) in scores:
                cost[i, j] = -scores[(s.id, pid)]
    rows, cols = linear_sum_assignment(cost)
    assignments = [
        Assignment(students[i].id, seats[j], scores[(students[i].id, seats[j])])
        for i, j in zip(rows, cols, strict=True)
        if cost[i, j] < INFEASIBLE
    ]
    done = {a.student_id for a in assignments}
    return CohortResult("hungaro", assignments, [s.id for s in students if s.id not in done])


def assign_greedy(rec: Recommender, students: list[Student], params: Params) -> CohortResult:
    scores = eligible_scores(rec, students, params)
    capacity = {pl.id: pl.available for pl in rec.ds.placements}
    assignments, done = [], set()
    for (sid, pid), sc in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0])):
        if sid not in done and capacity[pid] > 0:
            assignments.append(Assignment(sid, pid, sc))
            done.add(sid)
            capacity[pid] -= 1
    return CohortResult("greedy", assignments, [s.id for s in students if s.id not in done])
