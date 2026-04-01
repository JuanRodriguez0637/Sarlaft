# Servicio Consulta de Clientes

> **Fuente Confluence:** [Servicio Consulta de Clientes](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1856536990)
> **Última modificación:** 2022-03-30 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 2
> **Sección:** [Servicios Web](./index.md)
- **Objetivo:** Permite consultar los datos básicos de un cliente en el modelo de base de datos del sarlaft y en el modelo de clientes de suramericana, obteniendo con prioridad los datos encontrados en el modelo de sura, dado que el gobierno de dicha información se encuentra en su repositorio.
- **Endpoint:** /sarlaftserv/client/get
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

[`request_getClient.json`](./ServicioConsultaClientes/request_getClient.json)

- **Dependencias:**
  - Base de Datos Saralft
  - Consulta en el modelo de Sura en Salesforce - Mensajería
