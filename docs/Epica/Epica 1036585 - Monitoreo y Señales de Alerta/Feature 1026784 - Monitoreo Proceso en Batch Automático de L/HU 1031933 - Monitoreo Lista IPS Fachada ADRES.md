# HU 1031933 — [Monitoreo]: Lista IPS Fachada ADRES

[Épica 1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585) › [Feature 1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784) › HU 1031933 — [Monitoreo]: Lista IPS Fachada ADRES

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1031933](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1031933) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Ciencia de datos |
| **Creado** | 2026-02-03 |
| **Última modificación** | 2026-02-06 |

## Jerarquía

- **Épica:** [1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585)  
  Estado: New  
- **Feature:** [1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784)  
  Estado: New  

## Descripción

Como Analista SARLAFT**  Quiero que el sistema ejecute de forma automática y diaria un proceso batch de monitoreo contra la Lista IPS Fachada ADRES Para validar el 100 % de la base de clientes, aplicar reglas de marcación, mantenimiento o desmarcación, y generar logs completos, garantizando trazabilidad auditable y cumplimiento normativo SARLAFT, sin intervención manual.  1. Naturaleza del Proceso – Lista IPS Fachada ADRES** **** AtributoDefiniciónTipo Batch Ejecución Automática Frecuencia Diario Momento Ventana definida (sin afectar producción) Alcance 100 % de los clientes vigentes Resultado Archivo de logs + actualización de marcas Margen de tolerancia 24 horas desde la última ejecución exitosa Trazabilidad Obligatoria y auditable Fuente de informaciónArchivo recibido mediante requerimiento, con tabla de Tipo ID y Número ID de IPS Fachada ADRES       ** Descripción Funcional – Lista IPS Fachada ADRES** 
- La fuente de consulta es un archivo entregado a la compañía mediante requerimiento formal al equipo. 
- El archivo contiene una tabla estructurada con mínimo los siguientes campos: 
- Tipo de ID 
- Número de ID 
- Razón social 
- Fecha de ingreso 
- Tipo de lista  
- El archivo corresponde exclusivamente a la Lista IPS Fachada ADRES. 
- El archivo es cargado y versionado por el sistema como insumo del proceso batch. 
- La fecha del archivo y su identificador hacen parte de la trazabilidad del proceso.   **Reglas de Coincidencia – Lista IPS Fachada ADRES** ** Marcación** Se genera una marca directa cuando: 
- Existe coincidencia exacta entre cliente y lista, según: 
- Tipo de documento 
- Número de documento 
- Nombres completos o razón social  
- En el archivo el cliente figura activamente en la Lista Proveedores Fachada DIAN. 
- Si se identifican nuevos tipos o números de documento asociados al cliente: 
- Se valida si existen vinculaciones vigentes. 
- Se adiciona el resultado al log.   
  **Tipo de Coincidencia y Acción** 
**Tipo de coincidencia**  
**Acción**  
Coincidencia por 1 dato (número ID)  
Generar log  
Coincidencia por 2 datos (razón social)  
Generar log  
Coincidencia exacta (tipo ID + número ID + razón social)  
Marca directa + log  
Error en la consulta  
Reintentar hasta tres veces + log técnico  
   **Desmarcación ocurre cuando:**** 
- En la consulta actual: La fuente indica que el cliente ya no figura en la Lista IPS Fachada ADRES.    Estado “Se mantiene” cuando:** 
- El cliente estaba marcado previamente. 
- La fuente confirma que: 
- Sigue figurando en la Lista IPS Fachada ADRES.    **Validaciones SARLAFT – Lista IPS Fachada ADRES** **** 
**Elemento**  
**Definición**  
Lista  
Lista Proveedores Fachada DIAN  
Decisión  
Marca / mantiene / Desmarcación  
Manejo coincidencia parcial  
Genera log  
Aplicativo de conexión  
API Infolaft  
Aplicativo dónde está la marca:   
Riesgos consultables  
Datos de consulta:  
Tipo ID, Número ID, Nombres completos o Razón Social  ** 
Trazabilidad Obligatoria – Lista IPS Fachada ADRES** 
Por cada cliente y consulta el batch debe registrar: 
- Fecha de consulta 
- Fuente consultada 
- Datos enviados 
- Resultado obtenido 
- Acción tomada (marca / mantiene / log) 
- Responsable (sistema) 
- Identificador del proceso batch 
- Archivo de logs  
**Contenido mínimo del Log – Lista IPS Fachada ADRES** 
- DNI del cliente: Tipo de Id y número de ID 
- Nombres completos o razón social 
- Tipo de persona: 
- Natural 
- Jurídico   
- Estado vinculación 
- **Vigente: **Tiene al menos una vinculación 
- **No vigente:** No tiene vinculaciones  
- Figura: Tomador, Asegurado, Beneficiario, Afianzado, Afiliado, Proveedor, Empleado, Administrador 
- Vinculaciones:  
- Ramo, producto, plan 
- Valor prima anual, valor asegurado cobertura principal 
- Indicador tipo de régimen EPS 
- Indicador de fondo de ahorro, valor del fondo de ahorro alcanzado y valor de abono al fondo de ahorro 
- Fecha de inicio de vigencia  
- Tipo de coincidencia: Coincidencia por 1 dato, Coincidencia por 2 datos, Coincidencia exacta y Error en la consulta 
- Tipo y nombre de la lista: Lista de control 
- Fecha de consulta 
- Es la fecha en que corre el proceso en batch con la fuente de consulta  
- Fecha de marcación 
- Fecha en que se marca el cliente porque hay coincidencia exacta 
- La fecha queda vacia cuando hay coincidencia por 1 dato, Coincidencia por 2 datos y Error en la consulta  
- Estado: Marca  o Mantiene 
- Causal 
- Es el programa o sanción al que pertenece el cliente 
- Si tiene mas de un programa o sanción se debe relacionar en un solo campo  
- Documentos asociados 
- Tipo id, número id 
- Nombres completos o razón social  
- Fuente de consulta: Indicar el nombre de la API que se tiene integrada 
- Errores técnicos (si aplica)  
 **Contenido mínimo del Log de errores – Lista IPS Fachada ADRES** 
- Fecha de consulta: Es la fecha en que corre el proceso en batch con la fuente de consulta 
- Fuente de consulta: Indicar el nombre de la API que se tiene integrada 
- Cliente: Tipo ID y número de ID 
- Motivo del error 
- Número de reintentos 
- Estado final: Indicar si se logro realizar la consulta del cliente  
 
**Control de Cobertura – Lista IPS Fachada ADRES** 
El proceso debe generar métricas automáticas de: 
- Total de clientes procesados 
- Clientes marcados por Lista de Control 
- Clientes con log 
- Clientes con error 
- % de cobertura del batch

## Criterios de Aceptación

**1. Orquestación y naturaleza del proceso**
 CA‑01 Ejecución automática diaria
 Dado que el proceso está configurado
 Cuando se cumple la ventana diaria definida
 Entonces el sistema ejecuta automáticamente el proceso batch contra la Lista IPS Fachada ADRES
 Y no requiere intervención manual
 Y registra un identificador único del proceso (batch_id).
 
 CA‑02 Ejecución en ventana controlada
 Dado que el proceso se ejecuta en una ventana definida
 Cuando el batch está en curso
 Entonces no interfiere con la operación productiva ni bloquea procesos transaccionales.
 
 CA‑03 Margen de tolerancia de 24 horas
 Dado que un cliente fue consultado exitosamente dentro de las últimas 24 horas
 Cuando se ejecuta el batch
 Entonces el cliente no es nuevamente procesado
 Y el evento queda registrado como “omitido por tolerancia de 24 horas”.
 
 **2. Fuente de información y carga del archivo**
 CA‑04 Uso exclusivo del archivo como fuente
 Dado que la fuente de información es un archivo recibido mediante requerimiento formal
 Cuando inicia el batch
 Entonces el sistema utiliza únicamente dicho archivo como fuente de consulta
 Y lo identifica como Lista IPS Fachada ADRES.
 
 CA‑05 Validación de estructura mínima del archivo
 Dado que el archivo es cargado
 Cuando se valida su estructura
 Entonces el archivo debe contener como mínimo:
 
- Tipo de ID 
- Número de ID 
- Razón social 
- Fecha de ingreso 
- Tipo de lista 
- Y si falta algún campo obligatorio, se genera log técnico.   
 CA‑06 Versionamiento y trazabilidad del archivo
 Dado que el archivo es cargado exitosamente
 Cuando el batch inicia su ejecución
 Entonces el sistema asigna versión e identificador al archivo
 Y registra la fecha del archivo como parte de la trazabilidad.
 
 **3. Cobertura del proceso**
 CA‑07 Cobertura total en la primera ejecución
 Dado que es la primera ejecución del proceso
 Cuando se ejecuta el batch
 Entonces se valida el 100 % de los clientes vigentes contra el archivo de la Lista IPS Fachada ADRES.
 
 CA‑08 Cobertura incremental en ejecuciones posteriores
 Dado que existen ejecuciones previas
 Cuando se ejecuta el batch
 Entonces el sistema valida los clientes vigentes contra los nuevos registros contenidos en el archivo vigente.
 
 **4. Reglas de coincidencia**
 CA‑09 Coincidencia exacta – Marcación directa
 Dado que existe coincidencia exacta entre cliente y archivo por:
 
 Tipo de documento
 Número de documento
 Nombres completos o razón social
 Y el cliente figura activamente en la Lista IPS Fachada ADRES
 Cuando se procesa el cliente
 Entonces el sistema genera marca directa
 Y registra el resultado en el log.
 
 CA‑10 Coincidencia por un dato Dado que solo existe coincidencia por número de ID
 Cuando se procesa el cliente
 Entonces el sistema no marca
 Y genera un log con tipo de coincidencia “Coincidencia por 1 dato”.
 
 CA‑11 Coincidencia por dos datos
 Dado que existe coincidencia por razón social
 Cuando se procesa el cliente
 Entonces el sistema no marca
 Y genera un log con tipo de coincidencia “Coincidencia por 2 datos”.
 
 CA‑12 Nuevos documentos asociados
 Dado que se identifican nuevos tipos o números de documento asociados al cliente
 Cuando se procesan
 Entonces el sistema valida la existencia de vinculaciones vigentes
 Y adiciona la información al log del cliente.
 
 **5. Mantenimiento y desmarcación**
 CA‑13 Mantener marca
 Dado que el cliente estaba previamente marcado
 Y en el archivo vigente sigue figurando en la Lista IPS Fachada ADRES
 Cuando se ejecuta el batch
 Entonces el estado del cliente se mantiene como “Mantiene”
 Y se actualiza la fecha de validación.
 
 CA‑14 Desmarcación
 Dado que el cliente estaba marcado previamente
 Y en la consulta actual ya no figura en el archivo
 Cuando se procesa el cliente
 Entonces el sistema realiza la desmarcación
 Y registra la decisión en el log.
 
 **6. Manejo de errores**
 CA‑15 Reintentos en caso de error
 Dado que ocurre un error durante el procesamiento del cliente
 Cuando se intenta la consulta
 Entonces el sistema reintenta automáticamente hasta tres (3) veces.
 
 CA‑16 Registro de error técnico
 Dado que el error persiste después de los reintentos
 Cuando finaliza el procesamiento del cliente
 Entonces se genera un log técnico de error
 Y se registra el estado final de la consulta.
 
 CA‑17 Continuidad del batch
 Dado que uno o más clientes presentan errores
 Cuando el batch se ejecuta
 Entonces el proceso continúa con los demás clientes
 Y no se interrumpe la ejecución total.
 
 **7. Actualización de marcas**
 CA‑18 Actualización en sistema destino
 Dado una decisión de marca, mantenimiento o desmarcación
 Cuando se procesa el resultado
 Entonces la información se actualiza en el sistema Riesgos consultables
 Y el responsable registrado es el sistema.
 
 **8. Trazabilidad y logs**
 CA‑19 Trazabilidad obligatoria por cliente
 Dado cada cliente procesado
 Cuando finaliza la consulta
 Entonces el sistema registra:
 
- Fecha de consulta 
- Fuente consultada (archivo IPS Fachada ADRES) 
- Datos enviados 
- Resultado obtenido 
- Acción tomada 
- Responsable (sistema) 
- Identificador del batch.   CA‑20 Archivo consolidado de logs Dado que finaliza el batch
 Cuando se consolidan los resultados
 Entonces el sistema genera un archivo único de logs
 Y contiene todos los campos mínimos definidos.
 
 CA‑21 Log técnico de errores
 Dado que se presentan errores
 Cuando finaliza el proceso
 Entonces se genera un log técnico con:
 
- Fecha de consulta 
- Fuente 
- Cliente 
- Motivo del error 
- Número de reintentos 
- Estado final.   **9. Métricas y control de cobertura** CA‑22 Generación automática de métricas
 Dado que finaliza el proceso batch
 Cuando se calculan las métricas
 Entonces el sistema genera automáticamente:
 
- Total de clientes procesados 
- Clientes marcados por Lista IPS Fachada ADRES 
- Clientes con log 
- Clientes con error 
- % de cobertura del batch.
