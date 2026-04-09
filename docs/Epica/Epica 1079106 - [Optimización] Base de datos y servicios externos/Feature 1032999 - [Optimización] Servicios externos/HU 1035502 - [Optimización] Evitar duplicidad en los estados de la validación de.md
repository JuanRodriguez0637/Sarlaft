# HU 1035502 — [Optimización]: Evitar duplicidad en los estados de la validación de identidad- Cuestionario

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999) › HU 1035502 — [Optimización]: Evitar duplicidad en los estados de la validación de identidad- Cuestionario

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1035502](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035502) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-05 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)  
  Estado: New  

## Descripción

Como Analista SARLAFT,
quiero que, cuando se cree una evaluación que requiera ejecutar el flujo de validación de identidad, el sistema verifique si el cliente presenta estados bloqueantes asociados al cuestionario de preguntas,
para evitar la continuidad de la evaluación cuando esta no sea viable y comunicar de manera clara al usuario el motivo del rechazo, mitigando riesgos de fraude y el uso indebido del proceso.   
 **Alcance** 
- **Tipo de operación:** negocio nuevo y reclamaciones 
- **Tipo de persona: **Natural 
- **Tipos de documentos: **cédula de ciudadanía, cédula de extranjería y permiso por protección temporal 
- **Momento de notificación:** 
- Cuando un cliente realice por primera vez el flujo de validación de identidad y, durante el diligenciamiento del cuestionario, el servicio de Experian retorne alguno de los estados bloqueantes, cualquier nueva evaluación que se cree posteriormente deberá responder de forma inmediata con estado **Rechazado**, asociándolo a dicha causal.   
- **Mecanismos para crear evaluaciones** 
- Modulo de clientes sarlaft 
- Servicio de crear evaluación que se expone a los aplicativos de negocio y la API de terceros  
- **Mecanismos para activar el flujo de validación de identidad** 
- Enlace del formulario notificado por medio del modulo de clientes Sarlaft - Crear evaluación 
- Botón de copiar y pegar el enlace en un navegador que se extrae en el modulo de clientes Sarlaft - consultar cliente - tipo de operación - negocio nuevo y reclamaciones 
- Botón para reenviar formulario cuando se consulta un cliente en el modulo de clientes sarlaft - consultar cliente - tipo de operación - reclamaciones 
- Enlace del formulario para validar identidad cuando se completa el diligenciamiento del formulario 
- Flujo integrado en el webcomponent 
- Flujo integrado en la API de terceros    **
** **Estados bloqueantes (para el cuestionario) ** 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR DÍA 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR MES 
- NO HAY SUFICIENTES PREGUNTAS 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE DÍA 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE MES  **Estados que no les aplica la regla (para el cuestionario)** 
- NO EXISTE IDENTIFICACION 
- NO FUE POSIBLE REALIZAR LA VALIDACION
 
- PREGUNTAS GENERADAS CON EXITO 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE AÑO
 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR AÑO
   
   **Reglas de negocio** 
- **R1. Alcance de documento: **Aplica exclusivamente para Cédula de Ciudadanía, cédula de extranjería y permiso por protección temporal. Otros tipos de documento siguen flujo normal.
 
- **R2. Filtro previo obligatorio:** Si el estado coincide con cualquiera de los cinco bloqueantes, no debe dar continuidad a la evaluación y se debe rechazar la evaluación por esa evidencia. Teniendo en cuenta: 
- **Mensaje en el servicio que crea la evaluación: **"No es posible continuar con el proceso. El proceso de validación de identidad no ha sido exitoso" (Definido actualmente) 
- **Mensaje en el modulo de clientes sarlaft: **"El proceso de validación de identidad no ha sido exitoso: (Detallar el estado bloqueante)"  
- **R3. Estados definitivos: **Los estados listados son bloqueantes y definitivos. Deben almacenarse y reutilizarse en toda reconsulta según las reglas de filtros previos:
 
- Cuando el estado es EXCEDIÓ EL NÚMERO DE INTENTOS POR DÍA y EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE DÍA se debe almacenar solo por 24 horas y rechazar las nuevas evaluaciones por esa causal durante ese día. 
- **Ejemplo: **El 4 de febrero del 2026 a las 2:00 pm el cliente "EXCEDIÓ EL NÚMERO DE INTENTOS POR DÍA"; si el cliente vuelve a intentar entre las 2:00 pm y las 12:00am, se debe rechazar la evaluación por esa causal. A las 12:01 AM, se permite volver a realizar el flujo de validación de identidad.  
- Cuando el estado es EXCEDIÓ EL NÚMERO DE INTENTOS POR MES, NO HAY SUFICIENTES PREGUNTAS y EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE MES se debe almacenar solo por 1 mes y rechazar las nuevas evaluaciones por esa causal durante ese mes. 
- **Ejemplo: **El 4 de febrero del 2026 a las 2:00 pm el cliente "EXCEDIÓ EL NÚMERO DE INTENTOS POR MES "; si el cliente vuelve a intentar entre las 4 al 28 de febrero del 2026, se debe rechazar la evaluación por esa causal. El día 01 de marzo del 2026, se permite volver a realizar el flujo de validación de identidad.   
- **R5. Estados sin bloqueo: **Los estados a los que no aplica la regla de bloqueo deberán conservar el estado de la evaluación asignado, sin generar cambios en su resultado. 
- **R6: Persistencia obligatoria: **La primera vez que se obtenga un estado definitivo, se debe guardar con los definidos actualmente en el diccionario del webhook. 
- **R7: Trazabilidad: **Guardar la respuesta del estado para identificar si es por primera vez o esta heredando la consulta con los datos básicos (tipo_id = CC, número_id y primer apellido), estado(Lista de estados bloqueantes) y fecha de consulta.

## Criterios de Aceptación

CA‑01. Verificación obligatoria al crear una evaluación 
**Dado** que se crea una evaluación que requiere ejecutar el flujo de validación de identidad,
**Cuando** el sistema valide si el cliente presenta estados previos asociados al **cuestionario de preguntas**,
**Entonces** el sistema deberá realizar un **filtro previo obligatorio** antes de permitir la continuidad de la evaluación. CA‑02. Alcance por tipo de persona, operación y documento 
**Dado** que la evaluación corresponde a: 
- Tipo de persona **Natural**, 
- Tipo de operación **Negocio nuevo** o **Reclamaciones**, 
- Tipo de documento **Cédula de ciudadanía**, **Cédula de extranjería** o **Permiso por Protección Temporal**,
**Cuando** se cree la evaluación,
**Entonces** deberán aplicarse las reglas de bloqueo por estados del cuestionario.  CA‑03. Exclusión por tipo de documento 
**Dado** que la evaluación se crea con un tipo de documento **diferente** a los definidos en el alcance,
**Cuando** se realice la validación previa,
**Entonces** el sistema deberá **continuar el flujo normal**, sin aplicar reglas de bloqueo por cuestionario. CA‑04. Bloqueo inmediato por estados bloqueantes 
**Dado** que el cliente, en una ejecución previa del flujo de validación de identidad, obtuvo alguno de los siguientes **estados bloqueantes** del cuestionario: 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR DÍA 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR MES 
- NO HAY SUFICIENTES PREGUNTAS 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE DÍA 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE MES  
**Cuando** se cree una nueva evaluación posteriormente,
**Entonces** el sistema deberá: 
- Responder **de forma inmediata** con estado **Rechazado**. 
- **No permitir** la continuidad de la evaluación ni el inicio del flujo de validación de identidad. 
- Asociar el rechazo a la **causal específica** del estado bloqueante.  CA‑05. Mensajes de rechazo según canal 
**Dado** que una evaluación es rechazada por un estado bloqueante del cuestionario,
**Cuando** el rechazo se origine desde: 
- **Servicio de creación de evaluación**,
**Entonces** el mensaje deberá ser:  
*“No es posible continuar con el proceso. El proceso de validación de identidad no ha sido exitoso.”* 
**Y cuando** el rechazo se visualice en el **Módulo de Clientes SARLAFT**,
**Entonces** el mensaje deberá ser: 
*“El proceso de validación de identidad no ha sido exitoso: (estado bloqueante)”* CA‑06. Persistencia temporal – Bloqueo diario 
**Dado** que el estado bloqueante obtenido es: 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR DÍA, o 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE DÍA,  
**Cuando** el estado sea registrado por primera vez,
**Entonces** el sistema deberá: 
- Almacenar el estado por un período de **24 horas**. 
- Rechazar automáticamente cualquier nueva evaluación creada durante ese mismo día por la misma causal.  
**Y** una vez superado el período (inicio del día siguiente),
**Entonces** se deberá permitir nuevamente la ejecución del flujo de validación de identidad. CA‑07. Persistencia temporal – Bloqueo mensual 
**Dado** que el estado bloqueante obtenido es: 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR MES, 
- NO HAY SUFICIENTES PREGUNTAS, o 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE MES,  
**Cuando** el estado sea registrado por primera vez,
**Entonces** el sistema deberá: 
- Almacenar el estado por un período de **un (1) mes calendario**. 
- Rechazar cualquier nueva evaluación creada dentro de ese mes por la misma causal.  
**Y** al iniciar el mes siguiente,
**Entonces** se deberá permitir nuevamente la creación de evaluaciones y la ejecución del flujo. CA‑08. Estados que no generan bloqueo 
**Dado** que el estado del cuestionario es alguno de los siguientes: 
- NO EXISTE IDENTIFICACION 
- NO FUE POSIBLE REALIZAR LA VALIDACION 
- PREGUNTAS GENERADAS CON EXITO 
- EXCEDIÓ EL NÚMERO DE INGRESOS PERMITIDOS PARA EL PRODUCTO POR ESTE AÑO 
- EXCEDIÓ EL NÚMERO DE INTENTOS POR AÑO  
**Cuando** se cree la evaluación,
**Entonces** el sistema **no deberá aplicar la regla de bloqueo**
**Y** deberá **conservar el estado de la evaluación asignado**, permitiendo la continuidad normal del proceso. CA‑09. Reutilización del estado bloqueante (herencia) 
**Dado** que un cliente ya tiene almacenado un estado bloqueante definitivo vigente,
**Cuando** se cree una nueva evaluación (por cualquier mecanismo habilitado),
**Entonces** el sistema deberá: 
- Reutilizar el estado previamente almacenado. 
- No reejecutar el cuestionario. 
- Rechazar la evaluación de forma inmediata por dicha causal.  CA‑10. Persistencia obligatoria del primer estado definitivo 
**Dado** que es la **primera vez** que se obtiene un estado bloqueante definitivo para un cliente,
**Cuando** se reciba la respuesta del servicio,
**Entonces** el sistema deberá: 
- Guardar el estado conforme al **diccionario del webhook** definido actualmente. 
- Marcarlo como referencia para futuras evaluaciones.  CA‑11. Trazabilidad obligatoria del estado 
**Dado** que se registre un estado bloqueante del cuestionario,
**Cuando** se almacene la información,
**Entonces** se deberá guardar como mínimo: 
- Tipo de documento 
- Número de documento 
- Primer apellido 
- Estado bloqueante 
- Fecha y hora de la consulta 
- Indicador de si es **primera ocurrencia** o **estado heredado**  CA‑12. Independencia del mecanismo de activación 
**Dado** que la evaluación o el flujo de validación de identidad se active desde: 
- Módulo de clientes SARLAFT 
- Servicio de creación de evaluación (aplicativos de negocio / API terceros) 
- Enlace de formulario 
- WebComponent 
- API de terceros  
**Cuando** se valide el estado previo del cuestionario,
**Entonces** las reglas de bloqueo deberán aplicarse **de forma uniforme**, sin depender del canal de origen.
