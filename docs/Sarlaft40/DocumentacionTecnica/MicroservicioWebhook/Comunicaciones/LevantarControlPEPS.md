# Levantar Control PEPS - Microservicio Webhook

> **Fuente Confluence:** [Levantar Control PEPS - Microservicio Webhook](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2314240187/Levantar+Control+PEPS+-+Microservicio+Webhook)
> **Última modificación:** 2021-08-09 — erikson.sanchez (Unlicensed) · versión 2
> **Sección:** [Comunicaciones](./index.md)

Esta integración se realiza por medio del Event Bus al escuchar el comando ***`Clients.clientpeps.enabled`***, que llega a la aplicación ***`sarlaftwebhook`*** esta integración al levantar el evento se encarga de registrar la evidencia PEP y se encarga de consultar el calculo de la evaluación en el que se encuentre el sarlaft para el cual se inserto la evidencia PEP y si ó solo si la Evaluacion se dio con un estado que entra en **FINALIZADO**, **FINALIZADOS SIN CARGA**, ó **PENDIENTE_ACCION_MANUAL**, se envía un comando ***`Notification.sarlaft.finished`*** a la aplicacion ***`webhook.`***

***`Clients.clientpeps.enabled`***

**Json Entrada:**

```json
{
    "dni": "C43988152",
    "ramo": "COR",
    "operacion": "07",
    "suboperacion": "14",
    "figura": "T",
    "cdOficina": "016",
    "cdAsesor": "4999",
    "feInicio": "1622491161895",
    "feFin": "1623355161895",
    "nroSolicitud": "2282"
}
```

***`Notification.sarlaft.finished`***

**Json Salida:**

```json
{
    "codAplicacionDestino": "9012",
    "mensaje": {
        "evaluacionId": "212b0d59-8db0-4974-a790-084ef19d70c5",
        "estado": "PENDIENTE",
        "idNegocio": "0007518269",
        "figuras": [
            {
                "dni": "C43988152",
                "estado": "PENDIENTE",
                "controles": [
                    {
                        "control": "GAFI",
                        "mensajeControl": "Notification GAFI"
                    },
                    {
                        "control": "RRCC",
                        "mensajeControl": "Notification RRCC"
                    },
                    {
                        "control": "IDENTITY",
                        "mensajeControl": "Notification IDENTITY"
                    },
                    {
                        "control": "PEPS",
                        "mensajeControl": "Notification PEP's"
                    }
                ]
            }
        ]
    }
}
```