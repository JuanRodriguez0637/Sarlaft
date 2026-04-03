---
title: "Desplegar Cambios"
confluence_id: 2462548015
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2462548015"
last_modified: "2021-10-28"
author: "5da8927fa627f40c2f3c20ac"
version: 2
---

# Desplegar Cambios

> **Fuente Confluence:** [Desplegar Cambios](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2462548015)
> **Última modificación:** 2021-10-28 — versión 2
> **Sección:** [Front (Web Component)](./index.md)

Para desplegar cambios en los diferentes ambientes se debe crear un Pull Request (PR), este debe ser revisado por los aprobadores, y luego que den el visto bueno se debe completar.

Hasta este punto ya estaría hecho el merge al ambiente respectivo

> **📝 Nota:** Por el momento se tiene definido que para desplegar en cada ambiente se debe crear un PR por ambiente, es decir uno para "develop" otro para "quality" otro para "master"

- Para lanzar los despliegues se deben hacer de forma manual, entrando a este repositorio, y lanzándolo desde el botón "Run pipeline", ahí sale una ventana lateral donde se indica cual de los ambientes se quiere desplegar

https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=283

![image-20211028-195104.png](./attachments/image-20211028-195104.png)

- Se lanza con el botón "Run" y se debe ver la ventana de ejecución:

![image-20211028-195213.png](./attachments/image-20211028-195213.png)

> **📝 Nota:** Se debe lanzar cada ambiente por separado

### Validación

Para verificar que se haya hecho el despliegue:

- Entrar a la url del respectivo ambiente
- Ingresar a Containers

![image-20211028-195520.png](./attachments/image-20211028-195520.png)

- Entrar a la ruta `$web`
- ![image-20211028-195559.png](./attachments/image-20211028-195559.png)

  de ahí a identityvalidator
- ![image-20211028-195627.png](./attachments/image-20211028-195627.png)

  y validar la fecha de modificación
- ![image-20211028-195732.png](./attachments/image-20211028-195732.png)

Url por ambiente

- Dllo: https://portal.azure.com/#@sura.com/resource/subscriptions/30233a10-a0f4-440e-9bb4-e98de74911d1/resourceGroups/rg-sarlaft-persistence-dllo-001/providers/Microsoft.Storage/storageAccounts/stsarlaft588e89ab/overview
- Lab: https://portal.azure.com/#@sura.com/resource/subscriptions/f6278fb3-d372-470e-b355-70025248eb80/resourceGroups/rg-sarlaft-persistence-lab-001/providers/Microsoft.Storage/storageAccounts/stsarlaft0e136506/containersList
- Pdn: Validar con el diseñador o arquitecto que tenga permisos sobre esta suscripción
