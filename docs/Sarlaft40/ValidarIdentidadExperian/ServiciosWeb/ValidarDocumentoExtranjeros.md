---
title: "Validar documento de identidad de extranjeros"
confluence_id: 2915205707
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2915205707"
last_modified: "2022-09-26"
author: "juan camilo muñoz burgos"
version: 1
---

# Validar documento de identidad de extranjeros

> **Fuente Confluence:** [Validar documento de identidad de extranjeros](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2915205707)
> **Última modificación:** 2022-09-26 — juan camilo muñoz burgos · versión 1
> **Sección:** [Servicios Web](./index.md)

- **Objetivo:** Permite evaluar la veracidad del documento de identidad de los extranjeros.
- **Endpoint:** `/api/v1/registry/validate`
- **Ejemplo Request:**

📎 [Request.json](./attachments/Request.json)

**Tipos Documentos permitidos:**

**CÉDULA DE EXTRANJERÍA (E), PERMISO ESPECIAL DE PERMANENCIA (TE) Y PERMISO POR PROTECCIÓN TEMPORAL (TT)**

- **Ejemplo Response:**

📎 [Response.json](./attachments/Response.json)

El valor `codigoSeguridad`: `"NA"` fue homologado a "NA" (No aplica) ya que en la respuesta recibida por experian el código de seguridad para este servicio es null.

- **Dependencias:**
  - Experian.
  - Azure Cache Redis.
