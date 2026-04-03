---
title: "IV005: Validación de Identidad - Iniciar y Generar OTP"
confluence_id: 2470609076
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470609076"
last_modified: "2024-02-15"
author: "712020:906704eb-807f-48fb-a1ad-4a4906f18183"
version: 10
---

# IV005: Validación de Identidad - Iniciar y Generar OTP

> **Fuente Confluence:** [IV005: Validación de Identidad - Iniciar y Generar OTP](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470609076)
> **Última modificación:** 2024-02-15 — versión 10
> **Sección:** [Integraciones - Validar identidad](./index.md)

## 1. Información del servicio

Este servicio inicializa y genera el código OTP (One Time Password) a través del proceso de Experian llamado Evidente Master.

El consumo de este servicio, valida la información entregada con los datos registrados en Experian para la persona y si coinciden los datos (numero del celular con persona) genera un código OTP el cuál es enviado al celular enviado.

## 2. Requerimientos Funcionales del Proceso

### Campos de Entrada

| **Campo** | **Tipo de dato** | **Longitud** | **Obligatorio** |
|---|---|---|---|
| `aplicacionOrigen` | String | 15 | SI |
| `codigoRamo` | String — Formato: Alfanumérico | 10 | SI |
| `codigoFlujo` | String — Formato: Alfanumérico | 10 | NO |
| `tipoDocumento` | String — **C** - Cédula de ciudadanía, **E** - Cédula de extranjería | 1-2 | SI |
| `numeroDocumento` | String | 3-16 | SI |
| `numeroCelular` | String | 10 | SI |
| `regValidacion` | String | 4-15 | SI |
| `idTransaccionOTP` | String | GUID | NO |

### Campos de Salida

| **Campo** | **Tipo de dato** | **Valores** |
|---|---|---|
| `codResultadoOTP` | String | 1 Validación OTP aprobado, continúa con el proceso; 2 Validación OTP no exitosa; 3 Validación OTP no exitosa, no hay coincidencia en los datos registrados del usuario; 4 Validación OTP en proceso; 5 No se generó validación por OTP; 6 Validación OTP expirado; 7 Error, se está generando doble OTP; 8 Error, se está generando doble verificación de OTP; 99 Error generando código OTP |
| `resultadoOTP` | String | "true","false" |
| `timestampOTP` | String | "true","false" |
| `idTransaccionOTP` | String | "true","false" |
| `requiereCuestionario` | String | "00-99" |
| `numeroValido` | String | "true","false" |
| `rankingReconocer` | String | 1-2 dígitos |
| `estado` | Boolean | true, false |
| `mensajeEstado` | String | Mensaje general del proceso de inicializar y generar OTP |

## 3. Diseño Técnico

### 3.1. Diagrama de componentes

![Diagrama de componentes](./attachments/image-20211019-152619.png)

### 3.2. Diseño Consulta documento identidad en Registraduría expuesto por IdentityValidatorMS

**Origen:** Aplicación que requiera iniciar y generar un código OTP durante una validación de identidad con el proceso Evidente de Experian.

**Destino:** Micro-servicio IdentityValidator.

**POST**: `/api/v1/otp/initializeGenerate`

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "numeroCelular": "3001234567",
    "regValidacion": "123456789",
    "codigoRamo": "041",
    "codigoFlujo": "CV01"
}
```

### 3.3. Diseño Consulta documento identidad en Registraduría expuesto por Data Credito Experian

**Origen:** Micro-servicio IdentityValidator

**Destino:** Data Credito Experian

Se realiza un consumo de un servicio REST de Data Crédito Experian de manera segura, con solicitud de token que debe ser generado previamente.

Adjunta documentación técnica entregada por Experian:

📎 [Manual_Implementacion_WS_Evidente_V5.PDF](./attachments/Manual_Implementacion_WS_Evidente_V5.PDF)

**Ejemplo de Mensaje ([Importante revisar Estrategia de seguridad en el punto 5](#5-estrategia-de-seguridad)):**

**POST**

DESARROLLO:

`https://sarlaftapi.dllosura.com/api/v1/otp/initializeGenerate`

LABORATORIO:

`https://sarlaftapi.labsura.com/api/v1/otp/initializeGenerate`

Mensaje de entrada:

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "numeroCelular": "3001234567",
    "regValidacion": "123456789",
    "codigoRamo": "041",
    "codigoFlujo": "CV01"
}
```

Mensaje de salida:

```json
{
  "codResultadoOTP": "4",
  "resultadoOTP": "true",
  "timestampOTP": "2021/10/13 17:02:34",
  "idTransaccionOTP": "b35143fd-68bb-41c9-be50-8755ea4c3174",
  "requiereCuestionario": "false",
  "numeroValido": "true",
  "rankingReconocer": "1",
  "estado": true,
  "mensajeEstado": "Validación OTP en proceso"
}
```

## 4. Manejo de errores

En cuanto a excepciones, éxito y errores, el micro-servicio maneja los estados de respuesta HTTP:

- 1xx: Respuestas informativas
- 2xx: Peticiones correctas
- 3xx: Redirecciones
- 4xx: Errores del cliente
- 5xx: Errores de servidor

## 5. Estrategia de seguridad

Estándar para todas las integraciones:

- Uso de SEUS 4 (Ambiente de desarrollo y laboratorio se puede autenticar con usuario nombrado impmasivos)
- Adicional se cuenta con otro tipo de Autenticación muy conocida, llamado JSON Web Tokens (JWT), se ha convertido rápidamente en un estándar en la autenticación de aplicaciones. [Ver generación JWT](./IV002GenerarJWT.md)
