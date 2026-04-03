---
title: "Front - Validar identidad (Web Component)"
confluence_id: 2432172101
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2432172101"
last_modified: "2025-08-27"
author: "632dd1a5234d44d406d0f129"
version: 28
---

# Front - Validar identidad (Web Component)

> **Fuente Confluence:** [Front - Validar identidad (Web Component)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2432172101)
> **Última modificación:** 2025-08-27 — versión 28
> **Sección:** [Integraciones - Validar identidad](./index.md)

> **📝 Nota:** El objetivo es detallar todo lo requerido para implementar la validación de identidad como WC (Web Component)

## Cómo empezar

La aplicación está construida en el framework de [Angular](https://angular.io/) y se utiliza la funcionalidad de [Angular Elements](https://angular.io/guide/elements) para crear un Web Component que luego se puede incrustar en otras aplicaciones.

La etiqueta del componente es la siguiente: `<validacionidentidad-app>`

## Implementación del Web Component

Para hacer el llamado al WC se deben importar los siguientes archivos:

| Tipo | Archivo(s) |
|---|---|
| Javascript | `webcomponent-main.js` |
| Estilos | `styles.css` |
| Fuentes | `Barlow-Bold.woff2`, `Barlow-Bold.woff`, `Barlow-Bold.ttf`, `Barlow-Medium.woff2`, `Barlow-Medium.woff`, `Barlow-Medium.ttf`, `Barlow-Regular.woff2`, `Barlow-Regular.woff`, `Barlow-Regular.ttf`, `FSJoeyWeb-Bold.eot`, `FSJoeyWeb-Bold.svg`, `FSJoeyWeb-Bold.woff`, `FSJoeyWeb-Bold.woff2` |
| Imágenes | `check_circle_green_24dp.svg`, `check_circle_red_24dp.svg`, `close-24px.svg`, `logo-sura.svg`, `problema-plataforma.svg`, `sarlaft.svg` |

## Parámetros de entrada

```typescript
@Input() token: string;
@Input('idaplicacionorigen') idAplicacionOrigen: string;
@Input('idevaluacionsarlaft') idEvaluacionSarlaft: string;
@Input('tipollamado') tipoLlamado: string;
@Input('informaciongeneral') informacionGeneral: string;
@Input('codigoflujo') codigoFlujo: string;
```

- `token` Token JWT para consumir servicios en el Back (identity-validator).
- `idAplicacionOrigen` Identificador de la aplicación que consume el WC.
- `idevaluacionsarlaft` identificador de la evaluación Sarlaft.
- `tipoLlamado` Indicar el tipo de llamado del WC. Existen 2 formas:
  - `redireccion` Se usar para ver la aplicación completa, es decir contiene header, y opciones para cerrarla.
  - `incrustado` Se usa para ver la aplicación como un componente adicional a la aplicación cliente (la que la esta implementado)
- `informacionGeneral` parámetro donde están los datos de negocio requeridos para hacer la validación de identidad, es un string pero debe llegar con formato tipo JSON.
- `codigoFlujo` identificador de flujo a tomar de parte de el back en cual tiene parametrias de experian definidad

> **⚠️ Nota:** Tener en cuenta: al pasar el parámetro `informaciongeneral` se deben tener las comillas **dobles**

Estructura:

| **Nombre atributo** | **Tipo dato** | **¿Acepta dato vacío?** |
|:---:|:---:|:---:|
| `tipoIdentificacion` | String | NO |
| `numeroIdentificacion` | String | NO |
| `primerNombre` | String | NO |
| `segundoNombre` | String | SI |
| `primerApellido` | String | NO |
| `segundoApellido` | String | SI |
| `numeroCelular` | String | NO |
| `fechaExpedicion` | String | SI |
| `rol` | String | NO |
| `producto` | String | SI |
| `ramo` | String | NO |
| `dniAsesor` | String | SI |
| `celularAsesor` | String | SI |

Ejemplo:

```json
{
	"tipoIdentificacion": "C",
	"numeroIdentificacion": "71263091",
	"primerNombre": "JUAN",
	"segundoNombre": "CAMILO",
	"primerApellido": "ZAPATA",
	"segundoApellido": "ALVAREZ",
	"numeroCelular": "3007149216",
	"fechaExpedicion": "2020-01-01",
	"rol": "RL",
	"producto": "VIDA",
	"ramo": "Vida Grupo",
	"dniAsesor": "C71263093",
	"celularAsesor": "3007749737"
}
```

*Los tipos de documento son los siguientes:

| **Tipo de Identificación** | **Descripción** | **Descripción Equivalente SURA** |
|:---:|:---:|:---:|
| C | C.C. Cédula de ciudadanía | CEDULA - Expedido en Colombia por la registraduria -Personas Naturales |
| A | NIT Número de identificación tributaria | NIT - Expedido por la Dian - Persona Jurídica |
| F | N.E. Nit de extranjería | ID. FISCAL PARA EXTRANJEROS |
| E | C.E. Cédula de Extranjería | CEDULA EXTRANJERIA - Es el documento expedido por el Das para personas naturales no nacidas en Colombia |
| P | PAS – Pasaporte | Pasaporte del país de origen para personas naturales no nacidas en Colombia |
| D | CD – Carné Diplomático | DIPLOMATICO |
| T | TI – Tarjeta de Identidad | Expedido en Colombia por la registraduría  para menores de edad -Personas Naturales |
| X | DNI – Documento Nacional de Identidad | No existe |
| TE | PEP – Permiso Especial de Permanencia | Permiso especial de permanencia |

## Parámetros de salida

- `@Output('resultevent') resultEvent = new EventEmitter<string>();`
- `@Output('salirDeAplicacion') salirDeAplicacion = new EventEmitter<boolean>();`

> **ℹ️ Info:** `salirDeAplicacion` esta variable se utiliza ya que cuando la aplicación que consume el WC, es la que debe cerrar la ventana ya que por seguridad navegador no permite que una aplicacion "hija" ejecute scripts hacia los padres.

El Web Component durante la ejecución de procesos internos puede devolver los siguientes valores:

| **Parámetro de salida** | **Tipos de salida** | **Descripción** |
|:---:|:---:|---|
| `resultevent` | `validacionExitosa` | Indica que la validación de identidad fue exitosa |
| | `intentosAgotados` | Indica que la validación de identidad NO fue exitosa, debido a que se agotaron los intentos disponibles por día |
| | `validacionFallida` | Indica que la validación de identidad NO fue exitosa |
| | `problemasPlataforma` | Indica que la validación de identidad NO fue exitosa, debido a que se presentaron problemas en la aplicación |
| | `valoresInicialesInvalidos` | Indica que no se pudo realizar el llamado de forma exitosa al Web Component debido a que faltaron los valores iniciales de entrada. |
| | `ValidacionFallidaDatosIncorrectos` | Indica que la validación de identidad ha fallado debido a que los datos del cliente no son los correctos, por ejemplo, nombres, apellidos, tipo y número de documento. |
| | `ValidacionIntentosAgotadosPorDiaIdentidad` | Indica que ha superado los intentos validos para la validación de identidad por día, el cliente debería poder intentar nuevamente en 24 horas |
| | `ValidacionIntentosAgotadosPorDiaCuestionario` | Indica que ha superado los intentos validos por día para la validación de identidad con el cuestionario proveído por Experian |
| | `ValidacionIntentosAgotadosPorMesCuestionario` | Indica que ha superado los intentos validos por mes para la validación de identidad con el cuestionario proveído por Experian |
| | `ValidacionIntentosAgotadosPorAnioCuestionario` | Indica que ha superado los intentos validos por año para la validación de identidad con el cuestionario proveído por Experian |
| `salirDeAplicacion` | `true \| false` | Para cuando el webcomponent es llamado en forma de redirección, la aplicación contiene acciones para salir de la ventana, dado que no se puede realizar desde el componente hijo, se retorna esta variable para el que implementa el web component realice está acción. |

## Uso del Web Component

<details>
<summary>Ejemplo de implementacion desde un html:</summary>

```html
<!doctype html>

<html lang="en">

<head>

  <meta charset="utf-8">

  <title>InitialApp</title>

  <base href="/">

  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="icon" type="image/x-icon" href="favicon.ico">

  <link href="https://sarlaft.dllosura.com/identityvalidatorfr/styles.css" rel="stylesheet">
  <link href="https://sarlaft.dllosura.com/identityvalidatorfr/Barlow-Bold.woff2" rel="stylesheet"> -->
  <link href="https://sarlaft.dllosura.com/identityvalidatorfr/Barlow-Bold.woff" rel="stylesheet">
  <link href="https://sarlaft.dllosura.com/identityvalidatorfr/Barlow-Bold.ttf" rel="stylesheet">

</head>

<body>

  <validacionidentidad-app
    token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
    idaplicacionorigen='SARLAFT' idevaluacionsarlaft='23423423423' tipollamado='redireccion' informaciongeneral='{
      "tipoIdentificacion": "1",
      "numeroIdentificacion": "71263091",
      "primerNombre": "JUAN",
      "segundoNombre": "CAMILO",
      "primerApellido": "ZAPATA",
      "segundoApellido": "ALVAREZ",
      "numeroCelular": "3007149216",
      "fechaExpedicion": "2020-01-01",
      "rol": "RL",
      "producto": "VIDA",
      "ramo": "Vida Grupo",
      "dniAsesor": "C71263093",
      "celularAsesor": "3007749737"
    }' (resultevent)="result($event)" (salirDeAplicacion)="salir($event)">
  </validacionidentidad-app>

  <script type="text/javascript" src="https://sarlaft.dllosura.com/identityvalidatorfr/webcomponent-main.js"></script>

</body>

</html>
```

</details>

## Accesos

Para cada ambiente se debe indicar su respectiva URL:

- `https://sarlaft.dllosura.com/identityvalidatorfr/`
- `https://sarlaft.labsura.com/identityvalidatorfr/`
- `https://sarlaft.sura.com.co/identityvalidatorfr/`

**Repositorios:**

Front: [https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/1101-validadorcliente_identidad-fr)

**CI / CD - Pipeline - Azure Pipeline**

Se realiza la actualización del pipeline en Azure Pipeline acogiendo el uso de templates dispuestos por la compañía.

**Url del nuevo pipeline:**

[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=4503](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_build?definitionId=4503)
