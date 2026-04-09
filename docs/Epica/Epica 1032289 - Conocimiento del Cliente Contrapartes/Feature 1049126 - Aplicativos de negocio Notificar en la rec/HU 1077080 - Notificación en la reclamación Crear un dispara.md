# HU 1077080 — [Notificación en la reclamación]: Crear un disparador programado

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1049126 — [Aplicativos de negocio]: Notificar en la reclamación el Formulario con estado pendiente](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1049126) › HU 1077080 — [Notificación en la reclamación]: Crear un disparador programado

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1077080](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077080) |
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

Se ejecuta cada lunes a las 8:00 AM (UTC-5) Consulta tabla día hábiles para validar que es día hábil Si NO es día hábil: busca el siguiente día hábil en la misma semana Si es día hábil: invoca al "orquestador de notificaciones" Registra en BD el inicio de ejecución

## Criterios de Aceptación

Se ejecuta cada lunes a las 8:00 AM (UTC-5) Consulta tabla día hábiles para validar que es día hábil Si NO es día hábil: busca el siguiente día hábil en la misma semana Si es día hábil: invoca al "orquestador de notificaciones" Registra en BD el inicio de ejecución
