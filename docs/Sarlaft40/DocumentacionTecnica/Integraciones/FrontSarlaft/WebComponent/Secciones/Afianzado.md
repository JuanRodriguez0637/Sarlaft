# Afianzado

> **Fuente Confluence:** [Afianzado](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2523496496/Afianzado)
> **Última modificación:** 2021-12-06 — Deivid Harritson Urrego Carvajal · versión 1
> **Sección:** [Secciones (pantallas)](./index.md)

Para hacer uso del webcomponent sección afianzado, se requieren los siguientes campos:

```
@Input() token: string (jwt);
@Input() app: string (aplicacion con la que fue creado el jwt); 
@Input() request: string; 
@Input() rol: string = 'AFIANZADO';
```

El campo request es de tipo string, sin embargo, este debe tener la forma de un JSON valido, con los siguientes campos

```
{
  idEvaluacion: string,
  sarlaft: Sarlaft[]
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
![AFIANZADO_PJ_SIMPLIFICADO.png](./attachments/AFIANZADO_PJ_SIMPLIFICADO.png)![AFIANZADO_PN_SIMPLIFICADO.png](./attachments/AFIANZADO_PN_SIMPLIFICADO.png)![AFIANZADO_PJ_ORDINARIO.png](./attachments/AFIANZADO_PJ_ORDINARIO.png)![AFIANZADO_PN_ORDINARIO.png](./attachments/AFIANZADO_PN_ORDINARIO.png)![AFIANZADO_PJ_INTENSIFICADO.png](./attachments/AFIANZADO_PJ_INTENSIFICADO.png)![AFIANZADO_PN_INTENSIFICADO.png](./attachments/AFIANZADO_PN_INTENSIFICADO.png)
