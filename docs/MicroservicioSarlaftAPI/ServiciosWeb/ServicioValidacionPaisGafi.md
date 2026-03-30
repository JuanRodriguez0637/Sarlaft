# Servicio Validación País Gafi

**Fuente Confluence:** [Servicio Validación País Gafi](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2314404003)
**Sección:** [Servicios Web](../index.md)

---

- **Objetivo:** Permite consultar a partir de un código de país (catalogo PAISES modelo de clientes) si este es gafi (gafi en true/false) y si es bloqueante o no en el proceso de sarlaft (bloqueante en true/false). Devuelve en su respuesta el campo.
- **Endpoint:** /sarlaftserv/gafi/validate
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

[`jsonEntrada.json`](./ServicioValidacionPaisGafi/jsonEntrada.json)

- **Dependencias:**
  - Base de Datos Saralft
