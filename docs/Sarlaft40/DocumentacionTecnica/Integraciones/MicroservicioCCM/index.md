# Microservicio - CCM

> **Fuente Confluence:** [Microservicio - CCM](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2345730088/Microservicio+-+CCM)
> **Última modificación:** 2022-06-29 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 6
> **Sección:** [Integraciones](../index.md)

**Objetivo:** Solicitar a CCM a través de la cola de rabbit, el envió de una notificación a través de los distintos medios parametrizados en cada comunicación.

**Manual de integración CCM:** [Manual de Integración asíncrona con CCM](https://segurosti.atlassian.net/wiki/spaces/EPA/pages?title=Manual%20de%20Integraci%C3%B3n%20as%C3%ADncrona%20con%20CCM)

**Información viasTrafficProps:**

| **codigoAplicacion** | 9082 | 9082 | 9082 | 9082 | 9082 | 9082 |
| --- | --- | --- | --- | --- | --- | --- |
| **descripcionProceso** | SARLAFT | SARLAFT | SARLAFT | SARLAFT | SARLAFT | SARLAFT |
| **descripcionSolucion** | * | * | * | * | * | * |
| **descripcionOperacion** | ACTUALIZACIONPENDIENTE | ACTUALIZACIONASESORES | CONFIRMACIONACTUALIZACION | VINCULACIONNUEVA | VALIDACIONIDENTIDAD | ACTIVACION |
| **compania** | TRANSVERSAL | TRANSVERSAL | TRANSVERSAL | TRANSVERSAL | TRANSVERSAL | TRANSVERSAL |
| **procesoSura** | ADMINISTRACION RIESGOS DEL CLIENTE | ADMINISTRACION RIESGOS DEL CLIENTE | ADMINISTRACION RIESGOS DEL CLIENTE | ADMINISTRACION RIESGOS DEL CLIENTE | ADMINISTRACION RIESGOS DEL CLIENTE | ADMINISTRACION RIESGOS DEL CLIENTE |

**Mapeo de campos de todas las comunicaciones: **

[Mapeo de campos Sarlaft_V04.xlsx](./attachments/Mapeo de campos Sarlaft_V04.xlsx)

## Páginas hijas

| Página | Descripción | Última modificación |
|--------|-------------|---------------------|
| [Configuración Ambiente - Microservicio CCM](./ConfiguracionAmbiente.md) | **Requisitos** | 2025-10-30 — Diana Muñoz |
| [Estructura Proyecto - Microservicio CCM](./EstructuraProyecto.md) | El microservicio sarlaftccm está construido a partir del generador de legos de Sura, se basa en | 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) |
| [Integración Activación Vinculación Nueva - CCM](./IntegracionActivacionVinculacionNueva.md) | **Objetivo**: | 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) |
| [Integración Reclamaciones - CCM](./IntegracionReclamaciones.md) | **Objetivo**: | 2022-07-12 — Alejandra Zuleta Gonzalez (Unlicensed) |
| [Función Validación de Identidad - CCM](./FuncionValidacionIdentidad.md) | **Mensaje de salida:** | 2021-09-01 — Deivid Harritson Urrego Carvajal |
| [Función Vinculación Nueva - CCM](./FuncionVinculacionNueva.md) | **Mensaje de salida:** | 2021-09-01 — Deivid Harritson Urrego Carvajal |
| [Función Actualización Pendiente - CCM](./FuncionActualizacionPendiente.md) | **Mensaje de salida:** | 2021-09-01 — Deivid Harritson Urrego Carvajal |
| [Función actualizaciones pendientes de los clientes (Asesor) - CCM](./FuncionActualizacionesPendientesAsesor.md) | **Mensaje de salida:** | 2021-09-01 — Deivid Harritson Urrego Carvajal |
| [Función Confirmación Actualización - CCM](./FuncionConfirmacionActualizacion.md) | **Mensaje de salida:** | 2021-09-01 — Deivid Harritson Urrego Carvajal |
| [Función Notificación Póliza Masiva - CCM](./FuncionNotificacionPolizaMasiva.md) | **Mensaje de salida:** | 2022-02-24 — Johnathan Monsalve Bello (Unlicensed) |
| [Configuración HealtchCheck con librería actuator - CCM](./ConfiguracionHealthCheckCCM.md) | Este nuevo servicio web de healthCheck permite evaluar las conexiones principales del microservicio ... | 2024-04-04 — Diana Muñoz |
