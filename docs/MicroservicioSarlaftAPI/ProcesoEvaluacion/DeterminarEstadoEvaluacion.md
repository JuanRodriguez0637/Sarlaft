# Determinar Estado Evaluación

**Fuente Confluence:** [Determinar Estado Evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2332327941)  
**Sección:** [Proceso Evaluación](./index.md)

---

## Descripción

- **Objetivo:** Esta funcionalidad permite definir el estado de una evaluación el cual puede ser: FINALIZADO, FALLA TÉCNICA, RECHAZADO, PENDIENTE ACCION MANUAL y PENDIENTE.

- **Descripción:** Estos estados son definidos a partir de los estados internos de los Sarlaft que posee la evaluación, y cada Sarlaft tiene como posible alguno de los siguientes estados: RECHAZADO, PENDIENTE ACCIÓN MANUAL, FINALIZADO SIN CARGA, FINALIZADO y PENDIENTE.

  Para esta funcionalidad se creó un caso de uso llamado **determinar estado de evaluación**, el cual se llama al final del ciclo de la evaluación y durante la validación de las evidencias (antes de validar requisitos).

  De igual forma, el caso de uso se permite utilizar para ser consumido por un entry point async query handler (espera el mensaje: `"Evaluation.status.calculate"`), el cual espera del microservicio Webhook un objeto de tipo JSON con el id de la evaluación a la que se le quiere determinar su estado. Se hace previamente una consulta de la evaluación por id y de ahí se pasa por el flujo completo del caso de uso de Determinar Estado Evaluación.

  Una vez se tiene la evaluación con su estado, se hace una conversión a un objeto respuesta para el SarlaftWebhook, que debe contener el id de la evaluación y su estado.

- **Endpoint:** `/sarlaftserv/assessment`

- **Perfil de Seus4:** `PF_CONSUMSERVSARLAFTAPI`

## Adjuntos de Ejemplo

- `EjemploDeterminarEstadoEvaluacionApi.json` — Ejemplo JSON Request SarlaftApi
- `EjemploDeterminarEstadoEvaluacionWebhook.json` — Ejemplo JSON Request SarlaftWebhook (mensaje RabbitMQ)
- `EjemploDeterminarEstadoEvaluacionWebhookResponse.json` — Ejemplo JSON Response SarlaftWebhook

> Los archivos JSON anteriores están adjuntos en la página de Confluence.

## Dependencias

- Base de Datos Sarlaft
- Aplicaciones Externas
- RabbitMQ
- SarlaftWebhook

## Diagrama

![Diagrama servicio Determinar Estado Evaluación](./img/Evaluacion_Actividades-Page-19.jpg)

> Diagrama de servicio que representa el consumo y respuesta del query handler.
