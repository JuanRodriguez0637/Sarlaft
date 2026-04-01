# DocumentacionTecnicaSarlaft

SARLAFT 4.0

## Propósito

El propósito de este documento es dar a conocer a los equipos de tecnología, un contexto de la arquitectura del nuevo aplicativo de Sarlaft 4.0 y los mecanismos de integración definidos, para que desde los aplicativos que dan soporte a los procesos de asesoría y ventas, expedición, modificación y renovación de pólizas puedan validar y solicitar el sarlaft a un cliente, dando cumplimiento a la nueva norma de Sarlaft 4.0.

## Versiones

| Número de Versión | Descripción de Cambios |
| --- | --- |
| 1.0 | Esta es la primera versión del documento, continuará en refinamiento dependiendo de la retroalimentación recibida por parte de los equipos |
| 1.1 | 6. INTERFACES DE SERVICIO. Servicio Validación Sarlaft. Cambio Obligatoriedad y Descripción campos Respuesta Pregunta PEPS y Respuesta Pregunta Beneficiario. 6. INTERFACES DE SERVICIO. Servicio Validación Sarlaft. - Adición campo de Figura, utilizado para validación de listas vinculantes de asegurados en pólizas colectivas, 6. INTERFACES DE SERVICIO. Nuevos Servicios de Almacenar Evidencias y Consultar Sarlaft. |
| 1.2 | 6. INTERFACES DE SERVICIO. Servicio Validación Sarlaft: Se elimina dato de entrada del DNI. Aclaración el campo de Fecha Expedición y País de Nacimiento solo aplican para persona natural. Ampliación datos de Preguntas PEPS. Adición pregunta mandatorio |
| 1.3 | 6. INTERFACES DE SERVICIO. Se crea agrupación de validación de sarlaft para todas las figuras de una operación de negocio. Esto cambia los datos de entrada y salida de cada uno de los servicios. Explicación Escenario de modificación del proceso de Evaluación: |
| 1.4 | 6. INTERFACES DE SERVICIO: Ajuste interfaz servicios adicionar evidencias e iniciar proceso actualización. Adición de url de los ambientes de desarrollo y laboratorio. Especificación del formato json aceptado por los servicios WebHook, cuando el aplicativo de sarlaft notificará la finalización de un proceso de sarlaft. |
| 1.5 | 6. INTERFACES DE SERVICIO: Mapeo de los campos de las interfaces con la implementación de los servicios |
| 1.6 | En el servicio de validar saralft : Se eliminan los campos de Forma de pago, Respuesta Pregunta Beneficiario y Respuesta Pregunta mandatorio. Adición campo cdagente Se adiciona figura de Afiliado y Afianzado, Se ajustan las preguntas PEPS Se adicionan los campos de país de constitución, respuesta pregunta relación laboral. El ws de assesment devuelve solo una url para diligenciamiento del formulario. Se ajusta interfaz del servicio webhook y se dan lineamiento para notificación por RabbitMQ Se ajusta ws de consultar sarlaft. Se expone el api en español Ajuste datos de entrada para el webcomponent |

| 1.7 | Adición campos en el ws assesment: licitación pública, tipo coaseguro, porcentaje de participación, El campo segundo apellido queda como no obligatorio. El nro de celular solo es obligatorio para persona natural. El campo correo electrónico de empresa, recibe el correo de contacto de esta. El campo de medio de recaudo será valor DEBITO_AUTOMATICO, cuando aplique Webhook   Queue:    especificación    de    exchanges    para    hacer    los    bindings correspondiente y escuchar los mensajes pertinentes. |
| --- | --- |
| 1.8 | Cambios en la interfaz del servicio de assessment: campo asesor pasa a obligatorio. Cambio campos en el modulo peps, Adición campo plan (Canal digital), Campos opcionales para AR. Eliminación campos indicadorPorcentaje y tipoPorcentaje Adición pregunta peps para persona natural y peps administradores para persona jurídica. Eliminación sección “SERVICIO PARA INICIAR PROCESO ACTUALIZACION”. |

- NECESIDAD

El proyecto de Sarlaft 4.0 surge por la necesidad de dar cumplimiento a la ***Circular****** ******básica****** ******027****** ******del****** ******2020****** ******(SARLAFT 4.0) emitida el 02 de septiembre del 2020 por la ******Superintendencia Financiera***, la cual cambia la regulación en relación con la prevención del lavado de activos y se establecen mecanismos diferentes de conocimiento del cliente de acuerdo con su naturaleza de riesgo, exigiendo a las entidades tener este conocimiento del cliente al momento de su vinculación. A su vez mantener la información actualizada de acuerdo con la vigencia del sarlaft que puede ser entre 1 y 3 años de acuerdo con la clasificación del riesgo del cliente, también establecer mecanismos de monitoreo de la información recolectada de tal forma que se puedan generar alertas en el proceso de prevención de lavados de activos.
Estos cambios regulatorios dan origen a que en ***SURA ***surja el proyecto de Saralft 4.0, que pretende centralizar los procesos de evaluación del riesgo y captura de información del sarlaft de un cliente, manteniendo las evidencias, trazabilidad de las validaciones y cambios en los datos. Estableciendo los mecanismos de integración hacia procesos de reporte y monitoreo que la compañía disponga como prevención del lavado de activos.
El Sarlaft 4.0 aplica de forma obligatoria para todos los clientes que deseen adquirir un producto por cualquier canal con Sura, siendo este proceso de vinculación intervenido con la evaluación y clasificación del riesgo, de tal forma que se pueda identificar qué tipo de formulario debe diligenciar de acuerdo con su clasificación (simplificado, ordinario e intensificado). A su vez requiere intervenir también los procesos de modificaciones valorables y renovaciones, con el objetivo de mantener la información actualizada de un cliente e identificar posibles cambios de niveles de riesgo.

## REQUISITOS NO FUNCIONALES

Basados en los requisitos funcionales que debe cumplir la plataforma de Sarlaft y la criticidad de esta, se listan a continuación las cualidades no funcionales del sistema que representan la percepción del negocio en cuanto a sus expectativas de calidad operacional y que acompañan las expectativas funcionales    del    sistema.

| CRÍTICOS | Escalabilidad | El aplicativo de Sarlaft será incorporado como un paso obligatorio en los procesos de expedición, renovación y reclamación en todos los productos o ramos de Seguros obligatorios y voluntarios y por ende, debe ser capaz de atender todas las solicitudes que se reciban de las aplicaciones de negocio que se integren con el aplicativo de Sarlaft. |
| --- | --- | --- |
| CRÍTICOS | Disponibilidad | Se requiere disponibilidad 24/7 para cubrir las disponibilidades que tienen las aplicaciones de negocio que usarían el aplicativo de Sarlaft. |
| CRÍTICOS | Interoperabilidad | El aplicativo de Sarlaft se integrará con múltiples plataformas de negocio por lo cual se debe contar con un API de servicios que permita consumir la experiencia de Sarlaft en todas las aplicaciones de negocio que requieran usar la plataforma. |
| CRÍTICOS | Seguridad | Sarlaft solicitará y almacenará información sensible de los clientes la cual se debe proteger por medio de control de acceso a usuarios no autorizados,    cifrado    y encriptación de datos durante el tránsito y en reposo. |
| CRÍTICOS | Integridad de la Información | Se debe garantizar la consistencia de la información recolectada de los clientes según las disposiciones de la Superintendencia Financiera para evitar consecuencias negativas por auditorias que la Superintendencia    pueda |

|  |  | realizar a la implementación de Sarlaft 4.0 |
| --- | --- | --- |
|  | Modularidad | El aplicativo de Sarlaft debe contar con mecanismo de protección contra el impacto sobre cambios externos, generalmente solicitados por la Superintendencia Financiera de Colombia. |
| NO CRÍTICOS | Operabilidad | El aplicativo de Sarlaft debe contar mecanismos de autogestión para el 90% o más de las tareas de mantenimiento, se puedan hacer vía parametrización delegada a los usuarios funcionales. |
| NO CRÍTICOS | Auditabilidad | Todas las transacciones que se realicen el aplicativo de Sarlaft, deben ser auditadas indicando la fecha de operación, tipo de operación y usuario que ejecuta la operación |
| NO CRÍTICOS | Idoneidad Funcional | El aplicativo de Sarlaft debe implementar todos los requisitos    funcionales necesarios para lograr la implementación del Sarlaft en la organización y cumplir las disposiciones legales de la superintendencia financiera de Colombia. |
| NO CRÍTICOS | Flexibilidad de la UI | La experiencia del usuario de Sarlaft debe estar enriquecida con controles interactivos y flujo de navegación amigable que faciliten al máximo el uso del aplicativo. |

## ARQUITECTURA

El presente diagrama muestra una vista general del diseño realizado para el aplicativo de Sarlaft donde se caracterizan cada uno de los componentes que intervienen y sus responsabilidades. La imagen a continuación sirve como referencia para entender como está construido el sistema y la complejidad que involucra a nivel de integración para poder ofrecer las funcionalidades requeridas para la gestión del Sarlaft.

Del anterior diagrama se pueden identificar los siguientes componentes principales:

- API: incluye todos los servicios Rest requeridos para brindar las funcionalidades de Sarlaft a las aplicaciones de negocio y aliados.
- Frontend: capa de presentación que incluye los formularios para diligenciar la información del Sarlaft (via webcomponent o página web) y exposición del API a través de Apigee.
- Broker, Event Hub: bus de mensajería interno a la aplicación para la recolección de evidencias vía integración con sistemas internos y externos a Sura y que son requeridos para completar el Sarlaft.
- Cache: componente que permite optimizar las integraciones requeridas para completar un Sarlaft, evitando hacer llamados a las aplicaciones que requiere la plataforma para la obtención de evidencias.
- Modelo Sarlaft: repositorio de los sarlaft diligenciados para cada cliente.
- WebhookNotificator: Mecanismo de integración tipo Callback via Webhook que permite al aplicativo de Sarlaft notificar a las aplicaciones de negocio cuando un formulario de Sarlaft está finalizado; para que así, puedan finalizar su proceso comercial.

## PASOS DE SARLAFT

Esta sección busca aclarar el proceso de evaluación y captura de información del sarlaft, para un escenario de vinculación de un cliente que no tenga sarlaft vigente y este deba ser diligenciado:

- Proceso Asesoría/Ventas: paso en el cuál un cliente realiza una solicitud de póliza por medio de una aplicación de negocio donde debe validar de forma obligatoria si un cliente requiere o no requiere sarlaft. Esta validación la puede realizar por medio de un servicio rest del API del aplicativo de Sarlaft.
- Validaciones Mínimas: paso ejecutado por el aplicativo de Sarlaft 4.0, donde se realizarán las validaciones mínimas requeridas por la norma y clasificará al cliente en un nivel de riesgo. Las validaciones con registraduría/ cámara de comercio a pesar de ser parte de las validaciones mínimas será completadas en un paso posterior por el aplicativo de Sarlaft y no afectarán la disponibilidad del sistema. Es posible que el proceso de sarlaft finalice en este punto cuando el cliente ya tiene un Sarlft vigente.
- Diligenciar Formulario: paso invocado desde el aplicativo cliente para abrir el formulario expuesto por el aplicativo de Sarlaft 4.0, constituye un formulario dinámico, que prediligenciará la información del cliente, en caso de existir en base de datos del modelo de Clientes de Sura o en base de datos externas autorizadas para tal fin.
- Almacenar Sarlaft: paso en el cual el aplicativo de Sarlaft 4.0, se encarga de almacenar la información del cliente, evidencias y trazabilidad, completar los requisitos creados de acuerdo con el nivel de riesgo y adjuntar evidencias de estos soportes a P8. Estas integraciones internas son realizadas de forma asíncrona para no afectar los procesos de vinculación.
- Notificar Resultado Proceso: paso de callback donde vía webhook el aplicativo de Sarlaft 4.0 notifica al aplicativo cliente que el proceso de sarlaft ha finalizado. Un proceso de sarlaft finalizado incluye validaciones mínimas, actualización de datos y almacenamiento de evidencias.

## TIPOS DE INTEGRACIÓN

En este gráfico se encuentran los mecanismos de integración expuestos por el aplicativo de Sarlaft, para dar soporte al requerimiento de conocimiento del cliente en cada uno de los procesos de negocio y que de acuerdo con la plataforma tecnológica se pueda escoger el más conveniente.
Para aplicativos cliente-servidor se plantea un escenario de integración en el punto 7 del presente documento.

## INTERFACES DE SERVICIO

**SERVICIO**** ****VALIDAR**** ****SARALFT**
Permite realizar las validaciones mínimas para clasificar el riesgo de un cliente y determinar el tipo de sarlaft que debe diligenciar de acuerdo con la naturaleza del cliente y del producto.
URL Desarrollo: POST  **<https://**> **apiinternal.dllosura.com****/****sarlaft/v1/evaluaciones**
URL Laboratorio: POST

Seguridad: Solicitar el apikey de consumo en apigee.
** ****Datos**** ****de**** ****Entrada:**
Para su mayor claridad se documentan los datos de entrada por secciones.
Datos de entrada correspondientes a cada una de las Figuras dentro de un negocio, por ejemplo, cuando tomador, asegurado y beneficiario son diferentes. También se recibe información de los afianzados, afiliado y representante legal, para los negocios en los que aplique estas figuras.

| Tomador | tomador | tomador | tomador | tomador |
| --- | --- | --- | --- | --- |
| Asegurado | asegurados | asegurados | asegurados | asegurados |
| Beneficiario | beneficiarios | beneficiarios | beneficiarios | beneficiarios |
| Afianzado | afianzado | afianzado | afianzado | afianzado |
| Afiliado | afiliado | afiliado | afiliado | afiliado |
| Representante Legal | tomador: | cliente: | asociaciones | asociaciones |
| Representante Legal | con tipoAsociacion: | con tipoAsociacion: | con tipoAsociacion: | AGENTE_LEGAL |

Si el tomador o cualquier cliente tiene dos figuras dentro de la póliza, deben enviarse los datos de igual forma en el campo correspondiente. Por ejemplo, si el tomador es el mismo asegurado y beneficiario, estos datos deben enviarse en los campos de asegurado y beneficiario.

Datos correspondientes a los clientes que tiene algún rol dentro de la póliza. Se debe enviar como mínimo el tomador. En caso de enviarse asegurados para un mismo negocio, siempre debe enviarse el tomador.

| Campo | WS | Obligatorio | Descripción |
| --- | --- | --- | --- |
| Tipo    de Identificación | Cliente:    documento: tipo | SI | Tipo de Identificación. Revisar página de Catalogo: Tipo de documento |
| Nro    de Identificación | Cliente:    documento: numero | SI | Nro de Identificación. |
| Primer Nombre | Cliente:    persona: primerNombre | Es obligatorio solo    para persona Natural | Primer Nombre. Es obligatorio   para   todas   las figuras en caso de que sean persona natural. Formado solamente por una palabra. |

| Segundo Nombre | Cliente:    persona: segundoNombre | NO | Segundo Nombre. Puede estar conformado por varias palabras. |
| --- | --- | --- | --- |
| Primer Apellido | Cliente:    persona: primerApellido | Es obligatorio solo    para persona Natural | Primer Apellido. Es obligatorio para todas las figuras en caso de que sean persona natural. Hay dos casos válidos: - Esta formado por solo una palabra. - Si esta formado por varias palabras los prefijos permitidos son: DE DE DEL SAN LA VIUDA VDA DE VIUDA DE SANTO DE LOS DE DE LA DE LAS DE SAN |
| Segundo Apellido | Cliente:    persona: segundoApellido | NO | Segundo Apellido. Puede estar conformado por varias palabras. |
| Razón Social | Cliente: razonSocial | Es obligatorio solo    para persona Jurídica | Razón social del cliente cuando se trata de una empresa. Es obligatorio para todas las figuras en caso de que sean persona jurídica. |
| Fecha Expedición | Cliente:    documento: fechaExpedicion | Obligatorio solo    para persona natural        y figura tomador | Fecha de expedición del documento de identidad. Obligatorio para cuando la figura es Tomador y corresponde a persona natural. |
| País Nacionalidad | Cliente:    persona: pais | Obligatorio solo    para persona natural        y figura tomador | Código del país de nacimiento. Obligatorio para cuando la figura es Tomador y corresponde a persona natural. Revisar página de Catalogo: País Nacionalidad y País Constitución |
| Tipo de Persona | Cliente: tipoPersona | SI | Permite identificar si una persona es natural o jurídica. Revisar página de Catalogo: Tipo de Persona |
| Celular | Cliente: celular | Obligatorio solo        para figura tomador y tipo de    persona natural | Número de Celular |
| Correo Electrónico | Cliente: correo | Obligatorio solo    para figura tomador | Persona    Natural:    Correo Electrónico Persona    Jurídica:    Correo    de contacto |
| País de constitución (Aplica solo para persona jurídica) | Cliente: paisConstitucion | Obligatorio solo    para persona jurídica        y figura tomador | Código del país de constitución de la empresa. Revisar página de Catalogo: País Nacionalidad y País Constitución |
| Respuesta a pregunta PEPs para Persona Natural | Tomador: personaPep | NO | Respuesta   a   la   pregunta:   “¿El tomador es una Persona Expuesta Políticamente?” Aplica solo para persona natural Opciones del campo SI/NO |
| Respuesta a pregunta PEPs para Persona jurídica | Tomador: administradorPep | NO | Respuesta a la pregunta: Alguno de    los    administradores (representantes        legales, miembros de la "Junta Directiva) o socio con una participación superior al 5% de la Persona Jurídica es una Persona Expuesta Políticamente (PEP)? Aplica solo para persona jurídica Opciones del campo SI/NO |

**Nota: **Si no puede enviar los datos del beneficiario, asegurado o cualquier otra figura involucrada en el negocio diferente al tomador, estos serán solicitados en el formulario de sarlaft de acuerdo con la clasificación del riesgo: Simplificado, Ordinario o Intensificado. Es decir, que al tomador se le presentará la pregunta si conoce o no los beneficiarios y/o asegurados, en caso de responder si, deberá diligenciar la información de estos, en caso de responder no, debe indicar una justificación.

## Datos de entrada propios de la operación de negocio:

| Campo | WS | Obligatorio | Descripción |
| --- | --- | --- | --- |
| Código de Ramo | polizas: codigoRamo | SI | Código del ramo del producto sobre el cuál se está realizando la operación. Revisar página de Catalogo: Código de Ramo |
| Código de Producto | polizas: codigoProducto | NO | Código del producto sobre el cuál se está realizando la operación. Revisar página de Catalogo: Código de Producto |
| Código de Canal | polizas: codigoCanal | NO | Código del canal por el cual se está realizando la operación. Revisar página de Catalogo: Códigos de Canales |
| Valor asegurado | polizas: valorAsegurado | NO | Valor asegurado de la póliza. Este valor es de la cobertura básica |
| Valor de Prima | polizas: valorPrima | NO | Valor de la prima anual de la póliza. |
| Medio de Recaudo | polizas: medioPago | NO | Medio de recaudo del pago de la póliza. Solo enviar DEBITO_AUTOMATICO para cuando el cliente pague por alguno de estos tres medios de pago: (CUENTA CORRIENTE, CUENTA AHORROS O TARJETA) (es decir la póliza quedo marcada para pago de débito automático). En caso contrario no enviar ningún valor |
| Tipo de Negocio | polizas: negocio | SI | Indica si una póliza es colectiva o individual. Revisar página de Catalogo: Tipo de Negocio |
| Código de Operación | codigoOperacion | SI | Código de la operación, por ejemplo: 01 – Negocio Nuevo, 05 – Renovación, RE - Reclamación |
| IdentificadorNego cio | negocioId | SI | Identificador del negocio para el sarlaft, puede ser el nro de cotización, nro de póliza o consecutivo generado en el aplicativo de negocio. |
| Tipo coaseguro | polizas: tipoCoaseguro | NO | Si el negocio tiene coaseguro enviar alguna de estas opciones: ACEPTADO CEDIDO En caso de no aplicar enviar el campo nulo. |
| Código de Oficina | polizas: codigoOficina | SI | Código de la oficina donde está inscrito el asesor. |
| Código agente | polizas: codigoAgente | SI | Código del agente asociado a la póliza de negocio |
| Licitación Pública | polizas: licitacionPubli ca | NO | Enviar true cuando se trate de una póliza con licitación pública. False en caso contrario. |
| Código de plan | polizas: codigoPlan |  | Código de plan. Utilizado por el canal digital. |

**NOTA:**

## Algunos datos como el código de canal, código de producto, valor asegurado y valor de prima son opcionales, pero son importantes para clasificación del riesgo, validar con las personas de negocio si deben ser enviados para su solución

**Datos de entrada cuando el negocio ya ejecuto las preguntas de conocimiento de PEPS, si no envía**** ****las**** ****respuestas**** ****a**** ****las**** ****preguntas**** ****PEPS,**** ****se**** ****presentará**** ****un**** ****formulario**** ****al**** ****tomador**** ****para**** ****su**** ****diligenciamiento**

## Estas preguntas solo aplican para la figura tomador

|  | Respuesta Pregunta PEPS | Respuesta Pregunta PEPS | Respuesta Pregunta PEPS | Respuesta Pregunta PEPS |
| --- | --- | --- | --- | --- |
| TieneAlgunaRelacionPEPS | TieneAlgunaRelacionPEPS | Cliente: relaciones: relacionPeps | NO | Indica si el cliente tiene alguna relación PEPS. Utilizada para cuando la respuesta del cliente es ninguna de las anteriores. En caso de que la información de relación PEPS no sea recibida en este paso de validación, el formulario    deberá    ser diligenciado. |
| Tipo Relación | Tipo Relación | Cliente: relaciones: tipo | NO | Tipo de Relación con el cliente: FAMILIAR    (Persona    Natural), CONYUGUE (Persona Natural) Y SOCIO (Persona Jurídica) Revisar página de Catalogo: Tipo de Relación |
| Parentesco PEPS | Parentesco PEPS | Cliente: relaciones: parentescoPeps | NO | Parentesco con el cliente. Por ejemplo: Conyuque, Familiar para |

|  |  |  | persona    natural.    Socio    y Accionista para persona jurídica Obligatorio cuando la respuesta del            campo TieneAlgunaRelacionPEPS es afirmativa y el tipo de Relación es Familiar. Revisar    página    de    Catalogo: Parentesco |
| --- | --- | --- | --- |
| Tipo Relación | Cliente: relaciones: codigoRelacion | NO | Obligatorio cuando se selecciona la opción Socio en Tipo Relación. Revisar página de Catalogo: Tipo Relación |
| Porcentaje de participación | Cliente: relaciones: porParticipacionAccionista | NO | Valor decimal correspondiente al porcentaje de participación. Obligatorio cuando la respuesta del    campo TieneAlgunaRelacionPEPS    es afirmativa y el tipo de Relación es Sociedad. |
| Tipo de Identificación PEPS | Cliente: relaciones: Documento: tipo | NO | Tipo de identificación del peps. Obligatorio cuando la respuesta del    campo TieneAlgunaRelacionPEPS    es afirmativa |
| Nro de identificación PEPS | Cliente: relaciones: Documento: numero | NO | Nro de identificación del peps. Obligatorio cuando la respuesta del    campo TieneAlgunaRelacionPEPS    es afirmativa |
| Primer Nombre PEPS | Cliente: relaciones: persona: primerNombre | NO | Primer Nombre del peps Obligatorio cuando la respuesta del    campo TieneAlgunaRelacionPEPS    es afirmativa |
| Segundo Nombre PEPS | Cliente: relaciones: persona: segundoNombre | NO | Segundo Nombre del peps Obligatorio cuando la respuesta del    campo TieneAlgunaRelacionPEPS    es afirmativa |
| Primer Apellido PEPS | Cliente: relaciones: persona: primerApellido | NO | Primer Apellido del peps Obligatorio cuando la respuesta del    campo TieneAlgunaRelacionPEPS    es afirmativa |
| Segundo Apellido PEPS | Cliente: relaciones: persona: segundoApellido | NO | Segundo Apellido del peps Obligatorio cuando la respuesta del    campo TieneAlgunaRelacionPEPS    es afirmativa |

**Otros**** ****Datos:**

| Respuesta a la pregunta de relación laboral entre el tomador y los asegurados | relacionLaboral | NO | S: El tomador tiene una relación laboral con los asegurados. N: En caso de que el tomador no tiene una relación laboral con los asegurados. Esta pregunta es opcional, en caso de que no se haga la pregunta en el aplicativo cliente, enviar la respuesta en NULL |
| --- | --- | --- | --- |
| Código de Aplicación | codigoAplicacion | SI | Código de aplicación del negocio que realiza la solicitud de evaluación de sarlaft |
| DNIActualiza | solicitudDni | SI | Dni del usuario logueado que realiza el proceso de sarlaft |
| IdEvaluación | EvaluacionId | NO | Identificador de Evaluación, generado por sarlaft en una invocación previa a este servicio. Se puede utilizar para adicionar/retirar figuras a la validación del sarlaft. Al enviar este id, el aplicativo de sarlaft generará un nuevo id para evitar confusiones sobre cuando termina el proceso de sarlaft actualizado correctamete. |
| Evaluación en Proceso | infoPendiente | NO | True: escenario para canales como WeSura y SuraEnlinea, cuando deben seguir enviando información de asegurado, beneficiarios y/o otras figurs. False: para cualquier otro canal |

Datos de las evidencias: Las evidencias no son obligatorias en este punto, de enviarse, deben cumplir con la siguiente información:

| Campo | WS | Obligatorio | Descripción |
| --- | --- | --- | --- |
| Resultado | evidencias: resultado | SI | Si la validación fue exitosa o fallida Revisar página de Catalogo: Tipo de Resultado Evidencia |
| Tipo de Evidencia | evidencias: tipo | SI | Tipo de Evidencia, Por Ejemplo: CIFIN (Validación Identidad), RRCC (Riesgos Consultables) Revisar página de Catalogo: Tipo de Evidencia |
| Observaciones | evidencias: observaciones | SI | Observaciones    de    la    evidencia adjuntada |
| Consecutivo | evidencias: controlConsecutivo | SI | Consecutivo propio de la evidencia, por   ejemplo,   para   validación   de |

|  |  |  | identidad el consecutivo de cifin. Para evidencias de firma digital el id de viafirma. |
| --- | --- | --- | --- |

## NOTA:

**En**** ****el**** ****caso**** ****de**** ****adicionar**** ****una**** ****evidencia**** ****de**** ****RRCC,**** ****tener**** ****presente**** ****que**** ****la**** ****validación**** ****que**** ****se**** ****ejecute**** ****sobre**** ****riesgos**** ****de**** ****consultables**** ****debe**** ****hacerse**** ****sobre**** ****el**** ****dni**** ****y**** ****nombres**** ****del**** ****cliente.**** ****De**** ****lo**** ****contrario**** ****la**** ****validación**** ****no**** ****queda**** ****completa.**

## Datos de Salida:

**Cabecera**** ****de**** ****la**** ****respuesta**

| Campo | ws | Descripción |
| --- | --- | --- |
| IdEvaluación | id | Identificador del proceso de evaluación realizado. Permite agrupar todas las evaluaciones de sarlaft realizadas sobre las figuras de un proceso de negocio. |
| URL | url | Url para abrir por el navegador el formulario de Sarlaft, en caso de que éste deba ser diligenciado. Se genera una sola url para que el tomador ingrese la información respectiva |
| Estado | estado | Estado de la evaluación del sarlaft: PENDIENTE, FINALIZADO, RECHAZADO Posibles valores: PENDIENTE: Hace falta ingresar información del sarlaft o levantar controles de validaciones. PENDIENTE_ACCION_MANUAL: Hace falta una validación manual, caso para aplicativos con procesos especiales. FINALIZADO: El proceso de evaluación del sarlaft para el negocio finalizo y puede expedirse. RECHAZADO: Se levanto un control bloqueante que impide la vinculación del cliente |

## El servicio devolverá un listado con este conjunto de datos por cada figura que se evalúo en el proceso de evaluación

| Campo | Descripción |
| --- | --- |
| RequiereDiligenciar (requiereFormulario) | true: Indica que el Sarlaft del cliente esta desactualizado y de acuerdo con su nivel de riesgo debe ser diligenciado. false: Indica que el Sarlaft del cliente esta actualizado o que de acuerdo con su nivel de riesgo no es necesario actualizar más información. |
| FechaActualización (fechaActualización) | Fecha de actualización del último sarlaft del cliente. Null para cuando no se tenga información de fecha de actualización. |
| DNI | Dni de la persona para la cual se solicita el sarlaft. |

| ( | dni | ) |  |
| --- | --- | --- | --- |
| Estado del Saraflt (estado) | Estado del Saraflt (estado) | Estado del Saraflt (estado) | Estado que indica si el sarlaft ha terminado o está pendiente Posibles valores: PENDIENTE: Hace falta ingresar información del sarlaft o levantar controles de validaciones. PENDIENTE_ACCION_MANUAL: Hace falta una validación manual, caso para aplicativos con procesos especiales. FINALIZADO: El proceso de evaluación del sarlaft para el negocio finalizo y puede expedirse. RECHAZADO: Se levanto un control bloqueante que impide la vinculación del cliente |
| Control (listaControl: control) | Control (listaControl: control) | Control (listaControl: control) | Código del control levantado para el dni, por ejemplo, cuando es un cliente PEPS, o pertenece a una lista de control. Posibles Valores: PEPS: El cliente este marcado como PEPS. RRCC: El cliente tiene una marca de lista de control GAFI: El cliente tiene una nacionalidad de alto riesgo o su país de constitución es de alto riesgo. |
| Mensaje Control (listaControl: mensajeControl) | Mensaje Control (listaControl: mensajeControl) | Mensaje Control (listaControl: mensajeControl) | Mensaje del control levantado al dni. Validar con cada negocio si este mensaje debe ser mostrado directamente al usuario. |
| Tipo Formulario (Sarlaft: tipoFormulario) | Tipo Formulario (Sarlaft: tipoFormulario) | Tipo Formulario (Sarlaft: tipoFormulario) | Tipo de formulario que se le asigno al sarlaft(ORDINARIO,SIMPLIFICADO,INTENSIFICADO), este parametro se agrega especialmente para el Egv de cotizador de vida. |

**Escenario de modificación del proceso de Evaluación: **Cuando dentro del proceso de solicitud de un negocio, se requiere cambiar la información de alguno de los roles dentro de la evaluación del sarlaft, se requiere volver a enviar la solicitud de evaluación, con toda la información e indicando en el campo de entrada: IdEvaluación**, **el id de evaluación que se desea actualizar. Como resultado el servicio devolverá un nuevo consecutivo para idEvaluación, que permitirá identificar cuando se ha terminado por completo el proceso.

## WEB COMPONENT

**Datos**** ****de**** ****Entrada:**

| Campo | Obligatorio | Descripción |
| --- | --- | --- |
| TokenWebCompo nent | SI | Token JWT |
| Json | SI | Un json con los mismos datos de entrada que se envían al servicio de assessment |

El webcomponent se encargará de establecer la comunicación con el servicio web de validación de saralft (assessment) y mostrar el formulario correspondiente y su debido almacenamiento.

## Resultado:

Una vez el formulario ha sido diligenciado, el aplicativo de Sarlaft 4.0 realizará el proceso de almacenamiento y una vez el proceso haya terminado notificará por medio de un servicio rest, expuesto por el aplicativo de negocio, que el sarlaft ya se encuentra finalizado.
Un proceso de evaluación de sarlaft solo ha finalizado para cuando se termine por completo el sarlaft de todas las figuras para las cuales fue solicitado. La respuesta al webhook puede ser exitosa o de fallida si alguno de los roles no pasa la validación de identidad.

## Seguridad:

La seguridad de este WebComponent será basada en un token JWT, el cual permitirá establecer la conexión entre el aplicativo de negocio y el aplicativo Sarlaft 4.0

## SERVICIO PARA ALMACENAR EVIDENCIAS

Permite recibir las evidencias de validaciones realizadas directamente por los aplicativos de negocio y así completar las validaciones mínimas del sarlaft
URL Desarrollo: **<https://sarlaftapi.dllosura.com/sarlaftserv/assessment/addevidence****> **URL Laboratorio: ** **Perfil de Consulta: **PF_CONSUMSERVSARLAFTAPI**** ****del**** ****SP**** ****Sarlaft4**

## Datos de Entrada:

**Recibe una lista con los siguientes campos, permitiendo adicionar evidencias para los dnis que**** ****pertenecen**** ****a un**** ****proceso**** ****de**** ****evaluación**** ****de**** ****sarlaft.**

| Campo | WS | Obligatorio | Descripción |
| --- | --- | --- | --- |
| DNI | dni | SI | DNI del cliente para el cual se toman las evidencias. |
| IdEvaluación | evaluacionId | SI | Identificador    del    proceso    de evaluación, devuelto por el servicio de validación salaft. |
| Tipo de Evidencia | tipo | SI | Tipo de Evidencia, Por Ejemplo: CIFIN (Validación Identidad), RRCC (Riesgos Consultables) Revisar página de Catalogo: Tipo de Evidencia |
| Observaciones | observaciones | SI | Observaciones    de    la    evidencia adjuntada |
| Consecutivo | controlConsecutivo | SI | Consecutivo propio de la evidencia, por ejemplo, para validación de identidad el consecutivo de cifin. Para evidencias de firma digital el id de viafirma. |
| Resultado | resultado | SI | Resultado de la evidencia. Exitoso o Fallido. Revisar página de Catalogo: Tipo de Resultado Evidencia |
| Código    de aplicación | codigoAplicacion | SI | Código de aplicación  que envia las evidencias. |

## Datos de Salida:

**El**** ****servicio**** ****devuelve**** ****una**** ****lista**** ****con**** ****los**** ****siguientes**** ****campos**

| Campo | Descripción |
| --- | --- |
| EvidenciasAlmacenadas | True: evidencias almacenadas False: ocurrió un error almacenando las evidencias |

| (resultado) |  |
| --- | --- |
| MensajeError (mensajeError) | En caso de que el almacenamiento haya terminado con error, se entrega en este campo el mensaje de error que permita hacer trazabilidad de este. |
| DNI (dni) | Dni del cliente al que pertenece la evidencia. |

## NOTA:

**En**** ****el**** ****caso**** ****de**** ****adicionar**** ****una**** ****evidencia**** ****de**** ****RRCC,**** ****tener**** ****presente**** ****que**** ****la**** ****validación**** ****que**** ****se**** ****ejecute**** ****sobre**** ****riesgos**** ****de**** ****consultables**** ****debe**** ****hacerse**** ****sobre**** ****el**** ****dni**** ****y**** ****nombres**** ****del**** ****cliente.**** ****De**** ****lo**** ****contrario**** ****la**** ****validación**** ****no**** ****queda**** ****completa.**

## SERVICIO PARA CONSULTAR FORMULARIO SARLAFT

Permite consultar si un cliente ya diligencio el formulario de sarlaft dentro de un proceso de evaluación.
URL Desarrollo: `<no disponible>`
URL Laboratorio: `<no disponible>`
Perfil de Consulta: `<no disponible>`

## Datos de Entrada:

| Campo | WS | Obligatorio | Descripción |
| --- | --- | --- | --- |
| IDEvaluación | evaluacionId | SI | Identificador del proceso de evaluación, devuelto por el servicio de validación salaft. |
| Código de aplicación | codigoAplicacion | SI | Código de aplicación que realiza la consulta. |

**Datos**** ****de**** ****Salida:**
Un listado de dnis asociados al formulario de sarlaft y su estado de formulario

| DNI | Dni del cliente |
| --- | --- |
| Formulario | True: proceso de diligenciamiento del formulario completo. False: el formulario de saraft no ha sido diligenciado. |

## INTERFAZ DE SERVICIO WEBHOOK

Cada aplicativo de negocio que utiliza el aplicativo de Sarlaft 4.0 deberá exponer un servicio Rest Post seguro con Seus 4 con la siguiente interfaz de servicio.

Por medio de esta interfaz el aplicativo de Sarlaft comunicará:

- Todo el proceso de sarlaft ha terminado y está completo para todas las figuras inmersas en el proceso de evaluación. Para este caso el campo processStatus estará en Finalizado (FINALIZADO) e indica que la póliza puede expedirse.
- Todo el proceso de sarlaft ha terminado, pero alguna de las figuras pudo no haber pasado la validación de identidad, para este caso el processStatus estará en pendiente (RECHAZADO).

| Campo | Descripción |
| --- | --- |
| evaluacionId | Identificador del proceso de evaluación realizado. Permite agrupar todas las evaluaciones de sarlaft realizadas sobre las figuras de un proceso de negocio. |
| estado | Estado de la evaluación del sarlaft PENDIENTE_ACCION_MANUAL: Hace falta una validación manual, caso para aplicativos con procesos especiales. FINALIZADO: El proceso de evaluación del sarlaft para el negocio finalizo y puede expedirse. RECHAZADO: Se   levanto   un   control   bloqueante   que   impide   la vinculación del cliente |
| idNegocio | Identificador de negocio propio del aplicativo que expide o renueva. |
| Datos de cada una de las figuras de la póliza | Datos de cada una de las figuras de la póliza |
| dni | Dni del cliente |
| estado | PENDIENTE_ACCION_MANUAL: Hace falta una validación manual, caso para aplicativos con procesos especiales. FINALIZADO: El proceso de evaluación del sarlaft para el negocio finalizo y puede expedirse. RECHAZADO: Se levanto un control bloqueante que impide la vinculación del cliente |

| Controles : control | Código de validación no superada, por ejemplo: IDENTITY (validación de identidad) |
| --- | --- |
| Controles : mensajeControl | Descripción de la validación no superada. |

Se espera una respuesta de tipo 200 OK con el siguiente json, en caso de que la recepción haya sido exitosa.

| Campo | Descripción |
| --- | --- |
| recibido | True: se confirma la recepción de la notificacion False: ocurrió un error y la notificación debe ser reenviada. |
| mensajeError | Mensaje de error en caso de presentarse cuando el campo received es false |

Notificación por Mensajería RabbitMQ (Lineamientos)

- Se mantiene la integración por Webhook como está diseñada actualmente, para el caso de mensajería por RabbitMQ Sura el mensaje Json es el mismo indicado en la sección anterior de Webhook.

- En el caso del webhook, al ser un servicio que se expone del lado del cliente, nos adaptamos al modelo de seguridad que nos brinden y no es requisito usar seus4. En este caso, necesitaríamos que nos proporcionen un usuario y clave para llamar el servicio expuesto, él método de autenticación y el endpoint del servicio. NOTA: es importante que el arquitecto de la aplicación cliente pueda garantizar que el método de autenticación seleccionado cumpla con los requisitos de seguridad que exige la compañía en la publicación de servicios rest.

- Al ser la integración por RabitMQ un mecanismo válido de integración en la compañía, daremos soporte a este esquema de integración únicamente para la notificación asíncrona de Sarlaft Finalizado como alternativa al Webhook (los servicios del API de Sarlaft se mantienen como servicios rest).

- Al usar el mecanismo de RabbitMQ, la aplicación cliente debe garantizar el procesamiento del mensaje y gestionar los posibles errores, indisponiblidades de plataformas, tiempos de respuesta, etc. NOTA: Para el caso del webhook, esta responsabilidad recae sobre el bus de mensajería propio del Sarlaft para garantizar la entrega del mensaje al servicio destino.

- En el caso que una aplicación cliente escoja notificaciones via rabbitMQ, ésta será responsable de crear la cola con binding al Exchange indicado y usuarios de conexión y entregar éstos al equipo base del Sarlaft para matricularlos en el api de Sarlaft. RabbitMQ Sura.

Para recibir mensajes de finalización por favor suscribir una cola al siguiente Exchange y rounting key en RabbtiMqSura

## Exchange: seguros.sarlaft.finalizacion

- INTEGRACIÓN CLIENTE/SERVIDOR

Para la integración con aplicativos de plataforma cliente servidor, se plantea el siguiente esquema de integración, donde se debe crear un aplicativo de capa intermedia que facilite la comunicación entre el Webcomponent de Sarlaft y los eventos de finalización del proceso de sarlaft.
*UI SPA: *Microservicio de front de estilo SPA (*Single Page Application*) cuyo objetivo es embeber el formulario de sarlaft e indicar el proceso de finalización de diligenciamiento al microservicio back.
*Backend SPA: *Microservicio encargado de recibir el evento de finalización de diligenciamiento del formulario, esperar la notificación de sarlaft actualizado por medio de un servicio webhook expuesto para recibir el callback desde el aplicativo de Sarlaft.
En escenarios de renovaciones masivas, este componente también se debe encargar de activar el proceso de actualización del Sarlaft por medio de los servicios dispuestos para este fin. Para este escenario, también se contempla que, una vez finalizado el proceso de actualización, se comunicará vía callback la finalización de la actualización del Sarlaft.
La construcción del aplicativo intermedio quedará a cargo del equipo de saralft en conjunto con cada equipo de tecnología que de soporte al negocio correspondiente.

## Catalogos

**Tipo**** ****de**** ****Documento**
Códigos de Identificación manejados desde seguros sura

| Código | Descripción |
| --- | --- |
| E | CED.EXTRANJERIA |
| C | CEDULA |
| D | DIPLOMATICO |
| X | DOC.IDENT. DE EXTRANJEROS |
| N | NUIP |
| P | PASAPORTE |
| TP | PASAPORTE ONU |
| T | TARJ.IDENTIDAD |
| F | IDENT. FISCAL PARA EXT. |
| A | NIT |
| J | P. JURIDICA SIN IDENTIFICACION |
| TO | PASAPORTE NACIONES UNIDAS |
| TE | PEMISO ESPECIAL DE PERMANENCIA |
| TS | SALVOCONDUCTO DE PERMANENCIA |
| R | REGISTRO CIVIL DE NACIMIENTO |

## País Nacionalidad y País Constitución

Códigos de Países manejados desde seguros sura para la tabla PAISES. Muestra de códigos

| Código | Descripción |
| --- | --- |
| 1 | COREA DEL NORTE |
| 2 | MONTENEGRO |
| 4 | AFGANISTAN |
| 8 | ALBANIA |
| 12 | ARGELIA |
| 20 | ANDORRA |
| 24 | ANGOLA |
| 28 | ANTIGUA Y BARBUDA |
| 31 | AZERBAIYAN |
| 44 | BAHAMAS |
| 57 | COLOMBIA |
| .. … .. | Entre muchos más países |

Este listado puede ser obtenido del catalogo de modelo de clientes, enviando `<tipo>PAISES</tipo>`
Url DLLO:  Url LABO:

## Tipo de Persona

| Código | Descripción |
| --- | --- |
| N | Natural |
| J | jurídica |

**Códigos**** ****de**** ****Canales**

| Nombre_Canal_Comercial | Codigo_Canal_Comercial |
| --- | --- |
| BANCASEGUROS - BANCOLOMBIA | CC001 |
| BANCASEGUROS - CONAVI | CC002 |
| BANCASEGUROS - CORFINSURA | CC003 |
| CORPORATIVO | CC004 |
| DIRECTO - AUTOS SURA | CC005 |
| DIRECTO - OF.CENTRAL | CC006 |
| DIRECTO - OTROS | CC007 |
| DIRECTO - RENTAS | CC008 |
| ALIANZA EXITO | CC009 |
| MÓDULOS DE SEGUROS | CC010 |
| PROMOTORAS | CC011 |
| PROMOTORÍAS | CC012 |
| SUCURSALES | CC013 |
| ALIANZA TUYA | CC014 |
| TELEVENTAS | CC015 |
| VENTA EN LÍNEA | CC016 |
| CORP. BANCOLOMBIA | CC017 |
| VENTA POR CATALOGO | CC018 |
| TARJETA ALKOSTO | CC019 |
| LIDERES VENTA DIRECTA | CC020 |
| PROTECCION | CC021 |
| CONSULTORES FINANCIEROS | CC022 |
| EXPANSION LOCAL | CC023 |
| PENDIENTE | CC024 |
| ALKOMPRAR | CC025 |
| WESURA | CC026 |
| ALIANZA CORBETA | CC027 |
| AFFINNITY | CC028 |
| BANCASEGUROS BANCOLOMBIA | CC029 |
| BANCASEGUROS FALABELLA | CC030 |
| BANCASEGUROS CONFIAR | CC031 |
| OTRAS ENTIDADES FINANCIERAS | CC032 |
| TELEVENTAS DIRECTO | CC033 |
| TELEVENTAS BANCASEGUROS | CC034 |
| TELEVENTAS TRADICIONAL | CC035 |
| TELEVENTAS RETAIL | CC037 |

| TELEVENTAS PROTECCION | CC038 |
| --- | --- |
| MIS ALIADOS | CC039 |
| CORRESPONSALES | CC040 |
| ALIANZA EURO | CC041 |
| ALIANZA FLAMINGO | CC042 |
| ALIANZA CENCOSUD | CC043 |
| GRAN EMPRESA | CC044 |

## Tipo de Negocio

| Código | Descripción |
| --- | --- |
| INDIVIDUAL | Individual |
| COLECTIVO | Colectiva |

**Tipo**** ****de**** ****Relación**

| Código | Descripción |
| --- | --- |
| FAMILIA | FAMILIAR |
| CONYUGE | CONYUGUE |
| SOCIO | SOCIEDAD |

## Relaciones

| Código | Descripción |
| --- | --- |
| R1 | REPRESENTANTE |
| R2 | PRESIDENTE |
| R3 | VICEPRESIDENTE |
| R4 | GERENTE |
| R5 | TESORERO |
| R6 | SOCIO CON PARTICIPACION SUPERIOR AL 5% |

**Parentesco**

| Código | Descripción |
| --- | --- |
| 01 | Padres |
| 02 | Abuelos |
| 03 | Hermanos |
| 04 | Hijos |
| 05 | Nietos |
| 06 | Yernos |
| 07 | Nueras |
| 08 | Suegros |
| 09 | Cuñados |
| 10 | Abuelos del conyugue |
| 11 | Compañero Permanente |
| 12 | Hijos adoptivos |
| 13 | Padres Adoptantes |

## Tipo de propietario:

| Código | Descripción |
| --- | --- |
| DIRECTO | Directo |
| INDIRECTO | Indirecto |

**Tipo**** ****de**** ****Resultado**** ****Evidencia**

| Código | Descripción |
| --- | --- |
| EXITOSO | Exitosa |
| FALLIDO | Fallido |

## Tipo de Evidencia

| Código | Descripción |
| --- | --- |
| CIFIN | Evidencia CIFIN |
| RRCC | Riesgos Consultables |

**Código**** ****de**** ****Ramo**
Códigos de ramos de sura, por ejemplo

| Código | Descripción |
| --- | --- |
| 028 | Hogar |
| 030 | Empresariales |
| 091 | Salud |
| …. | … (Entre muchos otros) |

## Código de Producto

Corresponde al código de subramo de sura, por ejemplo

| Código | Descripción |
| --- | --- |
| PYM | PLAN EMPRESARIO SURA PARA SU EMPRESA. (Ramo 030) |
| S01 | SEGURO MULTI RIESGO EMPRESARIAL (Ramo 030) |
| H09 | PLAN HOGAR GLOBAL (Ramo 028) |
| …. | … (Entre muchos otros) |
