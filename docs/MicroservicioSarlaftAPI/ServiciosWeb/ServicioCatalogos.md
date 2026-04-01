# Servicio Catálogos

**Fuente Confluence:** [Servicio Catalogos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2709094564)  
**Sección:** [Servicios Web](./index.md)

---

## Descripción

- **Objetivo:** Permite obtener los catálogos utilizados durante el diligenciamiento de un formulario de SARLAFT.
- **Endpoint:** `/sarlaftserv/catalogue/findCatalogue`
- **Perfil de Seus4:** `PF_CONSUMSERVSARLAFTAPI`

---

## Catálogos Disponibles

Los archivos JSON de request y response están disponibles en [`ServicioCatalogos/`](./ServicioCatalogos/).

| Catálogo | Request | Response |
| ---------- | --------- | ---------- |
| `TIPO_PERSONA` | `{"codigoCatalogo": "TIPO_PERSONA", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_PERSONA_RESPONSE.json](./ServicioCatalogos/TIPO_PERSONA_RESPONSE.json) |
| `COD_RAMOS` | `{"codigoCatalogo": "COD_RAMOS", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null, "fraccionTexto": null}` | [COD_RAMOS_RESPONSE.json](./ServicioCatalogos/COD_RAMOS_RESPONSE.json) |
| `COD_SUBRAMOS` | `{"codigoCatalogo": "COD_SUBRAMOS", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": "006"}` | [COD_SUBRAMOS_RESPONSE.json](./ServicioCatalogos/COD_SUBRAMOS_RESPONSE.json) |
| `TIPO_EVIDENCIA` | `{"codigoCatalogo": "TIPO_EVIDENCIA", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_EVIDENCIA_RESPONSE.json](./ServicioCatalogos/TIPO_EVIDENCIA_RESPONSE.json) |
| `TIPO_DIRECCION_PN` | `{"codigoCatalogo": "TIPO_DIRECCION_PN", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_DIRECCION_PN_RESPONSE.json](./ServicioCatalogos/TIPO_DIRECCION_PN_RESPONSE.json) |
| `TIPO_DIRECCION_PJ` | `{"codigoCatalogo": "TIPO_DIRECCION_PJ", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_DIRECCION_PJ_RESPONSE.json](./ServicioCatalogos/TIPO_DIRECCION_PJ_RESPONSE.json) |
| `CANALES` | `{"codigoCatalogo": "CANALES", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null, "fraccionTexto": null}` | [CANALES_RESPONSE.json](./ServicioCatalogos/CANALES_RESPONSE.json) |
| `TIPO_PROPIETARIO` | `{"codigoCatalogo": "TIPO_PROPIETARIO", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_PROPIETARIO_RESPONSE.json](./ServicioCatalogos/TIPO_PROPIETARIO_RESPONSE.json) |
| `TIPO_NEGOCIO` | `{"codigoCatalogo": "TIPO_NEGOCIO", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_NEGOCIO_RESPONSE.json](./ServicioCatalogos/TIPO_NEGOCIO_RESPONSE.json) |
| `TIPO_RELACION` | `{"codigoCatalogo": "TIPO_RELACION", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_RELACION_RESPONSE.json](./ServicioCatalogos/TIPO_RELACION_RESPONSE.json) |
| `PARENTESCO_PN` | `{"codigoCatalogo": "PARENTESCO_PN", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [PARENTESCO_PN_RESPONSE.json](./ServicioCatalogos/PARENTESCO_PN_RESPONSE.json) |
| `TIPO_COASEGURO` | `{"codigoCatalogo": "TIPO_COASEGURO", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_COASEGURO_RESPONSE.json](./ServicioCatalogos/TIPO_COASEGURO_RESPONSE.json) |
| `RELACIONES` | `{"codigoCatalogo": "RELACIONES", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [RELACIONES_RESPONSE.json](./ServicioCatalogos/RELACIONES_RESPONSE.json) |
| `OPERACION` | `{"codigoCatalogo": "OPERACION", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [OPERACION_RESPONSE.json](./ServicioCatalogos/OPERACION_RESPONSE.json) |
| `RESULTADO_EVIDENCIA` | `{"codigoCatalogo": "RESULTADO_EVIDENCIA", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [RESULTADO_EVIDENCIA_RESPONSE.json](./ServicioCatalogos/RESULTADO_EVIDENCIA_RESPONSE.json) |
| `TIPO_RIESGO` | `{"codigoCatalogo": "TIPO_RIESGO", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_RIESGO_RESPONSE.json](./ServicioCatalogos/TIPO_RIESGO_RESPONSE.json) |
| `TIPO_FORMULARIO` | `{"codigoCatalogo": "TIPO_FORMULARIO", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_FORMULARIO_RESPONSE.json](./ServicioCatalogos/TIPO_FORMULARIO_RESPONSE.json) |
| `TIPO_ENTIDAD` | `{"codigoCatalogo": "TIPO_ENTIDAD", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_ENTIDAD_RESPONSE.json](./ServicioCatalogos/TIPO_ENTIDAD_RESPONSE.json) |
| `TIPO_FIGURA` | `{"codigoCatalogo": "TIPO_FIGURA", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_FIGURA_RESPONSE.json](./ServicioCatalogos/TIPO_FIGURA_RESPONSE.json) |
| `TIPO_REQUISITO` | `{"codigoCatalogo": "TIPO_REQUISITO", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [TIPO_REQUISITO_RESPONSE.json](./ServicioCatalogos/TIPO_REQUISITO_RESPONSE.json) |
| `PARENTESCO_PJ` | `{"codigoCatalogo": "PARENTESCO_PN", "departamento": null, "pais": null, "tipoPersona": null, "subCodigoParametro": null}` | [PARENTESCO_PN_RESPONSE.json](./ServicioCatalogos/PARENTESCO_PN_RESPONSE.json) |
| `ACTIVIDADESECO` | ver [ACTIVIDADESECO_REQUEST.json](./ServicioCatalogos/ACTIVIDADESECO_REQUEST.json) | [ACTIVIDADESECO_RESPONSE.json](./ServicioCatalogos/ACTIVIDADESECO_RESPONSE.json) |

---

## Ejemplo Request

```json
[
    {
        "codigoCatalogo": "TIPO_PERSONA",
        "departamento": null,
        "pais": null,
        "tipoPersona": null,
        "subCodigoParametro": null
    }
]
```

---

## Dependencias

- Base de Datos Sarlaft
- Aplicaciones Externas

## Información Relacionada

- [Servicio obtener catálogos](./ServicioObtenerCatalogos.md)
