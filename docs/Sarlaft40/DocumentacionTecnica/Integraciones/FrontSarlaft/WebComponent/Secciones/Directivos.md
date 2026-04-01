# Directivos

> **Fuente Confluence:** [Directivos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2523136072/Directivos)
> **Última modificación:** 2021-12-06 — Deivid Harritson Urrego Carvajal · versión 1
> **Sección:** [Secciones (pantallas)](./index.md)

Se agrega la sección de directivos a la aplicación de webcomponent, en donde, se mostrarán cada una de las pestañas de acuerdo al tipo de empresa seleccionada.

Para hacer uso del webcomponent, se requieren los siguientes campos:

```
@Input() token: string (jwt);
@Input() app: string (aplicacion con la que fue creado el jwt); 
@Input() request: string; 
@Input() rol: string = 'DIRECTIVOS';
```

El campo request es de tipo string, sin embargo, este debe tener la forma de un JSON valido, con los siguientes campos

```
{
  idEvaluacion: string
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

Los codigo de respuestas, se detallan en la sección [Integración](../Integracion.md)
![TIPO_EMPRESAS.png](./attachments/TIPO_EMPRESAS.png)![PYMES.png](./attachments/PYMES.png)![SAS.png](./attachments/SAS.png)![SIN ANIMO DE LUCRO.png](./attachments/SIN ANIMO DE LUCRO.png)![CONSORCIO O UNION TEMPORAL.png](./attachments/CONSORCIO O UNION TEMPORAL.png)
