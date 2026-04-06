# Simplificar arquitectura de comunicación en proceso webhook - propuesta de cambio

> **Fuente Confluence:** [Simplificar arquitectura de comunicación en proceso webhook - propuesta de cambio](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3737911299)
> **Última modificación:** 2024-05-17 — Julián Andrés Curubo García · versión 9
> **Sección:** [Diseño Funcionalidades](../index.md)

Este artículo tiene como propósito simplificar la actual arquitectura de comunicación del proceso de webhook en el aplicativo Sarlaft 4.0 tras una propuesta de eliminación del microservicio `sarlaftwebhook` en el proceso webhook que se maneja actualmente en Sarlaft 4.0. A continuación se expone como se encuentra el proceso de comunicación actual y dos propuestas de posibles soluciones con las que se puede abarcar el tema de la eliminación del microservicio `salraftwebhook`:

📎 [SimplificarArquitecturaWebhookEnSarlaft4.pdf](./attachments/SimplificarArquitecturaWebhookEnSarlaft4.pdf)
📎 [SimplificarArquitecturaComunicacionWebhook.drawio](./attachments/SimplificarArquitecturaComunicacionWebhook.drawio)
📎 [DiagramaDeLaArquitecturaActualDelProcesoWebhookEnSarlaft4.docx](./attachments/DiagramaDeLaArquitecturaActualDelProcesoWebhookEnSarlaft4.docx)

## Páginas

| Página | Enlace |
| -------- | -------- |
| Diagrama de la arquitectura actual del proceso webhook en Sarlaft 4.0 | [DiagramaDeLaArquitecturaActualDelProcesoWebhookEnSarlaft40.md](./DiagramaDeLaArquitecturaActualDelProcesoWebhookEnSarlaft40.md) |
| Propuesta 1 - Omitir la comunicación que pasa por Azure Service Bus | [Propuesta1OmitirLaComunicacionQuePasaPorAzureServiceBus.md](./Propuesta1OmitirLaComunicacionQuePasaPorAzureServiceBus.md) |
| Propuesta 2 - Mantener la comunicación por el Azure Service Bus | [Propuesta2MantenerLaComunicacionPorElAzureServiceBus.md](./Propuesta2MantenerLaComunicacionPorElAzureServiceBus.md) |
| Conclusiones para simplificar la arquitectura del proceso webhook en Sarlaft 4.0 | [ConclusionesParaSimplificarLaArquitecturaDelProcesoWebhookEnSarlaft40.md](./ConclusionesParaSimplificarLaArquitecturaDelProcesoWebhookEnSarlaft40.md) |
