# Microservicio Webhook

> **Fuente Confluence:** [Microservicio Webhook](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2314207324/Microservicio+Webhook)
> **Última modificación:** 2024-07-12 — Kelvin Alejandro López David - Ceiba Software (Unlicensed) · versión 4
> **Sección:** Documentación Técnica

Los siguiente documentos buscan dar referencias de los cambios efectuados en los microservicios que de webhoook del sistema de sarlaft los cuales fueron modificados con el fin de realizar el ajuste en el json de notificación y respuesta REST o Queue para incluir los códigos de errores de la evidencia de `document_pn`.

[HISTORIA_WEBHOOK_AUDITORIA.pdf](./attachments/HISTORIA_WEBHOOK_AUDITORIA.pdf)

[HISTORIA_WEBHOOK.pdf](./attachments/HISTORIA_WEBHOOK.pdf)

Links asociados a la estructura de webhook.

- [7. Webhook (Assessment)](../DisenoArquitectura/DisenoFuncionalidades/07WebhookAssessment.md)
- [Estructura Proyecto - MicroServicio Webhook](./EstructuraProyecto.md)

Se agrega diagrama de clases basado en los microservicios de webhook llamadas `sarlaft_callback-ms` y `sarlaft-function_webhook-mi`.

`sarlaft_callback-ms`.

![webhook.Callback-20240507-155301.png](./attachments/webhook.Callback-20240507-155301.png)

`sarlaft-function_webhook-mi`.

![WEBHOOK_FUNCTIONS-20240507-182617.png](./attachments/WEBHOOK_FUNCTIONS-20240507-182617.png)

## Páginas hijas

| Página | Descripción | Última modificación |
|--------|-------------|---------------------|
| [Diseño Arquitectura](./DisenoArquitectura.md) | Diagrama de interacción de componentes en Sarlaft Webhook | 2021-08-09 — erikson.sanchez |
| [Estructura Proyecto](./EstructuraProyecto.md) | Estructura del proyecto basado en arquitectura hexagonal | 2022-01-04 — Diana Muñoz |
| [Configuración Ambiente](./ConfiguracionAmbiente.md) | Requisitos, repositorios y configuración de perfiles | 2025-10-30 — Diana Muñoz |
| [Comunicaciones](./Comunicaciones/index.md) | Operaciones intermedias sobre evaluaciones (PEPS, Estado, Masiva) | 2021-08-20 — erikson.sanchez |
| [Webhook Log de Errores en Splunk](./WebhookLogErroresSplunk.md) | Implementación de envío de logs a Splunk | 2021-09-13 — juan camilo muñoz burgos |
| [Configuración HealthCheck](./ConfiguracionHealthCheck.md) | HealthCheck con librería actuator para sarlaftwebhook | 2024-03-11 — Julián Andrés Curubo García |
| [Webhook - Sarlaft](./WebhookSarlaft.md) | Cambios en webhook, diagramas de clases y diccionario | 2024-07-16 — Brayan Estiven Sepúlveda Quintero |
