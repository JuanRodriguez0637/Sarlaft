# Datasource - Conexiones Multiples

> **Fuente Confluence:** [Datasource - Conexiones Multiples](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3537108995)
> **Última modificación:** 2024-03-26 · versión 11
> **Sección:** [Microservicio Backweb](./index.md)

La configuración de los datasource múltiples en el application se debe tener cuenta los siguientes parámetros, los cuales vamos a mencionar a continuación por ambiente :

|  |  |  |  |
| --- | --- | --- | --- |
| _**Datasource**_Objeto que contiene la configuración de la fuente de datos. |  |  |  |
| _**connectionWrite**_ | Conexión de escritura |  |  |
| **driver** | Controlador de JDBC para el manejador de base de datos | `org.postgresql.Driver` |  |
| _**url**_ | URL del recurso de conexión a la base de datos |  |  |
|  |  |  |  |
|  |  |  |  |
| _**username**_ | Nombre de usuario para conectarse a la base de datos |  |  |
| _**password**_ | Contraseña usada para conectarse a la base de datos |  |  |
|  |  |  |  |
| _**connectionRead**_ | Conexión de escritura |  |  |
| **driver** | Controlador de JDBC para el manejador de base de datos | `org.postgresql.Driver` |  |
| _**url**_ | URL del recurso de conexión a la base de datos |  |  |
|  |  |  |  |
|  |  |  |  |
| _**username**_ | Nombre de usuario para conectarse a la base de datos |  |  |
| _**password**_ | Contraseña usada para conectarse a la base de datos |  |  |
|  |  |  |  |

Configuraciones de JPA (Java Persistence API)  para la aplicación Spring.

[BaseJpaConfig](./BaseJpaConfig.md)

[JpaConfig](./JpaConfig.md)

[ReadOnlyJpaConfig](./ReadOnlyJpaConfig.md)

[Anotación - ReadOnlyRepository](./AnotacionReadOnlyRepository.md)
