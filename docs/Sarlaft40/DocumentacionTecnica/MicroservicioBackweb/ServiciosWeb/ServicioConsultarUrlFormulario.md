# Servicio Consultar url de formulario.

> **Fuente Confluence:** [Servicio Consultar url de formulario.](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2659942401)
> **Última modificación:** 2022-08-29 — Diego Alejandro Vélez González · versión 3
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite consultar la URL del formulario.

- **Endpoint:** `/sarlaftbackweb/consultar/url/formulario`

- **Perfil de Seus4:** `PF_SARLAFTADMCON`

- **Ejemplo Json Request:**

```json
{
    "idEvaluacion": "203e747d-5ff0-4f08-bbc1-143a2f7c2bbd"
}
```

- **Ejemplo Json Response:**

```text
https://local.suranet.com/E91D07080E234378DF865BAF52ECD90B7FB210803412C34B34ADDE4393BBFAEF/bce887d1-34b4-4e5d-9e75-0e1deb7f5805/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJTYXJsYWZ0Iiwic3ViIjoiU0FSTEFGVCIsImlzcyI6IlN1cmEuY29tIiwiZXhwIjoxNjQ4NDk4NDE0LCJpYXQiOjE2NDgwNjY0MTR9.7xdN0MSdhG9D_0BuVDbWg5ZdzLcWGNRhWrXM-c_A0M0
```

**Nota:** Para código Operación distinto de Reclamaciones y Actualización, se genera la url del formulario en base al sarlaft del tomador, en caso contrario se genera en base al reclamante o la a actualizar.

- **Dependencias:**
  - Base de datos de sarlaft.
