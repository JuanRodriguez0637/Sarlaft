# Configuración Ambiente - Actualizacion Clientes

> **Fuente Confluence:** [Configuración Ambiente - Actualizacion Clientes](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1864761362/Configuraci%C3%B3n+Ambiente+-+Actualizacion+Clientes)
> **Última modificación:** 2024-07-22 — Julián Andrés Curubo García · versión 8
> **Sección:** [Microservicio Azure - Actualización Cliente Sura](./index.md)

**Objetivo:** actualizar información del cliente en el modelo de clientes de Sura.

La idea en esta HU es solo implementar el proceso de actualización. Es decir, aun no vamos a implementar la escucha y comunicación del mecanismo de Reply.

**Mecanismo de Integración: **Mensajeria RabbitMQ Sura

[ManualFuncionalPlataformaIntegralDatosCliente.docx](./attachments/ManualFuncionalPlataformaIntegralDatosCliente.docx)

**Requisitos:**

â Java 8.0

â Gradle 6.8

**URL Repositorio:**

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-function_saveclientes-mi](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-function_saveclientes-mi)

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-function_saveclientes-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-function_saveclientes-conf)

**Pipeline:**

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-function_saveclientes-conf?path=/azure-pipelines.yml&version=GBdeploy_dev&_a=contents](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-function_saveclientes-conf?path=/azure-pipelines.yml&version=GBdeploy_dev&_a=contents)

**Sonar:**

[https://sonar.suramericana.com.co/dashboard?id=saveclient](https://sonar.suramericana.com.co/dashboard?id=saveclient)

**Pipeline con template:**

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=4124](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=4124)

**Sonarqube:**

[https://sonarqube.suramericana.com.co/solucionescorporativas/dashboard?id=892-sarlaft-function_saveclientes-mi&branch=release%2FRelease_JUL2024](https://sonarqube.suramericana.com.co/solucionescorporativas/dashboard?id=892-sarlaft-function_saveclientes-mi&branch=release%2FRelease_JUL2024)
