---
title: "Validación por OTP"
confluence_id: 3288957228
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3288957228"
last_modified: "2023-08-09"
author: "632dd1a5234d44d406d0f129"
version: 2
---

# Validación por OTP

> **Fuente Confluence:** [Validación por OTP](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3288957228)
> **Última modificación:** 2023-08-09 — versión 2
> **Sección:** [Front (Web Component)](./index.md)

Una vez realizada la validación de identidad de la persona de forma exitosa se continúa con el proceso de [Iniciar y Generar OTP](../IntegracionesValidarIdentidad/IV005IniciarGenerarOTP.md). En este proceso se valida la información entregada con los datos registrados en Experian para la persona y si coinciden los datos (número del celular con persona) genera un código OTP el cuál es enviado al celular ingresado.

Esta validación se realiza en el componente `src\app\routes\validar-identidad\generar-otp\generar-otp.component.ts` del proyecto [892-validadorcliente_identidad-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-validadorcliente_identidad-fr)

![image-20230809-214903.png](./attachments/image-20230809-214903.png)

En este proceso de validación pueden presentarse los siguientes escenarios:

## Escenarios

### 1. Coincidencia de la información entregada con los datos registrados en Experian.

En este caso tenemos que el json de la respuesta del servicio tiene la propiedad `estado` con el valor de **true.** El código ha sido enviado exitosamente al número de celular de la persona y se continua con el paso 3 del flujo el cual corresponde a Ingresar OTP.

![image-20230809-215034.png](./attachments/image-20230809-215034.png)

### 2. NO coincidencia de la información entregada con los datos registrados en Experian.

En este caso tenemos que el json de la respuesta del servicio tiene la propiedad `estado` con el valor de **false.** A continuación se valida que el valor de la propiedad `codResultadoOTP` sea alguno de los siguientes códigos:

3 → Validación OTP no exitosa, no hay coincidencia en los datos registrados del usuario

5 → No se generó validación por OTP

6 → Validación OTP expirado

![image-20230809-215802.png](./attachments/image-20230809-215802.png)

Si el `codResultadoOTP` es 3, 5 o 6 se continua con el paso del flujo correspondiente a cuestionario.

En este paso del flujo se debe tener en cuenta el tema de la parametría y si la persona se encuentra en [lista blanca](./ListaBlanca.md).

### 3. Validación fallida.

En este caso tenemos que el json de la respuesta del servicio tiene la propiedad `estado` con el valor de **false** y que el `codResultadoOTP` no es ni 3, ni 5 ni 6. En esta situación la validación queda como fallida y finaliza el flujo.
