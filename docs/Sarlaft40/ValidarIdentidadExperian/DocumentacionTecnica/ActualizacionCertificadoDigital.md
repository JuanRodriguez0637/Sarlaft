---
title: "Actualización certificado digital y keystore (Llavero) consumo seguro servicios SOAP de DataCrédito Experian"
confluence_id: 2481651740
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2481651740"
last_modified: "2021-11-19"
author: "Marwin Fabian Gelvez Quintero"
version: 10
---

# Actualización certificado digital y keystore (Llavero) consumo seguro servicios SOAP de DataCrédito Experian

> **Fuente Confluence:** [Actualización certificado digital y keystore (Llavero) consumo seguro servicios SOAP de DataCrédito Experian](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2481651740)
> **Última modificación:** 2021-11-19 — Marwin Fabian Gelvez Quintero · versión 10
> **Sección:** [Documentación técnica](./index.md)

# 1. Información relevante

La siguiente información describe cada uno de los pasos que debe seguir para actualizar los certificados digitales y el keystore, para conectarse de manera segura a los servicios web SOAP expuestos por DataCrédito Experian.

Los servicios web que ofrece DataCrédito Experian cuentan con una seguridad definida que cumple con las políticas AAA (Autenticación, Autorización y Auditoria) y adicional a ello siempre buscan garantizar la integridad y confidencialidad de los mensajes.

# 2. Pasos para actualización

DataCrédito Experian notificará que los certificados están próximos a vencer, lo realizan de la siguiente forma, Un (1) mes antes, quince (15) días antes, una (1) semana antes, y un (1) día antes. Con el fin de realizar la actualización pertinente y no sé afecte la integración con este. La notificación la realiza al correo del encargado del proceso registrado en Experian.

## 2.1. Solicitud de renovación o creación de certificado digital

El **área de seguridad** es el responsable de la creación o renovación del certificado digital, el certificado se usará para la conectividad de los servicios web (SOAP) seguros expuestos por Data crédito Experian.

1. El proceso para solicitar la creación de un nuevo certificado, se realiza a través de Catálogo de servicios, la opción es **Servicios de TI > Seguridad > Certificados digitales.** [Ir a Catálogo](https://ca-catalogo.suramericana.com/usm/wpf?id=69165666421215283348742709890560184659680)

2. En cuanto a la renovación de los certificados digitales, el área de seguridad debe notificar antes, y enviar el certificado digital al responsable de este. Si se requiere alguna información o trámite se puede generar un caso o CA, solicitar que se asigne al grupo AR - Certificados Digitales, o contactar a William Evelio Agudelo Corrales <wagudelo@sura.com.co> (Sujeto a cambios)

Estos certificados deban cumplir con las siguientes características:

- Deben ser generados por una CA (Certificate Authority) válida y reconocida, no se admiten certificados autofirmados
- La clave privada debe cumplir con un tamaño mínimo de 2048 bits
- La vigencia mínima del certificado debe ser de 1 año

El equipo de seguridad deberá entregar los siguientes archivos:

![image-20211105-145848.png](./attachments/image-20211105-145848.png)

**Contraseña Texto Plano.txt:** archivo que contiene la contraseña en texto plano para abrir el archivo `sarlaftapi.labsura.com.pfx` o el certificado

**sarlaftapi.labsura.com.cer (obligatorio para generar el keystore):** archivo que contiene la llave publica del certificado o información del certificado

![image-20211104-223144.png](./attachments/image-20211104-223144.png)

**sarlaftapi.labsura.com.key (obligatorio para generar el keystore):** archivo que contiene la llave privada del certificado en formato OPENSSL

![image-20211104-223401.png](./attachments/image-20211104-223401.png)

**sarlaftapi.labsura.com.pfx:** archivo que contiene toda la información de un certificado digital, incluyendo su llave pública y privada en formato PKCS#12

**sarlaftapi.labsura.com.pkcs8:** archivo que contiene la llave privada del certificado en formato PKCS#8

![image-20211104-223815.png](./attachments/image-20211104-223815.png)

**NOTA:** Las imágenes son ejemplos, sin mostrar la información importante de los certificados, son una guía para diferenciar las etiquetas iniciales de cada formato.

## 2.2. Intercambio de certificado público con DataCrédito Experian

De los archivos del certificado entregados por el área encargada, se debe enviar el certificado público a DataCrédito Experian, esto con el fin de añadirlo en la plataforma que realiza la validación SSL en doble vía. En nuestro caso, el certificado público es el archivo cuyo nombre es el dominio al cual está vinculado el certificado digital (ejemplo: **sarlaftapi.labsura.com.cer**)

Se debe enviar un correo en el siguiente formato:

**DESARROLLO y LABORATORIO**

**Para:** connectivity_support@experian.com\
**Asunto:** Renovación Certificado_SURA DESARROLLO O LABORATORIO\
**Cuerpo:**\
Buen día,\
A continuación, el certificado\
\<Certificado\>

![image-20211105-182527.png](./attachments/image-20211105-182527.png)

Los datos son:

Servicios contratados:

https://demo-servicesesb.datacredito.com.co/wss/dhws3/services/DHServicePlus

https://demo-servicesesb.datacredito.com.co/wss/HCPL_WS/HcplWSClientes

SEGUROS GENERALES SURAMERICANA S.A\
NIT 890903407-9

Cordial saludo

**PRODUCCIÓN**

**Para:** Mirneyi.Tamayo@experian.com; Paola.Garcia@experian.com; Rocio.Garcia@experian.com\
**Asunto:** Renovación Certificado_SURA PRODUCCION\
**Cuerpo:**\
Buen día,\
A continuación, el certificado\
\<Certificado\>

![image-20211105-182527.png](./attachments/image-20211105-182527.png)

Los datos son:

Servicios contratados:

https://servicesesb.datacredito.com.co/wss/dhws3/services/DHServicePlus

https://servicesesb.datacredito.com.co/wss/HCPL_WS/HcplWSClientes

SEGUROS GENERALES SURAMERICANA S.A\
NIT 890903407-9

Cordial saludo

Una vez se realiza exitosamente la configuración del certificado digital en DataCrédito Experian, enviará un correo de confirmación de la renovación del certificado.

## 2.3. Creación del Keystore

### 2.3.1. Herramienta para creación del Keystore

Para la creación del Keystore o llavero que combina la llave pública con su respectiva llave privada, existen diferentes herramientas, para la creación de esta documentación y con fin ilustrativo se usará **KEYSTORE EXPLORER**, el cual se podrá descargar de la página oficial http://keystore-explorer.org/downloads.html

### 2.3.2. Requisitos para la creación del Keystore y formato de las llaves

Tenga en cuenta que, para realizar la creación del keystore, debe disponer de la llave o certificado público (que es el mismo que se envió a DataCrédito Experian en el paso 2.2), la llave privada otorgada por la Certification Authority (CA), y el certificado público de los servicios SOAP de DataCrédito Experian que se deberá solicitar.

- La llave pública cuando se abre en editor de texto se puede reconocer, porque contiene una cadena de texto dentro de las etiquetas `BEGIN CERTIFICATE-----` y `-----END CERTIFICATE-----`
- La llave privada que debe entregar la CA (Certification Authority) y el formato en la que esta se encuentra, cuando se abre en editor de texto se puede reconocer:

| Formato **PKCS#8** contiene una cadena de texto dentro de las etiquetas `-----BEGIN PRIVATE KEY-----` y `-----END PRIVATE KEY-----` | Formato **OPENSSL** contiene una cadena de texto dentro de las etiquetas `-----BEGIN RSA PRIVATE KEY-----` y `-----END RSA PRIVATE KEY-----` **(RECOMENDADA)** |
| --- | --- |

### 2.3.2. Creación de Key Pair (Combinación de llave pública-privada)

Una vez que se dispone de los dos archivos, que contienen la llave pública y la llave privada, se debe ejecutar la herramienta KeyStore Explorer, y en la pantalla que carga, se da clic a la opción **"Create a new keystore"**

![image-20211108-155302.png](./attachments/image-20211108-155302.png)

Se abre un cuadro de dialogo en el cual debe seleccionar el formato del llavero, en este caso, para sistemas Java el formato adecuado es **JKS**, se selecciona esta, y se presiona el botón "**OK**"

![image-20211118-043622.png](./attachments/image-20211118-043622.png)

Posteriormente, se debe ir al menú "**Tools**", y dar clic en la opción "**Import Key Pair**"

![image-20211118-044049.png](./attachments/image-20211118-044049.png)

Se abre un cuadro de diálogo, para seleccionar el formato en el que viene la llave privada, en este caso se selecciona OpenSSL, la manera de reconocer el formato, porque en el archivo viene dentro de las etiquetas `-----BEGIN RSA PRIVATE KEY-----` y `-----END RSA PRIVATE KEY-----`, se debe dar clic en "**OK**"

![image-20211118-044439.png](./attachments/image-20211118-044439.png)

En el cuadro de dialogo que se abre, se debe pulsar sobre el botón "**Browse**" correspondiente a la opción de la llave privada

![image-20211118-044713.png](./attachments/image-20211118-044713.png)

En el explorador que se abre se debe buscar la ubicación del archivo que corresponde a la llave privada

![image-20211118-044935.png](./attachments/image-20211118-044935.png)

Lo mismo se debe realizar para seleccionar el certificado público en la sección correspondiente a "**Certificate(s) File**"

![image-20211118-045433.png](./attachments/image-20211118-045433.png)

Y se debe elegir el archivo que corresponde al certificado público

![image-20211118-045208.png](./attachments/image-20211118-045208.png)

Se presiona en el botón "**Import**"

![image-20211118-045325.png](./attachments/image-20211118-045325.png)

Se debe ingresar un **Alias** en la ventana que se habilita y se presiona el botón "**OK**"

![image-20211118-045644.png](./attachments/image-20211118-045644.png)

**IMPORTANTE:** Para ambiente de DESARROLLO y LABORATORIO el alias es **sarlaftapi.labsura.com**, para ambiente PRODUCCIÓN es **validadoridentidad.sura.com.co**, que corresponde al nombre de cada certificado usado de acuerdo el ambiente. (Validar configuración por ambiente del microintegrador `identityValidatorMS` en repositorio https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-validadorcliente-identidad-conf)

![image-20211118-050508.png](./attachments/image-20211118-050508.png)

En el proceso se solicita una contraseña, en este paso se debe ingresar la definida en la configuración por ambiente, por ejemplo en desarrollo y laboratorio **sarlaftapi.labsura.com**, y se presiona el botón "**OK**"

![image-20211118-050551.png](./attachments/image-20211118-050551.png)

Si todo sale bien, se muestra un mensaje de confirmación indicando que la importación ha sido correcta:

![image-20211118-050730.png](./attachments/image-20211118-050730.png)

Se verá de la siguiente manera en la herramienta:

![image-20211118-051017.png](./attachments/image-20211118-051017.png)

También se debe incluir el certificado público de DataCrédito Experian del ambiente demo y/o producción, dentro del KeyStore, este será entregado por el equipo de Experian de acuerdo el ambiente, o se exporta desde la URL del servicio en el navegador, para que, al momento de utilizarlo en la aplicación, permita la validación de doble vía. Para ello, se debe dar clic en el menú "**Tools**" y la opción "**Import Trusted Certificate**"

![image-20211118-051411.png](./attachments/image-20211118-051411.png)

Se selecciona el certificado enviado por DataCrédito Experian o exportado de acuerdo al ambiente, y se da clic en "**Abrir**"

![image-20211118-051835.png](./attachments/image-20211118-051835.png)

Se le asigna un nombre, que será el HOST del servicio `demo-servicesesb.datacredito.com.co` ambiente demo o `servicesesb.datacredito.com.co` en ambiente productivo, y se debe dar clic en "**OK**"

![image-20211118-052111.png](./attachments/image-20211118-052111.png)

Se muestra un mensaje o alerta indicando que el certificado se ha importado correctamente:

![image-20211118-052211.png](./attachments/image-20211118-052211.png)

Luego se procede a guardar el KeyStore, en el menú "**File**" se debe dar clic en la opción "**Save**", la herramienta solicita el ingreso y confirmación de la contraseña definida previamente, recuerda que en ambiente desarrollo y laboratorio es **sarlaftapi.labsura.com**, y dar clic en "**OK**":

![image-20211118-052823.png](./attachments/image-20211118-052823.png)

Se debe definir el nombre al KeyStore, el nombre de este para todos los ambientes será **experian.jks**, y se debe guardar con la extensión jks, finalmente dar clic en "**Guardar**" en la ubicación seleccionada:

![image-20211118-053130.png](./attachments/image-20211118-053130.png)

## 2.4. Actualizar Keystore en la aplicación IdentityValidator

Importante conocer que los certificados que se usaron para implementar la seguridad en la comunicación con DataCrédito Experian son los siguientes de acuerdo al ambiente:

**LOCAL, DESARROLLO y LABORATORIO:** Se uso el certificado digital de **sarlaftapi.labsura.com**

**PRODUCCIÓN:** Se uso el certificado digital de **validadoridentidad.sura.com.co**

Sobre estos certificados DataCrédito Experian reportará el vencimiento.

### 2.4.1. Actualización de Keystore experian.jks en el repositorio

Para la actualización del Keystore o llavero que combina la llave pública con su respectiva llave privada, en los repositorios de cada ambiente, se deben realizar los siguientes pasos:

#### Repositorio Microintegrador identityValidatorMS:

- Se debe clonar el repositorio del microservicio `identityValidatorMS` https://SuraColombia@dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-validadorcliente-identidad-ms
- Se deberá crear una rama a partir del develop en la cual se realizará la actualización o reemplazo del Keystore llamado `experian.jks` por el nuevo Keystore creado en el punto 2.3. Y se deberá integrar el cambio al ambiente develop, posterior a las pruebas en desarrollo, se debe promover entre ambientes de develop a quality, y de quality a master. (En el desarrollo se uso la estrategia o flujo de trabajo para organizar versiones Git Flow)

![image-20211119-022413.png](./attachments/image-20211119-022413.png)

- Posteriormente abrir el proyecto de la rama creada en el punto anterior en el IDE de su preferencia, se recomienda el uso de Intellij IDEA, una vez abierto y compilado el proyecto en el IDE, se debe realizar la eliminación del archivo llamado `experian.jks`, y reemplazarlo con el nuevo keystore creado en el punto 2.3 con el mismo nombre `experian.jks`, ubicado en la ruta `[RUTA DONDE SE CLONO PROYECTO]\adm_y_fin-validadorcliente-identidad-ms\applications\app-service\src\main\resources`.

  Se deberá integrar dicho cambio desde la rama creada a todas las ramas principales de este repositorio (develop, quality, master), dado que estos primeros pasos son requeridos si luego se quiere realizar una ejecución local. [Ver configuración para ejecución local](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2378924049/Configuraci+n+Ambiente+-+IdentityValidator#Despliegue-local-Identity-Validator)

![image-20211119-021717.png](./attachments/image-20211119-021717.png)

#### Repositorio de configuración de identityValidator

- Se debe clonar el repositorio de CONFIGURACIÓN del microservicio `identityValidatorMS` https://SuraColombia@dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-validadorcliente-identidad-conf
- Se deberá crear una rama de acuerdo al ambiente en la cual se realizará la actualización o reemplazo del Keystore llamado `experian.jks` en el repositorio de configuración.

![image-20211119-022502.png](./attachments/image-20211119-022502.png)

- Recuerda que el KeyStore del certificado digital **sarlaftapi.labsura.com** aplica para local, desarrollo y laboratorio, por ende se deberá actualizar o reemplazar el archivo `experian.jks` en los repositorios de configuración **dev** y **lab**, dado que en local aplica desde el código o repositorio de la aplicación como tal.

- Para producción se debe realizar el proceso de creación del keystore del punto 2.3 con el certificado digital **validadoridentidad.sura.com.co**, por ende se debe integrar la actualización o reemplazo del keystore, que se trata del archivo `experian.jks` de la rama **master**

- Realizar pruebas con el consumo de los siguientes servicios, a los que aplica este tipo de seguridad:

| **Servicio** | **URL Desarrollo** | **URL Laboratorio** | **URL Producción** | **Información adicional** |
| --- | --- | --- | --- | --- |
| [**POST**] Consulta de cliente con Registraduría | https://sarlaftapi.dllosura.com/api/v1/registry/validate | https://sarlaftapi.labsura.com/api/v1/registry/validate | https://sarlaftapi.sura.com.co/api/v1/registry/validate | [Ver documentación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2456289281/IV001+Validar+documento+de+identidad+con+Registradur+a) |
| [**POST**] Consulta de perfil personal de un cliente | https://sarlaftapi.dllosura.com/api/v1/profile/personal | https://sarlaftapi.labsura.com/api/v1/profile/personal | https://sarlaftapi.sura.com.co/api/v1/profile/personal | [Ver documentación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2479816929/IV009+Consultar+perfil+personal+con+Data+Cr+dito+Experian) |
