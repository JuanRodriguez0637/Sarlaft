# Servicio Matricular Entidad

> **Fuente Confluence:** [Servicio Matricular Entidad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2928377889)
> **Última modificación:** 2022-10-03 — Johnathan Monsalve Bello · versión 2
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite matricular entidades en la base de datos, las cuales tienen los\
  datos asociados a tipo de entidad, razón social y los datos básicos de la persona\
  o empresa.

- **Endpoint:** `/sarlaftbackweb/entidades/matricular`

- **Perfil de Seus4:** `PF_SARLAFTADMCON`

- **Ejemplo Json Request:**

```json
{
    "tipoIdentificacion": "C",
    "numeroIdentificacion": "1022385109",
    "tipoEntidad": "BOLSA",
    "razonSocial": "Emp",
    "tipoPersona": "N",
    "primerNombre": "David",
    "segundoNombre": null,
    "primerApellido": "Soto",
    "segundoApellido": null
}
```

- **Ejemplo Json Response:**

```text
Se ha matriculado exitosamente la entidad
```
