# Validación por figura | ApiTerceros

> **Fuente Confluence:** [Validación por figura | ApiTerceros](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2676588688)
> **Última modificación:** 2022-04-06 — Edwin Didier Méndez Rojas - Ceiba Software · versión 1
> **Sección:** [ApiTerceros](./index.md)

- **Objetivo:** Proveer una conexión a terceros al motor de validaciones de las figuras de un Evaluación en el proceso de Sarlaft.
- **Query:** `Evaluacion.externos.sarlaft.validaciones`
- **Nota:** los ejemplos a continuación se hicieron desde un proyecto sender que se comunicaba en la cola de service bus.

| Data Request | Data | Tipo | Observaciones/Valores |
| --- | --- | --- | --- |
| `codigoOperacion` | **Requerido** | String | Ejemplos:\
01 → Negocio Nuevo\
RE → Reclamación |
| `sarlaft.cliente.tipoPersona` | **Requerido** | String | N → Persona Natura\
J → Persona Juridica |
| `sarlaft.riesgo.tipoRiesgo` | **Requerido** | String | INTENSIFICADO\
SIMPLIFICADO\
ORDINARIO |
| `evaluacionId` | **Opcional** | String | dato para realizar traza a la petición - splunk |

![image-20220406-024809.png](./attachments/image-20220406-024809.png)

| Data Response | Data | Tipo | Observaciones/Valores |
| --- | --- | --- | --- |
| `validaciones` | **Requerido** | List | validaciones que debe tener la figura |
| `validaciones[n].codigo` | **Requerido** | String | Nombre de la validación |
| `validaciones[n].bloqueante` | **Requerido** | Boolean | Indicador si es bloqueante en el proceso |
| `error` | **Requerido** | String | si retorna un mensaje diferente a null nos indica que occurrio un error en el proceso de ejecutar las validaciones, o algun campo requerido no se envio |
| `flowlog` | **No Requerido** | List | permite ver las condiciones que cumplio la figura en proceso del motor, Dato tecnico del proyecto |
| `lastflowlog` | **No Requerido** | String | Datos Tecnico del proyecto |

![image-20220406-025322.png](./attachments/image-20220406-025322.png)

- Error

![image-20220406-031042.png](./attachments/image-20220406-031042.png)

**Query Request:**

[Query-Request.json](./attachments/Query-Request.json)

**Query Response:**

[Query-Response.json](./attachments/Query-Response.json)

**Query Error Request:**

[Query-Error-Response.json](./attachments/Query-Error-Response.json)
