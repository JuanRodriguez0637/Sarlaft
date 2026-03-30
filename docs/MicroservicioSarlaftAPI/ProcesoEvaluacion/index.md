# Proceso Evaluación - SarlaftAPI

> **Fuente:** [Confluence - Proceso Evaluación - SarlaftAPI](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1804861546/Proceso+Evaluaci%C3%B3n+-+SarlaftAPI)  
> **Página padre:** [Microservicio SarlaftAPI](../index.md)

---

## Descripción

Esta sección documenta la lógica interna del proceso de evaluación SARLAFT dentro del microservicio, incluyendo la determinación de estados, comunicación con sistemas externos (P8), y el manejo de procesos masivos.

---

## Subpáginas

| Subpágina | Descripción | Enlace |
|-----------|-------------|--------|
| Determinar Estado Evaluación | Lógica para determinar el estado de una evaluación | [DeterminarEstadoEvaluacion.md](./DeterminarEstadoEvaluacion.md) |
| Proceso Evaluación - Masivo | Proceso de evaluación en modo masivo | [ProcesoEvaluacionMasivo.md](./ProcesoEvaluacionMasivo.md) |
| Comunicación Requisitos | Comunicación de requisitos en el proceso (CrearRequisito / ActualizarRequisito) | [ComunicacionRequisitos.md](./ComunicacionRequisitos.md) |
| Comunicación P8 | Integración con el sistema P8 vía RabbitMQ | [ComunicacionP8.md](./ComunicacionP8.md) |
| Registro de ID documento P8 | Registro del identificador de documento en P8 | [RegistroIDDocumentoP8.md](./RegistroIDDocumentoP8.md) |
| Estados documento registraduría | Tabla de estados del documento de registraduría | [EstadosDocumentoRegistraduria.md](./EstadosDocumentoRegistraduria.md) |
| Herencia Sarlaft API para el SOAT | Ajuste de herencia de evidencias para evaluaciones SOAT | [HerenciaSarlaftAPISOAT.md](./HerenciaSarlaftAPISOAT.md) |

---

## Notas de Implementación

- La lógica del proceso de evaluación se encuentra en la clase abstracta `PrepararEvaluacion.java` del módulo `domain-usecase`.
- El proceso incluye validaciones de identidad vía **Registraduría**, manejo de **formularios** y comunicación con el sistema **P8**.
- Para la herencia de evaluaciones SOAT, ver [Herencia Sarlaft API para el SOAT](./HerenciaSarlaftAPISOAT.md).
