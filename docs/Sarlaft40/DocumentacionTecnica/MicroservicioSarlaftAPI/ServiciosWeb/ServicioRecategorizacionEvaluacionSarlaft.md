# Servicio Recategorización Evaluación Sarlaft

> **Fuente Confluence:** [Servicio Recategorización Evaluación Sarlaft](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2476834835)
> **Última modificación:** 2022-08-10 — juan camilo muñoz burgos (Unlicensed) · versión 4
> **Sección:** [Servicios Web](./index.md)
- **Objetivo:** Permite realizar la recategorización de una evaluación sarlaft al momento de responder a las preguntas: `¿El tomador es una Persona Expuesta Políticamente? o ¿Alguno de los administradores (representantes legales, miembros de la Junta Directiva) o socio con una participación superior al 5% de la Persona Jurídica es una Persona Expuesta Políticamente (PEP)?`

- **Endpoint:** /sarlaftserv/assessment/recategorize
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

[`Request.json`](./ServicioRecategorizacionEvaluacionSarlaft/Request.json) | [`response.json`](./ServicioRecategorizacionEvaluacionSarlaft/response.json) | [`Request-1.json`](./ServicioRecategorizacionEvaluacionSarlaft/Request-1.json) | [`RequestConCampoLicitacionPublica.json`](./ServicioRecategorizacionEvaluacionSarlaft/RequestConCampoLicitacionPublica.json)

- **Dependencias:**
  - Base de Datos Saralft
  - Motor de Reglas - API
  - Cache Redis
