"""Etapa 1: reglas duras de elegibilidad tomadas de los Lineamientos de Práctica 2026.

Una plaza que incumple una regla NO se puntúa: se excluye y se informa el motivo
con su referencia normativa. Las reglas no se "aprenden" ni se compensan con un
buen puntaje: son condiciones institucionales.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import date

from app.models import Organization, Placement, Student

Check = Callable[[Student, Placement, Organization, date], str | None]


@dataclass(frozen=True)
class Rule:
    id: str
    name: str
    reference: str
    check: Check  # devuelve el motivo si la regla se incumple; None si se cumple


@dataclass(frozen=True)
class Violation:
    rule_id: str
    rule_name: str
    reason: str
    reference: str


def _program(s: Student, p: Placement, o: Organization, start: date) -> str | None:
    if p.program != s.program:
        return f"La plaza es para {p.program}; el estudiante es de {s.program}."
    return None


def _agreement(s: Student, p: Placement, o: Organization, start: date) -> str | None:
    if o.agreement_until < start:
        return f"El convenio con {o.name} venció el {o.agreement_until.isoformat()}, antes del inicio ({start.isoformat()})."
    return None


def _slots(s: Student, p: Placement, o: Organization, start: date) -> str | None:
    if p.available <= 0:
        return f"Sin cupos disponibles ({p.slots_taken} de {p.slots} ocupados)."
    return None


def _relatives(s: Student, p: Placement, o: Organization, start: date) -> str | None:
    if o.id in s.relatives_at:
        return f"El estudiante declaró familiares en {o.name} (propietarios, directivos o supervisor)."
    return None


def _workplace(s: Student, p: Placement, o: Organization, start: date) -> str | None:
    if s.works_at == o.id and not s.job_matches_profile:
        return f"Trabaja en {o.name}, pero las funciones de su cargo no son acordes al perfil del programa."
    return None


def _health(s: Student, p: Placement, o: Organization, start: date) -> str | None:
    if o.sector == "salud" and not s.vaccinated:
        return f"{o.name} es un escenario de salud y el estudiante no acredita el esquema de vacunación."
    return None


def _international(s: Student, p: Placement, o: Organization, start: date) -> str | None:
    if o.international and not s.intl_insurance:
        return f"Práctica en {o.country}: requiere seguro de salud y accidentes internacional."
    return None


RULES: tuple[Rule, ...] = (
    Rule("R1", "Pertinencia con el programa", "Lineamientos §6 y §5.3: actividades articuladas al perfil del programa", _program),
    Rule("R2", "Convenio vigente", "Lineamientos §10.1 y §10.3: formalización por alianza o carta de intención", _agreement),
    Rule("R3", "Cupo disponible", "Condición operativa del escenario (asignación, Lineamientos §3.4.i)", _slots),
    Rule("R4", "Sin vínculo familiar", "Lineamientos §9: parentesco hasta 3.er grado de consanguinidad, 2.º de afinidad o 1.º civil", _relatives),
    Rule("R5", "Práctica donde labora", "Lineamientos §9: funciones del cargo acordes al perfil del programa", _workplace),
    Rule("R6", "Vacunación en salud", "Lineamientos §9: esquema de vacunación en escenarios de salud", _health),
    Rule("R7", "Seguro internacional", "Lineamientos §8: seguro de salud y accidentes internacional", _international),
)

RULE_IDS = tuple(r.id for r in RULES)


def violations(
    student: Student,
    placement: Placement,
    org: Organization,
    cohort_start: date,
    disabled: frozenset[str] = frozenset(),
) -> list[Violation]:
    """Todas las reglas activas que la plaza incumple para el estudiante."""
    found = []
    for rule in RULES:
        if rule.id in disabled:
            continue
        reason = rule.check(student, placement, org, cohort_start)
        if reason is not None:
            found.append(Violation(rule.id, rule.name, reason, rule.reference))
    return found
