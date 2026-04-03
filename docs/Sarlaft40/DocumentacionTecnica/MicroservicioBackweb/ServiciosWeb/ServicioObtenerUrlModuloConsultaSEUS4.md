# Servicio para obtener URL Modulo consulta (SEUS 4)

> **Fuente Confluence:** [Servicio para obtener URL Modulo consulta (SEUS 4)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2836725968)
> **Última modificación:** 2022-08-01 · versión 1
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite obtener url para módulo de consulta indicando el código de asesor y código de aplicación.

- **Endpoint:** `/sarlaftbackweb/getUrlByToken`

- **Perfil de Seus4:** `PF_ASESOR_ASIST_VIRTUAL`

- **Ejemplo Json Request:**

```json
{
   "codAsesor": "1234",
   "codAplicacion": "01"
}
```

- **Ejemplo Json Response:**

```json
{
    "url": "https://local.suranet.com/admsarlaft/inicio/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJTYXJsYWZ0Iiwic3ViIjoiMDEiLCJjb2RBcGxpY2FjaW9uIjoiMDEiLCJpc3MiOiJTdXJhLmNvbSIsImNvZEFzZXNvciI6IjEyMzQiLCJleHAiOjE2NTk4MDE2NjYsImlhdCI6MTY1OTM2OTY2Nn0.f-X2EZMGutA0m79FxLN5IkC2LmGjBkt5b2jZVuYhwUc"
}
```
