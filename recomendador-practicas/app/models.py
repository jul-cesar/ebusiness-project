"""Entidades del dominio: estudiante, organización, plaza de práctica e historial."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

PROGRAMA_SISTEMAS = "Ingeniería de Sistemas"

# Áreas o énfasis de práctica del programa. La pre-práctica valora al estudiante
# en cada una (escala 0-5) y cada plaza declara el nivel que requiere.
AREAS: tuple[str, ...] = (
    "Desarrollo de Software",
    "Bases de Datos",
    "Redes e Infraestructura",
    "Ciberseguridad",
    "Analítica de Datos",
    "Soporte TI",
)

MODALIDADES = ("presencial", "remota")


@dataclass
class Student:
    id: str
    name: str
    program: str
    municipality: str
    modality_pref: str  # "presencial" | "remota" | "cualquiera"
    area_prefs: list[str]  # preferencias en orden (máximo 3), declaradas en la pre-práctica
    competencies: dict[str, float]  # área -> nivel 0..5 según la pre-práctica
    relatives_at: list[str] = field(default_factory=list)  # organizaciones con familiares (Lineamientos §9)
    works_at: str | None = None  # organización donde trabaja actualmente
    job_matches_profile: bool = False  # funciones del cargo acordes al perfil (§9)
    vaccinated: bool = False  # esquema de vacunación para escenarios de salud (§9)
    intl_insurance: bool = False  # seguro internacional (§8)


@dataclass
class Organization:
    id: str
    name: str
    sector: str  # tecnologia | salud | gobierno | educacion | comercio | financiero
    municipality: str
    country: str
    agreement_until: date  # vigencia del convenio o carta de intención (§10.1, §10.3)

    @property
    def international(self) -> bool:
        return self.country != "Colombia"


@dataclass
class Placement:
    """Plaza de práctica: una organización ofrece cupos en un área."""

    id: str
    org_id: str
    program: str
    area: str
    modality: str  # presencial | remota
    required: dict[str, float]  # área -> nivel requerido 0..5
    slots: int
    slots_taken: int = 0

    @property
    def available(self) -> int:
        return self.slots - self.slots_taken


@dataclass
class HistoryRecord:
    """Resultado de un practicante de semestres anteriores en una plaza."""

    placement_id: str
    competencies: dict[str, float]  # perfil del practicante anterior
    performance: float  # nota de desempeño 1..5 (evaluación del supervisor, §10.4.1)
    rating: float  # evaluación del escenario por el estudiante 1..5 (§10.4.2)


@dataclass
class Dataset:
    students: list[Student]
    organizations: dict[str, Organization]
    placements: list[Placement]
    history: list[HistoryRecord]
    cohort_start: date  # fecha de inicio de la práctica de la cohorte

    def student(self, student_id: str) -> Student:
        for s in self.students:
            if s.id == student_id:
                return s
        raise KeyError(student_id)

    def placement(self, placement_id: str) -> Placement:
        for p in self.placements:
            if p.id == placement_id:
                return p
        raise KeyError(placement_id)
