
## INTEGRACIONES MASIVAS

Dirigido a: analistas que implementen la integración del sarlaft 4.0 desde aplicativos como canales
masivos o que requieran hacer una integración enviando grandes cantidades de pólizas.
Aplica para expedición de pólizas colectivas o pólizas individuales con una gran cantidad de riesgos.

## SERVICIO VALIDAR SARLAFT MASIVO

Permite validar el estado del sarlaft de un cliente para un proceso de validación, enviando varios
negocios en una sola invocación, el tamaño máximo permitido es de 100 pólizas. Es un proceso
asíncrono. Aplica para expedición de pólizas colectivas que tienen muchos riesgos o pólizas
individuales con una gran cantidad de riesgos.
URL Desarrollo: https://sarlaftapi.dllosura.com/sarlaftserv/assessment/massive
URL Laboratorio: http://sarlaftapi.labsura.com/sarlaftserv/assessment/massive
Perfil de Consulta: PF_CONSUMSERVSARLAFTAPI del SP Sarlaft4
Datos de Entrada:
Se recibirá una lista de negocios, como payload, con los mismos campos descritos en el servicio de
Validar Sarlaft explicados en el documento DocumentacionTecnicaSarlaft, sección 6. INTERFACES

## DE SERVICIO.

(URL Confluence
https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070150/Descripci+n+de+Interfaces+Pr
incipales)
Datos de Entrada:
Datos de Salida:

| Campo | Obligatorio | Descripción |
| --- | --- | --- |
| payload (payload) | SI | String con el json de acuerdo con la estructura del ws de validar sarlaft (assessment) y el campo numeroMensaje. Ejemplo del JSon en la página 3 del presente documento. |

| Campo | Descripción |
| --- | --- |
| ProcesoIniciado (procesoIniciado) | True: el proceso de validación se ha iniciado correctamente. False: ocurrió un error iniciando el proceso de inicio de validación. |


## MENSAJE VALIDAR SARLAFT MASIVO

Permite validar el estado del sarlaft de un cliente para un proceso de validación, enviando varios
para
de
Servidor RabbitMQ Sura DLLO: msgdllo.suramericana.com.co
Servidor RabbitMQ Sura LABO: msglab.suramericana.com.co
Servidor RabbitMQ Sura PDN: msg.suramericana.com.co
Exchange: seguros.sarlaft.masivo
Rounting key: seguros.sarlaft.masivo.assessment
Usuario de Conexión: Cada aplicativo cliente debe crear su usuario de conexión con permisos de
escritura sobre el Exchange:
Datos de Entrada:
Se recibirá una lista de negocios, como payload, con los mismos campos descritos en el servicio de
Validar Sarlaft explicados en el documento DocumentacionTecnicaSarlaft, sección 6. INTERFACES

## DE SERVICIO.

(URL Confluence
https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070150/Descripci+n+de+Interfaces+Pr
incipales)
Datos de Entrada:

|  |  | Aplica para |
| --- | --- | --- |
| también para expedición de pólizas colectivas o pólizas individuales con una gran cantidad de |  |  |
| riesgos. | Es un proceso asíncrono por medio de mensajería de RabbitMQ |  |

| Campo | Obligatorio | Descripción |
| --- | --- | --- |
| numeroMensaj e | NO | Número de mensaje actual dentro del total de peticiones enviada en el servicio de /assessment/massive/start. En caso de no tener envio por lotes seria enviado vacio. |
| payload (payload) | SI | String con el json de acuerdo con la estructura del ws de validar sarlaft (assessment) |

Ejemplo:
{
"numeroMensaje": "1",
"solicitudEvaluacion" : " [{
"solicitudDni": "C990199",
"codigoOperacion": "01",
"codigoAplicacion": "118",
"negocioId": "0145451",
"tomador": {
"cliente": {
"tipoPersona": "N",
"correo": "mail_1@mail.com.co",
"celular": "3102345670",
"razonSocial": null,
"documento": {
"tipo": "C",
"numero": "990199",
"fechaExpedicion": "2007-05-27"
},
"persona": {
"primerNombre": "Nestor",
"segundoNombre": "Fernando",
"primerApellido": "Arevalo",
"segundoApellido": "Espitia",
"pais": "01"
},
"relaciones": [
]
}
},
"asegurados": [],
"beneficiarios": [],
"polizas": [
{
"codigoRamo": "1",
"codigoProducto": "1",
"codigoCanal": "1",
"valorAsegurado": 500000,
"valorPrima": 500000,
"medioPago": "PSE",
"negocio": "COLECTIVO",
"coaseguro": false,
"codigoOficina": "00"
}
]
}]
}

## SERVICIO INICIAR PROCESO MASIVO

Permite iniciar el proceso de evaluación de evaluación de sarlaft masivo para una póliza colectiva o
una póliza individual, que tienen muchos riesgos, y donde se hace necesario dividir los payloads en
varias solicitudes.
Este servicio debe consumirse solo si el proceso de validación de sarlaft, debe recibir varios lotes,
en caso contrario omitir este consumo.
En los casos que aplique se debe consumir como primer paso, tanto si la integración se va a realizar
por API o como si se va a realizar por mensajería en RabbitMQ.
URL Desarrollo: https://sarlaftapi.dllosura.com/sarlaftserv/assessment/massive/start
URL Laboratorio: http://sarlaftapi.labsura.com/sarlaftserv/assessment/massive/start
Perfil de Consulta: PF_CONSUMSERVSARLAFTAPI del SP Sarlaft4
Datos de Entrada:
Datos de Salida:

| Campo | Obligatorio | Descripción |
| --- | --- | --- |
| totalMensajes | SI | Total de mensajes o peticiones para el proceso de evaluación masivo. |
| codigoAplicacion | SI | Código de aplicación que inicia el proceso de validación. |
| identificadorNegocio | SI | Identificador de negocio para hacer trazabilidad a la solicitud de carga masiva |

| Campo | Descripción |
| --- | --- |
| evaluacionID | Identificador de la evaluación iniciada, este identificador debe enviarse siempre en cada mensaje a rabbitmq o petición al servicio rest, para indicar a que proceso pertenece. |

A continuación, se realiza la explicación de los servicios webhook que deben exponer los aplicativos
que consuman este servicio de validación masivo.
El primer servicio webhook permite retornar el resultado del proceso de evaluación para todo el
lote enviado.
El segundo servicio webhook permite retornar el resultado del proceso de terminación de sarlaft
exitoso por cada negocio, es decir que si se envía un paquete de 100 pólizas para validar saralft, el
aplicativo de negocio debe esperar un llamado al webhook de evaluación y 100 llamados
independientes al webhook de finalización de sarlaft. En resumen:

## PROCESO EVALUACIÓN:

1. pólizas individuales: Un callback por lote, cada lote tiene el resultado de n pólizas
2. Pólizas colectivas: Un callback por póliza, al finalizar la evaluación de todos los lotes del total
indicado.

## PROCESO FINALIZACION SARLAFT:

1. Pólizas individuales: Un callback por cada póliza
2. Pólizas colectivas: Un callback por cada póliza.

## INTERFAZ DE SERVICIO WEBHOK PARA RETORNAR RESULTADO DE LA EVALUACIÓN

Cada aplicativo de negocio que utiliza el aplicativo de Sarlaft 4.0 deberá exponer un servicio Rest
Post seguro con Seus 4 con la siguiente interfaz de servicio, el cual permitirá retornar el resultado
del lote solicitado a evaluar sarlaft.
Por medio de esta interfaz el aplicativo de Sarlaft 4.0 comunicará:
1. El proceso de evaluación ha terminado, pero pueden existir pendientes para terminar el
sarlaft, en estado caso el campo processStatus se encontrará en estado pendiente y dentro
de cada figura (rol) indicará los pendientes o controles necesarios.
Encabezado:

| Campo | Descripción |  |
| --- | --- | --- |
| mensajeError | Mensajes de error cuando se inclumple el tamaño de negocios recibido |  |
|  | por mensaje, en ese caso no se realizará ningún procesamiento. |  |
| negocios | Resultado de las evaluaciones para todas las pólizas enviadas en el lote. |  |

Por cada resultado de póliza dentro de la lista de bussiness se encontrarán:
El servicio devolverá un listado con este conjunto de datos por cada figura que se evalúo en el
proceso de evaluación.

| Campo | Descripción |
| --- | --- |
| evaluacionId | Identificador del proceso de evaluación realizado. Permite agrupar todas las evaluaciones de sarlaft realizadas sobre las figuras de un proceso de negocio. |
| estado | Estado de la evaluación del sarlaft FINALIZADO: todo el proceso de sarlaft ha finalizado y se puede seguir con el proceso de expedición. |
|  | PENDIENTE_ACCION_MANUAL: hace falta solo un paso para completar |
|  | el sarlaft, de forma manual por el aplicativo cliente, solo aplica para |
|  | procesos especiales. |
| mensajeError | Mensaje de error si ocurrió algún problema en el procesamiento de la |
|  | evaluación o algún dato de entrada es invalido. En caso no de presentarse |
|  | ningún error se enviará vacío. |

| idNegocio | Identificador de negocio propio del aplicativo que expide o renueva. |
| --- | --- |
| url | URl para diligenciar el saralft |

| Campo | Descripción |
| --- | --- |
| dni | Dni de la persona para la cual se solicita el sarlaft. |
| estado | FINALIZADO: todo el proceso de sarlaft ha finalizado y se puede seguir con el proceso de expedición. |
|  | PENDIENTE_ACCION_MANUAL: hace falta solo un paso para completar |
|  | el sarlaft, de forma manual por el aplicativo cliente, solo aplica para |
|  | procesos especiales. |

fechaActualizacion Fecha de actualización del último sarlaft del cliente.
Null para cuando no se tenga información de fecha de actualización.
Se espera una respuesta de tipo 200 OK con el siguiente json, en caso de que la recepción haya sido
exitosa.
{
"recibido":"",
"mensajeError" : ""
}

| formularioRequerido | true: Indica que el Sarlaft del cliente esta desactualizado y de acuerdo con su nivel de riesgo debe ser diligenciado. false: Indica que el Sarlaft del cliente esta actualizado o que de acuerdo con su nivel de riesgo no es necesario actualizar más información. |
| --- | --- |
| Controles : control | Código de validación no superada, por ejemplo: IDENTITY (validación de identidad) Posibles Valores: IDENTITY: Validación de identidad |
| Controles: mensajeControl | Descripción de la validación no superada. |

| Campo | Descripción |
| --- | --- |
| received | True: se confirma la recepción de la notificacion False: ocurrio un error y la notificacion debe ser reenviada. |
| messageError | Mensaje de error en caso de presentarse cuando el campo received es false |


## INTERFAZ DE SERVICIO WEBHOOK

Cada aplicativo de negocio que utiliza el aplicativo de Sarlaft 4.0 deberá exponer un servicio Rest
Post seguro con Seus 4 con la siguiente interfaz de servicio:
Por medio de esta interfaz el aplicativo de Sarlaft comunicará:
1. Todo el proceso de sarlaft ha terminado y está completo para todas las figuras inmersas en
el proceso de evaluación. Para este caso el campo processStatus estará en Finalizado
(FINALIZADO) e indica que la póliza puede expedirse.
2. Todo el proceso de sarlaft ha terminado, pero alguna de las figuras pudo no haber pasado
la validación de identidad, para este caso el estado estará en rechazado (RECHAZADO).

| Campo | Descripción |  |
| --- | --- | --- |
| evaluacionId | Identificador del proceso de evaluación realizado. Permite agrupar todas las evaluaciones de sarlaft realizadas sobre las figuras de un proceso de negocio. |  |
| estado |  | Estado de la evaluación del sarlaft |
|  |  | PENDIENTE_ACCION_MANUAL: hace falta solo un paso para |
|  |  | completar el sarlaft, de forma manual por el aplicativo cliente, solo |
|  |  | aplica para procesos especiales. |
|  |  | FINALIZADO: todo el proceso de sarlaft ha finalizado y se puede seguir |
|  |  | con el proceso de evaluación. |
|  |  | RECHAZADO: todo el proceso de sarlaft ha finalizado, pero NO se |
|  |  | puede expedir dado que alguna de las figuras no paso la validación de |
|  |  | identidad o tiene un control bloqueante. |
| idNegocio | Identificador de negocio propio del aplicativo que expide o renueva. |  |
| Datos de cada una de las figuras de la póliza |  |  |
| dni | Dni del cliente |  |

Se espera una respuesta de tipo 200 OK con el siguiente json, en caso de que la recepción haya sido
exitosa.
Notificación a través de mensajería RabbitMQ
Cuando la integración de notificación de resultado de evaluación y notificación de terminación del
sarlaft, no se realice a través del mecanismo webhook, el aplicativo cliente deberá implementar un
mecanismo de comunicación a través de RabbitMQ Sura, bajo los siguientes lineamientos:
1. Los mensajes para comunicar serán iguales a los json expuestos en la anterior sección para
los dos webhooks.
2. Al usar el mecanismo de RabbitMQ, la aplicación cliente debe garantizar el
procesamiento del mensaje y gestionar los posibles errores, indisponibilidades de
plataformas, tiempos de respuesta, etc. NOTA: Para el caso del webhook, esta
responsabilidad recae sobre el bus de mensajería propio del Sarlaft para garantizar la
entrega del mensaje al servicio destino.
será
y

| estado | FINALIZADO: Terminado, SE PUEDE EXPEDIR PENDIENTE_ACCION_MANUAL: Para procesos especiales. RECHAZADO: no se puede expedir |
| --- | --- |
| Controles : control | Código de validación no superada, por ejemplo: IDENTITY (validación de identidad) Posibles Valores: IDENTITY: Validación de identidad |
| Controles : mensajeControl | Descripción de la validación no superada. |

| Posibles Valores: |
| --- |
| IDENTITY: Validación de identidad |

| Campo | Descripción |
| --- | --- |
| recibido | True: se confirma la recepción de la notificacion False: ocurrió un error y la notificación debe ser reenviada. |
| mensajeError | Mensaje de error en caso de presentarse cuando el campo received es false |

| 3. En el caso que una aplicación cliente escoja notificaciones via RabbitMQ, ésta será |  |
| --- | --- |
|  | responsable de crear la cola con binding al Exchange indicado y usuarios de conexión y |
|  | entregar éstos al equipo base del Sarlaft para matricularlos en el api de Sarlaft. |

Exchange: seguros.sarlaft.finalizacion
Exchange: seguros.sarlaft.evaluacion

| Para recibir mensajes de finalización por favor suscribir una cola al siguiente Exchange y |
| --- |
| rounting key en RabbitQM Sura |

| Para recibir mensajes de evaluación por favor suscribir una cola al siguiente Exchange y |
| --- |
| rounting key en RabbitQM Sura |
