# HU 1098643 — [Riesgo]: Crear evaluaciones sarlaft a las operaciones no conectadas

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000) › HU 1098643 — [Riesgo]: Crear evaluaciones sarlaft a las operaciones no conectadas

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1098643](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1098643) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-26 |
| **Última modificación** | 2026-03-30 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000)  
  Estado: New  

## Descripción

**Como** sistema SARLAFT
 **Quiero** crear evaluaciones de **Negocio Nuevo** para operaciones **no conectadas**
**Para** identificar y evaluar el riesgo LA/FT del **tomador, asegurado, beneficiario o afiliado**, ya sea persona natural o jurídica, cuando el cliente no ha pasado previamente por **SARLAFT 4.0**. 
 Alcance funcional 
La funcionalidad debe permitir la **creación automática de evaluaciones SARLAFT** para operaciones no conectadas, mediante un **proceso en batch**, con las siguientes características: 
- Se debe disponibilizar el servicio de creación de evaluación de Negocio Nuevo con las secciones de: 
- Tomador 
- Figuras distintas al tomador 
- Póliza 
- Datos del Id de negocio, solicitud dni y aplicación  
- La evaluación debe aplicar a las figuras:

- Tomador 
- Asegurado 
- Beneficiario 
- Afiliado   
- La figura evaluada puede ser **persona natural o persona jurídica**. 
- El proceso debe:

- Crear la evaluación SARLAFT 
- Ejecutar las validaciones mínimas  
- Nota: Mantener condiciones de crear, remitir un resultado de la evaluación de negocio nuevo, mensajes de inconsistencias y errores y, reglas del motor)    Integración y disponibilidad 
- La funcionalidad debe estar disponible para integrarse con:

- **Administración del riesgo** 
- Cualquier otro flujo del proceso que se defina   
- Aplica cuando el cliente **no ha pasado previamente por SARLAFT 4.0**.  Comportamiento del proceso batch 
- Las validaciones deben ejecutarse en **modalidad batch**. 
- Aunque el proceso reciba el **código de la aplicación origen**, **no se debe entregar respuesta** al sistema que invoca el servicio. 
- La **fecha de creación de la evaluación** debe corresponder a la **fecha en la que se ejecuta el proceso batch**.  Resultados y visibilidad 
- Los **resultados de las evaluaciones** deben ser visibles en el **Datalake de Administración del Riesgo**. 
- Si a la evaluación le aplica **formulario**, el sistema debe **notificar a la Administración del Riesgo** para que dicho flujo determine **cuándo lanzar el proceso de actualización** correspondiente.  Operaciones habilitadas para evaluaciones no conectadas 
Cuando se trate de una **operación no conectada**, se deben habilitar las siguientes opciones: 
- Negocio nuevo (01) 
- Reclamaciones (RE) 
- Modificaciones Valorables (MV) 
- Modificaciones No Valorables (MNV) 
- Cancelaciones (05) 
- Inclusión de asegurados (IA)

## Criterios de Aceptación

Creación de evaluaciones SARLAFT 
- El sistema debe permitir la **creación automática de evaluaciones SARLAFT de Negocio Nuevo** para **operaciones no conectadas**. 
- La creación de evaluaciones debe ejecutarse mediante un **proceso en modalidad batch**. 
- El sistema debe disponibilizar el **servicio de creación de evaluación de Negocio Nuevo** con las siguientes secciones:

- Tomador 
- Figuras distintas al tomador 
- Póliza 
- Datos del ID de negocio, solicitud DNI y aplicación   
- La evaluación creada debe aplicar a las siguientes figuras:

- Tomador 
- Asegurado 
- Beneficiario 
- Afiliado   
- La figura evaluada puede corresponder a **persona natural o persona jurídica**. 
- El proceso batch debe:

- Crear la evaluación SARLAFT. 
- Ejecutar las **validaciones mínimas** definidas.   
- El proceso debe mantener las condiciones actuales relacionadas con:

- Creación de la evaluación. 
- Remisión del resultado de la evaluación de negocio nuevo. 
- Mensajes de inconsistencias y errores. 
- Reglas del motor.    Integración y disponibilidad 
- La funcionalidad debe estar disponible para integrarse con el flujo de **Administración del Riesgo**. 
- La funcionalidad debe estar disponible para integrarse con **otros flujos del proceso que se definan**. 
- La funcionalidad aplica únicamente cuando el cliente **no ha pasado previamente por SARLAFT 4.0**.  Comportamiento del proceso batch 
- Las validaciones deben ejecutarse exclusivamente en **modalidad batch**. 
- Aunque el proceso reciba el **código de la aplicación origen**, **no se debe entregar respuesta** al sistema que invoca el servicio. 
- La **fecha de creación de la evaluación** debe corresponder a la **fecha en la que se ejecuta el proceso batch**.  Resultados y visibilidad 
- Los **resultados de las evaluaciones** deben ser visibles en el **Datalake de Administración del Riesgo**. 
- Si a la evaluación le aplica formulario, el sistema debe **notificar a la Administración del Riesgo** para que dicho flujo determine **cuándo lanzar el proceso de actualización** correspondiente.  Operaciones habilitadas para evaluaciones no conectadas 
- Para evaluaciones creadas a partir de **operaciones no conectadas**, se deben habilitar las siguientes opciones:  
- Negocio Nuevo (01) 
- Reclamaciones (RE) 
- Modificaciones Valorables (MV) 
- Modificaciones No Valorables (MNV) 
- Cancelaciones (05) 
- Inclusión de asegurados (IA)
