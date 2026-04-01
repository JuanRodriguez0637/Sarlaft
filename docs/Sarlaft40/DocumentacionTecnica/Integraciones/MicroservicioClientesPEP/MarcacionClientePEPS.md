# Marcación Cliente PEPS

> **Fuente Confluence:** [Marcación Cliente PEPS](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2197815411/Marcaci%C3%B3n+Cliente+PEPS)
> **Última modificación:** 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 5
> **Sección:** [Microservicio - Clientes PEP](./index.md)

**Objetivo**:

Marcar un cliente como pep.

**Comunicación:**
![SURA Documentacion-Page-2 (3).png](<./attachments/SURA Documentacion-Page-2 (3).png>)
**Descripción**:

Utilizando la librería de reactive commons, la integración escucha los comandos encolados en la cola ***peps*** con el evento de nombre **Clients.client.markPEP**. Con el mensaje de entrada se realiza la consulta con el cliente web y se convierten los datos al mensaje de salida correspondiente para responder por medio de otro comando hacia sarlaftAPI con el nombre** Clients.clientpeps.marked**

Nota: internamente la función utiliza los patrones Circuit Braker y Retry para consumir el microservicio peps.

**Mensaje de entrada en comando hacía peps:**

{

"tipoDocumento": "A",

"numeroDocumento": "9009270423",

"dniSolicitante": "",

"primerNombre": "",

"segundoNombre": "",

"primerApellido": "",

"segundoApellido": ""

}

**Mensaje de salida en comando hacia Sarlaft API:**

{

"resultado": true/false,

"mensajeError": ""

}

**Mapeo de los campos de entrada con los datos del request del servicio**

| tipoDocumento | documentType |
| --- | --- |
| numeroDocumento | documentNumber |
| primerNombre | firstName |
| segundoNombre | secondName |
| primerApellido | firstSurname |
| segundoApellido | secondSurname |
| dniSolicitante | requestDni |
| Codigo de aplicación parametrizado en la función. | application |

**Dependencias Ecosistema Sura:**

**Url DLLO:**

[http://segvol.dllosura.com/pepsserv/pep/](https://segvol.dllosura.com/pepsserv/pep/check)mark

**Url LABO:**

[https://segvol.labsura.com/pepsserv/pep/](https://segvol.labsura.com/pepsserv/pep/check)mark
