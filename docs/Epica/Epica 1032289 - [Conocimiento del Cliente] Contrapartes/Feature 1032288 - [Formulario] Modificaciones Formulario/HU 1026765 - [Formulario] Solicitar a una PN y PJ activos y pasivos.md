# HU 1026765 — [Formulario]: Solicitar a una PN y PJ activos y pasivos

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1026765 — [Formulario]: Solicitar a una PN y PJ activos y pasivos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1026765](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026765) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-01-29 |
| **Última modificación** | 2026-02-12 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)  
  Estado: New  

## Descripción

Como Analista SARLAFT
  Quiero que el formulario de datos financieros permita capturar y actualizar los valores de Activos y Pasivos del cliente Persona Natural y Persona Jurídica
Para contar con información financiera completa, consistente y vigente que soporte los análisis de conocimiento del cliente y el cumplimiento normativo. 
 
- **Alcance funcional** 
- **Aplica a formularios:** Ordinario e Intensificado. 
- **Tipo de persona:** Natural 
- **Secciones impactadas:** Datos financieros del formulario. 
- **Poblaciones: **Persona Natural y Persona Jurídica 
- **Campos nuevos: **Activos y Pasivos (numéricos, obligatorios ambos). 
- **Persistencia: **se almacena el último valor vigente (no hay histórico). 
- **Operación:** no hay recolección retroactiva para las persona naturales sin dato; se captura sólo desde la salida a producción.    **Definición de Campos ** 
**1) Activos (obligatorio)** 
- **Tipo de dato funcional:** numérico no negativo. 
- **Formato de entrada:** dígitos; separadores de miles visibles opcionales (autoformateo), sin símbolos 
- **Rango funcional:** >= 10.000 
- **Mensajes:** 
- Vacío: “El valor de **Activos** es obligatorio.” 
- No numérico: “Solo se permiten números en **Activos**.” 
- Rango: “El valor de **Activos** debe ser **mayor o igual a 10.000**.”   
**2) Pasivos (obligatorio)** 
- **Tipo de dato funcional:** numérico no negativo. 
- **Formato de entrada:** igual a Activos. 
- **Rango funcional:** >= 0 
- **Mensajes:**
- Vacío: “El valor de **Pasivos** es obligatorio.” 
- No numérico: “Solo se permiten números en **Pasivos**.” 
- Rango: “El valor de **Pasivos** debe ser **mayor o igual a 0**.”    
**Precarga / Edición** 
- Si existe valor registrado en BD → mostrar prellenado y editable. 
- Si NO existe valor → mostrar vacío con validaciones activas.  
**Persistencia** 
- Guardar como campos separados: Activos y pasivos 
- No gestionar histórico (sólo último valor).

## Criterios de Aceptación

1. Alcance y disponibilidad CA‑01 Formularios habilitados 
**Dado** un formulario de tipo **Ordinario** o **Intensificado**
**Cuando** el usuario accede a la sección **Datos financieros**
**Entonces** el sistema muestra los campos **Activos** y **Pasivos**. CA‑02 Tipo de persona 
**Dado** un cliente **Persona Natural** o **Persona Jurídica**
**Cuando** se diligencia el formulario
**Entonces** el comportamiento de los campos **Activos** y **Pasivos** es el mismo para ambos tipos de persona. 2. Definición y validaciones del campo Activos CA‑03 Tipo de dato Activos 
**Dado** el campo **Activos**
**Cuando** el usuario ingresa información
**Entonces** el sistema acepta **únicamente valores numéricos**
**Y** no permite letras, caracteres especiales ni símbolos. CA‑04 Obligatoriedad de Activos 
**Dado** el campo **Activos**
**Cuando** el usuario intenta **guardar o avanzar** sin diligenciarlo
**Entonces** el sistema bloquea la acción
**Y** muestra el mensaje: 
*“El valor de Activos es obligatorio.”* CA‑05 Rango mínimo de Activos 
**Dado** el campo **Activos** diligenciado
**Cuando** el valor ingresado es **menor a 10.000**
**Entonces** el sistema no permite guardar
**Y** muestra el mensaje: 
*“El valor de Activos debe ser mayor o igual a 10.000.”* CA‑06 Validación de formato Activos 
**Dado** el campo **Activos**
**Cuando** el usuario intenta ingresar un valor no numérico
**Entonces** el sistema muestra el mensaje: 
*“Solo se permiten números en Activos.”* 3. Definición y validaciones del campo Pasivos CA‑07 Tipo de dato Pasivos 
**Dado** el campo **Pasivos**
**Cuando** el usuario ingresa información
**Entonces** el sistema acepta **únicamente valores numéricos**
**Y** no permite letras, caracteres especiales ni símbolos. CA‑08 Obligatoriedad de Pasivos 
**Dado** el campo **Pasivos**
**Cuando** el usuario intenta **guardar o avanzar** sin diligenciarlo
**Entonces** el sistema bloquea la acción
**Y** muestra el mensaje: 
*“El valor de Pasivos es obligatorio.”* CA‑09 Rango mínimo de Pasivos 
**Dado** el campo **Pasivos** diligenciado
**Cuando** el valor ingresado es **menor a 10.000**
**Entonces** el sistema no permite guardar
**Y** muestra el mensaje: 
*“El valor de Pasivos debe ser mayor o igual a 0.”* 
*(Se valida exactamente según la definición funcional entregada.)* CA‑10 Validación de formato Pasivos 
**Dado** el campo **Pasivos**
**Cuando** el usuario intenta ingresar un valor no numérico
**Entonces** el sistema muestra el mensaje: 
*“Solo se permiten números en Pasivos.”* 4. Precarga y edición de información CA‑11 Precarga cuando existe información previa 
**Dado** que el cliente tiene valores de **Activos** y/o **Pasivos** registrados en la base de datos
**Cuando** se carga el formulario
**Entonces** el sistema **precarga automáticamente** los valores
**Y** los campos se muestran **editables**. CA‑12 Visualización cuando no existe información 
**Dado** que el cliente **no tiene valores registrados**
**Cuando** se carga el formulario
**Entonces** los campos **Activos** y **Pasivos** se muestran **vacíos**
**Y** con las validaciones activas. CA‑13 Actualización de valores 
**Dado** que existen valores precargados
**Cuando** el usuario modifica **Activos** y/o **Pasivos** y guarda
**Entonces** el sistema reemplaza los valores previamente almacenados. 5. Persistencia de la información CA‑14 Almacenamiento estructurado 
**Dado** valores válidos diligenciados
**Cuando** el usuario guarda el formulario
**Entonces** el sistema almacena los valores en base de datos como campos separados: 
- **Activos** 
- **Pasivos**  CA‑15 Sin gestión de histórico 
**Dado** una actualización de **Activos** o **Pasivos**
**Cuando** se guarda la información
**Entonces** el sistema conserva **solo el último valor vigente**
**Y** no mantiene histórico de cambios. 6. Alcance operacional CA‑16 Captura desde salida a producción 
**Dado** que la funcionalidad entra en producción
**Cuando** se diligencian los campos
**Entonces** el sistema almacena únicamente información capturada **a partir de la salida a producción**
**Y** no realiza recolección retroactiva para personas naturales ni jurídicas sin dato previo. 7. Trazabilidad auditable CA‑17 Trazabilidad del registro 
**Dado** un guardado o actualización de **Activos** y/o **Pasivos**
**Cuando** se persiste la información
**Entonces** el sistema registra trazabilidad que permita identificar como mínimo: 
- Origen del registro 
- Fecha y hora de registro 
- Responsable del registro
