---
title: "IV008: Validación de Identidad - Verificar Cuestionario"
confluence_id: 2470641866
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470641866"
last_modified: "2024-02-15"
author: "712020:906704eb-807f-48fb-a1ad-4a4906f18183"
version: 6
---

# IV008: Validación de Identidad - Verificar Cuestionario

> **Fuente Confluence:** [IV008: Validación de Identidad - Verificar Cuestionario](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470641866)
> **Última modificación:** 2024-02-15 — versión 6
> **Sección:** [Integraciones - Validar identidad](./index.md)

## 1. Información del servicio

Este servicio verifica las respuestas al cuestionario de preguntas para la validación de identidad a través del proceso de Experian llamado Evidente Master.

## 2. Requerimientos Funcionales del Proceso

### Campos de Entrada

| **Campo** | **Subcampo 1** | **Tipo de dato** | **Longitud** | **Obligatorio** |
|---|---|---|---|---|
| `aplicacionOrigen` | | String | 15 | SI |
| `codigoRamo` | | String — Formato: Alfanumérico | 10 | SI |
| `codigoFlujo` | | String — Formato: Alfanumérico | 10 | NO |
| `tipoDocumento` | | String — **C** - Cédula de ciudadanía, **E** - Cédula de extranjería | 1-2 | SI |
| `numeroDocumento` | | String | 3-16 | SI |
| `idCuestionario` | | String | 4-15 | SI |
| `regCuestionario` | | | | |
| `respuestas` | | | | |
| | `idPregunta` | String | 1 dígito | SI |
| | `idRespuesta` | String | 3 dígitos | SI |

### Campos de Salida

| **Campo** | **Tipo de dato** | **Valores** |
|---|---|---|
| `resultado` | String | "true","false" |
| `aprobacion` | String | "true","false" |
| `preguntasCompletas` | String | "true","false" |
| `score` | String | 1-3 dígitos |
| `codigoSeguridad` | String | 5-10 alfanumérico |
| `aprobado100PorCientoOK` | String | "true","false" |

## 3. Diseño Técnico

### 3.1. Diagrama de componentes

![Diagrama de componentes](./attachments/image-20211019-152619.png)

### 3.2. Diseño Consulta documento identidad en Registraduría expuesto por IdentityValidatorMS

**Origen:** Aplicación que requiera verificar las respuestas de un cuestionario de preguntas durante una validación de identidad con el proceso Evidente de Experian.

**Destino:** Micro-servicio IdentityValidator.

**POST**: `/api/v1/questionary/generate`

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "idCuestionario": "6542187",
    "regCuestionario": "543215",
    "respuestas": [
		{
			"idPregunta": "1",
			"idRespuesta": "002"
		},
		{
			"idPregunta": "2",
			"idRespuesta": "005"
		},
		{
			"idPregunta": "3",
			"idRespuesta": "001"
		},
		{
			"idPregunta": "4",
			"idRespuesta": "003"
		}
	],
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

`https://sarlaftapi.dllosura.com/api/v1/questionary/verify`

LABORATORIO:

`https://sarlaftapi.labsura.com/api/v1/questionary/verify`

Mensaje de entrada:

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "idCuestionario": "6542187",
    "regCuestionario": "543215",
    "respuestas": [
		{
			"idPregunta": "1",
			"idRespuesta": "002"
		},
		{
			"idPregunta": "2",
			"idRespuesta": "005"
		},
		{
			"idPregunta": "3",
			"idRespuesta": "001"
		},
		{
			"idPregunta": "4",
			"idRespuesta": "003"
		}
	],
	"codigoRamo": "041",
    "codigoFlujo": "CV01"
}
```

Mensaje de salida:

```json
{
  "resultado": "true",
  "aprobacion": "false",
  "preguntasCompletas": "true",
  "score": "685",
  "codigoSeguridad": "G9H0356",
  "aprobado100PorCientoOK": "false"
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
