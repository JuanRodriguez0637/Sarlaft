# HU 1076945 — [Optimización]: Depuración evaluaciones BD Sarlaft -  Implementación pipeline de consulta Datafactory

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1035141 — [Optimización]: Depuración evaluaciones BD Sarlaft - Proceso automático](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141) › HU 1076945 — [Optimización]: Depuración evaluaciones BD Sarlaft -  Implementación pipeline de consulta Datafactory

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1076945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076945) |
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
   quiero implementar un pipeline para el proceso de consulta e identificación de evaluaciones a eliminar. Debe recibir fechas para el rango de depuración. La idea es que se utilice el query de la HU [Optimización]: Depuración evaluaciones BD Sarlaft - histórico(https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171 ). Los ids de evaluaciones candidatos a depurar de la db, se dejen en una nueva tabla del modelo de sarlaft: columnas idEvaluacion, fechaCreacion, estadoEvaluacion

## Criterios de Aceptación

- Implementar un pipeline para el proceso de consulta e identificación de evaluaciones a eliminar.  
- Debe recibir fechas para el rango de depuración. La idea es que se utilice el query de la HU [Optimización]: Depuración evaluaciones BD Sarlaft - histórico https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171. 
- Los ids de evaluaciones candidatos a depurar de la db, se dejen en una nueva tabla del modelo de sarlaft: columnas idEvaluacion, fechaCreacion, estadoEvaluacion
