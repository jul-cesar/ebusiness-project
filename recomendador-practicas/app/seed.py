"""Generador de datos ficticios reproducibles (semilla fija).

Simula un "mundo" con una cohorte de estudiantes, organizaciones, plazas e historial
de practicantes anteriores. El mundo tiene variables ocultas (calidad real de cada
plaza) que el recomendador NO ve: solo ve el historial observado (notas y
evaluaciones con ruido). Las variables ocultas se usan únicamente en la evaluación
offline para saber cuál habría sido la mejor plaza para cada estudiante.

Ningún dato corresponde a personas u organizaciones reales (Ley 1581 de 2012).
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import date

from app.models import (
    AREAS,
    PROGRAMA_SISTEMAS,
    Dataset,
    HistoryRecord,
    Organization,
    Placement,
    Student,
)

SEED = 42
COHORT_START = date(2027, 1, 25)

# Áreas relacionadas: una plaza de un área también exige algo de estas.
RELATED: dict[str, dict[str, int]] = {
    "Desarrollo de Software": {"Bases de Datos": 2, "Analítica de Datos": 1},
    "Bases de Datos": {"Desarrollo de Software": 2, "Analítica de Datos": 2},
    "Redes e Infraestructura": {"Ciberseguridad": 2, "Soporte TI": 2},
    "Ciberseguridad": {"Redes e Infraestructura": 3, "Soporte TI": 1},
    "Analítica de Datos": {"Bases de Datos": 3, "Desarrollo de Software": 2},
    "Soporte TI": {"Redes e Infraestructura": 2},
}

ORGANIZATIONS: list[Organization] = [
    Organization("O01", "SoftCaribe S.A.S.", "tecnologia", "Sincelejo", "Colombia", date(2027, 12, 31)),
    Organization("O02", "DataSucre Analytics", "tecnologia", "Sincelejo", "Colombia", date(2028, 6, 30)),
    Organization("O03", "Clínica Santa María", "salud", "Sincelejo", "Colombia", date(2027, 12, 31)),
    Organization("O04", "Hospital Regional de Sucre", "salud", "Sincelejo", "Colombia", date(2028, 12, 31)),
    Organization("O05", "Gobernación de Sucre - Oficina TIC", "gobierno", "Sincelejo", "Colombia", date(2027, 12, 31)),
    Organization("O06", "Alcaldía de Corozal", "gobierno", "Corozal", "Colombia", date(2027, 6, 30)),
    Organization("O07", "RedNet Telecomunicaciones", "tecnologia", "Montería", "Colombia", date(2028, 3, 31)),
    Organization("O08", "CiberSeguro Colombia", "tecnologia", "Bogotá", "Colombia", date(2027, 12, 31)),
    Organization("O09", "Banco Regional del Caribe", "financiero", "Sincelejo", "Colombia", date(2028, 12, 31)),
    Organization("O10", "Supermercados La Sabana", "comercio", "Sincelejo", "Colombia", date(2027, 12, 31)),
    Organization("O11", "Institución Educativa San José", "educacion", "Sampués", "Colombia", date(2027, 12, 31)),
    Organization("O12", "Hotel Golfo de Morrosquillo", "comercio", "Tolú", "Colombia", date(2027, 9, 30)),
    Organization("O13", "TechPanamá Corp", "tecnologia", "Ciudad de Panamá", "Panamá", date(2028, 6, 30)),
    Organization("O14", "Cooperativa Agropecuaria del Sinú", "comercio", "Montería", "Colombia", date(2026, 6, 30)),
    Organization("O15", "Startup NovaLab", "tecnologia", "Sincelejo", "Colombia", date(2028, 12, 31)),
    Organization("O16", "Clínica del Golfo", "salud", "Tolú", "Colombia", date(2027, 12, 31)),
    Organization("O17", "AgroData Córdoba", "tecnologia", "Montería", "Colombia", date(2028, 12, 31)),
    Organization("O18", "Notaría Segunda de Sincelejo", "comercio", "Sincelejo", "Colombia", date(2027, 12, 31)),
    Organization("O19", "Dirección TIC Universitaria", "educacion", "Sincelejo", "Colombia", date(2029, 12, 31)),
    Organization("O20", "Logística Costa Norte", "comercio", "Cartagena", "Colombia", date(2027, 12, 31)),
]

# (id, organización, área, modalidad, cupos, cupos ya ocupados)
PLACEMENT_SPECS: list[tuple[str, str, str, str, int, int]] = [
    ("P01", "O01", "Desarrollo de Software", "presencial", 3, 0),
    ("P02", "O01", "Bases de Datos", "presencial", 1, 0),
    ("P03", "O02", "Analítica de Datos", "presencial", 2, 0),
    ("P04", "O02", "Bases de Datos", "remota", 1, 0),
    ("P05", "O03", "Soporte TI", "presencial", 2, 0),
    ("P06", "O04", "Soporte TI", "presencial", 1, 0),
    ("P07", "O04", "Bases de Datos", "presencial", 1, 0),
    ("P08", "O05", "Desarrollo de Software", "presencial", 2, 0),
    ("P09", "O05", "Redes e Infraestructura", "presencial", 1, 0),
    ("P10", "O06", "Soporte TI", "presencial", 2, 0),
    ("P11", "O07", "Redes e Infraestructura", "presencial", 2, 0),
    ("P12", "O07", "Ciberseguridad", "presencial", 1, 0),
    ("P13", "O08", "Ciberseguridad", "remota", 2, 0),
    ("P14", "O08", "Desarrollo de Software", "remota", 1, 0),
    ("P15", "O09", "Bases de Datos", "presencial", 1, 0),
    ("P16", "O09", "Ciberseguridad", "presencial", 1, 0),
    ("P17", "O09", "Analítica de Datos", "presencial", 1, 0),
    ("P18", "O10", "Soporte TI", "presencial", 1, 0),
    ("P19", "O10", "Desarrollo de Software", "presencial", 1, 0),
    ("P20", "O11", "Soporte TI", "presencial", 1, 0),
    ("P21", "O12", "Redes e Infraestructura", "presencial", 1, 0),
    ("P22", "O13", "Desarrollo de Software", "presencial", 2, 0),
    ("P23", "O14", "Analítica de Datos", "presencial", 1, 0),
    ("P24", "O15", "Desarrollo de Software", "presencial", 2, 0),
    ("P25", "O15", "Analítica de Datos", "remota", 1, 0),
    ("P26", "O16", "Soporte TI", "presencial", 1, 0),
    ("P27", "O17", "Analítica de Datos", "presencial", 1, 0),
    ("P28", "O18", "Soporte TI", "presencial", 1, 1),
    ("P29", "O19", "Desarrollo de Software", "presencial", 2, 0),
    ("P30", "O19", "Redes e Infraestructura", "presencial", 1, 0),
    ("P31", "O20", "Bases de Datos", "presencial", 1, 0),
    ("P32", "O20", "Desarrollo de Software", "remota", 1, 0),
]

# Organizaciones nuevas: sin practicantes anteriores (arranque en frío).
NEW_ORGS = {"O15", "O17"}

# Calidad oculta fijada a mano para que la demostración tenga casos claros.
PLANTED_QUALITY = {"P01": 0.85, "P13": 0.95, "P10": 0.30, "P24": 0.90}

MUNICIPALITIES = ["Sincelejo"] * 5 + ["Corozal", "Sampués", "Tolú", "Montería", "Cartagena"]

N_STUDENTS = 40
N_HISTORY = 360


@dataclass
class World:
    dataset: Dataset
    latent_quality: dict[str, float]  # placement_id -> calidad real 0..1 (oculta)


def _r(x: float) -> float:
    return round(x * 2) / 2  # escala de 0,5 en 0,5 como un instrumento de valoración


def _required(rng: random.Random, area: str) -> dict[str, float]:
    req = {area: float(rng.randint(3, 4))}
    for rel, lvl in RELATED[area].items():
        req[rel] = float(max(1, lvl + rng.choice((-1, 0, 0))))
    return req


def build_placements(rng: random.Random) -> list[Placement]:
    return [
        Placement(pid, org, PROGRAMA_SISTEMAS, area, mod, _required(rng, area), slots, taken)
        for pid, org, area, mod, slots, taken in PLACEMENT_SPECS
    ]


def random_profile(rng: random.Random) -> tuple[list[str], dict[str, float]]:
    """Preferencias y competencias coherentes: el área fuerte suele ser la preferida."""
    main = rng.choice(AREAS)
    comps: dict[str, float] = {}
    for a in AREAS:
        if a == main:
            comps[a] = _r(rng.uniform(3.5, 5.0))
        elif a in RELATED[main]:
            comps[a] = _r(rng.uniform(2.0, 4.0))
        else:
            comps[a] = _r(rng.uniform(0.5, 2.5))
    others = sorted((a for a in AREAS if a != main), key=lambda a: -comps[a] + rng.uniform(-1, 1))
    prefs = [main, *others[:2]]
    if rng.random() < 0.2:  # a veces la preferencia no coincide con la fortaleza
        prefs[0], prefs[1] = prefs[1], prefs[0]
    return prefs, comps


def generate_students(rng: random.Random, n: int, prefix: str, start: int = 1) -> list[Student]:
    org_ids = [o.id for o in ORGANIZATIONS]
    students = []
    for i in range(start, start + n):
        prefs, comps = random_profile(rng)
        works_at = rng.choice(org_ids) if rng.random() < 0.05 else None
        students.append(
            Student(
                id=f"{prefix}{i:03d}",
                name=f"Estudiante {prefix}{i:03d}",
                program=PROGRAMA_SISTEMAS,
                municipality=rng.choice(MUNICIPALITIES),
                modality_pref=rng.choices(["presencial", "cualquiera", "remota"], [50, 35, 15])[0],
                area_prefs=prefs,
                competencies=comps,
                relatives_at=[rng.choice(org_ids)] if rng.random() < 0.08 else [],
                works_at=works_at,
                job_matches_profile=works_at is not None and rng.random() < 0.5,
                vaccinated=rng.random() < 0.7,
                intl_insurance=rng.random() < 0.1,
            )
        )
    return students


def demo_students() -> list[Student]:
    """Casos construidos a mano para demostrar cada regla en la sustentación."""

    def comps(**levels: float) -> dict[str, float]:
        keys: dict[str, str] = dict(zip(("dev", "bd", "redes", "ciber", "analitica", "soporte"), AREAS, strict=True))
        return {keys[k]: v for k, v in levels.items()}

    return [
        Student("E001", "Ana Pérez", PROGRAMA_SISTEMAS, "Sincelejo", "presencial",
                ["Desarrollo de Software", "Analítica de Datos", "Bases de Datos"],
                comps(dev=4.5, bd=3.5, redes=1.5, ciber=1.0, analitica=3.0, soporte=2.0),
                relatives_at=["O01"], vaccinated=True),
        Student("E002", "Carlos Gómez", PROGRAMA_SISTEMAS, "Corozal", "presencial",
                ["Redes e Infraestructura", "Ciberseguridad", "Soporte TI"],
                comps(dev=1.5, bd=1.5, redes=4.0, ciber=3.0, analitica=1.0, soporte=3.5),
                works_at="O06", job_matches_profile=False, vaccinated=True),
        Student("E003", "Laura Díaz", PROGRAMA_SISTEMAS, "Sincelejo", "presencial",
                ["Soporte TI", "Redes e Infraestructura", "Bases de Datos"],
                comps(dev=2.0, bd=2.5, redes=3.0, ciber=1.5, analitica=1.5, soporte=4.0),
                vaccinated=False),
        Student("E004", "Miguel Torres", PROGRAMA_SISTEMAS, "Sincelejo", "cualquiera",
                ["Desarrollo de Software", "Bases de Datos", "Analítica de Datos"],
                comps(dev=5.0, bd=3.5, redes=1.0, ciber=1.5, analitica=3.0, soporte=1.5),
                vaccinated=True, intl_insurance=False),
        Student("E005", "Sofía Herrera", "Ingeniería Industrial", "Sincelejo", "presencial",
                ["Analítica de Datos", "Bases de Datos", "Desarrollo de Software"],
                comps(dev=2.0, bd=3.0, redes=1.0, ciber=1.0, analitica=4.0, soporte=1.5),
                vaccinated=True),
    ]


# ---------------------------------------------------------------------------
# Modelo del "mundo": cómo le iría realmente a un estudiante en una plaza.
# Es independiente del recomendador; el recomendador solo ve sus efectos.
# ---------------------------------------------------------------------------

def world_coverage(comps: dict[str, float], required: dict[str, float]) -> float:
    total = sum(required.values())
    return sum(min(comps.get(a, 0.0), lvl) for a, lvl in required.items()) / total


def world_area_match(prefs: list[str], area: str) -> float:
    return {0: 1.0, 1: 0.6, 2: 0.3}.get(prefs.index(area), 0.0) if area in prefs else 0.0


def world_utility(student: Student, placement: Placement, org: Organization, quality: float) -> float:
    """Desempeño esperado (0..1) sin ruido. La cobertura de competencias pesa de forma
    no lineal: una brecha grande perjudica más que proporcionalmente."""
    local = 1.0 if placement.modality == "remota" or org.municipality == student.municipality else 0.0
    cov = world_coverage(student.competencies, placement.required)
    return 0.40 * cov**1.5 + 0.30 * quality + 0.20 * world_area_match(student.area_prefs, placement.area) + 0.10 * local


def _clip(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def build_world(seed: int = SEED) -> World:
    rng = random.Random(seed)
    placements = build_placements(rng)
    orgs = {o.id: o for o in ORGANIZATIONS}
    quality = {p.id: PLANTED_QUALITY.get(p.id, round(rng.uniform(0.25, 0.9), 2)) for p in placements}

    students = demo_students() + generate_students(rng, N_STUDENTS - 5, "E", start=6)

    # Historial de semestres anteriores. Unas plazas reciben más practicantes que otras.
    with_history = [p for p in placements if p.org_id not in NEW_ORGS]
    popularity = [p.slots * rng.uniform(0.3, 1.6) for p in with_history]
    history: list[HistoryRecord] = []
    for past in generate_students(rng, N_HISTORY, "H"):
        p = rng.choices(with_history, popularity)[0]
        u = world_utility(past, p, orgs[p.org_id], quality[p.id])
        perf = 1 + 4 * _clip(u + rng.gauss(0, 0.08))
        rating = 1 + 4 * _clip(quality[p.id] + rng.gauss(0, 0.15))
        history.append(HistoryRecord(p.id, past.competencies, round(perf, 1), round(rating, 1)))

    dataset = Dataset(students, orgs, placements, history, COHORT_START)
    return World(dataset, quality)


if __name__ == "__main__":
    from pathlib import Path

    from app.db import DEFAULT_DB, save_dataset

    world = build_world()
    Path(DEFAULT_DB).parent.mkdir(parents=True, exist_ok=True)
    save_dataset(world.dataset, DEFAULT_DB)
    ds = world.dataset
    print(f"Base creada en {DEFAULT_DB}: {len(ds.students)} estudiantes, "
          f"{len(ds.organizations)} organizaciones, {len(ds.placements)} plazas, {len(ds.history)} registros históricos")
