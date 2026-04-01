# Tomador

> **Fuente Confluence:** [Tomador](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2526347292/Tomador)
> **Última modificación:** 2021-12-07 — 603e455a6a01a30069f1cf29 · versión 1
> **Sección:** [Secciones (pantallas)](./index.md)

Se agrega la sección de tomador a la aplicación de webcomponent, en donde, se mostrarán cada una de las pestañas (Antes de empezarDatos apoderado, Datos básicos, Datos de ubicación, Relación PEP, Datos financieros, Datos adicionales, SoportesDatos directivos) de acuerdo a los criterios de aceptación de esta HU.

Para hacer uso del webcomponent, se requieren los siguientes campos:@Input() token: string (jwt);@Input() app: string (aplicacion con la que fue creado el jwt); ejemplo: (digital)@Input() request: string; @Input() rol: string = 'TOMADOR';El campo request es de tipo string, sin embargo, este debe tener la forma de un JSON valido, con los siguientes campos

```
{
  idEvaluacion: string,
}

```

En donde el sarlaft, corresponde a la información se desea mostrar.

Al momento de completar el formulario se emitirá la siguiente información:

```
{ 
 idEvaluacion: string, 
 riesgo: ClasificacionForm, 
 codigoResp: WebComponentResponse, 
 messageError: string; 
}
```

El riesgo puede ser: SIMPLIFICADO, ORDINARIO O INTENSIFICADO.

El campo messageError: Solo se mostrará en caso de presentarse un error.

Los codigo de respuestas, se detallan a continuación:

| **Código** | **Descripción** |
| --- | --- |
| ERROR_SECURITY_INVALID_TOKEN | Error de Seguridad Token invalido |
| ERROR_SECURITY_EXPIRED_TOKEN | Error de Seguridad Token expirado |
| ERROR_INTERNAL_NO_PROCESS | Error Interno no controlado |
| ERROR_API_CALL_METHOD | Error emitido cuando la API de Sarlaft no esta disponible o presenta fallas al momento de consumirla. |
| ERROR_POLITICS_SARLAFT | Error cuando se presenta una restricción por politicas de sarlaft (Fallo en los controles, por ejemplo GAFI - Pais de alto riesgo) |
| SARLAFT_SAVE_SUCCESS | La información de Sarlaft se guardo correctamente |
| ERROR_SECURITY_INVALID_PARAM | Parámetros incorrectos enviados al webcomponent |
