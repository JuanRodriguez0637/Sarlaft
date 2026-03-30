# Servicio omitir formulario

**Fuente Confluence:** [Servicio omitir formulario](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2612297802)
**Sección:** [Servicios Web](../index.md)

---

- **Objetivo:** Permite omitir el diligenciamiento del formulario en el caso que una evaluación sarlaft se identifique con un determinado producto parametrizado. En ese ese caso el llenado del formulario es opcional para el cliente. Si el producto no es apto para usar el servicio se denegará su uso.
- **Endpoint:** /sarlaftserv/form/skip
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

```json
{
    "evaluacionId": "8ac8063f-b4d8-43c9-8ce1-cca031fda67c"
}
```

**Response:**

200 OK
400 Bad Request

**Dependencias:**

- Base de datos de sarlaft
- SarlaftWebhook
