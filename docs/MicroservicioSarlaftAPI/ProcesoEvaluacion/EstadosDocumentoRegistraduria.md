# Estados Documento Registraduría - SarlaftAPI

> **Fuente:** [Confluence - Estados documento registraduria](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3902537737/Estados+documento+registraduria)  
> **Página padre:** [Proceso Evaluación - SarlaftAPI](./index.md)

---

## Tabla de Estados

La tabla `CodigoEstadoDocumentoRegistraduria` define cómo se deben interpretar los códigos de estado retornados por la Registraduría al validar un documento de identidad.

| Regla | Descripción | Estado |
|-------|-------------|--------|
| `<30` los códigos menores a 30 que no sean 0, 21 y 12 | `CANCELADA` | FALLIDO |
| `>=30 y <=59` | `NO_EXPEDIDA` | FALLIDO |
| `>=60` los códigos mayores a 60 que no sean 99 | `INDEFINIDO` | FALLIDO |
| Vacío o Null | FALLA TÉCNICA | FALLA TÉCNICA |

---

## Notas

- Los códigos `0`, `21` y `12` (menores a 30) se excluyen de la regla CANCELADA y tienen tratamiento especial.
- El código `99` (mayor a 60) se excluye de la regla INDEFINIDO.
- Un resultado vacío o nulo se considera un error técnico, no un fallo de negocio.
- Esta tabla es usada por el proceso de evaluación para determinar si la validación de identidad con Registraduría fue exitosa o fallida.
