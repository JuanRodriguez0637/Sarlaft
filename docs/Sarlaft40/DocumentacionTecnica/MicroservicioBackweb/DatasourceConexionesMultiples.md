# Datasource - Conexiones Multiples

> **Fuente Confluence:** [Datasource - Conexiones Multiples](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3537108995)
> **Última modificación:** 2024-03-26 — Alejandro Ocampo (Unlicensed) · versión 11
> **Sección:** [Microservicio Backweb](./index.md)

La configuración de los datasource múltiples en el application se debe tener cuenta los siguientes parámetros, los cuales vamos a mencionar a continuación por ambiente:

| | | | |
| --- | --- | --- | --- |
| ***Datasource*** | Objeto que contiene la configuración de la fuente de datos. | | |
| ***connectionWrite*** | Conexión de escritura | | |
| **`driver`** | Controlador de JDBC para el manejador de base de datos | `org.postgresql.Driver` | |
| ***`url`*** | URL del recurso de conexión a la base de datos | | |
| ***`username`*** | Nombre de usuario para conectarse a la base de datos | | |
| ***`password`*** | Contraseña usada para conectarse a la base de datos | | |
| ***connectionRead*** | Conexión de lectura | | |
| **`driver`** | Controlador de JDBC para el manejador de base de datos | `org.postgresql.Driver` | |
| ***`url`*** | URL del recurso de conexión a la base de datos | | |
| ***`username`*** | Nombre de usuario para conectarse a la base de datos | | |
| ***`password`*** | Contraseña usada para conectarse a la base de datos | | |

Configuraciones de JPA (Java Persistence API) para la aplicación Spring.

[BaseJpaConfig](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3632300037/BaseJpaConfig)

[JpaConfig](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3538321427/JpaConfig)

[ReadOnlyJpaConfig](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3539337222/ReadOnlyJpaConfig)

[Anotación - ReadOnlyRepository](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3539238915/Anotaci%C3%B3n+-+ReadOnlyRepository)
