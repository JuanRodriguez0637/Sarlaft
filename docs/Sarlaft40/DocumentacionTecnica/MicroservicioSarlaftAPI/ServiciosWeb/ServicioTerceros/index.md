# Servicio Terceros

> **Fuente Confluence:** [Servicio Terceros](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2671313235)
> **Última modificación:** 2024-01-15 — Diana Muñoz · versión 6
> **Sección:** [Servicios Web](../index.md)
- **Objetivo:** Permite crear la evaluación ingresando tanto la información del assesment como la de guardar formulario en un solo request para generar la evaluación correspondiente.
- **Endpoint:** /sarlaftserv/api/v1/assessment
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI

**Nuevo Endpoint:** PUT/sarlaftserv/v1/evaluaciones

**Perfil de Seus4:** aun no creado para consumo interno a SURA.

- **Ejemplo Json Request:**

```json
{
    "codigoOperacion": "01",
    "negocioId": "01",
    "infoPendiente": true,
    "codigoAplicacion": "01",
    "sarlafts": [
        {
            "figuras": [
                "Tomador"
            ],
            "evidencias":[
                {
                    "tipo":"RRCC",
                    "observaciones":"RRCC",
                    "controlConsecutivo" : "RRCC"
                },
                {
                    "tipo":"DOCUMENT_PN",
                    "observaciones":"DOCUMENT_PN",
                    "controlConsecutivo" : "DOCUMENT_PN"
                }
            ],
            "cliente": {
                "tipoPersona": "N",
                "correo": "mail_1@mail.com.co",
                "celular": "3102345670",
                "persona": {
                    "primerNombre": "Ñestor",
                    "segundoNombre": "Fernando",
                    "primerApellido": "Arevalo",
                    "segundoApellido": "Espitia",
                    "pais": "57"
                },
                "documento": {
                    "tipo": "C",
                    "numero": "1036683385",
                    "fechaExpedicion": "2007-05-27"
                },
                "infoFinanciera": {
                    "ingresos": "20000",
                    "egresos": "15000",
                    "actividadEconomica": "N1922",
                    "codigoOcupacion": "A50",
                    "origenFondos": "TRABAJO"
                },
                "direcciones": [
                    {
                        "tipo": "RS",
                        "pais": "57",
                        "departamento": "15",
                        "ciudad": "123",
                        "direccion": "Calle"
                    }
                ],
                "relaciones": [
                    {
                        "relacionPeps": true,
                        "parentescoPeps": "01",
                        "tipo": "FAMILIA",
                        "documento": {
                            "tipo": "C",
                            "numero": "1036683385"
                        },
                        "persona": {
                            "primerNombre": "Sandra",
                            "segundoNombre": "Milena",
                            "primerApellido": "Arevalo",
                            "segundoApellido": "Espitia"
                        }
                    }
                ]
            },
            "tipoRiesgo": "SIMPLIFICADO",
            "cuentaConInformacion": false
        }
    ],
    "poliza": {
        "tipoNegocio": "COLECTIVO",
        "codigoRamo": "1",
        "codigoProducto": "00",
        "codigoCanal": "1",
        "valorAsegurado": 500000,
        "valorPrima": 500000,
        "medioPago": "DEBITO_AUTOMATICO",
        "tipoCoaseguro": "ACEPTADO",
        "licitacionPublica": false
    }
}
```text

**Ejemplo de Response Correcto:**

```json
{
   "id":"94d81513-2da4-488c-a637-8330c8ba378a",
   "estado":"FINALIZADO",
   "fechaCreacion":"2022-05-02T20:17:03.512+00:00",
   "ultimaActualizacion":"2022-05-02T20:17:03.512+00:00",
   "sarlafts":[
      {
         "dni":"C1036683385",
         "estado":"FINALIZADO",
         "listaControl":[
            {
               "mensajeControl":"RRCC",
               "control":"RRCC",
               "estado":"EXITOSO"
            },
            {
               "mensajeControl":"DOCUMENT_PN",
               "control":"DOCUMENT_PN",
               "estado":"EXITOSO"
            }
         ],
         "fechaCreacion":"2022-05-02T20:17:03.512+00:00",
         "fechaActualizacion":"2022-05-02T20:17:03.512+00:00",
         "soportesPendientes":[]
      }
   ]
}
```

## Sub-páginas

- [Guardar Formulario - Terceros](./GuardarFormularioTerceros.md)
- [Comunicación backend to backend con motor - sarlaftapi](./ComunicacionBackendMotorSarlaftapi.md)
