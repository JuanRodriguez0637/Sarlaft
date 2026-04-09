# HU 1029994 — [Monitoreo]: Listas PEP - Infolaft

[Épica 1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585) › [Feature 1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784) › HU 1029994 — [Monitoreo]: Listas PEP - Infolaft

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1029994](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029994) |
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
 
quiero que el sistema ejecute de forma automática y diaria un proceso batch de monitoreo contra la Lista PEPpara validar el 100 % de la base de clientes, aplicar reglas de marcación, mantenimiento o desmarcación, y generar logs completos, garantizando trazabilidad auditable y cumplimiento normativo SARLAFT, sin intervención manual. 
** 
**Naturaleza del Proceso – Lista PEP** 
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
Archivo de logs + actualización de marcas de Lista PEP  
**Margen de tolerancia**  
El margen de tolerancia para volver a consultar un cliente es de 24 horas, contado a partir de la última ejecución exitosa del proceso  
**Trazabilidad**  
Obligatoria y auditable  
  
**Descripción Funcional – Lista PEP** 
**Alcance del Proceso** 
El proceso batch debe: 
- La consulta de los clientes vigentes en la lista de control debe ejecutarse automáticamente todos los días. 
- Tomar la totalidad de clientes vigentes y ejecutar según las siguientes ejecuciones: 
- Cobertura de la 1.ª ejecución: 100 % de los clientes de la compañía. 
- Cobertura de la 2.ª ejecución: consulta solo los “nuevos registros” de la lista de control con los clientes vigentes de la compañía.  
- Validar cada cliente exclusivamente contra la lista PEP 
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
**Reglas de Coincidencia – Lista PEP** 
**Marcación** 
Se genera una marca directa cuando: 
- Existe coincidencia exacta entre cliente y lista, según: 
- Tipo de documento 
- Número de documento  
- La fuente confirma que el cliente figura activamente en la Lista PEP. 
- Si se identifican nuevos tipos o números de documento asociados al cliente: 
- Se valida si existen vinculaciones vigentes. 
- Se adiciona el resultado al log.   
  **Tipo de Coincidencia y Acción** 
**Tipo de coincidencia**  
**Acción**  
Coincidencia por 1 dato (número ID)  
Generar log  Coincidencia exacta (tipo ID + número ID)  Marca directa + log Error en la consulta   Reintentar hasta tres veces + log técnico 
  **Desmarcación ocurre cuando:**

 
- En la consulta actual: 
- La fuente indica que el cliente ya no figura en la Lista PEP.    **Estado “Se mantiene” cuando:**  
- El cliente estaba marcado previamente. 
- La fuente confirma que: 
- Sigue figurando en la Lista PEP. 
- No hay cambios relevantes en programa o condición.  
- El cliente no tiene vinculaciones activas.
  
 
 
**Decisión SARLAFT – Lista PEP** 
**Elemento**  
**Definición**  
Lista  
Lista PEP  
Decisión  
Marca / mantiene /Desmarca  
Manejo coincidencia parcial  
Genera log  
Aplicativo de conexión  
API Infolaft  
Aplicativo donde queda la marca  
Riesgos consultables  
Datos de consulta  
Tipo ID, Número ID  
  
**Trazabilidad Obligatoria – Lista PEP.** 
Por cada cliente y consulta el batch debe registrar: 
- Fecha de consulta 
- Fuente consultada 
- Datos enviados 
- Resultado obtenido 
- Acción tomada (marca / mantiene / desmarcacion / log) 
- Responsable (sistema) 
- Identificador del proceso batch 
- Archivo de logs  
**Contenido mínimo del Log – PEP** 
- DNI del cliente: Tipo de Id y número de ID 
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
- Tipo de coincidencia: Coincidencia por 1 dato, Coincidencia exacta y Error en la consulta 
- Tipo y nombre de la lista: Lista PEP 
- Fecha de consulta 
- Es la fecha en que corre el proceso en batch con la fuente de consulta  
- Fecha de marcación 
- Fecha en que se marca el cliente porque hay coincidencia exacta 
- La fecha queda vacia cuando hay coincidencia por 1 dato, Coincidencia por 2 datos y Error en la consulta  
- Estado: Marca, desmarcación o Mantiene 
- Causal 
- Cargo  
- Documentos asociados 
- Tipo id, número id 
- Nombres completos o razón social  
- Fuente de consulta: Indicar el nombre de la API que se tiene integrada 
- Errores técnicos (si aplica)  
 **Contenido mínimo del Log de errores – Lista PEP** 
- Fecha de consulta: Es la fecha en que corre el proceso en batch con la fuente de consulta 
- Fuente de consulta: Indicar el nombre de la API que se tiene integrada 
- Cliente: Tipo ID y número de ID 
- Motivo del error 
- Número de reintentos 
- Estado final: Indicar si se logro realizar la consulta del cliente  
 
**Control de Cobertura – Lista PEP** 
El proceso debe generar métricas automáticas de: 
- Total de clientes procesados 
- Clientes marcados por Lista PEP 
- Clientes con log 
- Clientes con error 
- % de cobertura del batch

## Criterios de Aceptación

1. Orquestación y naturaleza del proceso CA‑01 Ejecución automática diaria 
**Dado** que el proceso está configurado en una ventana definida
**Cuando** llega la hora programada
**Entonces** el sistema ejecuta automáticamente el batch de Lista PEP
**Y** no requiere intervención manual
**Y** registra el identificador único del proceso batch. CA‑02 Ventana controlada sin impacto productivo 
**Dado** que el proceso se ejecuta en ventana definida
**Cuando** el batch está en ejecución
**Entonces** no afecta la operación productiva ni bloquea otros procesos. CA‑03 Tolerancia de 24 horas por cliente 
**Dado** que un cliente fue consultado exitosamente en las últimas 24 horas
**Cuando** se ejecuta el batch
**Entonces** el cliente no es nuevamente consultado
**Y** se registra en trazabilidad como “omitido por tolerancia 24h”. 2. Cobertura del proceso CA‑04 Cobertura total en primera ejecución 
**Dado** que es la primera ejecución del proceso
**Cuando** se ejecuta el batch
**Entonces** se consulta el **100 % de los clientes vigentes** de la compañía
**Y** la cobertura queda reflejada en las métricas del proceso. CA‑05 Cobertura incremental en ejecuciones posteriores 
**Dado** que ya existe una ejecución previa
**Cuando** se ejecuta el batch
**Entonces** se consultan únicamente los **nuevos registros de la Lista PEP**
**Y** se validan contra la base total de clientes vigentes. CA‑06 Exclusividad de validación 
**Dado** un cliente vigente
**Cuando** es consultado
**Entonces** se valida **exclusivamente contra la Lista PEP**
**Y** no se evalúan otras listas o causales SARLAFT. 3. Reglas de coincidencia y decisión CA‑07 Coincidencia exacta – Marca directa 
**Dado** que existe coincidencia exacta por: 
- Tipo de documento 
- Número de documento
**Y** la fuente confirma que el cliente figura activamente como PEP
**Cuando** se procesa el cliente
**Entonces** el sistema genera **marca directa PEP**
**Y** registra el evento en el log.  CA‑08 Coincidencia parcial por 1 dato 
**Dado** que solo existe coincidencia por número de documento
**Cuando** se procesa el cliente
**Entonces** el sistema **no marca**
**Y** genera únicamente un **log informativo**. CA‑09 Identificación de nuevos documentos 
**Dado** que la fuente retorna nuevos tipos o números de documento asociados al cliente
**Cuando** se procesan
**Entonces** el sistema valida si existen vinculaciones vigentes
**Y** adiciona el resultado en el log del cliente. 4. Mantenimiento y desmarcación CA‑10 Mantener marca PEP 
**Dado** que el cliente estaba previamente marcado como PEP
**Y** la fuente confirma que sigue figurando en la Lista PEP
**Y** no hay cambios relevantes en cargo o condición
**Y** el cliente no tiene vinculaciones activas
**Cuando** se ejecuta el batch
**Entonces** el estado del cliente se mantiene como **“Mantiene”**
**Y** se actualiza la fecha de validación. CA‑11 Desmarcación de cliente PEP 
**Dado** que el cliente estaba previamente marcado
**Y** en la consulta actual la fuente indica que **ya no figura** en la Lista PEP
**Cuando** se procesa el cliente
**Entonces** el sistema **desmarca** al cliente
**Y** registra la desmarcación en el log con fecha y causal. 5. Manejo de errores y continuidad CA‑12 Reintentos automáticos 
**Dado** que ocurre un error en la consulta a la fuente
**Cuando** se intenta consultar el cliente
**Entonces** el sistema reintenta automáticamente hasta **3 veces**. CA‑13 Registro de error técnico 
**Dado** que el error persiste tras los reintentos
**Cuando** finaliza la consulta del cliente
**Entonces** se genera un **log técnico de error**
**Y** se registra el estado final de la consulta. CA‑14 No bloqueo del batch 
**Dado** que uno o varios clientes presentan error
**Cuando** se ejecuta el batch
**Entonces** el proceso continúa con los demás clientes
**Y** no se interrumpe la ejecución total. 6. Actualización de marcas CA‑15 Actualización en sistema destino 
**Dado** una decisión de marca, mantiene o desmarca
**Cuando** se procesa el resultado
**Entonces** la marca se actualiza en el aplicativo **Riesgos consultables**
**Y** el responsable registrado es el sistema. 7. Trazabilidad y logs CA‑16 Trazabilidad obligatoria por cliente 
**Dado** cada cliente procesado
**Cuando** se completa la consulta
**Entonces** el sistema registra: 
- Fecha de consulta 
- Fuente consultada 
- Datos enviados 
- Resultado obtenido 
- Acción tomada 
- Responsable (sistema) 
- Identificador del batch.  CA‑17 Generación de archivo consolidado de logs 
**Dado** que finaliza el batch
**Cuando** se generan los resultados
**Entonces** se produce un **archivo consolidado de logs**
**Y** contiene todos los campos mínimos definidos para Lista PEP. CA‑18 Log técnico de errores 
**Dado** que existen errores
**Cuando** finaliza el proceso
**Entonces** se genera un log de errores con: 
- Fecha de consulta 
- Fuente 
- Cliente 
- Motivo del error 
- Número de reintentos 
- Estado final.  8. Métricas y control de cobertura CA‑19 Generación automática de métricas 
**Dado** que el batch finaliza
**Cuando** se consolidan los resultados
**Entonces** el sistema genera automáticamente: 
- Total de clientes procesados 
- Clientes marcados PEP 
- Clientes con log 
- Clientes con error 
- % de cobertura del batch.  CA‑20 Disponibilidad para auditoría 
**Dado** un proceso ejecutado
**Cuando** se solicita información por auditoría o control SARLAFT
**Entonces** las métricas, logs y trazabilidad están disponibles por identificador de batch.
