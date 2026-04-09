# HU 1078869 — [Analista de vida grupo] quiere evaluar beneficiarios ingresados masivamente para mitigar riesgos SARLAFT sin afectar la expedición

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1078852 — [Aplicativos de Negocio] - Ajustes C/S Vida y Cotizador Rentas](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078852) › HU 1078869 — [Analista de vida grupo] quiere evaluar beneficiarios ingresados masivamente para mitigar riesgos SARLAFT sin afectar la expedición

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1078869](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078869) |
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

Como **analista de vida grupo**

Quiero que los beneficiarios ingresados por **cargas masivas** se evalúen posteriormente en **batch**

Para mitigar riesgos SARLAFT sin frenar la expedición inicial.

## Criterios de Aceptación

- Dado que se realiza una carga masiva, cuando se procesa, entonces la información queda disponible para evaluación posterior. 
- Dado que se ejecuta evaluación batch, cuando se detectan alertas SARLAFT, entonces se generan insumos para monitoreo/acciones. 
- Dado que la póliza fue expedida, cuando corre el batch, entonces no afecta la vigencia inicial.
