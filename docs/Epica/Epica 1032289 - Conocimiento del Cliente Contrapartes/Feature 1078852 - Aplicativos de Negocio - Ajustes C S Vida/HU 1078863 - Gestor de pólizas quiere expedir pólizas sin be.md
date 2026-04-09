# HU 1078863 — [Gestor de pólizas] quiere expedir pólizas sin beneficiarios cuando no se cuenta con información mínima para no frenar el negocio

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078863 — [Gestor de pólizas] quiere expedir pólizas sin beneficiarios cuando no se cuenta con información mínima para no frenar el negocio

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078863](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078863) |
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

Como **gestor de pólizas**

Quiero que el sistema permita **expedir pólizas sin beneficiarios** cuando el cliente no tenga información mínima

Para evitar bloquear la expedición y dejar la definición para la reclamación según regla acordada.

## Criterios de Aceptación

- Dado que el cliente no tiene información mínima de beneficiarios, cuando se expide la póliza, entonces el sistema permite continuar sin exigir beneficiarios. 
- Dado que se expide sin beneficiarios, cuando se consulta la póliza, entonces queda registrado que se definirán en reclamación. 
- Dado que hoy el campo es obligatorio, cuando aplica la condición de ausencia de datos mínimos, entonces la obligatoriedad no bloquea el proceso.
