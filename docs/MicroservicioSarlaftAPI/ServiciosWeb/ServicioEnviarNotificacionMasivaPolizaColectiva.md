# Servicio Enviar Notificación Masiva Póliza Colectiva

**Fuente Confluence:** [Servicio Enviar Notificación Masiva Póliza Colectiva](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2587557930)
**Sección:** [Servicios Web](../index.md)

---

- **Descripción Técnica:** Servicio http POST Asíncrono.
- **Objetivo:** Servicio para validación de información de cliente y envío de notificaciones para diligenciamiento de formulario.
- **Endpoint:** /sarlaftserv/massiveform/justification/save
- **Ejemplo de Json Request:**

[`RequestEnviarNotificacionMasivo.json`](./ServicioEnviarNotificacionMasivaPolizaColectiva/RequestEnviarNotificacionMasivo.json)

- **Ejemplo de Json Response:**

```json
{
    "actualizado":true
}
```

- **Dependencias:**
  - Base de datos Sarlaft
  - Función CCM

- **Ejemplo Postman (cambiar url por el indicado arriba):**

[`Enviar Notificacion Masivo.postman_collection.json`](./ServicioEnviarNotificacionMasivaPolizaColectiva/Enviar%20Notificacion%20Masivo.postman_collection.json)
