# Integración Reclamaciones - CCM

> **Fuente Confluence:** [Integración Reclamaciones - CCM](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2360508537/Integraci%C3%B3n+Reclamaciones+-+CCM)
> **Última modificación:** 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 7
> **Sección:** [Microservicio - CCM](./index.md)

**Objetivo**:

Enviar a CCM a través de una mensaje de RabbitMQ el información necesaria para el envió de la NOTIFICACIÓN PARA PROCESOS DE VINCULACIÓN Y RECLAMACIONES.

**Comunicación:**
![SURA Documentacion-Page-3 (9).png](<./attachments/SURA Documentacion-Page-3 (9).png>)
**Diagrama de flujo de la funcionalidad**:
![FuncionCCMActivacionVinculacion-Diagrama de flujo (2).png](<./attachments/FuncionCCMActivacionVinculacion-Diagrama de flujo (2).png>)
**Descripción**:

El microservicio utiliza reactive commons para escuchar continuamente los comandos encolados en la cola ccm con el evento de nombre **CCM.Notification.Reclamation**.

Se convierten los campos, siguiendo el manual de integración CCM y se verifica si el mensaje de salida generado contiene los campos obligatorios siguiendo las reglas de negocio.

Si se cumplen todas las validaciones de los campos obligatorios, se publica el mensaje de salida usando la conexión a rabbitmqccm configurada en el application.yaml.

El método usado para publicar el mensaje en el exchage de rabbit de ccm, cuenta con la anotación @CircuitBreaker, lo cual permite abrir el circuito e impedir el intento de conexión a la cola de rabbit existente, si el porcentaje de fallas supera el 50%. El tamaño de la ventana establecido es el valor por defecto definido en la librería de resilience4j, el cual es de 100 mensajes.

Pasados 90 segundos, el estado del circuito pasará a medio abierto y permitirá realizar 2 peticiones para comprobar el estado de la conexión, en caso de fallar más del 50% de las peticiones volverá a colocarse en estado abierto por 90 segundos más, de lo contrario, el circuito estará en estado cerrado. (La configuración del resilience4j se encuentra en application.yaml)

**Para esta comunicación, CCM notifica a través de correo electrónico.**

**Mensaje de entrada:**

```json
{
    "tipoDocumentoCliente": "C",
    "nroDocumentoCliente": "2137777",
    "nmEvaluacion": "40916ba7-7dd2-4c1f-8687-48953aca9016",
    "sarlaftId" : "50016cc7-7dd2-4c1f-8687-48953ccn9015",
    "sarlaftToken" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2NDI1MTk4MTMsImV4cCI6MTY3NDA1NTgxMywiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.rS248_Kq2Z7Znuhx3g4e8vOxz1CaeRhfOVvSsYLQXCM"
}
```

**Mensaje de salida:**

```json
{
    "claves": {
        "clave1": {
            "valor": "numeroDeIdentificaciondelCliente=2137777|tipoDeIdentificacionDelCliente=C"
        },
        "clave2": {
            "valor": ""
        },
        "clave3": {
            "valor": ""
        }
    },
    "codigoProceso": "",
    "consecutivo": "9082-C2137777-68acf92b-b6b2-4d88-b160-3cb866d236d4",
    "content": {
        "datosComunicacion": {
            "primerNombreCliente": "NESTOR",
            "numeroCelularCliente": "311520111",
            "emailCliente": "prueba@gmail.com.co",
            "emailAsesor": "asesor@sura.com.co",
            "tipoDeTramite": "reclamaciones"
            "urlSarlaft": "https://local.suranet.com/4F9DF4AC671F5FB187D103D2C0BEDF6DD082AF9E66F2A12EFB4C0CD30157BEFC"
        },
        "viasTrafficProps": {
            "codigoAplicacion": "9082",
            "descripcionOperacion": "ACTIVACION",
            "descripcionProceso": "SARLAFT",
            "descripcionSolucion": "*",
            "compania": "TRANSVERSAL",
            "procesoSura": "ADMINISTRACION RIESGOS DEL CLIENTE",
            "idCliente": ""
        }
    }
}

```

**Dependencias Ecosistema Sura:**

Mensaje Destino en RabbitMQSura:

**Usuario de Conexión: sarlaft4.ccm.usr**

**URL RabbitMQ DLLO: **[msgdllo.suramericana.com.co](http://msgdllo.suramericana.com.co:15672/)

**URL RabbitMQ LABO: **[msglab.suramericana.com.co](http://msglab.suramericana.com.co:15672/)

**Exchange RabbitMQ: sura.iccm.paquetizado**

A continuación, se presentan las pruebas de comunicación (Correo)

[Notificacion Reclamaciones Persona Natural.pdf](./attachments/Notificacion Reclamaciones Persona Natural.pdf)

[Notificacion Reclamaciones Persona Juridica.pdf](./attachments/Notificacion Reclamaciones Persona Juridica.pdf)
