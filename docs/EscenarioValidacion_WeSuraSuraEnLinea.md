
## SERVICIO DE VALIDAR SARLAFT

Dirigido a: analistas que implementen la integración del sarlaft 4.0 para canales como WeSura o
SuraEnlinea ó productos de Salud, que envían la información de asegurados en un posterior request.
Contexto Servicio: Validar Sarlaft
Permite realizar las validaciones mínimas para clasificar el riesgo de un cliente y determinar el tipo
de sarlaft que debe diligenciar de acuerdo con la naturaleza del cliente y del producto.
URL Desarrollo: https://sarlaftapi.dllosura.com/sarlaftserv/assessment
URL Laboratorio: https://sarlaftapi.labsura.com/sarlaftserv/assessment
Perfil de Consulta: PF_CONSUMSERVSARLAFTAPI del SP Sarlaft4
Datos de Entrada:
Descritos en el documento DocumentacionTecnicaSarlaft, URL Confluence
(https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070150/Descripci+n+de+Interfaces+P
rincipales)
Escenario de WeSura y SuraEnLinea: Para estos canales se crea la propiedad infoPendiente, para
recrear el siguiente flujo:
1. Se invoca al servicio de assessment con los datos del tomador y la propiedad infoPendiente
en true.
2. Se invoca el servicio de assessment con los datos del tomador y cada una de las figuras
restantes (asegurados, beneficiarios, afiliados, afianzado o mandatorio) enviando el
evaluacionId retornado por el servicio en el paso 1 tomador y la propiedad infoPendiente
en true.
3. Se invoca el servicio de assessment con los datos de la última figura del negocio, enviando
evaluacionId retornado por el servicio en el paso 1 y la propiedad infoPendiente en false.
La integración con el WebComponent desarrollado por sarlaft, implica que la data de negocio sea
enviada con estas propiedades al componente, y sea este último quien se encargue de consumir el
API de Sarlaft para:
1. Consumir el ws de validación saralft: /sarlaftserv/assessment
2. De acuerdo con la respuesta de la evaluación presentar o no el formulario correspondiente.
3. Si el formulario debe diligenciarse el componente debe consumir el api de sarlaft para
construir el formulario y guardar la información correspondiente.
Seguridad:
La seguridad del webcomponent será manejada a través de un token JWT, dado que estos canales
no poseen seguridad basada en Seus 4.
Escenario de Productos de Salud:
Para estos productos donde primero se envía al ws de validación sarlaft (assessment) la información
del tomador y en un posterior paso se envían las demás figurasm se crea la propiedad
infoPendiente, para recrear el siguiente flujo:
1. Se invoca al servicio de assessment con los datos del tomador y la propiedad infoPendiente
en true.
2. Se invoca el servicio de assessment con los datos del tomador y cada una de las figuras
restantes (asegurados, beneficiarios, afiliados, afianzado o mandatorio) enviando el
evaluacionId retornado por el servicio en el paso 1 tomador y la propiedad infoPendiente
en true.
3. Se invoca el servicio de assessment con los datos de la última figura del negocio, enviando
evaluacionId retornado por el servicio en el paso 1 y la propiedad infoPendiente en false.
Solo cuando el ws de validación sarlaft (assessment) recibe la notificación de terminación, se
consolidan los resultados para ser comunicados con el webhook de finalización de proceso de
sarlaft.