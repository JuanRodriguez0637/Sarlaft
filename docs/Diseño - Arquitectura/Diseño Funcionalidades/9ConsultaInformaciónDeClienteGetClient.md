# 9. Consulta información de Cliente (getClient)

> **Fuente Confluence:** [9. Consulta información de Cliente (getClient)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3226009603/9.+Consulta+informaci+n+de+Cliente+getClient)  
> **Última modificación:** 2023-06-15 — Diana Muñoz · versión 2  
> **Sección:** [Diseño Funcionalidades](./index.md)

## Archivos adjuntos

| Archivo | Enlace |
|---------|--------|
| `Sarlaft_Laura-PrecargaCliente2 (1)-20230615-151307.jpg` | [Sarlaft_Laura-PrecargaCliente2 (1)-20230615-151307.jpg](./attachments/Sarlaft_Laura-PrecargaCliente2 (1)-20230615-151307.jpg) |
| `Sarlaft_Laura-PrecargaCliente2-20230615-135502.jpg` | [Sarlaft_Laura-PrecargaCliente2-20230615-135502.jpg](./attachments/Sarlaft_Laura-PrecargaCliente2-20230615-135502.jpg) |

Al momento de diligenciar un formulario de sarlaft, el aplicativo de sarlaft hace un prediligenciamiento del formulario con la información que encuentre en las siguientes fuentes de información de clientes: modelo de información propio de saralft, modelo de clientes de Sura, información de personas naturales en la fuente de proveedor Experian, información de personas jurídicas en la fuente de proveedor Informacolombia.

La consulta de información se hace en orden, primero se consulta en las fuentes internas el modelo propio de sarlaft y en el modelo de clientes de Sura, si hace falta algún dato se procede a consultar en las fuentes externas correspondiente al tipo de persona, Experian para personas naturales e Informacolombia para personas jurídicas.

![imagen](https://segurosti.atlassian.net/wiki/download/attachments/3226009603/Sarlaft_Laura-PrecargaCliente2%20(1)-20230615-151307.jpg?version=1&modificationDate=1686842032027&cacheVersion=1&api=v2)