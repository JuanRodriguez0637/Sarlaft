# Asignar Riesgo, Evidencias  requisitos Web Service

> **Fuente Confluence:** [Asignar Riesgo, Evidencias  requisitos Web Service](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4010672206/Asignar+Riesgo+Evidencias+requisitos+Web+Service)
> **Última modificación:** 2024-09-04 — Mauricio Marin Martinez · versión 3
> **Sección:** [Actualización](./index.md)

- **Objetivo:** Proveer una conexión al motor de riesgo para el proceso de actualización de los Sarlaft de una Evaluación por medio de un servicio web el cual realiza la asignación del riesgo, las validaciones y la asignación de Formulario/Requisitos desde un solo llamado.
- **Path:** `api/actualizacion/evaluacion`

> **ℹ️ Info:**
> - **Nota:** El ejemplo a a continuación tiene el json del request que contiene la informacion necesaria a ser evaluada.

## Json Request

```json
{
    "id": "0da5a475-144d-49b8-9f3a-f5ee8861ae7b",
    "codigoOperacion": "AC",
    "sarlafts": [
        {
            "riesgoOriginal": {
                "id": "Carga-Sarlaft-HU-83304-1",
                "tipoRiesgo": "SIMPLIFICADO"
            },
            "cliente": {
                "dni": "A1234567990",
                "peps": true,
                "tipoPersona": "J",
                "paisConstitucion": "57",
                "documento": {
                    "tipo": "A"
                },
                "persona": {
                    "pais": "0"
                },
                "segmentacion": {
                    "score": 1.0
                },
                "relaciones": [
                    {
                        "tipo": "ACCIONISTA",
                        "relacionPeps": true,
                        "fechaBaja": null
                    }
                ]
            },
            "administradorPep": false
        }
    ]
}
```

### Campos del Request

| Data Query Request | Tipo | Observaciones/Valores |
| --- | --- | --- |
| `id` | String | Id de la evaluacion |
| `codigoOperacion` | String | Ejemplos: `01` → Negocio Nuevo, `RE` → Reclamación, `AC` → Actualizacion |
| `sarlafts[n].id` | String | Identificador del sarlaft |
| `sarlafts[n].riesgoOriginal` | Object | El Objecto riesgoOriginal, riesgo de entrada al proceso de actualización |
| `sarlafts[n].riesgoOriginal.tipoRiesgo` | String | `INTENSIFICADO`, `SIMPLIFICADO`, `ORDINARIO` |
| `sarlafts[n].cliente` | Object | Objeto con la informacion del cliente |
| `sarlafts[n].cliente.dni` | String | Dni del cliente |
| `sarlafts[n].cliente.peps` | boolean | Persona Expuesta Políticamente |
| `sarlafts[n].cliente.tipoPersona` | String | `N` → Persona Natural, `J` → Persona Juridica |
| `sarlafts[n].cliente.paisConstitucion` | String | Codigo de pais, campo para persona juridica |
| `sarlafts[n].cliente.persona.pais` | String | Codigo de pais, campo para persona juridica |
| `sarlafts[n].cliente.documento.tipo` | String | Tipo de documento |
| `sarlafts[n].cliente.segmentacion.score` | Double | Puntaje para la valoración del riesgo |
| `sarlafts[n].cliente.relaciones[n].tipo` | String | Ejemplo: `FAMILIA`, `SOCIO`, `ACCIONISTA`, `CONYUGE` |
| `sarlafts[n].cliente.relaciones[n].relacionPeps` | boolean | |
| `sarlafts[n].cliente.relaciones[n].fechaBaja` | Date | |
| `sarlafts[n].administradorPep` | boolean | Persona Expuesta Políticamente |

## Request y Response

### Request

```json
{
    "id": "0da5a475-144d-49b8-9f3a-f5ee8861ae7b",
    "codigoOperacion": "AC",
    "sarlafts": [
        {
            "riesgoOriginal": {
                "id": "Carga-Sarlaft-HU-83304-1",
                "tipoRiesgo": "SIMPLIFICADO"
            },
            "cliente": {
                "dni": "A1234567990",
                "peps": true,
                "tipoPersona": "J",
                "paisConstitucion": "57",
                "documento": {
                    "tipo": "A"
                },
                "persona": {
                    "pais": "0"
                },
                "segmentacion": {
                    "score": 1.0
                },
                "relaciones": [
                    {
                        "tipo": "ACCIONISTA",
                        "relacionPeps": true,
                        "fechaBaja": null
                    }
                ]
            },
            "administradorPep": false
        }
    ]
}
```

📎 [Json-Request.json](./attachments/Json-Request.json)

### Response

```json
{
    "riesgoResult": {
        "id": "0da5a475-144d-49b8-9f3a-f5ee8861ae7b",
        "codigoOperacion": "AC",
        "sarlafts": [
            {
                "id": null,
                "riesgoOriginal": {
                    "id": "Carga-Sarlaft-HU-83304-1",
                    "condicion": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "mensaje": null,
                    "bloqueante": false,
                    "causales": [],
                    "ultimaCausa": ""
                },
                "riesgoActualizado": {
                    "id": null,
                    "condicion": "HU 83304 1",
                    "tipoRiesgo": "INTENSIFICADO",
                    "mensaje": "El cliente es PEP (Persona Expuesta Políticamente), por favor tramite con su Líder",
                    "bloqueante": false,
                    "causales": [
                        "Cliente con riesgo simplificado y recategorizado como PEP por el proceso de actualización"
                    ],
                    "ultimaCausa": "Cliente con riesgo simplificado y recategorizado como PEP por el proceso de actualización"
                },
                "cliente": {
                    "dni": "A1234567990",
                    "peps": true,
                    "tipoPersona": "J",
                    "paisConstitucion": "57",
                    "documento": {
                        "tipo": "A"
                    },
                    "persona": {
                        "pais": "0"
                    },
                    "segmentacion": {
                        "score": 1.0
                    },
                    "relaciones": [
                        {
                            "tipo": "ACCIONISTA",
                            "relacionPeps": true,
                            "fechaBaja": null
                        }
                    ],
                    "paisSegunTipoPersona": "57"
                },
                "administradorPep": false,
                "dataTecnica": {
                    "test": null,
                    "descripcion": null,
                    "flowlog": [
                        "HU 83304 1",
                        "HU 83304 4",
                        "HU 83304 7",
                        "HU 83304 16"
                    ],
                    "banderas": [
                        "GAFI",
                        "GAFI"
                    ],
                    "lastFlowlog": "HU 83304 16"
                },
                "reglasConsecutivas": [
                    {
                        "id": null,
                        "condicion": "HU 83304 4",
                        "tipoRiesgo": "INTENSIFICADO",
                        "mensaje": "No es posible continuar con el proceso. Debe completar el Conocimiento del Cliente si le aplica.",
                        "bloqueante": false,
                        "causales": [
                            "Cliente con riesgo intensificado y recategorizado como PEP por el proceso de actualización"
                        ],
                        "ultimaCausa": "Cliente con riesgo intensificado y recategorizado como PEP por el proceso de actualización"
                    },
                    {
                        "id": null,
                        "condicion": "HU 83304 7",
                        "tipoRiesgo": "INTENSIFICADO",
                        "mensaje": "No es posible continuar con el proceso. Debe completar el Conocimiento del Cliente si le aplica.",
                        "bloqueante": false,
                        "causales": [
                            "Cliente con riesgo simplificado  y recategorizado por SCORE DE RIESGOS por el proceso de actualización"
                        ],
                        "ultimaCausa": "Cliente con riesgo simplificado  y recategorizado por SCORE DE RIESGOS por el proceso de actualización"
                    },
                    {
                        "id": null,
                        "condicion": "HU 83304 16",
                        "tipoRiesgo": "SIMPLIFICADO",
                        "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                        "bloqueante": false,
                        "causales": [
                            "Cliente con riesgo simplificado por el proceso de actualización"
                        ],
                        "ultimaCausa": "Cliente con riesgo simplificado por el proceso de actualización"
                    }
                ],
                "evidencias": [
                    {
                        "consecutivo": "1c961b66-d22f-408d-afe2-a4fed071b63d",
                        "consecutivoControl": null,
                        "dni": "A1234567990",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2024-09-04T21:01:30.397+00:00",
                        "ultimaActualizacion": "2024-09-04T21:01:30.397+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ]
            }
        ],
        "error": null
    },
    "validacionesResult": {
        "validacionesDTO": [
            {
                "sarlaft": {
                    "id": null,
                    "tipoPersona": "J",
                    "tipoRiesgo": "INTENSIFICADO",
                    "cliente": {
                        "documento": {
                            "tipo": "A"
                        }
                    }
                },
                "validaciones": [
                    {
                        "codigo": "RRCC",
                        "bloqueante": true
                    },
                    {
                        "codigo": "CLIENTE_ACTIVO",
                        "bloqueante": true
                    }
                ],
                "flowlog": [
                    "HU 83305 Validacion 6"
                ],
                "lastFlowlog": "HU 83305 Validacion 6"
            }
        ],
        "error": null,
        "evaluacionId": "0da5a475-144d-49b8-9f3a-f5ee8861ae7b"
    },
    "formularioResult": {
        "id": "0da5a475-144d-49b8-9f3a-f5ee8861ae7b",
        "sarlafts": [
            {
                "id": null,
                "tipoPersona": "J",
                "tipoRiesgo": "INTENSIFICADO",
                "tipoFormulario": "INTENSIFICADO_PJ",
                "requisitos": [
                    {
                        "id": null,
                        "codigo": "2303",
                        "nombre": "Certificado de Existencia y Representación Legal",
                        "fechaCreacion": null,
                        "ultimaActualizacion": null,
                        "estado": "PENDIENTE",
                        "vigencia": 30
                    },
                    {
                        "id": null,
                        "codigo": "2037",
                        "nombre": "Estados Financieros",
                        "fechaCreacion": null,
                        "ultimaActualizacion": null,
                        "estado": "PENDIENTE",
                        "vigencia": 0
                    }
                ],
                "flowlog": [
                    "Regla 6: tipo formulario intensificado PERSONA JURÍDICA"
                ]
            }
        ],
        "error": null
    }
}
```

📎 [Json-Response.json](./attachments/Json-Response.json)
