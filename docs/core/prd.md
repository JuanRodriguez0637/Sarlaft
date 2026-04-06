# PRD — Fortalecimiento Sarlaft 4.0
## Product Requirements Document

---

## 1. Visión del Producto

Fortalecer la plataforma Sarlaft 4.0 de Suramericana para cerrar brechas normativas identificadas por la Superintendencia Financiera, optimizar costos operativos en validaciones de identidad con terceros, y completar las funcionalidades de conocimiento del cliente en formularios de Persona Natural y Persona Jurídica.

---

## 2. Objetivos

| # | Objetivo | Métrica de éxito |
|---|---|---|
| O1 | Completar las validaciones de formularios SARLAFT para cumplimiento normativo | 100% de historias del Feature Formularios desplegadas en producción |
| O2 | Reducir costos por consultas duplicadas a Experian/Registraduría/Migración | Eliminación de consultas redundantes mediante caché y estados bloqueantes |
| O3 | Depurar la base de datos de evaluaciones obsoletas | Eliminación controlada de evaluaciones Pendientes (>6 meses) y Canceladas (>1 año) |
| O4 | Desacoplar el validador de identidad como componente transversal | Nuevo microservicio independiente desplegado |

---

## 3. Usuarios y Roles

| Usuario | Descripción |
|---|---|
| **Analista SARLAFT** | Opera los formularios de conocimiento del cliente. Principal usuario de las modificaciones de formularios. |
| **Administrador SARLAFT** | Configura parametrías, gestiona estados de documentos, administra reglas del motor. |
| **Sistemas terceros (APIs)** | Aliados y aplicativos de negocio que consumen APIs de creación de evaluaciones y guardado de formularios. |
| **Equipo de Operaciones** | Ejecuta y monitorea procesos de depuración y reintentos. |

---

## 4. Requisitos Funcionales

### 4.1 FEATURE: Modificaciones Formulario

---

#### RF-01: Modificar campo Actividad Económica (CIIU 4)
**ID Azure DevOps:** 1025877 | **Puntos:** 9

**Descripción:** Permitir buscar y seleccionar la Actividad Económica Principal (obligatoria) y Secundaria (opcional) usando exclusivamente el catálogo oficial CIIU versión 4 vigente.

**Alcance:**
- Persona Natural y Persona Jurídica
- Formularios: Ordinario e Intensificado
- Búsqueda por código, nombre o ambos
- Formato de resultados: `[código CIIU] – [nombre de la actividad]`
- Solo selección del catálogo (sin ingreso manual)

**Reglas de negocio:**
- Si el cliente tiene CIIU 4 registrada → precargar automáticamente
- Si el cliente tiene CIIU 3 registrada → NO precargar, solicitar diligenciamiento manual de CIIU 4
- Si no tiene actividad → campos vacíos
- Almacenamiento estructurado: código + descripción
- Trazabilidad: cliente, campo afectado, código/descripción CIIU, fecha/hora, origen, responsable

**Impacto técnico:**
- Modificar modelo BD: campo adicional en `tsaf_financiero` para actividad económica secundaria
- Ajustar servicio `/sarlaftserv/client/get` y `/clientes` para devolver actividad secundaria
- Ajustar servicio `/sarlaftserv/form/save` y `/formularios`
- Ajustar API terceros `/api/v1/form/save`
- Ajustar pantallas datos financieros en redirect y webcomponent (PN y PJ)

---

#### RF-02: Eliminar/Hacer opcional el requisito "Certificado de Ingresos y Retenciones"
**IDs Azure DevOps:** 1025884, 1035950, 1057319 | **Puntos:** 14 + 9 + 15 = 38

**Descripción:** Eliminar la obligatoriedad del documento "Certificado de Ingresos y Retenciones" en formularios de Persona Natural, haciéndolo opcional. Incluye validación de seguridad de archivos adjuntos.

**Alcance:**
- PN Riesgo Intensificado: documento pasa a opcional
- Sección de soportes: no se solicita como obligatorio
- La declaración de renta se mantiene como está

**Impacto técnico:**
- Ajustar tabla `tsaf_tipo_requisito`: campo de obligatoriedad
- Ajustar back para indicar obligatoriedad por soporte en consulta de evaluación
- Ajustar API terceros para indicar no obligatoriedad para PN
- Ajustar `DeterminarEstadoEvaluacion` para validar solo requisitos obligatorios
- Ajustar integración con app de requisitos (externo)
- Validación de archivos con Apache Tika (bytes, extensión, dominios permitidos)
- Ajustar formularios redirect y webcomponent
- Pruebas de seguridad dinámicas + capacidad para remediación (5 pts)

---

#### RF-03: Solicitar Ingresos y Egresos a PN y PJ
**ID Azure DevOps:** 1026762 | **Puntos:** 9

**Descripción:** Adicionar campos Ingresos y Egresos en la sección Datos Financieros para Persona Jurídica en formularios Ordinario e Intensificado.

**Reglas:**
- Campos numéricos, obligatorios
- No se permiten letras, caracteres especiales ni símbolos
- Precarga si existen datos previos, vacíos si no
- Solo último valor vigente (sin histórico)
- No hay recolección retroactiva

**Impacto técnico:**
- Validar servicio `/sarlaftserv/client/get` devuelva ingresos/egresos para PJ
- Ajustar servicios de guardado: campos obligatorios para PJ según tipo formulario
- Ajustar pantallas datos financieros (redirect y webcomponent) para PN y PJ
- Pruebas SoapUI, seguridad, flujos críticos (impacto medio)

---

#### RF-04: Solicitar Activos y Pasivos a PN y PJ
**ID Azure DevOps:** 1026765 | **Puntos:** 9

**Descripción:** Adicionar campos Activos y Pasivos en sección Datos Financieros para PN y PJ, formularios Ordinario e Intensificado.

**Reglas:**
- Activos: numérico, obligatorio, >= 10,000
- Pasivos: numérico, obligatorio, >= 0
- Mensajes de validación específicos por campo
- Precarga si existen datos, vacío si no
- Sin histórico

**Impacto técnico:**
- Validar servicio de consulta devuelva activos/pasivos para PN
- Ajustar servicios de guardado con obligatoriedad según tipo formulario
- Ajustar pantallas datos financieros (redirect y webcomponent) para PN
- Pruebas SoapUI, seguridad, flujos críticos (impacto medio)

---

#### RF-05: Solicitar requisitos por tipo de sociedad
**ID Azure DevOps:** 1026770 | **Puntos:** 23

**Descripción:** Configurar dinámicamente en la sección de Soportes los documentos que certifican existencia legal de PJ según su tipo de sociedad.

**Alcance:**
- PJ: Riesgo Simplificado, Ordinario e Intensificado
- Tabla de equivalencias tipo sociedad → documento requerido (18+ tipos)
- Integración con P8 (gestor documental): uso de código existente o creación de código interno
- Vigencia por tipo de riesgo: Simplificado/Ordinario = 3 años, Intensificado = 1 año
- Manejo de fallos de P8 sin bloquear formulario + reintentos

**Impacto técnico (3 HUs):**
- **HU Back (9 pts):** Parametrizar `tsaf_tipo_requisito`, propiedades P8, campo usuario en `tsaf_requisito`, actualizar motor de reglas
- **HU Front (9 pts):** Ajustar front para usar `soportesRequeridos` del servicio
- **HU Reintentos (5 pts):** Proceso nocturno en `sarlaftbatch`, columna Reintento en `tsaf_notificacion`, circuit breaker con log en Splunk, máximo 3 reintentos

---

#### RF-06: Tipificar PJ por tipo de sociedad
**ID Azure DevOps:** 1026776 | **Puntos:** 5

**Descripción:** Tipificar automáticamente a las PJ por tipo de sociedad y clasificación analizando la razón social con reglas de coincidencia por denominación.

**Reglas:**
- Catálogo de denominaciones: Sociedad comercial, Estructura sin personería jurídica, Sin ánimo de lucro, Entidad estatal, Otros
- Priorizar coincidencia más específica
- Si empate → log de inconsistencias + permitir actualización
- Si no hay coincidencia → Clasificación: "Otros", Tipo: "Otros"
- No editable una vez tipificado
- No tipificación retroactiva

**Impacto técnico:**
- Parametrizar tabla de denominaciones en Catálogo y Parámetros → cargar en caché
- Adicionar 3 campos a `tsaf_cliente`: clasificación, tipo PJ, usuario que actualiza
- Actualizar modelo de cliente en `sarlaftapi` para cálculo automático en servicios: assessment, evaluaciones, API terceros, formularios terceros

---

#### RF-07: Adicionar cláusula de tratamiento de datos
**ID Azure DevOps:** 1032311 | **Puntos:** 15

**Descripción:** Incluir obligatoriamente la cláusula de tratamiento de datos personales en todos los formularios (negocio nuevo, reclamaciones, actualización).

**Reglas:**
- Pantalla posterior a "Conocerte es muy importante para nosotros"
- Radio buttons: "Sí, autorizo" / "No autorizo" — selección obligatoria
- Texto parametrizable (sin cambio de código)
- Envío al servicio de Modelo de Clientes (envío masivo diario)
- Log de errores para respuestas no procesadas
- Autorización asociada al cliente que diligencia (tomador para negocio nuevo, beneficiario para reclamación)
- Solo registros desde salida a producción (sin migración histórica)

**Impacto técnico:**
- Nueva tabla de autorizaciones asociada al cliente
- Ajustar servicio `/sarlaftserv/client/get` para devolver autorización
- Ajustar servicios de guardado (`/sarlaftserv/form/save`, `/api/v1/form/save`)
- Ajustar servicio de consulta por evaluación (`/sarlaftbackweb/resultevaluation`)
- Nueva pantalla en formularios redirect y webcomponent (PN y PJ)
- Ajustar módulo de consultas
- Pruebas de seguridad back y front, SoapUI, automatizadas (impacto alto)

---

#### RF-08: Adicionar figura de Junta Directiva en Datos Directivos
**ID Azure DevOps:** 1035467 | **Puntos:** 64

**Descripción:** Crear la figura/rol "Junta Directiva" en el módulo de Datos Directivos para PJ con clasificación Sociedad Comercial.

**Reglas:**
- Visible solo para PJ + Sociedad Comercial
- Habilitación del sub-bloque si accionistas capturados alcanzan ≥ 50% de participación
- S.A.: junta obligatoria por ley; S.A.S., Ltda., etc.: opcional por estatutos
- Campos: Tipo ID, Número ID, Primer nombre, Segundo nombre, Primer apellido, Segundo apellido, País de nacimiento
- Validaciones SARLAFT: listas de control, PEP, fachada DIAN, ADRES, Registraduría, Migración
- Parametrizable por clasificación (sin despliegue de código)
- Sin histórico, solo datos nuevos

**Impacto técnico (6 HUs):**
- **HU Back (14 pts):** Nuevo tipo de figura en dominio, casos de uso (agregar/eliminar/validar), reglas de estado evaluación (>50% accionistas), servicios getForm/formularios, logs Splunk
- **HU Motor (9 pts):** PrepararEvaluacion y DeterminarEstadoEvaluacion
- **HU Front (14 pts):** Nuevo componente sección junta directiva (redirect y webcomponent), integración en datos-directivos PJ
- **HU Validación RRCC (9 pts):** Cache marcaciones ADRES/DIAN, nuevas evidencias en motor, clases de validación con adaptadores
- **HU Parametrización Back (9 pts):** Tabla parametrización por clasificación/tipo PJ, servicios web CRUD
- **HU Parametrización Front (9 pts):** Pantalla administrativa para gestionar parametrización

---

### 4.2 FEATURE: Optimización BD y Servicios Externos

---

#### RF-09: Depuración evaluaciones BD — Proceso automático
**ID Azure DevOps:** 1035141 | **Puntos:** 47

**Descripción:** Implementar proceso de depuración periódica de evaluaciones en estado Pendiente (semestral, >6 meses) y Cancelado (anual, >1 año) para operaciones de negocio nuevo y reclamaciones.

**Reglas:**
- Ejecución en ventana no productiva
- No eliminar tablas de clientes, direcciones, información financiera, asociaciones
- Trazabilidad completa: id_evaluacion, estado_original, fecha_creacion, tipo_lote, origen_operacion, accion_ejecutada, motivo_decision, fecha_ejecucion_lote, id_lote
- Indicadores de cobertura: total generadas, procesadas, eliminadas, preservadas, con error
- Alerta si cobertura < 100%
- Rollback controlado en caso de error

**Impacto técnico (5 HUs + 2 Tareas):**
- **HU Onboarding DataFactory (9 pts):** Aprendizaje, linked services, KeyVault, pipelines CI/CD
- **HU Diseño pipelines (3 pts):** Pipeline consulta + pipeline depuración, nueva tabla de depuraciones
- **HU Pipeline consulta (3 pts):** Implementación pipeline de identificación de evaluaciones
- **HU Pipeline depuración (5 pts):** Implementación pipeline de eliminación por lotes con manejo de errores y timeouts
- **Tarea Pruebas laboratorio (18 pts):** 2 sprints de pruebas incluyendo posible refactor con Databricks
- **Tarea Ejecución producción (5 pts):** Backup BD, pruebas iniciales en producción
- **HU Automatización (4 pts):** Automatización en servidor de procesos masivos

---

#### RF-10: Depuración evaluaciones BD — Histórico (one-off)
**ID Azure DevOps:** 1035171 | **Puntos:** 5

**Descripción:** Depuración histórica única de evaluaciones Pendientes y Canceladas creadas entre 01/01/2021 y 31/12/2024.

**Impacto técnico:**
- Queries de identificación y Delete para tablas: evaluacion, evidencia, figura, notificacion, poliza, requisito, riesgo, sarlaft, token
- Ejecución fragmentada por rangos de fechas
- Foto BD antes y después, foto Dynatrace tiempos de servicios
- Coordinación con Kyndryl para backup y acompañamiento

---

#### RF-11: Evitar duplicidad consulta Registraduría
**ID Azure DevOps:** 1035500 | **Puntos:** 26

**Descripción:** Crear un nuevo microservicio (Validador de Identidad) que verifique estados bloqueantes antes de ejecutar consultas a Registraduría vía Experian para CC. Rechazar evaluaciones cuando existan estados definitivos previos.

**Estados bloqueantes permanentes:** Cancelada, Cancelada por intento de suplantación, Doble cedulación, Fallecido, Falsa identidad
**Estados bloqueantes temporales (1 mes):** En tramite, El número de identificación enviado no existe

**Impacto técnico (3 HUs):**
- **HU Front Sarlaft (3 pts):** Adicionar resultado validación registraduría a pantalla detalles de figuras
- **HU IAC (9 pts):** Creación infraestructura IaC para el nuevo microservicio 1101
- **HU Validador Admon MS (9 pts):** Nuevo microservicio con Lego Sura, pipeline Azure, conexión BD nueva, Redis Cache, modelo de parametría de rechazos
- **HU Validador MS (5 pts):** Lógica de cache, consulta parametría, decisión de rechazo automático o invocación a Experian, logs de herencia

---

#### RF-12: Evitar duplicidad validación identidad — Datos básicos
**ID Azure DevOps:** 1035498 | **Puntos:** 4

**Descripción:** Verificar estados bloqueantes del cuestionario de datos básicos antes del flujo de validación de identidad (CC, CE, PPT). Rechazo temporal de 1 mes.

**Estados bloqueantes:** EXCEDIDO NÚMERO DE INTENTOS, NO EXISTE IDENTIFICACIÓN, NO FUE POSIBLE REALIZAR LA VALIDACIÓN

**Impacto técnico:** Reutiliza implementaciones de RF-11. Consulta cache, parametría, decisión automática.

---

#### RF-13: Evitar duplicidad validación identidad — Cuestionario
**ID Azure DevOps:** 1035502 | **Puntos:** 4

**Descripción:** Verificar estados bloqueantes del cuestionario de preguntas antes del flujo de validación de identidad.

**Estados bloqueantes diarios:** EXCEDIÓ INTENTOS POR DÍA, EXCEDIÓ INGRESOS PRODUCTO POR DÍA
**Estados bloqueantes mensuales:** EXCEDIÓ INTENTOS POR MES, NO HAY SUFICIENTES PREGUNTAS, EXCEDIÓ INGRESOS PRODUCTO POR MES

**Impacto técnico:** Reutiliza implementaciones de RF-11.

---

#### RF-14: Evitar duplicidad consulta Migración Colombia
**ID Azure DevOps:** 1037054 | **Puntos:** 4

**Descripción:** Verificar estados bloqueantes antes de consultar Migración Colombia vía Experian (CE, PPT). Rechazo temporal de 1 mes.

**Estados bloqueantes:** Inactivo, Cancelado, El número de identificación enviado no existe

**Impacto técnico:** Reutiliza implementaciones de RF-11.

---

#### RF-15: Reemplazar datos de consulta estado documento
**ID Azure DevOps:** 1037085 | **Puntos:** 5

**Descripción:** Posterior a consulta de estado del documento, validar y corregir automáticamente 1er apellido, 2do apellido, fecha de expedición del cliente si hay diferencias con Registraduría/Migración. Guardar nacionalidad tal como la entrega el servicio.

**Aplica para estados:** VIGENTE, CANCELADO, INACTIVO, CANCELADO POR DUPLICIDAD, FALLECIDO, FALSA IDENTIDAD

**Impacto técnico:**
- Modificar `tsaf_cliente`: campo nacionalidad
- Nuevo caso de uso para actualización del cliente
- Crear operación en `ClienteRepositoryAdapter`
- Invocar después de consultas a Registraduría/Migración
- Logs en Splunk (campos antes/después, resultado)

---

#### RF-16: Gestión del estado del documento del cliente
**ID Azure DevOps:** 1037162 | **Puntos:** 49

**Descripción:** Nuevo módulo administrativo (front + back) para consultar y cambiar estados de documentos almacenados desde validaciones con Registraduría/Migración. Incluye gestión de parametrías de reglas de bloqueo.

**Funcionalidades:**
- Consultar cliente por tipo/número de ID
- Grilla con resultados: Número ID, Nombre, Estado actual, Estado a cambiar, Fecha, Acción
- Cambio controlado de estado (solo con perfil Administrador)
- Mensajes de éxito/error estandarizados
- Pantalla de administración de reglas de bloqueo (tipo, estado, vigencia)
- CRUD de parametrías
- Trazabilidad completa y auditable

**Impacto técnico (7 HUs):**
- **HU Back — Gestión estado (9 pts):** Servicios consultar/desactivar bloqueos, autenticación SEUS
- **HU Back — Parametrías v1 (9 pts):** Servicios consultar/actualizar reglas, auditoría BD
- **HU Back — Parametrías v2 (5 pts):** Servicios eliminar/crear reglas
- **HU Front — Setup (5 pts):** Nuevo front Angular con Lego Sura, SEUS, pipeline CI/CD
- **HU Front — Gestión estado (9 pts):** Pantalla consulta y desactivación de bloqueos
- **HU Front — Parametrías v1 (6 pts):** Pantalla consulta y actualización de reglas
- **HU Front — Parametrías v2 (6 pts):** Pantalla eliminación y creación de reglas

---

## 5. Requisitos No Funcionales

| Categoría | Requisito |
|---|---|
| **Seguridad** | Pruebas de seguridad dinámicas en back y front. Validación de archivos adjuntos con Apache Tika. Autenticación/autorización con SEUS para todos los servicios. |
| **Rendimiento** | Búsquedas en formularios con respuesta en tiempo operativo razonable. Depuración BD en ventana no productiva sin afectar transacciones. |
| **Trazabilidad** | Logs en Splunk para operaciones críticas. Registros de auditoría en BD para cambios de estado, parametrías, y datos del cliente. |
| **Parametrización** | Textos de cláusulas, tipos de sociedad, reglas de bloqueo, requisitos documentales: configurables sin cambio de código. |
| **Disponibilidad** | Fallos en P8 o servicios externos no deben bloquear formularios. Circuit breaker con reintentos controlados. |
| **Caché** | Catálogos CIIU, denominaciones de sociedades, parametrías de bloqueo: cargados en Azure Redis Cache. |

---

## 6. Dependencias

| Dependencia | Descripción | Responsable |
|---|---|---|
| Experian | Servicio de consulta Registraduría, Migración Colombia, validación de identidad | Externo |
| IBM P8 | Gestor documental para carga de requisitos | Externo |
| Modelo de Clientes | Servicio para sincronizar autorización de tratamiento de datos | Equipo interno Sura |
| Gestión Documental | Propiedades documentales de P8 por requisito | Equipo interno Sura |
| SEUS | Autenticación/autorización | Infraestructura Sura |
| Azure Data Factory | Pipelines de depuración (requiere onboarding) | Equipo de desarrollo |
| Kyndryl | Acompañamiento para backup y depuración en producción | Proveedor Sura |
| DataLake | Consulta de datos para auditoría (alternativa a archivo de validación "Otros") | Equipo datos Sura |

---

## 7. Fuera de Alcance

- Integración directa con el Modelo de Clientes para sincronización en tiempo real de tratamiento de datos.
- Recolección retroactiva de información para clientes existentes sin datos previos.
- Tipificación retroactiva de PJ ya almacenadas.
- Migración o reconstrucción de datos históricos de autorizaciones.
- Procesos de actualización (diferentes a negocio nuevo y reclamaciones) para depuración de BD.
- Ajustes en el frontend del módulo de clientes Sura (el front del validador de identidad es un aplicativo nuevo separado).

---

## 8. Resumen de Esfuerzo

| Feature | Historias | Puntos | % del total |
|---|---|---|---|
| Modificaciones Formulario | 10 | 172 | 54% |
| Optimización BD y Servicios | 8 | 144 | 46% |
| **Total** | **18** | **316** | **100%** |

**Conversión:** 316 puntos × 9 horas/punto = **2,844 horas base**
**Con reducción IA 30%:** ~**1,991 horas objetivo**
