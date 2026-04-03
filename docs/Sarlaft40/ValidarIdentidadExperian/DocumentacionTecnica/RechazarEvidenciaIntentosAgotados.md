---
title: "Rechazar evidencia de Experian por intentos agotados"
confluence_id: 4048683013
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4048683013/Rechazar+evidencia+de+Experian+por+intentos+agotados"
last_modified: "2024-09-17"
author: "Brayan Estiven Sepúlveda Quintero"
version: 1
---

# Rechazar evidencia de Experian por intentos agotados

> **Fuente Confluence:** [Rechazar evidencia de Experian por intentos agotados](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4048683013/Rechazar+evidencia+de+Experian+por+intentos+agotados)
> **Última modificación:** 2024-09-17 — Brayan Estiven Sepúlveda Quintero · versión 1
> **Sección:** [Documentación técnica](./index.md)

# Asignación incorrecta de falla técnica

Durante el análisis de código que se hizo para el incidente 6543336 se encontró el siguiente problema, desconozco en el momento quien lo inyectó (eso sí, no fue algo que hayamos manipulado nosotros desde la iniciativa de SOAT Orden Administrativa, ya estaba inyectado en PDN el problema), pero es lo siguiente:

![estadoValidacion](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcyoBa1rCa4QfksYgTHy8vopgpUXDpf3kqJZgJ8nHRZ-Ppro2I4OBHS55K8y3u03IBsMNgPLfroS_8P9IM-J4uxESyYMFxrw1UNo8xbTkWJnJ8FLYW8Mo8J3Ce9QvB6FxCMM048Ikyf5l0PPkrzGxhLWSET?key=4dCTfkzZhQ2YWjk1-iopzA)

Ese `estadoValidacion` se está mapeando a partir del siguiente fragmento de código en el repositorio `892-sarlaft-function_identity-mi` y la clase `ResultadoIdentidadAsyncAdapter`:

![ResultadoIdentidadAsyncAdapter](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdCly7n25m64JhVq_zzhfyvGrDn7ObjocnvZb5K7oVeXMTcalMSVVUhMG7GXQS7Eiig0N9zRtSabxelmMiPdFkPOqPLgF12Ts_9PFkheyVjBOsawCdowXlod2BNN6Lh6dc-bj1jO0xoQd7hzHHWfYNHUXJ0?key=4dCTfkzZhQ2YWjk1-iopzA)

Y justo cuando se hace el mapeo como no coincide el string exactamente debido a que se tienen espacios en blanco en vez de guiones bajos, lo setea como falla técnica, cuando en realidad según esa lógica debería ser fallido y no falla técnica:

![mapeo falla técnica](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeG46G4If2DQy9MjASgh6ISJ_RjHDBGX7n675Y9eK5THgQh-3Ib6079sbQ7C6ilYw2VpPJlgOBanT9M3_kIkbftBGt1HGWZCfxQWy4rLPD9z9gWUN48MFvw0J5L-VqKoQwpKsq5BlYQCR-LgOWqYJL3DCwC?key=4dCTfkzZhQ2YWjk1-iopzA)

Se debería modificar este diccionario para cambiar los espacio en blanco por underlines:

![diccionario](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcW06yD7nSB96Mxm1_jvn3zM9qNyd_8eauQP5l3N6gLQJzWjTMGVyMD4U5Z70f-jX4Hh3UuZN_FSGvAbUbTGzo2ZOf653DbFNNuE04ApeyimR_n8W5W_xdWYiffdwRxy7hXBCc2dffH_ioFY9spWhByGvs?key=4dCTfkzZhQ2YWjk1-iopzA)

Para este nuevo problema se destinó la HU613379:

https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/613379
