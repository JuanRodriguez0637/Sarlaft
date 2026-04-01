# Query consulta Cliente PEPS

>**Fuente:**[Ver en Confluence](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1864597599)
>**Fecha extracción:**2026-03-27

## Archivos Adjuntos

  [exists] image-20210527-123947.png
  [exists] SURA Documentacion-Page-2 (2).png
  [exists] SURA Documentacion-Page-2 (6).png

- [image-20210527-123947.png](../imagenes/image-20210527-123947.png)
- [SURA Documentacion-Page-2 (2).png](../imagenes/SURA Documentacion-Page-2 (2).png)
- [SURA Documentacion-Page-2 (6).png](../imagenes/SURA Documentacion-Page-2 (6).png)

---

**Objetivo**:

Conocer si un cliente está marcado como peps validando su dni.

**Comunicación:**Query

**Descripción**:

Escucha continuamente las peticiones encoladas en la cola peps.query con el evento de nombre**Clients.client.validatePEP**.

Con el mensaje de entrada se realiza la consulta con el cliente web y se convierten los datos al mensaje de salida correspondiente para responder al query.

**Mensaje de Entrada:**

{

            "tipoDocumento":"A",

            "numeroDocumento":"9009270423",

}

**Mensaje de Salida:**

{

                        "tipoDocumento":"A",

                        "numeroDocumento":"9009270423",

                        "isPEP":"",

                        "mensaje":"",

                        "solicitudes":""

}

**Mapeo de los campos de respuesta con los del mensaje de salida:**

||

tipoDocumento

||

Dato del cliente recibido en el mensaje de entrada

||
||

numeroDocumento

||

Dato del cliente recibido en el mensaje de entrada

||
||

isPEP

||

pep

||
||

mensaje

||

message

||
||

solicitudes

||

request

||

**Dependencias Ecosistema Sura:**

**Url DLLO:**

[https://segvol.dllosura.com/pepsserv/pep/check](https://segvol.dllosura.com/pepsserv/pep/check)

**Url LABO:**

[https://segvol.labsura.com/pepsserv/pep/check](https://segvol.labsura.com/pepsserv/pep/check)
