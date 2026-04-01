# Regla Tablas Paramétricas PJ_SOAT - Motor Evaluación Tipo Formulario

> **Fuente Confluence:** [Regla Tablas Paramétricas PJ_SOAT - Motor Evaluación Tipo Formulario](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3890151437/Regla+Tablas+Param+tricas+PJ_SOAT+-+Motor+Evaluaci+n+Tipo+Formulario)
> **Última modificación:** 2024-09-24 — Brayan Estiven Sepúlveda Quintero · versión 4
> **Sección:** [Regla Tablas Paramétricas PJ_SOAT - Motor Evaluación](../index.md)

## Archivos adjuntos

| Archivo | Enlace |
| --------- | -------- |
| `lab.postman_environment.json` | [lab.postman_environment.json](./attachments/lab.postman_environment.json) |
| `local.postman_environment.json` | [local.postman_environment.json](./attachments/local.postman_environment.json) |
| `Invalid file id - 598b4cd7-5174-4510-87ee-ba9e6e6f335c` | [Invalid file id - 598b4cd7-5174-4510-87ee-ba9e6e6f335c](./attachments/Invalid file id - 598b4cd7-5174-4510-87ee-ba9e6e6f335c) |
| `Endpoints HU 565396.postman_collection.json` | [Endpoints HU 565396.postman_collection.json](./attachments/Endpoints HU 565396.postman_collection.json) |
| `TipoFormularioRequisitosRules.xls` | [TipoFormularioRequisitosRules.xls](./attachments/TipoFormularioRequisitosRules.xls) |
| `image-20240717-130139.png` | [image-20240717-130139.png](./attachments/image-20240717-130139.png) |

Se agregan dos nuevas reglas al motor de tipificación (formularios y requisitos), una para entidades de régimen y otra para entidades financieras:
![image-20240717-130139.png](./attachments/image-20240717-130139.png)
Adjunto archivo con las nuevas reglas:

[/wiki/download/attachments/3890151437/TipoFormularioRequisitosRules.xls?version=1&modificationDate=1721221363521&cacheVersion=1&api=v2](/wiki/download/attachments/3890151437/TipoFormularioRequisitosRules.xls?version=1&modificationDate=1721221363521&cacheVersion=1&api=v2)

Adjunto colección de Postman con el caso de prueba para la regla de régimen y la regla de financieras:

[Enlace a la colección](https://suramericana.sharepoint.com/:f:/r/sites/MESA7-CALIDADDEINFORMACIN/Shared%20Documents/General/Proyecto%20SARLAFT%204.0/DocumentacionDesarrollo/IniciativaSoat_2024/Documentos%20Complementarios%20SARLAFT/sarlaft/motor/formularios?csf=1&web=1&e=5Ks2pT)

[Enlace a los ambientes](https://suramericana.sharepoint.com/:f:/r/sites/MESA7-CALIDADDEINFORMACIN/Shared%20Documents/General/Proyecto%20SARLAFT%204.0/DocumentacionDesarrollo/IniciativaSoat_2024/Documentos%20Complementarios%20SARLAFT/sarlaft?csf=1&web=1&e=JJ7Cu4)

Adicional se adjunta log de splunk para visualizar la regla que se ejecuta del motor:
index="idx_sarlaft4_*" message="*modulo=SARLAFTENGINE*" message="*response*" message="*252c3b83-a7bf-4932-b1f8-80637c3210c3*"

[https://holmeslab.suramericana.com.co:9000/en-GB/app/group_center/search?earliest=-60m&latest=now&q=search%20index%3D%22idx_sarlaft4_*%22%20message%3D%22*modulo%3DSARLAFTENGINE*%22%20message%3D%22*response*%22%20message%3D%22*252c3b83-a7bf-4932-b1f8-80637c3210c3*%22&display.page.search.mode=fast&dispatch.sample_ratio=1&sid=1721221974.12532](https://holmeslab.suramericana.com.co:9000/en-GB/app/group_center/search?earliest=-60m&latest=now&q=search%20index%3D%22idx_sarlaft4_*%22%20message%3D%22*modulo%3DSARLAFTENGINE*%22%20message%3D%22*response*%22%20message%3D%22*252c3b83-a7bf-4932-b1f8-80637c3210c3*%22&display.page.search.mode=fast&dispatch.sample_ratio=1&sid=1721221974.12532)
