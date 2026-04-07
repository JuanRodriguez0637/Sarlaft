# Análisis de Requisitos Funcionales — Fortalecimiento Sarlaft 4.0

**Fuentes:** PRD (docs/core/prd.md), Brief (docs/core/brief.md), Documentación Técnica (docs/Sarlaft40/DocumentacionTecnica/)
**Fecha de análisis:** Abril 2026

---

## 1. Resumen Ejecutivo

El sistema **Sarlaft 4.0** es la plataforma de Suramericana para el cumplimiento normativo SARLAFT (Sistema de Administración del Riesgo de Lavado de Activos y Financiación del Terrorismo). Opera sobre una arquitectura de microservicios en Azure con:

- **Backend:** Java (arquitectura hexagonal) — microservicios: SarlaftAPI, MotorEvaluación, Backweb, SarlaftBatch, SarlaftClientes, Webhook, PEPS
- **Frontend:** Angular (Web Component + modo Redirect), base de formularios de conocimiento del cliente
- **Base de datos:** PostgreSQL (Azure)
- **Integraciones:** Experian, IBM P8, SEUS, Modelo de Clientes, RabbitMQ, Azure Redis Cache, Azure Data Factory

El proyecto de fortalecimiento introduce **16 requisitos funcionales** agrupados en dos features, derivados de brechas normativas identificadas por la Superintendencia Financiera y optimizaciones operativas.

---

## 2. Catálogo de Requisitos Funcionales

### Convenciones de prioridad

| Prioridad | Criterio |
|-----------|----------|
| **Alta** | Cierre de brecha normativa directa, bloqueo de flujos críticos, o impacto > 20 pts |
| **Media** | Optimización de costos, mejora operativa, impacto 9–20 pts |
| **Baja** | Tareas puntuales, ajustes de datos, impacto < 9 pts |

---

## 3. FEATURE 1 — Modificaciones a Formularios

> Objetivo: completar y ajustar los formularios de conocimiento del cliente (PN y PJ) para cumplimiento normativo.

### RF-01 — Modificar campo Actividad Económica (CIIU 4)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1025877 |
| **Prioridad** | Media |
| **Esfuerzo** | 9 puntos |
| **Actores** | Analista SARLAFT, Sistemas terceros (APIs) |
| **Formularios** | PN Ordinario, PN Intensificado, PJ Ordinario, PJ Intensificado |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) |

**Descripción:**
El sistema debe permitir buscar y seleccionar la Actividad Económica Principal (obligatoria) y Secundaria (opcional) usando exclusivamente el catálogo oficial CIIU versión 4 vigente. No se permite ingreso manual.

**Reglas de negocio:**

1. La búsqueda debe soportar consulta por código, nombre, o ambos simultáneamente.
2. Los resultados deben mostrarse en formato `[código CIIU] – [nombre de la actividad]`.
3. Si el cliente tiene CIIU 4 registrada → precargar automáticamente en el formulario.
4. Si el cliente tiene CIIU 3 registrada → **no** precargar; solicitar diligenciamiento manual de CIIU 4.
5. Si el cliente no tiene actividad registrada → campos vacíos.
6. El almacenamiento debe ser estructurado: código + descripción por separado.
7. Toda modificación debe quedar en trazabilidad: cliente, campo afectado, código/descripción CIIU, fecha/hora, origen, responsable.

**Impacto técnico identificado (desde documentación técnica):**

- Modificar modelo BD: campo adicional en `tsaf_financiero` para actividad económica secundaria.
- Ajustar servicios `/sarlaftserv/client/get` y `/clientes` para devolver actividad secundaria.
- Ajustar servicios `/sarlaftserv/form/save`, `/formularios` y `/api/v1/form/save`.
- Actualizar pantallas de datos financieros en formulario redirect y web component (PN y PJ).

---

### RF-02 — Hacer opcional el Certificado de Ingresos y Retenciones (PN)

| Atributo | Detalle |
|----------|---------|
| **IDs Azure DevOps** | 1025884, 1035950, 1057319 |
| **Prioridad** | Alta |
| **Esfuerzo** | 38 puntos (14 + 9 + 15) |
| **Actores** | Analista SARLAFT, Sistemas terceros (APIs) |
| **Formularios** | PN Riesgo Intensificado |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-brms-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms), [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr), [892-sarlaft-function_requisitos-conf](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_requisitos-conf) |

**Descripción:**
El documento "Certificado de Ingresos y Retenciones" debe dejar de ser obligatorio en los formularios de Persona Natural Riesgo Intensificado. El campo pasa a ser opcional; la declaración de renta no se modifica.

**Reglas de negocio:**

1. El sistema debe marcar el soporte como no obligatorio para PN en la tabla `tsaf_tipo_requisito`.
2. El back debe indicar la obligatoriedad de cada soporte al consultar la evaluación.
3. La API de terceros debe reflejar que el documento no es obligatorio para PN.
4. `DeterminarEstadoEvaluacion` debe validar **únicamente** los soportes marcados como obligatorios.
5. Los archivos adjuntos deben ser validados con Apache Tika: verificar tipo MIME real (no solo extensión), tamaño máximo y dominios permitidos.
6. La integración con la app externa de requisitos debe reflejar el cambio de obligatoriedad.

**Nota de seguridad:** La validación de archivos con Apache Tika es un control de seguridad crítico (OWASP A05 – Security Misconfiguration / File Upload). Debe validar bytes del archivo, no solo extensión declarada.

---

### RF-03 — Solicitar Ingresos y Egresos (PJ)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1026762 |
| **Prioridad** | Media |
| **Esfuerzo** | 9 puntos |
| **Actores** | Analista SARLAFT, Sistemas terceros (APIs) |
| **Formularios** | PJ Ordinario, PJ Intensificado |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) |

**Descripción:**
Se deben adicionar campos de Ingresos y Egresos en la sección Datos Financieros para Persona Jurídica.

**Reglas de negocio:**

1. Los campos son numéricos y obligatorios para PJ.
2. No se permiten letras, caracteres especiales ni símbolos monetarios.
3. Si existen datos previos → precargar; si no → campos vacíos.
4. Solo se captura el último valor vigente: sin recolección histórica ni retroactividad.
5. El servicio `/sarlaftserv/client/get` debe devolver ingresos y egresos para PJ.

---

### RF-04 — Solicitar Activos y Pasivos (PN y PJ)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1026765 |
| **Prioridad** | Media |
| **Esfuerzo** | 9 puntos |
| **Actores** | Analista SARLAFT, Sistemas terceros (APIs) |
| **Formularios** | PN Ordinario, PN Intensificado, PJ Ordinario, PJ Intensificado |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) |

**Descripción:**
Se deben adicionar campos de Activos y Pasivos en la sección Datos Financieros para PN y PJ.

**Reglas de negocio:**

1. Activos: numérico, obligatorio, valor mínimo aceptado = 10,000.
2. Pasivos: numérico, obligatorio, valor mínimo aceptado = 0.
3. Los mensajes de validación deben ser específicos por campo.
4. Si existen datos previos → precargar; si no → campos vacíos.
5. Sin histórico ni retroactividad.

---

### RF-05 — Solicitar requisitos documentales por tipo de sociedad (PJ)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1026770 |
| **Prioridad** | Alta |
| **Esfuerzo** | 23 puntos |
| **Actores** | Analista SARLAFT, Administrador SARLAFT, Sistemas terceros (APIs) |
| **Formularios** | PJ Riesgo Simplificado, Ordinario, Intensificado |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-brms-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms), [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr), [892-sarlaft-batch-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-batch-ms), [892-sarlaft_function_documental-mi](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_function_documental-mi) |

**Descripción:**
La sección de Soportes debe mostrar dinámicamente los documentos requeridos para certificar la existencia legal de la PJ según su tipo de sociedad, configurados mediante tabla de equivalencias (18+ tipos de sociedad).

**Reglas de negocio:**

1. Cada tipo de sociedad tiene un documento requerido mapeado en tabla de equivalencias parametrizable.
2. La vigencia del documento varía por nivel de riesgo: Simplificado/Ordinario = 3 años; Intensificado = 1 año.
3. Si el código P8 del documento existe → usar código existente. Si no → crear código interno.
4. Los fallos de P8 **no deben bloquear** el formulario; debe quedar en estado pendiente con reintento nocturno.
5. El proceso de reintentos (en `sarlaftbatch`) tiene un máximo de **3 reintentos** por registro.
6. Cada intento debe registrarse en la columna `Reintento` de `tsaf_notificacion`.
7. Los fallos deben activar el circuit breaker y registrar log en Splunk.

---

### RF-06 — Tipificar PJ por tipo de sociedad

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1026776 |
| **Prioridad** | Media |
| **Esfuerzo** | 5 puntos |
| **Actores** | SarlaftAPI (automático) |
| **Formularios** | PJ (todos) |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-brms-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms) |

**Descripción:**
El sistema debe tipificar automáticamente a las PJ por tipo de sociedad y clasificación, analizando la razón social con reglas de coincidencia por denominación.

**Reglas de negocio:**

1. El catálogo de denominaciones incluye: Sociedad Comercial, Estructura sin Personería Jurídica, Sin Ánimo de Lucro, Entidad Estatal, Otros.
2. Se debe priorizar la coincidencia más específica en la razón social.
3. Si hay empate → registrar log de inconsistencia y permitir actualización manual.
4. Si no hay coincidencia → Clasificación: "Otros", Tipo: "Otros".
5. Una vez tipificado, el campo **no es editable**.
6. Sin tipificación retroactiva para PJ ya almacenadas.
7. El catálogo de denominaciones se carga en caché (Azure Redis).
8. Se deben agregar 3 campos a `tsaf_cliente`: clasificación, tipo PJ, usuario que actualiza.

---

### RF-07 — Adicionar cláusula de tratamiento de datos personales

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1032311 |
| **Prioridad** | Alta |
| **Esfuerzo** | 15 puntos |
| **Actores** | Analista SARLAFT, Sistemas terceros (APIs), Modelo de Clientes |
| **Formularios** | PN y PJ — Negocio nuevo, Reclamaciones, Actualización |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-admin-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-ms), [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) |

**Descripción:**
Todos los formularios deben incluir una pantalla de autorización de tratamiento de datos personales, posterior a la pantalla de bienvenida.

**Reglas de negocio:**

1. La pantalla aparece después de "Conocerte es muy importante para nosotros".
2. Muestra radio buttons: "Sí, autorizo" / "No autorizo" — selección obligatoria para continuar.
3. El texto de la cláusula es parametrizable sin cambio de código.
4. La autorización se asocia al cliente que diligencia: tomador (negocio nuevo / actualización), beneficiario (reclamación).
5. Las autorizaciones se envían al servicio de Modelo de Clientes en envío masivo diario (no tiempo real).
6. Los errores de respuesta del Modelo de Clientes deben quedar en log.
7. Solo se registran autorizaciones desde la salida a producción: sin migración histórica.

---

### RF-08 — Adicionar figura de Junta Directiva (PJ Sociedad Comercial)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1035467 |
| **Prioridad** | Alta |
| **Esfuerzo** | 64 puntos |
| **Actores** | Analista SARLAFT, Administrador SARLAFT |
| **Formularios** | PJ Sociedad Comercial |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [892-sarlaft-brms-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms), [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) |

**Descripción:**
El módulo de Datos Directivos para PJ con clasificación "Sociedad Comercial" debe habilitar la figura/rol "Junta Directiva", con sus respectivas validaciones SARLAFT.

**Reglas de negocio:**

1. La sección de Junta Directiva solo es visible para PJ + Clasificación: Sociedad Comercial.
2. El sub-bloque se habilita automáticamente cuando los accionistas capturados alcanzan ≥ 50% de participación.
3. Para S.A.: la junta es obligatoria por ley. Para S.A.S., Ltda. y otras: es opcional según estatutos.
4. Campos de cada miembro de junta: Tipo ID, Número ID, Primer nombre, Segundo nombre, Primer apellido, Segundo apellido, País de nacimiento.
5. Cada miembro debe pasar por validaciones SARLAFT: listas de control, PEP, fachada DIAN, ADRES, Registraduría, Migración Colombia.
6. El marcado de ADRES y DIAN debe usar caché para evitar consultas duplicadas.
7. La configuración de qué clasificaciones/tipos de PJ tienen Junta Directiva debe ser parametrizable sin despliegue de código (CRUD administrativo).
8. Sin datos históricos; solo datos nuevos capturados desde producción.

---

## 4. FEATURE 2 — Optimización BD y Servicios Externos

> Objetivo: depurar la base de datos, reducir costos por consultas duplicadas a Experian/Registraduría/Migración y crear el microservicio de validación de identidad.

### RF-09 — Depuración periódica de evaluaciones (proceso automático)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1035141 |
| **Prioridad** | Alta |
| **Esfuerzo** | 47 puntos |
| **Actores** | Equipo de Operaciones |
| **Componente** | Azure Data Factory, sarlaftbatch |
| **Repositorios** | [892-sarlaft-batch-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-batch-ms) *(+ pipelines Azure Data Factory — fuera de repositorios Git)* |

**Descripción:**
Implementar un proceso automático periódico de depuración de evaluaciones en estado Pendiente (antigüedad > 6 meses) y Cancelado (antigüedad > 1 año) para operaciones de negocio nuevo y reclamaciones.

**Reglas de negocio:**

1. La ejecución debe ocurrir exclusivamente en **ventana no productiva**.
2. No se deben eliminar: tablas de clientes, direcciones, información financiera, ni asociaciones.
3. Se deben eliminar registros en: evaluacion, evidencia, figura, notificacion, poliza, requisito, riesgo, sarlaft, token.
4. Cada operación debe quedar en trazabilidad completa: id_evaluacion, estado_original, fecha_creacion, tipo_lote, origen_operacion, accion_ejecutada, motivo_decision, fecha_ejecucion_lote, id_lote.
5. Indicadores de cobertura obligatorios: total generadas, procesadas, eliminadas, preservadas, con error.
6. Si cobertura < 100% → emitir alerta.
7. Ante cualquier error → rollback controlado del lote afectado.
8. El proceso debe ser automatizable en el servidor de procesos masivos.

---

### RF-10 — Depuración histórica puntual de evaluaciones (one-off)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1035171 |
| **Prioridad** | Alta |
| **Esfuerzo** | 5 puntos |
| **Actores** | Equipo de Operaciones, Kyndryl |
| **Componente** | Base de datos PostgreSQL |
| **Repositorios** | *(scripts SQL directos — sin repositorio de código; coordinación con Kyndryl)* |

**Descripción:**
Ejecución única de depuración de evaluaciones Pendiente y Canceladas creadas entre el 01/01/2021 y el 31/12/2024.

**Reglas de negocio:**

1. La depuración opera sobre las mismas tablas que RF-09.
2. La ejecución debe ser fragmentada por rangos de fechas para controlar el impacto.
3. Se debe tomar foto del estado de BD antes y después de la ejecución.
4. Se debe tomar foto de tiempos de servicios en Dynatrace antes y después.
5. Requiere backup coordinado con Kyndryl previo a la ejecución.

---

### RF-11 — Evitar duplicidad de consultas a Registraduría (CC)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1035500 |
| **Prioridad** | Alta |
| **Esfuerzo** | 26 puntos |
| **Actores** | SarlaftAPI (automático), Administrador SARLAFT |
| **Componente** | Nuevo microservicio Validador de Identidad (MS 1101) |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [1101-validadorcliente_identidad-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) ⚠️ *(pendiente creación — no existe en Azure DevOps, verificado 06/04/2026)*, [892-sarlaft-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) |

**Descripción:**
Crear un nuevo microservicio independiente (Validador de Identidad) que verifique estados bloqueantes antes de ejecutar consultas a Registraduría vía Experian para documentos tipo CC, evitando consultas redundantes y costosas.

**Reglas de negocio:**

1. **Estados bloqueantes permanentes** (rechazo sin expiración): Cancelada, Cancelada por intento de suplantación, Doble cedulación, Fallecido, Falsa identidad.
2. **Estados bloqueantes temporales** (rechazo por 1 mes): En tramite, El número de identificación enviado no existe.
3. Si existe un estado bloqueante vigente → rechazar la evaluación automáticamente sin invocar Experian.
4. Si no existe estado bloqueante → invocar Experian normalmente.
5. El microservicio debe usar Azure Redis Cache para los estados consultados previamente.
6. La parametría de reglas de rechazo debe ser administrable (CRUD) desde el módulo de gestión de estado del documento (ver RF-16).
7. Toda decisión de rechazo debe registrarse en log de herencia.
8. El resultado de la validación de Registraduría debe mostrarse en la pantalla de detalles de figuras (front Sarlaft).
9. El microservicio requiere infraestructura IaC nueva (pipeline Azure, BD nueva, Redis Cache).

---

### RF-12 — Evitar duplicidad en validación de identidad — Datos básicos (CC, CE, PPT)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1035498 |
| **Prioridad** | Media |
| **Esfuerzo** | 4 puntos |
| **Actores** | SarlaftAPI (automático) |
| **Componente** | Validador de Identidad (reutiliza RF-11) |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [1101-validadorcliente_identidad-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) ⚠️ *(pendiente creación — no existe en Azure DevOps, verificado 06/04/2026)* |

**Descripción:**
Verificar estados bloqueantes del cuestionario de datos básicos antes de iniciar el flujo de validación de identidad para documentos CC, CE y PPT.

**Reglas de negocio:**

1. **Estados bloqueantes** (rechazo temporal de 1 mes): EXCEDIDO NÚMERO DE INTENTOS, NO EXISTE IDENTIFICACIÓN, NO FUE POSIBLE REALIZAR LA VALIDACIÓN.
2. Reutiliza los mecanismos de caché, parametría y decisión automática implementados en RF-11.

---

### RF-13 — Evitar duplicidad en validación de identidad — Cuestionario

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1035502 |
| **Prioridad** | Media |
| **Esfuerzo** | 4 puntos |
| **Actores** | SarlaftAPI (automático) |
| **Componente** | Validador de Identidad (reutiliza RF-11) |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [1101-validadorcliente_identidad-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) ⚠️ *(pendiente creación — no existe en Azure DevOps, verificado 06/04/2026)* |

**Descripción:**
Verificar estados bloqueantes del cuestionario de preguntas antes de iniciar el flujo de validación de identidad.

**Reglas de negocio:**

1. **Estados bloqueantes diarios**: EXCEDIÓ INTENTOS POR DÍA, EXCEDIÓ INGRESOS PRODUCTO POR DÍA.
2. **Estados bloqueantes mensuales**: EXCEDIÓ INTENTOS POR MES, NO HAY SUFICIENTES PREGUNTAS, EXCEDIÓ INGRESOS PRODUCTO POR MES.
3. Reutiliza los mecanismos de caché, parametría y decisión automática implementados en RF-11.

---

### RF-14 — Evitar duplicidad de consultas a Migración Colombia (CE, PPT)

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1037054 |
| **Prioridad** | Media |
| **Esfuerzo** | 4 puntos |
| **Actores** | SarlaftAPI (automático) |
| **Componente** | Validador de Identidad (reutiliza RF-11) |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [1101-validadorcliente_identidad-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) ⚠️ *(pendiente creación — no existe en Azure DevOps, verificado 06/04/2026)* |

**Descripción:**
Verificar estados bloqueantes antes de consultar Migración Colombia vía Experian para documentos CE y PPT.

**Reglas de negocio:**

1. **Estados bloqueantes** (rechazo temporal de 1 mes): Inactivo, Cancelado, El número de identificación enviado no existe.
2. Reutiliza los mecanismos de caché, parametría y decisión automática implementados en RF-11.

---

### RF-15 — Corregir datos del cliente con resultados de Registraduría/Migración

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1037085 |
| **Prioridad** | Media |
| **Esfuerzo** | 5 puntos |
| **Actores** | SarlaftAPI (automático) |
| **Componente** | SarlaftAPI, tabla `tsaf_cliente` |
| **Repositorios** | [892-sarlaft-api-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [1101-validadorcliente_identidad-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) ⚠️ *(pendiente creación — no existe en Azure DevOps, verificado 06/04/2026)* |

**Descripción:**
Posterior a cada consulta de estado del documento, el sistema debe comparar y corregir automáticamente datos del cliente (apellidos, fecha de expedición, nacionalidad) si difieren de los entregados por Registraduría o Migración Colombia.

**Reglas de negocio:**

1. Los campos susceptibles de corrección automática son: 1er apellido, 2do apellido y fecha de expedición.
2. La corrección aplica para los estados: VIGENTE, CANCELADO, INACTIVO, CANCELADO POR DUPLICIDAD, FALLECIDO, FALSA IDENTIDAD.
3. La nacionalidad se guarda exactamente como la entrega el servicio externo (sin transformación).
4. Se debe crear un nuevo campo `nacionalidad` en `tsaf_cliente`.
5. Toda corrección debe registrarse en Splunk con campos antes/después y resultado.

---

### RF-16 — Módulo administrativo de gestión del estado del documento del cliente

| Atributo | Detalle |
|----------|---------|
| **ID Azure DevOps** | 1037162 |
| **Prioridad** | Alta |
| **Esfuerzo** | 49 puntos |
| **Actores** | Administrador SARLAFT |
| **Componente** | Nuevo front Angular + nuevo back (microservicio Validador Identidad) |
| **Repositorios** | [1101-validadorcliente_identidad-ms](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) ⚠️ *(pendiente creación — no existe en Azure DevOps, verificado 06/04/2026)*, [1101-validadorcliente_identidad-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr) ⚠️ *(pendiente creación — no existe en Azure DevOps, verificado 06/04/2026)* *(nuevo)* |

**Descripción:**
Nuevo módulo administrativo (front + back) para consultar y gestionar los estados de documentos almacenados desde las validaciones con Registraduría/Migración. También gestiona la parametría de reglas de bloqueo.

**Reglas de negocio:**

1. Solo usuarios con perfil **Administrador SARLAFT** pueden cambiar estados.
2. La consulta de cliente debe hacerse por tipo y número de identificación.
3. La grilla de resultados muestra: Número ID, Nombre, Estado actual, Estado a cambiar, Fecha, Acción.
4. Los cambios de estado deben quedar en trazabilidad completa y auditable en BD.
5. Los mensajes de éxito y error deben ser estandarizados.
6. La pantalla de administración de reglas de bloqueo debe soportar CRUD completo: crear, consultar, actualizar y eliminar reglas.
7. Cada regla de bloqueo contiene: tipo de documento, estado bloqueante, vigencia del bloqueo.
8. La autenticación se realiza mediante SEUS.
9. El frontend del módulo es un aplicativo Angular nuevo e independiente (Lego Sura, SEUS, pipeline CI/CD).

---

## 5. Mapa de Dependencias entre RF

```
RF-01  →  Servicios getSarlaft/clientes/formularios + modelo BD
RF-02  →  tsaf_tipo_requisito + DeterminarEstadoEvaluacion + Apache Tika
RF-03  →  Servicios getSarlaft + modelo BD (tablas financieros)
RF-04  →  Servicios getSarlaft + modelo BD (tablas financieros)
RF-05  →  tsaf_tipo_requisito + IBM P8 + RF-09 (reintentos sarlaftbatch)
RF-06  →  tsaf_cliente (3 campos nuevos) + caché Redis + motor evaluación
RF-07  →  Nueva tabla autorizaciones + Modelo Clientes (sync masivo)
RF-08  →  Motor evaluación (PrepararEvaluacion, DeterminarEstadoEvaluacion) + caché ADRES/DIAN + RF-11 (validaciones Registraduría/Migración)

RF-09  →  Azure Data Factory + sarlaftbatch + nueva tabla depuraciones
RF-10  →  Base de datos directa (queries SQL) + coordinación Kyndryl
RF-11  →  Nuevo microservicio MS-1101 + Redis Cache + IF(caché hit) ⟶ rechazo, IF(miss) ⟶ Experian
RF-12  →  Reutiliza MS-1101 (RF-11)
RF-13  →  Reutiliza MS-1101 (RF-11)
RF-14  →  Reutiliza MS-1101 (RF-11)
RF-15  →  MS-1101 + tsaf_cliente (campo nacionalidad nuevo)
RF-16  →  MS-1101 (admin back) + Nuevo front Angular + SEUS
```

---

## 6. Requisitos Funcionales Implícitos (identificados desde documentación técnica)

Los siguientes requisitos funcionales **no están enumerados explícitamente en el PRD** pero se derivan del análisis de la documentación técnica existente y son necesarios para la coherencia del sistema:

| ID | Descripción | RF relacionado | Fuente técnica |
|----|-------------|----------------|----------------|
| **RFI-01** | El sistema debe mantener el mecanismo existente de determinación de estado de evaluación (`FINALIZADO`, `FALLA TÉCNICA`, `RECHAZADO`, `PENDIENTE ACCIÓN MANUAL`, `PENDIENTE`) — RF-02 y RF-08 modifican sus condiciones pero no el mecanismo base. | RF-02, RF-08 | ProcesoEvaluacion/DeterminarEstadoEvaluacion.md |
| **RFI-02** | El Web Component Angular debe recibir los atributos `jsonRequest`, `token`, `app`, `tenant` con los valores actualizados que incluyan las nuevas secciones de formulario (CIIU 4, activos/pasivos, Junta Directiva, cláusula). | RF-01, RF-03, RF-04, RF-07, RF-08 | Front/index.md |
| **RFI-03** | Los catálogos CIIU 4 y denominaciones de tipo de sociedad deben precargarse en Azure Redis Cache al inicio de la aplicación para garantizar tiempos de respuesta operativos en formularios. | RF-01, RF-06 | brief.md (Caché Redis) |
| **RFI-04** | El proceso de comunicación asíncrona con IBM P8 (vía RabbitMQ, función `appp8`) debe mantenerse funcional para los nuevos tipos de soporte establecidos en RF-05. | RF-05 | ProcesoEvaluacion/ComunicacionP8.md |
| **RFI-05** | Los servicios de consulta de resultados en el microservicio Backweb (`/sarlaftbackweb/resultevaluation`) deben reflejar la autorización de tratamiento de datos del RF-07 en la pantalla de detalles de evaluación. | RF-07 | MicroservicioBackweb/ServiciosWeb/index.md |
| **RFI-06** | El API de terceros (`/api/v1/form/save`, `/api/v1/assessment`) debe actualizarse para todos los RF que modifican el modelo de datos del formulario (CIIU 4, activos/pasivos, ingresos/egresos, cláusula de datos, Junta Directiva). | RF-01, RF-03, RF-04, RF-07, RF-08 | ServiciosWeb/ServicioTerceros/ |
| **RFI-07** | La carga masiva de figuras (`ProcesosCargaMasiva`) debe ser evaluada y ajustada para incluir la figura de Junta Directiva y los nuevos campos de cliente (clasificación, tipo PJ, nacionalidad). | RF-06, RF-08, RF-15 | MicroservicioSarlaftAPI/ProcesosCargaMasiva/ |

---

## 7. Requisitos No Funcionales Relevantes al Contexto Técnico

Derivados del PRD y confirmados por la documentación técnica:

| Categoría | Descripción | RF impactados |
|-----------|-------------|---------------|
| **Seguridad** | Validación de archivos adjuntos con Apache Tika (tipo MIME real, tamaño, dominios). | RF-02 |
| **Seguridad** | Autenticación/autorización con SEUS para todos los nuevos servicios y módulos administrativos. | RF-11, RF-16 |
| **Seguridad** | Las pruebas de seguridad dinámicas deben cubrir back y front en RF-02, RF-07 (impacto alto). | RF-02, RF-07 |
| **Trazabilidad** | Logs en Splunk para: operaciones de caché (RF-11/12/13/14), correcciones de datos (RF-15), fallos P8 (RF-05), cambios de estado de documento (RF-16). | RF-05, RF-11–16 |
| **Trazabilidad** | Registros de auditoría en BD para: actividad CIIU modificada, tratamiento de datos autorizado, estado de documento cambiado, parametrías actualizadas. | RF-01, RF-07, RF-16 |
| **Disponibilidad** | Fallos en IBM P8 no deben bloquear la captura del formulario. Circuit breaker activo. | RF-05 |
| **Caché** | CIIU 4, denominaciones PJ, parametrías de bloqueo de identidad: deben cargarse en Azure Redis Cache. | RF-01, RF-06, RF-11 |
| **Rendimiento** | La depuración de BD debe ejecutarse únicamente en ventana no productiva con rollback controlado. | RF-09 |
| **Parametrización** | Textos de cláusula de datos, denominaciones de sociedades, documentos por tipo de sociedad, reglas de bloqueo: configurables sin redespliegue de código. | RF-05, RF-06, RF-07, RF-11, RF-16 |

---

## 8. Resumen y Priorización

| RF | Nombre | Feature | Prioridad | Puntos |
|----|--------|---------|-----------|--------|
| RF-08 | Figura Junta Directiva — Datos Directivos PJ | Formularios | Alta | 64 |
| RF-16 | Módulo administrativo gestión estado documento | Optimización | Alta | 49 |
| RF-09 | Depuración periódica de evaluaciones (DataFactory) | Optimización | Alta | 47 |
| RF-02 | Certificado Ingresos y Retenciones — opcional | Formularios | Alta | 38 |
| RF-11 | Evitar duplicidad consulta Registraduría | Optimización | Alta | 26 |
| RF-05 | Requisitos documentales por tipo de sociedad | Formularios | Alta | 23 |
| RF-07 | Cláusula tratamiento de datos personales | Formularios | Alta | 15 |
| RF-01 | Actividad Económica CIIU 4 | Formularios | Media | 9 |
| RF-03 | Ingresos y egresos PJ | Formularios | Media | 9 |
| RF-04 | Activos y pasivos PN y PJ | Formularios | Media | 9 |
| RF-06 | Tipificar PJ por tipo de sociedad | Formularios | Media | 5 |
| RF-10 | Depuración histórica evaluaciones (one-off) | Optimización | Alta | 5 |
| RF-15 | Corregir datos cliente con Registraduría/Migración | Optimización | Media | 5 |
| RF-12 | Evitar duplicidad datos básicos (CC/CE/PPT) | Optimización | Media | 4 |
| RF-13 | Evitar duplicidad cuestionario identidad | Optimización | Media | 4 |
| RF-14 | Evitar duplicidad consulta Migración Colombia | Optimización | Media | 4 |
| | **TOTAL** | | | **316 pts** |

---

## 9. Fuera de Alcance (confirmado)

- Integración en tiempo real con el Modelo de Clientes para tratamiento de datos (solo sincronización diaria).
- Recolección retroactiva de información financiera para clientes existentes.
- Tipificación retroactiva de PJ ya almacenadas en BD.
- Migración o reconstrucción de histórico de autorizaciones de tratamiento de datos.
- Depuración de evaluaciones en proceso de actualización (solo negocio nuevo y reclamaciones).
- Ajustes al frontend del módulo de clientes Sura existente (el módulo del validador de identidad es aplicativo nuevo y separado).

---

## 10. Repositorios Involucrados

Todos los repositorios están bajo la organización `SuraColombia` en Azure DevOps:
`https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/<nombre-repositorio>`

### 10.1 Repositorios con cambios de código (modificados)

| # | Repositorio (código fuente) | Componente | RF que lo impactan |
|---|----------------------------|------------|--------------------|
| 1 | `892-sarlaft-api-ms` / `adm_y_fin-sarlaft-api-ms` | **SarlaftAPI** — API principal, servicios REST, motor de evaluación de formularios, lógica de clientes | RF-01, RF-02, RF-03, RF-04, RF-05, RF-06, RF-07, RF-08, RF-11, RF-12, RF-13, RF-14, RF-15 |
| 2 | `892-sarlaft-brms-ms` | **SarlaftEngine (Motor de Evaluación)** — Reglas de negocio Drools: PrepararEvaluacion, DeterminarEstadoEvaluacion | RF-02, RF-05, RF-06, RF-08 |
| 3 | `892-sarlaft-fr` | **Front Angular (MonoRepositorio)** — Aplicaciones Redirect, WebComponent y Admin | RF-01, RF-02, RF-03, RF-04, RF-05, RF-07, RF-08, RF-11, RF-16 |
| 4 | `892-sarlaft-admin-ms` | **Backweb** — Módulo administrativo back: consulta de evaluaciones, cancelaciones, gestión de entidades | RF-07 |
| 5 | `892-sarlaft-batch-ms` | **SarlaftBatch** — Proceso nocturno de reintentos, procesos masivos | RF-05, RF-09 |
| 6 | `1101-validadorcliente_identidad-ms` ⚠️ | **Validador de Identidad MS** (proyecto #1101) — Nuevo componente de caché y gestión de estados bloqueantes — **⚠️ No existe en Azure DevOps, pendiente creación (verificado 06/04/2026)** | RF-11, RF-12, RF-13, RF-14, RF-15, RF-16 |

### 10.2 Repositorios de configuración (ajustados por cambios de propiedades/pipelines)

| # | Repositorio (configuración) | Componente asociado | Motivo de cambio |
|---|----------------------------|---------------------|-----------------|
| 1 | `892-sarlaft-api-conf` / `adm_y_fin-sarlaft-api-conf` | SarlaftAPI | Variables de entorno, propiedades de timeouts, caché Redis (catálogos CIIU, denominaciones PJ) |
| 2 | `adm_y_fin-sarlaft-brms-conf` | SarlaftEngine | Configuración de reglas Drools actualizadas |
| 3 | `892-sarlaft-fr-conf` / `adm_y_fin-sarlaft-fr-conf` | Front Angular | Pipeline CI/CD, variables de entorno por tenant/ambiente |
| 4 | `892-sarlaft-admin-conf` | Backweb | Configuración de ambientes |
| 5 | `892-sarlaft-batch-ms-conf` | SarlaftBatch | Configuración del proceso de reintentos nocturno |
| 6 | `1101-validadorcliente_identidad-conf` | Validador de Identidad | Configuración nueva: BD, Redis Cache, reglas de bloqueo parametrizadas |
| 7 | `892-sarlaft_function_documental-conf` / `892-sarlaft-function_p8-conf` | Integrador P8 (MI) | Propiedades de circuit breaker y reintentos (RF-05) |
| 8 | `892-sarlaft-function_requisitos-conf` | Integrador Requisitos (MI) | Ajuste de propiedades de obligatoriedad de soportes (RF-02, RF-05) |

### 10.3 Repositorio nuevo (creado desde cero)

| # | Repositorio | Componente | RF que lo originan |
|---|-------------|------------|--------------------|
| 1 | `1101-validadorcliente_identidad-fr` *(nuevo front admin)* | **Front administrativo del Validador de Identidad** — Aplicativo Angular independiente con Lego Sura y SEUS para gestión de estados y parametrías de bloqueo | RF-16 |

> **Nota:** La documentación técnica existente identifica el repositorio `892-validadorcliente_identidad-fr` como nombre alternativo del front administrativo del validador. El nombre definitivo debe confirmarse con el equipo de infraestructura al crear el repositorio.

> ⚠️ **Verificado el 06/04/2026:** Este repositorio **no existe aún en Azure DevOps**. Debe ser creado junto con `1101-validadorcliente_identidad-ms` como parte de la implementación de RF-16.

### 10.4 Repositorios de pruebas (actualizados)

| # | Repositorio (pruebas) | Componente | Motivo |
|---|----------------------|------------|--------|
| 1 | `892-sarlaft-pa` | SarlaftAPI | Pruebas SoapUI de los servicios modificados (RF-01 a RF-08) |
| 2 | `892-sarlaft-brms-pa` | SarlaftEngine | Pruebas automatizadas del motor (RF-02, RF-05, RF-06, RF-08) |
| 3 | `892-sarlaft-batch-pa` | SarlaftBatch | Pruebas del proceso de reintentos y depuración (RF-05, RF-09) |
| 4 | `1101-validadorcliente_identidad-pa` / `adm_y_fin-validadorcliente-identidad-pa` | Validador de Identidad | Pruebas de los nuevos flujos de caché y bloqueo (RF-11–RF-16) |

### 10.5 Repositorios NO impactados (sin cambios previstos)

| Repositorio | Componente | Justificación |
|-------------|------------|---------------|
| `892-sarlaft4-sarlaftclientes-ms` | SarlaftClientesMS | Solo consulta datos en fuentes externas; no recibe cambios de modelo de formulario |
| `adm_y_fin-sarlaft-sarlaft_callback-conf` | SarlaftWebhook | El webhook solo reacciona a eventos de evaluación; RF no modifican su lógica |
| `892-sarlaft-function_batch-mi` | Batch MI (Integrador) | Integrador de cola masiva; no cambia su interfaz, solo el batch interno |
| `892-sarlaft-function_clientes-mi` | Clientes MI (Integrador) | Integrador de clientes Sura; sin cambios en este proyecto |
| `adm_y_fin-sarlaft-function_saveclientes-mi` | Actualización Clientes MI | Sin cambio previsto; la sincronización de cláusula de datos es responsabilidad del Modelo de Clientes de Sura |
| `892-sarlaft-function_ccm-conf` | CCM MI | Notificaciones CCM; sin cambios en este proyecto |
| `1170-peps_pepsms-ms` | PEPS MS | Microservicio de consulta PEPs independiente; no impactado |

### 10.6 Mapa RF → Repositorios

| RF | Repositorios de código impactados |
|----|----------------------------------|
| RF-01 | `892-sarlaft-api-ms`, `892-sarlaft-fr` |
| RF-02 | `892-sarlaft-api-ms`, `892-sarlaft-brms-ms`, `892-sarlaft-fr`, `892-sarlaft-function_requisitos-conf` |
| RF-03 | `892-sarlaft-api-ms`, `892-sarlaft-fr` |
| RF-04 | `892-sarlaft-api-ms`, `892-sarlaft-fr` |
| RF-05 | `892-sarlaft-api-ms`, `892-sarlaft-brms-ms`, `892-sarlaft-fr`, `892-sarlaft-batch-ms`, `892-sarlaft_function_documental-mi` |
| RF-06 | `892-sarlaft-api-ms`, `892-sarlaft-brms-ms` |
| RF-07 | `892-sarlaft-api-ms`, `892-sarlaft-admin-ms`, `892-sarlaft-fr` |
| RF-08 | `892-sarlaft-api-ms`, `892-sarlaft-brms-ms`, `892-sarlaft-fr` |
| RF-09 | `892-sarlaft-batch-ms` *(+ pipelines Azure Data Factory — fuera de repositorios de código)* |
| RF-10 | *(scripts SQL directos — sin repositorio de código; coordinación con Kyndryl)* |
| RF-11 | `892-sarlaft-api-ms`, `1101-validadorcliente_identidad-ms` ⚠️ *(pendiente creación)*, `892-sarlaft-fr` |
| RF-12 | `892-sarlaft-api-ms`, `1101-validadorcliente_identidad-ms` ⚠️ *(pendiente creación)* |
| RF-13 | `892-sarlaft-api-ms`, `1101-validadorcliente_identidad-ms` ⚠️ *(pendiente creación)* |
| RF-14 | `892-sarlaft-api-ms`, `1101-validadorcliente_identidad-ms` ⚠️ *(pendiente creación)* |
| RF-15 | `892-sarlaft-api-ms`, `1101-validadorcliente_identidad-ms` ⚠️ *(pendiente creación)* |
| RF-16 | `1101-validadorcliente_identidad-ms` ⚠️ *(pendiente creación)*, `1101-validadorcliente_identidad-fr` ⚠️ *(pendiente creación)* *(nuevo)* |

---

*Documento generado con base en `docs/core/prd.md`, `docs/core/brief.md` y la documentación técnica en `docs/Sarlaft40/DocumentacionTecnica/`.*
