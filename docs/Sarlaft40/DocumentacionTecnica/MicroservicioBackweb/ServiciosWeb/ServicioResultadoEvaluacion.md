# Servicio Resultado Evaluación

> **Fuente Confluence:** [Servicio Resultado Evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2398191643)
> **Última modificación:** 2022-10-11 — Johnathan Monsalve Bello · versión 9
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite iniciar consultar los parámetros de la evaluación e información del sarlaft de cada figura según un id de evaluación. Se muestran los controles y mensajes de los asegurados, afiliados, beneficiarios, afianzados, representante legal y/o accionistas que tengan un estado pendiente, fallido o rechazado.
- **Endpoint:** `/sarlaftbackweb/resultevaluation`
- **Perfil de Seus4:** `PF_SARLAFTADMCON`
- **Ejemplo Json Request:**

```json
{
    "idEvaluacion": "8ac8063f-b4d8-43c9-8ce1-cca031fda67c"
}
```

- **Ejemplo Json Response:**
  - Para Assesment diferente a Reclamación

```json
{
    "reclamante": null,
    "evaluacion": {
        "idEvaluacion": "f5462a65-3ffd-4d0f-8eeb-e2015c2a9914",
        "estado": "RECHAZADO",
        "tipoOperacion": "Negocio nuevo",
        "tipoNegocio": "COLECTIVO",
        "ramo": "187",
        "producto": null,
        "cantidadAsegurados": 0,
        "medioPago": "No aplica",
        "tipoCoaseguro": "null",
        "valorAsegurado": 500000.0,
        "valorPrima": 500000.0,
        "canal": "1 - nombreCanal",
        "oficina": "00 - nombreOficina",
        "asesor": "00 - nombreAsesor",
        "fechaCreacion": "2022-04-27T20:37:17.572+00:00",
        "indProcesoJudicial": false,
        "juzgado": null,
        "ciudadProcesoJudicial": null,
        "sarlafts": [
            {
                "estado": "RECHAZADO",
                "roles": [
                    "BENEFICIARIO",
                    "TOMADOR"
                ],
                "tipoIdentificacion": "C",
                "numeroIdentificacion": "613570",
                "fechaExpedicionDocumento": "2007-05-27T00:00:00.000+00:00",
                "primerNombre": "ÑESTOR",
                "segundoNombre": "FERNANDO",
                "primerApellido": "PALACIO",
                "segundoApellido": "ESPITIA",
                "paisNacimiento": "COLOMBIA",
                "paisConstitucion": null,
                "rolReclamante": null,
                "correoElectronico": "MAIL_1@MAIL.COM.CO",
                "celular": "3102345670",
                "razonSocial": null,
                "soportesRequeridos": [],
                "indicadorRegimenPublico": false,
                "riesgoVo": {
                    "tipoRiesgo": "SIMPLIFICADO",
                    "bloqueante": false,
                    "causales": [
                        "Regla simplificado:  valor asegurado 135SMLV/primar 6SMLV para PN"
                    ],
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica."
                },
                "indicadorPeps": false,
                "indicadorGafi": false,
                "respuestaPEPS": "NO",
                "tipoFormulario": "SIMPLIFICADO_PN",
                "tipoPersona": "N",
                "terminoFormulario": true,
                "validacionIdentidad": "NOAPLICA",
                "listaControl": [
                    {
                        "mensajeControl": "No es posible continuar con el proceso. La validación del documento de identidad con Registraduría  Nacional no ha sido exitosa pues el documento no aparece vigente",
                        "control": "DOCUMENT_PN",
                        "estado": "FALLIDO"
                    }
                ],
                "riesgo": {
                    "pais": "COLOMBIA",
                    "indicadorPep": false,
                    "resultadoRegistraduria": "FALLIDO",
                    "resultadoListasVinculantes": "EXITOSO",
                    "resultadoControlPep": "No aplica",
                    "resultadoValidacionIdentidad": null,
                    "causalRegistraduria": "21-Cancelada por muerte o fallecido"
                },
                "tipoValidacionIdentidad": null,
                "cuentaConInformacion": true,
                "score": "NO"
            }
        ],
        "numeroRadicado": "SA0000000325",
        "urlComponenteWeb": "https://local.suranet.com/C87832685ED5658797A69C4E2776E73FB5EFF929833F9B1B4CFDF30B1675BD4A",
        "aplicacion": "981-WeSura",
        "idNegocio": "01"
    }
}
```

- **Ejemplo Json Response:**
  - Para Assesment de Reclamación:

```json
{
    "reclamante": {
        "estado": "FINALIZADO",
        "roles": [
            "BENEFICIARIO"
        ],
        "tipoIdentificacion": "C",
        "numeroIdentificacion": "43972686",
        "fechaExpedicionDocumento": "2000-05-27T00:00:00.000+00:00",
        "primerNombre": "DIANA",
        "segundoNombre": null,
        "primerApellido": "GOMEZ",
        "segundoApellido": "PEREZ",
        "paisNacimiento": "01",
        "paisConstitucion": null,
        "rolReclamante": "BENEFICIARIO",
        "correoElectronico": "JOHNATHAN.MONSALVE@SOFKA.COM.CO",
        "celular": "3219006000",
        "razonSocial": null,
        "soportesRequeridos": [],
        "indicadorRegimenPublico": false,
        "riesgoVo": {
            "tipoRiesgo": "ORDINARIO",
            "bloqueante": false,
            "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica."
        },
        "indicadorPeps": false,
        "indicadorGafi": false,
        "respuestaPEPS": "NO_REGISTRA",
        "tipoFormulario": "NO_APLICA",
        "tipoPersona": "N",
        "terminoFormulario": false,
        "validacionIdentidad": "NOAPLICA",
        "listaControl": [],
        "riesgo": {
            "pais": "01",
            "indicadorPep": false,
            "resultadoRegistraduria": null,
            "resultadoListasVinculantes": null,
            "resultadoControlPep": "No aplica",
            "resultadoValidacionIdentidad": null
        }
    },
    "evaluacion": {
        "idEvaluacion": "d4064657-c7a7-481f-a874-d491ced0cfbd",
        "estado": "FINALIZADO",
        "tipoOperacion": "Reclamaciones",
        "tipoNegocio": "INDIVIDUAL",
        "ramo": "VIDA INDIVIDUAL",
        "producto": "00",
        "cantidadAsegurados": 0,
        "medioRecaudo": "No aplica",
        "tipoCoasegurado": "null",
        "valorAsegurado": null,
        "valorPrima": null,
        "canal": "1 - nombreCanal",
        "oficina": "00 - nombreOficina",
        "asesor": "00 - nombreAsesor",
        "fechaCreacion": "2021-11-18T19:36:32.930+00:00",
        "indProcesoJudicial": true,
        "juzgado": "TEST",
        "ciudadProcesoJudicial": "MEDELLIN",
        "sarlafts": [
            {
                "estado": "FINALIZADO",
                "roles": [
                    "BENEFICIARIO"
                ],
                "tipoIdentificacion": "C",
                "numeroIdentificacion": "43972686",
                "fechaExpedicionDocumento": "2000-05-27T00:00:00.000+00:00",
                "primerNombre": "DIANA",
                "segundoNombre": null,
                "primerApellido": "GOMEZ",
                "segundoApellido": "PEREZ",
                "paisNacimiento": "01",
                "paisConstitucion": null,
                "rolReclamante": null,
                "correoElectronico": "JOHNATHAN.MONSALVE@SOFKA.COM.CO",
                "celular": "3219006000",
                "razonSocial": null,
                "soportesRequeridos": [],
                "indicadorRegimenPublico": false,
                "riesgoVo": {
                    "tipoRiesgo": "ORDINARIO",
                    "bloqueante": false,
                    "mensaje": "Cumple con politicas de SARLAFT. Debe completar el Conocimiento del Cliente si le aplica."
                },
                "indicadorPeps": false,
                "indicadorGafi": false,
                "respuestaPEPS": "NO_REGISTRA",
                "tipoFormulario": "NO_APLICA",
                "tipoPersona": "N",
                "terminoFormulario": false,
                "validacionIdentidad": "NOAPLICA",
                "listaControl": [],
                "riesgo": {
                    "pais": "01",
                    "indicadorPep": false,
                    "resultadoRegistraduria": null,
                    "resultadoListasVinculantes": null,
                    "resultadoControlPep": "No aplica",
                    "resultadoValidacionIdentidad": null
                },
                "score": "NO"
            },
            {
                "estado": "FINALIZADO",
                "roles": [
                    "TOMADOR"
                ],
                "tipoIdentificacion": "C",
                "numeroIdentificacion": "11389145",
                "fechaExpedicionDocumento": "2000-05-27T00:00:00.000+00:00",
                "primerNombre": "MARCELA",
                "segundoNombre": null,
                "primerApellido": "GOMEZ",
                "segundoApellido": "PEREZ",
                "paisNacimiento": "01",
                "paisConstitucion": null,
                "rolReclamante": null,
                "correoElectronico": "MAIL2@MAIL.COM.CO",
                "celular": "3219006000",
                "razonSocial": null,
                "soportesRequeridos": [],
                "indicadorRegimenPublico": false,
                "riesgoVo": {
                    "tipoRiesgo": "ORDINARIO",
                    "bloqueante": false,
                    "mensaje": null
                },
                "indicadorPeps": false,
                "indicadorGafi": false,
                "respuestaPEPS": "NO_REGISTRA",
                "tipoFormulario": "NO_APLICA",
                "tipoPersona": "N",
                "terminoFormulario": true,
                "validacionIdentidad": "NOAPLICA",
                "listaControl": [],
                "riesgo": {
                    "pais": "01",
                    "indicadorPep": false,
                    "resultadoRegistraduria": null,
                    "resultadoListasVinculantes": null,
                    "resultadoControlPep": "No aplica",
                    "resultadoValidacionIdentidad": null
                },
                "score": "NO"
            }
        ]
    }
}
```

- **Dependencias:**
  - Base de datos de sarlaft
  - Conexión a `service-bus` azure
