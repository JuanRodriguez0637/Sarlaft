# Servicio Evaluación Validación Sarlaft

> **Fuente Confluence:** [Servicio Evaluación Validación Sarlaft](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814233305)
> **Última modificación:** 2024-01-15 — Diana Muñoz · versión 10
> **Sección:** [Servicios Web](./index.md)
## Descripción

- **Objetivo:** Permite realizar las validaciones mínimas para clasificar el riesgo de un cliente y determinar el tipo de sarlaft que debe diligenciar de acuerdo a la naturaleza del cliente y del producto. Se denomina como un proceso de evaluación dado que según el resultado de información del tomador, se indica qué información debe solicitarse para los asegurados y beneficiarios.

  También permite realizar el proceso de reclamaciones; en los adjuntos se encuentran las 2 peticiones de REPN y REPJ, correspondientes a reclamaciones de PN y PJ.

- **Endpoint:** `POST /sarlaftserv/assessment`
- **Perfil de Seus4:** `PF_CONSUMSERVSARLAFTAPI`

### Nuevo Endpoint

- **Endpoint:** `POST /sarlaftserv/v1/evaluaciones`
- **Perfil de Seus4:** aún no creado para consumo interno a SURA.

---

## Archivos JSON de Ejemplo

Los archivos están disponibles en [`ServicioEvaluacionValidacion/`](./ServicioEvaluacionValidacion/).

| Archivo | Descripción |
| --------- | ------------- |
| [AsessmentREPJ.json](./ServicioEvaluacionValidacion/AsessmentREPJ.json) | Request de evaluación para Reclamación PJ |
| [AsessmentREPN.json](./ServicioEvaluacionValidacion/AsessmentREPN.json) | Request de evaluación para Reclamación PN |
| [TomadorPJ.json](./ServicioEvaluacionValidacion/TomadorPJ.json) | Request de evaluación para Tomador Persona Jurídica |
| [Assessemt.json](./ServicioEvaluacionValidacion/Assessemt.json) | Request de evaluación general |
| [request_assessment.json](./ServicioEvaluacionValidacion/request_assessment.json) | Request base de assessment |
| [RequestListAfilaidos.json](./ServicioEvaluacionValidacion/RequestListAfilaidos.json) | Request para lista de afiliados |

---

## Dependencias

- Base de Datos Sarlaft
- Motor de Reglas - API
- Validaciones de Peps - Mensajería
- Validación de Listas Vinculantes - Mensajería

---

> **Nota:** Para el cotizador de vida se agregó un nuevo campo `tipoFormulario` en la respuesta, el cual devuelve el tipo de formulario por sarlaft, especialmente para este `egv`.
