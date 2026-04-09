# HU 1046069 — [Reglas transversales]: Analizar clientes con nacionalidad de países GAFI Negro

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364) › HU 1046069 — [Reglas transversales]: Analizar clientes con nacionalidad de países GAFI Negro

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1046069](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046069) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-13 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364)  
  Estado: New  

## Descripción

Como analista SARLAFT, quiero que el sistema, cuando el país de nacimiento, persona natural o país de constitución en persona jurídica perteneciente a la categoría de países “Negra”, no rechace automáticamente, sino que deje la evaluación en estado Pendiente para análisis del equipo LA/FT y posterior cambio manual a Exitoso o Rechazado por el Administrador, para asegurar un tratamiento diferenciado y controlado en las operaciones de Negocio nuevo, Pago de reclamación, cancelación, Recaudo y pago. 
 **Alcance** 
- Figuras: Tomador, asegurado, beneficiario, afianzado, afiliado, representante legal, accionistas, junta directiva, beneficiario del pago, apoderado, responsable del pago.  
- Tipos de cliente: Persona natural y persona jurídica. 
- Operaciones: en Negocio nuevo, Pago de reclamación, cancelación, Recaudo y pago 
- Evidencia: Países de la lista GAFI en la categoría “Negra”  
- Estados involucrados:  
- Pendiente → (cambio manual por Administrador) → Exitoso. 
- Pendiente → (cambio manual por Administrador) → Rechazado.**  
- Las evidencias de la consulta con listas de control, consulta del estado del documento de identidad con la registraduria y migración, diligenciamiento del formulario, adjuntar requisitos y validar identidad  no cambia en sus estados. 
- El formulario actual es NO APLICA, se debe modificar a 
- Formulario: 
- Actual: No aplica 
- Nuevo: Intensificado (según el tipo de persona)  
- Requisitos: 
- 2305 CERTIFICADO DE INGRESOS Y RETENCIONES 
- 2307 COPIA DE LA DECLARACION DE RENTA DEL ULTIMO PERIODO GRAVABLE
  
- Validaciones: Asignar validación de identidad    ** **
** **Descripción Funcional** 
- 
Durante la evaluación SARLAFT (en Negocio nuevo, Pago de reclamación, cancelación, Recaudo y pago): 
- Persona Natural (PN): si el cliente tiene el país de nacimiento está clasificado en la categoría de países “Negra”, no se debe rechazar automáticamente por este motivo; se debe marcar como **Pendiente **para análisis manual LA/FT. 
- Persona Jurídica (PJ): si el país de constitución está clasificado en “Negra”, no se debe rechazar automáticamente por este motivo; se debe marcar como **Pendiente **para análisis manual LA/FT.   
- 
El estado **Pendiente **deberá mostrar un mensaje funcional al usuario "El cliente (DNI de la figura y nombres) debe ser analizado por el equipo de LAFT, por favor notifique para la gestión".   
- 
Se cambia de estado **Pendiente a Exitoso o Pendiente a Rechazado** mediante el botón ubicado en el modulo de clientes Sarlaft - consultar cliente - resultado evaluaciones  
- El resultado debe garantizar que se notifique la respuesta a los aplicativos de negocio con el fin de que puedan continuar o no con la expedición del seguro según el resultado del análisis LAFT.

## Criterios de Aceptación

**CA‑1. Aplicación por figuras** 
- **CA‑1.1:** El tratamiento definido para países en categoría “Negra” aplica a todas las figuras indicadas:

Tomador, asegurado, beneficiario, afianzado, afiliado, representante legal, accionistas, junta directiva, beneficiario del pago, apoderado, responsable del pago.    **CA‑2. Aplicación por tipo de cliente** 
- CA‑2.1: Para Persona Natural, si el país de nacimiento pertenece a la categoría “Negra”, la evaluación no debe ser rechazada automáticamente. 
- CA‑2.2: Para Persona Jurídica, si el país de constitución pertenece a la categoría “Negra”, la evaluación no debe ser rechazada automáticamente.    **CA‑3. Aplicación por tipo de operación** 
- CA‑3.1: Las reglas aplican para las operaciones de:
Negocio nuevo, Pago de reclamación, Cancelación, Recaudo y Pago.    **CA‑4. Estado asignado cuando hay coincidencia en categoría “Negra”** 
- CA‑4.1: Cuando se detecte país “Negra” (PN o PJ), la evaluación debe quedar en estado Pendiente. 
- CA‑4.2: Se debe mostrar al usuario el mensaje funcional:
“El cliente (DNI de la figura y nombres) debe ser analizado por el equipo de LAFT, por favor notifique para la gestión”.    **CA‑5. Cambios manuales de estado** 
- CA‑5.1: El estado Pendiente puede cambiarse manualmente a Exitoso mediante el botón disponible en Módulo de Clientes SARLAFT → Consultar cliente → Resultado evaluaciones. 
- CA‑5.2: El estado Pendiente puede cambiarse manualmente a Rechazado desde el mismo botón y ubicación.    **CA‑6. Evidencias que no cambian** 
- CA‑6.1: Las evidencias de:

- Consulta en listas de control 
- Consulta del estado del documento con Registraduría/Migración 
- Diligenciamiento del formulario 
- Adjuntar requisitos 
- Validación de identidad
no deben cambiar en sus estados por efecto de esta regla.      **CA‑7. Notificación a aplicativos de negocio** 
- CA‑7.1: El resultado final (Pendiente→Exitoso o Pendiente→Rechazado) debe ser notificado a los aplicativos de negocio para que puedan continuar o detener la expedición del seguro según corresponda.
