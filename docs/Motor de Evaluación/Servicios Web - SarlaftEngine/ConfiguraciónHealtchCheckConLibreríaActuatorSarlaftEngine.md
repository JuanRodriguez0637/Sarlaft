# Configuración HealtchCheck con librería actuator - SarlaftEngine

> **Fuente Confluence:** [Configuración HealtchCheck con librería actuator - SarlaftEngine](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3612016665/Configuraci+n+HealtchCheck+con+librer+a+actuator+-+SarlaftEngine)
> **Última modificación:** 2024-03-20 — Julián Andrés Curubo García · versión 2
> **Sección:** [Servicios Web - SarlaftEngine](./index.md)

## Archivos adjuntos

| Archivo | Enlace |
| --------- | -------- |
| `image-20240207-200559.png` | [image-20240207-200559.png](./attachments/image-20240207-200559.png) |
| `image-20240315-031220.png` | [image-20240315-031220.png](./attachments/image-20240315-031220.png) |
| `image-20240315-031217.png` | [image-20240315-031217.png](./attachments/image-20240315-031217.png) |
| `image-20240315-031119.png` | [image-20240315-031119.png](./attachments/image-20240315-031119.png) |
| `image-20240315-031112.png` | [image-20240315-031112.png](./attachments/image-20240315-031112.png) |
| `image-20240315-031043.png` | [image-20240315-031043.png](./attachments/image-20240315-031043.png) |

Este nuevo servicio web de healthCheck permite evaluar las conexiones principales del microservicio de tal forma que cuando desde el aks en azure, se haga el ping para evaluar la salud del microservicio, se evalué de igual forma la conexión al service bus de azure y base de datos Postgresql (nube).

Con la librería de spring actuator `spring-boot-starter-actuator` se logra este objetivo, se incluye la librería en el build.gradle
![image-20240207-200559.png](./attachments/image-20240207-200559.png)
La validación con la base de datos se hace automáticamente con el indicador por defecto DataSourceHealthIndicator que trae la librería, y obtiene el datasource utilizando la información de conexión a la base de datos del archivo application.yml.

La validación con redis se hace automáticamente con el indicador por defecto RedisHealthIndicator que trae la librería, y obtiene la conexión a redis utilizando la información de conexión del archivo application.yml.

La validación con el sevice bus se utiliza una clase personalizada `ServicebusHealthIndicator` en la cual se usa las dependencias:

```text
implementation 'com.microsoft.azure:azure-servicebus:3.6.7'
implementation 'com.azure:azure-messaging-servicebus:7.14.7'
implementation 'org.reactivecommons:async-service-bus-starter:1.1.39-BETA'
```

![image-20240315-031043.png](./attachments/image-20240315-031043.png)
Se realiza la siguiente configuración en el **application.yaml**

![image-20240315-031119.png](./attachments/image-20240315-031119.png)
Se realiza la siguiente configuración en el archivo **deployment.yml** en el proyecto de configuración para cada ambiente.

![image-20240315-031220.png](./attachments/image-20240315-031220.png)
