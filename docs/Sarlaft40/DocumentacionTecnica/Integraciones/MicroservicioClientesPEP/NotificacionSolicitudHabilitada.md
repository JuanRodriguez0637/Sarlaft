# Notificación Solicitud Habilitada

> **Fuente Confluence:** [Notificación Solicitud Habilitada](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2072281253/Notificaci%C3%B3n+Solicitud+Habilitada)
> **Última modificación:** 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 9
> **Sección:** [Microservicio - Clientes PEP](./index.md)

**Objetivo:** Recibir la notificación de solicitud habilitada para un cliente PEPS por medio de un mensaje de RabbitMQ de Sura y ser notificada como un evento a la aplicación de Sarlaft API.

**Comunicación:**
![SURA Documentacion-Page-2 (1).png](<./attachments/SURA Documentacion-Page-2 (1).png>)
**Descripción**:

La integración tiene un listener de rabbit configurado para escuchar la cola seguros.rrcc.habilitacion (parametrizada en el application.yaml).

La notificación recibida luego se envía usando la librería Reactive Commons, como un comando para que escuche la aplicación sarlaftapi.

**Mensaje de entrada desde RabbitMQ Sura:**

{"dni":"C71775944","ramo":"005","operacion":"00","suboperacion":"%","figura":"T","cdOficina":"403","cdAsesor":"4999","feInicio":"1620959764746","feFin":"1621823764746","nroSolicitud":"2282"}

**Mensaje de salida en comando hacia Sarlaft API:**

{"dni":"C71775944","ramo":"005","operacion":"00","suboperacion":"%","figura":"T","cdOficina":"403","cdAsesor":"4999","feInicio":"1620959764746","feFin":"1621823764746","nroSolicitud":"2282"}

**Dependencias Ecosistema Sura:**

Mensaje Origen en RabbitMQSura:

**Usuario de Conexión: **seguros.sarlaftpeps.usr

**URL RabbitMQ DLLO: **[msgdllo.suramericana.com.co](http://msgdllo.suramericana.com.co:15672/)

**URL RabbitMQ LABO: **[msglab.suramericana.com.co](http://msglab.suramericana.com.co:15672/)

**Queue RabbitMQ: **seguros.rrcc.habilitacion
