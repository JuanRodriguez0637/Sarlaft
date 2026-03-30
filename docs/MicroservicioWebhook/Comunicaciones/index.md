# Comunicaciones - Microservicio Webhook

> **Fuente Confluence:** [Comunicaciones - Microservicio Webhook](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2314469525/Comunicaciones+-+Microservicio+Webhook)
> **Última modificación:** 2021-08-20 — erikson.sanchez · versión 3
> **Sección:** [Microservicio Webhook](../index.md)

El microservicio de Webhook se encargar de operaciones intermedias sobre Evaluaciones que se estén procesando en el sarlaftapi.

Actualmente se procesan dos operaciones:

1. Levantar control PEPs.
2. Evaluar estado.
3. Evaluación Masiva

## Páginas de esta sección

| Página | Descripción | Última modificación |
|--------|-------------|---------------------|
| [Levantar Control PEPS](./LevantarControlPEPS.md) | Integración vía Event Bus con comando `Clients.clientpeps.enabled` | 2021-08-09 |
| [Evaluar Estado](./EvaluarEstado.md) | Integración vía Event Bus con comando `Assessment.define.status` | 2022-05-12 |
| [Evaluación Masiva](./EvaluacionMasiva.md) | Integración vía Event Bus con comando `Assessment.process.evaluated` | 2021-08-20 |
