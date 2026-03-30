# Microservicio SarlaftAPI

> **Fuente:** [Confluence - Microservicio SarlaftAPI](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1801159134/Microservicio+SarlaftAPI)  
> **Espacio:** 07) Dominio Soluciones Corporativas (EPA)  
> **Jerarquía:** Página de inicio → Subdominio: SOLUCIONES ADMINISTRATIVAS DE TI - SATI → Sarlaft 4.0 → Documentación Técnica → Microservicio SarlaftAPI

## Descripción

Esta sección contiene la documentación técnica completa del microservicio **SarlaftAPI** (proyecto `892-sarlaft-api-ms`), que es el componente principal de la solución Sarlaft 4.0 para la consulta y marcación de clientes PEP (Personas Expuestas Políticamente).

## Contenido

| Sección | Descripción | Archivo |
|---------|-------------|---------|
| Modelo de Dominio, Clases y BD | Diagramas del modelo de dominio, clases y base de datos | [ModeloDominioClasesBD.md](./ModeloDominioClasesBD.md) |
| Configuración Ambiente | Requisitos y pasos para configurar el ambiente de desarrollo | [ConfiguracionAmbiente.md](./ConfiguracionAmbiente.md) |
| Estructura Proyecto | Arquitectura hexagonal y organización del proyecto | [EstructuraProyecto/index.md](./EstructuraProyecto/index.md) |
| Configuración Base de Datos R2DBC | Configuración de acceso reactivo a PostgreSQL con R2DBC | [ConfiguracionBaseDatosR2DBC.md](./ConfiguracionBaseDatosR2DBC.md) |
| Servicios Web | Catálogo de todos los endpoints REST expuestos | [ServiciosWeb/index.md](./ServiciosWeb/index.md) |
| Proceso Evaluación | Lógica del proceso de evaluación SARLAFT | [ProcesoEvaluacion/index.md](./ProcesoEvaluacion/index.md) |
| Log Errores Splunk | Integración con Splunk para logging | [LogErroresSplunk.md](./LogErroresSplunk.md) |
| Procesos Carga Masiva | Procesos de carga masiva de figuras | [ProcesosCargaMasiva/index.md](./ProcesosCargaMasiva/index.md) |
| Configuración HealthCheck | HealthCheck con librería actuator | [ConfiguracionHealthCheck.md](./ConfiguracionHealthCheck.md) |
| Parametrización Timeout Registraduría | Configuración del timeout para consumo de registraduría | [ParametrizacionTimeoutRegistraduria.md](./ParametrizacionTimeoutRegistraduria.md) |
| Implementación Cabeceras de Seguridad | Cabeceras HTTP de seguridad implementadas | [ImplementacionCabecerasSeguridad.md](./ImplementacionCabecerasSeguridad.md) |
| Configuración Garbage Collector | Configuración JVM G1GC para el microservicio | [ConfiguracionGarbageCollector.md](./ConfiguracionGarbageCollector.md) |
| Evitar Duplicidad en Evidencias | Solución para evidencias duplicadas en evaluaciones | [EvitarDuplicidadEvidencias.md](./EvitarDuplicidadEvidencias.md) |
| Generar URL Validación Identidad | Endpoint para generar URL de validación de identidad | [GenerarUrlValidacionIdentidad.md](./GenerarUrlValidacionIdentidad.md) |
| Consumo de Nuevos Endpoints (Web Component) | Mapeo de endpoints nuevos para el Web Component | [ServiciosWeb/ConsumoNuevosEndpoints/index.md](./ServiciosWeb/ConsumoNuevosEndpoints/index.md) |

> **Nota:** `ConsumoNuevosEndpoints.md` en la raíz es un archivo legado de una sesión anterior. El contenido canónico está en `ServiciosWeb/ConsumoNuevosEndpoints/`.

## Repositorios

| Repositorio | Descripción |
|------------|-------------|
| [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms) | Repositorio principal |
| [892-sarlaft-api-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-conf) | Repositorio de configuración |
| [892-sarlaft-pa](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-pa) | Pruebas SoapUI y JMeter |

## Pipeline

- [Pipeline CI/CD](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=3349)
- [SonarQube](https://sonarqube.suramericana.com.co/solucionescorporativas/dashboard?id=892-sarlaft-api-ms)

## Ambientes

| Ambiente | URL |
|---------|-----|
| Local | http://local.suramericana.com.co:8091/sarlaftserv |
| Desarrollo | https://sarlaftapi.dllosura.com/sarlaftserv |
| Laboratorio | https://sarlaftapi.labsura.com/sarlaftserv |
| Producción | https://sarlaftapi.sura.com.co/sarlaftserv |
