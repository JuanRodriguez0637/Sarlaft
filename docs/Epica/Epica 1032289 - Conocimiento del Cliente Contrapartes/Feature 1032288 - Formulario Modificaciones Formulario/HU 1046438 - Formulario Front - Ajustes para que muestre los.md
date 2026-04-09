# HU 1046438 — [Formulario]: Front - Ajustes para que muestre los requisitos

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1046438 — [Formulario]: Front - Ajustes para que muestre los requisitos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1046438](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046438) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-16 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)  
  Estado: New  

## Descripción

Como Analista/PO del sistema de Clientes y SARLAFT,
quiero que el frontend del formulario de evaluación consulte y muestre los documentos requeridos definidos en el campo “soportesRequeridos”,
para garantizar que al usuario se le soliciten únicamente los documentos correctos, según las reglas del motor y los requisitos aplicables a cada evaluación.

## Criterios de Aceptación

CA1 – Lectura del campo “soportesRequeridos” Dado que el usuario abre o consulta el formulario de evaluación,
 Cuando el frontend consuma el servicio que retorna la información de la evaluación,
 Entonces el sistema debe leer el campo “soportesRequeridos” incluido en la respuesta. 
 CA2 – Mostrar varios documentos requeridos Dado que el servicio retorna uno o más documentos dentro de “soportesRequeridos”,
 Cuando el frontend procese esta información,
 Entonces debe mostrar en pantalla los controles de carga únicamente para los documentos listados en “soportesRequeridos”. 
 CA3 – No visualizar documentos no requeridos Dado que existan documentos definidos en otras reglas o requisitos,
 Cuando estos documentos no estén incluidos en el listado de “soportesRequeridos”,
 Entonces el frontend no deberá mostrarlos ni solicitar su carga. 
 CA4 – Mostrar atributos del documento Dado un documento incluido en “soportesRequeridos”,
 Cuando se renderice en pantalla,
 Entonces deben mostrarse sus atributos básicos: Nombre o tipo del soporte Indicador del estado: pendiente 
 CA5 – Validación de obligatoriedad Dado que un documento en “soportesRequeridos” está marcado como obligatorio,
 Cuando el usuario intente avanzar, guardar o finalizar el formulario,
 Entonces el sistema debe impedir la acción y mostrar un mensaje de validación si el documento no ha sido cargado. 
 CA6 – Actualización dinámica ante cambios en la evaluación Dado que el usuario modifique información que cambia las reglas de requisitos,
 Cuando el backend retorne un nuevo “soportesRequeridos”,
 Entonces el frontend debe actualizar en tiempo real: Los documentos solicitados, Sus estados, 
 CA7 – Manejo de errores Dado que el servicio falle, devuelva errores o no incluya “soportesRequeridos”,
 Cuando el front reciba la respuesta,
 Entonces debe mostrar un mensaje de error controlado y evitar dejar la pantalla en blanco o inconsistente.
