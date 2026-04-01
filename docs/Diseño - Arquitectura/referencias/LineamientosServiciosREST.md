# Lineamientos para servicios REST

>**Fuente:**[Ver en Confluence](https://segurosti.atlassian.net/wiki/spaces/AR/pages/256672056)
>**Fecha extracción:**2026-03-27

[data-colorid=oqwa705g56]{color:#333333} html[data-color-mode=dark] [data-colorid=oqwa705g56]{color:#cccccc}A continuación se definen los lineamientos que deben tenerse en cuenta para la construcción de servicios web basados en el protocolo**REST**, estos lineamientos derivan del [modelo de madurez de richardson](https://martinfowler.com/articles/richardsonMaturityModel.html), muchos ya están implementados en los artefactos que representan la arquitectura de referencia para aplicaciones transaccionales.

## Importante

Los lineamientos que tengan**ya se encuentran soportados en el LEGO REST

### Semántica

Las URLs deben seguir el siguiente estándar para garantizar un entendimiento común en la construcción de servicios:
![imagen](https://segurosti.atlassian.net/wiki/download/attachments/256672027/estandar_url.png?version=1&modificationDate=1531163152341&cacheVersion=1&api=v2)

**Dominio:**servidor que aloja los servicios

**App/Servicio:**nombre de la aplicación responsable del servicio

**Versión:**descripción de la versión del servicio, ayuda a identificar que servicios están actualizados, cuales han sido eliminados y/o deprecados.

**Recurso:**nombre del recurso que se esta utilizado y sus relaciones, debe ser lo suficientemente descriptivos y fáciles de entender.

#### Modelamiento de los recursos

Esta técnica permite establece los conceptos claves de un servicio, es un proceso similar al modelamiento de datos para una base de datos relacional o el modelamiento clásico de un sistema orientado a objetos, con esto se puede definir la estructura de cada API, por tanto es muy importante tener en cuenta los lineamientos que se explicarán mas abajo.

Existen unos arquetipos que ayudan a modelar los recursos, estos se pueden ver como patrones de diseño que permiten crear estructuras y comportamientos de forma consistente y estandarizadas, a continuación se brinda una breve introducción a cada uno:

_**Document:**_ es el arquetipo base de los otros, por tanto los demás son especializaciones de este, hace referencia a un recurso único.

   Ejemplo:

[http://apisura.segurossura.com/soat/poliza/123](http://apisura.segurossura.com/soat/polizas)

[http://apisura.segurossura.com/soat/poliza/123/tomador](http://apisura.segurossura.com/soat/polizas)

_**Collection:**_ representa a un directorio de recursos gestionados por el servicio (suelen ser maestros), es decir que un consumidor no podría agregar o quitar recursos que existan allí a menos que el servicio lo permita.

   Ejemplo:

[http://apisura.segurossura.com/soat/poliza/ramos](http://apisura.segurossura.com/soat/polizas)

_**Store:**_ representa un repositorio de recursos gestionado por el consumidor, por tanto este ultimo puede ejercer operaciones CRUD sobre este tipo de arquetipos, un _store_ no genera nuevas URLs.

  Ejemplo:

La siguiente URL agregaría una cobertura en la póliza con identificador 123, aquí coberturas seria la _collection_ sobre la cual los consumidores aplican operaciones tipo CRUD

PUT /soat/polizas/123/coberturas

_**Controller Resource:**_ con este arquetipo se puede modelar un concepto procedimental, es decir, se usa para mapear acciones que no se pueden mapear de forma lógica en los 4 métodos estándares CRUD (create, read, update, delete), el _controller_ debe ser el ultimo segmento de la URL por lo que no debe tener recursos hijos.

   Ejemplo:

La siguiente URL muestra un _controller_ resource para reenviar una alerta a un usuario

POST /alerts/45678/resend

Cada recurso de un servicio debe estar alineado con alguno de los arquetipos mencionados anteriormente, por tanto se debe prevenir el uso de formas híbridas para un recurso dado, generalmente cuando se presentan este tipo de situaciones, es mejor dividir el recurso en varios o planear el uso de links.

Ahora, teniendo en cuenta la definición de arquetipos anterior se establecen los siguientes lineamientos:

Los recursos deben ser sustantivos, no verbos

Ejemplo: _/clientes/ en lugar de /crear_cliente_

Los sustantivos deben estar en plural y no en singular

Ejemplo: /clientes en lugar de /cliente

Se debe usar singular cuando nos referimos a un _Document_.

_Ejemplo: /soat/clientes/exito_

Se debe usar plural cuando nos referimos a _Store _o una _Collection_

_Ejemplo: /soat/ciudades_

Los recursos de tipo _Controller_ deben definirse usando verbos

_Ejemplo: /soat/clientes/C1234/notificar-vencimiento_

Usar los verbos del HTTP (GET, POST, PUT, DELETE) para las operaciones sobre las colecciones o elementos. Las URLs no deben exponer operaciones CRUD como parte de su path.

![imagen](https://segurosti.atlassian.net/wiki/download/attachments/256672027/verbos_http.png?version=1&modificationDate=1531164605866&cacheVersion=1&api=v2)
_Ejemplo: DELETE /users/1234_

Los siguientes son antipatrones que violan esta regla:

_- GET /deleteUser?id=1234_

_- GET /deleteUser/1234_

_- DELETE /deleteUser/1234_

_- POST /users/1234/delete_

GET solo debe ser usado para obtener la representación de un recurso

HEAD puede ser usado para obtener la metadata de un recurso

PUT debe ser usado para insertar o actualizar un recurso de un _Store_

POST debe ser usado para crear un nuevo recurso dentro de una _Collection_

POST debe ser usado cuando se definan _Controllers _para mapear acciones que no encajen en los metodos HTTP por defecto.

DELETE debe ser usado cuando se desea eliminar un recurso de un _Collection_ o _Store_

OPTIONS puede ser usado para conocer que otros métodos están disponibles para el recurso indicado.

Si el recurso hace referencia a un elemento puntual se debe indicar de la forma: _/clientes/123 (utilizando la llave primaria)_

Se debe usar separador "/" para indicar las relaciones jerárquicas entre recursos por ejemplo: GET /clientes/123/polizas/456/coberturas

Mantener las relaciones entre recursos de una forma sencilla y entendible. Ejemplo: si queremos realizar operaciones sobre las facturas de un cliente en particular:GET /clientes/7821/facturas

GET /clientes/7821/facturas

POST /clientes/7821/facturas

##### Uso de Querys

Se pueden aplicar criterios de búsqueda sobre una _Collection_ o _Store_

Ejemplo: si deseamos obtener todos los clientes de USA que estén en el estado de California y ciudad San Francisco podemos usar: _GET /clientes?pais=usa&estado=ca&ciudad=sfo_

En el query se puede utilizar información de paginación de una _Collection_ o _Store, _teniendo en cuenta las siguientes variables:

pageSize: define el número máximo de elementos que deben ser devueltos

pageStarIndex: especifica el indice del primer elemento

Ejemplo: GET /polizas?pageSize=20&pageStartIndex=50

###### Tenga en cuenta

Cuando existen requerimientos que llevan a paginaciones o búsquedas con criterios muy complejos, se debe considerar crear un controller resource donde se puedan aceptar entradas complejas como parte del message body de la entidad.

Ejemplo: POST /users/search (en el body se mandan los parámetros)

###### Otros Semántica

En casos muy particulares donde necesito pasar parámetros o generar un mejor entendimiento del recurso, está permitido el uso de Guión medio (-) esta permitido como separador de palabras, ejemplo: /documento/poliza-vida

No se debe hacer uso del Guión bajo (_)

Todas las URLs deben ser definidas en minúsculas

Las URLs no deben incluir extensiones de tipo de archivo, para esto se debe hacer uso adecuado del header Accept

Las URLs no deberían terminar con "/" pues no agregan ninguna semántica, sin embargo, los consumidores que accedan con slash al final deberían redirigir a la URL correcta devolviendo un código HTTP 301

Disminuir la complejidad en el uso de los parámetros con "?", mantenerlo simple para los desarrolladores. Ejemplo: si deseamos obtener todos los clientes de USA que estén en el estado de California y ciudad San Francisco podemos usar:

_GET /clientes?pais=usa&estado=ca&ciudad=sfo_

###### Códigos de estado en respuestas

![imagen](https://segurosti.atlassian.net/wiki/download/attachments/256672027/status_code.png?version=2&modificationDate=1547844555408&cacheVersion=1&api=v2)

El código 201 debe ser usado cuando se crea un recurso sin importar el tipo de petición utilizado (PUT o POST)

El código 202 debe ser usado para indicar que la petición se realizará de forma asíncrona

El código 204 debe ser usado cuando no se envía un "body" como parte de la respuesta a una petición (PUT, POST o DELETE)

El código 200 debería usarse en peticiones exitosas para respuestas especificas donde ninguno de los códigos anteriores es apropiado.

El código 200 no debe ser utilizado para comunicar errores en el "body"

El código 301 indica que la URL que se intenta invocar es diferente y el recurso esta en otra URL, como parte de la respuesta de debe establecer el header "Location" con la nueva ubicación.

El código 303 indica que un _controller _ha terminado su tarea pero en lugar de devolver el "body" devuelve una URL en el header Location

El código 304 se usa cuando existe información asociada con el recurso pero el consumidor ya tiene la versión mas reciente

El código 401 debe usarse para expresar que un consumidor no tiene acceso a un recurso especifico y requiere de un proceso de Autenticación

El código 403 debe usarse cuando un consumidor no tiene los suficientes permisos para acceder a un recurso especifico

El código 404 debe usarse cuando no se puede mapear la URL hacia un recurso

El código 405 debe usarse para indicar que no es posible usar un método HTTP específico cuando se invoca una URL, en la respuesta se debe incluir el header "Allow" indicando los métodos soportados.

El código 406 debe usarse cuando no se puede generar ningún media type solicitado por el cliente en el header "Accept" de la petición

El código 409 debe usarse cuando un consumidor intenta violar el estado de un recurso, ejemplo: aplicar un DELETE hacia un Store que no se puede eliminar si tiene elementos.

El código 412 indica que el consumidor incluyó precondiciones en el header que no se cumplieron, se debería devolver en el "body" una descripción del error

El código 415 debe usarse cuando no se puede procesar el formato del mensaje enviado por el cliente

El código 400 es genérico para errores de lado del cliente, úselo cuando ningún otro código 4xx sea apropiado

El código 500 es error genérico relacionado con mal funcionamiento del servidor

###### Uso de Headers

_Content-Type_ debe ser usado, este valor se refiere al formato encontrado en el body del mensaje de una respuesta o una peticion. Esto le dice al cliente o al servidor como procesar la lectura de los bytes transferidos en el payload del mensaje.

_Content-Length_ puede ser usado, este valor se refiere a la longitud en bytes del mensaje. Es útil primero porque un cliente puede saber si tiene que leer el numero correcto de bytes y segundo porque el cliente puede hacer un HEAD para saber qué tan grande es el mensaje de la respuesta antes que tenga que descargarlo.

_Last-Modified_ puede ser usado, este valor solo aplica a los mensajes de respuesta y representa (en timestamp) la última vez que sucedió algo para alterar el recurso, este header debe estar presente en las respuestas GET y es útil por ejemplo para que el cliente pueda saber si cuenta ya cuenta con la versión más reciente o para que los sistemas de cache puedan llevar a cabo su función.

_ETag _puede ser usado, este valor identifica una versión especifica del estado de una entidad en una respuesta. La entidad es el payload el cual está comprendido de headers y body, este tag podría ser cualquier valor string que cambie junto con el estado de la representación del recurso, este header siempre debería estar presente en las respuestas a peticiones GET. Los consumidores podrían usar este _ETag_ para peticiones futuras o la API podría concluir que el tag de una entidad no ha cambiado y entonces podría ahorrar ancho de banda y tiempo al evitar enviar nuevamente la misma representación.

_Stores _deberían soportor peticiones PUT condicionales, un store utiliza el método**PUT**para actualizar o insertar, lo cual hace difícil para el API conocer la verdadera intención del usuario. A través de headers se provee una alternativa para solucionar cualquier ambig&uuml;edad potencial. El API debe soportar los headers**If-Unmodified-Since**y**If-Match**usados por el cliente para expresar su intención.

Con el header**If-Unmodified-Since**el API procede con la operación solicitada**si y solo si**el estado del recurso no ha cambiado desde el timestamp enviado como valor.

Con el header**If-Match**el API realiza la operación basado en el valor ETag pasado.

_Location_ debe ser usado para especificar la URL de un recurso creado recientemente. En respuestas de tipo**202 ("Accepted")**este header podría usarse para dirigir a los clientes hacia una URL con el estado de una operación asíncrona.

Los headers customizados solo deben ser usados para compartir información. Es decir que no deben ser usados para determinar el éxito o falla de una petición.

###### Uso de media types

Se debe hacer uso del header _Accept _para indicar los tipos de media types que soporta la petición.

###### Representación de recursos

La representación de los recursos se realizará en formato JSON

Se deberá seguir el estándar de estructura que recomienda JSON para la conformación de los recursos ([JSON FORMAT](https://jsonapi.org/format/))

###### Manejo de errores

Dependiendo del escenario se podrán presentar diversos tipos de error, dentro de los cuales tendremos los siguientes:

_Técnicos:_ son aquellos asociados propiamente a las tecnologías utilizadas en la construcción de los servicios, en donde alguno de los componentes (red, servidores, etc) falla y genera algún tipo de indisponibilidad. Normalmente se manejan respuestas HTTP 5XX

_Negocio: _aquellos asociados al proceso o la información de negocio que manejan los servicios, como por ejemplo se esta solicitando información que no existe.

_Formato: _aquellos asociados a la estructura de la información, tipos de datos, objetos o métodos erróneos o que no existen.

_Autenticación:_ aquellos asociados a los procesos de autenticación y autorización de los servicios, como datos de usuarios o recursos a los que no se tiene acceso.

Debe garantizarse una forma clara y consistente de manejo de errores en las peticiones. Se recomienda como parte de la respuesta enviar un arreglo de errores donde cada error contiene el campo**id**que representa un código o texto de error debidamente documentado, el**type**que hace referencia a los tipos previamente mencionados, el**message**que es una descripción básica del error (legible por humanos) y el campo**detail**que contiene un mensaje descriptivo hacia el cliente sobre la causa del error (legible por humanos).

_{ _

_  "errors" : [ _

_     { _

_       "id" : "auth-001",_

_        "type" : "authentication error"_

_        "message" : "Incorrect username or password",_

_       "detail" : "Ensure that the username and password included in the request are correct" _

_     } _

_   ] _

_}_

_Dependiendo del tipo de error se deberá hacer usos de los _[_códigos de estado_](#stateCodes)_ previamente referenciados en este documento_

###### Seguridad

Los recursos expuestos deben estar debidamente asegurados con algún mecanismo de seguridad (Se recomienda el uso de OAuth)

Se puede utilizar una plataforma de API management para la protección de los recursos en una API expuesta a terceros.

###### Composición de respuestas

Se debe dar soporte a escenarios donde un cliente necesite un subconjunto de datos en vez del recurso completo, esto puede ser util para el uso efectivo del ancho de banda muy necesario cuando se desarrollan aplicaciones que cuentan con capacidades de red limitadas como los dispositivos móviles. Para lograr esto el API debe recibir como parte del query el parámetro**fields**donde se indique una lista de campos que deben ser mapeados:

_GET /students/morgan?fields=(firstName, birthDate) HTTP/1.1 _
