# HU 1100215 — [Reglas transversales]: Crear evaluación para las figuras de la relación con PEP

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364) › HU 1100215 — [Reglas transversales]: Crear evaluación para las figuras de la relación con PEP

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1100215](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1100215) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-30 |
| **Última modificación** | 2026-03-30 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364)  
  Estado: New  

## Descripción

**Como** sistema SARLAFT
 **Quiero** que las figuras ingresadas en la sección de **Relación con PEP** sean evaluadas automáticamente
**Para** asignar el **riesgo intensificado**, ejecutar las validaciones correspondientes y garantizar el cumplimiento de los controles LA/FT asociados a la vinculación con PEP 
 Alcance funcional 
La funcionalidad debe aplicar a las **figuras relacionadas con PEP** que se ingresan en la sección correspondiente del proceso SARLAFT, con el siguiente comportamiento: 
- 
Las figuras ingresadas en la sección de **Relación con PEP** deben: 
- Ser evaluadas de manera automática. 
- Recibir **clasificación de riesgo intensificado**.   
- 
Para dichas figuras, el sistema debe ejecutar las siguientes validaciones mínimas: 
- Validación en **listas de control**. 
- **Consulta del estado del documento**, cuando aplique según el tipo de documento.    Impacto en la clasificación del tomador 
- Cuando el **tomador** tenga inicialmente una clasificación de **riesgo ordinario o simplificado**, y se registre una relación con PEP:

- El tomador debe ser **retipificado**. 
- Se debe asignar **riesgo intensificado**.    Controles y requisitos asociados 
Como resultado de la retipificación del tomador por relación con PEP, el sistema debe: 
- Asignar los **requisitos correspondientes**. 
- Activar la **validación de identidad**, cuando aplique. 
- Ejecutar el **control de vinculación de PEP** asociado a la relación identificada.

## Criterios de Aceptación

Evaluación de figuras con relación a PEP 
**Dado** que se ingresa una figura en la sección **Relación con PEP**
**Cuando** la información es registrada en el sistema
**Entonces** la figura debe ser **evaluada automáticamente**. Asignación de riesgo intensificado a figuras relacionadas con PEP 
**Dado** que una figura se encuentra registrada en la sección **Relación con PEP**
**Cuando** se ejecuta la evaluación de la figura
**Entonces** se debe asignar **riesgo intensificado**. Validaciones en listas de control para figuras relacionadas con PEP 
**Dado** que una figura se encuentra relacionada con PEP
**Cuando** se realiza la evaluación
**Entonces** se deben ejecutar las **validaciones mínimas en listas de control**. Consulta del estado del documento para figuras relacionadas con PEP 
**Dado** que una figura relacionada con PEP tiene un tipo de documento que lo requiere
**Cuando** se realiza la evaluación de la figura
**Entonces** se debe ejecutar la **consulta del estado del documento**. Retipificación del tomador por relación con PEP 
**Dado** que el tomador tiene inicialmente una clasificación de **riesgo ordinario o simplificado**
**Y** se registra una relación con PEP
**Cuando** el sistema evalúa dicha relación
**Entonces** el tomador debe ser **retipificado**. Asignación de riesgo intensificado al tomador retipificado 
**Dado** que el tomador ha sido retipificado por relación con PEP
**Cuando** se completa el proceso de retipificación
**Entonces** se le debe asignar **riesgo intensificado**. Asignación de requisitos al tomador retipificado 
**Dado** que el tomador ha sido retipificado
**Cuando** se asigna el nuevo nivel de riesgo
**Entonces** se deben **asignar los requisitos correspondientes**. Asignación de validación de identidad al tomador retipificado 
**Dado** que el tomador ha sido retipificado por relación con PEP
**Cuando** se asignan los controles correspondientes
**Entonces** se debe asignar la **validación de identidad**. Asignación del control de vinculación de PEP 
**Dado** que el tomador presenta una relación con PEP
**Cuando** se ejecutan los controles del proceso
**Entonces** se debe asignar el **control de vinculación de PEP**. Prueba de retipificación para tomador con riesgo simplificado 
**Dado** que el tomador tiene una clasificación inicial de **riesgo simplificado**
**Y** se ingresa una figura en la sección **Relación con PEP**
**Cuando** el sistema evalúa la relación con PEP
**Entonces** el tomador debe ser **retipificado** y recibir **riesgo intensificado**, junto con los controles definidos Prueba de retipificación para tomador con riesgo ordinario 
**Dado** que el tomador tiene una clasificación inicial de **riesgo ordinario**
**Y** se ingresa una figura en la sección **Relación con PEP**
**Cuando** el sistema evalúa la relación con PEP
**Entonces** el tomador debe ser **retipificado** y recibir **riesgo intensificado**, junto con los controles definidos. Comportamiento cuando NO se ingresa relación con PEP 
**Dado** que **no se ingresa ninguna figura** en la sección **Relación con PEP**
**Cuando** el sistema evalúa al cliente
**Entonces** los clientes con riesgo **simplificado**, **ordinario** o **intensificado** deben **mantener las condiciones actuales**, sin retipificación ni asignación adicional de controles.
