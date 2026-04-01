# Apoderado

> **Fuente Confluence:** [Apoderado](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2525134892/Apoderado)
> **Última modificación:** 2021-12-07 — 603e455a6a01a30069f1cf29 · versión 2
> **Sección:** [Secciones (pantallas)](./index.md)

Para hacer uso del webcomponent sección apoderado, se requieren los siguientes campos:

```
@Input() token: string (jwt);
@Input() app: string (aplicacion con la que fue creado el jwt); 
@Input() request: string; 
@Input() rol: string = 'APODERADO';

```

El campo request es de tipo string, sin embargo, este debe tener la forma de un JSON valido, con los siguientes campos

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

Los codigo de respuestas, se detallan en la sección [Integración](../Integracion.md)
![apoderdo1.png](./attachments/apoderdo1.png)![apoderado2.png](./attachments/apoderado2.png)![apoderado3.png](./attachments/apoderado3.png)![apoderado5.png](./attachments/apoderado5.png)![apoderado4.png](./attachments/apoderado4.png)
