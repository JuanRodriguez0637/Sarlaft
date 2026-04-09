# HU 1078893 — [Administrador de sistemas] quiere sincronizar en línea las actualizaciones de beneficiarios entre canales y core para asegurar consistencia SARLAFT

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078893 — [Administrador de sistemas] quiere sincronizar en línea las actualizaciones de beneficiarios entre canales y core para asegurar consistencia SARLAFT

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078893](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078893) |
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

Como **administrador de sistemas**

Quiero sincronizar actualizaciones de beneficiarios entre **cliente-servidor, core y GW** (negocio nuevo y modificaciones)

Para consistencia, trazabilidad y disponibilidad de datos SARLAFT.

## Criterios de Aceptación

- Dado que registro/actualizo beneficiarios en un canal habilitado, cuando guardo, entonces se reflejan cambios en sistemas destino y se pueden consultar. 
- Dado que existen campos SARLAFT asociados, cuando sincroniza, entonces los campos viajan/almacenan/visualizan sin pérdida. 
- Dado que la actualización fue por modificación (no solo negocio nuevo), cuando consulto desde otro sistema/canal, entonces se ve la última información.
