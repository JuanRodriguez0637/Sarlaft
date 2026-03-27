# Configuración Garbage Collector - SarlaftAPI

> **Fuente:** [Confluence - Configuración Garbage Collector](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4743725057/Configuraci%C3%B3n+Garbage+Collector)  
> **Página padre:** [Microservicio SarlaftAPI](../index.md)  
> **HU relacionada:** [HU 745111](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/745111)

---

## Descripción

La propiedad `-XX:InitiatingHeapOccupancyPercent` es una opción de la **JVM (Java Virtual Machine)** que se utiliza para configurar el umbral de ocupación del heap que desencadena el inicio de un ciclo de recolección de basura concurrente (**Concurrent Garbage Collection**).

---

## Detalles

| Parámetro | Descripción |
|-----------|-------------|
| **Propósito** | Define el porcentaje de ocupación del heap que debe alcanzarse para que el recolector de basura **G1GC** inicie un ciclo de recolección concurrente |
| **Valor predeterminado** | `45%` |
| **Configuración personalizada** | Al establecerlo en `30`, se indica que el ciclo de recolección debe iniciarse cuando el **30%** del heap esté ocupado |

---

## Beneficios

- **Reducción de pausas**: Ayuda a reducir las pausas de la aplicación al iniciar la recolección de basura antes de que el heap esté demasiado lleno.
- **Optimización de rendimiento**: Es útil en aplicaciones con requisitos de baja latencia, ya que permite un manejo más proactivo de la memoria.

---

## Configuración en el Proyecto

La configuración se realiza en el proyecto **conf** de SarlaftAPI (`892-sarlaft-api-conf`):

> 📎 Imagen de la configuración disponible en Confluence (`image-20250527-150752.png`)

---

## Motivación

La iniciativa surgió necesidad de resolver errores de tipo **"Long garbage-collection time"** que se venían presentando en el microservicio de SarlaftAPI.
