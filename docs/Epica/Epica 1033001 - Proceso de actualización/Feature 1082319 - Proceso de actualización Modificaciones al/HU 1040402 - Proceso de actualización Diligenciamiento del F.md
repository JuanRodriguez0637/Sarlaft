# HU 1040402 — [Proceso de actualización]: Diligenciamiento del Formulario

[Épica 1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001) › [Feature 1082319 — [Proceso de actualización]: Modificaciones al Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082319) › HU 1040402 — [Proceso de actualización]: Diligenciamiento del Formulario

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1040402](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1040402) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-10 |
| **Última modificación** | 2026-03-19 |

## Jerarquía

- **Épica:** [1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001)  
  Estado: New  
- **Feature:** [1082319 — [Proceso de actualización]: Modificaciones al Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082319)  
  Estado: New  

## Descripción

Como Analista SARLAFT quiero que el formulario SARLAFT permita al cliente completar la información pendiente y validar su identidad para cerrar el proceso de actualización y garantizar la calidad y veracidad de los datos suministrados. 
 **Reglas de negocio** **
** **Formulario** 
 
- Debe tomarse la experiencia del formulario actual definido para un proceso de actualización 
- Experiencia actual: https://sarlaft.labsura.com/redirect/iniciar-proceso/4F32D7379BBA648A39A890478B7E94CBEAF88ED4C8DB4C201B63C693248FF524/3445e978-5b0e-48c8-9e02-0362b291074f/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJTdXJhLmNvbSIsImF1ZCI6IlNhcmxhZnQiLCJzdWIiOiJTQVJMQUZUIiwiaWF0IjoxNzcwODM1MDUyLCJleHAiOjE3NzEyNjcwNTJ9.XjnUJfguqEMlaDTSZyXSxs-gKoL_S0E7qcY3hYva2Fo
  
- El formulario debe adaptarse al tipo de cliente (Persona Natural o Persona Jurídica) y al tipo de riesgo unificado (simplificado, ordinario o intensificado)
 
- Para el formulario de Personas Naturales (PN), debe realizarse validación de identidad antes de permitir el diligenciamiento de las demás secciones. 
- Tener en cuenta el flujo para validar identidad con Experian y el de adjuntar la copia del documento de identidad.  
- Para Personas Jurídicas (PJ), se muestran las secciones y posterior se envía la notificación para la validación de identidad (flujo definido actualmente) al representante legal.  
- A los accionistas y la junta directiva, no se les envía la notificación de validación de identidad  
- El formulario debe ser compatible con todos los navegadores (como Google Chrome) y con diferentes dispositivos de acceso, ya sea un computador o un teléfono móvil.    **Pre diligenciamiento** 
- En el pre llenado no se debe realizar consulta de nuevo con Experian o Informacolombia si ya se hizo anteriormente. Se debe pre cargar la información consultada anteriormente. 
- Respecto a las secciones  
- Datos básicos: No mostrar al usuario siempre y cuando este completamente diligenciada. Si tiene un campo vacio, mostrar la sección para completarlo. Los campos de: tipo id, número id, nombres y apellidos se muestran inhabilitados. 
- Datos de contacto, financieros, relación con PEP y soportes: Mostrar los campos que tengan información guardada en la base de datos y los campos que estén vacios.  
- En los datos de contacto, mantener las reglas de enmascarar los datos para: número de celular, correo electrónico y dirección  
- Debe contener las reglas de obligatoriedad y calidad de los campos en cada sección definidos actualmente.  **Resultado** 
 
- El formulario solo puede finalizarse cuando: 
- Todas las secciones han sido completadas. Si el cliente modifica el dato que se mostró se debe actualizar en la base de datos. 
- Al menos un requisito ha sido adjuntado cuando aplique,   
- La actualización se completa cuando: 
- El formulario este finalizado 
- La validación de identidad sea exitosa. 
- El cliente pasa de estado "Desactualizado" a "Actualizado" si cumple las dos condiciones mencionadas.  
- Si el formulario se interrumpe sin completarse, el cliente debe quedar con estado “Desactualizado”. 
- Si la validación de identidad es fallida y el formulario esta pendiente, el cliente queda con el estado "Desactualizado".
 
- Si la validación de identidad es fallida y el formulario esta finalizado, el cliente queda con el estado "Rechazado". Estos clientes no se deben incluir de nuevo en el lote.

## Criterios de Aceptación

**CA‑1. Uso de la experiencia actual del formulario** 
- CA‑1.1: El formulario SARLAFT debe utilizar la experiencia actual definida para el proceso de actualización, según el formulario vigente. 
- CA‑1.2: El formulario debe adaptarse al tipo de cliente: Persona Natural (PN) o Persona Jurídica (PJ). 
- CA‑1.3: El formulario debe adaptarse al tipo de riesgo unificado: simplificado, ordinario o intensificado.      **CA‑2. Validación de identidad para Personas Naturales** 
- CA‑2.1: Para Personas Naturales, se debe validar la identidad antes de permitir el diligenciamiento de las demás secciones. 
- CA‑2.2: Debe tenerse en cuenta el flujo actual de:

- Validación de identidad con Experian. 
- Adjuntar copia del documento de identidad.        **CA‑3. Validación de identidad para Personas Jurídicas** 
- CA‑3.1: Para Personas Jurídicas, el formulario debe mostrar las secciones correspondientes antes de la validación de identidad. 
- CA‑3.2: Luego de diligenciar el formulario, se debe enviar la notificación para validar la identidad del representante legal, según el flujo actual. 
- CA‑3.3: A accionistas y junta directiva no se les envía la notificación de validación de identidad.      **CA‑4. Compatibilidad del formulario** 
- CA‑4.1: El formulario debe ser compatible con el navegador de Google Chrome definido por la compañía. 
- CA‑4.2: El formulario debe ser accesible desde computador y teléfono móvil.      **CA‑5. Pre diligenciamiento** 
- CA‑5.1: En el pre llenado, no se debe volver a consultar Experian ni Informacolombia si ya se consultó previamente. 
- CA‑5.2: Se debe pre‑cargar la información obtenida previamente de esas consultas.      **CA‑6. Comportamiento por sección** 
 6.1 Datos básicos 
- CA‑6.1.1: La sección de Datos básicos no se muestra al usuario cuando está completamente diligenciada. 
- CA‑6.1.2: La sección de Datos básicos  se muestra al usuario cuando al menos un campo este vacío. Los campos de tipo id, número id, nombres apellidos se muestran inhabilitados.
      6.2 Datos de contacto, financieros, relación con PEP y soportes 
- CA‑6.2.1: Se deben mostrar los campos que ya tengan información guardada en la base de datos. 
- CA‑6.2.2: Se deben mostrar los campos que estén vacíos para su diligenciamiento. 
- CA‑6.2.3: En datos de contacto, se debe mantener la regla de enmascarar:

- Número de celular 
- Correo electrónico 
- Dirección   
- CA‑6.2.4: En todas las secciones deben mantenerse las reglas de obligatoriedad y calidad definidas actualmente.      **CA‑7. Finalización del formulario** 
- CA‑7.1: El formulario solo puede finalizarse cuando:

- Todas las secciones estén completadas. 
- Al menos un requisito esté adjuntado, cuando aplique.   
- CA‑7.2: Si el cliente modifica un dato que se mostró en el formulario, el sistema debe actualizar ese dato en la base de datos.      **CA‑8. Condiciones para completar la actualización** 
- CA‑8.1: La actualización se completa únicamente cuando:

- El formulario está finalizado. 
- La validación de identidad es exitosa.   
- CA‑8.2: Si se cumplen ambas condiciones, el cliente debe pasar de estado “Desactualizado” a “Actualizado”.      **CA‑9. Comportamiento cuando el proceso no finaliza** Formulario incompleto 
- CA‑9.1: Si el formulario se interrumpe sin completarse, el cliente queda en estado “Desactualizado”.      Validación de identidad fallida + formulario pendiente 
- CA‑9.2: Si la validación de identidad es fallida y el formulario no está finalizado, el cliente queda en estado “Desactualizado”.      Validación de identidad fallida + formulario finalizado 
- CA‑9.3: Si la validación de identidad es fallida y el formulario está finalizado, el cliente queda en estado “Rechazado”. 
- CA‑9.4: Los clientes en estado “Rechazado” no deben ser incluidos nuevamente en el lote.
