# Motor Evaluación - Retirar evidencia de IDENTITY para asesores directos del canal Affinity en la solución de movilidad

> **Fuente Confluence:** [Motor Evaluación - Retirar evidencia de IDENTITY para asesores directos del canal Affinity en la solución de movilidad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3988389894/Motor+Evaluaci+n+-+Retirar+evidencia+de+IDENTITY+para+asesores+directos+del+canal+Affinity+en+la+soluci+n+de+movilidad)
> **Última modificación:** 2024-08-23 — Jose Mosquera · versión 2
> **Sección:** [Motor Evaluación - Retirar evidencia de IDENTITY para asesores](./index.md)

**Generalidades:**

Se implementa regla en el motor de evaluaciones que excluye la asignación de la validación de identidad (IDENTITY) a los asesores directos del canal Afinity en los productos del ramo de movilidad.

Esta medida asegura que no se realice una doble validación de identidad para los clientes del canal Afinity, específicamente aquellos vinculados al aliado Falabella.

Tomamos como ejemplo el siguiente criterio que nos da un ejemplo claro de como seria un escenario de prueba.

**Escenario de Prueba:**

- Exclusión de Validación de Identidad en Evaluación de Negocio Nuevo

**Dado:**

- Que se crea una evaluación para un negocio nuevo.

- Que el cliente es una persona natural.

- Que el cliente tiene la figura de tomador, asegurado y/o beneficiario.

- Que el producto corresponde al ramo 040 - movilidad.

- Que el asesor asociado tiene el código `185499 `.

- Que el canal asignado tiene el código `CC015`.

**Cuando:**

- Se asigne el riesgo ORDINARIO al tomador, asegurado y/o beneficiario.

- El tomador indica que no cuenta con la información del asegurado y/o beneficiario.

**Entonces:**

- La evidencia de validación de identidad a través de EXPERIAN no se asignará al tomador, asegurado y/o beneficiario.

- Y se finalizará la evaluación SARLAFT.

- **Endpoint:** [sarlaftapi.labsura.com](http://sarlaftapi.labsura.com)/sarlaftserv/v1/evaluaciones

- **Ejemplo1 Json Request:**

```text
{
    "solicitudDni": "C1038098972",
    "codigoOperacion": "01",
    "codigoAplicacion": "230",
    "negocioId": "0940000444",
    "tomador": {
        "cliente": {
            "tipoPersona": "N",
            "correo": "josejhouar.mosqueraramirez@amaris.com.co",
            "celular": "3166273241",
            "documento": {
                "tipo": "C",
                "numero": "1070327148",
                "fechaExpedicion": "2007-11-22"
            },
            "persona": {
                "primerNombre": "CLAUDIA",
                "segundoNombre": "LIZETH",
                "primerApellido": "FERNANDEZ",
                "segundoApellido": "CANTES",
                "pais": "57"
            }
        }
    },
  "polizas": [
        {
            "codigoRamo": "040",
            "codigoProducto": "ARL",
            "codigoCanal": "CC015",
            "negocio": "INDIVIDUAL",
            "codigoOficina": "099",
            "codigoAgente": "185499 ",
            "valorAsegurado": 130000000,
            "valorPrima": 130000000
        }
    ]
}
```

- **Ejemplo1 Json Response:**

```text
{
    "id": "8139fc40-61a1-4341-8ba2-a8de5a2a5de8",
    "estado": "PENDIENTE",
    "fechaCreacion": "2024-08-23T14:16:51.022+00:00",
    "ultimaActualizacion": "2024-08-23T14:16:51.022+00:00",
    "error": null,
    "url": "https://sarlaft.labsura.com/redirect/iniciar-proceso/54733DB7726DB0010A8E3E75628C684FC5B682A9E1BAEF4E723BEC23073BCD91",
    "sarlafts": [
        {
            "dni": "C1070327148",
            "estado": "PENDIENTE",
            "requiereFormulario": true,
            "listaControl": [
                {
                    "mensajeControl": "La validación del documento de identidad con la Registraduría Nacional aun está pendiente por realizar. Una vez se obtenga respuesta, se emite el estado final de la consulta.",
                    "control": "DOCUMENT_PN",
                    "estado": "PENDIENTE"
                }
            ],
            "fechaCreacion": "2024-08-23T14:16:51.000+00:00",
            "fechaActualizacion": "2024-08-23T14:16:51.000+00:00",
            "mensajeFormulario": "Cumple con políticas de SARLAFT. Debe completar la información del Formulario de Conocimiento del Cliente SARLAFT para continuar con el proceso.",
            "tipoFormulario": "ORDINARIO"
        }
    ]
}
```

- **Ejemplo2 Json Request:**

```text
{
    "solicitudDni": "C1038098972",
    "codigoOperacion": "01",
    "codigoAplicacion": "230",
    "negocioId": "0940000444",
    "tomador": {
        "cliente": {
            "tipoPersona": "N",
            "correo": "josejhouar.mosqueraramirez@amaris.com.co",
            "celular": "3166273241",
            "documento": {
                "tipo": "C",
                "numero": "1070327148",
                "fechaExpedicion": "2007-11-22"
            },
            "persona": {
                "primerNombre": "CLAUDIA",
                "segundoNombre": "LIZETH",
                "primerApellido": "FERNANDEZ",
                "segundoApellido": "CANTES",
                "pais": "57"
            }
        }
    },
  "polizas": [
        {
            "codigoRamo": "040",
            "codigoProducto": "ARL",
            "codigoCanal": "CC028",
            "negocio": "INDIVIDUAL",
            "codigoOficina": "099",
            "codigoAgente": "48946",
            "valorAsegurado": 130000000,
            "valorPrima": 130000000
        }
    ]
}
```

- **Ejemplo2 Json Response:**

```text
{
    "id": "8b5d4dea-20c4-4ded-936e-29d7768c020f",
    "estado": "PENDIENTE",
    "fechaCreacion": "2024-08-23T14:19:43.520+00:00",
    "ultimaActualizacion": "2024-08-23T14:19:43.520+00:00",
    "error": null,
    "url": "https://sarlaft.labsura.com/redirect/iniciar-proceso/336D1F9590938855FB9D3E5720ACD3970BE8A9B37A5BBA8A5ECFBE2F23395777",
    "sarlafts": [
        {
            "dni": "C1070327148",
            "estado": "PENDIENTE",
            "requiereFormulario": true,
            "listaControl": [
                {
                    "mensajeControl": "La validación del documento de identidad con la Registraduría Nacional aun está pendiente por realizar. Una vez se obtenga respuesta, se emite el estado final de la consulta.",
                    "control": "DOCUMENT_PN",
                    "estado": "PENDIENTE"
                }
            ],
            "fechaCreacion": "2024-08-23T14:19:43.000+00:00",
            "fechaActualizacion": "2024-08-23T14:19:43.000+00:00",
            "mensajeFormulario": "Cumple con políticas de SARLAFT. Debe completar la información del Formulario de Conocimiento del Cliente SARLAFT para continuar con el proceso.",
            "tipoFormulario": "ORDINARIO"
        }
    ]
}
```

- **Nota**

Al crear una nueva regla en el motor de evaluación SARLAFT 4.0, es importante considerar que la edición del archivo debe realizarse utilizando una alternativa como LibreOffice.
