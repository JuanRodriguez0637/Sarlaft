# Start Wc (Webcomponent )

> **Fuente Confluence:** [Start Wc (Webcomponent )](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2544271384/Start+Wc+%28Webcomponent+%29)
> **Última modificación:** 2021-12-20 — 5b9d486096cb052b5f65d629 · versión 1
> **Sección:** [Secciones (pantallas)](./index.md)

Para hacer uso del webcomponent en la sección de START_WC, se requieren los siguientes campos:

```
@Input() token: string (jwt);
@Input() app: string (aplicacion con la que fue creado el jwt); 
@Input() request: string; 
@Input() rol: string = 'START_WC';

```

El campo request es de tipo string, sin embargo, este debe tener la forma de un JSON valido, con el siguiente campo

```
{
  assessment: string,
}

```

En donde el `assessment`, corresponde a la información para consumir el servicio de assessment.

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

Los codigo de respuesta lo pueden encontrar en la sección [Integración](../Integracion.md)
