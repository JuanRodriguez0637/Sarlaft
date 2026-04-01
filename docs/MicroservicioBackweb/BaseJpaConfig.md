# BaseJpaConfig

> **Fuente Confluence:** [BaseJpaConfig](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3632300037)
> **Última modificación:** 2024-03-26 · versión 2
> **Sección:** [Microservicio Backweb](./index.md)

Esta clase Java llamada `BaseJpaConfig` proporciona métodos para configurar y crear los componentes necesarios para la persistencia de datos utilizando JPA (Java Persistence API).

```java
package com.sura.backweb.config;

import java.util.Properties;

import javax.persistence.EntityManagerFactory;
import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.orm.jpa.JpaTransactionManager;
import org.springframework.orm.jpa.JpaVendorAdapter;
import org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;
import org.springframework.transaction.PlatformTransactionManager;

import com.sura.backweb.jpa.config.DBConfig;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class BaseJpaConfig {

    @Autowired
    private Environment env;

    protected DBConfig createDbSecret(String prefix) {
        String url = env.getProperty(prefix + ".url");

        String driverClassName = env.getProperty(prefix + ".driverClassName");

        return DBConfig.builder()
                .url(url)

                .driverClassName(driverClassName)
                .build();
    }

    protected DataSource createDataSource(DBConfig secret) {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl(secret.getUrl());

        config.setDriverClassName(secret.getDriverClassName());
        return getDataSource(config);
    }

    protected HikariDataSource getDataSource(HikariConfig config) {
        return new HikariDataSource(config);
    }

    protected LocalContainerEntityManagerFactoryBean createEntityManagerFactory(DataSource dataSource, String dialect,
            String persistenceUnitName) {

        LocalContainerEntityManagerFactoryBean em = new LocalContainerEntityManagerFactoryBean();
        em.setDataSource(dataSource);
        em.setPackagesToScan("com.sura.backweb.jpa");

        JpaVendorAdapter vendorAdapter = new HibernateJpaVendorAdapter();
        em.setJpaVendorAdapter(vendorAdapter);
        em.setPersistenceUnitName(persistenceUnitName);

        Properties properties = new Properties();
        properties.setProperty("hibernate.dialect", dialect);
        em.setJpaProperties(properties);

        return em;
    }

    protected PlatformTransactionManager createTransactionManager(EntityManagerFactory entityManagerFactory) {
        return new JpaTransactionManager(entityManagerFactory);
    }
}

```
