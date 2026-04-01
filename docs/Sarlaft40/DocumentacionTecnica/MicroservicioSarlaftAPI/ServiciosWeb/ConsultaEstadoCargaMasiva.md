# Consulta Estado Carga Masiva

> **Fuente Confluence:** [Consulta Estado Carga Masiva](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2365948348)
> **Última modificación:** 2021-09-02 — juan camilo muñoz burgos (Unlicensed) · versión 2
> **Sección:** [Servicios Web](./index.md)
- **Objetivo:** Permite consultar el estado de procesamiento de la carga masiva de información del conocimiento del cliente que se envió por medio de una plantilla de excel.
- **Endpoint:** /sarlaftserv/file/getStatus
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

[`Request.json`](./ConsultaEstadoCargaMasiva/Request.json)

- **Ejemplo Response:** Si el proceso esta en estado RECIBIDO o INICIADO: Devuelve un http 202, con un header de retry-after; En caso tal el proceso este en estado FINALIZADO Devuelve un http 302, con un header de location del ws.
- **Dependencias:**
  - Cache Redis
