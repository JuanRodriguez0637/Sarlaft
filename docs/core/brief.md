# Brief del Proyecto — Fortalecimiento Sarlaft 4.0

## 1. Información General

| Campo | Detalle |
|---|---|
| **Cliente** | Suramericana S.A. (Sura) |
| **Proyecto** | Fortalecimiento Sarlaft 4.0 |
| **Coordinadora TI Cliente** | Elizabeth Zapata |
| **Líder Técnico Cliente** | Daniel Ruiz |
| **Analista Funcional Cliente** | Lady Diana Muñoz / Laura |
| **Modalidad** | Proyecto administrado (Método Ceiba) |
| **Fecha de briefing** | Febrero 2026 |

---

## 2. Contexto del Negocio

Suramericana, como empresa vigilada por la Superintendencia Financiera de Colombia, debe cumplir con los procedimientos **SARLAFT** (Sistema de Administración del Riesgo de Lavado de Activos y Financiación del Terrorismo).

En 2021 se implementó la plataforma **Sarlaft 4.0** en Azure, cubriendo procesos de expedición y reclamaciones. Desde entonces:
- Auditorías internas y revisiones de la Superintendencia han evidenciado **brechas recurrentes** y hallazgos repetitivos no corregidos.
- Los **indicadores de cubrimiento** se han deteriorado.
- La **Junta Directiva** ordenó cerrar las brechas: implementar todas las validaciones y fortalecer el sistema en todos los puntos requeridos.

El fortalecimiento busca cerrar esas brechas normativas, optimizar costos operativos en consultas a terceros (Experian, Registraduría, Migración Colombia) y completar funcionalidades pendientes en los formularios de conocimiento del cliente.

---

## 3. Objetivo del Proyecto

Implementar un conjunto de mejoras evolutivas y nuevas funcionalidades sobre la plataforma Sarlaft 4.0 existente, organizadas en dos grandes frentes:

1. **Modificaciones a Formularios** — Ajustar y completar los formularios de conocimiento del cliente (PN y PJ) para cumplimiento normativo.
2. **Optimización de BD y servicios externos** — Depurar la base de datos, reducir costos por consultas duplicadas a Experian/Registraduría/Migración y crear un nuevo microservicio de validación de identidad.

---

## 4. Alcance Funcional (Resumen)

### 4.1 Feature: Modificaciones Formulario

| ID | Historia | Puntos |
|---|---|---|
| 1025877 | Modificar campo actividad económica (CIIU 4) | 9 |
| 1025884 | Eliminar requisito Ingresos y Retenciones PN — Back Validación Adjuntos | 14 |
| 1026762 | Solicitar ingresos y egresos a PN y PJ | 9 |
| 1026765 | Solicitar activos y pasivos a PN y PJ | 9 |
| 1026770 | Solicitar requisitos por tipo de sociedad | 23 |
| 1026776 | Tipificar PJ por tipo de sociedad | 5 |
| 1032311 | Adicionar cláusula de tratamiento de datos | 15 |
| 1035467 | Adicionar figura de Junta Directiva en Datos Directivos | 64 |
| 1035950 | Eliminar requisito Ingresos y Retenciones PN — Back Requisitos | 9 |
| 1057319 | Cambiar a opcional el requisito "Ingresos y retenciones" | 15 |
| | **Subtotal Formularios** | **172** |

### 4.2 Feature: Optimización BD y Servicios Externos

| ID | Historia | Puntos |
|---|---|---|
| 1035141 | Depuración evaluaciones BD — Proceso automático (DataFactory) | 47 |
| 1035171 | Depuración evaluaciones BD — Histórico (one-off) | 5 |
| 1035498 | Evitar duplicidad validación identidad — Datos básicos | 4 |
| 1035500 | Evitar duplicidad consulta Registraduría | 26 |
| 1035502 | Evitar duplicidad validación identidad — Cuestionario | 4 |
| 1037054 | Evitar duplicidad consulta Migración Colombia | 4 |
| 1037085 | Reemplazar datos de consulta estado documento | 5 |
| 1037162 | Gestión del estado del documento del cliente (nuevo módulo admin) | 49 |
| | **Subtotal Optimización** | **144** |

| | **TOTAL** | **316 puntos** |
|---|---|---|

---

## 5. Contexto Técnico

- **Plataforma**: Azure (APIs, microservicios)
- **Arquitectura**: Backend en Java (arquitectura hexagonal), Frontend en Angular
- **Base de datos**: SQL Server (Azure)
- **Gestor documental**: IBM P8
- **Servicios externos**: Experian (Registraduría, Migración Colombia, validación de identidad)
- **Caché**: Azure Redis Cache
- **Procesamiento masivo**: Azure Data Factory, Databricks (evaluación)
- **Monitoreo**: Splunk, Dynatrace
- **Autenticación**: SEUS (sistema de autenticación Sura)
- **CI/CD**: Azure DevOps pipelines
- **Naturaleza predominante**: Backend pesado con ajustes de frontend (formularios y módulo administrativo nuevo)

---

## 6. Complejidades y Riesgos Identificados

| Riesgo | Mitigación |
|---|---|
| Integración con Experian (tercero) — no se tiene 100% control | Coordinación con proveedor, pruebas tempranas de integración |
| Nuevo microservicio de Validador de Identidad (infraestructura IaC nueva) | Sprint dedicado a onboarding de infraestructura |
| Depuración masiva de BD en producción — riesgo de integridad | Backup previo, ejecución por rangos de fechas, ventana no productiva |
| Azure Data Factory — curva de aprendizaje | Sprint de onboarding y configuración |
| Volumen alto de pruebas automatizadas a ajustar (impacto alto en flujos críticos) | QA dedicado, ejecución incremental |
| Pruebas de seguridad dinámicas — hallazgos impredecibles | Capacidad reservada para remediación (5 pts ya estimados) |

---

## 7. Premisas

1. La estimación base es de **316 puntos × 9 horas = 2,844 horas**.
2. Se espera una **reducción mínima del 30%** en tiempos de desarrollo mediante adopción de IA.
3. **Adopción de IA mínima del 80%** de las historias en el ciclo de desarrollo.
4. Las historias de usuario ya están **refinadas con criterios de aceptación** y estimadas por el equipo técnico de Sura.
5. No hay recolección retroactiva de datos para funcionalidades nuevas — solo desde salida a producción.
6. El componente de validación de identidad (Experian) se está desacoplando de Sarlaft como componente transversal.

---

## 8. Equipo Propuesto por el Cliente

| Rol | Cantidad |
|---|---|
| Desarrollador Full Stack | 3 |
| QA Automatizador | 1 |

Velocidad estimada: **27 puntos/sprint/desarrollador** → ~**11 sprints** con el equipo propuesto.

---

## 9. Entregables Esperados

- Historias de usuario implementadas, probadas y desplegadas en ambientes de desarrollo, laboratorio y producción.
- Pruebas unitarias, de integración (SoapUI), de seguridad y automatizadas.
- Ajustes de infraestructura IaC para nuevo microservicio.
- Pipelines de Data Factory para depuración de BD.
- Documentación técnica según estándares Sura.
