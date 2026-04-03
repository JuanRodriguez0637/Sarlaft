# Problemas con el link de validación de identidad

> **Fuente Confluence:** [Problemas con el link de validación de identidad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5174788164)
> **Última modificación:** 2025-12-01 — Antiguo usuario (Deleted) · versión 2
> **Sección:** [Documentación de Incidentes](./index.md)

## Requisitos previos

Para diagnosticar y solucionar problemas relacionados con el link de validación de identidad, es necesario:

- [**Acceso a los índices de Splunk**](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3641311258) para consultar trazas y logs.
- **Acceso a la base de datos de Producción** para validar parametrizaciones.
- **Acceso a la VPN** para conectarse a los sistemas internos.

## Casos detectados

Hasta el momento se han identificado dos escenarios:

1. **Ramo no parametrizado en la base de datos**
   - El error ocurre cuando el ramo asociado al proceso no está configurado correctamente en la base de datos.

2. **Token expirado**
   - El link de validación falla porque el token de seguridad ha caducado.

## Contextualización

Para entender cómo diagnosticar y resolver estos casos, se anexa un video explicativo:\
[**Video explicativo problemas con la url de validación de identidad.**](https://suramericana.sharepoint.com/sites/MESA7-CALIDADDEINFORMACIN/_layouts/15/stream.aspx?id=%2Fsites%2FMESA7%2DCALIDADDEINFORMACIN%2FShared%20Documents%2FGeneral%2FProyecto%20SARLAFT%204%2E0%2FDocumentacionDesarrollo%2FSoluci%C3%B3n%20de%20INC%2FProblemasUrlValidacionIdentidad%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eedd77bc6%2Dc2c9%2D434e%2D9cb9%2Dae14c0bd1dce)
