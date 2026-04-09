# Estructura Proyecto - Microservicio Backweb

> **Fuente Confluence:** [Estructura Proyecto - Microservicio Backweb](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2397339707)
> **Última modificación:** 2022-04-01 — Diana Muñoz · versión 2
> **Sección:** [Microservicio Backweb](./index.md)

---

Se basa en **Clean Architecture** y tiene los siguientes componentes:

> ⚠️ **Corrección (2026-04-08):** La documentación original indicaba "arquitectura hexagonal". El `README.md` del proyecto y la convención del equipo denominan este patrón **Clean Architecture**, que es conceptualmente similar pero con separación estricta en capas `domain` (model + usecase) e `infrastructure` (driven-adapters + entry-points).

![Estructura del proyecto](./attachments/image-20210917-estructura-proyecto.png)

*Figura 1. Estructura del proyecto.*

El proyecto está dividido en los siguientes subproyectos (Figura 2):

![Subproyectos](./attachments/image-20210917-subproyectos.png)

*Figura 2. Subproyectos.*

**1. applications-app-service**: contiene configuraciones generales del aplicativo, importa los módulos de las otras capas que siguen la Clean Architecture (Dominio e Infraestructura). Es la encargada de la interacción con el framework utilizado, sus complementos y la configuración de la ejecución del microservicio.

En el archivo de configuración `application.yaml` se encuentran las propiedades parametrizables para consulta de catálogos por service bus de azure, los parámetros para consumir base de datos y seguridad SEUS.

**2. domain**: La capa de dominio es la capa más interna del proyecto y es la encargada de dar las directivas del proceso teniendo en cuenta la lógica de negocio:

- **model**: representa los objetos de dominio (negocio) del aplicativo, sus características y comportamientos.
- **use-case**: contiene los casos de uso (actividades) que se ejecutan en la aplicación desde el proxy de la capa de infraestructura. Interactúan con los modelos para la conversión de los datos encontrados en los repositorios al modelo necesario.

  > ⚠️ **Corrección (2026-04-08):** La documentación original decía "el **único** caso de uso". Según análisis del código con Serena MCP, el módulo contiene **17 casos de uso** organizados en 8 dominios: `assessment`, `entidad`, `gafi`, `peps`, `salariominimo`, `formulario`, `token`, `seus`. El caso de uso más complejo es `GetResultEvaluationUseCase` (~248 líneas, 8 dependencias).

**3. infrastructure**:

- **driven-adapters-async-messages-senders:** módulo de adaptadores para comunicación asíncrona sobre **Azure Service Bus** mediante ReactiveCommons (`async-service-bus-starter:1.1.39-BETA`). Contiene los siguientes adaptadores:
  - `AsesorAsyncAdapter` → apps `sarlaftasesores` (query `List.bureau.find`) y `mdcmi` (query `Clients.client.adviser.validate`)
  - `CatalogoAsyncAdapter` → app `catalogos` (query `List.parameters.find`)
  - `PepsAsyncAdapter` → app `peps` (query `Clients.client.uncheckPEP`)
  - `NotificacionAsyncAdapter` → app `sarlaftwebhook` (command `Assessment.define.status`)

  > ⚠️ **Corrección (2026-04-08):** La documentación original describía este módulo únicamente como "adaptador para solicitar por query el catálogo de países". El código real contiene **4 adaptadores** que cubren 5 microservicios del ecosistema.
- **driven-adapters-jpa-repository:** aquí se encuentran las implementaciones para el control de persistencia de los objetos de dominio, además de implementaciones concretas para consulta de información de base de datos.
- **entry-points-reactive-web:** define los diferentes endpoints que se habilitarán en la aplicación, aquí se ubican los controllers que exponen los métodos de API Rest.

**Configuración base de datos**

> ⚠️ **Corrección (2026-04-08 — D-03 y D-11):** La documentación original (versión 2022) describía un único datasource con propiedades `spring.datasource.*` y un host PostgreSQL antiguo (`psql-srsarlaftd12576809`). La arquitectura actual usa **dual datasource** desde 2024: separación `connection-write` (escritura) y `connection-read` (lectura). Ver documentación actualizada en [DatasourceConexionesMultiples.md](./DatasourceConexionesMultiples.md).

La configuración de base de datos utiliza **dos datasources** (escritura y lectura) configurados en `application.yml` del proyecto `applications-app-service`. La clase `JpaConfig.java` extiende `BaseJpaConfig` para la conexión de escritura, y `ReadOnlyJpaConfig` gestiona la conexión de sólo lectura mediante la anotación `@ReadOnlyRepository`.

Properties (estructura actual — dual datasource)

```yaml
spring:
  application:
    name: sarlaftbackweb
  jpa:
    show-sql: true
    database: postgresql
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
  redis:
    host: <azure-redis-host>
    password: <password>
    ssl: true
    port: 6380
    type: redis
  cache:
    redis:
      time-to-live: 6900000
      cache-null-values: true

connection-write:
  driver-class-name: org.postgresql.Driver
  url: "jdbc:postgresql://psql-segsarlaftiacd-eus-b919.postgres.database.azure.com:5432/sarlaftdb?currentSchema=sarlaft&sslmode=require"
  username: <usuario-escritura>
  password: <password-escritura>

connection-read:
  driver-class-name: org.postgresql.Driver
  url: "jdbc:postgresql://psql-segsarlaftiacd-eus-b919.postgres.database.azure.com:5432/sarlaftdb?currentSchema=sarlaft&sslmode=require"
  username: <usuario-lectura>
  password: <password-lectura>

azure:
  connection-string: <service-bus-connection-string>
```

Configuration (patrón actual — dual datasource)

```java
// JpaConfig: datasource de ESCRITURA (connection-write)
@Configuration
public class JpaConfig extends BaseJpaConfig {
    // Extiende BaseJpaConfig del helper jpa-commons
    // Lee propiedades de connection-write.*
    // Escanea paquetes: com.sura.backweb.jpa
}

// ReadOnlyJpaConfig: datasource de LECTURA (connection-read)
@Configuration
public class ReadOnlyJpaConfig extends BaseJpaConfig {
    // Lee propiedades de connection-read.*
    // Los repositorios marcados con @ReadOnlyRepository
    // usan automáticamente este datasource
}
```

> Ver detalle completo del patrón dual datasource en [DatasourceConexionesMultiples.md](./DatasourceConexionesMultiples.md) y [JpaConfig.md](./JpaConfig.md).
