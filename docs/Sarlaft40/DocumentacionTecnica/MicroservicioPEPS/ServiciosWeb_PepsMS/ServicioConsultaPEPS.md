# Servicio Consulta PEPS

> **Fuente Confluence:** [Servicio Consulta PEPS](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1813971266)
> **Espacio:** EPA
> **Última modificación Confluence:** 2021-03-26 | Versión 1
> **Sección:** [Servicios Web - PepsMS](./index.md)

- **Objetivo:** Permite consultar si un cliente tiene marca peps. En caso de que la base de datos de PDN presente indisponibilidad para consultar la marcación de peps, el servicio valida la información en la BD de PDNHA a través de la vista `MPEP_PREGUNTAS_PEP`, garantizando asi la disponibilidad de la consulta.
- **Endpoint:** `/pepsserv/pep/check`
- **Perfil de Seus4:** `PF_CONSUMSERVPEPSAPI`
- **Ejemplo Json Request:**

  [request_checkpeps.json](./attachments/request_checkpeps.json)

- **Dependencias:**
  - Base de Datos PDN y PDNHA

---

## Adjuntos

| Archivo | Descripción |
|---------|-------------|
| [request_checkpeps.json](./attachments/request_checkpeps.json) | Request de ejemplo para consulta PEPS |
| [request_mark_consulta.json](./attachments/request_mark_consulta.json) | Request de ejemplo para marcación (`request_mark.json` original de esta página) |
