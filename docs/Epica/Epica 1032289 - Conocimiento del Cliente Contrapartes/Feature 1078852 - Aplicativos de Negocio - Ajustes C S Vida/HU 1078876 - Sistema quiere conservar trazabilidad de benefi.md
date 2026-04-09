# HU 1078876 — [Sistema] quiere conservar trazabilidad de beneficiarios históricos para garantizar control y auditoría SARLAFT

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078876 — [Sistema] quiere conservar trazabilidad de beneficiarios históricos para garantizar control y auditoría SARLAFT

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078876](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078876) |
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

Como **sistema de gestión de pólizas**

Quiero conservar trazabilidad de beneficiarios históricos (de esquemas anteriores)

Para control/auditoría SARLAFT, sin permitir uso operativo futuro.

## Criterios de Aceptación

- Dado que una póliza tiene beneficiarios históricos como texto, cuando se consulta, entonces se visualiza solo como informativo y no editable. 
- Dado que se registran nuevos beneficiarios estructurados, cuando se guarda, entonces el histórico queda inactivo para efectos operativos. 
- Dado que se requiere auditoría, cuando se consulta la póliza, entonces existe evidencia de cambios en beneficiarios.
