---
title: "Lista blanca"
confluence_id: 3289284925
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3289284925"
last_modified: "2023-08-09"
author: "632dd1a5234d44d406d0f129"
version: 3
---

# Lista blanca

> **Fuente Confluence:** [Lista blanca](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3289284925)
> **Última modificación:** 2023-08-09 — versión 3
> **Sección:** [Front (Web Component)](./index.md)

Esta funcionalidad tiene como propósito evitar el diligenciamiento del cuestionario de preguntas suministrado por Experian para la validación de identidad, a las personas que la compañía a categorizado como lista blanca en Experian.

Esta validación se realiza en el proyecto [892-validadorcliente_identidad-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-validadorcliente_identidad-fr).

En `src\app\shared\enums\resultado-generacion-cuestionario.ts` se creó la constante con el valor que identifica a una persona en lista blanca (18):

![image-20230809-221952.png](./attachments/image-20230809-221952.png)

En el componente `src\app\routes\validar-identidad\generar-otp\cuestinario.component.ts`, una vez se llama el servicio para [generar cuestionario](../IntegracionesValidarIdentidad/IV007GenerarCuestionario.md) lo primero que se hace es tomar el json de respuesta y se valida el valor de la propiedad `resultado` el cual nos indica si la persona se encuentra categorizada en lista blanca o no:

![image-20230809-222448.png](./attachments/image-20230809-222448.png)

Como resultado de esta validación se pueden presentar los siguientes escenarios:

## Escenarios

### 1. La persona existe en lista blanca

En este caso tenemos en el json de respuesta que el valor de la propiedad `resultado` es 18 (Consulta no autorizada) lo que nos indica que la persona se encuentra en lista blanca y por lo tanto no se le debe generar el cuestionario de preguntas para validar su identidad sino que simplemente el proceso de validación de identidad queda finalizado y exitoso.

### 2. La persona no existe en lista blanca

En este caso tenemos en el json de respuesta que el valor de la propiedad `resultado` es diferente a 18 (Consulta no autorizada) y el valor de la propiedad `estado` es **true,** lo que nos indica que la persona no se encuentra en lista blanca y por lo tanto se le debe generar el cuestionario de preguntas para validar su identidad.

### 3. Validación de intentos permitidos

Este caso ocurre cuando la persona no se encuentra en lista blanca y el valor de la propiedad `estado` en el json de respuesta es **false,** se validan los intentos permitidos para responder el cuestionario de preguntas cada vez que la persona de equivoque al responder el cuestionario.
