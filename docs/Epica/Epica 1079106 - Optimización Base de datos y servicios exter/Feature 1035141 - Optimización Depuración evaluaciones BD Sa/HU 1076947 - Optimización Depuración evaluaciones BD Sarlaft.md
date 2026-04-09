# HU 1076947 — [Optimización]: Depuración evaluaciones BD Sarlaft -  Implementación pipeline para el proceso de depuración de evaluaciones a eliminar Datafactory

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1035141 — [Optimización]: Depuración evaluaciones BD Sarlaft - Proceso automático](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141) › HU 1076947 — [Optimización]: Depuración evaluaciones BD Sarlaft -  Implementación pipeline para el proceso de depuración de evaluaciones a eliminar Datafactory

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1076947](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076947) |
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
    quiero Implementar un pipeline para el proceso de depuración de evaluaciones a eliminar, Debe recibir fechas para el rango de depuración. Que tome los identificadores de la nueva tabla de depuraciones,los elimine utilizando los Querys definidos en [Optimización]: Depuración evaluaciones BD Sarlaft - histórico (https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171)Apoyarse en este diseño con una agente de IA copilot. Tener en cuenta que posiblemente deban crearse varios pipelines para el proceso de eliminación, tener en cuenta el manejo de errores, relanzamiento, timeouts de las operaciones.Se recomienda tener eliminación por lotes o batch que eviten los timeouts de las operaciones en base de datos. Apoyarse con una agente de IA copilot

## Criterios de Aceptación

- Implementar un pipeline para el proceso de depuración de evaluaciones a eliminar, Debe recibir fechas para el rango de depuración. Que tome los identificadores de la nueva tabla de depuraciones, los elimine utilizando los Querys definidos en [Optimización]: Depuración evaluaciones BD Sarlaft - histórico (https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171)   
- Apoyarse en este diseño con una agente de IA copilot. Tener en cuenta que posiblemente deban crearse varios pipelines para el proceso de eliminación, tener en cuenta el manejo de errores, relanzamiento, timeouts de las operaciones. 
- Se recomienda tener eliminación por lotes o batch que eviten los timeouts de las operaciones en base de datos. Apoyarse con una agente de IA copilot
