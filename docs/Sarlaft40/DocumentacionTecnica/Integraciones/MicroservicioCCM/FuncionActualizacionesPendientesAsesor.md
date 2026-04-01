# Función actualizaciones pendientes de los clientes (Asesor) - CCM

> **Fuente Confluence:** [Función actualizaciones pendientes de los clientes (Asesor) - CCM](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2355200258/Funci%C3%B3n+actualizaciones+pendientes+de+los+clientes+%28Asesor%29+-+CCM)
> **Última modificación:** 2021-09-01 — Deivid Harritson Urrego Carvajal · versión 2
> **Sección:** [Microservicio - CCM](./index.md)

**Mensaje de salida:**

```json
{
    "claves": {
        "clave1": {
            "valor": "codigoAsesor=1122334455"
        },
        "clave2": {
            "valor": ""
        },
        "clave3": {
            "valor": ""
        }
    },
    "codigoProceso": "",
    "consecutivo": "9082-1122334455-65e6b682-e897-420b-9b0a-a55960514dcb",
    "content": {
        "datosComunicacion" : {
			"primerNombreAsesor": "DEIVID",
			"emailAsesor": "prueba@hotmail.com.co",
			"celularAsesor": "3115211111",
            "tipoDeTramite": "*",
			"adjunto": [
				{
					"tipoyNumerodeIdentificacionCliente": "C 1234567890",
					"nombreCompletoCliente": "MARIA ROSARIO TIJERAS",
					"ramo": "AUTOS, VIDA",
					"nombreOficina": "BOGOTA",
					"fechaDeUltimaActualizacion": "2020/06/15",
					"tipoDeProcedimiento": "INTENSIFICADO"
				},
				{
					"tipoyNumerodeIdentificacionCliente": "A 9541256232",
					"nombreCompletoCliente": "PEPE GOMEZ",
					"ramo": "AUTOS",
					"nombreOficina": "ANTIOQUIA",
					"fechaDeUltimaActualizacion": "2014/07/19",
					"tipoDeProcedimiento": "SIMPLIFICADO"
				},
				{
					"tipoyNumerodeIdentificacionCliente": "E 1392839212",
					"nombreCompletoCliente": "JUAN DAVID SANCHEZ",
					"ramo": "VIDA",
					"nombreOficina": "ANTIOQUIA",
					"fechaDeUltimaActualizacion": "2019/09/09",
					"tipoDeProcedimiento": "INTENSIFICADO"
				}
			]
		},
        "viasTrafficProps": {
            "codigoAplicacion": "9082",
            "descripcionOperacion": "ACTUALIZACIONASESORES",
            "descripcionProceso": "SARLAFT",
            "descripcionSolucion": "*",
            "compania": "TRANSVERSAL",
            "procesoSura": "ADMINISTRACION RIESGOS DEL CLIENTE",
            "idCliente": ""
        }
    }
}
```
