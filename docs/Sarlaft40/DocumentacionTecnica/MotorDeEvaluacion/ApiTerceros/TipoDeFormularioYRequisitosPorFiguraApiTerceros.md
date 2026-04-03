# Tipo de formulario y requisitos por figura | ApiTerceros

> **Fuente Confluence:** [Tipo de formulario y requisitos por figura | ApiTerceros](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2740748352)
> **Última modificación:** 2022-05-23 — Diego Alejandro Vélez González · versión 3
> **Sección:** [ApiTerceros](./index.md)

- **Objetivo:** Proveer una conexión a terceros al motor de tipo de formulario y requisitos de las figuras de un Evaluación en el proceso de Sarlaft.
- **Query:** `Evaluacion.externos.sarlaft.formulario.requisitos`
- **Nota:** los ejemplos a continuación se hicieron desde un proyecto sender que se comunicaba en la cola de service bus.

| **Data Request** | **Data** | **Tipo** | **Observaciones/Valores** |
|---|---|---|---|
| **`codigoRamo`** | **Requerido** | String | Ejemplos:<br> 041 → Soat<br>094 → ARL |
| **`error`** | **Requerido** | String | null |
| **`sarlafts`** | **Requerido** | List | Sarlafts a procesar |
| **`sarlafts[n].id`** | **Requerido** | String | Ejemplo: `00005120-5a52-4fd8-9acf-423e861fdf44` |
| **`sarlafts[n].tipoPersona`** | **Requerido** | String | N → Persona Natura<br>J → Persona Juridica |
| **`sarlafts[n].tipoRiesgo`** | **Requerido** | String | INTENSIFICADO<br>SIMPLIFICADO<br>ORDINARIO |

![image-20220523-171011.png](./attachments/image-20220523-171011.png)

| **Data Response** | **Data** | **Tipo** | **Observaciones/Valores** |
|---|---|---|---|
| **`id`** | **No Requerido** | String | id de la evaluación a procesar |
| **`sarlafts`** | **Requerido** | List | Sarlafts procesados |
| **`sarlafts[n].id`** | **Requerido** | String | id del sarlaft procesado |
| **`sarlafts[n].tipoPersona`** | **Requerido** | String | N → Persona Natura<br>J → Persona Juridica |
| **`sarlafts[n].tipoRiesgo`** | **Requerido** | String | INTENSIFICADO<br>SIMPLIFICADO<br>ORDINARIO |
| **`sarlafts[n].tipoFormulario`** | **Requerido** | String | SIMPLIFICADO_PN<br>SIMPLIFICADO_PJ<br>ORDINARIO_PN<br>ORDINARIO_PJ<br>INTENSIFICADO_PN<br>INTENSIFICADO_PJ |
| **`sarlafts[n].requisitos[n]`** | **Requerido** | List | Requisitos de la figura |
| **`sarlafts[n].requisitos[n].id`** | **Requerido** | String | id del requisito |
| **`sarlafts[n].requisitos[n].codigo`** | **Requerido** | String | código del requisito |
| **`sarlafts[n].requisitos[n].nombre`** | **Requerido** | String | Nombre del requisito |
| **`sarlafts[n].requisitos[n].fechaCreacion`** | **Requerido** | Date | Fecha de creación |
| **`sarlafts[n].requisitos[n].ultimaActualizacion`** | **Requerido** | Date | Fecha de actualización |
| **`sarlafts[n].requisitos[n].estado`** | **Requerido** | String | Estado del requisito |
| **`sarlafts[n].requisitos[n].estadoRequisito`** | **Requerido** | String | Estado del requisito |
| **`sarlafts[n].requisitos[n].idGestorDocmental`** | **Requerido** | String | id del gestor documental |
| **`sarlafts[n].requisitos[n].nombreDocumento`** | **Requerido** | Boolean | Indicador si es bloqueante en el proceso |
| **`sarlafts[n].requisitos[n].extension`** | **Requerido** | String | Extensión |
| **`sarlafts[n].requisitos[n].vigencia`** | **Requerido** | Long | días de vigencia |
| **`sarlafts[n].requisitos[n].obligatorio`** | **Requerido** | boolean | Indica la obligatoriedad del requisito |
| **`sarlafts[n].flowlog`** | **No Requerido** | List | permite ver las condiciones que cumplió la figura en proceso del motor, Dato técnico del proyecto |
| **`error`** | **Requerido** | String | si retorna un mensaje diferente a null nos indica que ocurrió un error en el proceso de ejecución, o algún campo requerido no se envió |
| **`codigoRamo`** | **Requerido** | String | Ejemplos:<br> 041 → Soat<br>094 → ARL |

![image-20220523-174620.png](./attachments/image-20220523-174620.png)

**Query Request:**

📎 [Response.json](./attachments/Response.json)

**Query Response:**

📎 [Response.json](./attachments/Response.json)
