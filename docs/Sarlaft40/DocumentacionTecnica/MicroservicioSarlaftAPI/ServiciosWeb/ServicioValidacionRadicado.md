# Servicio Validacion Radicado

> **Fuente Confluence:** [Servicio Validacion Radicado](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2619802061)
> **Última modificación:** 2022-06-07 — Mateo Valencia Muriel (Unlicensed) · versión 4
> **Sección:** [Servicios Web](./index.md)
- **Objetivo:** Permite validar la información de cada uno de los sarlafts ya almacenado por medio del numero del radico por el cual se realiza una consulta y se compara la información ingresada con la información almacenada y en caso de haber incongruencias se devuelve información de los campos que no coinciden.
- **Endpoint:** /sarlaftserv/assessment/validate
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

```json
{
    "codigoAsesor": "00",
    "codigoOficina": "00",
    "codigoRamo": "1",
    "codigoProducto": "02",
    "valorAsegurado": 500000,
    "valorPrima": 500000,
    "codigoCanal": "1",
    "tipoNegocio": "COLECTIVO",
    "codigoOperacion": "01",
    "medioRecaudo": "DEBITO_AUTOMATICO",
    "numeroRadicado": "SA0000000004",
    "tomador": {
        "tipoPersona": "N",
        "tipoDocumento": "C",
        "numeroDocumento": "11389126",
        "primerNombre": "ñestor",
        "segundoNombre": "fernando",
        "primerApellido": "arevalo",
        "segundoApellido": "Espitia",
        "correo": "mail_1@mail.com.co",
        "celular": "3102345670"
    },
    "beneficarios": [
        {
            "tipoPersona": "N",
            "tipoDocumento": "C",
            "numeroDocumento": "11389126",
            "primerNombre": "diana",
            "primerApellido": "gomez",
            "segundoApellido": "Perez"
        }
    ]
}
```text

Response:

```json
{
    "estado": "PENDIENTE",
    "mensajeRechazo": null,
    "error": false,
    "sarlafts": [
        {
            "requiereDiligenciar": false,
            "fechaActualizacion": "2022-03-02T20:30:15.571+00:00",
            "dni": "C18388805",
            "estado": "PENDIENTE",
            "listaControl": [
                {
                    "mensajeControl": "Pendiente por realizar el proceso de validación de identidad para continuar con la vinculación del cliente",
                    "control": "EXPERIAN",
                    "estado": "PENDIENTE"
                },
                {
                    "mensajeControl": null,
                    "control": "DOCUMENT_PN",
                    "estado": "FALLA_TECNICA"
                },
                {
                    "mensajeControl": "La persona está catalogada como PEP (Persona Expuesta Políticamente) por favor gestione el control de vinculación para continuar con el proceso.",
                    "control": "PEPS",
                    "estado": "FALLIDO"
                }
            ]
        }
    ]
}
```text

Respuesta en caso de datos diferentes a la base de datos:

```json
{
    "estado": null,
    "mensajeRechazo": "La siguiente Informacion no coincide con la informacion almacenada: CodigoOficina 45",
    "error": true,
    "sarlafts": null
}
```

**Dependencias:**

- Base de datos de sarlaft
