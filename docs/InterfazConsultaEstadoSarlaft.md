
## SERVICIO PARA CONSULTAR ESTADO SARLAFT

Dirigido a: analistas que implementen la integración del sarlaft 4.0 en tecnologías para las cuales no
puedan exponer un ws de webhook, el cual permite hacer el callback de notificación exitosa de
terminación del sarlaft. En este caso la responsabilidad queda del lado del aplicativo de negocio en
consultar el estado del proceso de sarlaft para conocer si puede o no expedir.
Contexto Servicio: Consultar Estado Sarlaft
Permite consultar el estado del sarlaft de un cliente para un proceso de validación.
Este
equipo
URL Desarrollo: https://sarlaftapi.dllosura.com/sarlaftserv/assessment/checkStatus
URL Laboratorio: http://sarlaftapi.labsura.com/sarlaftserv/assessment/checkStatus
Perfil de Consulta: PF_CONSUMSERVSARLAFTAPI del SP Sarlaft4
Datos de Entrada:

| Este servicio solo será para ciertos procesos de negocio, que sean validados y aprobados por el |
| --- |
| equipo de TI del aplicativo Sarlaft 4.0. De lo contrario se denegará su uso. |

| Campo | WS | Obligatorio | Descripción |
| --- | --- | --- | --- |
| DNI | dni | NO | DNI del cliente para el cual se desea conocer el estado del proceso de Sarlaft |
| IDEvaluación | evaluacionId | SI | Identificador del proceso de evaluación, devuelto por el servicio de validación salaft. |
| Código de aplicación | codigoAplicacion | SI | Código de aplicación que realiza la consulta. |
| ConsultarEstadoSarlaftRoles | consultarEstadoSarlaftRoles | NO | True: el servicio devolverá la discriminación del estado del |

Datos de Salida:
Cuando en la solicitud se envía el campo DNI o ConsultarEstadoSarlaftRoles en true, se obtienen
una lista con estos campos en la respuesta:

|  |  |  | sarlaft, para cada uno de las figuras dentro del proceso de sarlaft identificado por el campo IDEvaluación False: el servicio devolverá solo el estado del proceso de evaluación identificado por el campo IDEvaluación |
| --- | --- | --- | --- |

| Campo | Descripción |
| --- | --- |
| EstadoProcesoEvaluación (estado) | True: proceso de saraft completo para todas las figuras evaluadas. False: el proceso de sarlaft tiene pasos pendientes |
| Mensaje (mensaje) | Mensaje en caso de presentarse un error |

| Campo | Descripción |
| --- | --- |
| DNI (dni) | Dni de la persona para la cual se solicita el sarlaft. |
| ProcesoValidacion (procesoValidacion) | True: proceso de validación y evidencias completo. False: el proceso de validación tiene pasos pendientes |
| Formulario (formulario) | FINALIZADO: proceso de diligenciamiento completo. PENDIENTE: el formulario e saraft no ha sido diligenciado. |
| EstadoSarlaft (estado) | FINALIZADO: el cliente tiene un sarlaft vigente. Este campo solo será vigente cuando los atributos ProcesoValidacion, y Formulario son true PENDIENTE: el cliente no tiene un sarlaft vigente RECHAZADO: El cliente tiene un control bloqueante |
| FechaTerminacionProceso (fecha) | Fecha del sarlaft actualizado. Null si el sarlaft no se encuentra vigente |
