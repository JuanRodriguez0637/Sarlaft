# HU 1077081 — [Notificación en la reclamación]: Orquestador de notificaciones

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1049126 — [Aplicativos de negocio]: Notificar en la reclamación el Formulario con estado pendiente](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1049126) › HU 1077081 — [Notificación en la reclamación]: Orquestador de notificaciones

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1077081](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077081) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-16 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1049126 — [Aplicativos de negocio]: Notificar en la reclamación el Formulario con estado pendiente](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1049126)  
  Estado: New  

## Descripción

Orquestador que consulta formularios pendientes y delega actividades de evaluación y publicación. Consulta en bd los clientes con formularios en estado "Pendiente" Agrupa por client_id Para cada cliente único: Busca en la tabla de registro de notificaciones Si NO existe: crea registro nuevo Si YA existe: delega al motor de reglas

## Criterios de Aceptación

Orquestador que consulta formularios pendientes y delega actividades de evaluación y publicación. Consulta en bd los clientes con formularios en estado "Pendiente" Agrupa por client_id Para cada cliente único: Busca en la tabla de registro de notificaciones Si NO existe: crea registro nuevo Si YA existe: delega al motor de reglas
