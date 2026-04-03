# 7. Webhook (Assessment)

> **Fuente Confluence:** [7. Webhook (Assessment)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3222994946)
> **Última modificación:** 2023-06-14 — Diana Muñoz · versión 5
> **Sección:** [Diseño Funcionalidades](./index.md)

## Webhook Finalización:

Este mecanismo permite comunicar al aplicativo que envió la solicitud de crear evaluación el resultado de la misma. Se realiza notificación webhook cuando la evaluación queda en los siguientes estados:

| Estado | Descripción |
|---|---|
| `FINALIZADO` | La evaluación ha cumplido todos los pasos: validaciones, formulario, requisitos. Por estar finalizado el negocio puede expedirse. |
| `RECHAZADO` | Alguna de las validaciones dejo una evidencia en estado FALLIDO y de esta forma la evaluación es rechazada. Por estar rechazado el negocio no puede expedirse. |
| `PENDIENTE_ACCION_MANUAL` | Estado que aplica solo para la aplicación del cotizador (6919) cuando el único pendiente de la evaluación es la validación de identidad del tomador. Por estar en este estado no se puede aun expedir el negocio, el aplicativo del cotizador (6919) debe completar la evaluación de identidad y adjuntar la evidencia a Sarlaft 4.0 |
| `FINALIZADO_EXCEPCION` | Es un estado especial para cuando un sarlaft finaliza sin diligenciar formulario, aplica para ciertos negocios que constituyen excepción en las reglas de negocio de Sarlaft 4.0. Por estar finalizado el negocio puede expedirse. |
| `FINALIZADO_SIN_CARGA` | La evaluación ha cumplido todos los pasos: validaciones, formulario, requisitos. Algunos requisitos pudiesen haberse adjuntado pero no se han subido al gestor documental P8. Por estar finalizado el negocio puede expedirse. |

Existen dos tipos de comunicación de webhook, cada aplicativo puede elegir aquel que sea acorde a su arquitectura.

### Mecanismo QUEUE:

En la tabla `tsaf_consumidor` se parametriza **QUEUE** para el código de aplicación y el `cdtipo_evento` **FINALIZACION**. El mensaje siempre se publica en el exchange **`seguros.sarlaft.finalizacion`** con el binding parametrizado en el campo `dsbinding`.

![Webhook Finalización - Mecanismo QUEUE](./attachments/Sarlaft_Laura-WebhookFinalizacion1.jpg)

### Mecanismo REST:

En la tabla `tsaf_consumidor` se parametriza **REST** para el código de aplicación y el `cdtipo_evento` **FINALIZACION**. El mensaje siempre se envía al servicio rest parametrizado en el campo `dsruta_servicio` utilizando el campo `dspropiedades` para la autenticación

Se soportan solo dos tipos de autenticación Seus 4 y token JWT.

![Webhook Finalización - Mecanismo REST](./attachments/Sarlaft_Laura-WebhookFinalizacion2.jpg)

Documentación mensaje webhook: [Descripción de Interfaces Principales](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070150/Descripci+n+de+Interfaces+Principales)

## Webhook Evaluación:

Este mecanismo permite comunicar al aplicativo que envió la solicitud de crear evaluación, por medio de un mecanismo masivo, el resultado inicial de la evaluación, en comparación es decir como si el resultado fuera del servicio web de assessment.

Se puede hacer el webhook por QUEUE o por REST parametrizado para el tipo de evento EVALUACION (`cdtipo_evento`)

![Webhook Evaluación](./attachments/Sarlaft_Laura-WebhookFinalizacion3.jpg)

Descripción integración masiva [Interfaz Procesos Masivos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070163/Interfaz+Procesos+Masivos)
