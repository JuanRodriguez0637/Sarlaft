# HU 1030004 — [Monitoreo]: Lista Proveedores Fachada DIAN - InfoLaft

[Épica 1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585) › [Feature 1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784) › HU 1030004 — [Monitoreo]: Lista Proveedores Fachada DIAN - InfoLaft

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1030004](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1030004) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Ciencia de datos |
| **Creado** | 2026-02-02 |
| **Última modificación** | 2026-02-06 |

## Jerarquía

- **Épica:** [1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585)  
  Estado: New  
- **Feature:** [1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784)  
  Estado: New  

## Descripción

Como Analista SARLAFT** 
 
quiero que el sistema ejecute de forma automática y diaria un proceso batch de monitoreo contra la Lista Proveedores Fachada DIAN,para validar el 100 % de la base de clientes, aplicar reglas de marcación, mantenimiento o desmarcación, y generar logs completos, garantizando trazabilidad auditable y cumplimiento normativo SARLAFT, sin intervención manual. 
** 
**Naturaleza del Proceso – Lista Proveedores Fachada DIAN** 
**Atributo**  
**Definición**  
**Tipo**  
Batch  
**Ejecución**  
Automática  
**Frecuencia**  
Diario  
**Momento**  
Ventana definida (sin afectar producción)  
**Alcance**  
100 % de los clientes vigentes de la compañía.  
**Resultado**  
Archivo de logs + actualización de marcas de Lista de Control  
**Margen de tolerancia**  
El margen de tolerancia para volver a consultar un cliente es de 24 horas, contado a partir de la última ejecución exitosa del proceso  
**Trazabilidad**  
Obligatoria y auditable  
  
**Descripción Funcional – Lista Proveedores Fachada DIAN** 
**Alcance del Proceso** 
El proceso batch debe: 
- La consulta de los clientes vigentes en la lista de control debe ejecutarse automáticamente todos los días. 
- Tomar la totalidad de clientes vigentes y ejecutar según las siguientes ejecuciones: 
- Cobertura de la 1.ª ejecución: 100 % de los clientes de la compañía. 
- Cobertura de la 2.ª ejecución: consulta solo los “nuevos registros” de la lista de control con los clientes vigentes de la compañía.  
- Validar cada cliente exclusivamente contra la causal “Lista Proveedores Fachada DIAN”. 
- Aplicar reglas de coincidencia y decisión. 
- El proceso marca, mantiene, actualiza fechas y genera logs completos.** 
- Si la fuente de consulta falla: 
- Reintenta automáticamente según política de reintentos  
- Registra el error en log técnico con el estado final. 
- Continúa con los demás clientes (no bloquea todo el batch).  
- Actualizar las marcas correspondientes en los sistemas definidos. 
- Generar un archivo consolidado de logs con los resultados. 
- Guardar trazabilidad auditable por cliente y por lista. 
- Generar métricas de los clientes procesados.  
** 
**Reglas de Coincidencia – Lista Proveedores Fachada DIAN** 
**Marcación** 
Se genera una marca directa cuando: 
- Existe coincidencia exacta entre cliente y lista, según: 
- Tipo de documento 
- Número de documento 
- Nombres completos o razón social  
- La fuente confirma que el cliente figura activamente en la Lista Proveedores Fachada DIAN. 
- Si se identifican nuevos tipos o números de documento asociados al cliente: 
- Se valida si existen vinculaciones vigentes. 
- Se adiciona el resultado al log.   
  
 **Tipo de Coincidencia y Acción** 
**Tipo de coincidencia**  
**Acción**  
Coincidencia por 1 dato (número ID)  
Generar log  
Coincidencia por 2 datos (nombres completos)  
Generar log  
Coincidencia exacta (tipo ID + número ID + nombres)  
Marca directa + log  
Error en la consulta  
Reintentar hasta tres veces + log técnico  
  
**Estado “Se mantiene” cuando:** 
- El cliente estaba marcado previamente. 
- La fuente confirma que: 
- Sigue figurando en la Lista Proveedores Fachada DIAN. 
- No hay cambios relevantes en programa o condición.   
**Decisión SARLAFT – Lista Proveedores Fachada DIAN** 
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
Aplicativo donde queda la marca  
Riesgos consultables  
Datos de consulta  
Tipo ID, Número ID, Nombres completos o Razón Social  
  
**Trazabilidad Obligatoria – Lista Proveedores Fachada DIAN** 
Por cada cliente y consulta el batch debe registrar: 
- Fecha de consulta 
- Fuente consultada 
- Datos enviados 
- Resultado obtenido 
- Acción tomada (marca / mantiene / log) 
- Responsable (sistema) 
- Identificador del proceso batch 
- Archivo de logs  
**Contenido mínimo del Log – Lista Proveedores Fachada DIAN** 
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
 **Contenido mínimo del Log de errores – Lista Proveedores Fachada DIAN** 
- Fecha de consulta: Es la fecha en que corre el proceso en batch con la fuente de consulta 
- Fuente de consulta: Indicar el nombre de la API que se tiene integrada 
- Cliente: Tipo ID y número de ID 
- Motivo del error 
- Número de reintentos 
- Estado final: Indicar si se logro realizar la consulta del cliente  
 
**Control de Cobertura – Lista Proveedores Fachada DIAN** 
El proceso debe generar métricas automáticas de: 
- Total de clientes procesados 
- Clientes marcados por Lista de Control 
- Clientes con log 
- Clientes con error 
- % de cobertura del batch

## Criterios de Aceptación

1. Naturaleza y ejecución del proceso CA‑01 Ejecución automática diaria 
**Dado** que el proceso está parametrizado
**Cuando** llega la ventana diaria definida
**Entonces** el sistema ejecuta automáticamente el proceso batch de monitoreo contra la **Lista Proveedores Fachada DIAN**
**Y** no requiere intervención manual
**Y** registra un identificador único del proceso batch. CA‑02 Ejecución en ventana controlada 
**Dado** que el proceso tiene una ventana definida
**Cuando** el batch se ejecuta
**Entonces** no afecta la operación productiva ni bloquea procesos transaccionales. CA‑03 Margen de tolerancia de 24 horas 
**Dado** que un cliente fue consultado exitosamente dentro de las últimas 24 horas
**Cuando** se ejecuta el batch
**Entonces** el cliente no es nuevamente consultado
**Y** el evento queda registrado como “omitido por tolerancia 24h”. 2. Cobertura y alcance CA‑04 Cobertura total en la primera ejecución 
**Dado** que es la primera vez que se ejecuta el proceso
**Cuando** corre el batch
**Entonces** se consulta el **100 % de los clientes vigentes** de la compañía
**Y** la cobertura queda reflejada en las métricas del proceso. CA‑05 Cobertura incremental en ejecuciones posteriores 
**Dado** que existen ejecuciones previas del proceso
**Cuando** se ejecuta el batch
**Entonces** se consultan únicamente los **nuevos registros de la Lista Proveedores Fachada DIAN**
**Y** se cruzan contra la base de clientes vigentes. CA‑06 Exclusividad de causal 
**Dado** un cliente vigente
**Cuando** se realiza la consulta
**Entonces** el cliente se valida **exclusivamente contra la causal “Lista Proveedores Fachada DIAN”**
**Y** no se evalúan otras listas o causales SARLAFT. 3. Reglas de coincidencia CA‑07 Coincidencia exacta – Marcación directa 
**Dado** que existe coincidencia exacta por: 
- Tipo de documento 
- Número de documento 
- Nombres completos o razón social
**Y** la fuente confirma que el cliente figura activamente en la Lista Proveedores Fachada DIAN
**Cuando** se procesa el cliente
**Entonces** el sistema genera **marca directa**
**Y** registra el evento en el log.  CA‑08 Coincidencia parcial por un dato 
**Dado** que solo existe coincidencia por número de documento
**Cuando** se procesa el cliente
**Entonces** el sistema **no marca**
**Y** genera un **log informativo**. CA‑09 Coincidencia parcial por dos datos 
**Dado** que existe coincidencia por nombres completos o razón social
**Cuando** se procesa el cliente
**Entonces** el sistema **no marca**
**Y** genera un **log informativo**. CA‑10 Identificación de nuevos documentos 
**Dado** que la fuente retorna nuevos tipos o números de documento asociados al cliente
**Cuando** se detectan
**Entonces** el sistema valida si existen vinculaciones vigentes
**Y** adiciona esta información al log del cliente. 4. Mantenimiento y desmarcación CA‑11 Mantener marca existente 
**Dado** que el cliente estaba previamente marcado
**Y** la fuente confirma que sigue figurando en la Lista Proveedores Fachada DIAN
**Y** no hay cambios relevantes en programa o condición
**Cuando** se ejecuta el batch
**Entonces** el estado del cliente se mantiene como **“Mantiene”**
**Y** se actualiza la fecha de validación. CA‑12 Desmarcación del cliente 
**Dado** que el cliente estaba marcado previamente
**Y** en la consulta actual la fuente indica que **ya no figura** en la lista
**Cuando** se procesa el cliente
**Entonces** el sistema **desmarca** al cliente
**Y** registra la desmarcación en el log con fecha y causal. 5. Manejo de errores y continuidad CA‑13 Reintentos automáticos 
**Dado** que ocurre un error al consultar la fuente
**Cuando** se realiza la consulta
**Entonces** el sistema reintenta automáticamente hasta **tres (3) veces**. CA‑14 Registro de errores técnicos 
**Dado** que el error persiste después de los reintentos
**Cuando** finaliza la consulta del cliente
**Entonces** se genera un **log técnico de error**
**Y** se registra el estado final de la consulta. CA‑15 Continuidad del batch 
**Dado** que uno o más clientes presentan error
**Cuando** el batch está en ejecución
**Entonces** el proceso continúa con los demás clientes
**Y** no se interrumpe la ejecución total. 6. Actualización de marcas CA‑16 Actualización en sistema destino 
**Dado** una decisión de marca, mantiene o desmarcación
**Cuando** se procesa el resultado
**Entonces** la información se actualiza en el aplicativo **Riesgos consultables**
**Y** el responsable registrado es el **sistema**. 7. Trazabilidad y logs CA‑17 Trazabilidad obligatoria por cliente 
**Dado** un cliente consultado
**Cuando** finaliza su procesamiento
**Entonces** el sistema registra como mínimo: 
- Fecha de consulta 
- Fuente consultada 
- Datos enviados 
- Resultado obtenido 
- Acción tomada 
- Responsable (sistema) 
- Identificador del batch.  CA‑18 Archivo consolidado de logs 
**Dado** que finaliza el proceso batch
**Cuando** se consolidan los resultados
**Entonces** se genera un **archivo único de logs**
**Y** contiene todos los campos mínimos definidos para la Lista Proveedores Fachada DIAN. CA‑19 Log técnico de errores 
**Dado** que existen errores en la ejecución
**Cuando** finaliza el batch
**Entonces** se genera un log técnico con: 
- Fecha de consulta 
- Fuente 
- Cliente 
- Motivo del error 
- Número de reintentos 
- Estado final.  8. Métricas y control de cobertura CA‑20 Generación automática de métricas 
**Dado** que el batch finaliza
**Cuando** se calculan las métricas
**Entonces** el sistema genera automáticamente: 
- Total de clientes procesados 
- Clientes marcados por Lista Proveedores Fachada DIAN 
- Clientes con log 
- Clientes con error 
- % de cobertura del batch.  CA‑21 Disponibilidad para auditoría 
**Dado** un batch ejecutado
**Cuando** se requiere información para auditoría SARLAFT
**Entonces** las métricas, logs y trazabilidad están disponibles por identificador del proceso.
