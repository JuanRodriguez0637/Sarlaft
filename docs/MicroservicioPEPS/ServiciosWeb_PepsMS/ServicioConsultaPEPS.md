# Servicio Consulta PEPS

> **Fuente Confluence:** [https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1813971266](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1813971266)
> **Fecha extracción:** 2026-03-30

- **Objetivo:** Permite consultar si un cliente tiene marca peps. En caso de que la base de datos de PDN presente indisponibilidad para consultar la marcación de peps, el servicio valida la información en la BD de PDNHA a través de la vista MPEP_PREGUNTAS_PEP, garantizando asi la disponibilidad de la consulta.

- **Endpoint:** /pepsserv/pep/check

- **Perfil de Seus4: **PF_CONSUMSERVPEPSAPI

- **Ejemplo Json Request:**

[/wiki/download/attachments/1813971266/request_checkpeps.json?version=1&modificationDate=1616785571405&cacheVersion=1&api=v2](/wiki/download/attachments/1813971266/request_checkpeps.json?version=1&modificationDate=1616785571405&cacheVersion=1&api=v2)

- **Dependencias:**

Base de Datos PDN y PDNHA

## Ejemplos JSON (Adjuntos)

### `request_mark.json`

```json
{
  "requestDni": "C43260574",
  "application": "118",
  "client": {
    "documentType": "A",
    "documentNumber": "8001973840",
    "firstName": null,
    "secondName": null,
    "firstSurname": null,
    "secondSurname": null
  }
}
```

### `request_checkpeps.json`

```json
{
  "dni": "A8001973840"
}
```
