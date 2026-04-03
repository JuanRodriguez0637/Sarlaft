# Propiedades de PrefetchCount y MaxConcurrency en microservicios

> **Fuente Confluence:** [Propiedades de PrefetchCount y MaxConcurrency en microservicios](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3403874362/Propiedades+de+PrefetchCount+y+MaxConcurrency+en+microservicios)
> **Última modificación:** 2023-11-15 — Julián Andrés Curubo García · versión 6
> **Sección:** [Documentación Técnica](./index.md)

En esta sección se especifican los valores para las propiedades `prefetchCount` y `MaxConcurrency` a los que se llegó en busca de optimizar el flujo de sarlaft para el procesamiento masivo:

| # | Microservicio | Tipo | Descripción | Proyecto de configuración | PrefetchCount | MaxConcurrency | Instancias | RabbitMQ |
|---|---|---|---|---|---|---|---|---|
| 1 | `SarlaftAPI` | Microservicio | Microservicio encargado de las funciones principales de sarlaft, exponer servicios de api a otros aplicativos de negocio de Sura y el api a aplicaciones externas a Sura | [adm_y_fin-sarlaft-api-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-api-conf) | 20 | 20 | 3 |  |
| 2 | `SarlaftWebhook` | Microservicio | Microservicio encargado de decidir si una evaluacion de sarlaft debe ejecutar un callback al aplicativo cliente origen. | [adm_y_fin-sarlaft-sarlaft_callback-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-sarlaft_callback-conf) | 25 | 25 | 3 |  |
| 3 | `SarlaftEngine` | Microservicio | Microservicio que contiene las reglas de negocio según la norma de sarlaft 4.0, la ejecución de estas reglas se realiza con Drools. | [adm_y_fin-sarlaft-brms-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-brms-conf) | 60 | 60 | 3 |  |
| 4 | `Batch MI` | Microservicio Integrador | Microservicio encargado de recibir las solicitudes de evaluacion de sarlaft de aplicativos de negocio de sura que quieran un mecanismo de integracion de colas (rabbit mq) ideal para procesamientos masivos por ejemplo polizas colectivas | [892-sarlaft-function_batch-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_batch-conf) | 50 | 50 | 3 | [ver configuración](#configuracion-rabbitmq-batch-mi) |
| 5 | `P8 MI` | Microservicio Integrador | Microservicio que maneja las integraciones con el aplicativo de gestion documental P8, donde se suben documentos recibidos en sarlaft | [892-sarlaft-function_p8-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_p8-conf) | 10 | 10 | 3 |  |
| 6 | `Webhook MI` | Microservicio Integrador | Microservicio integrador que se encarga de enviar la notificacion de webhook (callback) al aplicativo de negocio cliente, se puede notificar a servicio web rest (con autenticacion con seus 4 o jwt) y por medio de rabbitmq | [892-sarlaft-function_webhook-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_webhook-conf) | 20 | 20 | 3 |  |
| 7 | `Requisitos MI` | Microservicio Integrador | Microservicio integrador con el aplicativo de requisitos de sura, el cual se encarga de crear, actualizar y eliminar requisitos de un cliente. | [892-sarlaft-function_requisitos-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_requisitos-conf) | 10 | 10 | 3 |  |
| 8 | `Identidad MI` | Microservicio Integrador | Microservicio integrador que permite establecer comunicación con el microservicio de validacion de identidad de Sura. El componente de validacion de identidad se comunica con el proveedor externo de Experian para realizar los proceso de: validacion de identificacion en registraduria nacional, consulta de informacion y validacion de identidad con OTP y preguntas reto | [892-sarlaft-function_identity-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_identity-conf) | 10 | 10 | 3 |  |
| 9 | `CCM MI` | Microservicio Integrador | Microservicio integrador encargado de enviar las comunicaciones a traves de CCM. | [892-sarlaft-function_ccm-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_ccm-conf) | 10 | 10 | 3 |  |

## Configuracion RabbitMQ Batch MI

Configuración del listener RabbitMQ para el microservicio `Batch MI`:

```yaml
listener:
  simple:
    prefetch: 1
    max-concurrency: 1
    acknowledge-mode: MANUAL
```
