# Consultar clientes en fuentes de externas y actualizar base de datos de Sarlaft 4.0 - NoMasivo

> **Fuente Confluence:** [Consultar clientes en fuentes de externas y actualizar base de datos de Sarlaft 4.0 - NoMasivo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2719023220)
> **Última modificación:** 2022-05-23 — Diego Alejandro Vélez González · versión 7
> **Sección:** [Comunicaciones - Microservicio SarlaftClientes](./index.md)

Esta integración se realiza por medio del Service Bus al escuchar el comando `Clientes.informacion.completar` que llega de las aplicaciones ***sarlaftbatch*** y ***sarlaftapi***. En la integración se recibe una lista de documentos que corresponden a los clientes que serán consultados en fuentes de información externas (***WebApp Clientes PJ***, ***WebApp Clientes PN*** y ***WebApp Clientes***) y actualizados en la base de datos de Sarlaft 4.0. En caso que el campo `requiereRespuesta` es **true** se envía el comando `Clients.informacion.terminada` a la aplicación ***sarlaftbatch***.

**`Clientes.informacion.completar`**\
**Json Entrada:**

```json
{
   "aplicacionOrigen": {
      "nombreAplicacion": "sarlaftbatch",
      "comandoRespuesta": "Clients.informacion.terminada",
      "requiereRespuesta": true
   },
   "numeroTransaccion":"c476527c-9b11-40ad-8532-8986f3bb730b",
   "clientes":[
      {
         "tipoIdentificacion": "C",
         "nroIdentificacion": "15380765"
      },
      {
         "tipoIdentificacion": "C",
         "nroIdentificacion": "1040183675"
      }
   ]
}
```

Los campos `requiereRespuesta`, `numeroTransaccion`, `clientes` son obligatorios siempre. Los campos `nombreAplicacion`, `comandoRespuesta` solo son obligatorios si el campo `requiereRespuesta` es igual a **true**.

**`Clients.informacion.terminada`**\
**Json Salida:**

```json
{
   "numeroTransaccion": "c476527c-9b11-40ad-8532-8986f3bb730b",
   "clientes":[
      {
         "tipoIdentificacion": "C",
         "nroIdentificacion": "15380765"
      },
      {
         "tipoIdentificacion": "C",
         "nroIdentificacion": "1040183675"
      }
   ]
}
```

Los campos `numeroTransaccion` y `clientes` son obligatorios siempre.
