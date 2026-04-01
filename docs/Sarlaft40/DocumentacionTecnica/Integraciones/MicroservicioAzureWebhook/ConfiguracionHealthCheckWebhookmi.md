# Configuración HealtchCheck con librería actuator - webhookmi

> **Fuente Confluence:** [Configuración HealtchCheck con librería actuator - webhookmi](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3617652750/Configuraci%C3%B3n+HealtchCheck+con+librer%C3%ADa+actuator+-+webhookmi)
> **Última modificación:** 2024-04-04 — Diana Muñoz · versión 3
> **Sección:** [MicroServicio Azure - Webhook](./index.md)

Este nuevo servicio web de healthCheck permite evaluar las conexiones principales del microservicio de tal forma que cuando desde el aks en azure, se haga el ping para evaluar la salud del microservicio se evalué de igual forma las conexiones a base de datos, cache redis, rabbitmq y conexión al service bus de azure.

Con la librería de spring actuator `spring-boot-starter-actuator` se logra este objetivo, se incluye la librería en el main.gradle
![image-20240207-200559.png](./attachments/image-20240207-200559.png)
La validación con la base de datos se hace automáticamente con el indicador por defecto DataSourceHealthIndicator que trae la librería, y obtiene el datasource utilizando la información de conexión a la base de datos del archivo application.yml.

La validación con RabbitMQ se hace automáticamente con el indicador por defecto RabbitHealthIndicator que trae la librería spring actuator.

La validación con el service bus se utiliza una clase personalizada `ServicebusHealthIndicator`.

Se realiza la siguiente configuración en el **application.properties**

![image-20240404-213211.png](./attachments/image-20240404-213211.png)Se realiza la siguiente configuración en el archivo deployment.yml en el proyecto de configuración para cada ambiente.
![image-20240318-220021.png](./attachments/image-20240318-220021.png)
