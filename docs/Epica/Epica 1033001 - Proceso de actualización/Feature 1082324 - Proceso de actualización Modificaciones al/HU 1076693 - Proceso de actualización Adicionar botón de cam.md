# HU 1076693 — [Proceso de actualización]: Adicionar botón de cambiar estado de desactualizado a actualizado

[Épica 1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001) › [Feature 1082324 — [Proceso de actualización]: Modificaciones al Modulo de Clientes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082324) › HU 1076693 — [Proceso de actualización]: Adicionar botón de cambiar estado de desactualizado a actualizado

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1076693](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076693) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | sin revisar |
| **Creado** | 2026-03-16 |
| **Última modificación** | 2026-03-30 |

## Jerarquía

- **Épica:** [1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001)  
  Estado: New  
- **Feature:** [1082324 — [Proceso de actualización]: Modificaciones al Modulo de Clientes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082324)  
  Estado: New  

## Descripción

Como Administrador del Módulo de Clientes SARLAFT,**       quiero acceder al botón Cambiar estado desde la ruta del módulo y actualizar el estado de una evaluación RECHAZADO O CANCELADO a DESACTUALIZADO.para gestionar manualmente los casos del proceso de actualización en el que el cliente falle en la validación de identidad   Alcance****  
- Exposición del botón Cambiar estado solo para evaluaciones RECHAZADAS O CANCELADAS en Consultar cliente → Tipo operación: Actualización → Resultados.  
- Los tipos de operación que aplica son: Actualización 
- Modal con título, subtítulo, selectores de estado. 
- Incluir los logs de la evidencia de la modificación de estados que se realizo.  
- La visual y los textos del modal debe mantener la experiencia que se tiene en el botón de "Aprobar manual la validación de identidad" 
- Aplica para el perfil adminsitrador     Ruta de acceso (flujo de navegación)** 
- **Módulo de clientes SARLAFT → Logueo del administrador → Consultar cliente/Tipo de operación: Actualización → Buscar cliente por criterios de búsqueda → Resultados de evaluaciones.** 
- En la grilla de resultados, **solo** las evaluaciones con estado **RECHAZADO **muestran el botón **Cambiar estado**.     **Experiencia del modal ** 
Al hacer clic en **Cambiar estado**: 
- **Título:** *Cambiar estado de la evaluación* (**se mantiene**).  
- **Subtítulo:** Seleccione el nuevo estado de la evaluación, registre el análisis realizado y confirme la acción (Nuevo).**(**nuevo**).  
- **Controles:** **Selector único** (radio buttons) para elegir ACTUALIZADO **o **DESACTUALIZADO**.  
- **Detalle del análisis LA/FT: **Justificación de la modificación del estado realizado por el equipo LAFT (**nuevo**).  
- **Acción primaria:** Botón renombrado a **Confirmar estado** (antes: *Estoy seguro(a)*  **Lógica de cambio de estado (reglas funcionales)**   
- **Estado “RECHAZADO Y CANCELADO”** 
- Cuando cambie la evaluación a DESACTUALIZADO entonces las evidencias se comporten así: 
- GAFI: Mantener estado 
- RRCC: Mantener estado 
- PEPS: Mantener estado 
- EXPERIAN: Pasar a pendiente. Debe permitir volver a realizar la validación de identidad. Las funcionalidades para renviar y el botón aprobar deben estar habilitadas.  
- Formulario: Mantener estado  
- **Debe mostrar un modal informando el cambio y un Detalle del análisis LA/FT**  ****Título** 
**Cambiar estado de la evaluación** **Texto informativo** 
Verifique que la evaluación sea la correcta, ya que esta acción permitirá cambiar su estado de **Cancelado** o **Rechazado** a **Desactualizado**, con el fin de que el usuario pueda **completar nuevamente la evaluación de actualización**. **Detalle del análisis LA/FT** 
**Campo obligatorio (cuadro de texto)** 
**Etiqueta del campo:**
**Detalle del análisis LA/FT** 
**Descripción / ayuda contextual (opcional):**

Ingrese el análisis correspondiente que sustente el cambio de estado de la evaluación. 
**Reglas del campo:** 
- El campo es **obligatorio** para continuar con la acción. 
- Se permite el ingreso de:

- Letras 
- Números 
- Caracteres especiales    ¿Está seguro de cambiar el estado de la evaluación? **Botón** 
**Estoy seguro(a)**  ** 
- Mantener la experiencia que se tiene en el botón de "Aprobar manual la validación de identidad" 
- El mensaje al usuario y la experiencia de notificación deben conservar el comportamiento actualmente definido en el módulo de clientes SARLAFT. 
- Mensaje cuando pasa de rechazado a desactualizado o cancelado: La evaluación se encuentra desactualizada para que finalice la evaluación, por favor informar al usuario.     
- **Estado “DESACTUALIZADO Y ACTUALIZADO”**    
- El botón de cambiar estado no se habilita.

## Criterios de Aceptación

Exposición del botón **Cambiar estado** 
- El botón **“Cambiar estado”** debe visualizarse **únicamente** en evaluaciones con **tipo de operación Actualización**. 
- El botón **“Cambiar estado”** debe visualizarse solo para evaluaciones que se encuentren en estado **RECHAZADO** o **CANCELADO**. 
- En la grilla de resultados de evaluaciones, **solo las evaluaciones con estado RECHAZADO** deben mostrar el botón **“Cambiar estado”**. 
- Para evaluaciones en estado **DESACTUALIZADO** o **ACTUALIZADO**, el botón **“Cambiar estado”** **no debe estar habilitado**. 
- La visualización del botón **“Cambiar estado”** aplica **exclusivamente para el perfil Administrador**. 
- Para perfiles distintos al Administrador, el botón **“Cambiar estado”** **no debe mostrarse**.  Acceso y flujo de navegación 
- La funcionalidad debe ser accesible siguiendo la ruta:

- Módulo de clientes SARLAFT 
- Logueo del Administrador 
- Consultar cliente 
- Tipo de operación: Actualización 
- Buscar cliente por criterios de búsqueda 
- Visualizar resultados de evaluaciones    Experiencia del modal **Cambiar estado** 
- Al hacer clic en el botón **“Cambiar estado”**, debe desplegarse un modal. 
- El modal debe mantener la **misma experiencia visual y de textos** definida actualmente para el botón **“Aprobar manual la validación de identidad”**. 
- El modal debe mostrar el título **“Cambiar estado de la evaluación”**. 
- El modal debe mostrar el subtítulo:
**“Seleccione el nuevo estado de la evaluación, registre el análisis realizado y confirme la acción”**. 
- El modal debe contener un **selector único (radio buttons)** que permita elegir entre los estados:  
- **ACTUALIZADO** 
- **DESACTUALIZADO**  
- El modal debe incluir un campo denominado **“Detalle del análisis LA/FT”**. 
- El campo **“Detalle del análisis LA/FT”** debe ser **obligatorio**. 
- El campo **“Detalle del análisis LA/FT”** debe permitir el ingreso de:  
- Letras 
- Números 
- Caracteres especiales  
- El modal debe incluir la acción primaria **“Confirmar estado”**. 
- El modal debe incluir el mensaje de confirmación:
**“¿Está seguro de cambiar el estado de la evaluación?”**.  Lógica de cambio de estado 
- Cuando una evaluación en estado **RECHAZADO** o **CANCELADO** se cambie a **DESACTUALIZADO**, las evidencias deben comportarse de la siguiente manera:  
- **GAFI:** Mantener estado 
- **RRCC:** Mantener estado 
- **PEPS:** Mantener estado 
- **EXPERIAN:** Pasar a estado **Pendiente** 
- **Formulario:** Mantener estado  
- Al pasar la evidencia de **EXPERIAN** a **Pendiente**, debe permitir volver a realizar la validación de identidad. 
- Las funcionalidades de **reenviar** y el **botón aprobar** deben permanecer habilitadas para la validación de identidad. 
- El sistema debe registrar los **logs de la evidencia de la modificación de estados** realizada.  Mensajes y notificación al usuario 
- Al cambiar el estado de la evaluación de **Rechazado** o **Cancelado** a **Desactualizado**, se debe mostrar el siguiente mensaje al usuario:
**“La evaluación se encuentra desactualizada para que finalice la evaluación, por favor informar al usuario.”** 
- El mensaje al usuario y la experiencia de notificación deben conservar el comportamiento actualmente definido en el **Módulo de Clientes SARLAFT**.
