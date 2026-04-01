# IV001: Validar documento de identidad con Registraduría

>**Fuente:**[Ver en Confluence](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2456289281)
>**Fecha extracción:**2026-03-27

## Archivos Adjuntos

  [exists] 1.1. Instructivo Conectividad SOAP DataCredito Experian v1.2.pdf
  [exists] image-20211019-152619.png
  [exists] 560858de-1f87-4925-8fc8-61ed0f379722.png

- [1.1. Instructivo Conectividad SOAP DataCredito Experian v1.2.pdf](./attachments/1.1. Instructivo Conectividad SOAP DataCredito Experian v1.2.pdf)
- [image-20211019-152619.png](../imagenes/image-20211019-152619.png)
- [560858de-1f87-4925-8fc8-61ed0f379722.png](../imagenes/560858de-1f87-4925-8fc8-61ed0f379722.png)

---

### 1. Información del servicio

Este servicio permite consultar información sobre el documento de identidad con Registraduría, cabe resaltar que solo aplica Registraduría para el tipo de documento de identidad C-Cédula de ciudadanía, con respecto a los demás tipos de identificación la información se valida con la información que Data Credito Experian posee de otras instituciones.

#### 2. Requerimientos Funcionales del Proceso

##### Campos de Entrada

||

**Campo**

||

**Tipo de dato**

 |**

**Longitud**
**|**
**Obligatorio**
**|

||

tipoDocumento

||

String

**Valores permitidos:**

**C**- Cédula de ciudadanía

**A**- NIT

**F**- Identificación fiscal para extranjeros

**E**- Cédula de extranjería

||

 1-2

||

SI

||
||

numeroDocumento

||

String

||

3-16

||

SI

||
||

primerApellido

||

String

||

100

||

SI

||
||

aplicacionOrigen

||

String

||

15

||

SI

||

###### Campos de Salida

||

**Campo**

||

**Subcampo**

||

**Tipo de dato**

 |**

**Longitud/Comentario**
**|

||

fechaConsulta

||
||

Date (Formato ISO8601 2021-01-01T00:00:00)

||

||
||

codigoSeguridad

||
||

String

||

8-10

||
||

validado

||
||

Boolean

||

Este campo de la respuesta es entregado directamente por Experian-Registraduria, en la cual indica que los datos entregados se trajeron de registraduría o se consultaron de Registraduría.**No tiene ninguna validación de negocio adicional.**

||
||

datosRespuestaValidacion

||
||

Object

||
||
||
||

rut

||

Boolean

||
||
||
||

tipoPersona

||

String

**Posibles valores:**

PERSONA NATURAL NACIONAL

PERSONA NATURAL EXTRANJERA

PERSONA JURIDICA NACIONAL

PERSONA JURIDICA EXTRANJERA

24-27

||
||
||

tipoDocumento

||

String

**Posibles valores:**

**C**- Cédula de ciudadanía

**A**- NIT

**F**- Identificación fiscal para extranjeros

**E**- Cédula de extranjería

||

1-2

||
||
||

numeroDocumento

||

String

||

3-16

||
||
||

nombreCompleto

||

String

||
||
||
||

nombres

||

String

||
||
||
||

primerApellido

||

String

||
||
||
||

segundoApellido

||

String

||
||
||
||

codigoEstadoDocumento

||

String

**Posibles valores:**

Dependiendo de los estados de respuesta:

00 - 99

||

0-2

||
||
||

estadoDocumento

||

String

**Posibles valores:**

Dependiendo de los códigos de respuesta:

VIGENTE

CANCELADA POR MUERTE O FALLECIDO

CANCELADA

NO EXPEDIDA

EN TRAMITE

||
||
||

fechaExpedicion

||

Date (Formato ISO8601 2021-01-01T00:00:00)

||
||
||
||

ciudadExpedicion

||

String

||
||
||
||

departamentoExpedicion

||

String

||
||
||
||

nacionalidad

||

String

||
||
||
||

fechaNacimiento

||

Date (Formato ISO8601 2021-01-01T00:00:00)

||
||
||
||

estadoCivil

||

String

**Posibles valores:**

CASADA

VIUDA

MUJER

HOMBRE

5-6

||
||
||

genero

||

String

**Posibles valores:**

MUJER

HOMBRE

5-6

||
||
||

rangoEdad

||

String

**Ejemplo:**

Edad mínima-Edad máxima (29-35)

||
||

###### 3. Diseño Técnico

###### 3.1. Diagrama de componentes

###### 3.2. Diseño Consulta documento identidad en Registraduría expuesto por IdentityValidatorMS

**Origen:**Aplicación que requiera consultar información documento con Registraduría, por ejemplo SARLAFT

**Destino:**Micro-servicio IdentityValidator

**POST**: /api/v1/registry/validate

```{
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "primerApellido": "PRUEBAS",
    "aplicacionOrigen": "SARLAFT"
}
```text

###### 3.3. Diseño Consulta documento identidad en Registraduría expuesto por Data Credito Experian

**Origen:** Micro-servicio IdentityValidator

**Destino:** Data Credito Experian

Se realiza un consumo de un servicio SOAP de Data Crédito Experian de manera segura, con firma y cifrado de información de punta a punta.

Para temas internos de Sura:

Se requiere de un certificado digital emitido por una CA (Certificate Authority) reconocida, no se admiten certificados autofirmados, su vigencia mínima debe ser de 1 año y su clave privada debe cumplir con un tamaño mínimo de 2048 bits.

Enviar su llave pública a Experian, para su posterior registro

Crear un llavero o KEYSTORE, que contenga la llave pública y privada (Para consumo y descripción del servicio), se debe instalar en la máquina con el asistente para instalar certificados de Windows (Formato .p12)

Para uso dentro de una aplicación JAVA, se debe crear el llavero o KEYSTORE en formaro .jks, adicional al paso anterior se debe importar dentro del llavero el certificado del servicio SOAP de Experian.

Los consumos deberán realizarse agregando los certificados, y headers de seguridad sobre este servicio (Timestamp, username, Signature)

Adjunta documentación técnica entregada por Experian:

[![imagen](https://segurosti.atlassian.net/wiki/download/thumbnails/2456289281/1.1.%20Instructivo%20Conectividad%20SOAP%20DataCredito%20Experian%20v1.2.pdf?version=1&modificationDate=1634658268298&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/2456289281/1.1.%20Instructivo%20Conectividad%20SOAP%20DataCredito%20Experian%20v1.2.pdf?version=1&modificationDate=1634658268298&cacheVersion=1&api=v2)

**Ejemplo de Mensaje (**[**Importante revisar Estrategia de seguridad en el punto 5**](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2456289281/IV001+Validar+documento+de+identidad+con+Registradur+a#5.-Estrategia-de-seguridad)**):**

**POST**

DESARROLLO:

[https://sarlaftapi.dllosura.com/api/v1/registry/validate](https://sarlaftapi.dllosura.com/api/v1/registry/validate)

LABORATORIO:

[https://sarlaftapi.labsura.com/api/v1/registry/validate](https://sarlaftapi.labsura.com/api/v1/registry/validate)

Mensaje de entrada:

```{
    "tipoDocumento": "C",
    "numeroDocumento": "888888881",
    "primerApellido": "PRUEBAS",
    "aplicacionOrigen": "SARLAFT"
}
```text

Mensaje de salida:

```{
    "fechaConsulta": "2021-10-19T10:47:35",
    "codigoSeguridad": "EL8z8J1",
    "validado": true,
    "datosRespuestaValidacion": {
        "rut": false,
        "tipoPersona": "PERSONA NATURAL NACIONAL",
        "tipoDocumento": "C",
        "numeroDocumento": "888888881",
        "nombreCompleto": "PRUEBAS PEREZ JUAN",
        "nombres": "JUAN",
        "primerApellido": "PRUEBAS",
        "segundoApellido": "PEREZ",
        "codigoEstadoDocumento": "00",
        "estadoDocumento": "VIGENTE",
        "fechaExpedicion": "1988-10-05T00:00:00",
        "ciudadExpedicion": "BOGOTA DC",
        "departamentoExpedicion": "CUNDINAMAR",
        "nacionalidad": "",
        "fechaNacimiento": null,
        "estadoCivil": "",
        "genero": "HOMBRE",
        "rangoEdad": "46-55"
    }
}
```

###### 4. Manejo de errores

En cuanto a excepciones, éxito y errores, el micro-servicio maneja los estados de respuesta HTTP:

1xx: Respuestas informativas

2xx: Peticiones correctas

3xx: Redirecciones

4xx: Errores del cliente

5xx: Errores de servidor

###### 5. Estrategia de seguridad

Estándar para todas las integraciones:

Uso de SEUS 4 (Ambiente de desarrollo y laboratorio se puede autenticar con usuario nombrado impmasivos)

Adicional se cuenta con otro tipo de Autenticación muy conocida, llamado  JSON Web Tokens (JWT), se ha convertido rápidamente en un estándar en la autenticación de aplicaciones. [Ver generación JWT](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2464088065/IV002+Generar+JSON+WEB+TOKEN+seguridad+IdentityValidator)

###### 6. Configuración opciones JVM

Es importante esta configuración para que este servicio pueda funcionar correctamente, es decir, se realice la comunicación segura entre el microservicio identityValidatorMS y Data crédito Experian. [Ver configuración ejecución local](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2378924049/Configuraci+n+Ambiente+-+IdentityValidator#Despliegue-local-Identity-Validator)
