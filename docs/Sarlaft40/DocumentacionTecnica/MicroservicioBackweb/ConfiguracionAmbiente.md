# Configuración Ambiente - Microservicio Backweb

> **Fuente Confluence:** [Configuración Ambiente - Microservicio Backweb](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2398715932)
> **Última modificación:** 2025-12-29 — versión 10
> **Sección:** [Microservicio Backweb](./index.md)

**Requisitos:**

- Java 21
- Gradle `8.10.2`

**URL Repositorio:**

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-ms)

**URL Repositorio proyecto configuración:**

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-conf)

**URL Acceso local:**

[http://localhost:6380/sarlaftbackweb/](http://localhost:6380/sarlaftbackweb/resultevaluation)

**URL Acceso desarrollo:**

[http://sarlaftapi.dllosura.com/sarlaftbackweb/](http://sarlaftapi.dllosura.com/sarlaftbackweb/resultevaluation)

**URL Acceso laboratorio:**

[https://sarlaftapi.labsura.com/sarlaftbackweb/](https://sarlaftapi.labsura.com/sarlaftbackweb/resultevaluation)

**Pipeline con template:**

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=4125](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=4125)

**Sonarqube:**

[https://sonarqube.suramericana.com.co/solucionescorporativas/dashboard?id=892-sarlaft-admin-ms&branch=release%2FRelease_JUL2024](https://sonarqube.suramericana.com.co/solucionescorporativas/dashboard?id=892-sarlaft-admin-ms&branch=release%2FRelease_JUL2024)

### Ejecución del proyecto en local

Para la ejecución del proyecto desde el IntelliJ IDE se proveen tres archivos de configuración de perfilamiento para que se ejecute la aplicación con configuraciones de ambiente diferentes.

![Perfiles de configuración IntelliJ](./attachments/image-20210917-154518.png)

Dev, lab y local los cuales van configurados según las dependencias de su ambiente y los cuales defines al momento de la ejecución de la aplicación desde tu IDE con la variable de entorno **spring.profiles.active=local**

![Configuración de ejecución IntelliJ](./attachments/image-20210917-154604.png)

Para pruebas en el ambiente local se tiene otro 'string connection' para pruebas con un service-bus privado pero se puede cambiar al 'string connection' de dev.
