# HU 1083734 — [Proceso de actualización]: Retirar opción de cancelar evaluaciones de cancelación en el Modulo de Clientes

[Épica 1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001) › [Feature 1082324 — [Proceso de actualización]: Modificaciones al Modulo de Clientes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082324) › HU 1083734 — [Proceso de actualización]: Retirar opción de cancelar evaluaciones de cancelación en el Modulo de Clientes

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1083734](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1083734) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | sin revisar |
| **Creado** | 2026-03-20 |
| **Última modificación** | 2026-03-27 |

## Jerarquía

- **Épica:** [1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001)  
  Estado: New  
- **Feature:** [1082324 — [Proceso de actualización]: Modificaciones al Modulo de Clientes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082324)  
  Estado: New  

## Descripción

**Como** usuario del **Módulo de Clientes SARLAFT**
**Quiero** que la opción **“Cancelar”** no esté disponible para los perfiles diferentes al **Administrador** en las evaluaciones de **tipo de operación Actualización**
**Para** asegurar que solo el perfil autorizado pueda realizar la cancelación de este tipo de evaluaciones. 
 
La historia aplica a las evaluaciones con **tipo de operación Actualización**, consultadas desde el **Módulo de Clientes SARLAFT**. Ruta funcional 
- Módulo de Clientes SARLAFT 
- Consultar clientes 
- Seleccionar **Tipo de operación: Actualización** 
- Visualizar el listado de evaluaciones en pantalla  Comportamiento esperado 
- En la pantalla donde se visualizan las evaluaciones de **tipo de operación Actualización**, la opción **“Cancelar”** **no debe mostrarse** para los perfiles diferentes al Administrador. 
- El botón **“Cancelar”** debe estar visible **únicamente para el perfil Administrador**. 
- La restricción de visibilidad del botón aplica solo a evaluaciones de **Actualización** y no modifica otros procesos.  Consideraciones de perfil 
- Solo el **perfil Administrador** puede visualizar y utilizar la opción **“Cancelar”** evaluaciones de Actualización. 
- Para los demás perfiles, la opción **no debe aparecer** en la pantalla de resultados de evaluaciones.

## Criterios de Aceptación

- La funcionalidad debe aplicar únicamente a evaluaciones con **tipo de operación Actualización**. 
- La funcionalidad debe estar disponible desde el **Módulo de Clientes SARLAFT**, siguiendo la ruta:

- Consultar clientes 
- Seleccionar tipo de operación **Actualización** 
- Visualizar el listado de evaluaciones   
- En la pantalla donde se muestran las evaluaciones de **tipo de operación Actualización**, la opción **“Cancelar”** **no debe visualizarse** para los perfiles diferentes al **Administrador**. 
- El botón **“Cancelar”** debe visualizarse **únicamente para el perfil Administrador**. 
- Para los perfiles distintos al Administrador, la opción **“Cancelar”** no debe aparecer en el listado de evaluaciones. 
- La restricción de visibilidad del botón **“Cancelar”** aplica únicamente para evaluaciones del proceso de **Actualización**. 
- El cambio corresponde únicamente a la **visibilidad de la opción “Cancelar”**, sin modificar otros comportamientos del proceso.
