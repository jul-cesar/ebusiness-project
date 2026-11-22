"""Persistencia en SQLite. Las estructuras por área (competencias, requisitos)
se guardan como JSON para mantener el esquema pequeño y legible."""

from __future__ import annotations

import json
import os
import sqlite3
from datetime import date
from pathlib import Path

from app.models import Dataset, HistoryRecord, Organization, Placement, Student

DEFAULT_DB = os.environ.get("PRACTICAS_DB", str(Path(__file__).resolve().parent.parent / "data" / "practicas.db"))

SCHEMA = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE organizations (
    id TEXT PRIMARY KEY, name TEXT NOT NULL, sector TEXT NOT NULL,
    municipality TEXT NOT NULL, country TEXT NOT NULL, agreement_until TEXT NOT NULL
);
CREATE TABLE placements (
    id TEXT PRIMARY KEY, org_id TEXT NOT NULL REFERENCES organizations(id),
    program TEXT NOT NULL, area TEXT NOT NULL, modality TEXT NOT NULL,
    required_json TEXT NOT NULL, slots INTEGER NOT NULL CHECK (slots > 0),
    slots_taken INTEGER NOT NULL CHECK (slots_taken >= 0)
);
CREATE TABLE students (
    id TEXT PRIMARY KEY, name TEXT NOT NULL, program TEXT NOT NULL, municipality TEXT NOT NULL,
    modality_pref TEXT NOT NULL, area_prefs_json TEXT NOT NULL, competencies_json TEXT NOT NULL,
    relatives_at_json TEXT NOT NULL, works_at TEXT, job_matches_profile INTEGER NOT NULL,
    vaccinated INTEGER NOT NULL, intl_insurance INTEGER NOT NULL
);
CREATE TABLE history (
    id INTEGER PRIMARY KEY AUTOINCREMENT, placement_id TEXT NOT NULL REFERENCES placements(id),
    competencies_json TEXT NOT NULL,
    performance REAL NOT NULL CHECK (performance BETWEEN 1 AND 5),
    rating REAL NOT NULL CHECK (rating BETWEEN 1 AND 5)
);
"""


def save_dataset(ds: Dataset, path: str) -> None:
    if os.path.exists(path):
        os.remove(path)
    with sqlite3.connect(path) as con:
        con.executescript(SCHEMA)
        con.execute("INSERT INTO meta VALUES ('cohort_start', ?)", (ds.cohort_start.isoformat(),))
        con.executemany(
            "INSERT INTO organizations VALUES (?,?,?,?,?,?)",
            [(o.id, o.name, o.sector, o.municipality, o.country, o.agreement_until.isoformat())
             for o in ds.organizations.values()],
        )
        con.executemany(
            "INSERT INTO placements VALUES (?,?,?,?,?,?,?,?)",
            [(p.id, p.org_id, p.program, p.area, p.modality, json.dumps(p.required, ensure_ascii=False),
              p.slots, p.slots_taken) for p in ds.placements],
        )
        con.executemany(
            "INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            [(s.id, s.name, s.program, s.municipality, s.modality_pref,
              json.dumps(s.area_prefs, ensure_ascii=False), json.dumps(s.competencies, ensure_ascii=False),
              json.dumps(s.relatives_at), s.works_at, int(s.job_matches_profile), int(s.vaccinated),
              int(s.intl_insurance)) for s in ds.students],
        )
        con.executemany(
            "INSERT INTO history (placement_id, competencies_json, performance, rating) VALUES (?,?,?,?)",
            [(h.placement_id, json.dumps(h.competencies, ensure_ascii=False), h.performance, h.rating)
             for h in ds.history],
        )


def load_dataset(path: str) -> Dataset:
    with sqlite3.connect(path) as con:
        cohort_start = date.fromisoformat(con.execute("SELECT value FROM meta WHERE key='cohort_start'").fetchone()[0])
        orgs = {
            r[0]: Organization(r[0], r[1], r[2], r[3], r[4], date.fromisoformat(r[5]))
            for r in con.execute("SELECT * FROM organizations ORDER BY id")
        }
        placements = [
            Placement(r[0], r[1], r[2], r[3], r[4], json.loads(r[5]), r[6], r[7])
            for r in con.execute("SELECT * FROM placements ORDER BY id")
        ]
        students = [
            Student(r[0], r[1], r[2], r[3], r[4], json.loads(r[5]), json.loads(r[6]), json.loads(r[7]),
                    r[8], bool(r[9]), bool(r[10]), bool(r[11]))
            for r in con.execute("SELECT * FROM students ORDER BY id")
        ]
        history = [
            HistoryRecord(r[0], json.loads(r[1]), r[2], r[3])
            for r in con.execute("SELECT placement_id, competencies_json, performance, rating FROM history ORDER BY id")
        ]
    return Dataset(students, orgs, placements, history, cohort_start)
