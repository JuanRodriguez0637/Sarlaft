# Servicio Consultar Países Gafi por Código y Categoría

> **Fuente Confluence:** [Servicio Consultar Países Gafi por Código y Categoría](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4903010325)
> **Última modificación:** 2025-04-08 — Mauricio Marin Martinez · versión 1
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite consultar países por código y por categoría
- **Endpoint:** `GET` `/sarlaftbackweb/paisesgafi`
- **Params:** `codigo` (opcional), `categoria` (opcional)
- **Perfil de Seus4:** `PF_SARLAFTADM`
- **Ejemplo Request:** `/sarlaftbackweb/paisesgafi?codigo=894&categoria=N`

Nota: `codigo` y `categoria` son opcionales ya que el servicio permite consultar con filtros o sin filtros

**Ejemplo Json Response Exitoso:**

```json
[
    {
        "codigo": "894",
        "nombre": "ZAMBIA",
        "dsBloqueante": "N",
        "fechaCreacion": "2025-08-04T15:13:32.731+00:00",
        "fechaBaja": null
    }
]
```

- **Ejemplo Json Response con solo categoría:** `/sarlaftbackweb/paisesgafi?categoria=S`

```json
[
    {
        "codigo": "364",
        "nombre": "IRAN",
        "dsBloqueante": "S",
        "fechaCreacion": "2021-03-11T05:00:00.000+00:00",
        "fechaBaja": null
    },
    {
        "codigo": "1",
        "nombre": "COREA DEL NORTE",
        "dsBloqueante": "S",
        "fechaCreacion": "2021-03-11T05:00:00.000+00:00",
        "fechaBaja": null
    },
    {
        "codigo": "104",
        "nombre": "BIRMANIA",
        "dsBloqueante": "S",
        "fechaCreacion": "2021-03-11T05:00:00.000+00:00",
        "fechaBaja": null
    }
]
```

- **Ejemplo Json Response con error 400:**

```json
{
    "errors": [
        {
            "id": "formato-001",
            "tipo": "FORMATO",
            "mensaje": "Dato de entrada incorrecto",
            "detalle": "Dato de entrada incorrecto: codigo: Debe contener solo números. categoria: Solo se permite N, S, NA. "
        }
    ]
}
```

Iniciativa: [https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/612207](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/612207)
