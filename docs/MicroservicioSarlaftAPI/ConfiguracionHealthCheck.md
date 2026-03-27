# Configuración HealthCheck con Librería Actuator - SarlaftAPI

> **Fuente:** [Confluence - Configuración HealtchCheck con librería actuator - sarlaftapi](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3598712863/Configuraci%C3%B3n+HealtchCheck+con+librer%C3%ADa+actuator+-+sarlaftapi)  
> **Página padre:** [Microservicio SarlaftAPI](../index.md)

---

## Descripción

Este servicio web de HealthCheck permite evaluar las conexiones principales del microservicio. Cuando desde el **AKS en Azure** se hace el ping para evaluar la salud del microservicio, se evalúa también la conexión a:

- **Service Bus de Azure**
- **Base de datos PostgreSQL** (nube)
- **Redis** (nube)

---

## Librería Utilizada

Se usa Spring Actuator: `spring-boot-starter-actuator`

Se incluye en el `build.gradle`:

> 📎 Imagen de configuración disponible en Confluence (`image-20240207-200559.png`)

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

---

## Validaciones por Componente

### Base de Datos (PostgreSQL)

La validación con la base de datos se hace **automáticamente** con el indicador por defecto `DataSourceHealthIndicator`, que obtiene el datasource usando la información de conexión del `application.yml`.

### Redis

La validación con Redis se hace **automáticamente** con el indicador por defecto `RedisHealthIndicator`, usando la configuración de conexión del `application.yml`.

### Service Bus (Azure)

La validación con el Service Bus utiliza una clase **personalizada** `ServicebusHealthIndicator`, que depende de:

```gradle
implementation 'com.microsoft.azure:azure-servicebus:3.6.7'
implementation 'com.azure:azure-messaging-servicebus:7.14.7'
implementation 'org.reactivecommons:async-service-bus-starter:1.1.39-BETA'
```

> 📎 Imagen de la clase `ServicebusHealthIndicator` disponible en Confluence (`image-20240311-182202.png`)

---

## Configuración en `application.yaml`

> 📎 Imagen de configuración disponible en Confluence (`image-20240311-182224.png`)

---

## Configuración en `deployment.yml` (Proyecto de Configuración)

La configuración del deployment se realiza por ambiente en el proyecto de configuración:

> 📎 Imagen de configuración disponible en Confluence (`image-20240311-182303.png`)

---

## Incompatibilidad con SEUS (SSO Sura)

Debido a que el microservicio tiene seguridad SEUS, existe una incompatibilidad entre la librería `ssosura` y `actuator`. Para resolverlo, se debe incluir la siguiente línea en el archivo de Splunk, dentro de la sección de loggers:

```xml
<logger name="co.com.sura.sso.reactive.listeners" level="ERROR" />
```

> 📎 Imagen de configuración disponible en Confluence (`image-20240311-182330.png`)
