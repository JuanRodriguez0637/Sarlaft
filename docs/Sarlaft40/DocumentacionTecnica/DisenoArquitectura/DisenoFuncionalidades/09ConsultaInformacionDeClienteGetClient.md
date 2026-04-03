# 9. Consulta información de Cliente (getClient)

> **Fuente Confluence:** [9. Consulta información de Cliente (getClient)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3226009603)
> **Última modificación:** 2023-06-15 — Diana Muñoz · versión 2
> **Sección:** [Diseño Funcionalidades](./index.md)

Al momento de diligenciar un formulario de sarlaft, el aplicativo de sarlaft hace un prediligenciamiento del formulario con la información que encuentre en las siguientes fuentes de información de clientes: modelo de información propio de saralft, modelo de clientes de Sura, información de personas naturales en la fuente de proveedor Experian, información de personas jurídicas en la fuente de proveedor Informacolombia.

La consulta de información se hace en orden, primero se consulta en las fuentes internas el modelo propio de sarlaft y en el modelo de clientes de Sura, si hace falta algún dato se procede a consultar en las fuentes externas correspondiente al tipo de persona, Experian para personas naturales e Informacolombia para personas jurídicas.

![Precarga de información de Cliente](./attachments/Sarlaft_Laura-PrecargaCliente2%20%281%29-20230615-151307.jpg)
