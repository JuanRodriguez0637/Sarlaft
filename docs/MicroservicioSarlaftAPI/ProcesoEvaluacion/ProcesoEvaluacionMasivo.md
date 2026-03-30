# Proceso Evaluación - Masivo

> **Fuente Confluence:** [Proceso Evaluación - Masivo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2332262464)  
> **Última modificación:** 17 ago 2021 — Diana Muñoz · versión 1  
> **Sección:** [Proceso Evaluación - SarlaftAPI](./index.md)

---

## Cuerpo de página

Proceso de evaluación masivo iniciado por mensajería de **RabbitMQ**.

---

## Comentarios de Confluence

### Comentario 1

> **Autor:** juan camilo muñoz burgos  
> **Fecha:** 10 sep 2021  
> **ID comentario:** 2354675961

---

- **Objetivo:** En la plataforma SARLAFT 4.0 se construye la funcionalidad para que se pueda recibir carga masiva de información de clientes y se inicie una evaluación masiva del análisis LAFT.

- **Descripción:** Se recibe el mensaje `"Sarlaft.batch.start"`, el cual espera un objeto JSON que contiene toda la información de las evaluaciones a procesar de forma masiva. Toda vez que se procese la información recibida —exceptuando cuando se solicita una carga por lotes y no se han completado todos los mensajes para finalizar un lote— se envía un mensaje de respuesta `"Assessment.process.evaluated"`, el cual contiene un objeto JSON, al API **SarlaftWebhook**.

- **Mensaje request:** `"Sarlaft.batch.start"`

- **Mensaje response:** `"Assessment.process.evaluated"`

### Adjuntos del comentario

| Archivo | Descripción |
|---------|-------------|
| [`ProcesoMasivoRequest.json`](./attachments/ProcesoMasivoRequest.json) | Ejemplo JSON Request recibido en SarlaftApi |
| [`ProcesoMasivoResponse.json`](./attachments/ProcesoMasivoResponse.json) | Ejemplo JSON Response enviado a SarlaftWebhook mediante RabbitMQ |

### Dependencias

- Base de Datos Sarlaft
- Aplicaciones Externas
- RabbitMQ
- SarlaftWebhook
