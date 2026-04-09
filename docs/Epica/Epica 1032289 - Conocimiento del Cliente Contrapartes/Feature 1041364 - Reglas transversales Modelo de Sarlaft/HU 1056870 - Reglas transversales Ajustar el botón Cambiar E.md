# HU 1056870 — [Reglas transversales]: Ajustar el botón Cambiar Estado para permitir el estado Rechazado

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364) › HU 1056870 — [Reglas transversales]: Ajustar el botón Cambiar Estado para permitir el estado Rechazado

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1056870](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1056870) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-25 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364)  
  Estado: New  

## Descripción

Como Administrador del Módulo de Clientes SARLAFT,
     quiero acceder al botón Cambiar estado desde la ruta del módulo y actualizar el estado de una evaluación PENDIENTE a Exitoso o Rechazado,
para gestionar manualmente el resultado final según las evidencias y reglas de negocio definidas para SARLAFT. 
  **Alcance****  
- Exposición del botón Cambiar estado solo para evaluaciones PENDIENTE en Consultar cliente → Resultados.  
- Los tipos de operación que aplica son: Negocio nuevo, reclamación, pagos y recaudo 
- Modal con título, subtítulo, selectores de estado (Rechazado / Exitoso) y botón “Confirmar estado”.  
- Aplicación de las reglas de negocio descritas para GAFI Negro, Rechazado (con actualización de evidencias) y Exitoso. 
- Incluir los logs de la evidencia de la modificación de estados que se realizo.  
- La visual y los textos del modal son los definidos en el archivo de referencia.     Fuera de alcance ** 
- Cambios a otros estados diferentes de **Exitoso** y **Rechazado**. 
- Modificaciones a procesos/evidencias no mencionados. 
- Cualquier ajuste en navegación distinto a la ruta indicada.      **
** **Ruta de acceso (flujo de navegación)** 
- **Módulo de clientes SARLAFT → Logueo del administrador → Consultar cliente → Buscar cliente por criterios de búsqueda → Resultados de evaluaciones.** 
- En la grilla de resultados, **solo** las evaluaciones con estado **PENDIENTE** muestran el botón **Cambiar estado**.     **Experiencia del modal ** 
Al hacer clic en **Cambiar estado**: 
- **Título:** *Cambiar estado de la evaluación* (**se mantiene**).  
- **Subtítulo:** Seleccione el nuevo estado de la evaluación, registre el análisis realizado y confirme la acción (Nuevo).
 (**nuevo**).  
- **Controles:** **Selector único** (radio buttons) para elegir **Rechazado** o **Exitoso** (**nuevo**).  
- **Detalle del análisis LA/FT: **Justificación de la modificación del estado realizado por el equipo LAFT (**nuevo**).  
- **Acción primaria:** Botón renombrado a **Confirmar estado** (antes: *Estoy seguro(a)*  **Lógica de cambio de estado (reglas funcionales)**   
- **Estado “Exitoso”** 
- Se mantiene la definición actual para el cambio del estado **PENDIENTE → Exitoso**. 
- Cuando cambie la evaluación a exitoso entonces la evidencia de GAFI cambie a exitoso y en la observaciones detallar "Modificación de evidencia por el equipo LAFT"
 
- El mensaje al usuario y la experiencia de notificación deben conservar el comportamiento actualmente definido en el módulo de clientes SARLAFT.   
- **Estado “Rechazado”**    
- El estado solo podrá cambiar a **Rechazado** cuando las evidencias relacionadas (GAFI) se encuentren en PENDIENTE y deban pasar a **Fallido**. 
- **Mensaje al usuario:****
“El cambio de estado de la evaluación a ‘Rechazado’ ha sido realizado. Por favor verifique e informe al equipo comercial.”  
- **Experiencia:**

Utilizar los modales en color verde definidos para el módulo de clientes SARLAFT.   
- Estado del formulario**    
- 
El formulario debe quedar en estado **Finalizado** para permitir el cambio de estado a **Exitoso** o **Rechazado**.  
- 
Se debe validar que el formulario solo pueda finalizar cuando: 
- La información esté completamente diligenciada, y 
- Los requisitos estén debidamente adjuntos.   
- 
Si existen requisitos pendientes, el formulario **no debe finalizar**.  
- 
Se debe permitir abrir la URL del formulario y mostrar al usuario las secciones que aún están pendientes (información o requisitos).  
- 
Si el usuario intenta cambiar el estado a Exitoso o Rechazado sin tener el formulario completado, se debe bloquear la acción y mostrar el siguiente mensaje: 
**Mensaje al usuario:** **
“No es posible cambiar el estado de la evaluación porque el formulario está pendiente por completar. Complételo e intente de nuevo.”  
- 
**Experiencia:**

Utilizar los modales en color rojo definidos para el módulo de clientes SARLAFT.    
- Detalle del análisis LA/FT** 
- Mostrar un cuadro de texto obligatorio. 
- Se permiten letras, números y caracteres especiales 
- Mantener la experiencia que se tiene en el botón de "Aprobar manual la validación de identidad"

## Criterios de Aceptación

**CA‑1. Ruta de acceso y visibilidad del botón** 
- **CA‑1.1**: La ruta de acceso es: **Módulo de clientes SARLAFT → Logueo del administrador → Consultar cliente → Buscar cliente por criterios de búsqueda → Resultados de evaluaciones**. 
- **CA‑1.2**: En la grilla de **Resultados de evaluaciones**, **solo** las evaluaciones con estado **PENDIENTE** muestran el botón **Cambiar estado**.    **CA‑2. Experiencia del modal** 
- **CA‑2.1**: Al hacer clic en **Cambiar estado**, se muestra el modal con:

- **Título**: *Cambiar estado de la evaluación* (se mantiene). 
- **Subtítulo**: *Seleccione el nuevo estado de la evaluación y confirme la acción* (nuevo). 
- **Controles**: **Selector único (radio buttons)** para elegir **Rechazado** o **Exitoso** (nuevo). 
- **Acción primaria**: Botón **Confirmar estado** (renombrado desde *Estoy seguro(a)*).      **CA‑3. Lógica de cambio a Exitoso** 
- **CA‑3.1**: Se mantiene la **definición actual** del cambio **de PENDIENTE a Exitoso**. 
- **CA‑3.2**: **Excepción GAFI Negro**:

- Si la evaluación está **PENDIENTE** por **GAFI Negro**, **debe permanecer en PENDIENTE para análisis**; una vez resuelto el análisis (según proceso LA/FT), **se permite pasar a Exitoso** desde el modal.      **CA‑4. Lógica de cambio a Rechazado** 
- **CA‑4.1**: La evaluación **pasa a Rechazado** **solo** cuando las **evidencias**: **GAFI**, **validación de identidad**, **Registraduría/Migración**, **RRCC** y **formulario** están en **PENDIENTE** y **deben pasar a Fallido**. 
- **CA‑4.2**: Para el **formulario**, su estado debe **actualizarse de PENDIENTE a FINALIZADO** **antes** de confirmar el rechazo.    **CA‑5. Alcance / Fuera de alcance** 
- **CA‑5.1 (Alcance)**:

- Exposición del botón **Cambiar estado** **solo** para evaluaciones **PENDIENTE** en **Consultar cliente → Resultados**. 
- Modal con **título**, **subtítulo**, **selectores de estado (Rechazado / Exitoso)** y botón **Confirmar estado**. 
- Aplicación de las **reglas de negocio** descritas para **GAFI Negro**, **Rechazado** (con actualización de evidencias) y **Exitoso**.   
- **CA‑5.2 (Fuera de alcance)**:

- Cambios a **otros estados** distintos de **Exitoso** y **Rechazado**. 
- **Modificaciones** a procesos/evidencias **no mencionados**. 
- Cualquier **ajuste de navegación** diferente a la **ruta indicada**.
