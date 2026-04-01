# Comunicar Consulta Listado información asesores

> **Fuente Confluence:** [Comunicar Consulta Listado información asesores](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2888500034/Comunicar+Consulta+Listado+informaci%C3%B3n+asesores)
> **Última modificación:** 2022-09-06 — Edwin Didier Méndez Rojas - Ceiba Software · versión 2
> **Sección:** [Microservicio Asesores](./index.md)

- **Objetivo:** comunicar la consulta del listado de información de asesores del servicio de redcomercial /asesores/infocontacto por medio un comando en Service bus a la aplicación de sarlaftbatch.
- **Comando Request/Entrada:** Adviser.list.contact **Aplicación:** sarlaftasesores
- **Comando Response/Salida**: Adviser.list.found **Aplicación: **sarlaftbatch

| **Comando Request \| sarlaftasesores** | **Comando Response **(sarlaftasesores)**/Request **(sarlaftbatch) |
| --- | --- |
| ``` { "nmProceso": "12345", "codigosAsesores": [ "4999", "10279" ] } ``` | **nmProceso** | **String** | ``` { "error": "No se enviarios codigos de agentes a consultar", "nmProceso": "12345", "asesores": [ { "nombreAsesor": "TRANSPORTE EL ARRIERO CQLII", "correo": "pruebascoregw@sura.com.co", "celular": "3176353710", "agenteDirecto": false }, { "nombreAsesor": "PINTORES S.A. CQLII II", "correo": "ltvasquez@sura.com.co;glenis@sura.com.co;", "agenteDirecto": true } ] } ``` | **error** | **String** |
| **nmProceso** | **String** |
| **asesores** | **List** |
| **asesores[n].nombreAsesor** | **String** |
| **asesores[n].correo** | **String** |
| **codigosAsesores** | **List** | **asesores[n].celular** | **String** |
| **asesores[n].agenteDirecto** | **boolean** |
