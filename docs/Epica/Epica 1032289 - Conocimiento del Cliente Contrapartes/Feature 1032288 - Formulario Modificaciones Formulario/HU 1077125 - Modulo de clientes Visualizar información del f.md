# HU 1077125 — [Modulo de clientes]: Visualizar información del formulario en Resumen para perfil Administrador

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1077125 — [Modulo de clientes]: Visualizar información del formulario en Resumen para perfil Administrador

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1077125](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1077125) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | sin revisar |
| **Creado** | 2026-03-16 |
| **Última modificación** | 2026-03-27 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)  
  Estado: New  

## Descripción

**Como** usuario con perfil **Administrador**
**Quiero** que se ajusten los títulos de las secciones del resumen y que se visualice la información del formulario del tomador
**Para** mejorar la claridad del flujo de consulta de evaluaciones y contar con una vista completa del conocimiento del cliente bajo criterios SARLAFT.    Alcance funcional 
La historia contempla **dos ajustes principales** en la pantalla de **RESUMEN** al consultar una evaluación desde el Módulo de Clientes SARLAFT. Requerimiento 1: Cambio de títulos de secciones 
Se requiere actualizar los títulos actuales de la siguiente manera: 
- 
El título **“Conocimiento del Cliente”** debe cambiarse por:
**“Gestión del Formulario del Cliente”**  
- 
El título **“Datos adicionales”** debe cambiarse por:
**“Información de Figuras Diferentes al Tomador”**   
Estos cambios aplican únicamente a nivel de **visualización**, sin afectar la lógica de negocio ni los controles existentes. Consideraciones de perfil 
- Esta visualización aplica **para todos los perfiles del modulo**   Requerimiento 2: Visualización de la información del formulario del tomador 
Se debe incorporar una nueva sección denominada:    **Información del Formulario del Tomador** 
Esta sección debe mostrarse en la pantalla de **RESUMEN**, **debajo de “Información de Figuras Diferentes al Tomador”**, y debe seguir los lineamientos visuales definidos para el formulario. Datos a mostrar (Se adjunta ejemplo de la experiencia) **Datos de Ubicación** 
- País: código y nombre 
- Departamento: código y nombre 
- Ciudad: código y nombre 
- Dirección: dirección reportada  **Datos Financieros** 
- Actividad económica: código y nombre 
- Ocupación: código y nombre 
- Ingresos: valor numérico separado por puntos 
- Egresos: valor numérico separado por puntos 
- Activos: valor numérico separado por puntos 
- Pasivos: valor numérico separado por puntos 
- Declaración de bienes: texto   
Reglas generales 

- La información debe mostrarse **solo en modo consulta (lectura)**. 
- Si no existe el dato entonces mostrar: Sin información. 
- En la declaración de origen de bienes mostrar todo el texto ingresado que se guardo en el formulario. 
- Para los campos que tienen código y nombre, si no se cuenta con el nombre entonces mostrar el código. Si no tiene datos mostrar "Sin información".   Consideraciones de perfil 
- Esta visualización aplica **exclusivamente para el perfil Administrador**. 
- Para los demás perfiles, la sección **no debe ser visible**.

## Criterios de Aceptación

Criterios asociados al cambio de títulos 
- En la pantalla de **RESUMEN** de una evaluación consultada desde el **Módulo de Clientes SARLAFT**, el título **“Conocimiento del Cliente”** debe visualizarse como **“Gestión del Formulario del Cliente”**. 
- En la pantalla de **RESUMEN**, el título **“Datos adicionales”** debe visualizarse como **“Información de Figuras Diferentes al Tomador”**. 
- Los cambios de títulos deben aplicarse **únicamente a nivel de visualización**, sin modificar la lógica de negocio ni los controles existentes. 
- Los títulos actualizados deben visualizarse correctamente **para todos los perfiles del módulo**.  Criterios asociados a la visualización de la información del formulario del tomador 
- En la pantalla de **RESUMEN**, se debe mostrar una sección denominada **“Información del Formulario del Tomador”**. 
- La sección **“Información del Formulario del Tomador”** debe ubicarse **debajo de la sección “Información de Figuras Diferentes al Tomador”**. 
- La sección debe seguir los **lineamientos visuales definidos para el formulario**, conforme al ejemplo de experiencia adjunto. 
- La sección debe mostrar la información correspondiente a **Datos de Ubicación**, incluyendo:

- País (código y nombre) 
- Departamento (código y nombre) 
- Ciudad (código y nombre) 
- Dirección reportada   
- La sección debe mostrar la información correspondiente a **Datos Financieros**, incluyendo:

- Actividad económica (código y nombre) 
- Ocupación (código y nombre) 
- Ingresos (valor numérico separado por puntos) 
- Egresos (valor numérico separado por puntos) 
- Activos (valor numérico separado por puntos) 
- Pasivos (valor numérico separado por puntos) 
- Declaración de bienes (texto ingresado en el formulario)   
- La información de la sección **“Información del Formulario del Tomador”** debe mostrarse **solo en modo consulta (lectura)**. 
- La visualización de la sección **“Información del Formulario del Tomador”** debe estar disponible **exclusivamente para el perfil Administrador**. 
- Para los demás perfiles, la sección **no debe ser visible** en la pantalla de RESUMEN.
