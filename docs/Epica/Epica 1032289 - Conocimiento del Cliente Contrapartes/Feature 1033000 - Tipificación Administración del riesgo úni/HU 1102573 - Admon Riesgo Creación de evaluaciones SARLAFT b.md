# HU 1102573 — [Admon Riesgo]: Creación de evaluaciones SARLAFT batch para operaciones conectadas

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000) › HU 1102573 — [Admon Riesgo]: Creación de evaluaciones SARLAFT batch para operaciones conectadas

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1102573](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1102573) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-04-01 |
| **Última modificación** | 2026-04-01 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000)  
  Estado: New  

## Descripción

Como analista SARLAFT Quiero crear de forma automática evaluaciones SARLAFT para operaciones conectadas mediante un proceso batch Para asegurar que las operaciones que hacen parte de flujos conectados cuenten con evaluaciones SARLAFT generadas de forma masiva, consistente y trazable, conforme a SARLAFT 4.0. 
 **Alcance funcional** 
- La funcionalidad debe permitir la creación automática de evaluaciones SARLAFT para operaciones conectadas, mediante un proceso batch. 
- El proceso se ejecuta sobre operaciones provenientes de flujos conectados que requieren evaluación SARLAFT durante la expedición o posterior. 
- La creación de la evaluación aplica cuando el cliente:

- No ha sido evaluado previamente bajo SARLAFT 4.0, o 
- Requiere una nueva evaluación asociada a la operación conectada.  
- Cuando el aplicativo entregue la información se debe: 
- Validar estructura definida para recibir la información 
- Reglas de calidad 
- Emitir mensajes de errores (500) o inconsistencias (400)  
- La evaluación creada incluye las siguientes secciones:

- Tomador - Obligatorio 
- Tipo id, numero id, -> Obligatorio 
- primer nombre (obligatorio), segundo nombre (Opcional), primer apellido (obligatorio),, segundo apellido (Opcional) 
- Razón social -> Obligatorio 
- Fecha de expedición del documento -> Obligatorio 
- Fecha de nacimiento -> Opcional  
- Correo electrónico -> Obligatorio 
- Número de Celular -> Obligatorio 
- País de nacimiento o constitución -> Obligatorio  
- Figuras distintas al tomador -> Asegurado, beneficiario, afianzado, afiliado 
- Tipo id, numero id, -> Obligatorio 
- primer nombre (obligatorio), segundo nombre (Opcional), primer apellido (obligatorio),, segundo apellido (Opcional)  
- Póliza 
- Valor asegurado -> Obligatorio 
- Prima -> Obligatorio 
- Ramo -> Obligatorio 
- Subramo -> Obligatorio 
- Plan -> Obligatorio 
- Canal -> Obligatorio 
- Asesor -> Obligatorio 
- Oficina -> Obligatorio 
- Tipo persona -> Obligatorio 
- Tipo negocio -> Obligatorio  
- Datos del negocio 
- Id de negocio -> Obligatorio 
- Solicitud DNI -> Obligatorio 
- Aplicación origen -> Obligatorio 
- Tipo de operación -> Obligatorio 
- Negocio nuevo (01) 
- Reclamaciones (RE) 
- Modificaciones valorables (MV) 
- Modificaciones no valorables (MNV) 
- Cancelaciones (05) 
- Inclusión de asegurados (IA)   
- Auditoría de ejecución del proceso batch (control operativo) 
- El proceso batch debe registrar: 
- Identificador único de ejecución (ID de evaluación Sarlaft) 
- Fecha y hora de inicio de ejecución 
- Fecha y hora de fin de ejecución 
- Estado del batch:     
- Ejecutado correctamente 
- Ejecutado con errores 
- Ejecutado parcialmente 
- Número total de registros procesados 
- Número de evaluaciones creadas 
- Número de evaluaciones con error   
- El proceso que genere el error debe ser reportado al equipo de TI para relanzamiento indicando el motivo por el cual no termino de ejecutarse    **Decisiones sobre las figuras evaluadas** 1. Aplicación de reglas del motor y asignación de riesgo 
- Todas las figuras evaluadas deben **pasar por las reglas del motor SARLAFT**, de acuerdo con el **tipo de operación** asociada. 
- Como resultado de la evaluación, el motor debe:

- Asignar el **nivel de riesgo** 
- Determinar el **tipo de formulario** (si aplica) 
- Definir los **requisitos asociados**   
- Estas decisiones se aplican tanto al **Tomador** como a las **figuras distintas del tomador**. 
- Para el caso de las figuras distintas del tomador:

- **No se debe habilitar formulario**, independientemente del nivel de riesgo asignado.    2. Validaciones aplicables por tipo de figura 
- Las validaciones a ejecutar dependen de la figura evaluada:

- **Tomador**:

- Validaciones de **PEP** 
- Validaciones de **GAFI** 
- Validaciones de **RRCC** 
- Validación de **documento de persona natural (document_pn)** 
- Validación con **Experian**, cuando aplique según el **tipo de riesgo**   
- **Figuras distintas del tomador**:

- Validaciones de **RRCC** 
- Validación de **documento de persona natural (document_pn)**     
- No se deben ejecutar validaciones de PEP, GAFI ni Experian sobre figuras distintas del tomador.  3. Asignación de estado de la evaluación 
- A cada evaluación SARLAFT se le debe asignar uno de los **estados definidos actualmente**:

- **PENDIENTE** 
- **RECHAZADO** 
- **FINALIZADO**   
- El estado asignado corresponde al resultado del proceso de evaluación posterior a la expedición. 
- Los estados y resultados:

- **No deben ser enviados ni respondidos al aplicativo de origen**, dado que la evaluación se ejecuta de manera posterior a la expedición de la operación.    4. Persistencia y visibilidad de la evaluación 
- La evaluación SARLAFT generada debe:

- Guardarse en la **base de datos SARLAFT** 
- Estar disponible para su visualización en el **Datalake de Administración del Riesgo**   
- Para el caso específico de la validación de **documento de persona natural (document_pn)**:

- Se debe almacenar el **estado del documento**, según el resultado obtenido por:

- **Registraduría**, o 
- **Proceso de migración**, según corresponda      5. Reglas de herencia 
- Se deben **mantener las reglas de herencia vigentes** definidas para el proceso de **Negocio Nuevo**. 
- Esto incluye la reutilización de:

- Criterios de evaluación 
- Lógica de asignación de riesgo 
- Comportamiento por figura    **Comportamiento del proceso batch**  
- Las validaciones SARLAFT deben ejecutarse todos los días en modalidad batch durante la noche sin afectar la operación transaccional. 
- El proceso debe:

- Crear la evaluación SARLAFT 
- Ejecutar las validaciones mínimas requeridas 
- Aplicar las reglas del motor SARLAFT 
- Emitir un estado 
- Guardar en la base de datos   
- Aunque el proceso reciba el **código de la aplicación origen**:

- No se debe entregar respuesta síncrona o asíncrona al sistema que invoca el servicio.   
- La fecha de creación de la evaluación debe corresponder a la fecha de ejecución del proceso batch.

## Criterios de Aceptación

CA-01 Creación automática de evaluaciones SARLAFT en batch 
- Dado un conjunto de **operaciones conectadas** provenientes de flujos conectados 
- Cuando se ejecute el proceso batch 
- Entonces se deben **crear automáticamente evaluaciones SARLAFT** para dichas operaciones.  CA-02 Aplicabilidad de la creación de la evaluación 
- La evaluación SARLAFT **solo se debe crear** cuando:

- El cliente **no ha sido evaluado previamente bajo SARLAFT 4.0**, o 
- El cliente **requiere una nueva evaluación asociada a la operación conectada**.    CA-03 Validación de estructura y reglas de calidad de información 
- Cuando el aplicativo entregue la información al proceso batch:

- Se debe **validar la estructura definida** para recibir la información. 
- Se deben aplicar las **reglas de calidad**.   
- Si se presentan errores de estructura o información:

- Se deben emitir **mensajes de error (500)** o **mensajes de inconsistencias (400)** según corresponda.    CA-04 Secciones obligatorias de la evaluación SARLAFT 
- La evaluación creada debe incluir obligatoriamente las secciones:

- **Tomador** 
- **Figuras distintas al tomador** 
- **Póliza** 
- **Datos del negocio**    CA-05 Información obligatoria del Tomador 
- La evaluación SARLAFT **no debe crearse** si el Tomador no contiene como mínimo:

- Tipo de identificación (**obligatorio**) 
- Número de identificación (**obligatorio**) 
- Primer nombre (**obligatorio**) 
- Primer apellido (**obligatorio**) 
- Razón social (**obligatorio**) 
- Fecha de expedición del documento (**obligatorio**) 
- Correo electrónico (**obligatorio**) 
- Número de celular (**obligatorio**) 
- País de nacimiento o constitución (**obligatorio**)   
- Los campos segundo nombre, segundo apellido y fecha de nacimiento son **opcionales**.  CA-06 Información obligatoria de figuras distintas al tomador 
- Para las figuras **Asegurado, Beneficiario, Afianzado y Afiliado**, la evaluación debe incluir obligatoriamente:

- Tipo de identificación 
- Número de identificación 
- Primer nombre 
- Primer apellido   
- Los campos segundo nombre y segundo apellido son **opcionales**.  CA-07 Información obligatoria de la Póliza 
- La evaluación SARLAFT **no debe crearse** si no se informa:

- Valor asegurado 
- Prima 
- Ramo 
- Subramo 
- Plan 
- Canal 
- Asesor 
- Oficina 
- Tipo de persona 
- Tipo de negocio    CA-08 Información obligatoria de datos del negocio 
- La evaluación SARLAFT debe contener obligatoriamente:

- Id de negocio 
- Solicitud DNI 
- Aplicación origen 
- Tipo de operación    CA-09 Tipos de operación permitidos 
- El tipo de operación informado **solo puede corresponder** a uno de los siguientes valores:

- Negocio nuevo (01) 
- Reclamaciones (RE) 
- Modificaciones valorables (MV) 
- Modificaciones no valorables (MNV) 
- Cancelaciones (05) 
- Inclusión de asegurados (IA)    CA-10 Auditoría de ejecución del proceso batch 
- Cada ejecución del proceso batch debe registrar:

- Identificador único de ejecución (ID de evaluación SARLAFT) 
- Fecha y hora de inicio 
- Fecha y hora de fin 
- Estado del batch:

- Ejecutado correctamente 
- Ejecutado con errores 
- Ejecutado parcialmente   
- Número total de registros procesados 
- Número de evaluaciones creadas 
- Número de evaluaciones con error    CA-11 Reporte de errores del proceso batch 
- Cuando el proceso batch termine con errores o de forma parcial:

- El proceso que generó el error debe ser **reportado al equipo de TI** 
- El reporte debe indicar el **motivo por el cual no terminó de ejecutarse** 
- El objetivo del reporte es el **relanzamiento del proceso**.    CA-12 Aplicación de reglas del motor SARLAFT 
- Todas las figuras evaluadas deben pasar por las **reglas del motor SARLAFT**, según el tipo de operación. 
- El motor debe:

- Asignar nivel de riesgo 
- Determinar tipo de formulario (si aplica) 
- Definir requisitos asociados   
- Estas decisiones aplican tanto al Tomador como a las figuras distintas del tomador. 
- Para las figuras distintas del tomador:

- **No se debe habilitar formulario**, sin excepción.    CA-13 Validaciones por tipo de figura 
- Para el **Tomador**, se deben ejecutar:

- Validaciones PEP 
- Validaciones GAFI 
- Validaciones RRCC 
- Validación de document_pn 
- Validación con Experian, cuando aplique según el tipo de riesgo   
- Para las **figuras distintas del tomador**, se deben ejecutar únicamente:

- Validaciones RRCC 
- Validación de document_pn   
- No se deben ejecutar validaciones de PEP, GAFI ni Experian para figuras distintas del tomador.  CA-14 Asignación de estado de la evaluación 
- Cada evaluación SARLAFT debe quedar en **uno** de los estados:

- PENDIENTE 
- RECHAZADO 
- FINALIZADO   
- El estado corresponde al resultado del proceso posterior a la expedición. 
- Los estados y resultados:

- **No deben enviarse ni responderse** al aplicativo de origen.    CA-15 Persistencia y visibilidad de la evaluación 
- La evaluación SARLAFT generada debe:

- Guardarse en la **base de datos SARLAFT** 
- Estar disponible en el **Datalake de Administración del Riesgo**   
- Para document_pn:

- Se debe guardar el **estado del documento** 
- Según resultado de **Registraduría** o **migración**, según corresponda.    CA-16 Reglas de herencia 
- El proceso debe mantener las **reglas de herencia vigentes** definidas para Negocio Nuevo, incluyendo:

- Criterios de evaluación 
- Lógica de asignación de riesgo 
- Comportamiento por figura    CA-17 Ejecución operativa del proceso batch 
- Las validaciones SARLAFT deben ejecutarse:

- **Todos los días** 
- En modalidad **batch nocturno** 
- Sin afectar la operación transaccional   
- El proceso debe:

- Crear la evaluación 
- Ejecutar validaciones mínimas 
- Aplicar reglas del motor 
- Emitir un estado 
- Guardar la evaluación    CA-18 Fecha de creación de la evaluación 
- La fecha de creación de la evaluación SARLAFT debe ser exactamente la **fecha de ejecución del proceso batch**.  CA-19 No respuesta al aplicativo de origen 
- Aunque el proceso reciba el código de la aplicación origen:

- **No se debe entregar respuesta síncrona ni asíncrona** al sistema que invoca el servicio.
