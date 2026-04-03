# Desmarcar cliente peps

> **Fuente Confluence:** [Desmarcar cliente peps](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2968715399)
> **Última modificación:** 2022-11-02 — versión 2
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Servicio que permite desmarcar a un cliente peps, es decir, usando el query `Clients.client.uncheckPEP`.
- **Endpoint:** `/sarlaftbackweb/clientes/peps/desmarcar`
- **Perfil de Seus4:** `PF_SARLAFTADM`
- **Ejemplo Json Request:**

```json
{
    "tipoDocumento": "C",
    "numeroDocumento": "18762181"
}
```

- **Ejemplo Json Response:**
  - La desmarcación del cliente PEP se ha realizado exitosamente. Notifique al negocio que debe generar una evaluación nuevamente.

- **Dependencias:**
  - Services bus
