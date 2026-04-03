# Servicio Cambiar estado entidad

> **Fuente Confluence:** [Servicio Cambiar estado entidad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2935160848)
> **Última modificación:** 2022-10-07 — Johnathan Monsalve Bello · versión 1
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Descripción:** Servicio que permite cambiar el estado de una entidad (`tsaf_entidad`).

  Cuando se solicita activar una entidad y esta fue creada con una fecha diferente a la actual, se crea un nuevo registro con el fin de guardar la trazabilidad. En caso de que la fecha de creación sea igual a la actual, solo se dejará en null la fecha de baja, dado que de crear un nuevo registro se presentará un error por PK duplicada.

  Los datos permitidos en el request de entrada son:

  - Tipo Entidad: `BOLSA`, `FINASEPEN`, `REGIMEN`, `PASSTHROUGH`
  - Dni: String
  - Activar: Boolean
    - Notas:
      - Para inactivar una entidad se debe enviar el campo `activar` en `false`.
      - Es obligatorio que antes el registro a activar/inactivar exista en la BD tanto el DNI como el tipo de entidad.

- **Endpoint:** `/sarlaftbackweb/entidades/cambiarEstado`

- **Perfil Seus4:** `PF_SARLAFTADM`

- **Ejemplo Request:**

  📎 [request (1).json](<./attachments/request (1).json>)

- **Ejemplo Response:**

  ```text
  La entidad ha sido activada, por favor verifique el nuevo estado: ACTIVO
  ```
