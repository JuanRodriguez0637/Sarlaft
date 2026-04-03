---
title: "IV003: Obtener Token Experian"
confluence_id: 2474213387
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2474213387"
last_modified: "2021-11-04"
author: "5addeb242d1bf924e1fbca8c"
version: 4
---

# IV003: Obtener Token Experian

> **Fuente Confluence:** [IV003: Obtener Token Experian](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2474213387)
> **Última modificación:** 2021-11-04 — versión 4
> **Sección:** [Integraciones - Validar identidad](./index.md)

## 1. Información del servicio

Este servicio permite obtener el objeto \<Token\> provisto por Experian necesario para consumir y hacer uso de los demás recursos que proveen.

También se dispone de dos servicios para administrar la cache con el fin de recuperar el valor que tiene almacenado directamente y limpiarla.

## 2. Requerimientos funcionales del proceso

### 2.1 Solicitar Token Experian

#### Headers

| **Header** | **Value** | **Obligatorio** |
|---|---|---|
| `Content-Type` | `application/json` | Si |

#### Campos de Entrada

No requiere datos adicionales de entrada.

#### Campos de Salida

| **Campo** | **Tipo de dato** | **Descripcion** |
|---|---|---|
| `tokenType` | String | Tipo de token |
| `expiresIn` | Long | Tiempo de expiración del Token en segundos |
| `accessToken` | String | Cadena de caracteres correspondiente al Token de acceso |
| `scope` | String | alcance del Token |

### 2.2 Limpiar cache token experian

#### Campos de Entrada

No requiere datos adicionales de entrada.

#### Campos de Salida

| **Campo** | **Tipo de dato** | **Descripción** |
|---|---|---|
| `Response` | String | Success \| Error |

### 2.3 Consulta contenido del cache

#### Headers

| **Header** | **Value** | **Obligatorio** |
|---|---|---|
| `Content-Type` | `application/json` | Si |

#### Campos de Entrada

No requiere datos adicionales de entrada.

#### Campos de Salida

| **Campo** | **Tipo de dato** | **Descripcion** |
|---|---|---|
| `tokenType` | String | Tipo de token |
| `expiresIn` | Long | Tiempo de expiración del Token en segundos |
| `accessToken` | String | Cadena de caracteres correspondiente al Token de acceso |
| `scope` | String | alcance del Token |

## 3. Requerimientos funcionales del proceso

### 3.1 Diagrama de componentes

![Diagrama token Experian](./attachments/experian%20token.png)

### 3.2 Ejemplo de petición y respuesta del servicio

#### 3.2.1 Obtener token experian

URL (Local): `http://local.suramericana.com:8080/api/v1/token`

URL (Desarrollo): `http://sarlaftapi.dllosura.com/api/v1/token`

HTTP Method: GET

**Response**

```json
{
    "tokenType": "Bearer",
    "expiresIn": 14400,
    "accessToken": "eyJraWQiOiItZmtxdlRJbHZnU2NMRHBFVWlEcHpxNHp6VFdyY0wwYklTdFFOc3dSMVhvIiwiYWxnIjoiUlMyNTYifQ...",
    "scope": "expco_evidente_master"
}
```

#### 3.2.2 Limpiar cache token experian

URL (Local): `http://local.suramericana.com:8080/api/v1/token/clear`

URL (Desarrollo): `http://sarlaftapi.dllosura.com/api/v1/token/clear`

HTTP Method: GET

**Response**

```
Success
```

#### 3.2.3 Consulta contenido del cache

URL (Local): `http://local.suramericana.com:8080/api/v1/token/cache`

URL (Desarrollo): `http://sarlaftapi.dllosura.com/api/v1/token/cache`

HTTP Method: GET

**Response**

```json
{
    "tokenType": "Bearer",
    "expiresIn": 14400,
    "accessToken": "eyJraWQiOiItZmtxdlRJbHZnU2NMRHBFVWlEcHpxNHp6VFdyY0wwYklTdFFOc3dSMVhvIiwiYWxnIjoiUlMyNTYifQ...",
    "scope": "expco_evidente_master"
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
