# Servicio Proceso Masivo

**Fuente Confluence:** [Servicio Proceso Masivo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2093350926)
**Sección:** [Servicios Web](../index.md)

---

- **Objetivo:** Permite validar el estado del sarlaft de un cliente para un proceso de validación, enviando varios negocios en una sola invocación, el tamaño máximo permitido es de 100 pólizas. Es un proceso asíncrono. Aplica para expedición de pólizas colectivas que tienen muchos riesgos o pólizas individuales con una gran cantidad de riesgos.
- **Endpoint:** /sarlaftserv/assessment/massive
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

[`jsonMasivo_100.json`](./ServicioProcesoMasivo/jsonMasivo_100.json)

- **Dependencias:**
  - RabbitMQ Sarlaft
  - Genera el evento Sarlaft.batch.start
