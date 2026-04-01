# Guardar Formulario - Terceros

> **Fuente Confluence:** [Guardar Formulario - Terceros](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2797699257)
> **Última modificación:** 2024-01-15 — Diana Muñoz · versión 4
> **Sección:** [Servicio Terceros](./index.md)
- **Objetivo:** Permite guardar la información de formulario de los sarlafts y agregar el sarlaft de apoderado de ser necesario para continuar con el proceso de sarlafts.

Además, en caso que el tomador sea una persona jurídica, permite agregar el sarlaft de los representantes legales y accionistas, que para tener en cuenta, siempre que el tomador sea una **persona jurídica se deben agregar al menos un representante legal y un accionista**.

- **Endpoint:** /sarlaftserv/api/v1/form/save
- **Perfil de Seus4:** PF_TERCEROSSAVEFORMAPI

**Nuevo Endpoint:** POST /sarlaftserv/v1/formularios

**Perfil de Seus4:** aun no creado para consumo interno a SURA.

- **Notas:** El guardado de información se puede hacer segmentado, es decir, si la evaluación tiene Tomador, 3 asegurados y 2 beneficiarios se puede llenar la información inicialmente con el tomador y 2 asegurados y en otro request se puede enviar la información del asegurado y los 2 beneficiarios faltantes. Sin embargo, se deben tener en cuenta las siguientes excepciones:
  - Cuando el **tomador** es **Persona jurídica** la primera vez que se consuma el servicio se debe enviar al menos un **Representante Legal** y **Accionista**, los cuales serán agregados a la evaluación y se les guardará la información de formulario suministrada
  - El servicio agrega figuras y además guarda la información de formulario de las figuras, sin embargo, si al momento de agregar figuras se intenta agregar **Representante legal** o **Accionista** para un **tomador Persona natural** el servició fallará y no agregará ninguna figura ni intentará guardar la información de ningún servicio.
  - El servicio agrega figura y además guarda la información de formulario de las figuras, si ocurre algún error diferente a los anteriores al momento de agregar figura, entonces el servicio intentará guardar la información de las figuras que si se pudieron agregar o de las figuras anteriores, sin embargo, en caso que haya algún error al momento de guarda información de formulario, en ese caso se detendrá el servicio por completo y no agregará figuras ni guardará información.

- **Ejemplo Json Request:**

```json
{
    "evaluacionId": "1f9d710c-9e57-49c9-9275-839b758cf323",
    "relacionLaboral": false,
    "administradorPep": false,
    "sarlafts": [
        {
            "tipoFigura": ["TOMADOR"], 
            "personaPep": false,
            "cuentaConInformacion": null,
            "justificacionInformacion": "",
            "tieneRelacionPep": false,
            "tipoEmpresa": "PYMES",
            "cliente": {
                "celular": "3166273241",
                "correo": "LCORTIZ@SURA.COM.CO",
                "porParticipacionSocio": 0,
                "tipoPersona": "J",
                "razonSocial": "YA NO LAVAMOS ACTIVOS LTDA.",
                "paisConstitucion": "57",
                "documento": {
                    "numero": "8110463211",
                    "tipo": "A"
                }
            }
        },
        {
            "tipoFigura": ["REPRESENTANTE_LEGAL"],
            "tipoEmpresa": "PYMES",
            "cliente": {
                "tipoPersona": "N",
                "correo": "johnathan.monsalve@sofka.com.co",
                "celular": "3117899889",
                "documento": {
                    "tipo": "C",
                    "numero": "10172157",
                    "fechaExpedicion": "2005-10-12"
                },
                "persona": {
                    "primerApellido": "cur",
                    "primerNombre": "camilo",
                    "pais": "57"
                }
            }
        },
        {
            "tipoFigura": ["ACCIONISTA"],
            "tipoEmpresa": "PYMES",
            "cliente": {
                "porParticipacionSocio": 5,
                "tipoPersona": "N",
                "documento": {
                    "tipo": "C",
                    "numero": "1234567800",
                    "fechaExpedicion": "2005-10-12"
                },
                "persona": {
                    "primerApellido": "johnathan",
                    "primerNombre": "monsalve",
                    "pais": "57"
                }
            }
        }
    ]
}
```text

- **Ejemplo Response:**

```json
{
    "id": "1f9d710c-9e57-49c9-9275-839b758cf323",
    "estado": "PENDIENTE",
    "sarlafts": [
        {
            "dni": "A8110463211",
            "estadoSarlaft": "PENDIENTE",
            "estadoFormulario": "FINALIZADO",
            "figuras": ["TOMADOR"],
            "listaControles": []
        },
        {
            "dni": "C10172157",
            "estadoSarlaft": "PENDIENTE",
            "estadoFormulario": "FINALIZADO",
            "figuras": ["REPRESENTANTE_LEGAL"],
            "listaControles": [
                {
                    "mensajeControl": "Pendiente por realizar el proceso de validación de identidad para continuar con la vinculación del cliente",
                    "control": "EXPERIAN",
                    "estado": "PENDIENTE"
                }
            ]
        }
    ],
    "errorAgregarFigura": []
}
```

- **Colección de postman de apoyo:**

[`Feature-69273_ServicioGuardarFormularioTerceros.postman_collection.json`](./GuardarFormularioTerceros/Feature-69273_ServicioGuardarFormularioTerceros.postman_collection.json)
