# MicroServicio Integración Webhook

> **Fuente Confluence:** [MicroServicio Integración Webhook](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2183561226/MicroServicio+Integraci%C3%B3n+Webhook)
> **Última modificación:** 2022-06-08 — juan camilo muñoz burgos (Unlicensed) · versión 3
> **Sección:** [MicroServicio Azure - Webhook](./index.md)

**Objetivo:** Notificar a un aplicativo que el proceso de saralft de un cliente ha terminado

**Comunicación:**

**Descripción**:

EL Azure MicroServicio se ejecuta con un evento disparador de tipo timer, que permite escuchar las peticiones encoladas en la cola rrcc.query con los eventos de nombre Notification.sarlaft.finished y Notification.sarlaft.evaluated, cada minuto.

Se convierten los campos, siguiendo la historia de usuario para consultar la base de datos y obtener información del tipo de notificación (Rest o cola). Posteriormente, se procede a consumir servicio Post o Enviar a la cola indicada en la información de la base de datos y se transforma el resultado de la transacción para enviar comando **Notification.sarlaft.delivered **a SarlaftApi.

**Notification.sarlaft.finished:**

**Mensaje de entrada:**

{

"codAplicacionDestino" : "",

"mensaje" : {

"evaluacionId": "",

"estado": "",

"idNegocio" : "",

"figuras": [

{

"dni": "",

"estado": "",

"controles": [

{

"control": "",

"mensajeControl": ""

}

]

}

]

}

}

**Mensaje de salida:**

{

"codAplicacionDestino" : "",

"evaluacionId": "",

"codigoTransaccion" : "",

“entregado” : “”,

“mensajeError” : “”

}

**Mapeo entre datos:**

| codAplicacionDestino | Dato del cliente recibido en el mensaje de entrada |
| --- | --- |
| evaluacionId | Dato del cliente recibido en el mensaje de entrada |
| codigoTransaccion | “” (Vacío para este comando) |
| entregado | true: transacción exitosa; false: fallo en la transacción |
| mensajeError | Mensaje indicando finalización de transacción |

** **

**Notification.sarlaft.evaluated:**

**Mensaje de entrada:**

{

"codAplicacionDestino" : "",

"reencolamientos" : 0,

"codigoTransaccion" : "",

"mensaje" : {

"negocios": [{

"evaluacionId": "",

"estado": "",

"idNegocio" : "",

"url": "",

"figuras": [

{

"dni": "",

"estado": "",

"fechaActualizacion": "",

"formularioRequerido": "",

"controles": [

{

"control": "",

"mensajeControl": ""

}

]

}

],

"mensajeError": ""

}],

"mensajeError": ""

}

}

**Mensaje de salida:**

{

"codAplicacionDestino" : "",

"evaluacionId": "",

"codigoTransaccion" : "",

“entregado” : “”,

“mensajeError” : “”

}

**Mapeo entre datos:**

| codAplicacionDestino | Dato del cliente recibido en el mensaje de entrada |
| --- | --- |
| evaluacionId | “" (Vacío en este comando) |
| codigoTransaccion | Dato del cliente recibido en el mensaje de entrada |
| entregado | true: transacción exitosa; false: fallo en la transacción |
| mensajeError | Mensaje indicando finalización de transacción |

** Dependencias:**

- RabbitMQ de Sura
- Servicios Rest que se encuentren parametrizados en el aplicativo de sarlaft para webhook
