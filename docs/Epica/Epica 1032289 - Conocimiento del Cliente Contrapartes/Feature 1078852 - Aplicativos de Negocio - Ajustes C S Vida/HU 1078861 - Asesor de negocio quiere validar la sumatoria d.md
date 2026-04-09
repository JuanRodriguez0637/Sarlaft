# HU 1078861 — [Asesor de negocio] quiere validar la sumatoria de porcentajes de beneficiarios para garantizar coherencia en la asignación

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078861 — [Asesor de negocio] quiere validar la sumatoria de porcentajes de beneficiarios para garantizar coherencia en la asignación

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078861](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078861) |
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

Como **asesor de negocio**

Quiero que el sistema valide que la **sumatoria de porcentajes** asignados a beneficiarios sea **100%**

Para garantizar una distribución válida y evitar inconsistencias operativas.

## Criterios de Aceptación

- Dado que registro beneficiarios, cuando asigno porcentajes, entonces el sistema valida que la suma sea exactamente 100%. 
- Dado que la sumatoria es diferente a 100%, cuando intento guardar, entonces el sistema bloquea el guardado y muestra mensaje de validación. 
- Dado que la sumatoria es 100%, cuando confirmo, entonces el sistema permite continuar.
