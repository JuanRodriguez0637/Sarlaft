# Asegurados

> **Fuente Confluence:** [Asegurados](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2524938289/Asegurados)
> **Última modificación:** 2021-12-06 — 5b9d486096cb052b5f65d629 · versión 2
> **Sección:** [Secciones (pantallas)](./index.md)

Se agrega la sección de asegurados a la aplicación de webcomponent, en donde se mostrarán cada una de las pestañas de acuerdo al tipo persona que se indique.

Para hacer uso del webcomponent, se requieren los siguientes campos:

```code-java
@Input() token: string (jwt);
@Input() app: string (aplicacion con la que fue creado el jwt); 
@Input() request: string; 
@Input() rol: string = 'ASEGURADO';

```

El campo request es de tipo string, sin embargo, este debe tener la forma de un JSON valido, con los siguientes campos

```code-java
{
  idEvaluacion: string
}

```

En donde el sarlaft, corresponde a la información se desea mostrar.

Al momento de completar el formulario se emitirá la siguiente información:

```code-java
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
![ASEGURADO.png](./attachments/ASEGURADO.png)
