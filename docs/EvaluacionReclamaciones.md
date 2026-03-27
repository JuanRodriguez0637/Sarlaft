SARLAFT 4.0 – Evaluación para Reclamaciones
Dirigido a: analistas que implementen la integración del sarlaft 4.0 para el proceso de reclamaciones.
Para información de arquitectura base, integraciones y proceso por favor referirse al documento
DocumentacionTecnicaSarlaft_1.8
https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070150/Descripci+n+de+Interfaces+Prin
cipales
Generalidades:
A diferencia del proceso de evaluación en el proceso de reclamaciones debe enviarse una petición al
servicio de assessment por cada una de las figuras que reclaman en el seguro, es decir, si en una póliza
existe dos personas de figura beneficiario que inician proceso de reclamación, se debe consumir dos
veces el servicio de assesment, cada invocación con el tomador y en conjunto con una de las figuras
que reclaman. Es decir, se iniciarían dos procesos de evaluación independiente.
Definición Reclamante:
Se menciona como reclamante a cualquier figura, ya sea afiliado, afianzado, beneficiario, asegurado o
tomador que realiza la reclamación del seguro. No existe como tal la propiedad de reclamante en el
servicio web, si no que hace referencia a la parte de negocio.
Diligenciamiento Formulario:
El proceso de assessment para el proceso de reclamaciones enviará automáticamente una notificación
por correo electrónico al reclamante con la url para ingresar al formulario de saralft, en caso de que
requiera diligenciarse.

## SERVICIO VALIDAR SARALFT

Permite realizar las validaciones mínimas para clasificar el riesgo de un cliente y determinar el tipo de
sarlaft que debe diligenciar en un proceso de reclamaciones, de acuerdo con la naturaleza del cliente
y del producto.
URL Desarrollo: https://sarlaftapi.dllosura.com/sarlaftserv/assessment
URL Laboratorio: https://sarlaftapi.labsura.com/sarlaftserv/assessment
Perfil de Consulta: PF_CONSUMSERVSARLAFTAPI del SP Sarlaft4
Datos de Entrada:
Para su mayor claridad se documentan los datos de entrada por secciones.
Los datos de entrada correspondientes a cada una de las Figuras conservan la estructura del servicio
de assessment para negocio nuevo. En el caso de reclamaciones siempre será obligatorio recibir el
tomador y la información de la figura que reclama el pago del seguro, la cual podría ser: asegurado,
beneficiario, afianzado o afiliado.
Si el tomador o cualquier cliente tiene dos figuras dentro de la póliza, deben enviarse los datos de
igual forma en el campo correspondiente. Por ejemplo, si el tomador es el mismo beneficiario (figura
que reclama), estos datos deben enviarse en los campos de tomador y beneficiario.
Datos correspondientes a los clientes que tiene algún rol dentro de la póliza. Se debe enviar como
mínimo el tomador.

| Tomador |  | tomador |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Asegurado |  | asegurados |  |  |  |  |  |  |
| Beneficiario |  | beneficiarios |  |  |  |  |  |  |
| Afianzado |  | afianzado |  |  |  |  |  |  |
| Afiliado |  | afiliado |  |  |  |  |  |  |

| Campo | WS | Obligatorio | Descripción |
| --- | --- | --- | --- |
| Tipo de Identificación | Cliente: documento: tipo | SI | Tipo de Identificación. Revisar página de Catalogo: Tipo de documento |
| Nro de Identificación | Cliente: documento: numero | SI | Nro de Identificación. |
| Primer Nombre | Cliente: persona: primerNombre | Es obligatorio solo para persona Natural | Primer Nombre. Es obligatorio para todas las figuras en caso de que sean persona natural. |
| Segundo Nombre | Cliente: persona: segundoNombre | NO | Segundo Nombre. |
| Primer Apellido | Cliente: persona: primerApellido | Es obligatorio solo para persona Natural | Primer Apellido. Es obligatorio para todas las figuras en caso de que sean persona natural. |
| Segundo Apellido | Cliente: persona: segundoApellido | NO | Segundo Apellido. |
| Razón Social | Cliente: razonSocial | Es obligatorio solo para persona Jurídica | Razón social del cliente cuando se trata de una empresa. Es obligatorio para todas las figuras en caso de que sean persona jurídica. |
| Fecha Expedición | Cliente: documento: fechaExpedicion | Obligatorio solo para persona natural. | Fecha de expedición del documento de identidad. Obligatorio para persona natural. |
| País Nacionalidad | Cliente: persona: pais | Obligatorio solo para | Código del país de nacimiento. Obligatorio para persona natural. |

| Cliente: documento | : |
| --- | --- |
| tipo |  |

| Cliente: documento | : |
| --- | --- |
| numero |  |

| Cliente: persona: |
| --- |
| primerNombre |

| Cliente: persona: |
| --- |
| segundoNombre |

| Cliente: persona: |
| --- |
| primerApellido |

| Cliente: persona: |
| --- |
| segundoApellido |

| Cliente: documento | : |
| --- | --- |
| fechaExpedicion |  |

| Cliente: persona: |
| --- |
| pais |

Datos de entrada propios de la operación de negocio:

|  |  | persona natural. | Revisar página de Catalogo: País Nacionalidad y País Constitución |
| --- | --- | --- | --- |
| Tipo de Persona | Cliente: tipoPersona | SI | Permite identificar si una persona es natural o jurídica. Revisar página de Catalogo: Tipo de Persona |
| Celular | Cliente: celular | Obligatorio solo para tipo de persona natural | Número de Celular |
| Correo Electrónico | Cliente: correo | Obligatorio solo para figura tomador | Persona Natural: Correo Electrónico Persona Jurídica: Correo de contacto |
| País de constitución (Aplica solo para persona jurídica) | Cliente: paisConstitucion | Obligatorio solo para persona jurídica. | Código del país de constitución de la empresa. Revisar página de Catalogo: País Nacionalidad y País Constitución |

| Cliente: |
| --- |
| paisConstitucion |

| Campo | WS |  | Obligatorio | Descripción |
| --- | --- | --- | --- | --- |
| Código de Ramo | polizas: codigoRamo |  | SI | Código del ramo del producto sobre el cuál se está realizando la operación. Revisar página de Catalogo: Código de Ramo |
| Código de Producto | polizas: codigoProducto |  | NO | Código del producto sobre el cuál se está realizando la operación. Revisar página de Catalogo: Código de Producto |
| Código de Canal | polizas: codigoCanal |  | SI | Código del canal por el cual se está realizando la operación. Revisar página de Catalogo: Códigos de Canales |
| Código de Operación | codigoOperacion |  | SI | RE para Reclamación |
| IdentificadorNego cio | negocioId |  | SI | Identificador del negocio para el sarlaft, puede ser el nro de cotización, nro de póliza, identificador del reclamo o consecutivo generado en el aplicativo de negocio. |
| Código de Oficina | polizas: codigoOficina |  | SI | Código de la oficina donde está inscrito el asesor. |
| Código agente |  | polizas: | SI | Código del agente asociado a la póliza de negocio |
|  |  | codigoAgente |  |  |
| Indicador proceso judicial |  | polizas: | NO | True: si el proceso corresponde a un proceso judicial False: en caso contrario |
|  |  | indProcesoJudic |  |  |
|  |  | ial |  |  |
| Juzgado | polizas: juzgado | polizas: | Obligatorio cuando el indicador de | Número del juzgado que solicita la petición del pago de la reclamación |
|  |  | juzgado |  |  |

| polizas: |
| --- |
| codigoRamo |

| polizas: |
| --- |
| codigoProducto |

| polizas: |
| --- |
| codigoCanal |

| polizas: |
| --- |
| codigoOficina |

Otros Datos:
Datos de Salida:
Cabecera de la respuesta

|  |  | proceso judicial es true. |  |
| --- | --- | --- | --- |
| Ciudad de la solicitud del proceso judicial | polizas: ciudadProcesoJu dicial | Obligatorio cuando el indicador de proceso judicial es true. | Ciudad de la solicitud del proceso judicial |

| polizas: |
| --- |
| ciudadProcesoJu |
| dicial |

| Código de Aplicación | codigoAplicacion | SI | Código de aplicación del negocio que realiza la solicitud de evaluación de sarlaft |
| --- | --- | --- | --- |
| DNIActualiza | solicitudDni | SI | Dni del usuario logueado que realiza el proceso de sarlaft |
| IdEvaluación | evaluacionId | NO | Identificador de Evaluación, generado por sarlaft en una invocación previa a este servicio. Se puede utilizar para adicionar/retirar figuras a la validación del sarlaft. Al enviar este evaluacionId, el aplicativo de sarlaft generará un nuevo evaluacionId para evitar confusiones sobre cuando termina el proceso de sarlaft actualizado correctamete. |

| Campo | ws | Descripción |
| --- | --- | --- |
| IdEvaluación | id | Identificador del proceso de evaluación realizado. Permite agrupar todas las evaluaciones de sarlaft realizadas sobre las figuras de un proceso de negocio. |
| URL | url | Url para abrir por el navegador el formulario de Sarlaft, en caso de que éste deba ser diligenciado. Se genera una sola url para que el tomador ingrese la información respectiva |
| Estado | estado | Estado de la evaluación del sarlaft: PENDIENTE, FINALIZADO, RECHAZADO Posibles valores: PENDIENTE: Hace falta ingresar información del sarlaft o levantar controles de validaciones. PENDIENTE_ACCION_MANUAL: Hace falta una validación manual, caso para aplicativos con procesos especiales. FINALIZADO: El proceso de evaluación del sarlaft para el negocio finalizo y puede expedirse. |

El servicio devolverá un listado con este conjunto de datos por cada figura que se evalúo en el
proceso de evaluación.

|  |  | RECHAZADO: Se levanto un control bloqueante que impide la vinculación del cliente |
| --- | --- | --- |

| Campo | Descripción |
| --- | --- |
| RequiereDiligenciar (requiereFormulario) | true: Indica que el Sarlaft del cliente esta desactualizado y de acuerdo con su nivel de riesgo debe ser diligenciado. false: Indica que el Sarlaft del cliente esta actualizado o que de acuerdo con su nivel de riesgo no es necesario actualizar más información. |
| FechaActualización (fechaActualización) | Fecha de actualización del último sarlaft del cliente. Null para cuando no se tenga información de fecha de actualización. |
| DNI (dni) | Dni de la persona para la cual se solicita el sarlaft. |
| Estado del Saraflt (estado) | Estado que indica si el sarlaft ha terminado o está pendiente Posibles valores: PENDIENTE: Hace falta ingresar información del sarlaft o levantar controles de validaciones. PENDIENTE_ACCION_MANUAL: Hace falta una validación manual, caso para aplicativos con procesos especiales. FINALIZADO: El proceso de evaluación del sarlaft para el negocio finalizo y puede expedirse. RECHAZADO: Se levanto un control bloqueante que impide la vinculación del cliente |
| Control (listaControl: control) | Código del control levantado para el dni, por ejemplo, cuando es un cliente PEPS, o pertenece a una lista de control. Posibles Valores: PEPS: El cliente este marcado como PEPS. RRCC: El cliente tiene una marca de lista de control GAFI: El cliente tiene una nacionalidad de alto riesgo o su país de constitución es de alto riesgo. |
| Mensaje Control (listaControl: mensajeControl) | Mensaje del control levantado al dni. Validar con cada negocio si este mensaje debe ser mostrado directamente al usuario. |

|  | listaControl: |
| --- | --- |
| mensajeControl |  |

Catálogos
Tipo de Documento
Códigos de Identificación manejados desde seguros sura
País Nacionalidad y País Constitución
Códigos de Países manejados desde seguros sura para la tabla PAISES. Muestra de códigos
Este listado puede ser obtenido del catalogo de modelo de clientes, enviando <tipo>PAISES</tipo>
Url LABO: https://siclab.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl

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

| Url DLLO: http://segdllo02.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl |
| --- |
| Url LABO: https://siclab.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl |

Tipo de Persona
Códigos de Canales

| Código | Descripción |
| --- | --- |
| N | Natural |
| J | jurídica |

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

Tipo de Negocio
Tipo de Relación
Relaciones
Parentesco
Tipo de propietario:

| TELEVENTAS PROTECCION | CC038 |
| --- | --- |
| MIS ALIADOS | CC039 |
| CORRESPONSALES | CC040 |
| ALIANZA EURO | CC041 |
| ALIANZA FLAMINGO | CC042 |
| ALIANZA CENCOSUD | CC043 |
| GRAN EMPRESA | CC044 |

| Código |  |  |  | Descripción |
| --- | --- | --- | --- | --- |
|  | INDIVIDUAL |  |  | Individual |
|  | COLECTIVO |  |  | Colectiva |

| Código | Descripción |
| --- | --- |
| FAMILIA | FAMILIAR |
| CONYUGE | CONYUGUE |
| SOCIO | SOCIEDAD |

| Código | Descripción |  |  |
| --- | --- | --- | --- |
| R1 |  | REPRESENTANTE |  |
| R2 |  | PRESIDENTE |  |
| R3 | VICEPRESIDENTE |  |  |
| R4 | GERENTE |  |  |
|  |  | GERENTE |  |
| R5 |  | TESORERO |  |
| R6 |  | SOCIO CON PARTICIPACION SUPERIOR AL 5% |  |

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

Tipo de Resultado Evidencia
Tipo de Evidencia
Código de Ramo
Códigos de ramos de sura, por ejemplo
Código de Producto
Corresponde al código de subramo de sura, por ejemplo

| Código | Descripción |
| --- | --- |
| DIRECTO | Directo |
| INDIRECTO | Indirecto |

| Código |  |  | Descripción |
| --- | --- | --- | --- |
|  | EXITOSO |  | Exitosa |
|  | FALLIDO |  | Fallido |

| Código | Descripción |
| --- | --- |
| CIFIN | Evidencia CIFIN |
| RRCC | Riesgos Consultables |

| Código | Descripción |
| --- | --- |
| 028 | Hogar |
| 030 | Empresariales |
| 091 | Salud |
| …. | … (Entre muchos otros) |

| Código | Descripción |
| --- | --- |
| PYM | PLAN EMPRESARIO SURA PARA SU EMPRESA. (Ramo 030) |
| S01 | SEGURO MULTI RIESGO EMPRESARIAL (Ramo 030) |
| H09 | PLAN HOGAR GLOBAL (Ramo 028) |
| …. | … (Entre muchos otros) |
