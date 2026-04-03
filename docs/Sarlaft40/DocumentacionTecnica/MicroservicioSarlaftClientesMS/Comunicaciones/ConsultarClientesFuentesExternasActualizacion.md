# Consultar clientes en fuentes de externas (Proceso de actualización)

> **Fuente Confluence:** [Consultar clientes en fuentes de externas (Proceso de actualización)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2873163781)
> **Última modificación:** 2022-08-25 — Diego Alejandro Vélez González · versión 3
> **Sección:** [Comunicaciones - Microservicio SarlaftClientes](./index.md)

Esta integración se realiza por medio del Service Bus al escuchar el query **Proceso.actualizacion.autocompletar** que llega de la aplicación _**sarlaftbatch**_. En la integración se recibe el documento que corresponde al cliente que será consultado en fuentes de información externas (_**WebApp Clientes PJ, WebApp Clientes PN y WebApp Clientes**_) y para el cual se responderá dicha información.

_**Proceso.actualizacion.autocompletar**_

**Json Entrada:**

```json
{
    "tipoIdentificacion": "C",
    "nroIdentificacion": "15380765"
    "fechaExpedicion": "2008-10-15T00:00:00.000+00:00"
}
```

**Json Salida:**

```json
{
    "infoContacto": {
        "celular": "3102345670",
        "correo": "ANDRES.GOMEZ@SOFKA.COM.CO"
    },
    "infoFinanciera": {
        "ingresos": "2500000",
        "gastos": "1300000",
        "actividadEconomica": "N7210",
        "codigoOcupacion": "04",
    },
    "direcciones": [
        {
            "id": ""1c85cc80-00a4-43a0-9471-8eef354bb18f""
            "tipo": "RS",
            "pais": "170",
            "departamento": "05",
            "ciudad": "4292",
            "descricionDireccion": "1088 Junkins Avenue",
            "nroIdentificacion": "15380765",
            "fechaCreacion": "2008-10-15T00:00:00.000+00:00",
            "ultimaActualizacion": "2008-10-15T00:00:00.000+00:00"
        }
    ]
}
```
