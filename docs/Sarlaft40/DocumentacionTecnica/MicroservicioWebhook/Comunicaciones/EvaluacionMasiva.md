# Evaluación Masiva - Microservicio Webhook

> **Fuente Confluence:** [Evaluación Masiva - Microservicio Webhook](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2340126826/Evaluaci%C3%B3n+Masiva+-+Microservicio+Webhook)
> **Última modificación:** 2021-08-20 — erikson.sanchez (Unlicensed) · versión 2
> **Sección:** [Comunicaciones](./index.md)

Esta integración se realiza por medio del Event Bus al escuchar el comando ***`Assessment.process.evaluated`*** que se emite desde el ***sarlaftapi***, y que llega a la aplicación ***`sarlaftwebhook`*** esta integración al levantar el evento se encarga de consultar la evaluación y construir el objeto de Notificacion y envía un comando ***`Notification.sarlaft.evaluated`*** a la aplicación ***`webhook.`***

***`Assessment.process.evaluated`***

**Json Entrada:**

```json
{
    "codigoAplicacion": "9012",
    "solicitudesRecibidas": 1,
    "solicitudesExitosas": 1,
    "evaluaciones": [
        {
            "evaluacionId": "ae5d12a4-2377-4c0a-8189-abea1d60baba",
            "idNegocio": "0145451"
        }
    ]
}
```

```json
{
    "codigoAplicacion": "9012",
    "solicitudesRecibidas": 100,
    "solicitudesExitosas": 0,
    "errorValidaciones": "Se recibieron mas solicitudes de las permitidas(100)",
    "evaluaciones": []
}
```

```json
{
    "codigoAplicacion": "118",
    "solicitudesRecibidas": 3,
    "solicitudesExitosas": 2,
    "evaluaciones": [
        {
            "evaluacionId": "f531ded3-e672-4cfa-b435-0021c3df89c0",
            "idNegocio": "098"
        },
        {
            "evaluacionId": "212b0d59-8db0-4974-a790-084ef19d70c5",
            "idNegocio": "098"
        },
        {
            "evaluacionId": null,
            "mensajeError": "Informacion incompleta: RelacionPep",
            "idNegocio": "098"
        }
    ]
}
```

***`Notification.sarlaft.evaluated`***

**Json Salida:**

```json
{
    "codAplicacionDestino": "9012",
    "reencolamientos": 0,
    "codigoTransaccion": "0145451",
    "mensaje": {
        "negocios": [
            {
                "evaluacionId": "ae5d12a4-2377-4c0a-8189-abea1d60baba",
                "estado": "PENDIENTE",
                "idNegocio": "0145451",
                "url": "https://local.suranet.com/C41F19F1E8B6B3D72A664B056FDD03C9DAEB27C10D0BBC9F87B6C5700756E826",
                "figuras": [
                    {
                        "dni": "C21303620",
                        "estado": "PENDIENTE",
                        "fechaActualizacion": "2021-08-19T10:51:31.013-05:00",
                        "formularioRequerido": false,
                        "controles": [
                            {
                                "control": "GAFI",
                                "mensajeControl": "No es Gafi"
                            },
                            {
                                "control": "PEPS",
                                "mensajeControl": "Control PEPS"
                            },
                            {
                                "control": "DOCUMENT_PN",
                                "mensajeControl": "Pendiente por validacion de documento"
                            },
                            {
                                "control": "EXPERIAN",
                                "mensajeControl": "Pendiente por validacion de identidad"
                            },
                            {
                                "control": "RRCC",
                                "mensajeControl": "La consulta a RRCC fue Exitosa"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```