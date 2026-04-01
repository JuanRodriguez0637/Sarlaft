# Estados documento registraduria

> **Fuente Confluence:** [Estados documento registraduria](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3902537737)
> **Última modificación:** 2024-07-22 — Kelvin Alejandro López David - Ceiba Software (Unlicensed) · versión 1
> **Sección:** [Proceso Evaluación](./index.md)
## Tabla CodigoEstadoDocumentoRegistraduria

La tabla CodigoEstadoDocumentoRegistraduria define cómo interpretar los códigos de estado retornados por la Registraduría al validar un documento de identidad.

| Regla | Descripción | Estado |
| ------- | ------------- | -------- |
| <30 — códigos menores a 30 que **no** sean 0, 21 y 12 | CANCELADA | **FALLIDO** |
| >=30 y <=59 | NO_EXPEDIDA | **FALLIDO** |
| >=60 — códigos mayores a 60 que **no** sean 99 | INDEFINIDO | **FALLIDO** |
| Vacío o Null | FALLA TECNICA | **FALLA TECNICA** |
