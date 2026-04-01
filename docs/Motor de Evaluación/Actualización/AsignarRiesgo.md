# Asignar Riesgo

> **Fuente Confluence:** [Asignar Riesgo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2879258769/Asignar+Riesgo)
> **Última modificación:** 2022-09-05 — Edwin Didier Méndez Rojas - Ceiba Software · versión 14
> **Sección:** [Actualización](./index.md)

## Archivos adjuntos

| Archivo | Enlace |
|---------|--------|
| `Json-Query-Response.json` | [Json-Query-Response.json](./attachments/Json-Query-Response.json) |
| `Json-Query-Request.json` | [Json-Query-Request.json](./attachments/Json-Query-Request.json) |
| `image-20220829-162646.png` | [image-20220829-162646.png](./attachments/image-20220829-162646.png) |
| `image-20220829-161741.png` | [image-20220829-161741.png](./attachments/image-20220829-161741.png) |
| `image-20220829-161614.png` | [image-20220829-161614.png](./attachments/image-20220829-161614.png) |
| `image-20220828-154511.png` | [image-20220828-154511.png](./attachments/image-20220828-154511.png) |
| `image-20220828-154418.png` | [image-20220828-154418.png](./attachments/image-20220828-154418.png) |
| `image-20220828-154253.png` | [image-20220828-154253.png](./attachments/image-20220828-154253.png) |

- **Objetivo:**  Proveer una conexión al motor de riesgo para el proceso de actualización de los Sarlaft de una Evaluación.

- **Query:** Evaluacion.sarlaft.actualizacion.riesgo

> **Nota:** los ejemplos a continuación se hicieron desde un proyecto sender que se comunicaba en la cola de service bus.El objeto de entrada es el mismo objeto de salida al proceso del motor.No se requiere enviar evidencias, pero se retorna la evidencia de gafi.

| Json Query Request/Response | Data Query Request | Tipo | Observaciones/Valores |
| --- | --- | --- | --- |
| {     "id": "evaluacion-id",     "codigoOperacion": "01",     "sarlafts": [         {             "id": "sarlaft-id",             "riesgoOriginal": {                 "id": "id-riesgo-original",                 "condicion": "HU-condicion",                 "tipoRiesgo": "SIMPLIFICADO",                 "mensaje": "mensaje-condicion",                 "causales": []             },             "riesgoActualizado": {                 "id": null,                 "condicion": null,                 "tipoRiesgo": null,                 "mensaje": null,                 "causales": []             },             "cliente": {                 "peps": true,                 "tipoPersona": "N",                 "paisConstitucion": "0",                 "persona": {                     "pais": "0"                 },                 "segmentacion": {                     "score": 1.0                 },                 "relaciones": [                     {                         "tipo": "ACCIONISTA",                         "relacionPeps": true,                         "fechaBaja": null                     }                 ]             },             "administradorPep": false,             "reglasConsecutivas": [                 {                     "id": null,                     "condicion": "HU 83304 16",                     "tipoRiesgo": "SIMPLIFICADO",                     "mensaje": "Cumple con po.",                     "causales": [                       "Cliente es..."                     ]                 }             ],             "evidencias": [                 {                     "consecutivo": "f0a6c182-aef9-45d2-b551-98a497cd2617",                     "consecutivoControl": null,                     "dni": "9292022",                     "resultado": "EXITOSO",                     "tipo": "GAFI",                     "observaciones": "No es Gafi",                     "fechaCreacion": "2022-08-29T16:38:30.589+00:00",                     "ultimaActualizacion": "2022-08-29T16:38:30.589+00:00",                     "codigoAplicacion": "9995",                     "bloqueante": false,                     "codigoEstadoDocumento": null                 }             ]         }     ],     "error": null } | codigoOperacion | String | Ejemplos:01 → Negocio NuevoRE → Reclamación |
| sarlafts[n].riesgoOriginal | Object | El Objecto riesgoOriginal, riesgo de entrada al proceso de actualización  | |
| sarlafts[n].riesgoOriginal.condicion | String | Nombre de la condición cumplida en el motor de decisión  | |
| sarlafts[n].riesgoOriginal.tipoRiesgo | String | INTENSIFICADOSIMPLIFICADOORDINARIO  | |
| sarlafts[n].riesgoOriginal.mensaje | String | Mensaje relacionado a la condición cumplida  | |
| sarlafts[n].riesgoOriginal.causales | ">List | lista de causas asignadas por la condición  | |
| sarlafts[n].riesgoActualizado | Object | El Objecto riesgoActualizado, es riesgo tipificado de salida al proceso de actualización  | |
| sarlafts[n].cliente.peps | boolean | Persona Expuesta Políticamente  | |
| sarlafts[n].cliente.tipoPersona | String | N → Persona NaturaJ → Persona Juridica  | |
| sarlafts[n].cliente.paisConstitucion | String | Codigo de pais, campo para persona juridica  | |
| sarlafts[n].cliente.segmentacion.score | Double | Puntaje para la valoración del riesgo  | |
| sarlafts[n].cliente.relaciones[n].tipo | String | Ejemplo:FAMILIA, SOCIO, ACCIONISTA, CONYUGE  | |
| sarlafts[n].cliente.relaciones[n].relacionPeps | boolean |   | |
| sarlafts[n].cliente.relaciones[n].fechaBaja | Date |   | |
| sarlafts[n].administradorPep | boolean | Persona Expuesta Políticamente  | |
| sarlafts[n].reglasConsecutivas[ ] | List | lista de reglas consecutivas que puede cumplir el sarlaft posterior a la del "riesgoActualizacion"  | |
| error | String | si retorna un mensaje diferente a null nos indica que occurrio un error en el proceso de ejecutar las validaciones, o algun campo requerido no se envio  | |

| Request | Response |
| --- | --- |
|  |  |
|  |  |
