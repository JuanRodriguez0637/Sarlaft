# HU 1076922 — [Optimización]: Depuración evaluaciones BD Sarlaft - Diseño inicial Pipelines Datafactory

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1035141 — [Optimización]: Depuración evaluaciones BD Sarlaft - Proceso automático](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141) › HU 1076922 — [Optimización]: Depuración evaluaciones BD Sarlaft - Diseño inicial Pipelines Datafactory

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1076922](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076922) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-03-16 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1035141 — [Optimización]: Depuración evaluaciones BD Sarlaft - Proceso automático](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141)  
  Estado: New  

## Descripción

Como Analista SARLAFT
  quiero que se diseñe un pipeline para el proceso de consulta e identificación de evaluaciones a eliminar. Debe recibir fechas para el rango de depuración. La idea es que se utilice el query de la HU [Optimización]: Depuración evaluaciones BD Sarlaft - histórico(https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171 ). Los ids de evaluaciones candidatos a depurar de la db, se dejen en una nueva tabla del modelo de sarlaft: columnas idEvaluacion, fechaCreacion, estadoEvaluacionDiseñar un pipeline para el proceso de depuracion de evaluaciones a eliminar, Debe recibir fechas para el rango de depuracion. Que tome los identificadores de la nueva tabla de depuraciones,los elimine utilizando los Querys definidos en [Optimización]: Depuración evaluaciones BD Sarlaft - histórico (https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171)Apoyarse en este diseño con una agente de IA copilot. Tener en cuenta que posiblemente deban crearse varios pipelines para el proceso de eliminación, tener en cuenta el manejo de errores, relanzamiento, timeouts de las operaciones.Se recomienda tener eliminación por lotes o batch que eviten los timeouts de las operaciones en base de datos.

## Criterios de Aceptación

**CA1 — El pipeline debe recibir fechas para el rango de depuración (consulta e identificación)** 
- El pipeline permite ingresar fecha inicial y fecha final como parámetros obligatorios. 
- El pipeline ejecuta el query definido en la HU “Optimización: Depuración evaluaciones BD Sarlaft – histórico” usando el rango de fechas recibido. 
- El pipeline identifica correctamente los IDs de evaluaciones candidatas a depurar según el query mencionado.  **CA2 — Los evaluadores identificados deben insertarse en una nueva tabla** 
- El pipeline almacena los evaluadores candidatos en la nueva tabla del modelo SARLAFT con las tres columnas especificadas:

- **idEvaluacion** 
- **fechaCreacion** 
- **estadoEvaluacion**   
- La tabla debe contener exclusivamente los registros retornados por el query para el rango solicitado. 
- El pipeline debe registrar la inserción sin realizar eliminación aún (solo identificación).  **CA3 — Debe diseñarse un segundo pipeline para el proceso de depuración (eliminación)** 
- El pipeline recibe fecha inicial y fecha final como parámetros obligatorios para el rango de depuración. 
- El pipeline consulta los IDs en la tabla creada en el proceso de identificación. 
- El pipeline utiliza los queries definidos en la HU “Optimización: Depuración evaluaciones BD Sarlaft – histórico” para realizar la eliminación. 
- El pipeline elimina únicamente los registros cuyos IDs se encuentren en la tabla de depuración.  **CA4 — Uso del agente de IA Copilot para apoyar el diseño** 
- Se debe evidenciar el uso de un agente IA Copilot para apoyar el diseño de los pipelines. 
- La evidencia debe incluir:

- consultas realizadas, 
- recomendaciones aplicadas, 
- elementos del diseño generados o ajustados con IA.    **CA5 — Considerar la creación de varios pipelines (si aplica)** 
- El diseño debe contemplar explícitamente la posibilidad de dividir el proceso en varios pipelines si es necesario por:

- estructura, 
- cargas, 
- límites, 
- u optimización de tiempos.    

 **CA6 — Manejo de errores, relanzamiento y timeouts** 
- El diseño del pipeline debe incluir manejo de errores durante:

- ejecución de consultas, 
- inserción en la tabla, 
- eliminación de registros.   
- El pipeline debe permitir relanzamiento en caso de fallas. 
- Se debe manejar explícitamente el riesgo de timeouts, tal como se menciona en la historia. 
- El diseño debe incluir lógica o controles que mitiguen el impacto de timeouts.  **CA7 — Eliminación por lotes o batch (recomendación obligatoria de diseño)** 
- El diseño de eliminación debe considerar y documentar la estrategia de ejecución por lotes/batches. 
- Se debe evidenciar cómo la eliminación por lotes mitiga los timeouts en base de datos. 
- Si la eliminación se realiza efectivamente en batch, debe quedar reflejado en el pipeline.
