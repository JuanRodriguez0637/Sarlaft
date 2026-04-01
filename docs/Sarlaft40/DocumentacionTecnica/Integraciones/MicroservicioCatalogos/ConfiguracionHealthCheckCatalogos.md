# Configuración HealtchCheck con librería actuator - catalogos

> **Fuente Confluence:** [Configuración HealtchCheck con librería actuator - catalogos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3598778541/Configuraci%C3%B3n+HealtchCheck+con+librer%C3%ADa+actuator+-+catalogos)
> **Última modificación:** 2024-03-12 — Julián Andrés Curubo García · versión 1
> **Sección:** [Microservicio - Catálogos](./index.md)

Este nuevo servicio web de healthCheck permite evaluar las conexiones principales del microservicio de tal forma que cuando desde el aks en azure, se haga el ping para evaluar la salud del microservicio, se evalué de igual forma la conexión al service bus de azure.

Con la librería de spring actuator `spring-boot-starter-actuator` se logra este objetivo, se incluye la librería en el build.gradle
![image-20240207-200559.png](./attachments/image-20240207-200559.png)
La validación con el sevice bus se utiliza una clase personalizada `ServicebusHealthIndicator` en la cual se usa las dependencias:

```
implementation 'com.microsoft.azure:azure-servicebus:3.6.7'
implementation 'com.azure:azure-messaging-servicebus:7.14.7'
implementation 'org.reactivecommons:async-service-bus-starter:1.1.39-BETA'
```
![image-20240312-000110.png](./attachments/image-20240312-000110.png)
Se realiza la siguiente configuración en el **application.yaml**
![image-20240312-000137.png](./attachments/image-20240312-000137.png)
Se realiza la siguiente configuración en el archivo **deployment.yml** en el proyecto de configuración para cada ambiente.
![image-20240312-000234.png](./attachments/image-20240312-000234.png)
