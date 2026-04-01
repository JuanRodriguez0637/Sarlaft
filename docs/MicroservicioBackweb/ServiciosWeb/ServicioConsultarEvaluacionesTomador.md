# Servicio Consultar evaluaciones de un tomador.

> **Fuente Confluence:** [Servicio Consultar evaluaciones de un tomador.](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2427879670)
> **Última modificación:** 2026-02-19 · versión 8
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite  consultar las evaluaciones generadas de un cliente en los procesos de negocio nuevo, reclamaciones y actualizacion

- **Endpoint:** /sarlaftbackweb/consultar/evaluaciones/generadas

- **Perfil de Seus4: **PF_SARLAFTADMCON

- **Ejemplo Json Request:**

```json
{
    "tipoIdentificacion": "C",
    "numeroIdentificacion": "71287053",
    "fechaInicial": "2026-01-01",
    "fechaFinal": "2026-02-01",
    "codigoAgente":null,
    "idNegocio":null,
    "tipoOperacion":null,
    "tipoPersona":null,
    "tipoFormulario": "ORDINARIO",
    "estadoEvaluacion":null,
    "radicado":"0000000692",
    "pagina": 1,
    "cantidadDatosPermitidos": 15,
    "order": "FECHA_CREACION",
    "tipoOrder": "DESC"
}
Donde fechaInicial y fechaFinal son obligatorios y con un maximo de 3 meses de rango
Donde tipoOperacion es obligatorio
Donde tipoPersona puede recibir los siguientes valores: N, J.
Donde order puede recibir los siguientes. valores:   DNI, NOMBRE, RAMO, ESTADO, TIPO_FORMULARIO, FECHA_CREACION, TIPO_RIESGO.
Donde tipoOrder puede recibir los siguientes valores: ASC, DESC.
Donde tipoFormulario puede recibir los siguientes valores:   SIMPLIFICADO, ORDINARIO, INTENSIFICADO, NO_APLICA
```text

- **Ejemplo Json Response:**

```json
{
    "listaEvaluaciones": [
        {
            "evaluacionId": "24c3a332-32e2-48f9-b78f-dd771556a20e",
            "nmIdentificacion": "9994339331",
            "codigoOperacion": "RE",
            "primerNombre": null,
            "segundoNombre": null,
            "primerApellido": null,
            "segundoApellido": null,
            "codigoRamo": "083",
            "nombreRamo": "VIDA DE GRUPO",
            "codigoProducto": "084",
            "nombreProducto": "PES PARA SUS EMPLEADOS Y FAMILIAS CONTRIBUTIVO",
            "estado": "PENDIENTE",
            "dsTipoFormulario": "ORDINARIO_PJ_DE_VIDA",
            "fechaCreacion": "2022-08-23T16:43:16.111+00:00",
            "nmToken": "F223E6E221B4367D7A8591474AF54EF21F5511AD03A0D7F54BA81DAB74713F25",
            "razonSocial": "CLUB LOS TRIUNFADORES CQLII",
            "tipoIdentificacion": "A",
            "correo": "CHUCHO1804J@GMAIL.COM",
            "oficina": "4031",
            "asesor": "6705",
            "tipoRiesgo": "ORDINARIO"
        }
    ],
    "numeroPagina": 1,
    "cantidadPagina": 1,
    "cantidadDatos": 1
}
```

**Nota: **Se agrega código Operación para identificar las evaluaciones de reclamación.

- **Dependencias**:

Base de datos de sarlaft.
