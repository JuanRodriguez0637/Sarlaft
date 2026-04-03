# Servicio Finalizar Evaluación

> **Fuente Confluence:** [Servicio Finalizar Evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2903408641)
> **Última modificación:** 2022-09-14 — juan camilo muñoz burgos · versión 2
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite finalizar una evaluación en estado pendiente o pendiente acción manual.

- **Endpoint:** `/sarlaftbackweb/evaluacion/finalizar`

- **Perfil de Seus4:** `PF_SARLAFTADM`

- **Ejemplo Json Request:**

```json
{
    "idEvaluacion":"1c73801a-5986-4f3a-80d7-17cbdcf0b03a"
}
```

- **Ejemplo Response:**

```text
Actualizacionde estado Exitosa con codigo status 200
```

- **Dependencias**:
  - Base de datos de sarlaft.
