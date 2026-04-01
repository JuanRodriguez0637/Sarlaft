# Anotación - ReadOnlyRepository

> **Fuente Confluence:** [Anotación - ReadOnlyRepository](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3539238915)
> **Última modificación:** 2024-03-26 · versión 5
> **Sección:** [Microservicio Backweb](./index.md)

Esta clase se define como una anotación personalizada llamada ReadOnlyRepository, la cual, se utiliza para marcar los repositorios que son de lectura en la aplicación.

```java
package com.sura.backweb.annotation;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE})
@Documented
public @interface ReadOnlyRepository {

}
```text

`@Retention(RetentionPolicy.RUNTIME)`: Esta anotación lo que indica que esta disponible en tiempo de ejecución.

`@Target({ElementType.TYPE})`: Solo puede ser aplicada a los elementos de tipo, en este caso, a clases.

`public @interface ReadOnlyRepository {`: Aquí se define la anotación `ReadOnlyRepository` como una anotación de interfaz. Esto significa que `ReadOnlyRepository` puede ser aplicada a clases como un metadato.

Ejemplo de la implementación de la anotación `@ReadOnlyRepository`

```java
package com.sura.backweb.jpa.aplicacion;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.QueryByExampleExecutor;

import com.sura.backweb.annotation.ReadOnlyRepository;

@ReadOnlyRepository
public interface ReadAplicacionDataRepository extends CrudRepository<AplicacionData, String>, QueryByExampleExecutor<AplicacionData> {

    AplicacionData findByCodigoAplicacion(String codigoAplicacion);

}
```
