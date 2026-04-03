---
title: "Comunicación P8 Flujo externo de Validación de Identidad"
confluence_id: 2625700076
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2625700076"
last_modified: "2022-02-25"
author: "juan camilo muñoz burgos"
version: 2
---

# Comunicación P8 Flujo externo de Validación de Identidad

> **Fuente Confluence:** [Comunicación P8 Flujo externo de Validación de Identidad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2625700076)
> **Última modificación:** 2022-02-25 — juan camilo muñoz burgos · versión 2
> **Sección:** [Validar identidad por cargue de soporte a P8](./index.md)

- **Objetivo:** Esta funcionalidad permite lanzar un mensaje a la función `appp8` de Services Bus a partir del cargue del documento soporte al azure storage account, para el flujo externo de validación de identidad.
- **Descripción:** Una vez el documento es cargado a azure storage account, se procede a construir el mensaje que será lanzado a la cola de mensajes mediante la función **appp8**. a través del comando `Documents.identity.p8.upload`
- **Ejemplo Json Request:**

📎 [MensajeAppp8.json](./attachments/MensajeAppp8.json)

**Dependencias:**

- Aplicaciones Externas.
- Services Bus Azure.

A continuación, se muestra el diagrama de servicio que permite representar el flujo de la construcción del mensaje y su envío.
