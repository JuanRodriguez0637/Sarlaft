# Interfaces de Servicio

> **Fuente Confluence:** [Interfaces de Servicio](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070133)  
> **Última modificación:** 2021-07-29 — Diana Muñoz · versión 6  
> **Sección:** Sarlaft 4.0 → Documentación Técnica

Documentación de las interfaces de Servicio del Sarlaft 4.0 para su comunicación con todos los aplicativos de Suramericana.

Proyectos Postman de ejemplo de consumo — Ambiente Desarrollo y Laboratorio.

Se ajusta request del ws de assessment, se incluye ejemplo de consumo del ws de catálogos.

## Proyectos Postman

| Archivo | Descripción |
|---------|-------------|
| [`Sarlaft 4.0 DLLO.postman_environment.json`](./attachments/Sarlaft%204.0%20DLLO.postman_environment.json) | Environment Postman — Ambiente Desarrollo |
| [`Sarlaft 4.0 LABO.postman_environment.json`](./attachments/Sarlaft%204.0%20LABO.postman_environment.json) | Environment Postman — Ambiente Laboratorio |
| [`Sarlaft 4.0 Interfaces.postman_collection.json`](./attachments/Sarlaft%204.0%20Interfaces.postman_collection.json) | Colección Postman de interfaces Sarlaft 4.0 |

## Sub-secciones

| Página | Descripción | Última modificación |
|--------|-------------|---------------------|
| [Descripción de Interfaces Principales](./DescripcionInterfacesPrincipales/index.md) | Descripción de las interfaces principales: Validar Sarlaft, Almacenar Evidencias, Consultar Formulario Sarlaft, WebHook, Web Component | 2025-11-07 |
| [Interfaz Procesos Masivos](./InterfazProcesosMasivos/index.md) | Diseño asíncrono para validación masiva de hasta 100 pólizas mediante mensajería RabbitMQ | 2021-08-18 |
| [Escenario de Validación Sarlaft en varios request](./EscenarioValidacion/index.md) | Escenario de validación para WeSura, SuraEnLinea y algunos productos de Salud | 2021-05-05 |
| [Interfaz de Consulta de Estado Sarlaft](./InterfazConsultaEstadoSarlaft/index.md) | Interfaz de consulta para cotizadores y `Policy Center` que no implementan el patrón WebHook | 2021-05-05 |
| [Evaluación para Reclamaciones](./EvaluacionReclamaciones/index.md) | Proceso de assessment para la operación de reclamaciones `RE` | 2021-09-22 |
