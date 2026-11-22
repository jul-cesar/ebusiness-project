# Recomendador de escenarios de práctica

Prototipo académico de la Ruta A. Trabaja con datos ficticios. La Coordinación conserva la decisión de asignación.

## Ejecución local

Con `uv`, desde este directorio:

```sh
uv sync --locked
uv run --locked uvicorn app.main:app --port 8765
```

Abre http://127.0.0.1:8765. Para ver el contrato de la API, abre `/docs`. En el primer arranque se genera la base SQLite local a partir de una semilla fija.

## Demostración

- Ana Pérez: abre «Plazas excluidas» y busca la regla de parentesco.
- Modifica un peso o la modalidad preferida para explorar cómo cambia la recomendación. Los cambios no se guardan.
- En «Cohorte», compara la asignación húngara con la voraz. Ninguna confirma una asignación real.
- En «Evaluación», compara los métodos con datos simulados; los resultados no estiman el impacto en CECAR.

## Reproducción

```sh
uv run --locked pytest -q
uv run --locked python -m app.evaluation
```

La evaluación escribe `evidencias/resultados_evaluacion.json`.
