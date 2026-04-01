# Consulta Cliente RRCC

> **Fuente Confluence:** [Consulta Cliente RRCC](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1860862186/Consulta+Cliente+RRCC)
> **Última modificación:** 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 5
> **Sección:** [Microservicio - Cliente RRCC](./index.md)

**Objetivo**:

Conocer si un cliente este marcado como riesgo consultable, validando su dni y nombres/razón social.

**Comunicación: **Query
![SURA Documentacion-Page-3 (4).png](<./attachments/SURA Documentacion-Page-3 (4).png>)
**Descripción**:

Utilizando la librería de reactive commons, se escuchan las peticiones encoladas en la cola rrcc.query con el evento de nombre **Clients.client.validateRRCC**.

Se convierten los campos, siguiendo el manual del modelo de clientes para crear el request para consumir el servicio post *validarriesgosmodulos*, posteriormente, se convierte la respuesta del servicio y datos de mensajes de entrada para responder al evento de la cola.

**Mensaje de entrada:**

{

"tipoDocumento":"C",

"numeroDocumento":"1001234546",

"primerNombre" :"",

"segundoNombre" :"",

"primerApellido" :"",

"segundoApellido" :"",

"razonSocial" : ""

}

**Mensaje de salida:**

{

"tipoDocumento": "C",

"numeroDocumento": "1001234546",

"esRiesgo": false,

"tipoValidacion": “N”,

"mensaje": “”,

"idValidacion": "ff84d9d6-7389-4a4c-915c-46e60d679ad9"

}

**Mapeo entre datos:**

| documentType | Dato del cliente recibido en el mensaje de entrada |
| --- | --- |
| documentNumber | Dato del cliente recibido en el mensaje de entrada |
| isRisk | esRiesgo (Dato de response de servicio) |
| typeValidation | tipoValidacion (Dato de response de servicio) |
| message | mensajeValidacion (Dato de response de servicio) |
| idValidation | idRegistroValidacion (Dato de response de servicio) |

** Dependencias Ecosistema Sura:**

Url DLLO: [https://cotizadordllo.sura.com/regulacion/secureCommand/validarriesgosmodulos](https://cotizadordllo.sura.com/regulacion/secureCommand/validarriesgosmodulos)

Url LABO: [https://cotizadorlab.sura.com/regulacion/secureCommand/validarriesgosmodulos](https://cotizadorlab.sura.com/regulacion/secureCommand/validarriesgosmodulos)
