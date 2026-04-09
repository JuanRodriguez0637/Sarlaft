# HU 1046535 — [Formulario]: Relanzamiento de documentos a P8

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1046535 — [Formulario]: Relanzamiento de documentos a P8

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1046535](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046535) |
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

**** Como Analista/PO del sistema de Clientes y SARLAFT,
 quiero implementar un mecanismo automático de reintentos para las notificaciones de tipo P8 que presenten errores,
 para asegurar que los documentos sean reenviados de manera controlada, evitar reprocesos manuales, minimizar fallas operativas y garantizar estabilidad mediante un esquema de circuit breaker.  
 **Descripción Funcional** **1. Ajustes en tabla sarlaft.tsaf_notificacion** El sistema debe: Registrar en sarlaft.tsaf_notificacion todas las notificaciones de documentos enviadas a P8. Adicionar una nueva columna:
Reintento (valores posibles: PROGRAMADO, FINALIZADO, N/A). Usar esta columna para identificar las notificaciones que deben ser reprocesadas por el mecanismo nocturno. 
 **2. Lógica del proceso automático (batch nocturno)** Se debe crear un proceso en sarlaftbatch que: Se ejecute cada noche. Identifique notificaciones de tipo P8 cuyo estado sea:

- ERROR del día en curso, o 
- PROGRAMADO (marcadas para reintento). 
- Para cada registro encontrado:

- Cambiar el valor del campo Reintento a FINALIZADO (solo al iniciar el proceso de relanzamiento). 
- Relanzar la notificación ejecutando el comando consumido por sarlaftp8. 
- El proceso debe permitir como máximo 3 reintentos automáticos por cada notificación.   
 **3. Circuit Breaker** Implementar un circuit breaker para evitar reintentos infinitos y proteger el sistema cuando P8 esté caído. El mecanismo debe: 
- Activarse cuando se detecten fallas consecutivas por indisponibilidad de P8.   Registrar un log en Splunk, bajo el módulo sarlaftp8, incluyendo:

- Identificador de la notificación 
- Tipo de documento 
- Número de reintentos acumulados 
- Fecha/hora del bloqueo 
- Mensaje indicando “Operación quedó en proceso de reintentos – circuit breaker activo” 
- Mantener un tiempo de espera y número máximo de reintentos prudente y parametrizable. 
- Evitar que el sistema siga lanzando reintentos constantes durante la indisponibilidad del servicio. 
- Permitir que el circuito se restablezca cuando P8 vuelva a estar disponible.   
 **4. Alcances y restricciones** No existe relanzamiento manual de documentos hacia P8; todo reintento será automático vía batch. El comando relanzado debe ser el mismo actualmente escuchado por sarlaftp8 (no se crea un comando nuevo). El proceso debe dejar trazabilidad de:

- Peticiones reintentadas 
- Peticiones exitosas 
- Peticiones que superaron los 3 intentos 
- Estado del circuito (abierto/cerrado)

## Criterios de Aceptación

1. Ajustes en la tabla sarlaft.tsaf_notificacion
CA1 – Nueva columna Reintento
Dado que existe la tabla sarlaft.tsaf_notificacion,
Cuando se aplique la actualización del modelo,
Entonces la tabla debe incluir la columna Reintento, con valores permitidos: PROGRAMADO, FINALIZADO, N/A.
CA2 – Registro de notificaciones
Dado que el sistema envía una notificación de documento hacia P8,
Cuando se genere el registro en sarlaft.tsaf_notificacion,
Entonces se debe almacenar:
- tipo de notificación  
- estado  
- fecha  
- trazabilidad  
- valor por defecto “N/A” en la columna Reintento, salvo que el proceso marque reintentos.  CA3 – Identificación de solicitudes para reproceso
Dado que una notificación presenta estado ERROR,
Cuando sea del día en curso o el valor de Reintento sea PROGRAMADO,
Entonces la notificación debe ser elegible para reproceso por el batch nocturno.
2. Proceso automático nocturno (sarlaftbatch)
CA4 – Ejecución del proceso
Dado que se requiere relanzar notificaciones fallidas,
Cuando el proceso automático nocturno (sarlaftbatch) se ejecute,
Entonces debe leer únicamente las notificaciones:
- en estado ERROR del día en curso  
- o con Reintento = PROGRAMADO.  CA5 – Marcar reintento como FINALIZADO
Dado que el batch está por relanzar una notificación,
Cuando inicie el reproceso de esa notificación,
Entonces debe actualizar la columna Reintento → FINALIZADO.
CA6 – Relanzamiento del comando
Dado que una notificación cumple condiciones para reproceso,
Cuando el batch ejecute el reproceso,
Entonces debe lanzar el comando actual consumido por sarlaftp8, sin crear comandos nuevos.
CA7 – Límite de reintentos
Dado que cada notificación puede fallar múltiples veces,
Cuando el proceso nocturno intente reenviarla,
Entonces el sistema debe permitir máximo 3 reintentos automáticos por notificación
y después de superar ese número, la notificación no debe volver a ser relanzada automáticamente.
CA8 – Registro de trazabilidad
Dado que una notificación es relanzada, exitosa o falla definitivamente,
Cuando el batch procese el registro,
Entonces se debe guardar trazabilidad indicando:
- fecha/hora del reintento  
- estado final  
- cantidad de intentos acumulados  
- si se ejecutó o no el circuito  3. Circuit Breaker
CA9 – Activación del circuito
Dado que el sistema intenta reenviar notificaciones,
Cuando se detecten fallas consecutivas atribuibles a indisponibilidad de P8,
Entonces debe activarse el circuit breaker.
CA10 – Registro del evento en Splunk
Dado que el circuit breaker es activado,
Cuando se registre la indisponibilidad,
Entonces debe enviarse un log a Splunk, módulo sarlaftp8, que contenga:
- identificador de la notificación  
- tipo de documento  
- número de reintentos acumulados  
- fecha/hora  
- mensaje: “Operación quedó en proceso de reintentos – circuit breaker activo”  CA11 – Suspensión temporal de reintentos
Dado que el circuit breaker está activo,
Cuando el batch nocturno intente procesar nuevas notificaciones fallidas,
Entonces no debe ejecutar reintentos mientras el circuito esté abierto.
CA12 – Reinicio controlado
Dado que el circuito está abierto,
Cuando P8 restablezca su disponibilidad,
Entonces el sistema debe permitir que el circuito se cierre
y reactivar la lógica de reintentos de manera controlada.
4. Restricciones y Comportamiento Operativo
CA13 – No existe relanzamiento manual
Dado que un usuario operativo consulte notificaciones con error,
Cuando intente realizar un relanzamiento,
Entonces la interfaz debe indicar que el proceso es 100% automático y no admite ejecución manual.
CA14 – Uso del mismo comando
Dado que debe relanzarse una notificación,
Cuando se envíe el reproceso,
Entonces el sistema debe usar el mismo comando ya existente consumido por sarlaftp8, sin crear nuevos endpoints o colas.
CA15 – Estado final de gestión
Dado que una notificación complete sus 3 reintentos sin éxito,
Cuando el proceso nocturno finalice,
Entonces la notificación debe quedar marcada con un estado final que indique:
- superó número máximo de reintentos,  
- y debe quedar disponible para análisis manual técnico/operativo.
