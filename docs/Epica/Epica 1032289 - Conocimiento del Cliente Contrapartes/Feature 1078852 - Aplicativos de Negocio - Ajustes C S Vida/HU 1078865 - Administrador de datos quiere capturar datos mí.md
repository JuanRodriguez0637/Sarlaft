# HU 1078865 — [Administrador de datos] quiere capturar datos mínimos obligatorios de beneficiarios para fortalecer el monitoreo SARLAFT

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078865 — [Administrador de datos] quiere capturar datos mínimos obligatorios de beneficiarios para fortalecer el monitoreo SARLAFT

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078865](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078865) |
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

Como **administrador de datos**

Quiero que en el ingreso/actualización de beneficiarios se capturen **datos mínimos SARLAFT**

Para mejorar calidad, habilitar monitoreo y responder a auditoría/regulación.

## Criterios de Aceptación

- Dado que registro/actualizo beneficiario persona natural, cuando diligencio, entonces el sistema solicita país de nacimiento y fecha de nacimiento. 
- Dado que registro beneficiario persona jurídica, cuando diligencio, entonces el sistema solicita fecha de constitución. 
- Dado que guardo la información, cuando se consulta desde cliente-servidor/core/GW, entonces los campos están almacenados y visibles.
