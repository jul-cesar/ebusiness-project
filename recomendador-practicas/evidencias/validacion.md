# Pruebas y validación del prototipo

La validación separa el funcionamiento del prototipo de la calidad del orden recomendado. Se usaron datos ficticios reproducibles. Las pruebas no consultaron datos de CECAR.

## Pruebas funcionales

Desde `recomendador-practicas`, ejecutar `uv run --locked pytest -q --tb=short`. La ejecución obtuvo **14 pruebas aprobadas**. Las funciones identificadas en la tabla están en `tests/test_recommendation.py`.

| Objetivo | Datos y procedimiento | Resultado esperado | Resultado obtenido y evidencia | Conclusión |
|---|---|---|---|---|
| Aplicar las restricciones | Solicitar el ranking de los perfiles ficticios E001–E004. Buscar las plazas con parentesco, convenio vencido, cupo agotado, falta de vacunación, falta de seguro o empleo no afín. | Cada plaza queda fuera del ranking y muestra la regla incumplida. | Coincidió en los seis casos de `test_exclusion_visible`. | El filtro excluye y explica los incumplimientos ensayados. |
| Recalcular la elegibilidad | Marcar la vacunación como acreditada para E003 y volver a recomendar. | P05 pasa al conjunto elegible. | P05 entró al ranking en `test_health_requirement_changes_eligibility`. | El resultado depende del dato del perfil. |
| Reordenar al cambiar prioridades | Comparar el ranking de E001 con los pesos iniciales y con todo el peso en logística. | Cambia el orden y una plaza local de modalidad preferida queda primera. | Se observó el cambio en `test_logistics_can_reorder_results`. | Los pesos modifican el ranking, no solo cómo se muestra. |
| Explicar el puntaje | Puntuar para E001 con pesos 3 en área y 2 en competencias. | Los pesos efectivos son 60 % y 40 %. La suma de aportes coincide con el puntaje. | Ambas comprobaciones pasaron en `test_weights_are_normalized_and_explain_score`. | El puntaje se puede reconstruir a partir de los aportes. |
| Manejar una plaza nueva | Revisar P24, sin historial, en el ranking de E001. | Calidad y desempeño de perfiles similares usan sus respectivos promedios generales. | Ambos valores coincidieron en `test_new_placement_uses_prior`. | La falta de historial no convierte el puntaje histórico en cero. |
| Respetar cupos y elegibilidad en la cohorte | Ejecutar la asignación húngara y la voraz sobre la cohorte ficticia. | La solución húngara no duplica estudiantes ni supera cupos. No usa pares inelegibles ni resulta peor al comparar primero el número asignado y después el puntaje total. | Las comprobaciones pasaron en `test_cohort_respects_capacity_and_eligibility`. | La propuesta respeta las restricciones probadas y el objetivo de comparación. |
| Gestionar la ausencia de plazas y repetir resultados | Pedir un ranking para E005, de otro programa. Regenerar los datos y repetir el ranking para E001. | E005 recibe un mensaje sin recomendaciones. E001 recibe la misma salida al repetir los datos y parámetros. | Coincidió en `test_no_eligible_placement` y `test_repeatable_ranking`. | El resultado vacío es explícito y la demo se puede reproducir. |

## Evaluación del ranking

**Objetivo:** comprobar si el método híbrido ordena mejor las plazas elegibles que las alternativas dentro de la simulación. **Datos:** 200 perfiles ficticios de prueba, separados del historial usado por el motor. El generador define un orden ideal a partir de su propia función de utilidad.

**Procedimiento:** ejecutar `uv run --locked python -m app.evaluation`. Para cada perfil, comparar las cinco primeras recomendaciones con el orden ideal. NDCG@5 considera la utilidad y la posición. Precision@5 mide la proporción de recomendaciones que coinciden con las cinco mejores plazas simuladas.

**Esperado:** el híbrido supera a los métodos basados en popularidad y azar en las dos métricas. **Obtenido:** los resultados archivados en `resultados_evaluacion.json` fueron:

| Método | NDCG@5 | Precision@5 |
|---|---:|---:|
| Híbrido | 0,9804 | 76,9 % |
| Solo contenido | 0,9596 | 70,9 % |
| Popularidad | 0,6865 | 21,3 % |
| Aleatorio | 0,6544 | 18,17 % |

**Conclusión:** el método híbrido superó las dos referencias y también obtuvo mejores resultados que el método sin historial en esta simulación. En el análisis de concentración, el quinto más popular recibió el 21,54 % de las recomendaciones híbridas frente al 98,46 % del método por popularidad. Esto describe la distribución de la muestra, no demuestra ausencia de sesgo.

## Límites de la evidencia

El generador define las relaciones entre perfil y desempeño. Por eso el orden ideal es un resultado del modelo simulado, no una observación de prácticas reales. Tampoco se midió si el prototipo reduce tiempos, errores de asignación o retiros. Para valorar su utilidad institucional, se necesita contrastar reglas y recomendaciones con Coordinación y usar datos autorizados.
