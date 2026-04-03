# Solicitud de request and respose

> **Fuente Confluence:** [Solicitud de request and respose](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5174689830)
> **Última modificación:** 2025-12-01 — Antiguo usuario (Deleted) · versión 2
> **Sección:** [Documentación de Incidentes](./index.md)

### Permisos requeridos

Para manejar los índices necesarios, el perfil requerido es:\
`GS_SR_SPLUNK_EGV_TI`

La solicitud de permisos se realiza en el siguiente enlace:\
[Guía para la solicitud de permisos de perfil en Splunk](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3641311258) (leer la última parte).

### Acceso a Splunk

Para realizar consultas, se debe acceder a Splunk en los siguientes entornos:

- **Laboratorio:**\
  <https://holmeslab.suramericana.com.co/en-GB/app/1149-gestor_tareas/search>

- **Producción:**\
  <https://sherlock.suramericana.com.co/en-GB/app/cargamasivap8/search>

### Índices y consulta en Splunk

Para el proceso de request and response, se utiliza el siguiente índice:

```text
index="idx_identityvalidator_*" message="*número de identificación*"
```

**Parámetros:**

- `index`: `idx_identityvalidator_*`
- `message`: Contiene el número de identificación que se desea consultar.

### Formato del mensaje y canal de envío

Una vez obtenida la información, se debe enviar por **chat privado** al encargado de gestionar las solicitudes, usando el siguiente formato:

```text
Nombre Completo Tipo de ID: Número de ID
Request:
Response:
```

Lo más importante en la respuesta es el **código de respuesta (**`respuesta="09"`**)**, ya que indica el resultado de la validación.\
Los significados de estos códigos se encuentran en el siguiente enlace:\
[Traductor de códigos en Azure DevOps](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-conf?path=%2Fconfigmap%2Ftranslator.yml)

Para mayor detalle sobre qué índice utilizar según la necesidad, se recomienda consultar la siguiente página:\
[**Logs de Experian en Splunk**](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3641311258)

Se anexa un video para dar mayor contexto del proceso:\
Video: [respuesta a la solicitud de request and response.](https://suramericana.sharepoint.com/sites/MESA7-CALIDADDEINFORMACIN/_layouts/15/stream.aspx?id=%2Fsites%2FMESA7%2DCALIDADDEINFORMACIN%2FShared%20Documents%2FGeneral%2FProyecto%20SARLAFT%204%2E0%2FDocumentacionDesarrollo%2FSoluci%C3%B3n%20de%20INC%2FRequestResponse%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E64bb93e2%2D542b%2D4ad2%2Da227%2D6a9f293eca5e)
