# Consultar clientes en fuentes de externas y actualizar base de datos de Sarlaft 4.0 - NoMasivo

> **Fuente Confluence:** [Consultar clientes en fuentes de externas y actualizar base de datos de Sarlaft 4.0 - NoMasivo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2719023220)
> **Última modificación:** 2022-05-23 · versión 7
> **Sección:** [Comunicaciones - Microservicio SarlaftClientes](./index.md)

Esta integración se realiza por medio del Service Bus al escuchar el comando **Clientes.informacion.completar** que llega de las aplicaciones _**sarlaftbatch y sarlaftapi**_. En la integración se recibe una lista de documentos que corresponden a los clientes que serán consultados en fuentes de información externas(_**WebApp Clientes PJ, WebApp Clientes PN y WebApp Clientes**_) y actualizados en la base de datos de Sarlaft 4.0. En caso que el campo **requiereRespuesta **es **true** se envía el comando **Clients.informacion.terminada **a** **la aplicación _**sarlaftbatch**_.

_**Clientes.informacion.completar**_
**Json Entrada:**

```text
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
```text

Los campos _**requiereRespuesta,  numeroTransaccion, clientes **_son obligatorios siempre. Los campos _**nombreAplicacion, comandoRespuesta **_solo son obligatorios si el campo _**requiereRespuesta**_ es igual a **true.**

_**Clients.informacion.terminada**_
**Json Salida:**

```text
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

Los campos _**numeroTransaccion **_y_** clientes **_son obligatorios siempre.
