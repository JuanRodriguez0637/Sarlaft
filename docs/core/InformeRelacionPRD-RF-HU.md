# Informe de Trazabilidad: PRD → Requisitos Funcionales → Historias de Usuario
## Fortalecimiento Sarlaft 4.0

**Fecha:** Abril 2026  
**Fuentes:** [prd.md](./prd.md) · [RF.md](./RF.md) · Épicas y Features en `docs/Epica/`

---

## 1. Resumen del Producto

El proyecto **Fortalecimiento Sarlaft 4.0** tienen cuatro objetivos estratégicos definidos en el PRD:

| Objetivo | Descripción | Métrica de éxito |
|----------|-------------|-----------------|
| **O1** | Completar las validaciones de formularios SARLAFT para cumplimiento normativo | 100% de HUs del Feature Formularios desplegadas en producción |
| **O2** | Reducir costos por consultas duplicadas a Experian / Registraduría / Migración | Eliminación de consultas redundantes mediante caché y estados bloqueantes |
| **O3** | Depurar la base de datos de evaluaciones obsoletas | Eliminación controlada de Pendientes (> 6 meses) y Canceladas (> 1 año) |
| **O4** | Desacoplar el validador de identidad como componente transversal | Nuevo microservicio MS-1101 independiente desplegado |

**Total del proyecto:** 16 Requisitos Funcionales · 316 puntos de esfuerzo · 122 Historias de Usuario únicas

---

## 2. Estructura del Backlog

```
Épica
└── Feature
    └── Historia de Usuario (HU)
```

Las épicas que cubren el alcance del PRD/RF son:

| ID Épica | Nombre | RF cubiertos |
|----------|--------|-------------|
| **1032289** | Conocimiento del Cliente — Contrapartes | RF-01 al RF-08 (Feature 1) |
| **1079106** | Optimización — Base de datos y servicios externos | RF-09 al RF-16 (Feature 2) |
| **1033001** | Proceso de actualización | HUs de contexto / habilitadores |
| **1036585** | Monitoreo y Señales de Alerta | HUs de componentes transversales |
| **1046076** | Conexión Módulo de Clientes — Reglas para clientes | HUs de integraciones externas |
| **1078398** | Aplicativos de negocio — Cancelaciones de pólizas | HUs de aplicativos de negocio |

---

## 3. Mapa de Trazabilidad RF → HU

### FEATURE 1 — Modificaciones a Formularios  
> Épica 1032289 · Objetivo PRD: O1

---

#### RF-01 — Modificar campo Actividad Económica (CIIU 4)
**Prioridad:** Media · **Esfuerzo:** 9 pts · **ID Azure DevOps:** 1025877  
**Feature:** [1032288 — Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1025877](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1025877) | Modificar el campo de actividad económica (CIIU 4) | **New** | HU principal del RF |

---

#### RF-02 — Hacer opcional el Certificado de Ingresos y Retenciones (PN)
**Prioridad:** Alta · **Esfuerzo:** 38 pts · **IDs Azure DevOps:** 1025884, 1035950, 1057319  
**Feature:** [1057319 — Cambiar a opcional la solicitud del certificado](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1057319)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1082005](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082005) | Requisito opcional "Ingresos y retenciones" — Back Validación Adjuntos | **New** | Validación Apache Tika (seguridad OWASP A05) |
| [1082032](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082032) | Requisito opcional "Ingresos y retenciones" — Back Validación Adjuntos (soluciones pruebas de seguridad) | **New** | Correcciones post-prueba de seguridad |
| [1082042](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082042) | Requisito opcional "Ingresos y retenciones" — Back Requisitos | **New** | Ajuste `tsaf_tipo_requisito` |
| [1082089](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082089) | Requisito opcional "Ingresos y retenciones" — Front Requisitos | **New** | UI formulario PN Intensificado |

---

#### RF-03 — Solicitar Ingresos y Egresos (PJ)
**Prioridad:** Media · **Esfuerzo:** 9 pts · **ID Azure DevOps:** 1026762  
**Feature:** [1032288 — Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1026762](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026762) | Solicitar a una PN y PJ ingresos y egresos | **New** | Campos datos financieros PJ |

---

#### RF-04 — Solicitar Activos y Pasivos (PN y PJ)
**Prioridad:** Media · **Esfuerzo:** 9 pts · **ID Azure DevOps:** 1026765  
**Feature:** [1032288 — Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1026765](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026765) | Solicitar a una PN y PJ activos y pasivos | **New** | Campos datos financieros PN y PJ |

---

#### RF-05 — Solicitar requisitos documentales por tipo de sociedad (PJ)
**Prioridad:** Alta · **Esfuerzo:** 23 pts · **ID Azure DevOps:** 1026770  
**Feature:** [1026770 — Solicitar requisitos por tipo de sociedad](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026770)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1079051](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079051) | Solicitar requisitos por tipo de sociedad — Back | **New** | Tabla de equivalencias 18+ tipos |
| [1079058](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079058) | Solicitar requisitos por tipo de sociedad — Front | **New** | UI dinámica soportes PJ |
| [1079062](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079062) | Solicitar requisitos por tipo de sociedad — Reintentos | **New** | Circuit breaker IBM P8; máx 3 reintentos |
| [1046415](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046415) | Back — Parametrizar los códigos de los requisitos por tipo de sociedad | **New** | Habilitador parametría |
| [1046438](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046438) | Front — Ajustes para mostrar los requisitos | **New** | Ajuste presentación soportes |
| [1046535](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046535) | Relanzamiento de documentos a P8 | **New** | Proceso de reintento P8 |

---

#### RF-06 — Tipificar PJ por tipo de sociedad
**Prioridad:** Media · **Esfuerzo:** 5 pts · **ID Azure DevOps:** 1026776  
**Feature:** [1032288 — Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) | Tipificar a las personas jurídicas por tipo de sociedad | **New** | Análisis razón social + Redis cache |

---

#### RF-07 — Adicionar cláusula de tratamiento de datos personales
**Prioridad:** Alta · **Esfuerzo:** 15 pts · **ID Azure DevOps:** 1032311  
**Feature:** [1032288 — Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1032311](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032311) | Adicionar cláusula de tratamiento de datos personales | **New** | Pantalla post-bienvenida; sincronización diaria a Modelo Clientes |

---

#### RF-08 — Adicionar figura de Junta Directiva (PJ Sociedad Comercial)
**Prioridad:** Alta · **Esfuerzo:** 64 pts · **ID Azure DevOps:** 1035467  
**Feature:** [1035467 — Adicionar figura de junta directiva](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035467)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1082241](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082241) | Adicionar figura de junta directiva — Back | **New** | Modelo BD + servicios REST |
| [1082249](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082249) | Adicionar figura de junta directiva — Motor de evaluación y Riesgo | **New** | Preparar/Determinar estado evaluación |
| [1082267](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082267) | Adicionar figura de junta directiva — Front | **New** | UI sub-bloque Junta Directiva |
| [1082270](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082270) | Adicionar figura de junta directiva — Validación riesgos RRCC | **New** | Validación listas SARLAFT por miembro |
| [1082272](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082272) | Adicionar figura de junta directiva — Parametrización formulario — Front | **New** | CRUD parametrización tipos de PJ |
| [1082281](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082281) | Adicionar figura de junta directiva — Parametrización formulario — Back | **New** | CRUD admin sin redespliegue |

---

### FEATURE 2 — Optimización BD y Servicios Externos  
> Épica 1079106 · Objetivos PRD: O2, O3, O4

---

#### RF-09 — Depuración periódica de evaluaciones (proceso automático)
**Prioridad:** Alta · **Esfuerzo:** 47 pts · **ID Azure DevOps:** 1035141  
**Feature:** [1035141 — Depuración evaluaciones BD Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1076668](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076668) | Depuración evaluaciones BD — Onboarding y Configuración Datafactory | **New** | Setup Azure Data Factory · Repo: [`892-sarlaft4_adm_y_fin_sarlaft-md`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4_adm_y_fin_sarlaft-md) |
| [1076922](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076922) | Depuración evaluaciones BD — Diseño inicial Pipelines Datafactory | **New** | Arquitectura pipelines |
| [1076945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076945) | Depuración evaluaciones BD — Implementación pipeline de consulta | **New** | Pipeline consulta evaluaciones |
| [1076947](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076947) | Depuración evaluaciones BD — Implementación pipeline de depuración | **New** | Pipeline eliminar evaluaciones |
| [1076961](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076961) | Depuración evaluaciones BD — Automatización del proceso | **New** | Scheduler ventana no productiva |

---

#### RF-10 — Depuración histórica puntual (one-off)
**Prioridad:** Alta · **Esfuerzo:** 5 pts · **ID Azure DevOps:** 1035171  
**Feature:** [1032999 — Optimización Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1035171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171) | Depuración evaluaciones BD Sarlaft — histórico | **New** | Scripts SQL; coordinación Kyndryl; backup previo |

---

#### RF-11 — Evitar duplicidad de consultas a Registraduría (CC)
**Prioridad:** Alta · **Esfuerzo:** 26 pts · **ID Azure DevOps:** 1035500  
**Feature:** [1035500 — Evitar duplicidad estados validación de identidad](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035500)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1081870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081870) | Evitar duplicidad — Front Pantalla Módulo Sarlaft (Datos adicionales) | **New** | Resultado Registraduría en detalles figuras |
| [1081880](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081880) | Evitar duplicidad — Front Validador Identidad — IaC | **New** | Infraestructura nueva (pipeline, BD, Redis) |
| [1081885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081885) | Evitar duplicidad — Validador Identidad Admon MS (nuevo micro Back) | **New** | Repo: [`1101-validadorcliente_identidad-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) — estados bloqueantes permanentes y temporales |
| [1081888](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081888) | Evitar duplicidad — ValidadorIdentidad MS (integración SarlaftAPI) | **New** | Consumo desde SarlaftAPI existente |

---

#### RF-12 — Evitar duplicidad en validación de identidad — Datos básicos (CC, CE, PPT)
**Prioridad:** Media · **Esfuerzo:** 4 pts · **ID Azure DevOps:** 1035498  
**Feature:** [1032999 — Optimización Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1035498](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035498) | Evitar duplicidad en estados validación de identidad — Datos básicos | **New** | Reutiliza MS-1101 de RF-11 |

---

#### RF-13 — Evitar duplicidad en validación de identidad — Cuestionario
**Prioridad:** Media · **Esfuerzo:** 4 pts · **ID Azure DevOps:** 1035502  
**Feature:** [1032999 — Optimización Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1035502](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035502) | Evitar duplicidad en estados validación de identidad — Cuestionario | **New** | Reutiliza MS-1101 de RF-11 |

---

#### RF-14 — Evitar duplicidad de consultas a Migración Colombia (CE, PPT)
**Prioridad:** Media · **Esfuerzo:** 4 pts · **ID Azure DevOps:** 1037054  
**Feature:** [1032999 — Optimización Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1037054](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037054) | Evitar duplicidad en estados de consulta con Migración Colombia | **New** | Reutiliza MS-1101 de RF-11 |

---

#### RF-15 — Corregir datos del cliente con resultados de Registraduría/Migración
**Prioridad:** Media · **Esfuerzo:** 5 pts · **ID Azure DevOps:** 1037085  
**Feature:** [1032999 — Optimización Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1037085](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037085) | Reemplazar datos de la consulta del estado del documento | **New** | Corrección automática apellidos, f. expedición, nacionalidad · Repos: [`892-sarlaft-api-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms), [`1101-validadorcliente_identidad-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) |

---

#### RF-16 — Módulo administrativo de gestión del estado del documento
**Prioridad:** Alta · **Esfuerzo:** 49 pts · **ID Azure DevOps:** 1037162  
**Feature:** [1037162 — Gestión del estado del documento del cliente](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037162)

| ID HU | Historia de Usuario | Estado | Notas |
|-------|--------------------|---------|----- |
| [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) | Validador Identidad Admon MS — Servicios gestión estado cliente | **New** | Repo back: [`1101-validadorcliente_identidad-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) |
| [1096178](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096178) | Validador Identidad Admon MS — Servicios gestión parametrías validación | **New** | CRUD reglas de bloqueo |
| [1096189](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096189) | Validador Identidad Admon MS — Servicios gestión parametrías (parte 2) | **New** | Continuación CRUD parametrías |
| [1096205](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096205) | Validador Identidad Admon (nuevo Front) — Gestión estado cliente Parte 1 | **New** | Repo front: [`1101-validadorcliente_identidad-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr) |
| [1096228](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096228) | Validador Identidad Admon (nuevo Front) — Gestión estado cliente Parte 2 | **New** | Continuación UI gestión |
| [1096310](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096310) | Validador Identidad Admon (nuevo Front) — Parametrías validación Parte 1 | **New** | UI CRUD reglas bloqueo |
| [1096313](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096313) | Validador Identidad Admon (nuevo Front) — Parametrías validación Parte 2 | **New** | Continuación UI parametrías |

---

## 4. HUs fuera del alcance directo del PRD/RF

Las siguientes HUs pertenecen a épicas y features del backlog **no cubiertas directamente por los 16 RF del PRD** (habilitadores, integraciones de negocio, proceso de actualización, monitoreo). Se documentan aquí para completitud:

### Épica 1032289 — Features complementarios

| ID HU | Feature | Historia de Usuario | Estado |
|-------|---------|--------------------|----|
| [1035971](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035971) | 1033000 — Tipificación Admon riesgo único | Determinar riesgo único del cliente | New |
| [1041068](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041068) | 1033000 — Tipificación Admon riesgo único | Migración de clientes | New |
| [1098643](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1098643) | 1033000 — Tipificación Admon riesgo único | Crear evaluaciones sarlaft a las operaciones no conectadas | New |
| [1102573](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1102573) | 1033000 — Tipificación Admon riesgo único | Creación de evaluaciones SARLAFT batch (conectadas) | New |
| [1102574](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1102574) | 1033000 — Tipificación Admon riesgo único | Generar evaluaciones SARLAFT desde información parcial | New |
| [1041366](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041366) | 1041364 — Reglas transversales | Herencia por tipo de riesgo | New |
| [1046069](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046069) | 1041364 — Reglas transversales | Analizar clientes con nacionalidad países GAFI Negro | New |
| [1052091](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1052091) | 1041364 — Reglas transversales | Reprocesar fallas técnicas consulta Registraduría/Migración | New |
| [1053179](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1053179) | 1041364 — Reglas transversales | Actualización nombres tablas paramétricas — Front | New |
| [1056870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1056870) | 1041364 — Reglas transversales | Ajustar botón "Cambiar Estado" para estado Rechazado | New |
| [1066094](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1066094) | 1041364 — Reglas transversales | Incluir fecha nacimiento/constitución en la evaluación | New |
| [1100215](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1100215) | 1041364 — Reglas transversales | Crear evaluación figuras de relación con PEP | New |
| [1046075](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046075) | 1046074 — Aplicativos de negocio reglas | Validación Sarlaft batch para canales masivos y vida grupo | New |
| [1041386](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041386) | 1046077 — Aplicativos de negocio reglas | Vida individual y fondo de ahorro — API | New |
| [1055003](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1055003) | 1046077 — Aplicativos de negocio reglas | Vida individual y fondo de ahorro — Front Módulo Clientes | New |
| [1076996](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076996) | 1049120 — Aplicativos de negocio reclamaciones | Ajustar el flujo de proceso judicial | New |
| [1077071](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077071) | 1049126 — Notificación reclamación | Diseño y creación del modelo de datos | New |
| [1077075](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077075) | 1049126 — Notificación reclamación | Carga del Calendario de Días Hábiles | New |
| [1077080](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077080) | 1049126 — Notificación reclamación | Crear un disparador programado | New |
| [1077081](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077081) | 1049126 — Notificación reclamación | Orquestador de notificaciones | New |
| [1077083](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077083) | 1049126 — Notificación reclamación | Gestión de reglas | New |
| [1077085](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077085) | 1049126 — Notificación reclamación | Pruebas de integración punta a punta | New |
| [1077087](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077087) | 1049126 — Notificación reclamación | Prendido controlado en producción | New |
| [1073532](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1073532) | 1073128 — Reclamaciones | Sincronizar datos básicos Sarlaft/Contact Manager | New |
| [1073537](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1073537) | 1073128 — Reclamaciones | Notificar datos pendientes del proceso Sarlaft | New |
| [1073547](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1073547) | 1073128 — Reclamaciones | Bloquear pagos cuando SARLAFT es rechazado | New |
| [1077125](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077125) | 1032288 — Modificaciones Formulario | Visualizar información del formulario en Resumen (perfil Admin) | New |
| [1078859](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078859) | 1078852 — Ajustes C&S Vida | Registrar beneficiarios estructurados en cotizador | New |
| [1078861](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078861) | 1078852 — Ajustes C&S Vida | Validar sumatoria porcentajes beneficiarios | New |
| [1078862](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078862) | 1078852 — Ajustes C&S Vida | Manejar beneficiarios onerosos y no onerosos | New |
| [1078863](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078863) | 1078852 — Ajustes C&S Vida | Expedir pólizas sin beneficiarios (información mínima) | New |
| [1078865](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078865) | 1078852 — Ajustes C&S Vida | Capturar datos mínimos obligatorios de beneficiarios | New |
| [1078869](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078869) | 1078852 — Ajustes C&S Vida | Evaluar beneficiarios ingresados masivamente | New |
| [1078873](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078873) | 1078852 — Ajustes C&S Vida | Diferenciar modificaciones valorables/no valorables | New |
| [1078876](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078876) | 1078852 — Ajustes C&S Vida | Conservar trazabilidad de beneficiarios históricos | New |
| [1078883](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078883) | 1078852 — Ajustes C&S Vida | Mensajes informativos claros sobre definición de beneficiarios | New |
| [1078893](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078893) | 1078852 — Ajustes C&S Vida | Sincronizar actualizaciones de beneficiarios entre canales | New |
| [1078905](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078905) | 1078852 — Ajustes C&S Vida | Plantilla de carga masiva con campos SARLAFT obligatorios | New |
| [1078907](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078907) | 1078852 — Ajustes C&S Vida | Designar/actualizar beneficiarios en sucursal virtual | New |

### Épica 1033001 — Proceso de actualización

| ID HU | Feature | Historia de Usuario | Estado |
|-------|---------|--------------------|----|
| [1040402](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1040402) | 1082319 — Modificaciones al formulario | Diligenciamiento del Formulario | New |
| [1041011](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041011) | 1082320 — Notificaciones red comercial | Notificaciones a Directores y Gerentes | New |
| [1076693](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076693) | 1082324 — Modificaciones al proceso | Adicionar botón de cambiar estado desactualizado→actualizado | New |
| [1077124](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077124) | 1082324 — Modificaciones al proceso | Habilitar levantamiento manual de validación de identidad | New |
| [1083734](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1083734) | 1082324 — Modificaciones al proceso | Retirar opción de cancelar evaluaciones de cancelación | New |
| [1082361](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082361) | 1040973 — Reenvio masivo | Reenvio masivo en Módulo de Clientes — Back | New |
| [1082386](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082386) | 1040973 — Reenvio masivo | Reenvio masivo en Módulo de Clientes — Front | New |
| [1082387](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082387) | 1040973 — Reenvio masivo | Reenvio masivo — Proceso Masivo de Notificaciones | New |
| [1082389](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082389) | 1040973 — Reenvio masivo | Reenvio masivo — Modelo de notificación y reenvío | New |

### Épica 1036585 — Monitoreo y Señales de Alerta

| ID HU | Feature | Historia de Usuario | Estado |
|-------|---------|--------------------|----|
| [1029945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029945) | 1026784 — Proceso Batch SARLAFT | Componente Transversal Monitoreo Listas | New |
| [1029968](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029968) | 1026784 — Proceso Batch SARLAFT | Componente Transversal Monitoreo Listas — PipeLine Despliegue | New |
| [1029972](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029972) | 1026784 — Proceso Batch SARLAFT | Lista de control (ONU, OFAC, Grupos terroristas) — Infolaft | New |
| [1029992](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029992) | 1026784 — Proceso Batch SARLAFT | Consulta estado Persona jurídica con Informacolombia | New |
| [1029994](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029994) | 1026784 — Proceso Batch SARLAFT | Listas PEP — Infolaft | New |
| [1030004](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1030004) | 1026784 — Proceso Batch SARLAFT | Lista Proveedores Fachada DIAN — InfoLaft | New |
| [1031933](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1031933) | 1026784 — Proceso Batch SARLAFT | Lista IPS Fachada ADRES | New |
| [1053885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1053885) | 1026784 — Proceso Batch SARLAFT | Consulta causales IPS y DIAN Fachada desde Riesgos Consultables | New |

### Épica 1046076 — Conexión Módulo de Clientes

| ID HU | Feature | Historia de Usuario | Estado |
|-------|---------|--------------------|----|
| [1078435](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078435) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — Back 1 | New |
| [1078438](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078438) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — sarlaftclientes | New |
| [1078446](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078446) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — Back 2 Motor | New |
| [1078462](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078462) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — Api Terceros | New |
| [1097345](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097345) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — Front módulo consultas clientes | New |
| [1097347](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097347) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — Front Redirect | New |
| [1097349](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097349) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — Módulo de crear evaluación | New |
| [1097354](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097354) | 1046082 — Analizar nuevas figuras | Analizar nuevas figuras — Front SarlaftBackweb | New |
| [1096695](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096695) | 1046084 — Reglas pagos Rentas | Reglas para pagos de Rentas — Ajustes modelo, entidades y servicios | New |
| [1096829](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096829) | 1046084 — Reglas pagos Rentas | Reglas para pagos de Rentas — Ajuste servicio resultados evaluación | New |
| [1096832](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096832) | 1046084 — Reglas pagos Rentas | Reglas para pagos de Rentas — Ajustes creación de evaluaciones | New |
| [1096836](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096836) | 1046084 — Reglas pagos Rentas | Reglas para pagos de Rentas — Ajustes reglas motor de riesgo | New |
| [1096837](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096837) | 1046084 — Reglas pagos Rentas | Reglas para pagos de Rentas — Pantalla "CREAR EVALUACIÓN" Front | New |

### Épica 1078398 — Cancelaciones de pólizas

| ID HU | Feature | Historia de Usuario | Estado |
|-------|---------|--------------------|----|
| [1096589](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096589) | 1046088 — Cancelaciones Vida | Cancelaciones Vida con Fondo de ahorro — Modificar `/assessment` | New |
| [1096591](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096591) | 1046088 — Cancelaciones Vida | Cancelaciones Vida con Fondo de ahorro — Cambio en API terceros | New |
| [1096598](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096598) | 1046088 — Cancelaciones Vida | Cancelaciones Vida con Fondo de ahorro — Nuevo motor | New |
| [1096599](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096599) | 1046088 — Cancelaciones Vida | Cancelaciones Vida con Fondo de ahorro — Ajustar Webhook | New |
| [1096601](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096601) | 1046088 — Cancelaciones Vida | Cancelaciones Vida con Fondo de ahorro — Servicio Backweb cambio estado | New |
| [1096602](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096602) | 1046088 — Cancelaciones Vida | Cancelaciones Vida con Fondo de ahorro — Pruebas punta a punta | New |

### Sin Épica catalogada

| ID HU | Historia de Usuario | Estado |
|-------|--------------------|--------|
| [1026815](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026815) | Motor — Reglas para evaluar figuras de Rentas | New |
| [1026823](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026823) | Evaluación — Reglas para evaluar figuras de Rentas | New |
| [1026827](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026827) | Evaluación — Crear operaciones para evaluar clientes de Rentas | New |
| [1026983](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026983) | Datos mínimos — Reglas para verificar datos básicos con Registraduría/Migración | New |
| [1032876](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032876) | Integración Modelo de Clientes | New |

---

## 5. Tabla Consolidada RF ↔ HU

| RF | Nombre RF | Prioridad | Pts | HUs asociadas |
|----|-----------|-----------|-----|---------------|
| RF-01 | Actividad Económica CIIU 4 | Media | 9 | 1025877 |
| RF-02 | Certificado Ingresos opcional (PN) | Alta | 38 | 1082005, 1082032, 1082042, 1082089 |
| RF-03 | Ingresos y Egresos PJ | Media | 9 | 1026762 |
| RF-04 | Activos y Pasivos PN y PJ | Media | 9 | 1026765 |
| RF-05 | Requisitos documentales por tipo sociedad | Alta | 23 | 1079051, 1079058, 1079062, 1046415, 1046438, 1046535 |
| RF-06 | Tipificar PJ por tipo sociedad | Media | 5 | 1026776 |
| RF-07 | Cláusula tratamiento de datos | Alta | 15 | 1032311 |
| RF-08 | Figura Junta Directiva PJ | Alta | 64 | 1082241, 1082249, 1082267, 1082270, 1082272, 1082281 |
| RF-09 | Depuración periódica evaluaciones (DataFactory) | Alta | 47 | 1076668, 1076922, 1076945, 1076947, 1076961 |
| RF-10 | Depuración histórica one-off (SQL) | Alta | 5 | 1035171 |
| RF-11 | Evitar duplicidad Registraduría (CC) | Alta | 26 | 1081870, 1081880, 1081885, 1081888 |
| RF-12 | Evitar duplicidad datos básicos (CC/CE/PPT) | Media | 4 | 1035498 |
| RF-13 | Evitar duplicidad cuestionario identidad | Media | 4 | 1035502 |
| RF-14 | Evitar duplicidad Migración Colombia (CE/PPT) | Media | 4 | 1037054 |
| RF-15 | Corregir datos cliente (Registraduría/Migración) | Media | 5 | 1037085 |
| RF-16 | Módulo admin gestión estado documento | Alta | 49 | 1096171, 1096178, 1096189, 1096205, 1096228, 1096310, 1096313 |
| **Total** | | | **316** | **42 HUs directas** |

---

## 6. HUs del PRD/RF por objetivo estratégico

```
O1 — Formularios (cumplimiento normativo)
├── RF-01 → HU 1025877
├── RF-02 → HU 1082005, 1082032, 1082042, 1082089
├── RF-03 → HU 1026762
├── RF-04 → HU 1026765
├── RF-05 → HU 1079051, 1079058, 1079062, 1046415, 1046438, 1046535
├── RF-06 → HU 1026776
├── RF-07 → HU 1032311
└── RF-08 → HU 1082241, 1082249, 1082267, 1082270, 1082272, 1082281

O2 — Reducir costos consultas duplicadas
├── RF-11 → HU 1081870, 1081880, 1081885, 1081888
├── RF-12 → HU 1035498
├── RF-13 → HU 1035502
└── RF-14 → HU 1037054

O3 — Depuración base de datos
├── RF-09 → HU 1076668, 1076922, 1076945, 1076947, 1076961
└── RF-10 → HU 1035171

O4 — Validador de identidad transversal (MS-1101)
├── RF-11 → HU 1081885
├── RF-15 → HU 1037085
└── RF-16 → HU 1096171, 1096178, 1096189, 1096205, 1096228, 1096310, 1096313
```

---

## 7. Puntos de atención

| # | Descripción | RF / HUs afectados |
|---|-------------|-------------------|
| ✅ 1 | Los repositorios `1101-validadorcliente_identidad-ms` y `1101-validadorcliente_identidad-fr` **sí existen en Azure DevOps** — confirmado en la documentación técnica de `ValidarIdentidadExperian` ([ConfiguracionAmbiente.md v16](../Sarlaft40/ValidarIdentidadExperian/DocumentacionTecnica/MicroservicioIdentityValidator/ConfiguracionAmbiente.md), [FrontValidarIdentidad.md](../Sarlaft40/ValidarIdentidadExperian/DocumentacionTecnica/IntegracionesValidarIdentidad/FrontValidarIdentidad.md)). El RF.md indicaba "pendiente creación (verificado 06/04/2026)" pero la doc técnica contradice esa afirmación. | RF-11, RF-15, RF-16 |
| ⚠️ 2 | Todas las HUs están en estado **New**. No hay ninguna en progreso o completada al corte de este informe. | Todo el backlog |
| ⚠️ 3 | La validación de archivos con **Apache Tika** (RF-02) es un control de seguridad crítico (OWASP A05). Debe incluirse en criterios de aceptación de HU 1082005 y 1082032. | RF-02 |
| ⚠️ 4 | RF-09 requiere que la depuración se ejecute en **ventana no productiva** con rollback controlado. Los criterios de aceptación de las HUs 1076945 y 1076947 deben reflejarlo. | RF-09 |
| ⚠️ 5 | 80 HUs del backlog están **fuera del alcance directo de los 16 RF del PRD** (habilitadores, integraciones de negocio, monitoreo). Requieren priorización adicional. | Secciones 4 de este informe |
| ⚠️ 6 | El componente Validador de Identidad tiene **dos naming conventions** en los repositorios: `1101-validadorcliente_identidad-*` (nombre nuevo en configuración de ambiente) y `adm_y_fin-validadorcliente-identidad-*` (nombre usado en docs de certificados y pruebas). Confirmar con infraestructura cuál es el nombre canónico. | RF-11, RF-15, RF-16 |
| ⚠️ 7 | El repo del Front Angular tiene también dos nombres de configuración: `892-sarlaft-fr-conf` (doc configuración ambiente) y `adm_y_fin-sarlaft-fr-conf` (doc despliegue). Verificar cuál está activo. | RF-01 a RF-08, RF-11, RF-16 |

---

## 8. Catálogo de Repositorios (validado desde Documentación Técnica Sarlaft40)

Todos los repositorios están bajo `https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/`

### 8.1 Microservicios principales (código fuente)

| # | Componente | Repo código | Repo configuración | Repo pruebas | RF impactados |
|---|------------|-------------|-------------------|--------------|---------------|
| 1 | **SarlaftAPI** | [`892-sarlaft-api-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms) *(también: `adm_y_fin-sarlaft-api-ms`)* | [`892-sarlaft-api-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-conf) *(también: `adm_y_fin-sarlaft-api-conf`)* | [`892-sarlaft-pa`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-pa) | RF-01 a RF-08, RF-11–15 |
| 2 | **SarlaftEngine (BRMS)** | [`892-sarlaft-brms-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms) | [`892-sarlaft-brms-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-conf) *(también: `adm_y_fin-sarlaft-brms-conf`)* | [`892-sarlaft-brms-pa`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-pa) | RF-02, RF-05, RF-06, RF-08 |
| 3 | **Front Angular** | [`892-sarlaft-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) | [`892-sarlaft-fr-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr-conf) *(también: `adm_y_fin-sarlaft-fr-conf`)* | — | RF-01 a RF-08, RF-11, RF-16 |
| 4 | **Backweb (admin-ms)** | [`892-sarlaft-admin-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-ms) | [`892-sarlaft-admin-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-conf) | — | RF-07 |
| 5 | **SarlaftBatch** | [`892-sarlaft-batch-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-batch-ms) | [`892-sarlaft-batch-ms-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-batch-ms-conf) | [`892-sarlaft-batch-pa`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-batch-pa) | RF-05, RF-09 |
| 6 | **SarlaftWebhook** | [`892-sarlaft_callback-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_callback-ms) | [`892-sarlaft_callback-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_callback-conf) *(también: `adm_y_fin-sarlaft-sarlaft_callback-conf`)* | [`892-sarlaft_callback-pa`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_callback-pa) | Sin impacto directo de RF |
| 7 | **SarlaftClientesMS** | [`892-sarlaft4-sarlaftclientes-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4-sarlaftclientes-ms) | [`892-sarlaft4-sarlaftclientes-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4-sarlaftclientes-conf) | [`892-sarlaft4-sarlaftclientes-pa`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4-sarlaftclientes-pa) | Sin impacto directo de RF |
| 8 | **Validador Identidad MS** *(proyecto 1101)* | [`1101-validadorcliente_identidad-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) *(también: `adm_y_fin-validadorcliente-identidad-ms`)* | [`1101-validadorcliente_identidad-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-conf) *(también: `adm_y_fin-validadorcliente-identidad-conf`)* | [`1101-validadorcliente_identidad-pa`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-pa) *(también: `adm_y_fin-validadorcliente-identidad-pa`)* | RF-11–16 |
| 9 | **Validador Identidad Front** *(proyecto 1101)* | [`1101-validadorcliente_identidad-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr) *(también: `892-validadorcliente_identidad-fr`)* | — | — | RF-16 |
| 10 | **PEPS MS** | [`1170-peps_pepsms-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1170-peps_pepsms-ms) | [`1170-peps_pepsms-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1170-peps_pepsms-conf) | [`1170-peps_pepsms-pa`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1170-peps_pepsms-pa) | Sin impacto directo de RF |

### 8.2 Microservicios integradores (MI)

| # | Integrador | Repo código | Repo configuración | RF impactados |
|---|-----------|-------------|-------------------|---------------|
| 1 | **P8 MI** (documental) | [`892-sarlaft_function_documental-mi`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_function_documental-mi) | [`892-sarlaft-function_p8-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_p8-conf) | RF-05 |
| 2 | **Requisitos MI** | [`892-sarlaft-function_requisitos-mi`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_requisitos-mi) | [`892-sarlaft-function_requisitos-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_requisitos-conf) | RF-02, RF-05 |
| 3 | **Batch MI** | [`892-sarlaft-function_batch-mi`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_batch-mi) | [`892-sarlaft-function_batch-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_batch-conf) | RF-09 |
| 4 | **Identidad MI** | [`892-sarlaft-function_identity-mi`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_identity-mi) | [`892-sarlaft-function_identity-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_identity-conf) | RF-11–14 |
| 5 | **Webhook MI** | — | [`892-sarlaft-function_webhook-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_webhook-conf) | Sin impacto directo |
| 6 | **CCM MI** | — | [`892-sarlaft-function_ccm-conf`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-function_ccm-conf) | Sin impacto directo |

### 8.3 Azure Data Factory

| Componente | Repositorio | RF impactados |
|-----------|------------|---------------|
| DataFactory pipelines depuración | [`892-sarlaft4_adm_y_fin_sarlaft-md`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4_adm_y_fin_sarlaft-md) | RF-09 |

### 8.4 Discrepancias detectadas entre RF.md y la Documentación Técnica

| Ítem en RF.md | Nombre en Documentación Técnica | Corrección necesaria |
|---------------|--------------------------------|----------------------|
| `892-sarlaft-api-ms` / `adm_y_fin-sarlaft-api-ms` (sin diferenciar) | `892-sarlaft-api-ms` (código fuente principal) | El repo de código es `892-sarlaft-api-ms`; `adm_y_fin-sarlaft-api-ms` puede ser alias o rama de naming convention más reciente — confirmar con el equipo |
| `1101-validadorcliente_identidad-ms` ⚠️ *(pendiente creación)* | [`1101-validadorcliente_identidad-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) **ya existe** con setup completo documentado (Java 11, Gradle 6.8, pipeline #3786) | Eliminar la marca ⚠️ — el repo **existe** |
| `1101-validadorcliente_identidad-fr` ⚠️ *(pendiente creación)* | [`1101-validadorcliente_identidad-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr) **ya existe** confirmado en FrontValidarIdentidad.md | Eliminar la marca ⚠️ — el repo **existe** |
| `892-sarlaft-admin-ms` referenciado como "Backweb" | Confirmado como `892-sarlaft-admin-ms` | Sin corrección |
| No mencionado en RF.md | `892-sarlaft-function_identity-mi` (Identidad MI) — integrador que media entre SarlaftAPI y el MS Validador | Agregar a la lista de repositorios de configuración que deben ajustarse en RF-11 |
| No mencionado en RF.md | `892-sarlaft4_adm_y_fin_sarlaft-md` (DataFactory) | Agregar explícitamente en RF-09 como repositorio de infraestructura de ADF |

---

## 9. Mapa de Dependencias y Orden de Desarrollo

> Análisis generado el **08/04/2026** a partir de las **118 HUs** leídas directamente de los archivos en `docs/Epica/`.  
> Objetivo: establecer el orden de implementación para evitar bloqueos entre equipos.  
> Cada OLA puede ejecutarse internamente en paralelo salvo dependencias explícitas señaladas en la columna **Depende de**.

### 9.1 Leyenda de Repositorios

| Alias | Repositorio / Sistema | Tipo |
|---|---|---|
| **admin-ms** | [`892-sarlaft-admin-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-ms) | Microservicio Backend (Backweb) |
| **motor** | [`892-sarlaft-brms-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms) | Motor de reglas SARLAFT |
| **sarlaft-clientes** | [`892-sarlaft4-sarlaftclientes-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4-sarlaftclientes-ms) | Microservicio Backend |
| **SARLAFTAPI** | [`892-sarlaft-api-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms) | API principal / Facade |
| **api-terceros** | [`892-sarlaft-api-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms) (módulo terceros) | Integraciones externas |
| **front** | [`892-sarlaft-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) | Frontend Angular |
| **webcomponent** | [`892-sarlaft-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) (webcomponent) | Componente embebido |
| **webhook** | [`892-sarlaft_callback-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_callback-ms) | Servicio de eventos (callback) |
| **validador-ms** | [`1101-validadorcliente_identidad-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) | Microservicio Backend MS-1101 (Validador Identidad) |
| **validador-fr** | [`1101-validadorcliente_identidad-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr) | Frontend Angular MS-1101 (Validador Identidad) |
| **DataFactory** | [`892-sarlaft4_adm_y_fin_sarlaft-md`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4_adm_y_fin_sarlaft-md) | Azure Data Factory + IaC |
| **BD** | PostgreSQL `sarlaft` schema | Base de Datos |
| **ext-Experian** | Experian (externo) | Servicio Externo |
| **ext-Infolaft** | Infolaft / Informacolombia / ADRES (externos) | Servicios Externos |
| **ext-CCM** | CCM Canal Comunicaciones (externo) | Sistema Externo |
| **ext-ModeloClientes** | Modelo de Clientes Sura (externo) | Sistema Externo |

---

### 9.2 OLA 0 — Habilitadores *(pre-condición de todo)*

> Sin estas HUs el resto no puede iniciar. Son fundacionales y no dependen entre sí.

| ID | Historia de Usuario | Repo Principal | Repos Secundarios | Servicios afectados |
|---|---|---|---|---|
| [1029945](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029945) | [Monitoreo] Infra IaC — Suscripción, DataFactory, Integration Runtime | `DataFactory` | Azure Subscriptions | Suscripción Monitoreo LAFT, ADF Dllo/Labo/Pdn |
| [1032876](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032876) | Integración Modelo de Clientes (sync bidireccional) | `admin-ms` | `ext-ModeloClientes` | Sync Tratamiento de Datos, Modelo SARLAFT |
| [1026983](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026983) | [Datos mínimos] Reglas con Registraduría / Migración Colombia | `admin-ms` | `ext-Experian` | Verificación datos básicos del cliente |
| [1035171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171) | [Optimización] Depuración BD histórico 2021–2024 (one-off) | `BD` | `admin-ms` | Tabla evaluaciones, snapshot `/assessment` |

---

### 9.3 OLA 1 — Modelos Core y Motores Base

> Define estructuras de datos y motores que toda la lógica de negocio posterior consume.

| ID | Historia de Usuario | Repo Principal | Repos Secundarios | Servicios afectados | Depende de |
|---|---|---|---|---|---|
| [1029968](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029968) | [Monitoreo] Pipeline Despliegue DataFactory | `DataFactory` | IaC repo | Pipelines Dllo/Labo/Pdn | 1029945 |
| [1081880](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081880) | [RF-11] Validador Identidad — IaC (pipeline, BD, Redis MS-1101) | `validador-ms` | Azure Infra | Infraestructura nueva MS-1101 Dllo/Labo/Pdn | 1026983 |
| [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) | [Formulario] Tipificar PJ por tipo de sociedad | `admin-ms` | `BD` | Motor tipificación, campo tipo sociedad | — |
| [1026815](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026815) | [Motor] Reglas para figuras de Rentas | `motor` | — | Motor de reglas SARLAFT | — |
| [1096695](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096695) | [Conexión Manual] Modelo/entidades BD Rentas (suboperación, recaudo, valor pago) | `admin-ms` | `BD` | `/assessment`, entidad Póliza | — |
| [1078435](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078435) | [Conexión Manual] Nuevas figuras Back 1 (Delegado / Responsable / Beneficiario) | `SARLAFTAPI` + `admin-ms` | `BD` | `/assessment`, formulario terceros | — |
| [1096589](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096589) | [Cancelaciones] Modificar servicio `/assessment` — operación cancelación | `admin-ms` | `ext-CCM` | `/assessment`, deshabilitar notif. CCM | — |

---

### 9.4 OLA 2 — Lógica de Negocio y Procesos Batch

> Puede ejecutarse en paralelo dentro de la ola. Requiere OLA 0 y OLA 1 completas.

| ID | Historia de Usuario | Repo Principal | Repos Secundarios | Servicios afectados | Depende de |
|---|---|---|---|---|---|
| [1026823](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026823) | [Evaluación] Reglas figuras de Rentas | `motor` | — | Reglas evaluación Rentas | 1026815 |
| [1026827](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026827) | [Evaluación] Crear operaciones evaluar Rentas | `motor` + `admin-ms` | — | Operaciones evaluación | 1026815, 1026823 |
| [1029972](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029972) | [Monitoreo] ONU / OFAC / Terroristas — batch Infolaft | `DataFactory` | `ext-Infolaft` | Batch diario lista control | 1029945, 1029968 |
| [1029992](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029992) | [Monitoreo] PJ Informacolombia — batch | `DataFactory` | `ext-Infolaft` | Batch diario PJ | 1029945, 1029968 |
| [1029994](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029994) | [Monitoreo] Listas PEP Infolaft — batch | `DataFactory` | `ext-Infolaft` | Batch diario PEP | 1029945, 1029968 |
| [1030004](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1030004) | [Monitoreo] Lista DIAN Infolaft — batch | `DataFactory` | `ext-Infolaft` | Batch diario DIAN | 1029945, 1029968 |
| [1031933](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1031933) | [Monitoreo] Lista IPS ADRES — batch | `DataFactory` | `ext-Infolaft` | Batch diario ADRES | 1029945, 1029968 |
| [1078438](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078438) | [Conexión Manual] sarlaftclientes — nuevas figuras | `sarlaft-clientes` | — | Modelo de figuras en microservicio | 1078435 |
| [1078446](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078446) | [Conexión Manual] Back 2 Motor — nuevas figuras | `motor` | — | Motor controles por figura | 1078435 |
| [1096598](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096598) | [Cancelaciones] Nuevo motor para cancelaciones | `motor` | — | Motor específico cancelaciones | 1096589 |
| [1035498](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035498) | [Optimización] Evitar duplicidad datos básicos Experian | `admin-ms` | `api-terceros` · `webcomponent` · `webhook` | Crear evaluación, estados bloqueantes datos básicos | 1026983 |
| [1035502](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035502) | [Optimización] Evitar duplicidad cuestionario Experian | `admin-ms` | `api-terceros` · `webcomponent` · `webhook` | Crear evaluación, estados bloqueantes cuestionario | 1026983 |
| [1037054](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037054) | [Optimización] Evitar duplicidad Migración Colombia | `admin-ms` | `api-terceros` · `webhook` | Crear evaluación, estados bloqueantes Migración CO | 1026983 |
| [1037085](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037085) | [Optimización] Reemplazar datos consulta estado documento | `admin-ms` | `ext-Experian` | Corrección nombres / fecha expedición en evaluación | 1026983 |

---

### 9.5 OLA 3 — Formularios, APIs y Servicios

> Las HUs de formulario pueden desarrollarse en paralelo entre sí.

| ID | Historia de Usuario | Repo Principal | Repos Secundarios | Servicios afectados | Depende de |
|---|---|---|---|---|---|
| [1025877](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1025877) | [Formulario] Campo actividad económica CIIU 4 | `admin-ms` | `BD` | Formulario PN/PJ, catálogo CIIU | — |
| [1026762](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026762) | [Formulario] Ingresos y egresos PN/PJ | `admin-ms` | `BD` | Formulario datos financieros | — |
| [1026765](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026765) | [Formulario] Activos y pasivos PN/PJ | `admin-ms` | `BD` | Formulario datos financieros | — |
| [1078462](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1078462) | [Conexión Manual] API Terceros — nuevas figuras | `api-terceros` | — | Servicio guardar formulario | 1078435 |
| [1096829](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096829) | [Conexión Manual] Ajuste servicio resultados evaluación Rentas | `admin-ms` | — | `/sarlaftbackweb/resultevaluation` | 1096695 |
| [1096836](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096836) | [Conexión Manual] Reglas motor riesgo Rentas (Excel config) | `motor` | — | Motor riesgo, archivo Excel configuración | 1096695 |
| [1096832](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096832) | [Conexión Manual] Creación evaluaciones Rentas — API Terceros | `api-terceros` | — | APIs terceros evaluaciones, pruebas E2E | 1096695, 1096836 |
| [1096591](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096591) | [Cancelaciones] API terceros — operación cancelación | `api-terceros` | `ext-CCM` | Flujo evaluación cancelación | 1096589 |
| [1096599](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096599) | [Cancelaciones] Ajuste webhook — notificación cancelaciones | `webhook` | — | Evento notificación cancelaciones | 1096591 |
| [1082361](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082361) | [Actualización] Reenvío masivo Back — servicios consulta/programación | `admin-ms` | `BD` | Servicios reenvío, programación batch | — |
| [1082389](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082389) | [Actualización] Modelo notificación y reenvío | `admin-ms` | `BD` | Modelo notificación reenvío | — |
| [1081885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081885) | [RF-11] Validador Identidad Admon MS — nuevo microservicio Back (estados bloqueantes) | `validador-ms` | `BD` · `ext-Experian` | MS-1101 core, estados bloqueantes permanentes y temporales | 1026983, 1081880 |
| [1081888](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081888) | [RF-11] ValidadorIdentidad MS — integración SarlaftAPI | `SARLAFTAPI` | `validador-ms` | Consumo MS-1101 desde SarlaftAPI existente | 1081885 |

---

### 9.6 OLA 4 — Use Cases Complejos e Integraciones

> Requiere que los formularios, modelos y motores de OLAs 1–3 estén listos.

| ID | Historia de Usuario | Repo Principal | Repos Secundarios | Servicios afectados | Depende de |
|---|---|---|---|---|---|
| [1032311](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032311) | [Formulario] Cláusula tratamiento de datos | `admin-ms` + `front` | `ext-ModeloClientes` | Formulario, sync diario Modelo Clientes | 1032876 |
| [1041366](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041366) | [Reglas transversales] Herencia por tipo de riesgo | `admin-ms` | `ext-Experian` · `ext-Infolaft` | Evidencias identidad/listas, herencia | Monitoreo OLA 2, Experian |
| [1035971](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035971) | [Riesgo] Determinar riesgo único del cliente | `admin-ms` | `motor` | Motor tipificación, riesgo único diario | 1026776, 1041366 |
| [1040402](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1040402) | [Actualización] Diligenciamiento del Formulario | `front` + `api-terceros` | `ext-Experian` · `ext-Infolaft` | Formulario actualización, validación identidad | 1025877, 1026762, 1026765 |
| [1041011](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041011) | [Actualización] Notificaciones a Directores y Gerentes (mensual) | `admin-ms` | `ext-CCM` | Proceso mensual, plantillas CCM por rol | Estados de clientes disponibles |
| [1082387](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082387) | [Actualización] Proceso masivo de notificaciones | `admin-ms` | — | Batch notificaciones masivas | 1082361, 1082389 |
| [1096601](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096601) | [Cancelaciones] Servicio backweb cambiar estado front | `admin-ms` | `front` | `/sarlaftbackweb/resultevaluation`, rechazar evaluaciones | 1096589, 1096598 |
| [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) | [RF-16] Validador Identidad Admon MS — Servicios gestión estado cliente | `validador-ms` | `BD` · `ext-Experian` | CRUD estado cliente, consulta resultado Registraduría/Migración | 1026983, 1081885 |
| [1096178](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096178) | [RF-16] Validador Identidad Admon MS — Servicios gestión parametrías validación | `validador-ms` | `BD` | CRUD reglas de bloqueo | 1081885 |
| [1096189](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096189) | [RF-16] Validador Identidad Admon MS — Servicios gestión parametrías (parte 2) | `validador-ms` | `BD` | Continuación CRUD parametrías | 1096178 |

---

### 9.7 OLA 5 — Frontend y Capa de Presentación

> Toda la UI va al final. Puede iniciarse en paralelo con OLA 4 **solo si los contratos de API están definidos y comunicados**.

| ID | Historia de Usuario | Repo Principal | Repos Secundarios | Servicios afectados | Depende de |
|---|---|---|---|---|---|
| [1082386](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082386) | [Actualización] Reenvío masivo — Front | `front` | `admin-ms` | Módulo reenvío masivo | 1082361 |
| [1083734](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1083734) | [Actualización] Retirar opción cancelar evaluaciones (perfil no Admin) | `front` | — | Grilla Módulo Clientes | — |
| [1076693](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076693) | [Actualización] Botón cambiar estado Desactualizado→Actualizado | `front` | `admin-ms` | Grilla Módulo Clientes, modal LA/FT | Flujo evaluación |
| [1077124](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077124) | [Actualización] Levantar validación identidad manual (Admin) | `front` | `admin-ms` | Modal autorización, evidencia Experian | Proceso aprobación Negocio Nuevo |
| [1096837](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096837) | [Conexión Manual] Front pantalla "CREAR EVALUACIÓN" — Rentas | `front` | `admin-ms` | Pantalla crear evaluación, campos suboperación/recaudo | 1096829 |
| [1097345](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097345) | [Conexión Manual] Front módulo consultas clientes — nuevas figuras | `front` | `admin-ms` | Módulo consultas, nuevas figuras Educación/Pensión | 1078435 |
| [1097347](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097347) | [Conexión Manual] Front redirect — nuevas figuras | `front` | — | Front redirect flujo manual | 1078435 |
| [1097349](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097349) | [Conexión Manual] Front módulo crear evaluación — nuevas figuras | `front` | — | Módulo crear evaluación | 1078435 |
| [1097354](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1097354) | [Conexión Manual] Front sarlaftbackweb — nuevas figuras | `front` | `admin-ms` | Consulta nuevas figuras sarlaftbackweb | 1078435, 1078446 |
| [1081870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081870) | [RF-11] Front Pantalla Módulo Sarlaft — resultado Registraduría en detalles figuras | `front` | `validador-ms` | Datos adicionales, resultado Registraduría en módulo Sarlaft | 1081885, 1081888 |
| [1096205](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096205) | [RF-16] Validador Identidad Admon Front — Gestión estado cliente Parte 1 | `validador-fr` | `validador-ms` | UI gestión estado cliente | 1096171 |
| [1096228](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096228) | [RF-16] Validador Identidad Admon Front — Gestión estado cliente Parte 2 | `validador-fr` | `validador-ms` | Continuación UI gestión estado | 1096205 |
| [1096310](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096310) | [RF-16] Validador Identidad Admon Front — Parametrías validación Parte 1 | `validador-fr` | `validador-ms` | UI CRUD reglas bloqueo | 1096178, 1096189 |
| [1096313](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096313) | [RF-16] Validador Identidad Admon Front — Parametrías validación Parte 2 | `validador-fr` | `validador-ms` | Continuación UI parametrías | 1096310 |

---

### 9.8 OLA 6 — Migración y Validación Final

| ID | Historia de Usuario | Repo Principal | Repos Secundarios | Servicios afectados | Depende de |
|---|---|---|---|---|---|
| [1041068](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041068) | [Clientes] Migración | `admin-ms` + `BD` | `ext-ModeloClientes` | Migración datos clientes | Modelo completo OLA 1–4 |
| [1096602](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096602) | [Cancelaciones] Pruebas punta a punta | `admin-ms` + `motor` + `api-terceros` + `front` | `webhook` | Flujo completo cancelaciones | Todas las HUs de Cancelaciones |

---

### 9.9 Resumen: HUs por Repositorio

| Repositorio | Alias | HUs afectadas | OLAs |
|---|---|---|---|
| [`892-sarlaft-admin-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-admin-ms) | `admin-ms` | **28** | 0–6 |
| [`1101-validadorcliente_identidad-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-ms) | `validador-ms` | **6** | 1–4 |
| [`892-sarlaft-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-fr) | `front` | **12** | 4–5 |
| [`1101-validadorcliente_identidad-fr`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr) | `validador-fr` | **4** | 5 |
| [`892-sarlaft4_adm_y_fin_sarlaft-md`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4_adm_y_fin_sarlaft-md) | `DataFactory` | **6** | 0–2 |
| [`892-sarlaft-brms-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms) | `motor` | **6** | 1–4 |
| [`892-sarlaft-api-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-api-ms) | `api-terceros` / `SARLAFTAPI` | **7** | 1–4 |
| [`892-sarlaft_callback-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft_callback-ms) | `webhook` | **2** | 3–6 |
| [`892-sarlaft4-sarlaftclientes-ms`](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft4-sarlaftclientes-ms) | `sarlaft-clientes` | **1** | 2 |
| `PostgreSQL schema sarlaft` | `BD` | **3** | 0–1 |

> **`admin-ms` es el repositorio con mayor concentración de cambios (28 HUs)**. Planificar revisiones de arquitectura y gestión de ramas con el equipo de Backweb antes de iniciar OLA 1.

### 9.10 Grafo de Dependencias Crítico

```
1029945 (Infra Monitoreo — DataFactory)
  └─► 1029968 (Pipeline despliegue)
        └─► 1029972, 1029992, 1029994, 1030004, 1031933

1026983 (Datos mínimos — Experian/Registraduría)
  ├─► 1035498, 1035502, 1037054, 1037085
  └─► 1081880 (IaC MS-1101)
        └─► 1081885 (MS-1101 nuevo microservicio Back)
              ├─► 1081888 (integración SarlaftAPI)
              │     └─► 1081870 (front pantalla Módulo Sarlaft)
              ├─► 1096171 (gestión estado cliente Back) ←── bloquea front
              │     └─► 1096205 ─► 1096228 (front gestión estado)
              └─► 1096178 ─► 1096189 (parametrías validación Back)
                    └─► 1096310 ─► 1096313 (front parametrías)

1032876 (Integración Modelo Clientes)
  └─► 1032311

1078435 (Nuevas figuras Back 1 — admin-ms + SARLAFTAPI)
  ├─► 1078438 (sarlaft-clientes)
  ├─► 1078446 (motor)
  ├─► 1078462 (api-terceros)
  └─► 1097345, 1097347, 1097349, 1097354 (front)

1096695 (Modelo BD Rentas — admin-ms)
  ├─► 1096836 (motor) ─► 1096832 (api-terceros)
  └─► 1096829 (admin-ms) ─► 1096837 (front)

1096589 (Assessment Cancelaciones — admin-ms)
  ├─► 1096591 (api-terceros) ─► 1096599 (webhook)
  ├─► 1096598 (motor) ─► 1096601 (admin-ms)
  └─► 1096602 (pruebas E2E — todos)

1026815 (Motor Rentas — brms-ms)
  └─► 1026823 ─► 1026827 (motor + admin-ms)
```
