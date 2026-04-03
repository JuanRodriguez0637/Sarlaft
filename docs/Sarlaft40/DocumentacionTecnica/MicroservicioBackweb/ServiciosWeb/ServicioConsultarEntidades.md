# Servicio Consultar Entidades

> **Fuente Confluence:** [Servicio Consultar Entidades](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2893152310)
> **Última modificación:** 2022-09-09 — Alejandra Zuleta Gonzalez · versión 1
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

**Descripción:**

Servicio que permite consultar las entidades matriculadas tanto activas como inactivas. Si una entidad ha sido activada e inactivada en varias ocasiones para la misma tabla, siempre se mostrará el estado más reciente.

**Endpoint:** `/sarlaftbackweb/entidades/consultar`

**Perfil Seus4:** `PF_SARLAFTAD`

Los datos permitidos en el request de entrada son:

- Estado: `ACTIVO`, `INACTIVO`
- Tipo Entidad: `BOLSA`, `FINASEPEN`, `REGIMEN`, `PASSTHROUGH`
- Order: `DNI`, `NOMBRE_ENTIDAD`, `TIPO_ENTIDAD`, `ESTADO`, `FECHA_ESTADO`
- Tipo Order: `ASC`, `DESC`

**Notas:**

- Si no se envía un `ORDER` por defecto se organiza por `FECHA_ESTADO`
- Si no se envía un `TIPO ORDER` por defecto se organiza de manera descendente.

**Ejemplo Request:**

```json
{
    "tipoIdentificacion": null,
    "numeroIdentificacion": null,
    "tipoEntidad": null,
    "estado": "INACTIVO",
    "pagina": 1,
    "cantidadDatosPermitidos": 25,
    "order": "TIPO_ENTIDAD",
    "tipoOrder": "DESC"
}
```

**Ejemplo Response:**

```json
{
    "listaEntidades": [{
            "tipoIdentificacion": "C",
            "numeroIdentificacion": "1106895652",
            "nombreEntidad": "USUARIO PRUEBA",
            "tipoEntidad": "BOLSA",
            "estado": "INACTIVO",
            "trazabilidad": [{
                    "estado": "INACTIVO",
                    "fechaEstado": "2022-09-06T05:00:00.000+00:00",
                    "usuario": "pedrvevi"
                }
            ],
            "fechaEstado": "2022-09-06T05:00:00.000+00:00"
        }
    ],
    "numeroPagina": 1,
    "cantidadPagina": 1,
    "cantidadDatos": 1
}
```

**Dependencias:**

- Base de datos
