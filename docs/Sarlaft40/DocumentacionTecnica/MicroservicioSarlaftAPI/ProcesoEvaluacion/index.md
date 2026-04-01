# Proceso Evaluación - SarlaftAPI

> **Fuente Confluence:** [Proceso Evaluación - SarlaftAPI](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1804861546)
> **Última modificación:** 2021-03-24 — Diana Muñoz · versión 1
> **Sección:** [Microservicio SarlaftAPI](../index.md)
## Descripción

Sección que documenta la lógica interna del **proceso de evaluación SARLAFT** dentro del microservicio, incluyendo la determinación de estados, comunicación con sistemas externos (P8) y el manejo de procesos masivos.

---

## Sub-páginas

| Sub-página | Descripción | Última modificación |
|------------|-------------|----------------------|
| [Determinar Estado Evaluación](./DeterminarEstadoEvaluacion.md) | Lógica para determinar el estado de una evaluación (FINALIZADO, RECHAZADO, PENDIENTE, etc.) | 17 ago 2021 |
| [Proceso Evaluación - Masivo](./ProcesoEvaluacionMasivo.md) | Proceso masivo vía RabbitMQ — msg request `Sarlaft.batch.start`, response `Assessment.process.evaluated` | 17 ago 2021 |
| [Comunicación Requisitos](./ComunicacionRequisitos.md) | CrearRequisito y ActualizarRequisito vía comandos asíncronos | 20 ago 2021 |
| [Comunicación P8](./ComunicacionP8.md) | Envío de mensaje a la función `appp8` de RabbitMQ al cargar documento | 31 ago 2021 |
| [Registro de ID documento P8](./RegistroIDDocumentoP8.md) | Recepción del ID de documento desde la cola `sarlaft-api` de RabbitMQ | 08 sep 2021 |
| [Estados documento registraduría](./EstadosDocumentoRegistraduria.md) | Tabla de códigos de estado `CodigoEstadoDocumentoRegistraduria` | 22 jul 2024 |
| [Herencia Sarlaft API para el SOAT](./HerenciaSarlaftAPISOAT.md) | Ajuste de herencia de validación de identidad (EXPERIAN) para SEL vs. SOAT SURA | 29 jul 2024 |
