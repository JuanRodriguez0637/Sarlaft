# Comunicaciones - Microservicio Webhook

> **Fuente Confluence:** [Comunicaciones - Microservicio Webhook](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2314469525/Comunicaciones+-+Microservicio+Webhook)
> **Última modificación:** 2021-08-20 — erikson.sanchez (Unlicensed) · versión 3
> **Sección:** [Microservicio Webhook](../index.md)

El microservicio de Webhook se encargar de operaciones intermedias sobre Evaluaciones que se estén procesando en el sarlaftapi.

Actualmente se procesan dos operaciones:

1. Levantar control PEPs.
2. Evaluar estado.
3. Evaluación Masiva

## Páginas hijas

| Página | Descripción | Última modificación |
|--------|-------------|---------------------|
| [Levantar Control PEPS](./LevantarControlPEPS.md) | Integración por Event Bus para registrar evidencia PEP | 2021-08-09 — erikson.sanchez |
| [Evaluar Estado](./EvaluarEstado.md) | Integración por Event Bus para consultar cálculo de evaluación | 2022-05-12 — juan camilo muñoz burgos |
| [Evaluación Masiva](./EvaluacionMasiva.md) | Integración por Event Bus para evaluaciones masivas | 2021-08-20 — erikson.sanchez |