# HU 1073547 — Bloquear los pagos cuando el sarlarft es rechazado

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1073128 — [Reclamaciones]: Conexión con Cleims Center](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1073128) › HU 1073547 — Bloquear los pagos cuando el sarlarft es rechazado

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1073547](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1073547) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-11 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1073128 — [Reclamaciones]: Conexión con Cleims Center](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1073128)  
  Estado: New  

## Descripción

Se debe bloquear en el aplicativo (que no viaje a SAP) el pago cuando el estado de Sarlaft es rechazado, por la causas de listas vinculantes y estado del documento de identidad (Fallecido y cancelado). 
 En Sarlaft se encuentra del estado del documento

## Criterios de Aceptación

- Bloquear el pago en el aplicativo cuando el beneficiario del pago esta marcado en listas de control y tiene un estado del documento diferente al vigente (fallecido, cancelados e inactivos) . A los 30 días se podrá cambiar a exitoso siempre y cuando desde el equipo de LAFT nos confirmen si es posible el pago. Los 30 días empiezan a contar desde el día que se entrega el ultimo documento. 
- Los casos de rechazos diferentes hay que mostrar los errores para que se corrijan , como por ejemplo, error en el apellido que se puede corregir, o el numero de contacto es decir datos errados o ID no existe, si se debe permitir el pago - Validar si realmente debe ser 30 días.
