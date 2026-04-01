# Servicio Consultar País Gafi por Código

> **Fuente Confluence:** [Servicio Consultar País Gafi por Código](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4903010314)
> **Última modificación:** 2025-08-04 · versión 1
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo: **Permite consultar un país gafi por su código

- **Endpoint: GET** /sarlaftbackweb/paisesgafi/{{codigo}}

- **Perfil de Seus4:** PF_SARLAFTADM

- **Ejemplo Request: **/sarlaftbackweb/paisesgafi/894

**Ejemplo Json Response Exitoso:**

```json
{
    "codigo": "894",
    "nombre": "ZAMBIA",
    "dsBloqueante": "N",
    "fechaCreacion": "2025-08-04T15:13:32.731+00:00",
    "fechaBaja": null
}
```text

- **Ejemplo Json Response con error 500:**

```json
{
    "errors": [
        {
            "id": "tecnico-001",
            "tipo": "TECNICO",
            "mensaje": "Se ha presentado un error no controlado en el proceso de Sarlaft",
            "detalle": "Se ha presentado un error no controlado en el proceso de Sarlaft"
        }
    ]
}
```text

- **Ejemplo Json Response con error 400:**

```json
{
    "errors": [
        {
            "id": "formato-001",
            "tipo": "FORMATO",
            "mensaje": "Dato de entrada incorrecto",
            "detalle": "Dato de entrada incorrecto: codigo: Debe contener solo números. "
        }
    ]
}
```

Iniciativa: [https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/612207](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/612207)
