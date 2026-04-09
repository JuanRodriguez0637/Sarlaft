# HU 1078883 — [Usuario del sistema] quiere recibir mensajes informativos claros sobre la definición de beneficiarios para evitar errores operativos

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078883 — [Usuario del sistema] quiere recibir mensajes informativos claros sobre la definición de beneficiarios para evitar errores operativos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078883](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078883) |
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

Como **usuario del sistema (asesor/gestor)**

Quiero mensajes informativos claros cuando no se registren beneficiarios

Para entender implicaciones y reducir errores operativos.

## Criterios de Aceptación

- Dado que se expide póliza sin beneficiarios, cuando finaliza el proceso, entonces se muestra mensaje: “beneficiarios se definirán en reclamación” (según regla). 
- Dado que el usuario continúa sin información mínima, cuando el sistema lo permite, entonces informa la condición y su implicación. 
- Dado que luego se registran beneficiarios estructurados, cuando se consulta/actualiza, entonces no se muestran mensajes contradictorios.
