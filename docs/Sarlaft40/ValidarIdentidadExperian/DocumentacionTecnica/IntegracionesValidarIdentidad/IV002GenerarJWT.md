---
title: "IV002: Generar JSON WEB TOKEN seguridad IdentityValidator"
confluence_id: 2464088065
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2464088065"
last_modified: "2021-10-23"
author: "5df7c7d29a14250cb69eb76d"
version: 4
---

# IV002: Generar JSON WEB TOKEN seguridad IdentityValidator

> **Fuente Confluence:** [IV002: Generar JSON WEB TOKEN seguridad IdentityValidator](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2464088065)
> **Última modificación:** 2021-10-23 — versión 4
> **Sección:** [Integraciones - Validar identidad](./index.md)

## 1. Información del servicio

Este servicio permite generar un JSON WEB TOKEN de seguridad para acceder a los servicios expuestos por el microservicio de validador de identidad (IdentityValidatorMs).

## 2. Requerimientos Funcionales del Proceso

### Headers

| **Header** | **Descripción** | **Obligatorio** |
|---|---|---|
| `X-APP` | Este header es importante y requerido para la generación del token, ya que se genera para la aplicación específica que genera dicho token | SI |

### Campos de Entrada

No requiere datos adicionales de entrada, diferente a el Header `X-APP`, y la autenticación para el consumo de este servicio con SEUS 4

### Campos de Salida

| **Campo** | **Tipo de dato** | **Longitud** |
|---|---|---|
| `token` | String | |
| `aplicacion` | String — Es el nombre de la aplicación enviado en el Header X-APP, **recomendación:** debe ser un nombre corto de aplicación, en mayúscula, por ejemplo **SARLAFT** | |

## 3. Diseño Técnico

### 3.1. Diagrama de componentes

![Diagrama de seguridad token](./attachments/Diagrama_seguridad_token.drawio-20211022-185817.png)

### 3.2. Diseño generar JWT Autenticación/Autorización expuesto por IdentityValidatorMS

**Origen:** Aplicación que requiera obtener un JSON Web Token, para poder consumir los servicios expuestos por el microservicio, por ejemplo SARLAFT

**Destino:** Micro-servicio IdentityValidator

**GET**: `/api/v1/security/token`

Ejemplo de consumo con cURL

```bash
curl --location --request GET 'https://sarlaftapi.dllosura.com/api/v1/security/token' \
--header 'X-APP: SARLAFT' \
--header 'Authorization: Basic XXXXXXXXXXXXXXXXXXX' \
--data-raw ''
```

**Ejemplo de Mensaje ([Importante revisar Estrategia de seguridad en el punto 5](#5-estrategia-de-seguridad)):**

**GET**

DESARROLLO:

`https://sarlaftapi.dllosura.com/api/v1/security/token`

LABORATORIO:

`https://sarlaftapi.labsura.com/api/v1/security/token`

Mensaje de entrada con Headers, ejemplo cURL:

```bash
curl --location --request GET 'https://sarlaftapi.dllosura.com/api/v1/security/token' \
--header 'X-APP: SARLAFT' \
--header 'Authorization: Basic XXXXXXXXXXXXXXXXXXX' \
--data-raw ''
```

Mensaje de salida:

```json
{
    "token": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJJZGVudGl0eVZhbGlkYXRvciIsInN1YiI6IlNBUkxBRlQiLCJpc3MiOiJTdXJhLmNvbSIsImV4cCI6MTYzNDg2MzkwNSwiaWF0IjoxNjM0ODYwMzA1fQ.R_GXe8He8TMQsXhTsf26u9o5zISJrD6uFiak2dbrp-4",
    "aplicacion": "SARLAFT"
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

- Uso de SEUS 4 (Ambiente de desarrollo y laboratorio se puede autenticar con usuario nombrado impmasivos o con token de sesión SEUS 4)
