# Servicio Consultar Salario Mínimo

> **Fuente Confluence:** [Servicio Consultar Salario Mínimo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4221992968)
> **Última modificación:** 2024-11-12 · versión 2
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo: **Permite consultar los salarios mínimos creados y actualizados en un rango de fechas, ya sea en estado activos o inactivos

- **Endpoint: GET** /sarlaftbackweb/salariosminimos

- **Params:  **fechaInicial, fechaFinal

- **Perfil de Seus4:** PF_SARLAFTADM

- **Ejemplo Request: **/sarlaftbackweb/salariosminimos?fechaInicial=01-10-2024&fechaFinal=24-10-2025

**Ejemplo Json Response:**

```json
[
    {
        "id": "3f61e06c-d84c-46fe-b954-637775aa0b3c",
        "valor": 1300000.0,
        "feCreacion": "2024-11-12T19:05:52.855+00:00",
        "feActualizacion": "2024-11-12T19:05:52.855+00:00",
        "usuario": "IMPMASIVOS",
        "estadoRegistro": "ACTIVO"
    },
    {
        "id": "ed992e49-6cf0-468a-a73c-ebfebdf08d69",
        "valor": 1300000.0,
        "feCreacion": "2024-11-07T20:00:05.295+00:00",
        "feActualizacion": "2024-11-12T19:05:52.856+00:00",
        "usuario": "IMPMASIVOS",
        "estadoRegistro": "INACTIVO"
    }
]
```
