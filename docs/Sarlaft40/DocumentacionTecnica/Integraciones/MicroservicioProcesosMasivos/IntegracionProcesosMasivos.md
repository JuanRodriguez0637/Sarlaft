# Integración de procesos Masivos

> **Fuente Confluence:** [Integración de procesos Masivos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2105933932/Integraci%C3%B3n+de+procesos+Masivos)
> **Última modificación:** 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 7
> **Sección:** [Microservicio - Procesos Masivos](./index.md)

**Objetivo**:

Recibir la solicitud de evaluación de sarlaft de forma masiva.

**Comunicación: **
![SURA Documentacion-Page-3 (6).png](<./attachments/SURA Documentacion-Page-3 (6).png>)
**Descripción**:

El proyecto tiene un listener configurado para escuchar la cola seguros.sarlaft.assessment, de la conexión configurada en el archivo application.yaml.

La notificación recibida luego se envía usando la librería Reactive Commons, como un comando para que escuche la aplicación sarlaftapi.

**Mensaje de entrada desde RabbitMQ Sura:**

El json completo del campo **solicitudEvaluacion**, se puede ver en

[**https://sarlaftapi.dllosura.com/sarlaftserv/documentation/swagger-ui/index.html?configUrl=/sarlaftserv/api-docs/swagger-config#/crear-evaluacion-service/createNew**](https://sarlaftapi.dllosura.com/sarlaftserv/documentation/swagger-ui/index.html?configUrl=/sarlaftserv/api-docs/swagger-config#/crear-evaluacion-service/createNew)

{

"numeroMensaje": "1",

"solicitudEvaluacion": [

{

"solicitudDni": "C990199",

"codigoOperacion": "01",

"codigoAplicacion": "118",

"negocioId": "0145451",

"tomador": {

"cliente": {

"tipoPersona": "N",

"correo": "[mail_1@mail.com.co](mailto:mail_1@mail.com.co)",

"celular": "3102345670",

"razonSocial": null,

"documento": {

"tipo": "C",

"numero": "990199",

"fechaExpedicion": "2007-05-27"

},

"persona": {

"primerNombre": "Nestor",

"segundoNombre": "Fernando",

"primerApellido": "Arevalo",

"segundoApellido": "Espitia",

"pais": "01"

},

"relaciones": [

]

}

},

"asegurados": [

],

"beneficiarios": [

],

"polizas": [

{

"codigoRamo": "1",

"codigoProducto": "1",

"codigoCanal": "1",

"valorAsegurado": 500000,

"valorPrima": 500000,

"medioPago": "PSE",

"negocio": "COLECTIVO",

"coaseguro": false,

"codigoOficina": "00"

}

]

}

]

}

**Mensaje de salida en comando hacia Sarlaft API:**

{

"numeroMensaje": "1",

"solicitudEvaluacion": [

{

"solicitudDni": "C990199",

"codigoOperacion": "01",

"codigoAplicacion": "118",

"negocioId": "0145451",

"tomador": {

"cliente": {

"tipoPersona": "N",

"correo": "[mail_1@mail.com.co](mailto:mail_1@mail.com.co)",

"celular": "3102345670",

"razonSocial": null,

"documento": {

"tipo": "C",

"numero": "990199",

"fechaExpedicion": "2007-05-27"

},

"persona": {

"primerNombre": "Nestor",

"segundoNombre": "Fernando",

"primerApellido": "Arevalo",

"segundoApellido": "Espitia",

"pais": "01"

},

"relaciones": [

]

}

},

"asegurados": [

],

"beneficiarios": [

],

"polizas": [

{

"codigoRamo": "1",

"codigoProducto": "1",

"codigoCanal": "1",

"valorAsegurado": 500000,

"valorPrima": 500000,

"medioPago": "PSE",

"negocio": "COLECTIVO",

"coaseguro": false,

"codigoOficina": "00"

}

]

}

]

}

**Dependencias Ecosistema Sura:**

**Mensaje Origen en RabbitMQSura:**

**Usuario de Conexión: **`seguros.sarlaftmsv.usr`

**URL RabbitMQ DLLO: **[**msgdllo.suramericana.com.co**](http://msgdllo.suramericana.com.co:15672/)

**URL RabbitMQ LABO: **[**msglab.suramericana.com.co**](http://msglab.suramericana.com.co:15672/)

**Queue RabbitMQ: **`seguros.sarlaft.assessment`
