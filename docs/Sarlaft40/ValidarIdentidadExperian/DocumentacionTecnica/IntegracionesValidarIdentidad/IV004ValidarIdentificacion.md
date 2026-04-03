---
title: "IV004: Validación de Identidad - Validar Identificación"
confluence_id: 2470641791
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470641791"
last_modified: "2024-08-16"
author: "632dd1a5234d44d406d0f129"
version: 18
---

# IV004: Validación de Identidad - Validar Identificación

> **Fuente Confluence:** [IV004: Validación de Identidad - Validar Identificación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470641791)
> **Última modificación:** 2024-08-16 — versión 18
> **Sección:** [Integraciones - Validar identidad](./index.md)

## 1. Información del servicio

Este servicio realiza la validación de la identificación para el proceso de Validación de Identidad, a través del proceso de Experian llamado Evidente Master.

Validar la identificación con este servicio genera un código de validación dado en la respuesta, `regValidación`, el cuál debe ser enviado en los siguientes pasos como parámetro durante todo el proceso de validación de identidad.

## 2. Requerimientos Funcionales del Proceso

### Campos de Entrada

| **Campo** | **Tipo de dato** | **Longitud** | **Obligatorio** |
|---|---|---|---|
| `aplicacionOrigen` | String | 15 | SI |
| `codigoRamo` | String — Formato: Alfanumérico | 10 | SI |
| `codigoFlujo` | String — Formato: Alfanumérico | 10 | NO |
| `tipoDocumento` | String — **C** - Cédula de ciudadanía, **E** - Cédula de extranjería | 1-2 | SI |
| `numeroDocumento` | String | 3-16 | SI |
| `fechaExpedicion` | String — Formato fecha: `yyyy-mm-dd` | 10 | NO |
| `primerNombre` | String | 100 | SI |
| `segundoNombre` | String | 100 | NO |
| `primerApellido` | String | 100 | SI |
| `segundoApellido` | String | 100 | NO |

Se agregan validaciones de entrada para los siguientes atributos:

- `primerNombre`: La cadena debe cumplir con la regex `"^[a-zA-ZÑñ.]+(-[a-zA-ZÑñ.]*)?$"`
- `segundoNombre`: La cadena debe cumplir con la regex `"^[a-zñA-ZÑ.\\-\\s]+$"`
- `primerApellido`: La cadena debe cumplir con la regex `"^[a-zñA-ZÑ.\\-\\s]+$"`
- `segundoApellido`: La cadena debe cumplir con la regex `"^[a-zñA-ZÑ.\\-\\s]+$"`
- `fechaExpedicion`: Debe cumplir con el formato de fecha `"yyyy-MM-dd"` y no debe ser una fecha superior a la fecha actual.

### Campos de Salida

| **Campo** | **Tipo de dato** | **Valores** |
|---|---|---|
| `valApellido` | String | "true","false" |
| `valNombre` | String | "true","false" |
| `valFechaExp` | String | "true","false" |
| `alertas` | String | "true","false" |
| `respuestaAlertas` | String | "00-99" |
| `resultado` | String | 01 Válido con historia de crédito, 05 Válido sin historia de crédito, 06 No coinciden datos, 07 No existe identificación, 08 Válido con Documento no Vigente, 09 Superado el número de intentos de validación máximo del día, 11 Cliente monitoreado por la entidad consulta no autorizada |
| `regValidacion` | String | 4-15 dígitos |
| `resultadoProceso` | String | "true","false" |
| `consultasDisponibles` | String | 1-2 dígitos |
| `estado` | Boolean | true, false |
| `mensajeEstado` | String | Mensaje general del proceso de validar identificación |

## 3. Diseño Técnico

### 3.1. Diagrama de componentes

![Diagrama de componentes](./attachments/image-20211019-152619.png)

### 3.2. Diseño Consulta documento identidad en Registraduría expuesto por IdentityValidatorMS

**Origen:** Aplicación que requiera validar la identificación durante una validación de identidad con el proceso Evidente de Experian.

**Destino:** Micro-servicio IdentityValidator.

**POST**: `/api/v1/identification/validate`

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "primerNombre": "PRUEBAS",
    "segundoNombre": "TEST",
    "primerApellido": "PRUEBAS",
    "segundoApellido": "TEST",
    "fechaExpedicion": "2007-11-22",
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

`https://sarlaftapi.dllosura.com/api/v1/identification/validate`

LABORATORIO:

`https://sarlaftapi.labsura.com/api/v1/identification/validate`

Mensaje de entrada:

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "primerNombre": "PRUEBAS",
    "segundoNombre": "TEST",
    "primerApellido": "PRUEBAS",
    "segundoApellido": "TEST",
    "fechaExpedicion": "2007-11-22",
    "codigoRamo": "041",
    "codigoFlujo": "CV01"
}
```

Mensaje de salida:

```json
{
  "valApellido": "true",
  "valNombre": "true",
  "valFechaExp": "true",
  "alertas": "false",
  "respuestaAlerta": "03",
  "resultado": "01",
  "regValidacion": "123465789",
  "resultadoProceso": "true",
  "consultasDisponibles": "1",
  "estado": true,
  "mensajeEstado": "Validación de identificación exitosa, coincidencia en los datos"
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
