# HU 1078862 — [Sistema] quiere manejar de forma diferenciada beneficiarios onerosos y no onerosos para cumplir reglas contractuales

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078862 — [Sistema] quiere manejar de forma diferenciada beneficiarios onerosos y no onerosos para cumplir reglas contractuales

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078862](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078862) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-17 |
| **Última modificación** | 2026-03-17 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852)  
  Estado: New  

## Descripción

Como **sistema de expedición de pólizas**

Quiero diferenciar el comportamiento para beneficiarios **onerosos** y **no onerosos**

Para garantizar cumplimiento contractual, generación correcta de carátula y estandarización de información.

## Criterios de Aceptación

- Dado que el beneficiario es oneroso, cuando se registra, entonces se carga automáticamente el texto estándar y no es editable. 
- Dado que el beneficiario no es oneroso, cuando se gestiona la información, entonces no existe campo de texto libre para beneficiarios. 
- Dado que se expide póliza con beneficiario oneroso, cuando se genera la carátula, entonces se refleja el texto estándar definido.
