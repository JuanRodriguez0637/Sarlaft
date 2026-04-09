# HU 1037085 — [Optimización]: Reemplazar datos de la consulta del estado del documento

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999) › HU 1037085 — [Optimización]: Reemplazar datos de la consulta del estado del documento

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1037085](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037085) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-06 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)  
  Estado: New  

## Descripción

Como Analista SARLAFT, 
quiero que, después de la creación de una evaluación y como resultado de la consulta del estado del documento con la Registraduría Nacional y Migración Colombia (a través del servicio de Experian), el sistema valide y, de ser necesario, corrija automáticamente los nombres completos y la fecha de expedición, y guarde el resultado de la nacionalidad exactamente como lo entrega el servicio, 
para garantizar la consistencia de la información de identidad antes de ejecutar el flujo de validación de identidad, evitar rechazos por datos errados y mitigar costos operativos originados por fallas en la consulta a la Registraduría y en el proceso de validación de identidad cuando posteriormente se logra validar dichos datos, sin generar impacto ni visibilidad para el usuario final. 
 ** Reglas de negocio** **
** **Disparador y alcance** 
- La verificación y corrección se ejecuta posterior a la creación de la evaluación y antes de iniciar el flujo de validación de identidad. 
- El proceso no debe exponer mensajes ni pantallas al usuario final. 
- Cuando el estado del documento es VIGENTE, CANCELADO, INACTIVO, CANCELADO POR DUPLICIDAD, FALLECIDO, FALSA IDENTIDAD, le aplica las reglas de negocio que están a continuación: 
- Si el estado es diferente a los mencionados, no le aplica las reglas de negocio.   **Condición de coincidencia base** 
- Si la respuesta del servicio (Registraduría / Migración vía Experian) indica coincidencia en:

- Tipo de documento 
- Número de documento 
- Primer apellido  
- Entonces proceder con la comparación de campos críticos.  **Comparación de datos críticos**

- Comparar nombres completos y fecha de expedición entre:

- Datos retornados por el servicio (fuente externa).  
- Datos almacenados en la evaluación (fuente interna). 
- Si son iguales: no realizar cambios; continuar flujo. 
- Si son diferentes: actualizar los campos internos con los valores del servicio y persistir el cambio.    **Nacionalidad (regla específica)** 
- Guardar la nacionalidad exactamente como la entrega el servicio (mismo texto/valor, sin normalizaciones adicionales). 
- Esta regla aplica tanto si hubo corrección de otros campos como si no.   **Trazabilidad técnica (no visible al usuario)** 
- Registrar en bitácora interna: id_evaluacion, campos antes/después, fuente, fecha/hora y resultado de la operación (actualizado / sin cambios / error). 
- Cualquier error debe no bloquear el flujo

## Criterios de Aceptación

CA‑01. Ejecución automática posterior a la creación de la evaluación 
**Dado** que se ha creado una evaluación,
**Cuando** el sistema ejecute la consulta del estado del documento con la Registraduría Nacional y Migración Colombia a través del servicio de Experian,
**Entonces** la validación y corrección automática de datos deberá ejecutarse **después de la creación de la evaluación y antes de iniciar el flujo de validación de identidad**,
**Y** el proceso **no deberá mostrar mensajes ni generar interacción visible** para el usuario final.    CA‑02. Aplicabilidad por estado del documento 
**Dado** que el servicio retorna uno de los siguientes estados del documento:

VIGENTE, CANCELADO, INACTIVO, CANCELADO POR DUPLICIDAD, FALLECIDO o FALSA IDENTIDAD,
**Cuando** se procese la respuesta de la consulta,
**Entonces** el sistema deberá aplicar las reglas de negocio definidas para la validación y corrección automática.    CA‑03. Estados no elegibles 
**Dado** que el estado del documento retornado por el servicio **no** se encuentra dentro de los estados definidos como elegibles,
**Cuando** se procese la respuesta,
**Entonces** el sistema **no deberá aplicar ninguna validación ni corrección automática** sobre los datos de la evaluación 
**Y** deberá continuar el flujo normal sin modificaciones.    CA‑04. Condición de coincidencia base cumplida 
**Dado** que la respuesta del servicio de Experian indica coincidencia en: 
- Tipo de documento 
- Número de documento 
- Primer apellido  
**Cuando** se valide la respuesta de la consulta,
**Entonces** el sistema deberá proceder a comparar los **nombres completos** y la **fecha de expedición**.    CA‑05. Coincidencia total de datos críticos 
**Dado** que existe coincidencia en tipo, número de documento y primer apellido,
**Y** los **nombres completos** y la **fecha de expedición** retornados por el servicio son **iguales** a los almacenados en la evaluación,
**Cuando** se ejecute la validación posterior a la creación,
**Entonces** el sistema **no deberá realizar ninguna modificación** sobre los datos
**Y** deberá permitir la continuidad normal del proceso.    CA‑06. Diferencia en nombres y/o fecha de expedición 
**Dado** que existe coincidencia en tipo, número de documento y primer apellido,
**Y** los **nombres completos** y/o la **fecha de expedición** retornados por el servicio son **diferentes** a los registrados en la evaluación,
**Cuando** se ejecute la validación,
**Entonces** el sistema deberá: 
- **Actualizar automáticamente** los campos discrepantes en la evaluación. 
- **Persistir únicamente** los valores retornados por el servicio de Experian como fuente confiable. 
- Continuar el proceso usando los datos corregidos.     CA‑07. Persistencia de la nacionalidad 
**Dado** que el servicio de Experian retorna el campo **nacionalidad**,
**Cuando** se procese la respuesta,
**Entonces** el sistema deberá **guardar la nacionalidad exactamente como la entrega el servicio**,
**Y** esta acción deberá realizarse **independientemente** de si se corrigieron o no otros campos de la evaluación.    CA‑08. Uso correcto en el flujo de validación de identidad 
**Dado** que la evaluación fue corregida automáticamente en nombres completos y/o fecha de expedición,
**Cuando** posteriormente se ejecute el flujo de validación de identidad,
**Entonces** el sistema deberá utilizar los **datos corregidos**,
**Y** no deberá producir rechazos asociados a inconsistencias en dichos campos.    CA‑09. Trazabilidad técnica obligatoria 
**Dado** que el sistema ejecute una validación o corrección automática,
**Cuando** finalice el proceso,
**Entonces** se deberá registrar en una bitácora interna, como mínimo: 
- id_evaluacion 
- Campos originales y campos finalizados 
- Fuente del dato (Experian) 
- Fecha y hora del proceso 
- Resultado de la operación (ACTUALIZADO / SIN CAMBIOS / ERROR)     CA‑10. Manejo de errores no bloqueante 
**Dado** que ocurra un error durante la validación o corrección automática,
**Cuando** el sistema capture la excepción,
**Entonces**: 
- El error deberá quedar **registrado en la bitácora interna**. 
- El proceso **no deberá bloquear el flujo** ni generar mensajes al usuario final. 
- El flujo de evaluación deberá continuar conforme a las reglas generales del sistema.
