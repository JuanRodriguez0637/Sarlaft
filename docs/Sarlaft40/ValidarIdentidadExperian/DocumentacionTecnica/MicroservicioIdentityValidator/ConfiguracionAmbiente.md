---
title: "Configuración Ambiente - IdentityValidator"
confluence_id: 2378924049
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2378924049"
last_modified: "2025-08-27"
author: "632dd1a5234d44d406d0f129"
version: 16
---

# Configuración Ambiente - IdentityValidator

> **Fuente Confluence:** [Configuración Ambiente - IdentityValidator](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2378924049)
> **Última modificación:** 2025-08-27 — versión 16
> **Sección:** [Microservicio - identity validator](./index.md)

**Requisitos:**

- Java 11
- Gradle 6.8
- Git, puedes descargarlo del siguiente enlace (https://git-scm.com/)
- Aplicativo Sourcetree, puedes descargarlo del siguiente enlace ([Sourcetree](https://www.sourcetreeapp.com/))
- Intellij IDEA, puedes descargarlo del siguiente enlace (https://www.jetbrains.com/es-es/idea/download/)

Estos dos últimos pueden ser instalados en las propias máquinas para pruebas en local

- MongoDB, puedes descargarlo del siguiente enlace ([MongoDB](https://www.mongodb.com/try/download/community))
- RabbitMQ, puedes descargarlo del siguiente enlace ([RabbitMQ](https://www.rabbitmq.com/download.html))

**URL Repositorio Proyecto microservicio:**

https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms

**URL Repositorio Proyecto configuración**

https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-conf

**URL Repositorio Proyecto pruebas**

https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-pa

**URL ACCESO LOCAL**

http://local.suramericana.com:8080/api

**URL DESARROLLO**

http://local.suramericana.com.co:8080/api (Ajustar cuando esté ambiente)

**URL LABORATORIO**

http://local.suramericana.com:8080/api (Ajustar cuando esté ambiente)

[**NOTA:** Tener en cuenta cambio en archivo host.](#nota-importante)

**Ruta Pipeline Azure**

https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=3786&_a=summary

**URL Repositorio Pruebas SoapUI y JMeter**

https://SuraColombia@dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-validadorcliente-identidad-pa

## Manual instalación Identity Validator

Clone el repositorio de Identity Validator (`adm_y_fin-validadorcliente-identidad-ms`) en su equipo desde el branch de develop, a través de la herramienta de Sourcetree:

![image-20210909-154729.png](./attachments/image-20210909-154729.png)

![image-20210909-155341.png](./attachments/image-20210909-155341.png)

En el IDE IntelliJ o el de su preferencia, importe el proyecto que fue clonado:

![image-20210909-155406.png](./attachments/image-20210909-155406.png)

Se da clic en Confiar en proyecto (Trust project), para proceder a abrir el proyecto, dado que el IDE detecto que es un proyecto Gradle, y procederá a descargar las librerías configuradas, basado en la versión del Gradle configurado en este, en este caso la versión de Gradle 6.8

![image-20210909-155455.png](./attachments/image-20210909-155455.png)

Inicia el proceso de importar librerías, configurar estructura, y compilar el proyecto:

![image-20210909-155513.png](./attachments/image-20210909-155513.png)

Una vez compilado el proyecto, mostrará el siguiente mensaje:

![image-20210909-155559.png](./attachments/image-20210909-155559.png)

## Nota importante:

Antes de desplegar el servicio revise:

- En el archivo host de su máquina, se encuentra la siguiente configuración

  **127.0.0.1           local.suramericana.com**

  **Ruta Archivo Hosts: C:\Windows\System32\drivers\etc\ hosts**

- Revisar la configuración del proyecto `\adm_y_fin-validadorcliente-identidad-ms\applications\app-service\src\main\resources\application.yml`

  Para identificar la configuración de MongoDB y RabbitMQ, si es local, debe tenerlos instalados, y escuchando por los puertos configurados.

  Recuerda, por el momento el microservicio en este momento al clonar el proyecto, apunta a la base de datos mongoDB y RabbitMQ local.

## Despliegue local Identity Validator

Despliegue local del microservicio, desde la parte superior derecha del IDE, se debe realizar la edición de la configuración, para el correcto funcionamiento de ciertos servicios expuestos por IdentityValidatorMS

![image-20211027-205352.png](./attachments/image-20211027-205352.png)

Se deben agregar las siguientes opciones a Java Virtual Machine:

**`-Djavax.net.ssl.keyStore`**, la ruta del keystore construido para realizar los consumos seguros de algunos servicios de Experian. Esta ruta en la ejecución local debería apuntar al classpath por defecto donde se encuentra el archivo `Experian.jks`, que se encuentra `[RUTA PROYECTO]/applications/app-service/build/resources/main/experian.jks`. Esta propiedad se puede parametrizar de dos formas en intellij IDEA, seteando el Working Directory `[RUTA PROYECTO]`, y a la propiedad solo setear la ruta relativa `./applications/app-service/build/resources/main/experian.jks`, o setear la ruta completa del archivo `[RUTA PROYECTO]/applications/app-service/build/resources/main/experian.jks`

**`-Djavax.net.ssl.keyStorePassword`**, la contraseña del keystore construido para realizar los consumos seguros de algunos servicios de Experian. En la ejecución local la contraseña del keystore es `sarlaftapi.labsura.com`

**`-Dspring.profiles.active`**, el pérfil del ambiente en el que se desea trabajar (Ejemplo: `dev`, `lab`, `pdn`)

![image-20211027-210802.png](./attachments/image-20211027-210802.png)

Se debe dar clic en Apply, y luego OK, y ya podría ejecutarse, incluso subirlo en modo DEBUG:

![image-20210909-160223.png](./attachments/image-20210909-160223.png)

Aplicación iniciada:

![image-20210909-160249.png](./attachments/image-20210909-160249.png)

Pruebe la ejecución con el servicio de estado (status) localmente. URL: http://localhost.suramericana.com:8080/api/status

![image-20210910-133239.png](./attachments/image-20210910-133239.png)

**Configuración del proyecto**

La configuración del proyecto se realiza en el archivo **`application.yml`**

`\adm_y_fin-validadorcliente-identidad-ms\applications\app-service\src\main\resources\application.yml`

En caso de requerir cambios en el `application.yml`, realizarlos en el archivo correspondiente a cada uno de los ambientes: **dev** (desarrollo), **lab** (laboratorio) y **master** (producción), de tal forma que en el momento del despliegue estos sean tomados.

Clone el proyecto de configuración

https://SuraColombia@dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-validadorcliente-identidad-conf

![image-20210909-160438.png](./attachments/image-20210909-160438.png)

Abra el archivo **`application.yml`** en la ruta donde descargo el proyecto de configuración, por ejemplo: `\adm_y_fin-validadorcliente-identidad-conf\configmap`

Realice el cambio para cada rama, con los valores correspondientes para cada ambiente

![image-20210909-160458.png](./attachments/image-20210909-160458.png)
