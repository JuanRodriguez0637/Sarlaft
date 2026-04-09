# HU 1077124 — [Proceso de actualización]: Habilitar funcionalidad para levantar manual la validación de identidad

[Épica 1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001) › [Feature 1082324 — [Proceso de actualización]: Modificaciones al Modulo de Clientes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082324) › HU 1077124 — [Proceso de actualización]: Habilitar funcionalidad para levantar manual la validación de identidad

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1077124](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077124) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | sin revisar |
| **Creado** | 2026-03-16 |
| **Última modificación** | 2026-03-27 |

## Jerarquía

- **Épica:** [1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001)  
  Estado: New  
- **Feature:** [1082324 — [Proceso de actualización]: Modificaciones al Modulo de Clientes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082324)  
  Estado: New  

## Descripción

**Como** usuario con rol **Administrador**
**Quiero** contar con un botón **“Aprobar”** en la pantalla de **Validación de Identidad** para evaluaciones de actualización con estado **Desactualizado**
**Para** permitir que la evidencia de validación de identidad pase de estado **Pendiente** a **Finalizado**, cuando aplique. 
 Alcance funcional 
La funcionalidad aplica para las evaluaciones con **tipo de operación Actualización** y **estado Desactualizado**, consultadas desde el **Módulo de Clientes SARLAFT**.  Ruta funcional 
- Módulo de Clientes SARLAFT 
- Consultar cliente 
- Seleccionar **Tipo de operación: Actualización** 
- Buscar al cliente cuyo estado se encuentre **Desactualizado** 
- Ingresar a la evaluación mediante la opción **Gestionar** 
- Acceder a la pantalla de **Validación de Identidad**  Comportamiento esperado 
- En la pantalla de **Validación de Identidad**, se debe visualizar el botón **“Aprobar”** para aquellas **figuras** a las que aplique la validación de identidad. 
- El botón **“Aprobar”** debe estar **habilitado únicamente para el rol Administrador**. 
- La interacción del botón debe permitir que la evidencia de validación de identidad cambie de estado **Pendiente** a **Finalizado**. 
- El botón debe contar con la **misma experiencia visual y funcional** que actualmente tiene el proceso de aprobación para **Negocio Nuevo** y **Reclamaciones**, conforme a la experiencia mostrada en la imagen adjunta. 
- Al accionar el botón **“Aprobar”**, debe desplegarse el modal de **Autorización del control Proceso de validación de identidad**, solicitando el argumento correspondiente, tal como funciona actualmente para los otros procesos.  Consideraciones de perfil 
- La visualización y habilitación del botón **“Aprobar”** aplica **exclusivamente para el rol Administrador**. 
- Para los demás roles, el botón **no debe mostrarse** en la pantalla de Validación de Identidad.

## Criterios de Aceptación

- La funcionalidad debe aplicar únicamente para evaluaciones con **tipo de operación Actualización** y **estado Desactualizado**. 
- La funcionalidad debe ser accesible desde el **Módulo de Clientes SARLAFT**, siguiendo la ruta definida:

- Consultar cliente 
- Seleccionar tipo de operación **Actualización** 
- Buscar al cliente con estado **Desactualizado** 
- Ingresar a la evaluación mediante la opción **Gestionar** 
- Acceder a la pantalla de **Validación de Identidad**   
- En la pantalla de **Validación de Identidad**, se debe visualizar el botón **“Aprobar”** para aquellas figuras a las que aplique la validación de identidad. 
- El botón **“Aprobar”** debe estar habilitado **exclusivamente para el rol Administrador**. 
- Para los demás roles, el botón **“Aprobar”** no debe mostrarse en la pantalla de Validación de Identidad. 
- Al accionar el botón **“Aprobar”**, la evidencia de validación de identidad debe cambiar de estado **Pendiente** a **Finalizado**. 
- El botón **“Aprobar”** debe contar con la **misma experiencia visual y funcional** que el proceso de aprobación actualmente implementado para **Negocio Nuevo** y **Reclamaciones**, conforme a la experiencia mostrada en la imagen adjunta. 
- Al seleccionar el botón **“Aprobar”**, debe desplegarse el **modal de Autorización del control Proceso de validación de identidad**, solicitando el argumento correspondiente, tal como funciona actualmente para los otros procesos.
