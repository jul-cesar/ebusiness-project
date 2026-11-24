# Evaluación y selección tecnológica

El prototipo debe ordenar plazas elegibles, explicar cada puntaje y funcionar localmente con datos ficticios. La comparación evalúa ese alcance, no una implantación institucional.

## Criterios de decisión

1. **Ajuste al problema:** el componente debe resolver una necesidad del flujo. Las reglas de elegibilidad no se compensan con el puntaje.
2. **Explicabilidad:** Coordinación debe poder reconstruir por qué una plaza se excluye o queda arriba.
3. **Reproducción y operación:** el equipo debe poder ejecutar y demostrar el prototipo localmente, sin servicios externos.
4. **Costo de cambio:** se prefiere una herramienta más compleja solo si aporta una capacidad que el prototipo necesita.

Los dos primeros criterios determinan si una alternativa es apta. Los últimos permiten elegir entre las alternativas aptas. No se hicieron pruebas de rendimiento entre herramientas no implementadas.

| Componente | Alternativas | Selección, evidencia y límite |
|---|---|---|
| Motor de ranking | Contenido (perfil y plaza) frente a híbrido (contenido e historial) | **Híbrido**, después del mismo filtro de reglas. En la simulación obtuvo NDCG@5 de 0,9804 frente a 0,9596 con solo contenido. Sin historial autorizado o de calidad suficiente, el método basado en contenido es una alternativa defendible. |
| Explicación | Mostrar coincidencias de área y competencias frente a mostrar aportes de todos los factores | **Aportes por factor**. No basta mostrar dos coincidencias si el historial y la logística también influyen. La prueba de puntaje verifica que la suma de aportes reproduce el valor calculado por el motor. La pantalla redondea los valores. |
| API web | FastAPI frente a Flask | **FastAPI**. El prototipo usa modelos para validar solicitudes y genera documentación OpenAPI en `/docs`. Flask permite implementar la misma API, pero ese esquema y la documentación requieren configuración o herramientas adicionales. No se comparó rendimiento. |
| Interfaz | HTML, CSS y JavaScript nativos frente a React con Vite | **React con Vite**. La versión nativa evitaba compilar, pero la interfaz rediseñada separa la elección del perfil, el ranking explicado y las exclusiones. React organiza el estado de los formularios y las vistas. Vite añade un paso de compilación. FastAPI sirve los archivos compilados, así que la demostración usa un solo servidor. El motor no cambió. |
| Datos | SQLite frente a PostgreSQL | **SQLite**. Conserva el catálogo y el historial ficticio en un archivo local, sin administrar otro servidor. PostgreSQL tendría sentido con varios usuarios escribiendo y requisitos institucionales de acceso y operación. Ese escenario no se ensayó. |
| Propuesta de cohorte | Asignación lineal con SciPy frente a algoritmo voraz | **SciPy**. La asignación considera todas las parejas elegibles y los cupos en conjunto. La prueba compara primero el número de estudiantes asignados y luego el puntaje total. El método voraz queda como referencia porque es fácil de entender, pero una elección temprana puede bloquear otra asignación. |

## Fuentes y trazabilidad

- Ranking y comparación sin historial: `app/scoring.py`, `app/evaluation.py` y `evidencias/resultados_evaluacion.json`.
- Puntaje y asignación: `tests/test_recommendation.py` y `evidencias/validacion.md`.
- Capacidades de las herramientas: [FastAPI](https://fastapi.tiangolo.com/features/), [Flask](https://flask.palletsprojects.com/en/stable/quickstart/), [React](https://react.dev/learn/installation), [SQLite](https://sqlite.org/whentouse.html), [PostgreSQL](https://www.postgresql.org/docs/current/tutorial-arch.html) y [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html).

Un catálogo filtrado ayuda a encontrar opciones permitidas, pero no prioriza una plaza para cada perfil. El valor de la Ruta A es ese orden personalizado y explicable. No depende de que se use aprendizaje automático ni de que la interfaz sea compleja.
