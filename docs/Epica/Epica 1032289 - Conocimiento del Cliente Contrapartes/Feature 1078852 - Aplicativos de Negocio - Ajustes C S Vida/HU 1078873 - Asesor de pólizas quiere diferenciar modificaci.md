# HU 1078873 — [Asesor de pólizas] quiere diferenciar modificaciones valorables y no valorables para gestionar correctamente los beneficiarios

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078873 — [Asesor de pólizas] quiere diferenciar modificaciones valorables y no valorables para gestionar correctamente los beneficiarios

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078873](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078873) |
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

Como **asesor de pólizas**

Quiero diferenciar reglas para modificaciones **valorables** y **no valorables** sobre beneficiarios

Para aplicar conservación/eliminación/actualización correcta y evitar inconsistencias.

## Criterios de Aceptación

- Dado que realizo modificación valorable, cuando consulto beneficiarios, entonces el histórico se muestra informativo y no editable. 
- Dado que realizo modificación no valorable de beneficiarios, cuando actualizo, entonces puedo registrar beneficiarios estructurados con datos requeridos. 
- Dado que existían beneficiarios como texto, cuando guardo modificación no valorable, entonces el texto anterior se elimina y quedan beneficiarios estructurados.
