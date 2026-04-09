# Plan de Trabajo — Épicas Prioritarias SARLAFT 4.0

> **Fecha:** 2026-04-09  
> **Proyecto:** Gerencia_Tecnologia  
> **Equipo:** do-soluci_corporativas-Fortalecimiento SARLAFT  
> **Fuente:** Azure DevOps — [Backlog](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_backlogs/backlog/do-soluci_corporativas-Fortalecimiento%20SARLAFT/Historias)

---

## Resumen Ejecutivo

| Épica | Título | Features | HUs | Estado |
|-------|--------|----------|-----|--------|
| [1107349](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1107349) | **Formulario: Datos financieros, requisitos y junta directiva** | 3 | 13 | New |
| [1079106](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) | **Optimización: Base de datos y servicios externos** | 4 | 23 | New |
| [1105971](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1105971) | **[Conocimiento del Cliente]: Formularios y Reglas** | 4 | 12 | New |
| | **TOTAL** | **11** | **48** | |

> **Observación:** Todas las 48 HUs están en estado **New**, sin Story Points asignados, sin responsable y sin refinar. Se recomienda una sesión de refinamiento y estimación como primer paso.

---

## Catálogo de Repositorios Involucrados

> Fuente: Documentación técnica Sarlaft 4.0 (`docs/Sarlaft40/DocumentacionTecnica/`) y repositorios locales (`desarrollo/`).

| Alias corto | Repositorio | URL Azure DevOps | Componente |
|-------------|-------------|-------------------|------------|
| **sarlaft-api** | `892-sarlaft-api-ms` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms) | API principal — orquestación de evaluaciones |
| **sarlaft-api-conf** | `892-sarlaft-api-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-conf) | Configuración por ambiente de SarlaftAPI |
| **sarlaft-fr** | `892-sarlaft-fr` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) | Monorepo frontend — formularios y web components |
| **sarlaft-brms** | `892-sarlaft-brms-ms` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms) | Motor de reglas de negocio (Drools) |
| **sarlaft-brms-conf** | `892-sarlaft-brms-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-conf) | Configuración del motor |
| **sarlaft-batch** | `892-sarlaft-batch-ms` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-batch-ms) | Procesamiento batch de evaluaciones |
| **sarlaft-batch-conf** | `892-sarlaft-batch-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-batch-conf) | Configuración batch |
| **sarlaft-admin** | `892-sarlaft-admin-ms` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-ms) | Backweb administrativo — parametrías y consultas |
| **sarlaft-clientes** | `892-sarlaft-sarlaftclientes-ms` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4-sarlaftclientes-ms) | Consulta clientes en fuentes externas |
| **sarlaft-clientes-conf** | `892-sarlaft-sarlaftclientes-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4-sarlaftclientes-conf) | Configuración del MS clientes |
| **sarlaft-callback** | `892-sarlaft_callback-ms` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_callback-ms) | Webhook de resultado de evaluación |
| **func-requisitos** | `892-sarlaft-function_requisitos-mi` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_requisitos-mi) | Azure Function — requisitos documentales |
| **func-requisitos-conf** | `892-sarlaft-function_requisitos-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_requisitos-conf) | Configuración requisitos |
| **func-identity** | `892-sarlaft-function_identity-mi` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_identity-mi) | Azure Function — validación identidad/Experian |
| **func-identity-conf** | `892-sarlaft-function_identity-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_identity-conf) | Configuración identity |
| **func-documental** | `892-sarlaft_function_documental-mi` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_function_documental-mi) | Azure Function — integración FileNet P8 |
| **func-documental-conf** | `892-sarlaft_function_documental-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_function_documental-conf) | Configuración documental |
| **func-batch** | `892-sarlaft-function_batch-mi` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_batch-mi) | Azure Function — evaluación masiva |
| **func-rrcc** | `adm_y_fin-sarlaft-function-rrcc-mi` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-function-rrcc-mi) | Azure Function — riesgo consultable RRCC |
| **validador-identidad-ms** | `1101-validadorcliente_identidad-ms` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) | Backend validador de identidad (Experian) |
| **validador-identidad-conf** | `1101-validadorcliente_identidad-conf` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-conf) | Configuración validador identidad |
| **validador-identidad-fr** | `1101-validadorcliente_identidad-fr` | [Repo](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr) | Front web component validador identidad |
| **validador-admon-ms** | _(nuevo)_ | — | **Nuevo microservicio** Back admin validador identidad |
| **validador-admon-fr** | _(nuevo)_ | — | **Nuevo front** Angular admin validador identidad |

---

## Orden de Ejecución Sugerido

El plan se organiza en **3 fases** correspondientes a las épicas, con las features ordenadas por complejidad e interdependencia.

---

## FASE 1 — Épica 1107349: Formulario — Datos financieros, requisitos y junta directiva

**Justificación de prioridad:** Cambios en formularios impactan directamente en la captura de datos del cliente y condicionan las reglas de negocio de las épicas siguientes.

### Feature 1.1 — [1107350](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1107350) Datos financieros (3 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1025877](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1025877) | Modificar el campo de actividad económica | Historia | `sarlaft-fr`, `sarlaft-api`, `sarlaft-api-conf` | Sprint 1 |
| 2 | [1026762](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026762) | Solicitar a una PN y PJ ingresos y egresos | Historia | `sarlaft-fr`, `sarlaft-api`, `sarlaft-api-conf` | Sprint 1 |
| 3 | [1026765](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026765) | Solicitar a una PN y PJ activos y pasivos | Historia | `sarlaft-fr`, `sarlaft-api`, `sarlaft-api-conf` | Sprint 1 |

> **Detalle técnico:** Nuevos campos en formulario (CIIU v4, ingresos/egresos, activos/pasivos). Requiere UI de formulario (`sarlaft-fr`), endpoints/DTOs de persistencia (`sarlaft-api`), y catálogos precargables desde BD.

**Dependencias:** Ninguna identificada. Paralelizable.

### Feature 1.2 — [1057319](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1057319) Requisito opcional "Ingresos y retenciones" (4 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1082005](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082005) | Requisito opcional — Back Validación Adjuntos | Historia técnica | `sarlaft-api`, `func-requisitos`, `func-documental` | Sprint 1 |
| 2 | [1082032](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082032) | Requisito opcional — Back Validación Adjuntos - Pruebas seguridad | Historia técnica | `sarlaft-api`, `func-requisitos` | Sprint 1 |
| 3 | [1082042](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082042) | Requisito opcional — Back Requisitos | Historia técnica | `sarlaft-api`, `func-requisitos`, `func-requisitos-conf` | Sprint 2 |
| 4 | [1082089](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082089) | Requisito opcional — Front Requisitos | Historia técnica | `sarlaft-fr` | Sprint 2 |

> **Detalle técnico:** Cambiar obligatoriedad del requisito "Ingresos y retenciones" a opcional. Back maneja validación de adjuntos (`sarlaft-api`, `func-requisitos`), integración documental P8 (`func-documental`). Front ajusta formulario (`sarlaft-fr`).

**Dependencias:** HU 1082032 depende de 1082005. Front (1082089) depende de Back (1082042).

### Feature 1.3 — [1035467](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035467) Adicionar figura de junta directiva (6 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1082241](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082241) | Junta Directiva — Back | Historia técnica | `sarlaft-api`, `sarlaft-api-conf` | Sprint 2 |
| 2 | [1082249](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082249) | Junta Directiva — Motor de evaluación y Riesgo | Historia técnica | `sarlaft-brms`, `sarlaft-brms-conf` | Sprint 2 |
| 3 | [1082281](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082281) | Junta Directiva — Parametrización formulario - Back | Historia técnica | `sarlaft-api`, `sarlaft-admin` | Sprint 2 |
| 4 | [1082267](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082267) | Junta Directiva — Front | Historia técnica | `sarlaft-fr` | Sprint 3 |
| 5 | [1082272](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082272) | Junta Directiva — Parametrización formulario - Front | Historia técnica | `sarlaft-fr` | Sprint 3 |
| 6 | [1082270](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082270) | Junta Directiva — Validación riesgos RRCC | Historia técnica | `sarlaft-brms`, `func-rrcc` | Sprint 3 |

> **Detalle técnico:** Nueva figura "Junta Directiva" en Datos Directivos. Back crea modelo/DTOs (`sarlaft-api`), parametrización (`sarlaft-admin`). Motor incorpora reglas de evaluación para la nueva figura (`sarlaft-brms`). Front muestra y captura datos (`sarlaft-fr`). Validación RRCC contra la nueva figura (`func-rrcc`).

**Dependencias:** Back (1082241) → Front (1082267). Motor (1082249) → Validación RRCC (1082270).

---

## FASE 2 — Épica 1079106: Optimización — Base de datos y servicios externos

**Justificación de prioridad:** Optimizaciones técnicas que reducen problemas de duplicidad y mejoran rendimiento. Se puede iniciar en paralelo con la Fase 1 con un equipo dedicado.

### Feature 2.1 — [1032999](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999) Servicios externos (5 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1035171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171) | Depuración evaluaciones BD Sarlaft — histórico | Historia | `sarlaft-api`, `sarlaft-batch` | Sprint 1 |
| 2 | [1035498](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035498) | Evitar duplicidad validación identidad — Datos básicos | Historia | `sarlaft-api`, `func-identity`, `validador-identidad-ms` | Sprint 1 |
| 3 | [1035502](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035502) | Evitar duplicidad validación identidad — Cuestionario | Historia | `sarlaft-api`, `func-identity`, `validador-identidad-ms` | Sprint 2 |
| 4 | [1037054](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037054) | Evitar duplicidad consulta Migración Colombia | Historia | `sarlaft-api`, `sarlaft-clientes` | Sprint 2 |
| 5 | [1037085](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037085) | Reemplazar datos consulta estado documento | Historia | `sarlaft-api`, `sarlaft-api-conf` | Sprint 3 |

> **Detalle técnico:** Optimizaciones backend para evitar llamadas duplicadas a servicios externos (Experian/Registraduría, Migración Colombia). Depuración de evaluaciones históricas directamente en BD (`sarlaft-api`, `sarlaft-batch`). Cambios en lógica de caché/estados en la API principal.

### Feature 2.2 — [1035500](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035500) Evitar duplicidad consulta Registraduría (4 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1081870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081870) | Front Pantalla Modulo Sarlaft — Datos adicionales | Historia técnica | `sarlaft-fr` | Sprint 2 |
| 2 | [1081880](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081880) | Front Validador Identidad — IAC | Historia técnica | IaC / Pipelines DevOps (`validador-identidad-conf`) | Sprint 3 |
| 3 | [1081885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081885) | Front Validador Identidad Admon MS (nuevo micro Back) | Historia técnica | **`validador-admon-ms`** _(nuevo)_, Azure Redis Cache, BD nueva | Sprint 3 |
| 4 | [1081888](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081888) | Front ValidadorIdentidad MS | Historia técnica | `validador-identidad-ms`, `func-identity`, Azure Redis Cache | Sprint 3 |

> **Detalle técnico:** HU 1081870 ajusta front de datos adicionales (`sarlaft-fr`). HU 1081880 crea infra IaC para el app 1101. HU 1081885 crea un **nuevo microservicio** Back administrador de reglas de validador de identidad con BD propia y Redis. HU 1081888 modifica el `validador-identidad-ms` existente para leer parametría de rechazo de Registraduría desde caché/BD antes de invocar Experian.

### Feature 2.3 — [1035141](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141) Depuración evaluaciones BD — Proceso automático (7 items)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1076668](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076668) | Onboarding y Configuración Datafactory | Historia técnica | Azure Data Factory (IaC/DevOps) | Sprint 1 |
| 2 | [1076922](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076922) | Diseño inicial Pipelines Datafactory | Historia técnica | Azure Data Factory, BD Sarlaft (SQL) | Sprint 1 |
| 3 | [1076945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076945) | Implementación pipeline de consulta Datafactory | Historia técnica | Azure Data Factory, BD Sarlaft (SQL) | Sprint 2 |
| 4 | [1076947](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076947) | Implementación pipeline depuración evaluaciones Datafactory | Historia técnica | Azure Data Factory, BD Sarlaft (SQL) | Sprint 2 |
| 5 | [1076961](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076961) | Automatización del proceso | Historia técnica | Azure Data Factory (triggers/scheduling) | Sprint 3 |
| 6 | [1076953](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076953) | Tarea pruebas procesos consulta y depuración laboratorio | Tarea | Azure Data Factory | Sprint 3 |
| 7 | [1076956](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076956) | Tarea ejecución del proceso en producción | Tarea | Azure Data Factory | Sprint 4 |

> **Detalle técnico:** No involucra microservicios de negocio. Se crean pipelines de Azure Data Factory para identificar y eliminar evaluaciones históricas por rango de fechas. Tabla intermedia en modelo SARLAFT con idEvaluacion, fechaCreacion, estadoEvaluacion. Eliminación por lotes con manejo de errores y timeouts.

**Dependencias:** Secuencia obligatoria: Onboarding → Diseño → Implementación → Automatización → Pruebas → Producción.

### Feature 2.4 — [1037162](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037162) Gestión del estado del documento del cliente (7 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) | Validador Identidad Admon MS (Back) — Servicios gestión estado cliente | Historia técnica | **`validador-admon-ms`** _(nuevo)_, BD nueva, Splunk, SEUS | Sprint 3 |
| 2 | [1096178](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096178) | Validador Identidad Admon MS (Back) — Servicios gestión parametrías validación | Historia técnica | **`validador-admon-ms`** _(nuevo)_, BD nueva | Sprint 3 |
| 3 | [1096189](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096189) | Validador Identidad Admon MS (Back) — Servicios gestión parametrías parte 2 | Historia técnica | **`validador-admon-ms`** _(nuevo)_, BD nueva | Sprint 4 |
| 4 | [1096205](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096205) | Validador Identidad Admon MS (Front) — Gestión estado cliente Parte 1 | Historia técnica | **`validador-admon-fr`** _(nuevo)_, Angular, SEUS4 | Sprint 4 |
| 5 | [1096228](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096228) | Validador Identidad Admon MS (Front) — Gestión estado cliente Parte 2 | Historia técnica | **`validador-admon-fr`** _(nuevo)_ | Sprint 4 |
| 6 | [1096310](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096310) | Validador Identidad Admon MS (Front) — Servicios gestión parametrías Parte 1 | Historia técnica | **`validador-admon-fr`** _(nuevo)_ | Sprint 5 |
| 7 | [1096313](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096313) | Validador Identidad Admon MS (Front) — Servicios gestión parametrías Parte 2 | Historia técnica | **`validador-admon-fr`** _(nuevo)_ | Sprint 5 |

> **Detalle técnico:** Requiere crear **2 repositorios nuevos**: `validador-admon-ms` (Back Java/Spring con Lego Sura, BD propia, Redis, SEUS, Splunk) y `validador-admon-fr` (Front Angular con Lego Sura, SEUS4). El Back expone servicios de consulta de clientes bloqueados, desactivación de bloqueos y gestión de parametrías. El Front consume esos servicios con pantallas de filtrado, paginación y acciones.

**Dependencias:** Back (1096171, 1096178, 1096189) → Front (1096205+). Partes 1 → Partes 2.

---

## FASE 3 — Épica 1105971: [Conocimiento del Cliente] — Formularios y Reglas

**Justificación de prioridad:** Reglas de negocio y clasificación de personas jurídicas que complementan los formularios de la Fase 1.

### Feature 3.1 — [1032288](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) Clasificar personas jurídicas por tipo de sociedad (4 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) | Tipificar a las personas jurídicas por tipo de sociedad | Historia | `sarlaft-api`, `sarlaft-brms`, `sarlaft-batch` | Sprint 3 |
| 2 | [1046415](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046415) | Back — Parametrizar códigos requisitos por tipo sociedad | Historia | `sarlaft-api`, `sarlaft-admin`, `func-requisitos` | Sprint 4 |
| 3 | [1046438](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046438) | Front — Ajustes para mostrar los requisitos | Historia | `sarlaft-fr` | Sprint 4 |
| 4 | [1046535](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046535) | Relanzamiento de documentos a P8 | Historia | `sarlaft-api`, `func-documental` | Sprint 4 |

> **Detalle técnico:** Tipificación automática de PJ por razón social usando matriz de denominaciones (`sarlaft-api`). Motor incorpora matching por tipo de sociedad (`sarlaft-brms`). Parametrización de códigos de requisitos por tipo (`sarlaft-admin`, `func-requisitos`). Front muestra requisitos filtrados (`sarlaft-fr`). Reenvío a FileNet P8 (`func-documental`).

### Feature 3.2 — [1105983](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1105983) Reglas de negocio (4 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1041366](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041366) | Herencia por tipo de riesgo | Historia | `sarlaft-brms`, `sarlaft-api`, `func-identity`, `sarlaft-clientes` | Sprint 4 |
| 2 | [1046069](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046069) | Analizar clientes con nacionalidad países GAFI Negro | Historia | `sarlaft-brms`, `sarlaft-api` | Sprint 4 |
| 3 | [1053179](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1053179) | Actualización de nombres en tablas paramétricas - Front | Historia | `sarlaft-fr`, `sarlaft-admin` | Sprint 5 |
| 4 | [1056870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1056870) | Ajustar botón Cambiar Estado para permitir Rechazado | Historia | `sarlaft-fr`, `sarlaft-api` | Sprint 5 |

> **Detalle técnico:** HU 1041366 es la más compleja: ajusta reglas de herencia/optimización de evidencias por categoría, riesgo y vigencia en el motor (`sarlaft-brms`). Reconsulta obligatoria para estados fallidos según reglas. Involucra integraciones con Experian (`func-identity`), Registraduría, PEPS, GAFI, RRCC. HU 1046069 agrega regla GAFI al motor. HU 1053179 y 1056870 son ajustes de front y admin.

### Feature 3.3 — [1107355](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1107355) Cláusula tratamiento de datos (1 HU)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1032311](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032311) | Adicionar cláusula de tratamiento de datos | Historia | `sarlaft-fr`, `sarlaft-api` | Sprint 3 |

> **Detalle técnico:** Agregar cláusula de tratamiento de datos en el formulario. Cambio de UI (`sarlaft-fr`) y texto/configuración en el back (`sarlaft-api`).

**Nota:** HU pequeña y autocontenida. Puede adelantarse a cualquier sprint.

### Feature 3.4 — [1026770](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026770) Solicitar requisitos por tipo de sociedad (3 HUs)

| # | ID | Título | Tipo | Repositorios | Sprint |
|---|---|--------|------|-------------|--------|
| 1 | [1079051](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079051) | Solicitar requisitos por tipo de sociedad — Back | Historia técnica | `sarlaft-api`, `func-requisitos`, `func-requisitos-conf` | Sprint 4 |
| 2 | [1079058](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079058) | Solicitar requisitos por tipo de sociedad — Front | Historia técnica | `sarlaft-fr` | Sprint 5 |
| 3 | [1079062](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079062) | Solicitar requisitos por tipo de sociedad — Reintentos | Historia técnica | `sarlaft-api`, `func-requisitos` | Sprint 5 |

> **Detalle técnico:** Back parametriza requisitos documentales diferenciados por tipo de sociedad (`sarlaft-api`, `func-requisitos`). Front consume nuevo endpoint para filtrar requisitos (`sarlaft-fr`). Reintentos maneja fallback/retry del proceso de requisitos.

**Dependencias:** Depende de Feature 3.1 (clasificación por tipo de sociedad). Back → Front → Reintentos.

---

## Detalle de HUs por Sprint

### Sprint 1 — 9 HUs

| # | ID | Título | Épica | Feature | Tipo | Repositorios |
|---|---|--------|-------|---------|------|-------------|
| 1 | [1025877](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1025877) | Modificar el campo de actividad económica | 1107349 | 1.1 Datos financieros | Historia | `sarlaft-fr`, `sarlaft-api`, `sarlaft-api-conf` |
| 2 | [1026762](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026762) | Solicitar a una PN y PJ ingresos y egresos | 1107349 | 1.1 Datos financieros | Historia | `sarlaft-fr`, `sarlaft-api`, `sarlaft-api-conf` |
| 3 | [1026765](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026765) | Solicitar a una PN y PJ activos y pasivos | 1107349 | 1.1 Datos financieros | Historia | `sarlaft-fr`, `sarlaft-api`, `sarlaft-api-conf` |
| 4 | [1082005](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082005) | Requisito opcional — Back Validación Adjuntos | 1107349 | 1.2 Requisito opcional | Historia técnica | `sarlaft-api`, `func-requisitos`, `func-documental` |
| 5 | [1082032](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082032) | Requisito opcional — Back Validación Adjuntos - Pruebas seguridad | 1107349 | 1.2 Requisito opcional | Historia técnica | `sarlaft-api`, `func-requisitos` |
| 6 | [1035171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171) | Depuración evaluaciones BD Sarlaft — histórico | 1079106 | 2.1 Servicios externos | Historia | `sarlaft-api`, `sarlaft-batch` |
| 7 | [1035498](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035498) | Evitar duplicidad validación identidad — Datos básicos | 1079106 | 2.1 Servicios externos | Historia | `sarlaft-api`, `func-identity`, `validador-identidad-ms` |
| 8 | [1076668](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076668) | Onboarding y Configuración Datafactory | 1079106 | 2.3 Depuración BD | Historia técnica | Azure Data Factory (IaC/DevOps) |
| 9 | [1076922](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076922) | Diseño inicial Pipelines Datafactory | 1079106 | 2.3 Depuración BD | Historia técnica | Azure Data Factory, BD Sarlaft (SQL) |

> **Foco Sprint 1:** Formularios datos financieros + inicio de optimizaciones back + provisión Datafactory.

---

### Sprint 2 — 10 HUs

| # | ID | Título | Épica | Feature | Tipo | Repositorios |
|---|---|--------|-------|---------|------|-------------|
| 1 | [1082042](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082042) | Requisito opcional — Back Requisitos | 1107349 | 1.2 Requisito opcional | Historia técnica | `sarlaft-api`, `func-requisitos`, `func-requisitos-conf` |
| 2 | [1082089](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082089) | Requisito opcional — Front Requisitos | 1107349 | 1.2 Requisito opcional | Historia técnica | `sarlaft-fr` |
| 3 | [1082241](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082241) | Junta Directiva — Back | 1107349 | 1.3 Junta directiva | Historia técnica | `sarlaft-api`, `sarlaft-api-conf` |
| 4 | [1082249](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082249) | Junta Directiva — Motor de evaluación y Riesgo | 1107349 | 1.3 Junta directiva | Historia técnica | `sarlaft-brms`, `sarlaft-brms-conf` |
| 5 | [1082281](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082281) | Junta Directiva — Parametrización formulario - Back | 1107349 | 1.3 Junta directiva | Historia técnica | `sarlaft-api`, `sarlaft-admin` |
| 6 | [1035502](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035502) | Evitar duplicidad validación identidad — Cuestionario | 1079106 | 2.1 Servicios externos | Historia | `sarlaft-api`, `func-identity`, `validador-identidad-ms` |
| 7 | [1037054](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037054) | Evitar duplicidad consulta Migración Colombia | 1079106 | 2.1 Servicios externos | Historia | `sarlaft-api`, `sarlaft-clientes` |
| 8 | [1081870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081870) | Front Pantalla Modulo Sarlaft — Datos adicionales | 1079106 | 2.2 Duplicidad Registraduría | Historia técnica | `sarlaft-fr` |
| 9 | [1076945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076945) | Implementación pipeline de consulta Datafactory | 1079106 | 2.3 Depuración BD | Historia técnica | Azure Data Factory, BD Sarlaft (SQL) |
| 10 | [1076947](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076947) | Implementación pipeline depuración evaluaciones Datafactory | 1079106 | 2.3 Depuración BD | Historia técnica | Azure Data Factory, BD Sarlaft (SQL) |

> **Foco Sprint 2:** Cierre feature requisito opcional + inicio junta directiva (Back/Motor) + pipelines Datafactory + anti-duplicidad.

---

### Sprint 3 — 13 HUs

| # | ID | Título | Épica | Feature | Tipo | Repositorios |
|---|---|--------|-------|---------|------|-------------|
| 1 | [1082267](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082267) | Junta Directiva — Front | 1107349 | 1.3 Junta directiva | Historia técnica | `sarlaft-fr` |
| 2 | [1082272](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082272) | Junta Directiva — Parametrización formulario - Front | 1107349 | 1.3 Junta directiva | Historia técnica | `sarlaft-fr` |
| 3 | [1082270](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082270) | Junta Directiva — Validación riesgos RRCC | 1107349 | 1.3 Junta directiva | Historia técnica | `sarlaft-brms`, `func-rrcc` |
| 4 | [1037085](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037085) | Reemplazar datos consulta estado documento | 1079106 | 2.1 Servicios externos | Historia | `sarlaft-api`, `sarlaft-api-conf` |
| 5 | [1081880](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081880) | Front Validador Identidad — IAC | 1079106 | 2.2 Duplicidad Registraduría | Historia técnica | IaC / Pipelines DevOps (`validador-identidad-conf`) |
| 6 | [1081885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081885) | Validador Identidad Admon MS (nuevo micro Back) | 1079106 | 2.2 Duplicidad Registraduría | Historia técnica | **`validador-admon-ms`** _(nuevo)_, Redis, BD nueva |
| 7 | [1081888](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081888) | ValidadorIdentidad MS | 1079106 | 2.2 Duplicidad Registraduría | Historia técnica | `validador-identidad-ms`, `func-identity`, Redis |
| 8 | [1076961](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076961) | Automatización del proceso | 1079106 | 2.3 Depuración BD | Historia técnica | Azure Data Factory (triggers) |
| 9 | [1076953](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076953) | Tarea pruebas procesos consulta y depuración laboratorio | 1079106 | 2.3 Depuración BD | Tarea | Azure Data Factory |
| 10 | [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) | Validador Identidad Admon MS (Back) — Gestión estado cliente | 1079106 | 2.4 Gestión estado doc. | Historia técnica | **`validador-admon-ms`** _(nuevo)_, BD, Splunk, SEUS |
| 11 | [1096178](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096178) | Validador Identidad Admon MS (Back) — Gestión parametrías validación | 1079106 | 2.4 Gestión estado doc. | Historia técnica | **`validador-admon-ms`** _(nuevo)_, BD nueva |
| 12 | [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) | Tipificar a las personas jurídicas por tipo de sociedad | 1105971 | 3.1 Clasificar PJ | Historia | `sarlaft-api`, `sarlaft-brms`, `sarlaft-batch` |
| 13 | [1032311](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032311) | Adicionar cláusula de tratamiento de datos | 1105971 | 3.3 Cláusula datos | Historia | `sarlaft-fr`, `sarlaft-api` |

> **Foco Sprint 3:** Sprint más cargado. Cierre épica Formularios (junta directiva Front + RRCC). Creación del **nuevo micro `validador-admon-ms`**. Automatización Datafactory. Inicio reglas PJ y cláusula datos.

---

### Sprint 4 — 10 HUs

| # | ID | Título | Épica | Feature | Tipo | Repositorios |
|---|---|--------|-------|---------|------|-------------|
| 1 | [1096189](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096189) | Validador Identidad Admon MS (Back) — Gestión parametrías parte 2 | 1079106 | 2.4 Gestión estado doc. | Historia técnica | **`validador-admon-ms`** _(nuevo)_, BD nueva |
| 2 | [1096205](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096205) | Validador Identidad Admon MS (Front) — Gestión estado cliente Parte 1 | 1079106 | 2.4 Gestión estado doc. | Historia técnica | **`validador-admon-fr`** _(nuevo)_, Angular, SEUS4 |
| 3 | [1096228](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096228) | Validador Identidad Admon MS (Front) — Gestión estado cliente Parte 2 | 1079106 | 2.4 Gestión estado doc. | Historia técnica | **`validador-admon-fr`** _(nuevo)_ |
| 4 | [1076956](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076956) | Tarea ejecución del proceso en producción | 1079106 | 2.3 Depuración BD | Tarea | Azure Data Factory |
| 5 | [1046415](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046415) | Back — Parametrizar códigos requisitos por tipo sociedad | 1105971 | 3.1 Clasificar PJ | Historia | `sarlaft-api`, `sarlaft-admin`, `func-requisitos` |
| 6 | [1046438](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046438) | Front — Ajustes para mostrar los requisitos | 1105971 | 3.1 Clasificar PJ | Historia | `sarlaft-fr` |
| 7 | [1046535](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046535) | Relanzamiento de documentos a P8 | 1105971 | 3.1 Clasificar PJ | Historia | `sarlaft-api`, `func-documental` |
| 8 | [1041366](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041366) | Herencia por tipo de riesgo | 1105971 | 3.2 Reglas de negocio | Historia | `sarlaft-brms`, `sarlaft-api`, `func-identity`, `sarlaft-clientes` |
| 9 | [1046069](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046069) | Analizar clientes con nacionalidad países GAFI Negro | 1105971 | 3.2 Reglas de negocio | Historia | `sarlaft-brms`, `sarlaft-api` |
| 10 | [1079051](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079051) | Solicitar requisitos por tipo de sociedad — Back | 1105971 | 3.4 Requisitos PJ | Historia técnica | `sarlaft-api`, `func-requisitos`, `func-requisitos-conf` |

> **Foco Sprint 4:** Nuevo front `validador-admon-fr` + cierre Datafactory en producción. Motor de reglas (herencia, GAFI). Clasificación PJ (back + front + P8).

---

### Sprint 5 — 6 HUs

| # | ID | Título | Épica | Feature | Tipo | Repositorios |
|---|---|--------|-------|---------|------|-------------|
| 1 | [1096310](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096310) | Validador Identidad Admon MS (Front) — Gestión parametrías Parte 1 | 1079106 | 2.4 Gestión estado doc. | Historia técnica | **`validador-admon-fr`** _(nuevo)_ |
| 2 | [1096313](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096313) | Validador Identidad Admon MS (Front) — Gestión parametrías Parte 2 | 1079106 | 2.4 Gestión estado doc. | Historia técnica | **`validador-admon-fr`** _(nuevo)_ |
| 3 | [1053179](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1053179) | Actualización de nombres en tablas paramétricas - Front | 1105971 | 3.2 Reglas de negocio | Historia | `sarlaft-fr`, `sarlaft-admin` |
| 4 | [1056870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1056870) | Ajustar botón Cambiar Estado para permitir Rechazado | 1105971 | 3.2 Reglas de negocio | Historia | `sarlaft-fr`, `sarlaft-api` |
| 5 | [1079058](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079058) | Solicitar requisitos por tipo de sociedad — Front | 1105971 | 3.4 Requisitos PJ | Historia técnica | `sarlaft-fr` |
| 6 | [1079062](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079062) | Solicitar requisitos por tipo de sociedad — Reintentos | 1105971 | 3.4 Requisitos PJ | Historia técnica | `sarlaft-api`, `func-requisitos` |

> **Foco Sprint 5:** Cierre de todas las épicas. Pantallas finales del validador admin. Ajustes front de reglas. Requisitos PJ (front + reintentos).

---

### Resumen por Sprint

| Sprint | É. 1107349 | É. 1079106 | É. 1105971 | **Total** |
|--------|:----------:|:----------:|:----------:|:---------:|
| **1**  | 5 | 4 | — | **9** |
| **2**  | 5 | 5 | — | **10** |
| **3**  | 3 | 8 | 2 | **13** |
| **4**  | — | 4 | 6 | **10** |
| **5**  | — | 2 | 4 | **6** |
| **Total** | **13** | **23** | **12** | **48** |

---

## Análisis de Dependencias entre HUs

### Leyenda

| Símbolo | Significado |
|---------|-------------|
| 🔵 | Dependencia **intra-sprint** (dentro del mismo sprint) |
| 🔴 | Dependencia **inter-sprint** (requiere HU de un sprint anterior) |
| 🟡 | Dependencia **cross-feature** (entre features o épicas distintas) |

---

### Sprint 1 — Dependencias internas

| Tipo | HU origen | → | HU destino | Razón |
|:----:|-----------|---|------------|-------|
| 🔵 | [1082005](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082005) Back Validación Adjuntos | → | [1082032](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082032) Pruebas seguridad | Las pruebas de seguridad validan el código implementado en 1082005 |
| 🔵 | [1076668](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076668) Onboarding Datafactory | → | [1076922](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076922) Diseño Pipelines | No se puede diseñar pipelines sin tener el ambiente Datafactory provisionado |

> **Riesgo Sprint 1:** Si el onboarding de Datafactory (1076668) se retrasa, bloquea la cadena completa de Feature 2.3 (7 HUs en 4 sprints).

---

### Sprint 2 — Dependencias internas + desde Sprint 1

| Tipo | HU origen | → | HU destino | Razón |
|:----:|-----------|---|------------|-------|
| 🔴 | [1082005](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082005) Back Validación Adjuntos _(S1)_ | → | [1082042](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082042) Back Requisitos _(S2)_ | Back requisitos extiende la lógica de validación de adjuntos implementada en S1 |
| 🔵 | [1082042](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082042) Back Requisitos | → | [1082089](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082089) Front Requisitos | El front requiere los endpoints del back para mostrar el requisito como opcional |
| 🔴 | [1035498](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035498) Anti-duplicidad Datos básicos _(S1)_ | → | [1035502](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035502) Anti-duplicidad Cuestionario _(S2)_ | Misma estrategia de anti-duplicidad aplicada primero a Datos básicos, luego a Cuestionario |
| 🔴 | [1076922](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076922) Diseño Pipelines _(S1)_ | → | [1076945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076945) Pipeline consulta _(S2)_ | La implementación sigue al diseño |
| 🔴 | [1076922](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076922) Diseño Pipelines _(S1)_ | → | [1076947](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076947) Pipeline depuración _(S2)_ | La implementación sigue al diseño |
| 🔵 | [1076945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076945) Pipeline consulta | → | [1076947](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076947) Pipeline depuración | El pipeline de depuración usa los IDs generados por el pipeline de consulta |

---

### Sprint 3 — Dependencias internas + desde Sprints 1-2

| Tipo | HU origen | → | HU destino | Razón |
|:----:|-----------|---|------------|-------|
| 🔴 | [1082241](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082241) Junta Directiva Back _(S2)_ | → | [1082267](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082267) Junta Directiva Front _(S3)_ | El front consume los endpoints/DTOs creados en el back |
| 🔴 | [1082281](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082281) Parametrización Back _(S2)_ | → | [1082272](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082272) Parametrización Front _(S3)_ | El front de parametrización consume los servicios back |
| 🔴 | [1082249](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082249) Motor evaluación _(S2)_ | → | [1082270](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082270) Validación RRCC _(S3)_ | Las reglas RRCC dependen de que el motor ya tenga la nueva figura |
| 🔵 | [1081880](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081880) IaC Validador Identidad | → | [1081885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081885) Nuevo micro `validador-admon-ms` | La infra (IaC) debe estar provisionada antes de crear el microservicio |
| 🔵 | [1081885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081885) Nuevo micro `validador-admon-ms` | → | [1081888](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081888) ValidadorIdentidad MS | El ValidadorIdentidad MS lee la parametría de rechazo que expone el nuevo micro |
| 🔵 | [1081885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081885) Nuevo micro `validador-admon-ms` | → | [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) Gestión estado cliente Back | El servicio de gestión de estado se construye sobre el micro creado en 1081885 |
| 🔵 | [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) Gestión estado cliente Back | → | [1096178](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096178) Gestión parametrías Back | Las parametrías reutilizan la base del micro, dominio y seguridad (SEUS) ya configurados |
| 🔴 | [1076945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076945) Pipeline consulta _(S2)_ | → | [1076961](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076961) Automatización _(S3)_ | La automatización/scheduling requiere pipelines ya implementados |
| 🔵 | [1076961](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076961) Automatización | → | [1076953](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076953) Pruebas laboratorio | Las pruebas se ejecutan sobre el proceso ya automatizado |

> **Riesgo Sprint 3:** Es el sprint con más dependencias internas (5 🔵). La cadena crítica es **1081880 → 1081885 → 1081888** y **1081885 → 1096171 → 1096178**. Si la IaC (1081880) se retrasa, bloquea 4 HUs dentro del mismo sprint y 7 HUs en sprints posteriores.

---

### Sprint 4 — Dependencias internas + desde Sprint 3

| Tipo | HU origen | → | HU destino | Razón |
|:----:|-----------|---|------------|-------|
| 🔴 | [1096178](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096178) Parametrías Back _(S3)_ | → | [1096189](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096189) Parametrías Back parte 2 _(S4)_ | Continuación del módulo de parametrías (parte 1 → parte 2) |
| 🔴 | [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) Gestión estado Back _(S3)_ | → | [1096205](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096205) Gestión estado Front P1 _(S4)_ | El front consume los servicios back de estado del cliente |
| 🔵 | [1096205](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096205) Gestión estado Front P1 | → | [1096228](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096228) Gestión estado Front P2 | Parte 2 continúa las pantallas de la Parte 1 |
| 🔴 | [1076953](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076953) Pruebas laboratorio _(S3)_ | → | [1076956](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076956) Ejecución producción _(S4)_ | No se puede ejecutar en producción sin pruebas exitosas en laboratorio |
| 🔴🟡 | [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) Tipificar PJ _(S3, F3.1)_ | → | [1046415](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046415) Parametrizar códigos _(S4, F3.1)_ | Los códigos de requisitos dependen de que la tipificación por sociedad esté implementada |
| 🔴🟡 | [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) Tipificar PJ _(S3, F3.1)_ | → | [1046535](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046535) Relanzamiento P8 _(S4, F3.1)_ | El relanzamiento a P8 usa la nueva clasificación de tipo de sociedad |
| 🔴🟡 | [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) Tipificar PJ _(S3, F3.1)_ | → | [1079051](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079051) Requisitos por tipo — Back _(S4, F3.4)_ | Los requisitos diferenciados dependen de la clasificación por tipo de sociedad |
| 🔵 | [1046415](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046415) Parametrizar códigos | → | [1046438](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046438) Front requisitos | El front necesita los códigos parametrizados por el back |

> **Riesgo Sprint 4:** La HU [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) (Tipificar PJ, Sprint 3) es **punto único de fallo** para 3 HUs de Sprint 4 en 2 features distintas (3.1 y 3.4).

---

### Sprint 5 — Dependencias desde Sprints 3-4

| Tipo | HU origen | → | HU destino | Razón |
|:----:|-----------|---|------------|-------|
| 🔴 | [1096205](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096205) Gestión estado Front P1 _(S4)_ | → | [1096310](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096310) Parametrías Front P1 _(S5)_ | Las pantallas de parametrías reutilizan la base del front creado en S4 |
| 🔵 | [1096310](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096310) Parametrías Front P1 | → | [1096313](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096313) Parametrías Front P2 | Parte 2 continúa la Parte 1 |
| 🔴🟡 | [1079051](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079051) Requisitos tipo — Back _(S4, F3.4)_ | → | [1079058](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079058) Requisitos tipo — Front _(S5, F3.4)_ | El front consume el endpoint back de requisitos por tipo |
| 🔴🟡 | [1079051](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079051) Requisitos tipo — Back _(S4, F3.4)_ | → | [1079062](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079062) Requisitos tipo — Reintentos _(S5, F3.4)_ | Reintentos maneja fallback sobre el mismo proceso back |

---

### Cadenas críticas (dependencias transitivas)

Las siguientes son las secuencias más largas de HUs encadenadas que, si una falla, retrasan toda la cadena:

#### Cadena 1 — Datafactory (7 HUs, 4 sprints)

```
S1: 1076668 → 1076922 → S2: 1076945 → 1076947 → S3: 1076961 → 1076953 → S4: 1076956
```

| Longitud | Sprints afectados | Riesgo | Mitigación |
|:--------:|:-----------------:|--------|------------|
| 7 HUs | S1 → S4 | Alto — secuencia estricta sin paralelismo | Priorizar onboarding Datafactory el primer día del Sprint 1 |

#### Cadena 2 — Validador Identidad Admon (9 HUs, 3 sprints)

```
S3: 1081880 → 1081885 → 1096171 → 1096178 → S4: 1096189 / 1096205 → 1096228 → S5: 1096310 → 1096313
                    ↘ 1081888
```

| Longitud | Sprints afectados | Riesgo | Mitigación |
|:--------:|:-----------------:|--------|------------|
| 9 HUs | S3 → S5 | **Crítico** — la IaC y creación del micro son prerrequisito de todo | Crear repos y provisionar infra antes de Sprint 3. Ejecutar IaC (1081880) la primera semana |

#### Cadena 3 — Clasificación PJ → Requisitos (6 HUs, 3 sprints)

```
S3: 1026776 → S4: 1046415 → 1046438
                   1046535
                   1079051 → S5: 1079058
                                  1079062
```

| Longitud | Sprints afectados | Riesgo | Mitigación |
|:--------:|:-----------------:|--------|------------|
| 6 HUs | S3 → S5 | Medio — 1026776 es punto único de fallo para 2 features | Priorizar 1026776 al inicio del Sprint 3 |

#### Cadena 4 — Junta Directiva (6 HUs, 2 sprints)

```
S2: 1082241 → S3: 1082267
    1082249 → S3: 1082270
    1082281 → S3: 1082272
```

| Longitud | Sprints afectados | Riesgo | Mitigación |
|:--------:|:-----------------:|--------|------------|
| 6 HUs | S2 → S3 | Bajo — 3 pares independientes entre sí | Validar en demo de S2 para desbloquear front en S3 |

---

### Resumen de dependencias por sprint

| Sprint | 🔵 Intra-sprint | 🔴 Inter-sprint | 🟡 Cross-feature | Total |
|:------:|:----------------:|:----------------:|:-----------------:|:-----:|
| **1** | 2 | — | — | **2** |
| **2** | 2 | 4 | — | **6** |
| **3** | 5 | 3 | — | **8** |
| **4** | 2 | 4 | 3 | **9** |
| **5** | 1 | 2 | 2 | **5** |
| **Total** | **12** | **13** | **5** | **30** |

> **Conclusión:** Hay **30 dependencias** identificadas entre las 48 HUs. El Sprint 4 es el que tiene más dependencias totales (9), pero el Sprint 3 tiene más dependencias internas (5 🔵), lo que lo convierte en el sprint de mayor complejidad de coordinación. Las **3 cadenas críticas** principales son: Datafactory (7 HUs secuenciales), Validador Identidad Admon (9 HUs, riesgo crítico) y Clasificación PJ (6 HUs, punto único de fallo).

---

## Mapa de Impacto por Repositorio

> Cuántas HUs tocan cada repositorio, agrupadas por épica.

| Repositorio | Componente | É. 1107349 | É. 1079106 | É. 1105971 | **Total HUs** |
|-------------|-----------|-----------|-----------|-----------|:----------:|
| `sarlaft-fr` | Front formularios | 6 | 1 | 4 | **11** |
| `sarlaft-api` | API principal | 6 | 3 | 6 | **15** |
| `sarlaft-api-conf` | Config API | 3 | 1 | — | **4** |
| `sarlaft-brms` | Motor reglas (Drools) | 2 | — | 3 | **5** |
| `sarlaft-brms-conf` | Config motor | 1 | — | — | **1** |
| `sarlaft-admin` | Backweb admin | 1 | — | 2 | **3** |
| `sarlaft-batch` | Batch evaluaciones | — | 1 | 1 | **2** |
| `func-requisitos` | Azure Func requisitos | 3 | — | 3 | **6** |
| `func-requisitos-conf` | Config requisitos | 1 | — | 1 | **2** |
| `func-documental` | Azure Func P8 | 1 | — | 1 | **2** |
| `func-identity` | Azure Func identidad | — | 2 | 1 | **3** |
| `func-rrcc` | Azure Func RRCC | 1 | — | — | **1** |
| `validador-identidad-ms` | Backend Experian | — | 3 | — | **3** |
| `validador-identidad-conf` | Config/IaC validador | — | 1 | — | **1** |
| `sarlaft-clientes` | MS clientes ext. | — | 1 | 1 | **2** |
| **`validador-admon-ms`** _(nuevo)_ | Nuevo Back admin validador | — | 4 | — | **4** |
| **`validador-admon-fr`** _(nuevo)_ | Nuevo Front admin validador | — | 4 | — | **4** |
| Azure Data Factory | Pipelines depuración | — | 7 | — | **7** |

### Repositorios nuevos a crear

| Repositorio | Tecnología | Feature | Épica |
|-------------|-----------|---------|-------|
| `validador-admon-ms` | Java/Spring (Lego Sura), BD PostgreSQL, Azure Redis Cache, SEUS, Splunk | Feature 2.2 + 2.4 | 1079106 |
| `validador-admon-fr` | Angular (Lego Sura), SEUS4, Azure Pipelines | Feature 2.4 | 1079106 |

---

## Acciones Inmediatas Requeridas

1. **Refinamiento y estimación** — Ninguna de las 48 HUs tiene Story Points. Programar sesiones de refinamiento por épica.
2. **Asignación de responsables** — Todas las HUs están sin asignar.
3. **Mover estados** — Todas están en "New". Aprobar y mover a "Ready" las del Sprint 1.
4. **Crear repositorios nuevos** — `validador-admon-ms` y `validador-admon-fr` no existen aún. Coordinar con DevOps para su creación antes del Sprint 3.
5. **Provisionar Azure Data Factory** — Feature 2.3 requiere onboarding y configuración de Datafactory como primer paso (Sprint 1).
6. **Validar dependencias** entre Fase 1 (formularios) y Fase 3 (reglas de negocio).
7. **Definir capacidad del equipo** para calibrar la cantidad de HUs por sprint.

---

_Generado automáticamente el 2026-04-09 desde Azure DevOps (Org: SuraColombia, Proyecto: Gerencia_Tecnologia)_  
_Fuente técnica: Documentación Sarlaft 4.0 (`docs/Sarlaft40/DocumentacionTecnica/`) y repos locales (`desarrollo/`)_
