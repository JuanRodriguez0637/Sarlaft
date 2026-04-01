# Servicio Iniciar proceso Masivo

**Fuente Confluence:** [Servicio Iniciar proceso Masivo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2120122503)
**Sección:** [Servicios Web](../index.md)

---

- **Objetivo:** Permite iniciar el proceso de evaluación de sarlaft masivo para una póliza colectiva o una póliza individual, que tienen muchos riesgos, y donde se hace necesario dividir los payloads en varias solicitudes.
- **Endpoint:** /sarlaftserv/assessment/massive/start
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

```json
    {
            "totalMensajes": "2",
            "codigoAplicacion": "118",
            "identificadorNegocio": "001"
    }
```

- **Dependencias:**
  - Base de Datos Saralft
  - Aplicaciones Externas.
