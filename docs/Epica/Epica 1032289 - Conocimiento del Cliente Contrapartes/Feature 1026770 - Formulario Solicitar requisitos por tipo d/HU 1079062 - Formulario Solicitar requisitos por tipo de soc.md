# HU 1079062 — [Formulario]: Solicitar requisitos por tipo de sociedad - Reintentos

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1026770 — [Formulario]: Solicitar requisitos por tipo de sociedad](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026770) › HU 1079062 — [Formulario]: Solicitar requisitos por tipo de sociedad - Reintentos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1079062](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079062) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-17 |
| **Última modificación** | 2026-03-17 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1026770 — [Formulario]: Solicitar requisitos por tipo de sociedad](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026770)  
  Estado: New  

## Descripción

Yo como analista sarlaft 
Quiero: 
 
- No tenemos relanzamiento de documentos a P8 
- El log de reintentos estaría en la tabla sarlaft.tsaf_notificacion. 
- En la tabla de sarlaft.tsaf_notificacion adicionar una columna Reintento, donde se pueda poner el valor de PROGRAMADO 
- Crear un proceso en sarlaftbatch que corra en la noche, que tome las notificación de tipo P8 en estado ERROR del dia en curso o en estado PROGRAMADO. 
- Al momento de lanzar el comando a sarlaftp8 cambie el estado de Reintento a FINALIZADO. 
- Las relance, lanzando el comando escuchado por sarlaftp8. Ajustar para que tenga un máximo de 3 reintentos automáticos por petición. 
- Implementar un circuit breaker en caso de que la información no pueda ser cargada en P8, se debe registrar un log en Splunk, bajo el módulo sarlaftp8, indicando que la operación quedó en proceso de reintentos. Este mecanismo no debería quedarse realizando reintentos constantes contra P8. Para esto se debe configurar un tiempo de espera y un número de reintentos prudentes, permitiendo verificar posteriormente si el servicio se restablece y así cerrar el circuito de manera controlada.

## Criterios de Aceptación

- No tenemos relanzamiento de documentos a P8 
- El log de reintentos estaría en la tabla sarlaft.tsaf_notificacion. 
- En la tabla de sarlaft.tsaf_notificacion adicionar una columna Reintento, donde se pueda poner el valor de PROGRAMADO 
- Crear un proceso en sarlaftbatch que corra en la noche, que tome las notificación de tipo P8 en estado ERROR del dia en curso o en estado PROGRAMADO. 
- Al momento de lanzar el comando a sarlaftp8 cambie el estado de Reintento a FINALIZADO. 
- Las relance, lanzando el comando escuchado por sarlaftp8. Ajustar para que tenga un máximo de 3 reintentos automáticos por petición. 
- Implementar un circuit breaker en caso de que la información no pueda ser cargada en P8, se debe registrar un log en Splunk, bajo el módulo sarlaftp8, indicando que la operación quedó en proceso de reintentos. Este mecanismo no debería quedarse realizando reintentos constantes contra P8. Para esto se debe configurar un tiempo de espera y un número de reintentos prudentes, permitiendo verificar posteriormente si el servicio se restablece y así cerrar el circuito de manera controlada.
