# Servicio Consultar Estado Proceso Evaluación

> **Fuente Confluence:** [Servicio Consultar Estado Proceso Evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1813610856)
> **Última modificación:** 2021-03-26 — Diana Muñoz · versión 1
> **Sección:** [Servicios Web](./index.md)
- **Objetivo:** Permite consultar el estado del sarlaft de un cliente para un proceso de validación.
  Este servicio solo será para ciertos procesos de negocio, que sean validados y aprobados por el equipo de TI del aplicativo Sarlaft 4.0. De lo contrario se denegará su uso.
- **Endpoint:** /sarlaftserv/assessment/checkStatus
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

[`request_cheskstatus.json`](./ServicioConsultarEstadoProcesoEvaluacion/request_cheskstatus.json)

- **Dependencias:**
  - Base de Datos Saralft
