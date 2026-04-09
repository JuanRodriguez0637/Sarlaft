# HU 1032311 — [Formulario]: Adicionar clausula de tratamiento de datos

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1032311 — [Formulario]: Adicionar clausula de tratamiento de datos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1032311](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032311) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-03 |
| **Última modificación** | 2026-02-13 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)  
  Estado: New  

## Descripción

Como PO del sistema de Clientes y SARLAFT,
quiero que todos los formularios de operación de negocio, Reclamaciones y actualización incluyan obligatoriamente la cláusula de tratamiento de datos personales,
para garantizar el cumplimiento normativo, la trazabilidad de la autorización del cliente, la obligatoriedad de su aceptación y la sincronización consistente del estado de la cláusula entre el Modelo de Clientes y el módulo SARLAFT.  
  ****  ****   **1. Inclusión obligatoria de la cláusula** 
- La cláusula de tratamiento de datos personales deberá mostrarse de manera obligatoria y permanente en los siguientes formularios: 
- Formularios de operación de negocio nuevo. 
- Formularios de reclamaciones. 
- Formularios de actualización.  
- La cláusula debe visualizarse en la pantalla inmediatamente posterior a “Conocerte es muy importante para nosotros”. 
- Su visualización será obligatoria sin excepciones, independientemente de: 
- El tipo de persona: Natural o Jurídica. 
- El tipo de riesgo: Ordinario, Intensificado o Simplificado.    **2. Campo obligatorio de aceptación** 
- El usuario deberá obligatoriamente seleccionar una opción (Sí o No) para poder: 
- Avanzar de pantalla. 
- Guardar la información. 
- Finalizar el formulario.  
- En todos los formularios se deberá incluir un campo tipo radio button, con las opciones: 
- Sí, autorizo 
- No autorizo  
- El texto de la cláusula deberá ser parametrizable, permitiendo su ajuste sin afectación del código.   **3. Registro y envío de la aceptación** 
- Una vez el cliente seleccione una opción, el sistema deberá: 
- Capturar la respuesta (Sí/No) dentro del formulario. 
- Enviar la respuesta al servicio del Modelo de Clientes durante el día.  
- En caso de que el servicio no confirme la recepción exitosa, el sistema deberá:

- Registrar un log detallado, que permita identificar:

- Respuestas no procesadas. 
- Errores técnicos presentados durante el envío. 
- El sistema deberá realizar un único intento de envío masivo diario,

- Este punto deberá validarse con el equipo del Modelo de Clientes o según las políticas definidas para la transmisión de información.    
- Se debe garantizar que la autorización del cliente quede almacenada, incluso cuando el envío deba ser reprocesado posteriormente.   **4. Restricciones sobre información histórica** 
- La aceptación de la cláusula se registrará únicamente a partir de la fecha de entrada en producción de esta funcionalidad. 
- No se contempla ningún proceso de carga, reconstrucción o migración histórica de aceptaciones previas.

## Criterios de Aceptación

1. Inclusión obligatoria de la cláusula en formularios
 CA1 – Visualización obligatoria
Dado que el usuario ingresa a un formulario de operación de negocio, reclamaciones o actualización
Cuando llegue a la pantalla posterior a “Conocerte es muy importante para nosotros”
Entonces el sistema debe mostrar la cláusula de tratamiento de datos personales sin excepción.
CA2 – Independencia del tipo de persona
Dado un cliente Natural o Jurídico
Cuando se despliegue el formulario
Entonces la cláusula debe visualizarse de forma obligatoria.
CA3 – Independencia del tipo de riesgo
Dado un cliente con riesgo Ordinario, Intensificado o Simplificado
Cuando navegue la pantalla correspondiente
Entonces la cláusula deberá mostrarse siempre, sin importar el nivel de riesgo.
CA4 – Texto parametrizable
Dado que el texto de la cláusula puede actualizarse por políticas normativas
Cuando se requiera un ajuste en el texto
Entonces este deberá poder modificarse mediante parametrización, sin modificar código.
2. Campo obligatorio de aceptación
CA5 – Selección obligatoria
Dado que el usuario está en la pantalla donde se muestra la cláusula
Cuando intente avanzar, guardar o finalizar el formulario
Entonces el sistema debe exigir obligatoriamente seleccionar una opción:
- “Sí, autorizo”, o  
- “No autorizo”.  CA6 – Control de validación
Dado que el usuario no ha seleccionado ninguna opción
Cuando intente continuar
Entonces el sistema debe bloquear la acción y mostrar un mensaje de validación indicando que debe seleccionar “Sí” o “No”.
CA7 – Componente visual obligatorio
Dado que el formulario está cargado
Cuando se muestre la cláusula
Entonces deberán visualizarse los radio buttons “Sí, autorizo” y “No autorizo”.
3. Registro y envío de la aceptación
CA8 – Captura de la selección
Dado que el usuario selecciona una opción
Cuando se registre el formulario
Entonces el sistema debe capturar la respuesta (Sí/No) de manera inmediata.
CA9 – Envío al servicio del Modelo de Clientes
Dado que existe un servicio para almacenar el estado de aceptación
Cuando el usuario seleccione una opción
Entonces el sistema debe enviar la respuesta al servicio durante el día, siguiendo la política definida.
CA10 – Manejo de errores del servicio
Dado que el servicio del Modelo de Clientes no confirma recepción exitosa
Cuando se intente enviar la respuesta
Entonces el sistema debe generar un log con:
- Identificador del cliente  
- Fecha y hora  
- Respuesta enviada  
- Error recibido del servicio  
- Estado del registro pendiente  CA11 – Intento de envío masivo diario
Dado que el servicio no recibió algunas respuestas durante el día
Cuando se ejecute el proceso masivo diario
Entonces el sistema debe intentar enviar nuevamente la información
Y solo deberá realizar un intento diario, salvo que el Modelo de Clientes defina otra política.
CA12 – Garantía de almacenamiento
Dado que se está registrando la aceptación del cliente
Cuando se presente un fallo temporal en el envío al servicio
Entonces el sistema debe garantizar que la autorización quede almacenada localmente para reprocesarla posteriormente.
4. Restricciones sobre información histórica
CA13 – Registro solo a partir de entrada en producción
Dado que la funcionalidad entra en producción
Cuando un cliente interactúe con un formulario
Entonces únicamente se registrarán aceptaciones a partir de esa fecha en adelante.
CA14 – No migración de datos históricos
Dado que el sistema debe mantener consistencia
Cuando se ejecute la funcionalidad
Entonces no deberá cargarse ni reconstruirse ninguna marca histórica previa del cliente.
