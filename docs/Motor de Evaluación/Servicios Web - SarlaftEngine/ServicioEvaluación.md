# Servicio Evaluación

> **Fuente Confluence:** [Servicio Evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3360751716/Servicio+Evaluaci+n)
> **Última modificación:** 2023-10-06 — Diana Muñoz · versión 1
> **Sección:** [Servicios Web - SarlaftEngine](./index.md)

- **Objetivo:**Permite realizar la identificación de riesgo, validaciones y formulario para una evaluación en el aplicativo de sarlaft 4.0. Este servicio se expone en reemplazo de la comunicación request reply que se tenia por medio del service bus, donde se integran las funcionalidades de los siguientes querys:  "Evaluacion.sarlaft.riesgo", "Evaluacion.sarlaft.validaciones", "Evaluacion.sarlaft.formulario.requisitos".

- **Endpoint:** /sarlaftengineserv/api/evaluacion

- **Perfil de Seus4:**NO aplica. Este servicio se expone interno al cluster del aks, por lo tanto se convierte en una comunicación back to back.

- **Ejemplo Json Request:**

```text
{
    "evaluacion": {
        "id": "d87f4a19-8fd6-4309-8d87-1142947e48f5",
        "solicitudDni": "A8090086587",
        "codigoAplicacion": "118",
        "codigoOperacion": "01",
        "negocioId": "4545454",
        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
        "estado": "PENDIENTE",
        "infoPendiente": false,
        "cargaMasiva": false,
        "polizas": [
            {
                "id": "1ea9a0b8-e6d2-4e5f-99e4-4a7098f84d59",
                "valorPrima": 0.0,
                "codigoCanal": "CC013",
                "codigoRamo": "040",
                "codigoProducto": "A80",
                "negocio": "COLECTIVO",
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "codigoOficina": "4029",
                "codigoAgente": "56066",
                "cargaMasiva": false
            }
        ],
        "sarlafts": [
            {
                "id": "d0c58e02-7065-43b8-acc9-3c76f5e6c46b",
                "figuras": [
                    {
                        "id": "4de94ff9-00c2-4ba7-8d08-7ca0739facc4",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364142",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364142",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364142"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "e05b3706-f8d3-4bc5-bd6c-d796197e6e2c",
                "figuras": [
                    {
                        "id": "27297583-7498-48ce-955a-3a10c25f3ed2",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364143",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364143",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364143"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "d235ef0f-974c-4b87-b572-de19cbfbc12a",
                "figuras": [
                    {
                        "id": "f81b7e14-d029-4b8e-9725-194cf3b22cae",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364144",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364144",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364144"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "83897be7-7977-431f-8a11-ca1e59522557",
                "figuras": [
                    {
                        "id": "714f6a40-5f73-4c50-98c5-a7549fdf0d81",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364145",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364145",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364145"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "dfb7db18-4989-4013-ac7a-188aa46a9950",
                "figuras": [
                    {
                        "id": "0f171d5b-5639-4f86-8c5a-c9c85b45d56b",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364146",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364146",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364146"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "da963006-5ce0-49d6-9367-1586a499c16d",
                "figuras": [
                    {
                        "id": "4306820a-0cd2-4b7f-941e-bb4def1ae905",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "BENEFICIARIO"
                    },
                    {
                        "id": "006337b4-cca7-437e-9cdf-44924751ba0d",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364149",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364149",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364149"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "9b655439-d8c1-47ae-a777-8c3128d1d163",
                "figuras": [
                    {
                        "id": "bb77b5c7-1e06-436e-a1d6-035afe283be0",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364147",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364147",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364147"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "be49c003-e5a9-441d-8b02-1785ddfe2867",
                "figuras": [
                    {
                        "id": "0b6a8cbc-d4fa-42ad-b4fd-4c41b9ca8f76",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364148",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364148",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364148"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "cb8809bb-6e75-43a9-b0eb-648ada13f0ba",
                "figuras": [
                    {
                        "id": "e7f69072-8182-4168-9965-1b6c8d104524",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364150",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364150",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "segmentacion": {
                        "dniCliente": "C10364150"
                    }
                },
                "indicadorPeps": false
            },
            {
                "id": "4311d440-0bfa-40c4-b2d0-bd98b080f94d",
                "figuras": [
                    {
                        "id": "2924a094-38e9-4a6c-8f93-d3b3fcb40dad",
                        "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                        "dsfigura": "TOMADOR"
                    }
                ],
                "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364163",
                    "tipoPersona": "N",
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364163",
                        "fechaExpedicion": "Dec 8, 2004 7:00:00 PM"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "relaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "Sep 22, 2023 9:01:50 AM",
                    "ultimaActualizacion": "Sep 22, 2023 9:01:50 AM",
                    "peps": false,
                    "segmentacion": {
                        "dniCliente": "C10364163"
                    }
                },
                "indicadorPeps": false,
                "evidencias": [
                    {
                        "consecutivo": "d5fced2c-ffa6-44a3-bf0d-fedda8759afc",
                        "dni": "C10364163",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "Sep 22, 2023 9:01:52 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:52 AM",
                        "codigoAplicacion": "0",
                        "bloqueante": true
                    },
                    {
                        "consecutivo": "4b0c6f68-565e-4465-a287-8d3c446d2995",
                        "dni": "C10364163",
                        "resultado": "EXITOSO",
                        "tipo": "PEPS",
                        "observaciones": "",
                        "fechaCreacion": "Sep 22, 2023 9:01:52 AM",
                        "ultimaActualizacion": "Sep 22, 2023 9:01:52 AM",
                        "codigoAplicacion": "0",
                        "bloqueante": true
                    }
                ]
            }
        ]
    }
}
```

Response:

```text
{
    "id": "d87f4a19-8fd6-4309-8d87-1142947e48f5",
    "solicitudDni": "A8090086587",
    "codigoAplicacion": "118",
    "codigoOperacion": "01",
    "respuestaBeneficiario": false,
    "negocioId": "4545454",
    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
    "estado": "PENDIENTE",
    "relacionLaboral": null,
    "infoPendiente": false,
    "token": null,
    "urlComponenteWeb": null,
    "tipoFormulario": null,
    "polizas": [
        {
            "id": "1ea9a0b8-e6d2-4e5f-99e4-4a7098f84d59",
            "valorAsegurado": null,
            "valorPrima": 0.0,
            "medioRecaudo": null,
            "codigoCanal": "CC013",
            "codigoRamo": "040",
            "codigoProducto": "A80",
            "negocio": "COLECTIVO",
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "tipoCoaseguro": null,
            "codigoOficina": "4029",
            "codigoAgente": "56066",
            "licitacionPublica": false,
            "codigoPlan": null,
            "indProcesoJudicial": null,
            "juzgado": null,
            "ciudadProcesoJudicial": null
        }
    ],
    "sarlafts": [
        {
            "id": "d0c58e02-7065-43b8-acc9-3c76f5e6c46b",
            "figuras": [
                {
                    "id": "4de94ff9-00c2-4ba7-8d08-7ca0739facc4",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "BENEFICIARIO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364142",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364142",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364142",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 2"
                ],
                "lastFlowlog": "Condición bajo HU 156478 2",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "8e742eac-9fbd-44b0-af33-217ee7f83cb0",
                    "consecutivoControl": null,
                    "dni": "C10364142",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 2"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 2"
        },
        {
            "id": "e05b3706-f8d3-4bc5-bd6c-d796197e6e2c",
            "figuras": [
                {
                    "id": "27297583-7498-48ce-955a-3a10c25f3ed2",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "BENEFICIARIO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364143",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364143",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364143",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 2"
                ],
                "lastFlowlog": "Condición bajo HU 156478 2",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "0966545b-44a8-48a5-af98-e1a8def0046e",
                    "consecutivoControl": null,
                    "dni": "C10364143",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 2"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 2"
        },
        {
            "id": "d235ef0f-974c-4b87-b572-de19cbfbc12a",
            "figuras": [
                {
                    "id": "f81b7e14-d029-4b8e-9725-194cf3b22cae",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "BENEFICIARIO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364144",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364144",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364144",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 2"
                ],
                "lastFlowlog": "Condición bajo HU 156478 2",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "c98f75fa-9f07-47f7-8b49-cef715e8d09d",
                    "consecutivoControl": null,
                    "dni": "C10364144",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 2"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 2"
        },
        {
            "id": "83897be7-7977-431f-8a11-ca1e59522557",
            "figuras": [
                {
                    "id": "714f6a40-5f73-4c50-98c5-a7549fdf0d81",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "BENEFICIARIO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364145",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364145",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364145",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 2"
                ],
                "lastFlowlog": "Condición bajo HU 156478 2",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "0e4b3d31-e63b-4f76-8443-86762c96b557",
                    "consecutivoControl": null,
                    "dni": "C10364145",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 2"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 2"
        },
        {
            "id": "dfb7db18-4989-4013-ac7a-188aa46a9950",
            "figuras": [
                {
                    "id": "0f171d5b-5639-4f86-8c5a-c9c85b45d56b",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "BENEFICIARIO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364146",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364146",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364146",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 2"
                ],
                "lastFlowlog": "Condición bajo HU 156478 2",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "dc829e03-5b5c-4352-938f-19d9f13b5a5d",
                    "consecutivoControl": null,
                    "dni": "C10364146",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 2"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 2"
        },
        {
            "id": "da963006-5ce0-49d6-9367-1586a499c16d",
            "figuras": [
                {
                    "id": "4306820a-0cd2-4b7f-941e-bb4def1ae905",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "BENEFICIARIO"
                },
                {
                    "id": "006337b4-cca7-437e-9cdf-44924751ba0d",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "ASEGURADO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364149",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364149",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364149",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 1"
                ],
                "lastFlowlog": "Condición bajo HU 156478 1",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "374bae3a-9071-4959-bce4-8bfd83470006",
                    "consecutivoControl": null,
                    "dni": "C10364149",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 1"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 1"
        },
        {
            "id": "9b655439-d8c1-47ae-a777-8c3128d1d163",
            "figuras": [
                {
                    "id": "bb77b5c7-1e06-436e-a1d6-035afe283be0",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "ASEGURADO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364147",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364147",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364147",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 1"
                ],
                "lastFlowlog": "Condición bajo HU 156478 1",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "ef9cbf87-303d-43c2-8858-7fcc7cb33d15",
                    "consecutivoControl": null,
                    "dni": "C10364147",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 1"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 1"
        },
        {
            "id": "be49c003-e5a9-441d-8b02-1785ddfe2867",
            "figuras": [
                {
                    "id": "0b6a8cbc-d4fa-42ad-b4fd-4c41b9ca8f76",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "ASEGURADO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364148",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364148",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364148",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 1"
                ],
                "lastFlowlog": "Condición bajo HU 156478 1",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "bb6f7ca9-fe4d-4358-8aac-6a68522aa9f5",
                    "consecutivoControl": null,
                    "dni": "C10364148",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 1"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 1"
        },
        {
            "id": "cb8809bb-6e75-43a9-b0eb-648ada13f0ba",
            "figuras": [
                {
                    "id": "e7f69072-8182-4168-9965-1b6c8d104524",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "ASEGURADO"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364150",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364150",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": "ANDRES",
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364150",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "SIMPLIFICADO",
                "causales": [
                    "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición bajo HU 156478 1"
                ],
                "lastFlowlog": "Condición bajo HU 156478 1",
                "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
            },
            "terminoFormulario": null,
            "tipoFormulario": "NO_APLICA",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": true,
            "evidencias": [
                {
                    "consecutivo": "3375a27c-87c3-4cac-8f04-f30b374bdab5",
                    "consecutivoControl": null,
                    "dni": "C10364150",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                    "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                    "codigoAplicacion": "9995",
                    "bloqueante": false,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condicion tipo formulario HU 156478 1"
            ],
            "banderas": [
                "GAFI"
            ],
            "lastFlowlog": "Condicion tipo formulario HU 156478 1"
        },
        {
            "id": "4311d440-0bfa-40c4-b2d0-bd98b080f94d",
            "figuras": [
                {
                    "id": "2924a094-38e9-4a6c-8f93-d3b3fcb40dad",
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "dsfigura": "TOMADOR"
                }
            ],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "estado": "PENDIENTE",
            "cliente": {
                "dni": "C10364163",
                "tipoPersona": "N",
                "tipoAsociacion": null,
                "razonSocial": null,
                "paisConstitucion": null,
                "infoContacto": {
                    "celular": "3006138524",
                    "correo": "DD@GMAIL.COM"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "10364163",
                    "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                },
                "persona": {
                    "primerNombre": "DIEGO",
                    "segundoNombre": null,
                    "primerApellido": "BAHAMON FREIDA",
                    "segundoApellido": "CHICA",
                    "pais": "57"
                },
                "infoFinanciera": null,
                "relaciones": [],
                "asociaciones": [],
                "direcciones": [],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "fechaCreacionAsociacion": null,
                "fechaBajaAsociacion": null,
                "peps": false,
                "porParticipacionSocio": null,
                "segmentacion": {
                    "dniCliente": "C10364163",
                    "score": null
                },
                "paisSegunTipoPersona": "57"
            },
            "riesgo": {
                "id": null,
                "tipoRiesgo": "ORDINARIO",
                "causales": [
                    "Regla por defecto en riesgo ordinario"
                ],
                "bloqueante": false,
                "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                "indicadorRegimenPublico": false,
                "fechaCreacion": null,
                "ultimaActualizacion": null,
                "monitoreo": false,
                "flowlog": [
                    "inicializacion",
                    "Condición Medio 1"
                ],
                "lastFlowlog": "Condición Medio 1",
                "ultimaCausa": "Regla por defecto en riesgo ordinario"
            },
            "terminoFormulario": null,
            "tipoFormulario": "ORDINARIO_PN",
            "cuentaConInformacion": null,
            "indicadorPeps": false,
            "personaPep": null,
            "administradorPep": null,
            "heredarRiesgo": false,
            "ignorarHerencias": false,
            "evidencias": [
                {
                    "consecutivo": "d5fced2c-ffa6-44a3-bf0d-fedda8759afc",
                    "consecutivoControl": null,
                    "dni": "C10364163",
                    "resultado": "EXITOSO",
                    "tipo": "GAFI",
                    "observaciones": "No es Gafi",
                    "fechaCreacion": "2023-09-22T14:01:52.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:52.000+00:00",
                    "codigoAplicacion": "0",
                    "bloqueante": true,
                    "codigoEstadoDocumento": null
                },
                {
                    "consecutivo": "4b0c6f68-565e-4465-a287-8d3c446d2995",
                    "consecutivoControl": null,
                    "dni": "C10364163",
                    "resultado": "EXITOSO",
                    "tipo": "PEPS",
                    "observaciones": "",
                    "fechaCreacion": "2023-09-22T14:01:52.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:52.000+00:00",
                    "codigoAplicacion": "0",
                    "bloqueante": true,
                    "codigoEstadoDocumento": null
                }
            ],
            "requisitos": [],
            "flowlog": [
                "inicializacion",
                "Condición Formulario 13"
            ],
            "banderas": [],
            "lastFlowlog": "Condición Formulario 13"
        }
    ],
    "figurasDto": [
        {
            "sarlaft": {
                "id": "d0c58e02-7065-43b8-acc9-3c76f5e6c46b",
                "figuras": [
                    {
                        "id": "4de94ff9-00c2-4ba7-8d08-7ca0739facc4",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364142",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364142",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364142",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 2"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 2",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "8e742eac-9fbd-44b0-af33-217ee7f83cb0",
                        "consecutivoControl": null,
                        "dni": "C10364142",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 2"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 2"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 15"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 15"
        },
        {
            "sarlaft": {
                "id": "e05b3706-f8d3-4bc5-bd6c-d796197e6e2c",
                "figuras": [
                    {
                        "id": "27297583-7498-48ce-955a-3a10c25f3ed2",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364143",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364143",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364143",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 2"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 2",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "0966545b-44a8-48a5-af98-e1a8def0046e",
                        "consecutivoControl": null,
                        "dni": "C10364143",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 2"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 2"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 15"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 15"
        },
        {
            "sarlaft": {
                "id": "d235ef0f-974c-4b87-b572-de19cbfbc12a",
                "figuras": [
                    {
                        "id": "f81b7e14-d029-4b8e-9725-194cf3b22cae",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364144",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364144",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364144",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 2"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 2",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "c98f75fa-9f07-47f7-8b49-cef715e8d09d",
                        "consecutivoControl": null,
                        "dni": "C10364144",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 2"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 2"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 15"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 15"
        },
        {
            "sarlaft": {
                "id": "83897be7-7977-431f-8a11-ca1e59522557",
                "figuras": [
                    {
                        "id": "714f6a40-5f73-4c50-98c5-a7549fdf0d81",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364145",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364145",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364145",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 2"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 2",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "0e4b3d31-e63b-4f76-8443-86762c96b557",
                        "consecutivoControl": null,
                        "dni": "C10364145",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 2"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 2"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 15"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 15"
        },
        {
            "sarlaft": {
                "id": "dfb7db18-4989-4013-ac7a-188aa46a9950",
                "figuras": [
                    {
                        "id": "0f171d5b-5639-4f86-8c5a-c9c85b45d56b",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "BENEFICIARIO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364146",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364146",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364146",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 2"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 2",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - Beneficiario no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "dc829e03-5b5c-4352-938f-19d9f13b5a5d",
                        "consecutivoControl": null,
                        "dni": "C10364146",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 2"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 2"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 15"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 15"
        },
        {
            "sarlaft": {
                "id": "da963006-5ce0-49d6-9367-1586a499c16d",
                "figuras": [
                    {
                        "id": "4306820a-0cd2-4b7f-941e-bb4def1ae905",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "BENEFICIARIO"
                    },
                    {
                        "id": "006337b4-cca7-437e-9cdf-44924751ba0d",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364149",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364149",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364149",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 1"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 1",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "374bae3a-9071-4959-bce4-8bfd83470006",
                        "consecutivoControl": null,
                        "dni": "C10364149",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 1"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 1"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 8"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 8"
        },
        {
            "sarlaft": {
                "id": "9b655439-d8c1-47ae-a777-8c3128d1d163",
                "figuras": [
                    {
                        "id": "bb77b5c7-1e06-436e-a1d6-035afe283be0",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364147",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364147",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364147",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 1"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 1",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "ef9cbf87-303d-43c2-8858-7fcc7cb33d15",
                        "consecutivoControl": null,
                        "dni": "C10364147",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 1"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 1"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 8"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 8"
        },
        {
            "sarlaft": {
                "id": "be49c003-e5a9-441d-8b02-1785ddfe2867",
                "figuras": [
                    {
                        "id": "0b6a8cbc-d4fa-42ad-b4fd-4c41b9ca8f76",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364148",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364148",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364148",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 1"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 1",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "bb6f7ca9-fe4d-4358-8aac-6a68522aa9f5",
                        "consecutivoControl": null,
                        "dni": "C10364148",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 1"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 1"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 8"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 8"
        },
        {
            "sarlaft": {
                "id": "cb8809bb-6e75-43a9-b0eb-648ada13f0ba",
                "figuras": [
                    {
                        "id": "e7f69072-8182-4168-9965-1b6c8d104524",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "ASEGURADO"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364150",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364150",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": "ANDRES",
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364150",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "SIMPLIFICADO",
                    "causales": [
                        "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición bajo HU 156478 1"
                    ],
                    "lastFlowlog": "Condición bajo HU 156478 1",
                    "ultimaCausa": "Regla simplificado: producto AUTOS COLECTIVO - asegurado no aplica ordinario por flexibilización de la junta"
                },
                "terminoFormulario": null,
                "tipoFormulario": "NO_APLICA",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": true,
                "evidencias": [
                    {
                        "consecutivo": "3375a27c-87c3-4cac-8f04-f30b374bdab5",
                        "consecutivoControl": null,
                        "dni": "C10364150",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-10-06T12:46:44.018+00:00",
                        "ultimaActualizacion": "2023-10-06T12:46:44.018+00:00",
                        "codigoAplicacion": "9995",
                        "bloqueante": false,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condicion tipo formulario HU 156478 1"
                ],
                "banderas": [
                    "GAFI"
                ],
                "lastFlowlog": "Condicion tipo formulario HU 156478 1"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 8"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 8"
        },
        {
            "sarlaft": {
                "id": "4311d440-0bfa-40c4-b2d0-bd98b080f94d",
                "figuras": [
                    {
                        "id": "2924a094-38e9-4a6c-8f93-d3b3fcb40dad",
                        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                        "dsfigura": "TOMADOR"
                    }
                ],
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "estado": "PENDIENTE",
                "cliente": {
                    "dni": "C10364163",
                    "tipoPersona": "N",
                    "tipoAsociacion": null,
                    "razonSocial": null,
                    "paisConstitucion": null,
                    "infoContacto": {
                        "celular": "3006138524",
                        "correo": "DD@GMAIL.COM"
                    },
                    "documento": {
                        "tipo": "C",
                        "numero": "10364163",
                        "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
                    },
                    "persona": {
                        "primerNombre": "DIEGO",
                        "segundoNombre": null,
                        "primerApellido": "BAHAMON FREIDA",
                        "segundoApellido": "CHICA",
                        "pais": "57"
                    },
                    "infoFinanciera": null,
                    "relaciones": [],
                    "asociaciones": [],
                    "direcciones": [],
                    "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                    "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                    "fechaCreacionAsociacion": null,
                    "fechaBajaAsociacion": null,
                    "peps": false,
                    "porParticipacionSocio": null,
                    "segmentacion": {
                        "dniCliente": "C10364163",
                        "score": null
                    },
                    "paisSegunTipoPersona": "57"
                },
                "riesgo": {
                    "id": null,
                    "tipoRiesgo": "ORDINARIO",
                    "causales": [
                        "Regla por defecto en riesgo ordinario"
                    ],
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
                    "indicadorRegimenPublico": false,
                    "fechaCreacion": null,
                    "ultimaActualizacion": null,
                    "monitoreo": false,
                    "flowlog": [
                        "inicializacion",
                        "Condición Medio 1"
                    ],
                    "lastFlowlog": "Condición Medio 1",
                    "ultimaCausa": "Regla por defecto en riesgo ordinario"
                },
                "terminoFormulario": null,
                "tipoFormulario": "ORDINARIO_PN",
                "cuentaConInformacion": null,
                "indicadorPeps": false,
                "personaPep": null,
                "administradorPep": null,
                "heredarRiesgo": false,
                "ignorarHerencias": false,
                "evidencias": [
                    {
                        "consecutivo": "d5fced2c-ffa6-44a3-bf0d-fedda8759afc",
                        "consecutivoControl": null,
                        "dni": "C10364163",
                        "resultado": "EXITOSO",
                        "tipo": "GAFI",
                        "observaciones": "No es Gafi",
                        "fechaCreacion": "2023-09-22T14:01:52.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:52.000+00:00",
                        "codigoAplicacion": "0",
                        "bloqueante": true,
                        "codigoEstadoDocumento": null
                    },
                    {
                        "consecutivo": "4b0c6f68-565e-4465-a287-8d3c446d2995",
                        "consecutivoControl": null,
                        "dni": "C10364163",
                        "resultado": "EXITOSO",
                        "tipo": "PEPS",
                        "observaciones": "",
                        "fechaCreacion": "2023-09-22T14:01:52.000+00:00",
                        "ultimaActualizacion": "2023-09-22T14:01:52.000+00:00",
                        "codigoAplicacion": "0",
                        "bloqueante": true,
                        "codigoEstadoDocumento": null
                    }
                ],
                "requisitos": [],
                "flowlog": [
                    "inicializacion",
                    "Condición Formulario 13"
                ],
                "banderas": [],
                "lastFlowlog": "Condición Formulario 13"
            },
            "validaciones": [
                {
                    "codigo": "RRCC",
                    "bloqueante": true
                },
                {
                    "codigo": "DOCUMENT_PN",
                    "bloqueante": true
                },
                {
                    "codigo": "IDENTITY",
                    "bloqueante": true
                }
            ],
            "heredarValidaciones": false,
            "flowlog": [
                "inicializacion",
                "Condición Validación 3"
            ],
            "aplicaDocumentPn": false,
            "aplicaIdentity": false,
            "lastFlowlog": "Condición Validación 3"
        }
    ],
    "cargaMasiva": false,
    "error": null,
    "tomador": {
        "id": "4311d440-0bfa-40c4-b2d0-bd98b080f94d",
        "figuras": [
            {
                "id": "2924a094-38e9-4a6c-8f93-d3b3fcb40dad",
                "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
                "dsfigura": "TOMADOR"
            }
        ],
        "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
        "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
        "estado": "PENDIENTE",
        "cliente": {
            "dni": "C10364163",
            "tipoPersona": "N",
            "tipoAsociacion": null,
            "razonSocial": null,
            "paisConstitucion": null,
            "infoContacto": {
                "celular": "3006138524",
                "correo": "DD@GMAIL.COM"
            },
            "documento": {
                "tipo": "C",
                "numero": "10364163",
                "fechaExpedicion": "2004-12-08T12:00:00.000+00:00"
            },
            "persona": {
                "primerNombre": "DIEGO",
                "segundoNombre": null,
                "primerApellido": "BAHAMON FREIDA",
                "segundoApellido": "CHICA",
                "pais": "57"
            },
            "infoFinanciera": null,
            "relaciones": [],
            "asociaciones": [],
            "direcciones": [],
            "fechaCreacion": "2023-09-22T14:01:50.000+00:00",
            "ultimaActualizacion": "2023-09-22T14:01:50.000+00:00",
            "fechaCreacionAsociacion": null,
            "fechaBajaAsociacion": null,
            "peps": false,
            "porParticipacionSocio": null,
            "segmentacion": {
                "dniCliente": "C10364163",
                "score": null
            },
            "paisSegunTipoPersona": "57"
        },
        "riesgo": {
            "id": null,
            "tipoRiesgo": "ORDINARIO",
            "causales": [
                "Regla por defecto en riesgo ordinario"
            ],
            "bloqueante": false,
            "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica.",
            "indicadorRegimenPublico": false,
            "fechaCreacion": null,
            "ultimaActualizacion": null,
            "monitoreo": false,
            "flowlog": [
                "inicializacion",
                "Condición Medio 1"
            ],
            "lastFlowlog": "Condición Medio 1",
            "ultimaCausa": "Regla por defecto en riesgo ordinario"
        },
        "terminoFormulario": null,
        "tipoFormulario": "ORDINARIO_PN",
        "cuentaConInformacion": null,
        "indicadorPeps": false,
        "personaPep": null,
        "administradorPep": null,
        "heredarRiesgo": false,
        "ignorarHerencias": false,
        "evidencias": [
            {
                "consecutivo": "d5fced2c-ffa6-44a3-bf0d-fedda8759afc",
                "consecutivoControl": null,
                "dni": "C10364163",
                "resultado": "EXITOSO",
                "tipo": "GAFI",
                "observaciones": "No es Gafi",
                "fechaCreacion": "2023-09-22T14:01:52.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:52.000+00:00",
                "codigoAplicacion": "0",
                "bloqueante": true,
                "codigoEstadoDocumento": null
            },
            {
                "consecutivo": "4b0c6f68-565e-4465-a287-8d3c446d2995",
                "consecutivoControl": null,
                "dni": "C10364163",
                "resultado": "EXITOSO",
                "tipo": "PEPS",
                "observaciones": "",
                "fechaCreacion": "2023-09-22T14:01:52.000+00:00",
                "ultimaActualizacion": "2023-09-22T14:01:52.000+00:00",
                "codigoAplicacion": "0",
                "bloqueante": true,
                "codigoEstadoDocumento": null
            }
        ],
        "requisitos": [],
        "flowlog": [
            "inicializacion",
            "Condición Formulario 13"
        ],
        "banderas": [],
        "lastFlowlog": "Condición Formulario 13"
    }
}
```

**Dependencias**:

- NA
