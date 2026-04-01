# Front

> **Fuente Confluence:** [Front](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1985511647)
> **Última modificación:** 2024-05-16 — Santiago Valencia Ochoa (Unlicensed) · versión 3
> **Sección:** [Front](./index.md)

## Contenido

- [Diseño MonoRepositorio.](DisenoMonoRepositorio.md)
- [Configuración ambiente](ConfiguracionAmbiente/index.md)
  - [Configuración Ambiente - Pasos importantes](ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md)
- [Despliegue](Despliegue.md)
- [Despliegue con Plantillas](DespliegueConPlantillas.md)
- [Errores](Errores/index.md)
  - [error:0308010C:digital envelope routines::unsupported](Errores/ErrorDigitalEnvelopeRoutines.md)

---

Versión Angular CLI Actual: `12.8.18`

El proyecto Front de SARLAFT 4.0 está construido sobre un prototipo  de aplicación Angular con el enfoque de ser implementado como un Web Component.

**Web Component:**

La definición de elementos reutilizables es ampliamente utilizada en frameworks de javascript como React, Angular o Vue. Sin embargo, como cada framework usa un estándar diferente, hace difícil la reutilización de  fragmentos de código en uno u otro aplicativo construido en dichos frameworks. Un ejemplo es el querer utilizar un datepicker construido en React en un aplicación Angular.

 Los web components solucionan este problema dado que son elementos HTML reutilizables que se construyen de manera de que sean compatibles con cualquier framework, dado que están construidos principalmente en javascript.

Los web components “los componentes web son bloques de código que encapsulan la estructura interna de elementos HTML, incluyendo CSS y JavaScript, permitiendo así que el código se pueda volver a usar como se quiera en otras webs y aplicaciones.”

**SARLAFT como Web Component: **

El proyecto base para la construcción de SARLAFT como Web Component fue el siguiente: [http://inboggit01.suramericana.com.co:8080/gitbucket/TIDIGITAL/mf-arquetipo](http://inboggit01.suramericana.com.co:8080/gitbucket/TIDIGITAL/mf-arquetipo)

Donde, en la carpeta _src/app_ vamos a construir todo lo relacionado con la lógica de los formularios  y en la carpeta  _src/root _ vamos a visualizar lo que construimos en _src/app _no como una app Angular si no como un Web Component, a root la podríamos denominar como aplicación contenedora. El web component se visualizará de la siguiente manera:
![dyd77wnB_LtTFb0_BgOzMp7-uAowYkKt7kD_wGQ_NZW6hi_veLnZZ34pdi9EHuJJ4VZ13K8tBKS_D3QFSA0yZ3foT5dhUAtsigAHsmH5figoHYEsLgzYJMDWzWbqOtFtenSCypNt](img/dyd77wnB_LtTFb0_BgOzMp7-uAowYkKt7kD_wGQ_NZW6hi_veLnZZ34pdi9EHuJJ4VZ13K8tBKS_D3QFSA0yZ3foT5dhUAtsigAHsmH5figoHYEsLgzYJMDWzWbqOtFtenSCypNt)
Los atributos que recibe son los siguientes:

- jsonRequest: este indica el json de entrada que recibe los datos mínimos del tomador para iniciar un proceso SARLAFT.

- token: jwt entregado por la app contenedora de negocio para realizar las peticiones de la api de SARLAFT.

- app: indica el negocio que está consultando al sarlaft.

- tenant: indica los colores/tema que debe tener el formulario de acuerdo al negocio que lo solicite.

- consultado (evento respuesta): es un evento que retorna algo (aún no definido) de acuerdo a lo que se ejecute dentro del componente de SARLAFT.

- class:  indica el estilo que se le va a aplicar al Web Component, siempre tiene la estructura: sarlaft-{{tenant}}-theme

**Assets**

Contiene una los estilos globales de la aplicación en el archivo styles.css y la carpeta Themes que incluye una carpeta de estilos tenant. Estos se crean con base a los Angular Material Themes.
![bPVLyk1G2HFMs8DHp8P2lZhWILNp-7y28zWwbYwdfYG0nnMi2_X-HV5m4PqQQMX36QAMbp8VHyS4GljhR75ucunYJgiAbL2mAoGu_pRPjkGzY7GWdGJZBr4byZPP9xdPcaBe98sY](img/bPVLyk1G2HFMs8DHp8P2lZhWILNp-7y28zWwbYwdfYG0nnMi2_X-HV5m4PqQQMX36QAMbp8VHyS4GljhR75ucunYJgiAbL2mAoGu_pRPjkGzY7GWdGJZBr4byZPP9xdPcaBe98sY)

**Utils/service**

Contiene dos archivos muy importantes:

- StateService:

Contiene el estado de los argumentos que recibimos como atributos como web component.

- Contiene los métodos para actualizar el estado de los atributos y para obtenerlos.

- EventService:

Contiene el evento a emitir como respuesta a la app contenedora.
