---
title: "IV007: Validación de Identidad - Generar Cuestionario"
confluence_id: 2470609161
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470609161"
last_modified: "2024-02-15"
author: "712020:906704eb-807f-48fb-a1ad-4a4906f18183"
version: 7
---

# IV007: Validación de Identidad - Generar Cuestionario

> **Fuente Confluence:** [IV007: Validación de Identidad - Generar Cuestionario](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2470609161)
> **Última modificación:** 2024-02-15 — versión 7
> **Sección:** [Integraciones - Validar identidad](./index.md)

## 1. Información del servicio

Este servicio genera un cuestionario de preguntas para la validación de identidad a través del proceso de Experian llamado Evidente Master.

No siempre se debe realizar el llamado de este servicio luego de realizar la validación de identidad con OTP, depende del escenario de negocio según el perfil de riesgo o en caso que no se haya podido verificar correctamente el código OTP enviado.

## 2. Requerimientos Funcionales del Proceso

### Campos de Entrada

| **Campo** | **Tipo de dato** | **Longitud** | **Obligatorio** |
|---|---|---|---|
| `aplicacionOrigen` | String | 15 | SI |
| `codigoRamo` | String — Formato: Alfanumérico | 10 | SI |
| `codigoFlujo` | String — Formato: Alfanumérico | 10 | NO |
| `tipoDocumento` | String — **C** - Cédula de ciudadanía, **E** - Cédula de extranjería | 1-2 | SI |
| `numeroDocumento` | String | 3-16 | SI |
| `regValidacion` | String | 4-15 | SI |

### Campos de Salida

| **Campo** | **Subcampo 1** | **Subcampo 2** | **Tipo de dato** | **Valores** |
|---|---|---|---|---|
| `idCuestionario` | | | String | sólo dígitos |
| `regCuestionario` | | | String | sólo dígitos |
| `resultado` | | | String | 00 Usuario no tiene activa la opción de última consulta ó no hubo resultados en la consulta; 01 Preguntas generadas con éxito; 02 Error en el proceso de generación de preguntas ó cuestionario ya generado para ese número de validación; 07 No hay suficientes preguntas; 10 Se han agotado el número de intentos permitidos por día; 11 Se han agotado el número de intentos permitidos por este mes; 12 Se han agotado el número de intentos permitidos por este año; 13 Se han agotado el número de ingresos permitidos al producto por día; 14 Se han agotado el número de ingresos permitidos para el producto por este mes; 15 Se han agotado el número de ingresos permitidos para el producto por este año; 17 Consulta no autorizada; 18 Consulta no autorizada; 19 Consulta no autorizada; 20 El Cuestionario ya fue generado; 21 Este cuestionario tiene un proceso OTP que no ha sido completado ó El número de identificación asociado a la solicitud no coincide con el que está asociado al regValidacion |
| `preguntas` | | | Array | |
| | `id` | | String | 8-10 dígitos |
| | `orden` | | String | 1 dígito |
| | `texto` | | String | |
| | `respuestas` | | Array | |
| | | `id` | String | 3 dígitos |
| | | `texto` | String | |
| `estado` | | | Boolean | true, false |
| `mensajeEstado` | | | String | Mensaje general del proceso de generación de cuestionario |

## 3. Diseño Técnico

### 3.1. Diagrama de componentes

![Diagrama de componentes](./attachments/image-20211019-152619.png)

### 3.2. Diseño Consulta documento identidad en Registraduría expuesto por IdentityValidatorMS

**Origen:** Aplicación que requiera generar un cuestionario de preguntas durante una validación de identidad con el proceso Evidente de Experian.

**Destino:** Micro-servicio IdentityValidator.

**POST**: `/api/v1/questionary/generate`

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
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

`https://sarlaftapi.dllosura.com/api/v1/questionary/generate`

LABORATORIO:

`https://sarlaftapi.labsura.com/api/v1/questionary/generate`

Mensaje de entrada:

```json
{
    "aplicacionOrigen": "SARLAFT",
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "regValidacion": "123456789",
    "codigoRamo": "041",
    "codigoFlujo": "CV01"
}
```

Mensaje de salida:

```json
{
  "idCuestionario": "6542187",
  "regCuestionario": "543215",
  "resultado": "01",
  "preguntas": [
    {
      "id": "00500001",
      "orden": "1",
      "texto": "HACE CUANTO TIEMPO TIENE SU CREDITO HIPOTECARIO?",
      "respuestas": [
        { "id": "001", "texto": "ENTRE 0 Y 3 AÑOS" },
        { "id": "002", "texto": "ENTRE 4 Y 5 AÑOS" },
        { "id": "003", "texto": "ENTRE 6 Y 9 AÑOS" },
        { "id": "004", "texto": "ENTRE 10 Y 14 AÑOS" },
        { "id": "005", "texto": "15 AÑOS O MAS" },
        { "id": "006", "texto": "NO TENGO CREDITO DE VIVIENDA" }
      ]
    },
    {
      "id": "00500002",
      "orden": "2",
      "texto": "EN JULIO DE 2021 SU CREDITO CON BANCO:",
      "respuestas": [
        { "id": "001", "texto": "ESTABA ABIERTO/VIGENTE" },
        { "id": "002", "texto": "ESTABA CANCELADA/SALDADA/CERRADA/INACTIVA" },
        { "id": "003", "texto": "NUNCA HE TENIDO CREDITO CON LA ENTIDAD" }
      ]
    },
    {
      "id": "00500003",
      "orden": "3",
      "texto": "EL VALOR DE LA CUOTA DE JULIO DE 2021 DE SU CREDITO CON BANCO ESTABA ENTRE:",
      "respuestas": [
        { "id": "001", "texto": "$337,001 Y $562,000" },
        { "id": "002", "texto": "$562,001 Y $787,000" },
        { "id": "003", "texto": "$787,001 Y $1,012,000" },
        { "id": "004", "texto": "$1,012,001 Y $1,237,000" },
        { "id": "005", "texto": "$1,237,001 Y $1,462,000" },
        { "id": "006", "texto": "NO TENGO CREDITO CON LA ENTIDAD" }
      ]
    },
    {
      "id": "00500004",
      "orden": "4",
      "texto": "CON CUAL DE LAS SIGUIENTES ENTIDADES USTED TIENE O HA TENIDO EN LOS ULTIMOS 5 AÑOS UN/UNA PLAN / PAQUETE TELEFONIA CELULAR?",
      "respuestas": [
        { "id": "001", "texto": "MOVISTAR - TELEFONICA MOVILES COLOMBIA S.A" },
        { "id": "002", "texto": "CLARO - COMUNICACION CELULAR - COMCEL S.A." },
        { "id": "003", "texto": "TIGO - COLOMBIA MOVIL S.A. E.S.P" },
        { "id": "004", "texto": "NINGUNA DE LAS ANTERIORES" }
      ]
    }
  ],
  "estado": true,
  "mensajeEstado": "Se generaron las preguntas del cuestionario"
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
