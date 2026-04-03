# ReadOnlyJpaConfig

> **Fuente Confluence:** [ReadOnlyJpaConfig](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3539337222)
> **Última modificación:** 2024-03-26 — Alejandro Ocampo · versión 2
> **Sección:** [Microservicio Backweb](./index.md)

Esta clase proporciona configuración para la gestión de lectura utilizando JPA en una aplicación Spring, la conexión que se esta utilizando es `connectionRead` que se encuentra en el archivo `application.yaml`.

```java
package com.sura.backweb.config;

import javax.persistence.EntityManagerFactory;
import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import com.sura.backweb.annotation.ReadOnlyRepository;
import com.sura.backweb.jpa.config.DBConfig;


@Configuration
@EnableTransactionManagement
@EnableJpaRepositories(
        basePackages = "com.sura.backweb.jpa",
        includeFilters = @ComponentScan.Filter(ReadOnlyRepository.class),
        entityManagerFactoryRef = "entityManagerFactoryRead"
)
@ConfigurationProperties(prefix = "spring.datasource.connection-read")
public class ReadOnlyJpaConfig extends BaseJpaConfig {
	
    @Bean(name = "readDataSource")
    public DataSource readDataSource() {
        DBConfig secret = createDbSecret("spring.datasource.connection-read");
        return createDataSource(secret);
    }
	
    @Bean(name = "entityManagerFactoryRead")
    public LocalContainerEntityManagerFactoryBean entityManagerFactoryRead(
            @Qualifier("readDataSource") DataSource dataSource,
            @Value("${spring.jpa.databasePlatform}") String dialect) {
        return createEntityManagerFactory(dataSource, dialect, "read");
    }

    @Bean(name = "readTransactionManager")
    public PlatformTransactionManager readTransactionManager(
            @Qualifier("entityManagerFactoryRead") EntityManagerFactory entityManagerFactoryRead) {
        return createTransactionManager(entityManagerFactoryRead);
    }
    
}
```

`@Configuration`: Esta anotación indica que esta clase proporciona configuración para la aplicación. Spring buscará los métodos anotados con `@Bean` dentro de esta clase para crear y configurar los componentes de la aplicación.

`@EnableJpaRepositories`: Esta anotación habilita la funcionalidad de repositorios basados en interfaces que extiendan `JpaRepository`, `CrudRepository` y entre otros.

- `basePackages`: Acá se hace la relación del paquete base donde Spring busca los repositorios JPA.
- `includeFilters`: Incluye los repositorios JPA que se encuentre con la anotación `ReadOnlyRepository`.
- `entityManagerFactoryRef`: Especifica el nombre del `EntityManagerFactory` que se usa.
- Métodos `@Bean`: Estos métodos son responsables de crear y configurar los beans de la aplicación.
  - `writeDbSecret`: Este método crea un objeto `DBSecret` utilizando la configuración proporcionada en el entorno (como propiedades en un archivo `application.yml`). Este objeto contiene la información de conexión a la base de datos, como la URL, el nombre de usuario y la contraseña.
  - `writeDataSource`: Este método crea y configura un bean `DataSource` utilizando un objeto `DBConfig` y la clase de controlador JDBC proporcionada. Se está utilizando el patrón de diseño Inyección de Dependencias (DI) para proporcionar el `DBConfig` y la clase de controlador JDBC necesaria.
  - `entityManagerFactoryWrite`: Este método crea y configura un bean `EntityManagerFactory` para la base de datos de escritura. Utiliza el `DataSource` creado anteriormente y el dialecto de base de datos proporcionado en las propiedades de la aplicación. También configura propiedades adicionales de JPA, como el dialecto de Hibernate.
  - `transactionManager`: Este método crea un bean `PlatformTransactionManager` que manejará las transacciones de la base de datos. Utiliza el `EntityManagerFactory` creado anteriormente para interactuar con las transacciones JPA.
