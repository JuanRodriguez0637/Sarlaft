# Simplificar arquitectura de comunicación en proceso webhook - propuesta de cambio

> **Fuente Confluence:** [Simplificar arquitectura de comunicación en proceso webhook - propuesta de cambio](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3737911299/Simplificar+arquitectura+de+comunicaci+n+en+proceso+webhook+-+propuesta+de+cambio)  
> **Última modificación:** 2024-05-17 — Julián Andrés Curubo García · versión 9  
> **Sección:** [Diseño Funcionalidades](./index.md)

## Archivos adjuntos

| Archivo | Enlace |
| --------- | -------- |
| `Simplificar Arquitectura webhook en Sarlaft 4.pdf` | [Simplificar Arquitectura webhook en Sarlaft 4.pdf](./attachments/Simplificar Arquitectura webhook en Sarlaft 4.pdf) |
| `Simplificar Arquitectura comunicacion webhook.drawio` | [Simplificar Arquitectura comunicacion webhook.drawio](./attachments/Simplificar Arquitectura comunicacion webhook.drawio) |
| `Diagrama de la arquitectura actual del proceso webhook en Sarlaft 4.docx` | [Diagrama de la arquitectura actual del proceso webhook en Sarlaft 4.docx](./attachments/Diagrama de la arquitectura actual del proceso webhook en Sarlaft 4.docx) |
| `image-20240514-213031.png` | [image-20240514-213031.png](./attachments/image-20240514-213031.png) |
| `image-20240514-212631.png` | [image-20240514-212631.png](./attachments/image-20240514-212631.png) |
| `image-20240514-212611.png` | [image-20240514-212611.png](./attachments/image-20240514-212611.png) |
| `image-20240514-212000.png` | [image-20240514-212000.png](./attachments/image-20240514-212000.png) |
| `image-20240514-211846.png` | [image-20240514-211846.png](./attachments/image-20240514-211846.png) |
| `image-20240514-211832.png` | [image-20240514-211832.png](./attachments/image-20240514-211832.png) |

Este artículo tiene como propósito simplificar la actual arquitectura de comunicación del proceso de webhook en el aplicativo Sarlaft 4.0 tras una propuesta de eliminación del microservicio sarlaftwebhook en el proceso webhook que se maneja actualmente en Sarlaft 4.0. A continuación se expone como se encuentra el proceso de comunicación actual y dos propuestas de posibles soluciones con las que se puede abarcar el tema de la eliminación del microservicio salraftwebhook:

[Diagrama de la arquitectura actual del proceso webhook en Sarlaft 4.0](/wiki/spaces/EPA/pages/3742531593/Diagrama+de+la+arquitectura+actual+del+proceso+webhook+en+Sarlaft+4.0)

[Propuesta 1 - Omitir la comunicación que pasa por Azure Service Bus](/wiki/spaces/EPA/pages/3742892047/Propuesta+1+-+Omitir+la+comunicaci+n+que+pasa+por+Azure+Service+Bus)

[Propuesta 2 - Mantener la comunicación por el Azure Service Bus](/wiki/spaces/EPA/pages/3743580178/Propuesta+2+-+Mantener+la+comunicaci+n+por+el+Azure+Service+Bus)

[Conclusiones para simplificar la arquitectura del proceso webhook en Sarlaft 4.0](/wiki/spaces/EPA/pages/3743219726/Conclusiones+para+simplificar+la+arquitectura+del+proceso+webhook+en+Sarlaft+4.0)

[/wiki/download/attachments/3737911299/Simplificar%20Arquitectura%20webhook%20en%20Sarlaft%204.pdf?version=2&modificationDate=1715951789475&cacheVersion=1&api=v2](/wiki/download/attachments/3737911299/Simplificar%20Arquitectura%20webhook%20en%20Sarlaft%204.pdf?version=2&modificationDate=1715951789475&cacheVersion=1&api=v2)[/wiki/download/attachments/3737911299/Simplificar%20Arquitectura%20comunicacion%20webhook.drawio?version=2&modificationDate=1715951789364&cacheVersion=1&api=v2](/wiki/download/attachments/3737911299/Simplificar%20Arquitectura%20comunicacion%20webhook.drawio?version=2&modificationDate=1715951789364&cacheVersion=1&api=v2)[/wiki/download/attachments/3737911299/Diagrama%20de%20la%20arquitectura%20actual%20del%20proceso%20webhook%20en%20Sarlaft%204.docx?version=2&modificationDate=1715951789220&cacheVersion=1&api=v2](/wiki/download/attachments/3737911299/Diagrama%20de%20la%20arquitectura%20actual%20del%20proceso%20webhook%20en%20Sarlaft%204.docx?version=2&modificationDate=1715951789220&cacheVersion=1&api=v2)
