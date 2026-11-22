# Propuesta de transformación digital para la gestión de prácticas profesionales de CECAR

*E-business   |   Ingeniería de Sistemas*\
*Desarrollo de los entregables 1 a 18   |   Septiembre de 2026*

## Participantes

Eduardo Rafael de Avila Florez\
Julio Cesar Martinez\
Alex Betin Uparela

## Propósito y resultado del análisis

La gestión de una práctica profesional comienza antes de que el estudiante llegue a la organización y continúa hasta la evaluación de sus resultados. Durante ese recorrido se verifican requisitos, se acuerdan actividades y se revisan evidencias. Este trabajo examina cómo se relacionan esas tareas en CECAR y qué oportunidades de transformación digital pueden mejorar su coordinación.

La prioridad propuesta es poder reconstruir el recorrido de cada práctica a partir de sus documentos, responsables y decisiones. También se recomienda aclarar las reglas para el control de horas y coordinar la revisión de requisitos. Estas mejoras darían una base más confiable al seguimiento del estudiante y a los informes del programa, manteniendo la confidencialidad de las novedades.

## Alcance académico

El informe desarrolla los 18 entregables de la guía: diagnóstico, rediseño del proceso, requisitos, arquitectura, datos, evaluación de tecnologías, prueba de concepto, prototipos, indicadores y análisis de viabilidad. La propuesta se acompaña de una demostración local; no constituye un sistema implantado en CECAR \[P, pp. 5–6].

## Método y tratamiento de la evidencia

Se realiza un análisis documental de los lineamientos de 2026 \[L] y de la guía del proyecto \[P]. El AS-IS representa el procedimiento establecido en los lineamientos; su secuencia se organiza para facilitar el análisis. No equivale a una observación directa de la operación. Las responsabilidades de validación y las transiciones no expresas se identifican como interpretaciones analíticas.

Las afirmaciones respaldadas por los lineamientos se acompañan de su referencia. Cuando se plantea una posible dificultad de la operación, se indica qué evidencia permitiría comprobarla. Las prioridades y metas son propuestas de diseño. La prueba de concepto usa datos ficticios y sus resultados se distinguen de las validaciones institucionales pendientes.

## Guía de lectura

Apartados 1–6: diagnóstico y prioridades. 7–12: proceso futuro, requisitos, arquitectura, datos y tecnologías. 13–16: validación técnica, prototipos e indicadores. 17–18: riesgos y viabilidad. Al final se incluyen referencias y una guía para la sustentación.

# 1 Caracterización del proceso

## 1 1 Objetivo y delimitación

El proceso tiene como objetivo vincular al estudiante con un escenario pertinente, acompañar su formación, verificar el desarrollo de las actividades y valorar los resultados obtenidos. Su gestión debe producir evidencias suficientes para la evaluación académica y el mejoramiento de las prácticas \[L, pp. 2, 5–7].

La unidad de análisis es la trayectoria de una práctica de un estudiante durante un semestre, conectada con la gestión del programa y la facultad. El inicio se sitúa en la formalización del curso y la incorporación; el cierre, en la entrega y consolidación de informes. La preparación de escenarios y alianzas se incluye como proceso relacionado, pues condiciona la asignación \[L, pp. 9, 13, 19–20].

Se mantiene una visión institucional. Las particularidades de cada programa, modalidad y escenario deben parametrizarse o verificarse posteriormente; no se presume una cantidad universal de horas ni se restringe el análisis a una sola modalidad \[L, pp. 14–17].

## 1 2 Ficha de caracterización

| **Elemento** | **Descripción** |
| --- | --- |
| Proceso | Gestión académica y administrativa de prácticas profesionales. |
| Propietario operativo | Coordinación de Prácticas del programa como articulador de la gestión. Es una denominación analítica basada en sus funciones, no un cargo nuevo \[L, p. 9]. |
| Dirección y supervisión | Coordinación Académica, Decanatura y Vicerrectoría Académica, según sus competencias \[L, pp. 6–9]. |
| Proveedores | Estudiantes; programa académico; organizaciones receptoras; asesores; supervisores; dependencias de alianzas y convenios. |
| Entradas | Matrícula y prerrequisitos; inscripción; soportes de preparación; información del escenario; alianza o carta de intención; agenda y criterios de evaluación. |
| Transformación | Verificar condiciones; asignar; formalizar; planificar; acompañar; registrar actividades; evaluar; consolidar resultados. |
| Salidas | Vinculación formalizada; agenda; registros de asistencia y seguimiento; informes de avance y final; evaluaciones; informe de gestión y acciones de mejora. |
| Destinatarios | Estudiante; asesor; supervisor; coordinaciones; Decanatura; instancias que analizan resultados y deciden mejoras. |
| Recursos | Tiempo de los actores, formatos institucionales, medios de comunicación, soportes físicos o digitales y plataformas que deben inventariarse. |
| Límites | Incluye diseño, prototipo y prueba local; no abarca una implantación institucional ni sustituye reglamentos o decisiones académicas. |

## 1 3 Relación con e-business

El caso permite estudiar cómo las tecnologías digitales pueden mejorar un proceso organizacional y sus intercambios con actores externos. Su valor se expresa en coordinación, trazabilidad y decisiones oportunas; la mejora debe justificarse desde el proceso y sus necesidades \[P, pp. 1–3].

# 1 Caracterización de fases y reglas

## 1 4 Fases y resultados esperados del proceso vigente

| **Fase** | **Actividades principales** | **Resultado institucional** |
| --- | --- | --- |
| Incorporación | Revisar requisitos, recibir inscripción, preparar al estudiante, asignar escenario y asesor, formalizar vinculación y acordar agenda. | Estudiante vinculado con responsables, condiciones y compromisos identificados \[L, pp. 9–13, 18–20]. |
| Acompañamiento | Orientar el plan de trabajo, brindar asesorías, realizar visitas, registrar asistencia y avances, gestionar novedades. | Seguimiento del estudiante y evidencias del desarrollo de la práctica \[L, pp. 10–13, 17]. |
| Seguimiento y evaluación | Revisar informes por corte, evaluar desempeño, socializar el producto final, evaluar actores y consolidar gestión. | Valoración académica e información para mejoramiento \[L, pp. 20–23]. |

## 1 5 Reglas que condicionan el análisis

| **ID** | **Regla documental** | **Implicación para la gestión** |
| --- | --- | --- |
| R1 | Matrícula, prerrequisitos y condiciones académicas y de conducta \[L, pp. 12, 19]. | Verificar condiciones antes de la incorporación y conservar el soporte de la decisión. |
| R2 | Certificado MOOC de habilidades blandas; actividades preparatorias e inducción; acta de compromiso \[L, pp. 12, 19]. | Relacionar cada requisito con evidencia y responsable de revisión. |
| R3 | Formalización mediante alianza o carta de intención; revisión semestral de escenarios y convenios \[L, pp. 18–20]. | Vincular al estudiante con un escenario y un instrumento de formalización identificables. |
| R4 | Horas según créditos y programa; incluyen sitio de práctica, asesorías y formación \[L, p. 17]. | Distinguir tipos de horas y condiciones específicas del programa. |
| R5 | Cambios de itinerario requieren aprobación escrita del asesor \[L, p. 13]. | Conservar versión de agenda, solicitud y autorización. |
| R6 | Informes de avance y final por corte, con soportes y visto bueno del supervisor \[L, p. 21]. | Rastrear entrega, revisión y respaldo de cada informe. |
| R7 | Primer corte 40 % y segundo 60 %; reglas de asistencia y cumplimiento de horas \[L, p. 22]. | Preservar la ponderación y aclarar el alcance de cada umbral antes de automatizarlo. |
| R8 | Novedades de retiro por conducto formal y ruta específica para acoso \[L, pp. 18–19, 24–25]. | Mantener intervención institucional y acceso restringido a los casos que lo requieran. |

## 1 6 Datos y documentos fundamentales

La inscripción genera datos del estudiante; la asignación relaciona programa, escenario, asesor y supervisor. La agenda y sus cambios originan compromisos. La asistencia, las asesorías y los productos originan evidencias. Los informes y evaluaciones consolidan el desempeño; las coordinaciones agregan resultados para gestión \[L, pp. 5, 9–12, 19–23].

Conviene distinguir un documento de los datos que contiene: un informe puede incluir horas, fechas, actividades y aprobaciones. Su existencia no garantiza que esos datos sean comparables o reutilizables entre programas. Esa capacidad requiere validación.

# 2 Actores y responsabilidades

Los lineamientos distribuyen la gestión entre la universidad, el estudiante y la organización receptora. El asesor orienta el proceso desde la academia; el supervisor acompaña y observa el trabajo en el escenario. La tabla recoge sus funciones y los intercambios de información que exige cada responsabilidad.

| **Actor** | **Responsabilidades principales** | **Información que entrega o utiliza** |
| --- | --- | --- |
| Estudiante | Cumplir requisitos y compromisos; participar en inducción y asesorías; desarrollar actividades; entregar productos e informes; utilizar el conducto regular. | Inscripción y certificados; agenda; evidencias; informes; evaluaciones de acompañamiento \[L, pp. 12–13, 19, 21–23]. |
| Coordinación de Prácticas del programa | Organizar selección y asignación; gestionar alianzas; planificar la agenda; actualizar protocolos; seguir actividades y consolidar informes. | Listado de estudiantes y escenarios; protocolos; seguimiento; informe por corte y de gestión \[L, p. 9]. |
| Asesor o tutor | Orientar y acompañar; realizar visitas de inicio y cierre; revisar asistencia con el supervisor; registrar seguimiento y evaluar por corte. | Agenda, registro de seguimiento, informes y conceptos de evaluación \[L, pp. 10, 13, 21]. |
| Supervisor del escenario | Inducir en el lugar; orientar el plan; controlar asistencia y actividades; evaluar desempeño; coordinar con el asesor y gestionar certificación. | Control de asistencia; observaciones; evaluación; visto bueno de informes \[L, pp. 11, 21]. |
| Coordinación Académica | Articular la práctica con el currículo; analizar resultados; acompañar la solución de situaciones académicas y el mejoramiento. | Resultados de evaluación e información para comités y mejora curricular \[L, pp. 8–9]. |
| Decanatura | Avalar alianzas; planear y seguir las prácticas de la facultad; consolidar resultados y orientar planes de mejora. | Informes de programas; avales; informes estadísticos y de impacto \[L, pp. 5, 7–8]. |
| Vicerrectoría Académica | Establecer lineamientos y articular procesos institucionales; contribuir al análisis de mejoras con las decanaturas. | Lineamientos y análisis institucional \[L, pp. 6–7]. |
| Organización receptora y oficina de Convenios y Alianzas | La organización aporta condiciones y soportes de formalización. La oficina recibe la documentación remitida por las coordinaciones. | Carta de intención, documentos de la organización y expediente del convenio \[L, pp. 3, 18–20]. |

## Participación de otras instancias

Los comités y consejos intervienen en el seguimiento y la toma de decisiones según el asunto. La ruta de acoso involucra además a Proyección Social y Prácticas, CAPS y otras instancias competentes \[L, pp. 6–7, 23, 25]. No todos estos actores necesitan consultar todos los datos de un estudiante.

# 2 Matriz de responsabilidades

La matriz RACI sintetiza la participación: R ejecuta; A responde por el cierre de la actividad; C es consultado; I recibe información. CP: Coordinación de Prácticas; AS: asesor; SU: supervisor; CA: Coordinación Académica; DE: Decanatura; ES: estudiante. R/A combina ejecución y responsabilidad de cierre.

Es una interpretación para organizar el análisis, no una delegación institucional. Los asteriscos señalan asignaciones de cierre que deben confirmarse, pues el documento describe funciones sin definir formalmente una matriz RACI.

| **Actividad** | **ES** | **CP** | **AS** | **SU** | **CA** | **DE** |
| --- | --- | --- | --- | --- | --- | --- |
| Verificar expediente de incorporación | R | A* | C | — | C | I |
| Seleccionar y asignar escenario | C | R/A | C | C | C | I |
| Gestionar formalización y aval | C | R | C | C | C | A |
| Organizar inducción y compromiso | R | R | C | — | C | A* |
| Acordar agenda y plan de trabajo | R | I | A* | C | — | — |
| Autorizar cambios de itinerario | R | I | R/A | C | — | — |
| Registrar y controlar asistencia en sitio | R | I | C | R/A | — | — |
| Realizar seguimiento académico | C | A* | R | C | I | — |
| Presentar informe y obtener visto bueno | R | I | C | A* | — | — |
| Valorar desempeño académico por corte | C | C | R/A* | R | I | — |
| Recibir evaluación de acompañamiento | R | R/A* | C | C | I | — |
| Consolidar informe del programa | — | R | C | C | A* | I |
| Consolidar resultados de facultad | — | C | — | — | C | R/A |
| Analizar mejoras académicas | — | R | C | C | R | A* |

## Criterios de interpretación

La Coordinación de Prácticas articula la incorporación por sus funciones de organización y asignación \[L, p. 9]. La Decanatura otorga el aval para formalizar alianzas \[L, p. 7]. El asesor autoriza cambios de itinerario por escrito \[L, p. 13]. El supervisor ejerce control de asistencia y emite el visto bueno de los informes \[L, pp. 11, 21].

La responsabilidad académica del asesor no elimina la autoevaluación, coevaluación y heteroevaluación ni las reglas del comité del programa. La Coordinación Académica avala el informe de gestión conforme a la definición institucional; esta relación se debe confirmar en el flujo operativo de cada programa \[L, pp. 5, 22–23].

## Intercambios que requieren especial atención

Estudiante–Coordinación: requisitos y asignación. Estudiante–Supervisor–Asesor: agenda, horas, evidencias e informes. Asesor–Coordinación: seguimiento y novedades. Coordinación–Facultad: resultados agregados. Estos puntos de intercambio orientan el diagnóstico de trazabilidad y consistencia de la información.

# 3 Modelo AS IS del proceso institucional

Figura 1. Flujo general por responsable principal. Las flechas muestran la secuencia analítica y el traspaso de información; no implican que las actividades solo puedan ejecutarse una vez. A3 depende de la disponibilidad de un escenario y del aval correspondiente. A4 puede coordinarse en paralelo con A3.

Proceso AS-IS por cinco carriles con actividades A1 a A13, desde inscripción hasta análisis de resultados. Las fichas del apartado 3 describen cada actividad y sus decisiones.

Fuente: elaboración a partir de \[L, pp. 9–13, 18–23]. Modelo funcional por carriles, no diagrama BPMN formal. Los demás participantes se detallan en las fichas A1–A13 y en la matriz de responsabilidades. El retorno por requisitos incompletos y la organización temporal son interpretaciones que deben validarse.

# 3 Descripción del AS IS de incorporación

Las fichas hacen explícito quién actúa, qué información utiliza, qué produce y cuál es el destino de esa información. No se asigna un canal digital específico cuando los lineamientos no lo determinan.

| **Paso y responsable** | **Entrada y actividad** | **Salida y decisión o intercambio** |
| --- | --- | --- |
| A1 Estudiante | Reúne información de inscripción y soportes de preparación, matrícula y prerrequisitos. | Entrega a CP la inscripción y certificados requeridos. Fuente: \[L, pp. 12, 19]. |
| A2 CP con apoyo académico | Contrasta condiciones de ingreso con las reglas del programa. La función de revisión se infiere de su papel de organización. | Decisión: ¿se acreditan requisitos? Si faltan soportes, se propone representar una subsanación hacia A1. Responsable exacto y tratamiento de excepciones por confirmar \[L, pp. 9, 19]. |
| A3 CP y Decanatura | Utilizan datos del estudiante, escenarios y documentos de alianzas. CP organiza la asignación; la Decanatura avala la formalización. | Estudiante asociado a escenario y responsables. La documentación empresarial se remite a Convenios y Alianzas y a instancias académicas. Si no hay escenario apto, se requiere nueva gestión, transición analítica \[L, pp. 7, 9, 18–20]. |
| A4 Facultad, CP y estudiante | Se realizan espacios de inducción durante las primeras dos semanas; CP suministra el acta de compromiso. | Estudiante informado y acta firmada. Se vincula a grupo y asesor. La secuencia exacta de asignación e inducción debe confirmarse \[L, pp. 19–20]. |
| A5 Estudiante, asesor y supervisor | El plan se construye con las necesidades del escenario. El asesor oficializa horarios en la visita de incorporación; el supervisor orienta el plan. | Agenda y cronograma acordados, comunicados al escenario y usados para seguimiento. Los cambios de itinerario requieren aprobación escrita del asesor \[L, pp. 11, 13, 17]. |

## Controles y fronteras de esta fase

La incorporación conecta dos verificaciones: que el estudiante reúna las condiciones y que el escenario sea pertinente y esté formalizado. El diagrama no autoriza iniciar la práctica sin estas condiciones. La intensidad, los productos y particularidades dependen del programa \[L, pp. 15, 18–20].

Los datos de matrícula y antecedentes académicos no se suponen obtenidos automáticamente. Es necesario identificar qué dependencia los certifica, qué evidencia se acepta y cómo se comunica el resultado de la revisión. Esta precisión es parte de la validación del AS-IS.

# 3 Descripción del AS IS de seguimiento y cierre

| **Paso y responsable** | **Información y actividad** | **Salida y destinatario** |
| --- | --- | --- |
| A6 Supervisor y estudiante | Agenda y actividades realizadas. Se controla asistencia y cumplimiento; el asesor revisa el registro con el supervisor. | Registro de asistencia y observaciones para estudiante y asesor \[L, pp. 10–11]. |
| A7 Asesor | Avances, evidencias y necesidades del estudiante. Desarrolla asesorías, visitas y retroalimentación; registra seguimiento. | Registro actualizado y orientaciones para el estudiante; comunicación con supervisor y CP \[L, pp. 10–11]. |
| A8 Estudiante | Al primer corte prepara informe de avance; al segundo, informe final. Adjunta asistencia consolidada y soportes definidos por el programa. | Informe dirigido al asesor, con visto bueno del supervisor \[L, p. 21]. |
| A9 Supervisor | Revisa informe y soportes del practicante; emite visto bueno y concepto de desempeño. | Informe respaldado y evaluación para el asesor. Si hay observaciones, su corrección y nueva revisión son un retorno analítico por validar \[L, pp. 11, 21]. |
| A10 Asesor y participantes de evaluación | Integra informes, evidencias y concepto del supervisor con autoevaluación, coevaluación y heteroevaluación. | Resultado por corte según reglas del programa. Primer corte 40 %; segundo 60 %. La socialización final debe considerarse en el cierre académico \[L, pp. 10, 21–22]. |
| A11 Estudiante y programa | Socializa producto final. El estudiante evalúa el acompañamiento de asesor y supervisor; los asesores evalúan al coordinador. | Resultados y retroalimentación a las instancias responsables de consolidarlos \[L, pp. 22–23]. |
| A12 CP | Recoge resultados y evidencias del semestre; elabora informe de avance y gestión. | Informe del programa, con aval académico y presentación ante las instancias correspondientes \[L, pp. 5, 9, 23]. |
| A13 Coordinación Académica y Facultad | Analizan informes, desempeño y resultados del seguimiento. | Consolidación de facultad y acciones de mejoramiento; resultados para espacios institucionales \[L, pp. 5–9]. |

## Excepciones que el modelo debe conservar

Cambio de itinerario: aprobación escrita del asesor \[L, p. 13]. Retiro o cambio de escenario: notificación formal, verificación y conducto institucional \[L, pp. 18–19]. Acoso: reporte al asesor, remisión a CP e instancias académicas y de apoyo según la ruta específica \[L, p. 25]. No se reduce esta ruta a un trámite genérico ni se presupone que todos puedan consultar su contenido.

El seguimiento es continuo. Las fechas de corte, entregas y espacios de socialización dependen del calendario y reglamento del programa. Las observaciones a informes, las incidencias y las evidencias incompletas deben validarse como ramificaciones operativas del modelo.

# 4 Identificación y análisis de problemas

La guía exige descubrir y sustentar problemas, sin partir de una lista prefijada \[P, p. 2]. Aquí se distinguen limitaciones de especificación documental e hipótesis de operación. La falta de un detalle en los lineamientos no demuestra que falte en las herramientas o procedimientos complementarios de CECAR.

## P1 Verificación de incorporación con evidencia distribuida

La incorporación exige matrícula y prerrequisitos, certificado MOOC, preparación, inscripción e inducción. CP organiza selección y asignación \[L, pp. 9, 12, 19].

Hipótesis. La consulta de evidencias provenientes de distintas actividades puede dificultar conocer si un expediente está completo y quién debe resolver un pendiente. Causa posible: criterios de revisión o estados no compartidos entre responsables; no está confirmada la existencia de esta dificultad.

Consecuencia potencial. Revisión repetida, incorporación pendiente o asignación sin visibilidad suficiente de soportes. Afecta al estudiante, CP y apoyo académico. Validación: reconstruir expedientes reales anonimizados y contrastar documentos exigidos, decisiones, responsables y tiempos de revisión. No se dispone de una tasa de expedientes incompletos.

## P2 Trazabilidad no especificada de documentos y aprobaciones

Existen agenda, asistencia, seguimiento, informes con visto bueno, formatos y protocolos que deben mantenerse actualizados en una plataforma \[L, pp. 9–10, 13, 17, 21]. Por tanto, no es válido afirmar que toda la gestión es manual o que no existen herramientas digitales.

Limitación documental e hipótesis. Los lineamientos no describen cómo se enlazan versiones, registros y aprobaciones de cada práctica ni quién consulta su historial completo. La hipótesis es que podría existir dificultad para reconstruirlo si los soportes se administran sin referencias comunes.

Consecuencia potencial. Revisión de una versión desactualizada, dificultad para ubicar un visto bueno o esfuerzo para reconstruir la secuencia de decisiones. Validación: inventariar plataformas y seguir un informe desde su creación hasta su aprobación y consolidación. Examinar identificación, versión, fecha, autor y acceso.

## P3 Alcance de los controles de horas y asistencia por aclarar

Las horas incluyen sitio, asesorías y formación \[L, p. 17]. El texto contempla inasistencia superior al 25 %, cumplimiento mínimo del 80 % de horas en el sitio y ausencias injustificadas del 25 % como falta \[L, pp. 13, 22, 24].

Limitación documental. No se explica en un solo criterio cómo se relacionan esos umbrales, sus denominadores y consecuencias. No son necesariamente contradictorios: pueden referirse a controles diferentes. Sin esa aclaración, convertirlos en una regla automática única sería una decisión no sustentada.

Consecuencia potencial. Cálculos no comparables o alertas improcedentes. Afecta a estudiantes, asesores y supervisores. Validación: solicitar interpretación académica, ejemplos de cálculo, tipos de horas y tratamiento de ausencias justificadas; contrastar el reglamento del programa.

# 4 Análisis de seguimiento e información

## P4 Consolidación de resultados con definiciones por armonizar

CP presenta informes por corte y de gestión; las facultades consolidan información y la utilizan para mejorar. Se mencionan formatos de informe y evaluaciones de varios actores \[L, pp. 5, 7–9, 23].

Limitación documental e hipótesis. El texto no detalla un diccionario común de datos ni el enlace entre asistencia, productos, evaluaciones y reportes de gestión. Debe comprobarse si los formatos y sistemas complementarios ya lo resuelven. La causa hipotética de dificultades sería la agregación de registros con definiciones o identificadores distintos.

Consecuencia potencial. Comparaciones poco consistentes o trabajo adicional para consolidar cifras. No se afirma que los informes existentes sean incorrectos. Validación: comparar un formato de informe de programa con sus registros fuente y con el consolidado de facultad; comprobar cada total y definición.

## P5 Visibilidad de compromisos y pendientes por verificar

Se exige seguimiento permanente; existen agenda, visitas, asesorías, evaluaciones por corte y reuniones institucionales de seguimiento \[L, pp. 6–7, 9–11, 17].

Hipótesis. Si compromisos, vencimientos y responsables se consultan por separado, podría ser difícil detectar a tiempo una actividad sin realizar o un informe pendiente de revisión. La causa posible sería la falta de una vista compartida de pendientes y de criterios explícitos para su escalamiento.

Consecuencia potencial. Intervención tardía o consultas repetidas para conocer avances. Validación: reconstruir el calendario de una cohorte, contrastar compromisos con sus evidencias y averiguar cómo se identifican y atienden pendientes. No se dispone de datos de retrasos ni de carga de trabajo.

## P6 Seguimiento confidencial de novedades por precisar

El retiro exige trámite formal; los conflictos siguen un conducto regular y existe una ruta de atención al acoso que exige tratamiento confidencial \[L, pp. 10, 18–19, 24–25].

Limitación documental e hipótesis. No se especifican en detalle permisos de consulta, registro de recepción y controles tecnológicos del expediente de cada caso. La hipótesis es que un seguimiento genérico sin separación de acceso podría dificultar la coordinación o exponer información a personas ajenas al trámite. No se afirma que haya ocurrido una filtración.

Consecuencia potencial. Falta de claridad sobre la instancia que debe actuar o acceso innecesario a información reservada. Validación: revisar el protocolo y los permisos con responsables autorizados, usando un caso ficticio. No es necesario recopilar testimonios ni expedientes sensibles para esta actividad.

## Síntesis causal

El diagnóstico muestra que los puntos más relevantes se encuentran en los intercambios de información: la revisión de requisitos, el visto bueno de un informe, la validación de horas y la consolidación de resultados. Antes de proponer cambios, debe comprobarse qué parte de esos intercambios resuelven las herramientas actuales y dónde se requiere una mejor coordinación.

# 5 Oportunidades de transformación digital

A partir del diagnóstico se plantean seis oportunidades. Cada una relaciona una dificultad con un cambio en la gestión, el beneficio que se espera y las condiciones para llevarlo a cabo. La elección de herramientas corresponde a una etapa posterior, una vez se confirme qué necesita el proceso y qué ofrecen los recursos institucionales actuales.

## O1 Verificación coordinada de requisitos de incorporación

Esta oportunidad responde a P1. Los soportes de incorporación provienen de distintas actividades; por ello, interesa que el estudiante y la coordinación puedan reconocer cuáles se han revisado y cuáles siguen pendientes.

Se propone organizar cada incorporación mediante una lista de requisitos aplicables al programa, con soporte asociado, responsable de verificación y estado. Registrar observaciones y devolución para subsanar, evitando repetir la solicitud de una evidencia ya validada cuando sea reutilizable.

Se espera facilitar que CP y estudiante conozcan qué falta y quién debe actuar. Evidencia futura del beneficio: comparación de tiempos de revisión y devoluciones antes y después, sin fijar todavía metas numéricas.

La aprobación de elegibilidad corresponde a la autoridad académica. No se propone aprobación automática ni se da por disponible una integración con matrícula. Primero deben confirmarse los requisitos, responsables y fuentes oficiales.

## O2 Expediente de práctica con trazabilidad de evidencias

Para atender P2 se propone relacionar los documentos y las decisiones de cada práctica. El propósito es que una consulta permita identificar la evidencia vigente y conocer cómo fue revisada.

La mejora consiste en relacionar los registros mediante una referencia común de práctica y conservar autor, fecha, versión y revisión. Permitir consultar el estado y el historial según la función de cada participante. Un expediente puede enlazar registros de herramientas existentes; no exige reunir todo en una aplicación nueva.

Esto permitiría reconstruir qué se presentó, quién lo revisó y qué decisión se tomó, con menor esfuerzo de búsqueda y menor riesgo de usar una versión incorrecta. Su verificación futura puede medir el tiempo necesario para recuperar una evidencia y su aprobación.

La evidencia original y su autoría se conservan. La digitalización no sustituye la revisión académica; los documentos sensibles requieren acceso restringido. Primero debe inventariarse la plataforma mencionada en los lineamientos.

## O3 Control diferenciado de horas y validación de evidencias

P3 requiere aclarar primero qué horas se contabilizan y cómo se aplica cada control de asistencia. Con esa base, el registro y la validación podrían hacerse de manera consistente durante el semestre.

Se propone registrar separadamente horas en escenario, asesoría y formación, relacionándolas con fechas y actividades. Acordar reglas de cómputo y revisión con el programa; establecer un ciclo de registro, observación y validación por el responsable correspondiente.

El resultado esperado es disponer de consolidaciones comprensibles y detectar inconsistencias antes del cierre. La evaluación futura puede contrastar correcciones de registros y diferencias entre consolidaciones.

Ningún umbral debe convertirse en sanción automática. Se mantienen la valoración humana, las excepciones institucionales y el conducto regular. La interpretación de las reglas es un requisito previo al uso de alertas de cumplimiento.

# 5 Oportunidades de información y coordinación

## O4 Consolidación de informes con datos comparables

La oportunidad asociada con P4 consiste en facilitar el paso de los registros de cada práctica a los informes del programa y la facultad. Para ello, las cifras deben conservar una relación clara con sus fuentes.

El primer paso es acordar definiciones, periodos de corte e identificadores comunes; reutilizar los datos validados en informes del programa y la facultad. Mantener acceso a su origen para explicar los resultados, junto con espacio para análisis cualitativo.

Se espera reducir conciliaciones y facilitar comparaciones interpretables entre periodos. La validación futura debe comprobar el tiempo de preparación y la concordancia entre totales del informe y registros fuente.

La consolidación no sustituye la interpretación de coordinadores y facultades. Los programas conservan sus particularidades. Su desarrollo depende de datos confiables de O2 y O3; no se promete un tablero con cifras que todavía no pueden obtenerse.

## O5 Seguimiento compartido de compromisos y pendientes

Frente a P5, se propone que los participantes puedan consultar los compromisos que les corresponden y reconocer cuándo una actividad necesita atención. Esto exige vincular la agenda con el seguimiento que ya realizan asesor y supervisor.

Se propone asociar compromisos con responsable, fecha y evidencia de cierre; facilitar vistas de pendientes por rol y avisos basados en fechas acordadas. Definir cuándo un pendiente debe ser revisado por el asesor o remitido a CP.

La mejora busca apoyar intervenciones oportunas y disminuir consultas repetidas sobre el estado de las actividades. El beneficio deberá contrastarse con entregas oportunas y tiempo transcurrido hasta la atención de un pendiente.

Una alerta no es una sanción. El acompañamiento, las visitas y la retroalimentación se mantienen. Evitar avisos redundantes y permitir que el responsable justifique o reprograme según las reglas del programa.

## O6 Gestión de novedades con acceso restringido y conducto regular

La oportunidad derivada de P6 busca que las novedades lleguen a la instancia responsable y puedan seguirse sin divulgar información reservada. Su organización debe respetar las rutas institucionales aplicables a cada caso.

El seguimiento debe registrar recepción, responsable actual y actuaciones necesarias, con acceso según competencia. Separar los datos reservados del seguimiento general. Reflejar las rutas institucionales específicas, en especial la de acoso, sin mezclarla con recordatorios académicos ordinarios.

Se espera facilitar que cada instancia conozca qué debe atender, preservando la confidencialidad. La comprobación deberá realizarse con casos ficticios y revisión de permisos, sin exponer datos reales.

La atención psicológica, la investigación, la decisión académica y cualquier actuación jurídica permanecen en las instancias competentes. No se propone clasificar automáticamente denuncias ni decidir sobre ellas.

## Criterio para transformar y conservar actividades

Conviene apoyar digitalmente la identificación de registros, el seguimiento de estados, los cálculos previamente aclarados y la reutilización de información. Deben conservar intervención humana la pertinencia del escenario, la valoración formativa, las autorizaciones excepcionales, la interpretación de casos y las decisiones de mejora. La propuesta transforma la coordinación; no busca automatizar todas las actividades \[P, p. 3].

# 6 Método de priorización de oportunidades

La priorización compara el valor potencial y las condiciones de adopción de O1–O6. Se utiliza una matriz ponderada de cinco criterios. Las calificaciones son estimaciones razonadas del análisis documental, no mediciones de CECAR ni resultados de una consulta al equipo institucional. Deben revisarse al validar los hallazgos.

| **Criterio y peso** | **Qué evalúa** | **Anclas de puntuación** |
| --- | --- | --- |
| I Impacto en el proceso<br>30 % | Alcance del beneficio sobre continuidad y coordinación de la práctica. | 1: actividad local aislada. 3: una fase con varios actores. 5: varias fases o condición crítica para continuidad o protección. |
| T Trazabilidad<br>25 % | Capacidad de relacionar evidencias, responsables y decisiones. | 1: aporta poca visibilidad. 3: mejora un registro o estado. 5: permite reconstruir un historial o una decisión relevante. |
| V Valor académico y de gestión<br>20 % | Apoyo al seguimiento, evaluación y mejora institucional. | 1: conveniencia administrativa menor. 3: mejora una tarea periódica. 5: sustenta evaluación o análisis agregado para decisiones. |
| F Facilidad de adopción<br>15 % | Complejidad relativa de acuerdos, cambio de hábitos y configuración. | 1: cambio amplio con alta dependencia. 3: coordinación de varios roles y reglas. 5: cambio acotado con pocas dependencias. |
| D Base documental de datos<br>10 % | Claridad de los registros de origen mencionados por los lineamientos. | 1: no se identifica la fuente. 3: existen registros pero falta armonizarlos. 5: origen, estructura y validación suficientemente definidos. |

Los valores 2 y 4 representan posiciones intermedias. Una puntuación alta en F significa mayor facilidad. D no mide disponibilidad digital ni acceso efectivo: mide la identificación documental de los datos y controles; esa diferencia evita sobreestimar la viabilidad tecnológica.

## Cálculo

Puntuación = 0,30 × I + 0,25 × T + 0,20 × V + 0,15 × F + 0,10 × D. El resultado se encuentra entre 1 y 5. Los pesos suman 100 %. El mayor peso se asigna al impacto y la trazabilidad porque responden directamente al reto del proyecto \[P, pp. 1–3].

## Reglas de decisión

Se considera alta una puntuación igual o superior a 4,20; media, de 3,50 a 4,19; y baja, menor a 3,50. Son umbrales de clasificación propuestos para este ejercicio, no reglas de CECAR. Un empate se resuelve primero por dependencia habilitadora y después por trazabilidad.

La clasificación no determina por sí sola el orden de ejecución. Deben respetarse tres condiciones: validar el problema; confirmar las reglas institucionales; y aplicar confidencialidad y control de acceso desde el inicio. Una oportunidad dependiente puede tener alto valor y aun así requerir trabajo previo.

# 6 Resultados y justificación de la priorización

| **Orden** | **Oportunidad** | **I** | **T** | **V** | **F** | **D** | **Total** | **Nivel** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | O2 Expediente y trazabilidad | 5 | 5 | 5 | 3 | 4 | 4,60 | Alta |
| 2 | O3 Horas y evidencias | 5 | 5 | 4 | 3 | 4 | 4,40 | Alta |
| 3 | O1 Requisitos de incorporación | 5 | 4 | 4 | 4 | 4 | 4,30 | Alta |
| 4 | O6 Novedades confidenciales | 5 | 5 | 4 | 2 | 3 | 4,15 | Media |
| 5 | O5 Compromisos y pendientes | 4 | 4 | 4 | 4 | 4 | 4,00 | Media |
| 6 | O4 Consolidación de informes | 4 | 4 | 5 | 3 | 3 | 3,95 | Media |

Ejemplo verificable para O2: 0,30 × 5 + 0,25 × 5 + 0,20 × 5 + 0,15 × 3 + 0,10 × 4 = 4,60. La clasificación resume el juicio documental y no implica que existan recursos, presupuesto o acuerdos para implementarla.

| **Oportunidad** | **Razón de las calificaciones** |
| --- | --- |
| O2 4,60 | I5/T5/V5: conecta fases y respalda decisiones con evidencia. F3: exige acuerdos entre varios roles y revisión de las herramientas. D4: se identifican registros fuente, pero no un esquema de enlace integral. |
| O3 4,40 | I5/T5: afecta seguimiento y cierre académico con evidencia verificable. V4: se concentra en cumplimiento. F3: requiere aclarar reglas y hábitos de registro. D4: la asistencia existe como registro, pero se deben precisar sus categorías. |
| O1 4,30 | I5: condiciona el inicio y la continuidad del recorrido. T4/V4: mejora la revisión de requisitos. F4: el cambio puede acotarse a un expediente y responsables. D4: los soportes están identificados, aunque la fuente de cada verificación debe confirmarse. |
| O6 4,15 | I5/T5: atiende situaciones críticas y su conducto institucional. V4: respalda atención y continuidad. F2: requiere acuerdos especializados y controles de acceso. D3: las rutas están descritas, pero falta concretar datos mínimos y permisos. |
| O5 4,00 | I4/T4/V4: mejora coordinación y oportunidad de intervención sin sustituir evaluación. F4: puede comenzar con compromisos acotados. D4: hay agenda y registros, pero es necesario contrastar fechas y evidencia de cierre. |
| O4 3,95 | I4/T4: conecta resultados de programa y facultad. V5: sustenta gestión y mejora. F3: necesita armonizar definiciones entre actores. D3: los informes se mencionan, pero la comparabilidad de sus campos está por verificar. |

## Interpretación

O2 ocupa el primer lugar porque habilita relaciones entre evidencias y decisiones que las demás oportunidades necesitan. O3 requiere aclaración académica previa. O6 recibe una prioridad cuantitativa media por complejidad, pero sus controles básicos de confidencialidad no pueden posponerse hasta una etapa tardía.

# 6 Sensibilidad y orden recomendado

## 6 1 Comprobación de sensibilidad

Para examinar cuánto depende el orden de los pesos, se recalcula la matriz dando mayor importancia a la facilidad: I 20 %, T 20 %, V 15 %, F 30 % y D 15 %. Las puntuaciones de cada oportunidad se mantienen. El escenario no es una estimación presupuestal; comprueba la estabilidad de la decisión.

| **Oportunidad** | **Escenario base** | **Mayor facilidad** | **Lectura** |
| --- | --- | --- | --- |
| O1 | 4,30 | 4,20 | Asciende al segundo lugar. |
| O2 | 4,60 | 4,25 | Conserva el primer lugar. |
| O3 | 4,40 | 4,10 | Pasa al tercer lugar. |
| O4 | 3,95 | 3,70 | Permanece entre las últimas. |
| O5 | 4,00 | 4,00 | Supera a O6 en facilidad. |
| O6 | 4,15 | 3,65 | Su complejidad reduce su posición. |

O2 se mantiene primera en ambos escenarios. O1 y O3 intercambian su posición, por lo que no conviene presentar su orden como definitivo. El diseño de O1 puede avanzar mientras se aclaran las reglas de O3. O6 debe tratarse como salvaguarda transversal aunque su desarrollo especializado sea más complejo.

## 6 2 Secuencia propuesta de trabajo posterior

| **Momento** | **Oportunidades y propósito** | **Condición para avanzar** |
| --- | --- | --- |
| Preparación | Validar P1–P6; inventariar plataformas y formatos; aclarar R4/R7; definir acceso mínimo para O6. | AS-IS contrastado con responsables y reglas académicas aclaradas. No requiere seleccionar una tecnología. |
| Base de trazabilidad | Priorizar O2 y acordar referencia de práctica, evidencias, versiones y revisores. | Confirmar qué puede resolverse con los registros existentes y qué debe mejorarse. |
| Gestión operativa | Desarrollar O1; avanzar O3 después de aclarar reglas; incorporar O5 conforme existan estados y fechas confiables. | Requisitos aplicables y responsables confirmados; registro de horas y agenda consistente. |
| Información para gestión | Profundizar O4 con registros validados. Desarrollar las particularidades de O6 con las instancias competentes. | Definiciones comparables, origen trazable y permisos revisados. Las protecciones de O6 rigen desde el inicio. |

## 6 3 Trazabilidad entre diagnóstico y decisión

P1 → O1 → incorporación coordinada. P2 → O2 → evidencia e historial verificables. P3 → O3 → cómputo y revisión de horas consistentes. P4 → O4 → informes comparables. P5 → O5 → seguimiento oportuno. P6 → O6 → atención con conducto regular y acceso restringido. Estas relaciones sustentan el TO-BE del apartado 7 y las decisiones tecnológicas de los apartados 9–12.

# 7 Modelo TO BE del proceso propuesto

La propuesta organiza la gestión alrededor de un expediente identificado por estudiante, programa y periodo. Cada requisito, documento, registro de horas o revisión se relaciona con esa práctica. Los actores mantienen sus responsabilidades académicas; la tecnología facilita el intercambio de información y conserva el recorrido de las decisiones.

El alcance inicial es un piloto de un programa durante un semestre. El diseño contempla incorporación, acompañamiento y cierre; las particularidades de otros programas se incorporarían después de validar reglas y capacidad de operación. Las novedades reservadas siguen rutas específicas y no se muestran en las consultas académicas ordinarias.

## 7 1 Decisiones de rediseño y trazabilidad

| **Origen** | **Decisión propuesta** | **Cambio verificable** |
| --- | --- | --- |
| P1 → O1 | D1 Asociar requisitos aplicables, soportes y decisión de revisión a la práctica. | RF02–RF03: el estudiante conoce el pendiente y CP confirma la habilitación. K1 y K2 miden incorporación. |
| P2 → O2 | D2 Conservar versiones y revisiones referidas a una versión concreta. | RF05–RF06: el visto bueno no se traslada a una corrección nueva. K4 y K5 parten del historial de informes. |
| P3 → O3 | D3 Separar minutos de sitio, asesoría y formación; registrar quién valida. | RF07: el cómputo de sitio no incluye asesorías. K3 usa solo tiempo de sitio validado. |
| P4 → O4 | D4 Calcular indicadores desde registros vinculados, con filtros y fecha de corte. | RF10: toda cifra permite identificar su base y su fórmula. El informe conserva análisis cualitativo. |
| P5 → O5 | D5 Relacionar compromisos, fechas, responsables y evidencia de atención. | RF04, RF08 y RF11: cada aviso corresponde a un pendiente. K6 muestra cobertura de seguimiento. |
| P6 → O6 | D6 Separar el acceso a los casos reservados del permiso para consultar una práctica. | RF09 y RNF01: ser supervisor de un estudiante no habilita a consultar sus novedades reservadas. |

## 7 2 Qué se automatiza

Se propone automatizar controles de campos obligatorios, identificación de versiones, sumas de minutos validados, cálculo de indicadores y detección de vencimientos. La habilitación, la pertinencia del escenario, el visto bueno, la evaluación y las decisiones sobre novedades corresponden a personas autorizadas.

Los porcentajes de asistencia de los lineamientos no se convierten en sanciones automáticas. Antes del piloto, el programa debe aclarar su aplicación, los tipos de horas y las excepciones. El diseño conserva el historial de cambios de agenda y la aprobación escrita del asesor \[L, pp. 13, 17, 22, 24].

# 7 Recorrido del proceso futuro

Figura 2. Proceso TO-BE. Elaboración de la propuesta a partir del diagnóstico. Los pasos T1–T12 describen el flujo principal; los retornos conservan la versión y la observación que los originaron.

Figura 2. Proceso TO-BE. Elaboración de la propuesta a partir del diagnóstico. Los pasos T1–T12 describen el flujo principal; los retornos conservan la versión y la observación que los originaron.

## Información que circula entre los participantes

T1–T3 intercambian requisitos, soportes, decisión de habilitación y asignaciones. T4–T6 producen agenda, compromisos, evidencia de asesoría y registros de horas. T7–T9 intercambian versiones de informes, observaciones, visto bueno y evaluación. T10–T12 consolidan el cierre y los datos necesarios para la gestión. Todos los pasos usan el identificador de práctica; solo los actores con competencia consultan sus evidencias.

## Variantes del recorrido

Si el escenario no está formalizado, T3 queda pendiente y CP gestiona la condición faltante. Un cambio de agenda conserva fecha anterior, motivo y autorización. Las actividades de acompañamiento continúan entre cortes. Una devolución en T8 o T9 exige una nueva versión en T7 y una nueva revisión; la evidencia anterior permanece consultable.

# 7 Estados y reglas de transición

| **Objeto y transición** | **Quién decide y condición** | **Información que se conserva** |
| --- | --- | --- |
| Expediente: borrador → recibido → en revisión | Estudiante envía; CP revisa requisitos aplicables. | Fecha de recepción, lista de requisitos y observaciones. |
| En revisión → pendiente o habilitado | CP confirma soportes y condiciones académicas, con el apoyo competente. | Autor, fecha, resultado y fuente de verificación; fecha en que el expediente quedó completo. |
| Habilitado → activo | CP confirma escenario formalizado, asignaciones y agenda. | Instrumento de formalización, vigencia de responsables e inicio previsto. |
| Informe: enviado → observado | Supervisor o asesor devuelve con observación motivada. | Versión revisada, comentario y fecha; el archivo no se sobrescribe. |
| Informe: enviado → visto bueno → validado | Supervisor asignado respalda la versión; asesor la valida. No se permite saltar el visto bueno. | Dos actuaciones distintas sobre la misma versión vigente. |
| Horas: enviadas → observadas o validadas | Supervisor valida sitio; asesor valida asesoría y formación, sujeto a la regla del programa. | Tipo, actividad, fecha, minutos, revisor y decisión. Correcciones conservan antecedente. |
| Activo → cierre en revisión → cerrado | Asesor completa evaluación; CP verifica evidencias de cierre. | Informes, soportes, evaluación, socialización y fecha de cierre. |
| Caso: recibido → asignado → en atención → cerrado | Instancias de la ruta correspondiente; cada remisión se registra. | Responsable actual, acceso autorizado y actuaciones reservadas. |

## Tratamiento de excepciones

Una habilitación no implica que el estudiante ya pueda iniciar si falta formalizar el escenario. Un archivo no se considera validado por haberse cargado. Una revisión desactualizada se rechaza y solicita recargar el estado vigente. Los recordatorios no cambian calificaciones ni cierran compromisos automáticamente.

Si el sistema no está disponible, CP conserva un registro temporal identificado y lo concilia al restablecer el servicio. El retiro y la ruta de acoso mantienen las instancias previstas en los lineamientos \[L, pp. 18–19, 25]. La aplicación registra las actuaciones; no sustituye la atención ni la decisión institucional.

# 8 Requisitos funcionales

Los requisitos se derivan de T1–T12. La prioridad Alta corresponde al flujo básico y al control de información; Media identifica capacidades necesarias para completar el piloto, sin anteponerlas al expediente y sus revisiones.

| **ID y prioridad** | **Capacidad requerida** | **Criterio de aceptación** |
| --- | --- | --- |
| RF01 Alta | Administrar asignaciones por rol, programa, práctica y vigencia. | Un usuario ajeno no consulta ni modifica un expediente; la reasignación conserva el historial. |
| RF02 Alta | Configurar requisitos por programa, modalidad y periodo. | Cada práctica conserva la versión de requisitos que le corresponde; cambiar el catálogo no modifica expedientes previos. |
| RF03 Alta | Revisar incorporación y registrar habilitación o pendientes. | No se confirma habilitación con un requisito obligatorio sin validar. Se registran fecha de expediente completo y decisión. |
| RF04 Alta | Gestionar agenda y cambios autorizados. | Un cambio conserva fecha anterior, motivo, autor y aprobación del asesor cuando aplica. |
| RF05 Alta | Recibir evidencias con versiones independientes. | Una nueva versión no reemplaza la anterior; conserva autor, fecha, referencia de archivo y hash. |
| RF06 Alta | Gestionar visto bueno y validación de informes. | Solo el supervisor asignado emite visto bueno y solo el asesor asignado valida la versión vigente. |
| RF07 Alta | Registrar y validar horas por categoría. | Las sumas distinguen sitio, asesoría y formación; registros pendientes, anulados o posteriores al corte no se suman como validados. |
| RF08 Alta | Registrar seguimiento y evidencia de compromisos. | Una actividad atendida tiene responsable, fecha y evidencia; el cierre conserva las observaciones. |
| RF09 Alta | Gestionar novedades con permisos específicos por caso. | El acceso al expediente académico no permite leer el contenido de un caso sin autorización expresa. |
| RF10 Media | Calcular y consultar KPI por ámbito y corte. | Los seis valores coinciden con una muestra controlada; muestran base, filtros, fórmula y N/D si no hay población. |
| RF11 Media | Crear avisos de vencimiento sin duplicarlos. | La misma práctica, compromiso y fecha generan un único evento; los reintentos conservan estado. |
| RF12 Alta | Registrar auditoría de operaciones relevantes. | Todo cambio de estado conserva actor, fecha, objeto y acción en la misma transacción. |
| RF13 Media | Consolidar informes y exportar resultados autorizados. | La exportación respeta filtros y permisos, identifica fecha de corte y excluye detalles de casos reservados. |
| RF14 Alta | Registrar evaluación por corte y cierre académico. | La ponderación 40/60 se configura según lineamientos; el cierre exige verificación humana de los productos del programa. |

# 8 Requisitos no funcionales

Las cifras siguientes son objetivos propuestos para aceptar un piloto; no describen la infraestructura ni el desempeño actual de CECAR. El escenario de referencia es de 200 prácticas, 50 sesiones concurrentes y documentos de hasta 10 MB. Debe ajustarse al inventario institucional.

| **ID** | **Condición verificable** | **Cómo se comprobaría** |
| --- | --- | --- |
| RNF01 Seguridad | Autorización en servidor por objeto y rol; casos con acceso explícito; MFA para cuentas privilegiadas mediante identidad institucional u OIDC. | Pruebas negativas de acceso y revisión de configuración de identidad. La PoC verifica un subconjunto de permisos; no prueba MFA. |
| RNF02 Integridad | Estado y auditoría se guardan juntos. No se admiten claves de versión o aviso duplicadas; revisión obsoleta rechazada. | Pruebas de fallo y repetición; comprobación transaccional en PostgreSQL antes del piloto. |
| RNF03 Disponibilidad | Objetivo mensual 99 % en horario acordado, excluyendo mantenimiento anunciado. | Monitoreo y reporte del periodo; no se garantiza esta cifra con la prueba local. |
| RNF04 Recuperación | Objetivos RPO ≤24 h y RTO ≤8 h; copia de base y archivos consistente, separada del servidor. | Restaurar ambos en un entorno de prueba y comprobar enlaces y hashes. RPO mide pérdida máxima; RTO, tiempo de recuperación. |
| RNF05 Rendimiento | 95 % de consultas de expediente o tablero ≤3 s en el escenario acordado, sin contar transferencias de archivos. | Prueba de carga con 50 sesiones, datos representativos y medición por operación. Pendiente. |
| RNF06 Accesibilidad | Objetivo WCAG 2.2 AA para los recorridos del piloto; teclado, etiquetas, contraste y foco visible \[T15]. | Revisión manual de teclado y lector de pantalla más evaluación automatizada. El prototipo no acredita conformidad completa. |
| RNF07 Protección de archivos | HTTPS; archivos privados fuera de la raíz pública; validación de tipo, tamaño y análisis antimalware antes de disponibilidad. | Intentar descarga directa y carga no permitida; revisar autorización, cuarentena y configuración. Antimalware no implementado en la PoC. |
| RNF08 Mantenibilidad | Reglas de programa separadas del código; migraciones versionadas, pruebas y documentación operativa. | Reproducir despliegue, cambio de regla y reversión controlada en un entorno de ensayo. |
| RNF09 Interoperabilidad | Exportaciones con esquema documentado y fechas ISO 8601; identificadores estables. Integraciones solo mediante interfaces autorizadas. | Importación de un archivo de ensayo y reconciliación de registros. No se presume una API de CECAR. |
| RNF10 Usabilidad | Al menos 4 de 5 participantes de un piloto de usabilidad completan envío y revisión sin ayuda; errores se explican junto al campo. | Sesiones observadas con roles representativos. Este estudio con usuarios no se ha realizado. |

# 9 Arquitectura tecnológica propuesta

Se propone una aplicación web con módulos internos para incorporación, evidencias, horas, seguimiento y gestión. Comparte datos y reglas para evitar duplicar revisiones. La separación mostrada es lógica: no obliga a desplegar cada módulo como un servicio independiente.

Figura 3. Arquitectura propuesta y flujos principales. C1 es el punto de autorización. C4 acredita identidad; la aplicación conserva la decisión sobre qué prácticas o casos puede consultar cada usuario.

Figura 3. Arquitectura propuesta y flujos principales. C1 es el punto de autorización. C4 acredita identidad; la aplicación conserva la decisión sobre qué prácticas o casos puede consultar cada usuario.

## Un recorrido representativo

El estudiante inicia sesión y C1 comprueba la asignación. Al enviar un informe, C3 almacena el archivo con una clave nueva y C2 conserva metadatos y evento. Supervisor y asesor revisan la misma versión mediante C1. C5 consulta únicamente registros autorizados para calcular indicadores. C6 identifica el compromiso pendiente y registra un aviso; nunca incluye contenido reservado en el mensaje.

## Fronteras de la propuesta

No se conectan sistemas institucionales durante este trabajo. Matrícula, convenios e identidad deberán confirmarse con TI y las dependencias responsables. Si CECAR dispone de un componente equivalente que satisfaga los requisitos, se evalúa su reutilización antes de desplegar otro.

# 9 Responsabilidad de cada componente

| **Componente** | **Función e información** | **Requisitos y dependencias** |
| --- | --- | --- |
| C1 Portal y proceso | Recibe formularios, referencias de archivos y decisiones. Devuelve estados, observaciones y vistas por rol. Aplica las transiciones T1–T10. | RF01–RF09, RF12 y RF14. Consulta C4 para identidad; usa C2 y C3; expone resultados de C5. |
| C2 Base relacional | Conserva prácticas, asignaciones, requisitos, versiones, revisiones, horas, agenda y eventos. Ejecuta transacciones y restricciones. | RNF02 y RF12. Recibe operaciones de C1 y C6; C5 realiza lectura de datos autorizados. |
| C3 Repositorio privado | Conserva el contenido de cada evidencia; C2 guarda su clave, tamaño, tipo y hash. La descarga pasa por C1. | RF05 y RNF07. Copia y restauración coordinadas con C2; no se usa un enlace público al archivo. |
| C4 Identidad | Autentica al usuario y entrega un identificador verificable. C1 lo relaciona con asignaciones vigentes. | RNF01. OIDC con Keycloak como alternativa de referencia; primero se verifica el proveedor institucional. |
| C5 Indicadores e informes | Recibe datos del programa y periodo autorizados, fechas y definiciones. Devuelve numerador, denominador, resultado y detalle de origen. | RF10 y RF13. Consultas de lectura; excluye descripciones reservadas de casos. |
| C6 Tareas y avisos | Lee compromisos vencidos; crea avisos con clave única y registra reintentos. Publica en bandeja interna. | RF11. Un proceso programado ejecuta comandos Django; correo opcional tras aprobar el canal institucional. |
| C7 Operación | Aloja la aplicación y servicios; aplica TLS, monitoreo, copias y restauración. Registra fallos y uso de capacidad. | RNF03–RNF05, RNF08. TI debe asumir operación, actualizaciones y gestión de incidentes. |

## Control de acceso y separación de funciones

El rol por sí solo no basta. La consulta combina identidad, programa, práctica, vigencia de asignación y, cuando corresponde, autorización del caso. Los usuarios técnicos de servicio no reciben permisos académicos. La administración de infraestructura requiere trazabilidad adicional, pues una bitácora de aplicación no es inmutable frente a un administrador de base de datos.

Los archivos en carga pasan por cuarentena. Si falla la persistencia de metadatos, se conserva un registro del error y se limpia el archivo huérfano mediante una tarea controlada. Cerrar una práctica no elimina su evidencia: retención y eliminación deben acordarse con la política institucional.

# 10 Modelo conceptual de datos

Figura 4. Entidades y relaciones del modelo conceptual. Programa y periodo se relacionan por separado con Práctica. Las asignaciones permiten conservar cambios de responsable; AccesoCaso establece permisos adicionales.

Figura 4. Entidades y relaciones del modelo conceptual. Programa y periodo se relacionan por separado con Práctica. Las asignaciones permiten conservar cambios de responsable; AccesoCaso establece permisos adicionales.

## Cardinalidades esenciales

Un estudiante puede tener varias prácticas en periodos distintos. Cada práctica pertenece a un programa y periodo y tiene un escenario asignado cuando se activa. Un usuario participa en varias prácticas y una práctica tiene varios usuarios mediante Asignación. Cada documento tiene una o más versiones; cada versión puede tener varias revisiones. Horas, compromisos, seguimientos y evaluaciones pertenecen a una práctica.

Un caso puede tener varias actuaciones y usuarios autorizados. Su relación con la práctica no concede acceso automático. Una definición de KPI puede originar muchos cálculos para distintos filtros y cortes. El resultado del indicador no reemplaza los datos de origen.

# 10 Diccionario y gobierno de datos

| **Entidad o conjunto** | **Datos esenciales y origen** | **Consulta y regla de calidad** |
| --- | --- | --- |
| Práctica y Asignación | Código, estudiante, programa, periodo, escenario, rol y vigencia. CP registra y confirma. | Actores asignados; una habilitación conserva fecha y soporte. No reutilizar códigos. |
| Escenario y Convenio | Organización, instrumento, vigencia, aval y referencias de documentos. CP y dependencias competentes. | CP, asesor y responsables de formalización. Un instrumento vencido exige revisión humana. |
| RequisitoAplicado | Catálogo y versión de regla; estado, evidencia, revisor, fecha completa y habilitación. Estudiante y CP. | Estudiante propio y revisores autorizados; distinguir recepción de validación. |
| Documento y Versión | Tipo, corte, número, clave de archivo, hash, autor, fecha y estado. Estudiante u originador. | Participantes autorizados. Unicidad documento+número; nunca sobrescribir contenido previo. |
| Revisión y EventoAuditoría | Actor, acción, versión revisada, estado anterior y posterior, fecha y motivo. Sistema y revisor. | Responsables y auditoría autorizada; conservar la secuencia transaccional. |
| RegistroHoras | Fecha, actividad, categoría, minutos, estado, revisor y fecha de validación. Estudiante y revisor. | Supervisor en sitio; asesor en asesoría y formación. Identificador estable; detectar solapamientos antes de validar. |
| Plan, Compromiso y Seguimiento | Actividad, fecha original y vigente, responsable, evidencia de atención. Asesor y actores asignados. | Actores del expediente; una reprogramación conserva la autorización y la historia. |
| Evaluación | Corte, instrumento, participantes, valoración, soportes y aprobación. Asesor y evaluadores. | Actores competentes. No inferir ponderaciones internas de auto/co/heteroevaluación no definidas. |
| Caso, Actuación y AccesoCaso | Clasificación, responsable, actuaciones, vigencia del permiso. Instancias de atención. | Solo autorizados por caso. No incluir contenido reservado en el tablero general. |
| Aviso y CálculoKPI | Clave de evento, destinatario, estado; o fórmula versionada, filtros, corte, base y valor. Sistema. | Avisos propios; KPI según ámbito. N/D si la base es cero; registrar fecha de generación. |

Las fechas se almacenan con zona horaria y se presentan en America/Bogota. El cálculo histórico debe reconstruir el estado al corte desde eventos o instantáneas; no basta filtrar el estado actual. Los catálogos de reglas se versionan. CP es responsable de calidad funcional; TI custodia y recupera los datos sin definir las reglas académicas.

# 11 Evaluación comparativa de tecnologías

La comparación sigue a la arquitectura. Se califican alternativas para cada componente relevante; las puntuaciones expresan un juicio de diseño para un piloto de un programa, no resultados de pruebas comparativas de rendimiento ni precios cotizados.

| **Criterio** | **Peso** | **Significado de 1 y 5** |
| --- | --- | --- |
| F Ajuste funcional | 30 % | 1: exige resolver capacidades centrales adicionales. 5: encaja con las funciones definidas. |
| S Control y seguridad | 25 % | 1: controles limitados para el caso. 5: ofrece mecanismos adecuados, que deben configurarse y comprobarse. |
| O Operación y costo relativo | 20 % | 1: agrega varias dependencias o costos operativos. 5: pocas dependencias bajo el escenario planteado. |
| M Mantenimiento | 15 % | 1: exige esfuerzo especializado continuo. 5: simplifica cambios y operación previstos. |
| I Interoperabilidad | 10 % | 1: integración muy restringida. 5: interfaces y formatos apropiados para el diseño. |

Puntaje = 0,30F + 0,25S + 0,20O + 0,15M + 0,10I. Los valores 2–4 son intermedios. Un costo relativo favorable no significa costo cero. Se excluye del puntaje la familiaridad del equipo con una herramienta; se exige documentación y evidencia de ajuste al problema.

| **Comp.** | **Alternativa** | **F** | **S** | **O** | **M** | **I** | **Total** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | Django 5.2 LTS | 5 | 4 | 4 | 4 | 5 | 4,40 |
| C1 | Laravel | 5 | 4 | 4 | 4 | 4 | 4,30 |
| C2 | PostgreSQL | 5 | 5 | 4 | 4 | 5 | 4,65 |
| C2 | MySQL InnoDB | 5 | 4 | 4 | 4 | 5 | 4,40 |
| C3 | Repositorio privado en VM | 4 | 4 | 5 | 4 | 4 | 4,20 |
| C3 | Amazon S3 con versionado | 5 | 5 | 3 | 3 | 4 | 4,20 |
| C4 | Keycloak vía OIDC | 5 | 5 | 3 | 3 | 5 | 4,30 |
| C4 | Autenticación nativa Django | 4 | 3 | 5 | 5 | 3 | 4,00 |
| C5 | Indicadores en el portal | 5 | 4 | 5 | 3 | 5 | 4,45 |
| C5 | Metabase | 5 | 4 | 3 | 4 | 4 | 4,10 |
| C6 | Comandos Django programados | 4 | 4 | 5 | 4 | 4 | 4,20 |
| C6 | Celery y scheduler | 5 | 4 | 2 | 3 | 5 | 3,85 |
| C7 | VM Linux administrada | 4 | 4 | 4 | 3 | 5 | 3,95 |
| C7 | Azure App Service | 4 | 4 | 3 | 5 | 4 | 3,95 |

# 11 Análisis de alternativas de proceso y datos

## C1 Aplicación Django y Laravel

Django incorpora usuarios, grupos y permisos; Laravel permite organizar autorización mediante gates y policies \[T1, T4]. Ambos requieren desarrollar el flujo académico y las verificaciones por expediente. Django obtiene 4,40 y Laravel 4,30: el pequeño diferencial se asigna a la integración del cálculo y la lógica en el entorno Python planteado, no a una superioridad general. La PoC reduce incertidumbre sobre el recorrido implementado en Django; Laravel no se probó.

Se propone Django por la coherencia entre formularios, datos, revisiones y pruebas reproducibles. La diferencia de 0,10 es sensible a los supuestos: si TI opera Laravel y no dispone de soporte Python, corresponde revisar la selección. Se usa la rama 5.2 LTS con un parche mantenido, verificando soporte y actualizaciones antes del despliegue \[T16].

## C2 PostgreSQL y MySQL

Ambas alternativas permiten relaciones y restricciones de integridad \[T5, T6]. PostgreSQL ofrece además políticas de seguridad por fila, una posible defensa complementaria para la separación por ámbito; su uso requiere diseño y no reemplaza los permisos de C1 \[T17]. En la valoración del proyecto obtiene 4,65 frente a 4,40 de MySQL. La ventaja se concentra en ese control adicional; el modelo relacional no depende exclusivamente de PostgreSQL.

Se selecciona PostgreSQL para el piloto institucional. La prueba local usa SQLite para facilitar reproducción, por lo que no verifica concurrencia, bloqueos ni políticas de PostgreSQL. Migraciones, restricciones y transacciones se deben repetir en el motor seleccionado antes de utilizar datos reales.

## C3 Repositorio privado y almacenamiento S3

Django permite abstraer el almacenamiento de archivos; sus referencias deben acompañarse de controles de acceso y validación \[T2, T12]. S3 dispone de versionado de objetos \[T7]. Las dos opciones empatan en 4,20: S3 destaca en capacidad de gestión de versiones, mientras que un repositorio privado reduce dependencias en un piloto alojado en una sola VM.

Se propone comenzar con un repositorio privado por la escala del piloto, únicamente si TI asume copias, restauración, control de acceso y vigilancia de capacidad. Las versiones se crean con nombres distintos y metadatos en C2. Si no existe capacidad operativa o se requiere almacenamiento distribuido, el empate favorece reevaluar S3. No se ha contratado ni configurado almacenamiento cloud.

## Interpretación de los resultados

Las fuentes acreditan capacidades; los números son una valoración del caso. El empate de almacenamiento y la cercanía entre frameworks impiden tratar la selección como una verdad universal. Los controles obligatorios se verifican como condiciones de aceptación, aunque una alternativa obtenga un puntaje alto.

# 11 Identidad, informes, tareas y alojamiento

## C4 Identidad

La autenticación nativa de Django reúne usuarios y permisos en la aplicación \[T1]. Keycloak permite integrar aplicaciones mediante OpenID Connect \[T8]. Se prefiere Keycloak como referencia de identidad, con 4,30 frente a 4,00, por separar autenticación del proceso académico y facilitar una política de acceso central. Esa ventaja exige operar un servicio adicional. Si ya existe un proveedor institucional compatible, debe preferirse su reutilización tras validar los requisitos. La conexión OIDC y MFA quedan pendientes de una prueba de integración.

## C5 Informes e indicadores

El portal puede calcular agregados de los registros mediante Django y consultas controladas \[T9]. Metabase ofrece herramientas de permisos sobre datos y colecciones; las capacidades específicas deben verificarse en la edición elegida \[T10]. Para seis KPI definidos y un piloto acotado se selecciona el tablero en el portal, 4,45 frente a 4,10: evita otro servicio y mantiene el mismo ámbito de autorización. Su desventaja es que cada nueva visualización requiere desarrollo. Metabase sería apropiado si aumenta la necesidad de exploración autónoma.

## C6 Tareas y avisos

Django permite crear comandos de gestión \[T3]; un programador del sistema operativo puede ejecutarlos cada hora en el piloto. Celery separa planificación y ejecución mediante tareas y workers, y advierte sobre duplicación si se opera más de un scheduler para la misma agenda \[T11]. Se elige el comando programado, 4,20 frente a 3,85, por la baja frecuencia prevista. Debe registrar último éxito, fallo y reintento; la clave única evita duplicar avisos. La necesidad de muchas tareas concurrentes justificaría revisar Celery.

## C7 Alojamiento

Una VM administrada permite alojar componentes con configuración a cargo de TI; la documentación de Ubuntu ejemplifica esa administración de servicios web \[T14]. Azure App Service ofrece alojamiento administrado de aplicaciones \[T13], pero la base, identidad y almacenamiento deben presupuestarse e integrarse por separado. Ambas alternativas obtienen 3,95: la VM favorece control e integración, mientras que App Service reduce tareas de mantenimiento de la aplicación.

Se selecciona una VM como escenario de referencia, condicionada a capacidad y responsable institucional. No se presupone que CECAR ya disponga de ella. Si debe contratarse toda la operación, el costo y la falta de personal pueden cambiar la decisión a un servicio administrado. La puntuación no autoriza una compra ni acredita un despliegue.

# 12 Selección y condiciones de implementación

| **Comp.** | **Selección propuesta** | **Condición que puede cambiarla** |
| --- | --- | --- |
| C1 | Django 5.2 LTS con plantillas y módulos del proceso. | Capacidad real de TI para mantener Python; reutilización de una plataforma existente. |
| C2 | PostgreSQL para operación institucional. | Repetir pruebas de integridad y concurrencia; compatibilidad con infraestructura aprobada. |
| C3 | Archivos privados con versiones y hash en VM. | Copia y restauración consistentes. Evaluar S3 si no hay capacidad operativa o crece la escala. |
| C4 | Keycloak/OIDC como referencia; preferencia por IdP institucional equivalente. | Integración, ciclo de altas y bajas y MFA privilegiado verificados. |
| C5 | Consultas y tablero dentro del portal. | Revisar Metabase si se necesitan análisis autónomos fuera de los KPI definidos. |
| C6 | Comandos Django programados y bandeja interna. | Monitoreo del job, reintentos y clave única. Correo solo tras validar el canal institucional. |
| C7 | VM Linux con operación asignada a TI. | Responsable, presupuesto y ensayo de recuperación. Revisar PaaS si no se cumplen. |

## Estimación de esfuerzo para un piloto

Como ejercicio de planeación se estiman 220 horas: validación y detalle 28; diseño de datos e identidad 32; flujo de expediente y documentos 48; horas y seguimiento 32; indicadores 24; verificación y seguridad 32; formación y puesta en marcha 24. Son supuestos de alcance, no una cotización ni un compromiso del equipo.

Un escenario ilustrativo de 60.000 COP por hora daría 13.200.000 COP; una reserva del 20 % elevaría el esfuerzo presupuestado a 15.840.000 COP. Ese cálculo no incluye infraestructura, impuestos ni soporte recurrente. La tarifa es un supuesto matemático, no un precio de mercado. TI debe cotizar alojamiento, identidad, copias y operación antes de decidir.

## Capacidad y costo recurrente

Con 200 prácticas, 10 documentos por práctica, 3 versiones por documento y 2 MB promedio, se estiman 12.000 MB de archivos: aproximadamente 12 GB decimales. Una copia completa adicional requiere otros 12 GB antes de compresión; no se incluyen logs, base de datos, sobrecarga ni retención de varios periodos. La cifra orienta una cotización y debe ajustarse con formatos reales.

Costo total del primer año = implementación + alojamiento + almacenamiento y copias + soporte + servicios/licencias aplicables + contingencia. Las fuentes consultadas no permiten determinar un total institucional sin conocer contratos y capacidad existente. Tampoco hay una línea base de tiempos o costos que permita afirmar un retorno de inversión numérico.

# 13 Prueba de concepto: propósito y método

Se construyó una prueba de concepto local para resolver una incertidumbre concreta: si un expediente puede conservar versiones, restringir revisiones por actor y producir indicadores consistentes sin perder el historial. La prueba comprueba una parte del diseño; no representa una instalación de la solución institucional.

| **Elemento** | **Descripción del ensayo** |
| --- | --- |
| Objetivo | Comprobar permisos sobre documentos y casos, secuencia de aprobación, integridad de cambios, avisos únicos y cálculo reproducible de seis KPI. |
| Entorno ejecutado | Python 3.12.14; Django 5.2.17; Windows; base SQLite temporal; almacenamiento local privado durante el ensayo. |
| Datos | Diez prácticas ficticias SIS-01 a SIS-10 para indicadores y una práctica LAB-01 para operaciones. Corte del conjunto: 18 de septiembre de 2026, 23:59:59, UTC−05:00. |
| Procedimiento | Crear una base temporal; cargar usuarios y asignaciones; guardar dos versiones; intentar accesos permitidos y prohibidos; ejecutar revisiones y un fallo provocado; repetir avisos; calcular indicadores y compararlos con resultados esperados independientes. |
| Criterio de éxito | Todas las respuestas deben coincidir con el resultado esperado. El fallo provocado debe dejar sin cambios el estado y la bitácora. Las seis cifras deben coincidir con el cálculo de control. |
| Ejecución registrada | 20 de septiembre de 2026, 21:49, hora de Colombia. El archivo JSON conserva la marca UTC exacta: 2026-09-21T02:49:22.140790+00:00. |
| Resultado | 20 de 20 comprobaciones aprobadas. La base temporal se elimina al terminar y las evidencias se conservan en los archivos de salida. |

## Evidencia reproducible

La muestra de KPI representa diez prácticas activas y un informe exigible por práctica. Usa estados y fechas preparados para el corte fijo; no implementa todavía la reconstrucción histórica completa ni múltiples informes por práctica. Esa ampliación es necesaria para el piloto.

La carpeta poc contiene ejecutar_poc.py, requirements.txt, datos_ficticios.json, resultados.json y resultados.txt. El código genera la muestra y los resultados sin conectarse a CECAR. El JSON conserva valores esperados y obtenidos, marcas de tiempo, hashes de archivos y eventos. El archivo LEEME de los anexos explica cómo repetirlo en un entorno local.

## Alcance de la conclusión

La prueba respalda la viabilidad de los controles ensayados en Django. Usa sesiones creadas por el cliente de pruebas y SQLite: no comprueba autenticación real, MFA, OIDC, PostgreSQL, envío de correo, carga concurrente ni recuperación de respaldos. La bitácora es transaccional, pero no es inmutable frente a un administrador de base de datos. Esos controles deben verificarse antes de operar con información real.

# 13 Resultados de permisos y flujo documental

| **Prueba** | **Operación** | **Esperado y obtenido** |
| --- | --- | --- |
| T01 | Descargar sin sesión. | 401; acceso rechazado. |
| T02 | Consultar desde un estudiante ajeno. | 404; recurso no expuesto. |
| T03 | Consultar desde el estudiante asignado. | 200; acceso permitido. |
| T04 | Intentar que el estudiante valide su informe. | 403; operación prohibida. |
| T05 | Validar sin visto bueno previo. | 409; transición rechazada. |
| T06 | Aprobar una versión que ya fue superada. | 409; revisión rechazada. |
| T07 | Emitir visto bueno como supervisor asignado. | 200; estado actualizado. |
| T08 | Validar como asesor después del visto bueno. | 200; estado actualizado. |
| T09 | Repetir una revisión con estado desactualizado. | 409; no se repite la aprobación. |
| T10 | Conservar dos archivos independientes. | Ambos existen y sus hashes difieren. |
| T11 | Contar eventos de revisión exitosos. | 2: visto bueno y validación. |
| T12 | Provocar un fallo dentro de la transacción. | Estado y evento revertidos juntos. |
| T13 | Intentar generar dos veces el mismo aviso. | Primero creado, segundo omitido; total 1. |
| T14 | Leer un caso reservado como supervisor. | 404; acceso rechazado. |
| T15 | Leerlo como responsable del caso. | 200; acceso permitido. |

## Qué demuestran estos resultados

El recorrido exige que las decisiones recaigan sobre la versión vigente y en el orden previsto. Las peticiones rechazadas no producen eventos de revisión exitosos. En T12 se introdujo deliberadamente una excepción después del cambio de estado; la reversión impidió que quedara un estado sin su evento correspondiente.

Los archivos LAB-01/v1.txt y LAB-01/v2.txt se guardaron durante el ensayo con hashes SHA-256 distintos. Sus valores completos figuran en resultados.json. Esto permite comprobar la separación de versiones en la muestra; por sí solo no garantiza retención, firma digital ni protección contra alteración administrativa.

# 13 Resultados de datos e indicadores

| **Prueba** | **Operación** | **Resultado comprobado** |
| --- | --- | --- |
| T16 | Calcular los seis KPI con la muestra controlada. | 80 %; 2 días; 90 %; 80 %; 70 %; 80 %. |
| T17 | Filtrar una población vacía. | Seis valores nulos, presentados como N/D. |
| T18 | Añadir horas de asesoría al conjunto. | K3 sigue en 90 %; no aumenta el tiempo de sitio. |
| T19 | Añadir horas con fecha posterior al corte. | K3 sigue en 90 %; el registro futuro se excluye. |
| T20 | Insertar directamente un aviso duplicado. | La restricción única de la base lo rechaza. |

## Cálculo de control de la muestra

| **KPI** | **Base de cálculo ficticia** | **Resultado** |
| --- | --- | --- |
| K1 | 8 habilitaciones antes o en el inicio previsto / 10 inicios exigibles × 100. | 80 % |
| K2 | Mediana de 1, 1, 2, 2, 2, 3, 3, 4 y 5 días; 9 decisiones. | 2 días |
| K3 | 21.600 minutos de sitio validados / 24.000 minutos previstos al corte × 100. | 90 % |
| K4 | 8 primeras entregas oportunas / 10 informes cuyo plazo venció × 100. | 80 % |
| K5 | 7 informes validados al corte / 10 informes exigibles × 100. | 70 % |
| K6 | 8 prácticas con seguimiento reciente / 10 prácticas activas × 100. | 80 % |

En K2 existe además un expediente completo pendiente de decisión. Mostrar ese pendiente evita interpretar la mediana de los casos terminados como el tiempo de toda la población. En K3, 21.600 minutos equivalen a 360 horas y 24.000 a 400 horas; son cantidades acumuladas al corte, no una exigencia normativa universal.

## Decisión derivada del ensayo

Se mantiene Django como alternativa para construir el piloto, porque el ensayo permite expresar las reglas centrales y comprobarlas con una muestra reproducible. La elección de PostgreSQL, el proveedor de identidad y el alojamiento sigue condicionada a pruebas en el entorno objetivo. No se extrapolan porcentajes de la muestra a la gestión real de CECAR.

# 14 Prototipos: incorporación y navegación

Se entrega un prototipo navegable en un único archivo HTML. Abre directamente en el navegador, funciona sin conexión y ofrece seis vistas: expediente, horas, informes, seguimiento, indicadores y novedades. Los datos son ficticios y las acciones permanecen en memoria hasta recargar la página.

Figura 5. Vista del expediente en el prototipo local. Los requisitos pendientes y los responsables se reúnen alrededor de una misma práctica.

Figura 5. Vista del expediente en el prototipo local. Los requisitos pendientes y los responsables se reúnen alrededor de una misma práctica.

## Recorrido de incorporación

El estudiante solicita revisión. La coordinación consulta el listado y confirma soportes; si falta alguno, el prototipo impide confirmar la incorporación. Este recorrido ilustra RF02–RF03. En la solución definitiva cada marca requiere un soporte y una decisión identificables; el HTML solo simula esa interacción.

El selector de rol permite explorar las pantallas durante la sustentación. No es un inicio de sesión ni un control de seguridad. La autorización en servidor se examina por separado en la prueba de concepto del apartado 13.

# 14 Prototipos: versiones y revisión de informes

Figura 6. Informe validado tras el visto bueno del supervisor y la intervención del asesor. El historial conserva la versión anterior.

Figura 6. Informe validado tras el visto bueno del supervisor y la intervención del asesor. El historial conserva la versión anterior.

## Secuencia para demostrar

En la vista Informes, el estudiante envía una nueva versión. Al seleccionar Asesor, la validación permanece bloqueada si falta el visto bueno. El supervisor respalda la versión y después el asesor puede validarla. La devolución registra una observación; una corrección genera otra versión y reinicia su revisión.

| **Control visible** | **Necesidad que representa** |
| --- | --- |
| Historial por versión | Evitar que se confunda una corrección con el documento revisado anteriormente: RF05. |
| Acciones según rol y estado | Distinguir envío, visto bueno y validación: RF06. |
| Observación y confirmación de estado | Informar al estudiante qué debe corregir y cuál es el resultado de la revisión. |

# 14 Prototipos: horas y seguimiento

Figura 7. Registro de horas separado por categoría y validación del supervisor en la demostración.

Figura 7. Registro de horas separado por categoría y validación del supervisor en la demostración.

El estudiante registra actividad, categoría y minutos. El supervisor valida el tiempo de sitio; el asesor puede revisar asesoría y formación. Los totales muestran únicamente registros validados y separan categorías. La pantalla de seguimiento permite que el asesor documente la atención de un compromiso; Novedades presenta un acceso separado para el caso reservado de ejemplo.

## Verificación de la interfaz

Se ejecutaron siete comprobaciones automatizadas en Chrome: bloqueo de validación sin visto bueno; recorrido de revisión completo; registro y validación de horas; coincidencia de seis KPI; filtro vacío N/D; restricción visual del caso reservado; y ausencia de desbordamiento horizontal a 390 píxeles. No se detectaron errores de JavaScript en estos recorridos. La evidencia está en verificacion_prototipo.json y en la carpeta capturas.

Estas comprobaciones no sustituyen una evaluación con estudiantes y funcionarios. Quedan pendientes la comprensión de etiquetas, el tiempo por tarea, el uso con lector de pantalla y el comportamiento con volúmenes reales.

# 15 Indicadores de incorporación

Las metas se proponen para un piloto y deben acordarse con el programa. Cada cálculo conserva programa, periodo, corte, población y fecha de actualización. Si no hay base suficiente, muestra N/D; nunca convierte la ausencia de datos en cumplimiento.

## K1 Habilitación oportuna

| **Campo** | **Definición** |
| --- | --- |
| Objetivo | Estimar si los estudiantes llegan habilitados a la fecha prevista de inicio. |
| Fórmula | 100 × prácticas habilitadas a más tardar en su inicio previsto / prácticas con inicio previsto hasta el corte. |
| Fuente de datos | Práctica.inicio_previsto, decisión de habilitación y su fecha, programa y periodo. La fecha prevista conserva historial. |
| Frecuencia | Actualización diaria; revisión semanal durante incorporación. |
| Meta propuesta | ≥95 %. Mayor es mejor. |
| Responsable | Coordinación de Prácticas. |
| Decisión que apoya | Priorizar expedientes próximos a iniciar y revisar causas de habilitación tardía. |
| Regla de lectura | Incluye pendientes en el denominador; excluye inicios posteriores al corte. No equivale a autorización de inicio si faltan otras condiciones. |

## K2 Tiempo de decisión de incorporación

| **Campo** | **Definición** |
| --- | --- |
| Objetivo | Medir la duración de la revisión una vez completo el expediente. |
| Fórmula | Mediana de (fecha de decisión de habilitación − fecha de expediente completo), expresada en días de 24 horas, de decisiones hasta el corte. |
| Fuente de datos | Eventos de expediente completo y habilitación; solo pares válidos del programa y periodo filtrados. |
| Frecuencia | Actualización diaria; revisión semanal. |
| Meta propuesta | ≤3 días. Menor es mejor. |
| Responsable | Coordinación de Prácticas. |
| Decisión que apoya | Reasignar revisión y examinar bloqueos cuando aumenta la demora. |
| Regla de lectura | No usa días hábiles. Mostrar tamaño de muestra y pendientes completos sin decisión; estos no tienen duración terminada y se informan aparte. |

# 15 Indicadores de horas y entregas

## K3 Cumplimiento de horas de sitio al corte

| **Campo** | **Definición** |
| --- | --- |
| Objetivo | Comparar el tiempo de sitio validado con el que debía cumplirse a la fecha. |
| Fórmula | 100 × suma de minutos de sitio validados al corte / suma de minutos de sitio previstos hasta el corte. |
| Fuente de datos | Agenda vigente e historial; registros de tiempo con categoría, fecha, minutos, estado y fecha de validación. |
| Frecuencia | Actualización diaria; seguimiento semanal. |
| Meta propuesta | ≥95 %. Mayor es mejor. |
| Responsable | Asesor, con validación del supervisor. |
| Decisión que apoya | Identificar rezagos de ejecución o validación y acordar ajustes autorizados. |
| Regla de lectura | Excluir asesoría, formación, pendientes y registros posteriores al corte. No limitar artificialmente a 100 %: un exceso exige revisar programación o duplicados. |

## K4 Entrega oportuna de informes

| **Campo** | **Definición** |
| --- | --- |
| Objetivo | Identificar si los informes se reciben dentro del plazo programado. |
| Fórmula | 100 × informes exigibles con primera entrega a más tardar en su vencimiento / informes con vencimiento hasta el corte. |
| Fuente de datos | Informe, agenda y primera versión enviada; fecha límite aprobada, fecha de primera entrega y periodo. |
| Frecuencia | Actualización diaria; análisis por corte académico. |
| Meta propuesta | ≥95 %. Mayor es mejor. |
| Responsable | Asesor y Coordinación de Prácticas. |
| Decisión que apoya | Contactar a quienes tienen entregas pendientes y revisar causas de retraso. |
| Regla de lectura | Los informes no enviados permanecen en el denominador. Entregar oportunamente no significa haber obtenido visto bueno o validación. |

# 15 Indicadores de validación y acompañamiento

## K5 Informes exigibles validados

| **Campo** | **Definición** |
| --- | --- |
| Objetivo | Medir cuánto del conjunto exigible ya completó la revisión académica. |
| Fórmula | 100 × informes exigibles cuya versión vigente está validada al corte / informes con vencimiento hasta el corte. |
| Fuente de datos | Informe, versiones y eventos de visto bueno y validación; reconstrucción del estado vigente al corte. |
| Frecuencia | Actualización diaria; revisión semanal y al cierre del corte. |
| Meta propuesta | ≥90 %. Mayor es mejor. |
| Responsable | Asesor. |
| Decisión que apoya | Priorizar revisión y correcciones; distinguir retraso de entrega y retraso de validación. |
| Regla de lectura | No basta una validación histórica de una versión superada. Debe interpretarse junto con K4 y la cantidad de informes pendientes. |

## K6 Cobertura de seguimiento reciente

| **Campo** | **Definición** |
| --- | --- |
| Objetivo | Identificar prácticas activas que cuentan con acompañamiento documentado reciente. |
| Fórmula | 100 × prácticas activas con al menos un seguimiento documentado en los últimos 14 días hasta el corte / prácticas activas al corte. |
| Fuente de datos | Práctica, vigencia de estado activo, actividad de seguimiento, responsable, fecha y evidencia de atención. |
| Frecuencia | Actualización diaria; revisión semanal. |
| Meta propuesta | ≥90 %. Mayor es mejor. |
| Responsable | Asesor; coordinación revisa cobertura. |
| Decisión que apoya | Programar contacto con prácticas sin seguimiento reciente y verificar disponibilidad de asesores. |
| Regla de lectura | La ventana de 14 días es propuesta del piloto, no una obligación inferida del reglamento. Cuenta prácticas distintas, no número de contactos. |

Reglas comunes: denominador cero o ausencia de observaciones válidas → N/D; redondeo a un decimal cuando sea necesario; zona horaria institucional UTC−05:00. Los datos faltantes se reportan como problemas de calidad, sin reemplazarlos por valores favorables.

# 16 Visualización de los indicadores

Figura 8. Tablero de la muestra ficticia al 18 de septiembre de 2026. Los resultados corresponden al cálculo ejecutado en la prueba de concepto.

Figura 8. Tablero de la muestra ficticia al 18 de septiembre de 2026. Los resultados corresponden al cálculo ejecutado en la prueba de concepto.

Las tarjetas muestran valor, base, meta y estado mediante texto, sin depender de colores. El usuario filtra programa y periodo, consulta fórmulas y revisa las filas de respaldo. Un filtro sin población muestra N/D en las seis tarjetas. El panel identifica el corte de la muestra para evitar confundirlo con información actual de la institución.

En el ejemplo, K2 cumple la meta propuesta; K1, K3, K4, K5 y K6 requieren revisión. Esto sirve para ilustrar decisiones, no para evaluar a CECAR. La pantalla reúne métricas complementarias: una entrega oportuna puede seguir sin validar, y una buena mediana puede coexistir con expedientes pendientes.

# 17 Riesgos, limitaciones y tratamiento

Se usa una escala cualitativa propuesta: probabilidad (P) e impacto (I), de 1 bajo a 3 alto. El producto P×I ayuda a ordenar atención; no es una probabilidad estadística. Los niveles residuales son estimaciones después de aplicar controles, todavía sin comprobar en operación.

| **Riesgo / P×I** | **Tratamiento y señal de alerta** | **Responsable / residual** |
| --- | --- | --- |
| Reglas ambiguas de horas, estados o cierre. 3×3=9. | Validar catálogo por programa, mantener versión y firma del acuerdo. Alerta: dos responsables resuelven distinto el mismo caso. | CP y Coordinación Académica / medio. |
| Acceso indebido a documentos o casos. 2×3=6. | Permisos por objeto, MFA privilegiado, revisión de asignaciones y registro de accesos. Alerta: consulta fuera del ámbito asignado. | TI y responsable de la ruta / medio. |
| Pérdida de base o archivos. 2×3=6. | Copias separadas y restauración conjunta probada. Alerta: copia fallida o referencia a archivo inexistente. | TI / medio. |
| Datos incompletos y KPI engañosos. 3×2=6. | Campos obligatorios, validación de fechas, N/D, población visible y muestra de conciliación. Alerta: caen registros sin una razón operativa. | CP y asesores / medio. |
| Baja adopción o doble registro. 3×2=6. | Pilotear con actores, acordar fuente oficial y formar por tareas. Alerta: evidencias relevantes siguen fuera del expediente. | CP y equipo del piloto / medio. |
| Falta de capacidad de operación. 2×3=6. | Nombrar operador, presupuestar soporte y comparar alojamiento. Alerta: no hay responsable de incidentes o actualizaciones. | TI y patrocinador / medio. |
| Integración de identidad no disponible. 2×2=4. | Inventariar acceso existente y probar OIDC antes del piloto. Alerta: ausencia de servicio o autorización de integración. | TI / bajo a medio. |
| Sobrecarga o revisiones simultáneas. 2×2=4. | Ensayo en PostgreSQL, control de revisión y carga representativa. Alerta: latencia sobre objetivo o conflictos frecuentes. | Equipo técnico / medio. |
| Aumento del alcance y costo. 3×2=6. | Priorizar flujo básico, aprobar cambios y medir esfuerzo real. Alerta: incorporación temprana de módulos ajenos al piloto. | CP y responsable del proyecto / medio. |

## Límites de la evidencia disponible

No se dispone de entrevistas, métricas históricas, inventario de aplicaciones, costos institucionales ni pruebas con usuarios reales. El AS-IS es documental; los problemas operativos son hipótesis verificables. El prototipo y la PoC son artefactos separados y no constituyen una aplicación integrada. La institución debe definir conservación, tratamiento y acceso a información antes de cargar datos reales.

# 18 Viabilidad y valor de la propuesta

La propuesta es viable como piloto condicionado a validar las reglas académicas y contar con operación institucional. El diagnóstico identifica intercambios de documentos, decisiones y registros que pueden organizarse alrededor de una práctica. La prueba local demuestra que algunos controles centrales pueden implementarse y verificarse; no demuestra todavía la viabilidad completa del despliegue.

| **Dimensión** | **Valoración y condición de avance** |
| --- | --- |
| Técnica | Favorable para continuar el diseño: se comprobaron permisos y flujo básicos en Django. Falta probar PostgreSQL, identidad, almacenamiento definitivo, recuperación y carga. |
| Operativa | Condicionada a acordar responsabilidades, excepciones, soporte y uso de un expediente común. Deben participar estudiantes, asesores, supervisores y coordinación. |
| Económica | Indeterminada en términos institucionales. Hay un escenario de esfuerzo y almacenamiento; falta cotización y línea base para valorar ahorro o retorno. |
| Académica | El diseño preserva revisión humana, visto bueno, evaluación y particularidades por programa. Las nuevas reglas de implementación requieren aprobación competente. |
| Información | El modelo separa evidencia académica y casos reservados. Permisos, retención, avisos de tratamiento y procedimientos de atención deben concretarse antes de operar. |

## Beneficios esperados y cómo comprobarlos

El expediente común permitiría localizar soportes y reconocer quién decidió sobre ellos. Las versiones reducirían ambigüedades entre entrega y aprobación; el registro por categorías permitiría revisar horas con una base consistente. El tablero facilitaría identificar pendientes y orientar acompañamiento. Son beneficios esperados: se confirmarían comparando indicadores y tiempos de tareas antes y durante el piloto, además de entrevistas breves de uso.

La contribución de e-business consiste en rediseñar intercambios entre universidad, estudiante y escenario externo para que la información útil acompañe las decisiones. Digitalizar archivos sin acordar responsabilidades, reglas de validación y fuentes de datos no alcanzaría ese resultado.

## Conclusión

Se recomienda avanzar con un piloto de alcance acotado, empezando por expediente, asignaciones y revisión de evidencias, seguido de horas, seguimiento e indicadores. El diseño conserva la intervención académica y hace comprobable el recorrido de la información. La expansión a más programas debe depender de resultados observados y de la capacidad de soporte, no únicamente de que la interfaz funcione.

# 18 Ruta de implementación y aceptación

La siguiente ruta es una estimación posterior a la aprobación institucional, distinta del calendario de entrega de esta actividad. Distribuye las 220 horas de esfuerzo del apartado 12 en seis semanas hipotéticas; puede cambiar según disponibilidad de los actores e infraestructura.

| **Semana / horas** | **Trabajo previsto** | **Resultado para decidir avance** |
| --- | --- | --- |
| 1 / 36 | Validar reglas, fuentes existentes y alcance; iniciar datos e identidad. | Acta de reglas y responsables; muestra anonimizada autorizada; inventario de sistemas. |
| 2 / 40 | Completar modelo e identidad; iniciar expediente y documentos. | Diseño aprobado y prueba de permisos en el entorno objetivo. |
| 3 / 40 | Completar revisiones y desarrollar registro de horas. | Flujo completo con versiones, visto bueno y trazabilidad. |
| 4 / 40 | Completar horas y seguimiento; implementar seis KPI; iniciar verificación. | Conciliación manual de indicadores y evidencia de acceso por ámbito. |
| 5 / 40 | Verificar seguridad, carga y recuperación; iniciar formación. | Incidencias críticas cerradas; restauración de base y archivos satisfactoria. |
| 6 / 24 | Formación restante, puesta en marcha y acompañamiento inicial. | Acta de aceptación del piloto y plan de revisión posterior. |

## Condiciones mínimas para iniciar con datos reales

| **Condición** | **Evidencia requerida** |
| --- | --- |
| Reglas y responsables confirmados | Acuerdo de programa sobre requisitos, categorías de horas, transiciones y excepciones. |
| Acceso e información controlados | Pruebas de autorización por objeto y caso; identidad configurada; retención y tratamiento definidos. |
| Continuidad y operación | Operador nombrado, presupuesto disponible y restauración verificada de base y documentos. |
| Datos e indicadores conciliados | Muestra revisada por el programa; seis KPI coincidentes y pendientes visibles. |
| Uso aceptado | Sesiones con actores; incidencias resueltas y plan de soporte. La meta de usabilidad de RNF10 debe comprobarse. |

Tras cuatro semanas de uso del piloto se propone revisar resultados, carga de trabajo y calidad de datos. La decisión de ampliar, corregir o detener debe quedar documentada con sus razones y acciones, incluyendo diferencias entre beneficios previstos y observados.

# Referencias documentales y técnicas

Las referencias \[L] y \[P] corresponden a los archivos suministrados para la actividad. Las páginas citadas son las páginas del PDF. Las fuentes técnicas se consultaron el 20 de septiembre de 2026; describen capacidades, mientras que puntajes, metas, costos ilustrativos y decisiones pertenecen a esta propuesta.

\[L] CECAR. Lineamientos de Práctica Profesional. Actualización 2026. Documento suministrado: Lineamientos de practica_ 20262.pdf.

\[P] Guía académica del proyecto final de E-business sobre transformación digital de las prácticas profesionales. Documento suministrado: Proyecto_Final_Corte_Transformacion_Digital_Practicas_Profesionales.pdf.

\[T1] Django Software Foundation. Using the Django authentication system, versión 5.2. https://docs.djangoproject.com/en/5.2/topics/auth/default/

\[T2] Django Software Foundation. Managing files, versión 5.2. https://docs.djangoproject.com/en/5.2/topics/files/

\[T3] Django Software Foundation. Writing custom django-admin commands. https://docs.djangoproject.com/en/5.2/howto/custom-management-commands/

\[T4] Laravel. Authorization, versión 12.x. https://laravel.com/framework/docs/12.x/authorization

\[T5] PostgreSQL Global Development Group. Constraints. https://www.postgresql.org/docs/current/ddl-constraints.html

\[T6] Oracle. MySQL 8.4 Reference Manual: FOREIGN KEY Constraints. https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html

\[T7] Amazon Web Services. Using versioning in S3 buckets. https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html

\[T8] Keycloak. OIDC layers. https://www.keycloak.org/securing-apps/oidc-layers

# Referencias técnicas y relación de anexos

\[T9] Django Software Foundation. Aggregation. https://docs.djangoproject.com/en/5.2/topics/db/aggregation/

\[T10] Metabase. Permissions overview. https://www.metabase.com/docs/latest/permissions/start

\[T11] Celery. Periodic tasks. https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html

\[T12] Django Software Foundation. Deployment checklist. https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

\[T13] Microsoft. Azure App Service overview. https://learn.microsoft.com/en-us/azure/app-service/overview

\[T14] Canonical. Install Apache2. https://ubuntu.com/server/docs/how-to/web-services/install-apache2/

\[T15] W3C. Web Content Accessibility Guidelines (WCAG) 2.2. https://www.w3.org/TR/WCAG22/

\[T16] Django Software Foundation. Download Django / Supported versions. https://www.djangoproject.com/download/

\[T17] PostgreSQL Global Development Group. Row Security Policies, versión 17. https://www.postgresql.org/docs/17/ddl-rowsecurity.html

## Anexos que acompañan el informe

Prototipo_Practicas_CECAR.html: demostración local. Carpeta diagramas: TO-BE, arquitectura y modelo conceptual. Carpeta capturas: pantallas verificadas. Carpeta poc: código, dependencias, datos ficticios y resultados del ensayo. verificacion_prototipo.json: verificación de interfaz. LEEME.txt: instrucciones de uso y reproducción.

# Apoyo para la sustentación

Guion sugerido de diez minutos, ajustable al tiempo que indique el docente. La distribución entre participantes es una propuesta de preparación; todos deben poder explicar el diagnóstico, las decisiones y los límites de la evidencia.

| **Participante / tiempo** | **Hilo de exposición y evidencia** |
| --- | --- |
| Eduardo Rafael de Avila Florez / 3 min | Explicar proceso y actores; mostrar AS-IS; relacionar las dificultades por verificar con la prioridad de expediente y evidencias. Aclarar que el diagnóstico es documental. |
| Julio Cesar Martinez / 3 min | Presentar TO-BE, requisitos y arquitectura. Defender Django, PostgreSQL e identidad centralizada con criterios y alternativas. Mostrar una corrección y su nueva revisión. |
| Alex Betin Uparela / 4 min | Recorrer el tablero y una fórmula; explicar los 20 resultados de PoC; cerrar con riesgos, costo ilustrativo y condiciones del piloto. |

## Preguntas que el equipo debe poder responder

| **Pregunta** | **Idea central para responder** |
| --- | --- |
| ¿Les entregaron una solución ya definida? | No. El caso y el proceso están delimitados; el equipo propone una solución después del diagnóstico y la evaluación de alternativas. |
| ¿Qué cambia frente al proceso descrito? | Las evidencias y decisiones quedan relacionadas con una práctica y una versión; se hacen visibles pendientes y bases de los indicadores. |
| ¿Por qué no basta una carpeta compartida? | Guardar archivos no asegura revisión por rol, secuencia de aprobación, validación de horas ni trazabilidad del indicador. |
| ¿Qué está comprobado? | Los controles incluidos en las 20 pruebas locales y siete recorridos de interfaz; los datos son ficticios. Integraciones, carga y aceptación institucional están pendientes. |
| ¿Cómo saben que mejorará el proceso? | Los beneficios son hipótesis razonadas. Se necesita línea base y comparación durante el piloto para afirmar una mejora medida. |
| ¿Por qué no automatizar toda decisión? | Habilitación, visto bueno, evaluación y novedades requieren competencia y juicio institucional; el sistema organiza y conserva evidencia. |

Para la demostración, abrir el HTML, recorrer Informes con Estudiante → Supervisor → Asesor y después mostrar Indicadores. Recargar restablece los datos. Tener el PDF y las capturas disponibles permite explicar el mismo recorrido si no se usa el prototipo en vivo.
