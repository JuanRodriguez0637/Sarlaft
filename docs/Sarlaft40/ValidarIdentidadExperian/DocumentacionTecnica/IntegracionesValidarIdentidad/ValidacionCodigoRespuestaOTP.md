---
title: "Validación Código Respuesta OTP - Lista Blanca"
confluence_id: 3969056934
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3969056934"
last_modified: "2024-08-15"
author: "712020:906704eb-807f-48fb-a1ad-4a4906f18183"
version: 4
---

# Validación Código Respuesta OTP - Lista Blanca

> **Fuente Confluence:** [Validación Código Respuesta OTP - Lista Blanca](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3969056934)
> **Última modificación:** 2024-08-15 — versión 4
> **Sección:** [Integraciones - Validar identidad](./index.md)

## Ajuste Regla de Negocio

A continuación se describe el ajuste que permite finalizar el flujo de validación de identidad cuando un cliente pertenece a la lista blanca, este ajuste se hace en el flujo de inicializar OTP de Experian, puesto que ya no se retornara dicho valor en el flujo de cuestionario como se venia haciendo, sino que cuando incluyeron el flujo de OTP, agregaron el mismo `codResultadoOTP` 18 que indicaba en el método de generar cuestionario si se debía excluir o no el cliente de la validación de identidad. Cuando se recibe dicho código no se aplica el flujo de OTP, ni cuestionario y adicional se finaliza de manera exitosa la validación de identidad para el cliente que pertenece a la lista blanca matriculada en Experian, esto implica que la evidencia se debe guardar con un estado exitoso.

A continuación se explica con capturas cronológicas el flujo asíncrono que se tiene para generar la evidencia de EXPERIAN. En las capturas se evidencia los proyectos y métodos de comunicación que enviaban o recibían el llamado de algún microservicio:

## Flujo Validación Identidad Experian

El campo clave es el `codigoEstadoValidacion` o `validationStatusCode` que son los que estan en el metodo `homologarRespuesta` del front. Tener en cuenta que aparentemente es el front quien está manejando esta lógica de negocio o toma la decisión de continuar o no con el proceso de validación de identidad.

### 892-validadorcliente_identidad-ms

![Flujo MS - Paso 1](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfd5-EDeqLPSIf86-Kw-kROBPnowh03zkzmbzlOfQITpY-C07aSw3LIgFXLAx53VMwU8E0pqdnDffFc4Ho6mck2VX1DcvmahBnZd-XFwzJeK0aETLwEyaP5torJTg79xeBm_eJndbAgbOtJvpC4m-3T8I2V?key=JJUe7q1iqM2zZZVAvQjHlA)

### 892-validadorcliente_identidad-fr

![Flujo FR - Paso 1](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfohcEAVQAEd0-4e9m005UVGG4Gs3qRktKYp2TDc39ztEMWTSUtNlA0UTeRIyzv_p5IxtOf4R70PQYBv9XEDE5PJ2L8GULe0qrLkmQXTC1lg8lYABOdTfQ5vttmr-If17VhikB1gji7DUjNrDAzKPMTozAk?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo FR - Paso 2](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe4ExTQ8AJdzUJoE38JqcrkPXnXC4ALwBLdKqset0m2OpqPjJIsr1lLq62_l7nEKmrS_c59E8o6v5uly-vap98Br2Cx7yEUmGGXjn4iBsdlxqFO8b6THfiXTg3NWv3s9n_bJa6-57vOvJXImBVJ3iOf24sk?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo FR - Paso 3](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcBwKqnJ9ESeRDo5bCWw2UU1Nd6S9PUiUAOX1IlODRAzDczWlrvbv1XSTdtYJQVRn56a5MTPCv6NFDkDqSrJJODJDcDBDLLrGFPGaVYoFbVta2nI-lOK_M4uiWk85e92kbaOi3yGIWoW54ZmHAIdOPKEJfy?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo FR - Paso 4](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdx4Hv3d--VuHQFCoiuqbxh9XqhsAnLXlZkSMB-6gHcWLwsLtxPynTBAU1Jx2iydZC5DCKwDrzHnGfjYa3zz7KnyLUw90M66g1N8OaJHOofK6m2lOcDeZVNSLR4CLn2CAvjX-fYsMfxRzsjoQwk2C_sCpUR?key=JJUe7q1iqM2zZZVAvQjHlA)

### 892-validadorcliente_identidad-ms

![Flujo MS - Paso 2](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZ2DBX4cL2qEykZyHq4g5eWmoRc0zgw2spZp8yxx7oLiQEa1nDB3oB8cSp1xCZhIrXxxLtaL4kFWGlonBDy8k6L1l6tUi3MmXtnVwUUNu4Ik33Z4iy212m1gejXQ1jusbf4-D2sGnpNpHAML5UU2OnfLw6?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo MS - Paso 3](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfilz9RL33ZpcI9WyVWv1gVqh_Xk0sBItP9NAZg_Gtq_Ezvh0XtcJLcQ635Enl3dI032wCdbjdglRpHjEOqjQDFiXCRPLOuUjiUUtj0qBR7_teu1PlKOFuiifdV-qJX6meOS1GVFTrsWrnzGwuMmlaY3S2F?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo MS - Paso 4](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSa9wWgN_mJUeWan7ArOsamfeMozJxXqAdCqFXaH0s8XbqSXHFxVpxkzyk6AY3lH8pReRGfWSFqCyaNfnLdpYYeUsgDCznIwmXocfQztRQRbeKdd-DmxB6aGkOCPOaxuSpkN7g95Jpt5ukqUogYkxaA_4?key=JJUe7q1iqM2zZZVAvQjHlA)

### 892-sarlaft-function_identity-mi

![Flujo MI - Paso 1](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf4hoxkIXeB3luA0sb9dfMDyvzN2J88oD36KSlxmLNKiyzSpbYyyj0CJLjQ3rchExzLLd2C1c8AUq4lXHjIepda7CgO-r3gg9oqxVJOD3ecwNoOO_uxUWJMXzfokJ4fJbg2RgW1kLwUZTt5goXBPdIJc2fX?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo MI - Paso 2](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe5qEx0J4I4lR9NxhuLsPfbWdWp0X3fZteJ9NLuk_VuAZyQf3q8aMckVYzXTyQWwY1P4B-iMrwu0JiDxJxzvnR44AVa7e8gqAViaS2UDy2-1KwQnwasP2fi5qL7hfzSZVJAj5MNAegCiIXkJy9g03TdLiD5?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo MI - Paso 3](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfVzP3_pJQcpVIboXbpBz3KMO53AbfBS_vOVnOmL-wst_vZB-BM4hJo_z9QPRDb0ruBYYs4R_iDwCtYZkaxbNqxTZu3gpXv8bmuVcAXEs_Z4FH4h02JleW9JXhFiE5Hr7LthwnxNezwhRujPLtPES1n64QO?key=JJUe7q1iqM2zZZVAvQjHlA)

### 892-sarlaft-api-ms

Del paso anterior se recibe es solo el campo `estadoValidacion` y no el `codigoEstadoValidacion`

![Flujo API - Paso 1](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcdOMhZzeAto5RxqnCjr_sMT093_L1Nk4Ae4bNqG1O9ya_AQ8XroCOH7O1Xb7R_JSom8GrJ6-_C9kn3wWAu6DofOYMmQBpMDLNIWAAX2dED2LQwLvSbFz-PDPxiG1xykYY9_qBL0RfqT-cmBloNkc-vFrvc?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo API - Paso 2](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfmJ0w4KmLgtdXmKj7pD2jNIi--n6Tor2KE1CWRAULtMuoysWm9GWaaz9sTeI9KgyFBwHDJ_egHaYIBlzR2q4WlJUpIv3f_QNme8zJG5GLcwEDvy1kCTe5Z1j5091IcoFN2St0o_23xvRqFdqarbP0OZtTe?key=JJUe7q1iqM2zZZVAvQjHlA)

![Flujo API - Paso 3](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe7-78KIOsAI04cUuVFZ6ERwMuxBdeUL7SBwqUd5MhLQO4SIS0-mVeTczxSPb578hb0-Qx9JeM4_7Y9hkbpT_CYD__sHRv88lkOrV7gmO2AkyKVmPznxE4-NLjn2MkWM_F-yafL3UlJfaCjtb4btz8twZmv?key=JJUe7q1iqM2zZZVAvQjHlA)

Se adjunta enlace a la historia de usuario 588343 asociada a esta validación, donde se evidencian los proyectos impactados y pull requests para conocer detalladamente los cambios efectuados en el código:

[https://dev.azure.com/SuraColombia/Portafolios/_workitems/edit/588343](https://dev.azure.com/SuraColombia/Portafolios/_workitems/edit/588343)

---

## Página relacionada

[IV005: Validación de Identidad - Iniciar y Generar OTP](./IV005IniciarGenerarOTP.md)
