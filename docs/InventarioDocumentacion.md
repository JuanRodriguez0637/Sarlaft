# Inventario de Documentación — Sarlaft 4.0 vs Confluence

> **Última actualización:** 2026-04-02
> **Espacio Confluence:** [EPA — Sarlaft 4.0](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1750892627/Sarlaft+4.0)
> **Directorio local:** `Sarlaft/docs/Sarlaft40/`

---

## Resumen General

| Métrica | Valor |
|---|---|
| Secciones top-level en Confluence | 14 |
| Secciones top-level documentadas localmente | 14 |
| Subsecciones Doc. Técnica en Confluence | 17 |
| Subsecciones Doc. Técnica documentadas localmente | 17 |
| **Total secciones en Confluence** | **31** |
| **Total secciones documentadas** | **31** |
| **Secciones faltantes** | **0** |
| Archivos `.md` generados | 410 |

---

## 1. Secciones Top-Level de Sarlaft 4.0

### Documentadas

| Sección Confluence | ID Página | Carpeta Local | Estado |
|---|---|---|---|
| Documentación Técnica | `1746830371` | `DocumentacionTecnica/` | ✅ Documentada |
| Documentación de Incidentes | `1742800723` | `DocumentacionDeIncidentes/` | ✅ Documentada |
| Preguntas frecuentes - Sarlaft | `1928167429` | `PreguntasFrecuentes/` | ✅ Documentada |
| Validar identidad (Experian) | `2370961900` | `ValidarIdentidadExperian/` | ✅ Documentada |
| API Sarlaft | `2558033927` | `ApiSarlaft/` | ✅ Documentada |
| Ingesta de datos Teradata | `2595160065` | `IngestaDatosTeradata/` | ✅ Documentada |
| Automatización Flujos Criticos | `4131979320` | `AutomatizacionFlujosCriticos/` | ✅ Documentada |
| Interfaces de Servicio | `1955070133` | `InterfacesDeServicio/` | ✅ Documentada |
| Proceso de Migración | `2596667457` | `ProcesoDeMigracion/` | ✅ Documentada |
| Proceso de Actualización | `3715006471` | `ProcesoDeActualizacion/` | ✅ Documentada |
| Proceso de Negocio | `1742800734` | `ProcesoDeNegocio/` | ✅ Documentada |
| Documentación de Solicitudes | `1746928745` | `DocumentacionDeSolicitudes/` | ✅ Documentada |
| Segmentación Core | `2739077470` | `SegmentacionCore.md` | ✅ Documentada |
| Guía de Aprendizaje Sarlaft 4.0 | `3228270786` | `GuiaDeAprendizaje.md` | ✅ Documentada |

### Pendientes por documentar

> ✅ **Todas las secciones top-level han sido documentadas** (actualización 2026-04-02).

> **Nota sobre "Interfaces de Servicio" (top-level):** Ya existe `DocumentacionTecnica/InterfacesDeServicio/` que documenta interfaces bajo Documentación Técnica. La sección top-level `1955070133` es una página **diferente** con su propio árbol de hijos. Validar si el contenido es distinto o redundante antes de documentar.

> **Nota sobre "Documentación de Solicitudes":** En local existe `DocumentacionTecnica/DocumentacionDeSolicitudes/`. En Confluence, "Documentación de Solicitudes" (`1746928745`) es hijo **directo** de Sarlaft 4.0, no de Documentación Técnica. Evaluar si reubicar.

---

## 2. Subsecciones de Documentación Técnica

### Documentadas

| Sección Confluence | ID Página | Carpeta Local |
|---|---|---|
| Gestión de la Configuración | `1809908067` | `GestionConfiguracion/` |
| Atributos de Calidad Desarrollo | `1813545175` | `AtributosCalidadDesarrollo/` |
| Diseño - Arquitectura | `1804697669` | `DisenoArquitectura/` |
| Microservicio SarlaftAPI | `1801159134` | `MicroservicioSarlaftAPI/` |
| Microservicio PEPS | `1804861539` | `MicroservicioPEPS/` |
| Motor de Evaluación | `1809941005` | `MotorDeEvaluacion/` |
| Microservicio Webhook | `2314207324` | `MicroservicioWebhook/` |
| Mircroservicio sarlaftBatch | `2554036309` | `MicroservicioSarlaftBatch/` |
| Microservicio Backweb | `2398027809` | `MicroservicioBackweb/` |
| Microservicio SarlaftClientesMS | `2701656178` | `MicroservicioSarlaftClientesMS/` |
| Integraciones | `1864597528` | `Integraciones/` |
| Front | `1985511647` | `Front/` |
| Configuración Plataforma Base Sarlaft | `2389114940` | `ConfiguracionPlataformaBase/` |
| Propiedades PrefetchCount y MaxConcurrency | `3403874362` | `PropiedadesPrefetchCountMaxConcurrency.md` |
| Pruebas Orden Administrativa Soat | `3819175965` | `PruebasOrdenAdministrativaSoat/` |
| Acceso a URLS necesarias para el equipo base | `1827046088` | `AccesoUrlsEquipoBase.md` |
| Documentación Procesos BI | `1856536871` | `DocumentacionProcesosBI.md` |

### Pendientes por documentar

> ✅ **Todas las subsecciones de Documentación Técnica han sido documentadas** (actualización 2026-04-02).

---

## 3. Detalle de Páginas Hijas — Secciones Faltantes

### Interfaces de Servicio (top-level) — `1955070133`

| ID | Título |
|---|---|
| `1955070150` | Descripción de Interfaces Principales |
| `1955070163` | Interfaz Procesos Masivos |
| `1955070170` | Escenario de Validación Sarlaft en varios request |
| `1954644239` | Interfaz de Consulta de Estado Sarlaft |
| `2406318105` | Evaluación para Reclamaciones |

### Validar identidad (Experian) — `2370961900`

| ID | Título |
|---|---|
| `2367455702` | Definiciones técnicas |
| `2372894725` | Documentación técnica |
| `2618294680` | Servicios Web |
| `4058480694` | Mejora Control de Alertas (No implementado) |

### API Sarlaft — `2558033927`

| ID | Título |
|---|---|
| `2557771783` | Proceso de exposición en ApiGee |
| `2557804567` | Documentación Técnica Servicios |
| `2610397242` | DISEÑO APIS |
| `2402385952` | Implementación Interfaz Gráfica Cotizador |

### Ingesta de datos Teradata — `2595160065`

| ID | Título |
|---|---|
| `2595258369` | Ingesta Databriks |
| `2595291151` | Trasporte Datafactory |
| `2624749588` | Guía Básica Azure |

### Proceso de Migración — `2596667457`

| ID | Título |
|---|---|
| `2595651662` | Modelo de Clientes - Modelo de Vinculaciones |
| `2662761001` | Migración - Tipificación |
| `2866249773` | Migración - Transporte Modelo Sarlaft 4.0 |

### Proceso de Actualización — `3715006471`

| ID | Título |
|---|---|
| `3713728533` | Sarlafts Candidatos para Actualizar |
| `3715661855` | Solucion Datafactory |
| `5696585734` | Nuevo Diseño - Proceso Actualización |

### Automatización Flujos Criticos — `4131979320`

| ID | Título |
|---|---|
| `4132077596` | [KR4 Excelencia técnica]: F1 Conocimiento Simplificado - PN |
| `4134043655` | [KR4 Excelencia técnica]: F2 Conocimiento Ordinario - PJ |
| `4134338583` | [KR4 Excelencia técnica]: F3 Medidas intensificadas |
| `4133486648` | [KR4 Excelencia técnica]: F4 Retipificación del riesgo |
| `4133748748` | [KR4 Excelencia técnica]: F5 Datos Directivos |
| `4133617685` | [KR4 Excelencia técnica]: F6 Parametrias |

### Documentación de Incidentes — `1742800723`

> Ya existe `DocumentacionDeIncidentes/` — verificar si las 5 páginas hijas están documentadas:

| ID | Título |
|---|---|
| `5174689830` | Solicitud de request and response |
| `5174886473` | Solucionar INC asignados en BMC Helix |
| `5174624323` | Limpiar Base de datos en laboratorio |
| `5174788164` | Problemas con el link de validación de identidad |
| `5624856625` | Error en el aplicativo de Banca (Negocio en estado PENDIENTE) |

### Proceso de Negocio — `1742800734`

| ID | Título |
|---|---|
| `1804959889` | Tableros de Información Negocio |

### Documentación de Solicitudes — `1746928745`

| ID | Título |
|---|---|
| `5227118615` | Parametrización de un nuevo subramo o producto |

### Segmentación Core — `2739077470`

> Página hoja (sin hijos). Solo requiere un `.md`.

### Guía de Aprendizaje Sarlaft 4.0 - Desarrollo — `3228270786`

> Página hoja (sin hijos). Solo requiere un `.md`.

---

## 4. Observaciones

1. **Ubicación incorrecta:** `DocumentacionDeSolicitudes/` existe bajo `DocumentacionTecnica/` en local, pero en Confluence es hijo directo de Sarlaft 4.0. Evaluar si mover a `Sarlaft40/DocumentacionDeSolicitudes/`.

2. **Sección duplicada potencial:** "Interfaces de Servicio" existe como top-level (`1955070133`) Y como subsección de Doc. Técnica (`DocumentacionTecnica/InterfacesDeServicio/`). Verificar si son la misma sección o contenido diferente.

3. **Volumen:** Las secciones faltantes suman ~24,500+ páginas descendientes en total (el espacio EPA es muy grande). El volumen real a documentar depende de la profundidad requerida.

4. **Páginas hoja:** `Segmentación Core` y `Guía de Aprendizaje` son páginas sin hijos — su documentación es un solo archivo `.md` cada una.
