# Servicio cancelar evaluación

> **Fuente Confluence:** [Servicio cancelar evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2896625843)
> **Última modificación:** 2022-09-14 · versión 4
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Cambia el estado de una evaluación y sus correspondientes sarlafts a estado CANCELADO.

- **Endpoint:** /sarlaftbackweb/evaluacion/cancelar

- **Perfiles de Seus4: **PF_SARLAFTADM_EMPLE_BANCASEG, PF_SARLAFTADM_EMPLE_CANALES, PF_ASESOR_ASIST_VIRTUAL, PF_SARLAFTADM_EMPLE_ASESOR, PF_SARLAFTADM

- **Ejemplo Json Request:**

```json
{
    "idEvaluacion": "203e747d-5ff0-4f08-bbc1-143a2f7c2bbd"
}
```text

- **Ejemplo Json Response:**

```text
ok
```

**Nota: **Solo se pueden cancelar evaluaciones con estados: PENDIENTE y PENDIENTE_ACCION_MANUAL

- **Dependencias**:

Base de datos de sarlaft.
