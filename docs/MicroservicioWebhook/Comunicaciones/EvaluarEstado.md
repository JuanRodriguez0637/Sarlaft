# Evaluar Estado - Microservicio Webhook

> **Fuente Confluence:** [Evaluar Estado - Microservicio Webhook](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2314010785/Evaluar+Estado+-+Microservicio+Webhook)
> **Última modificación:** 2022-05-12 — juan camilo muñoz burgos · versión 3
> **Sección:** [Comunicaciones](./index.md)

Esta integración se realiza por medio del Event Bus al escuchar el comando `Assessment.define.status`, que llega a la aplicación `sarlaftwebhook` esta integración al levantar el evento se encarga de consultar el calculo de la evaluación y envía un comando `Notification.sarlaft.finished` a la aplicacion `webhook`.

`Assessment.define.status`

**Ejemplo Json Entrada:**

```json
{
    "evaluacionId": "59a242c7-d3b5-439e-9d49-20f8068171d6",
    "codigoAplicacion": "SEL"
}
```

`Notification.sarlaft.finished`

**Ejemplo Json Salida:**

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
