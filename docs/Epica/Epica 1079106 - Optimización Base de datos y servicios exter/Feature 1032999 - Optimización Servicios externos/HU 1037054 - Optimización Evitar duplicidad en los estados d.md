# HU 1037054 — [Optimización]: Evitar duplicidad en los estados de la consulta con Migración Colombia

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999) › HU 1037054 — [Optimización]: Evitar duplicidad en los estados de la consulta con Migración Colombia

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1037054](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037054) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-06 |
| **Última modificación** | 2026-02-16 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)  
  Estado: New  

## Descripción

Como Analista SARLAFT, quiero que, cuando se cree una evaluación que requiera ejecutar la consulta del estado del documento con Migración Colombia, el sistema verifique si el cliente presenta estados bloqueantes asociados al estado que devuelve Experian, para evitar la continuidad de la evaluación cuando esta no sea viable y comunicar de manera clara al usuario el motivo del rechazo, mitigando riesgos de fraude y costos dobles por consulta.  **** **Alcance** 
- **Tipo de operación:** negocio nuevo y reclamaciones 
- **Tipo de persona: **Natural 
- **Tipos de documentos: **cédula de extranjería y permiso por protección temporal 
- **Momento de notificación:** 
- Cuando se cree por primera vez una evaluación y la consulta del estado del documento retorne alguno de los estados bloqueantes, cualquier evaluación que se cree posteriormente deberá responder de forma inmediata con estado *Rechazado*, asociándolo a dicha causal.    
- **Mecanismos para crear evaluaciones** 
- Modulo de clientes sarlaft 
- Servicio de crear evaluación que se expone a los aplicativos de negocio y la API de terceros  
- **Trazabilidad**  
- Datos mínimos para guardar el registro definitivo: *tipo_id*, *número_id*, *primer_apellido*, *estado*, *fecha_consulta_inicial*    
 
**Estados definitivos (bloqueantes)** 
- Inactivo 
- Cancelado 
- El número de identificación enviado no existe
  **Estados que no les aplica la regla**** 
- Vigente 
- Numero de documento errado 
- Tipo de documento errado
    Reglas de negocio ** 
- **R1. Alcance de documento: **Aplica exclusivamente para cédula de extranjería y permiso por protección temporal. Otros tipos de documento siguen flujo normal. 
- **R2. Filtro previo obligatorio:** Si el estado coincide con cualquiera de los cinco bloqueantes, no debe dar continuidad a la evaluación y se debe rechazar la evaluación por esa evidencia. Teniendo en cuenta: 
- **Mensaje en el servicio que crea la evaluación: **"No es posible continuar con el proceso. La validación del documento de identidad con Registraduría Nacional (cédula de ciudadanía) o Migración Colombia ( C. Extranjería, Permiso Especial de Permanencia o Permiso por Protección Temporal)no ha sido exitosa" (Definido actualmente) 
- **Mensaje en el modulo de clientes sarlaft: ** 
- Para el tomador: En la causal registraduria, mostrar el estado bloqueante (definición actual) 
- Para las figuras distintas al tomador: "La consulta del estado del documento con Migración Colombia no ha sido exitosa: (Detallar el estado bloqueante)"   
- **R3. Estados definitivos: **Los tres estados listados son bloqueantes y definitivos. Deben almacenarse y reutilizarse en toda reconsulta según las reglas de filtros previos:** 
- Cuando el estado es "inactivo", "cancelado" y "El número de identificación enviado no existe" se debe almacenar solo por 1 mes y rechazar las nuevas evaluaciones por esa causal durante ese mes. 
- Ejemplo: **El 4 de febrero del 2026 a las 2:00 pm el estado del documento del cliente es "CANCELADO"; si el cliente vuelve a intentar entre el 4 al 28 de febrero del 2026, se debe rechazar la evaluación por esa causal. El día 01 de marzo del 2026, se permite volver a realizar la consulta del estado del documento si se crea una evaluación.   
- **R5. Estados sin bloqueo: **Los estados a los que no aplica la regla de bloqueo deberán conservar el estado de la evaluación asignado, sin generar cambios en su resultado. 
- **R6: Persistencia obligatoria: **La primera vez que se obtenga un estado definitivo, se debe guardar con los definidos actualmente en el diccionario del webhook. 
- **R6: Trazabilidad: **Guardar la respuesta del estado para identificar si es por primera vez o esta heredando la consulta con los datos básicos (tipo_id = E o TT, número_id y primer apellido), estado(Lista de estados bloqueantes) y fecha de consulta.

## Criterios de Aceptación

CA‑01. Verificación obligatoria al crear una evaluación 
**Dado** que se crea una evaluación que requiere ejecutar la **consulta del estado del documento con Migración Colombia** a través de Experian,
**Cuando** el sistema valide la información del cliente,
**Entonces** deberá verificar previamente si el cliente presenta **estados definitivos bloqueantes** asociados a consultas anteriores, antes de permitir la continuidad de la evaluación. CA‑02. Alcance por tipo de persona, operación y documento 
**Dado** que la evaluación corresponde a: 
- Tipo de persona **Natural** 
- Tipo de operación **Negocio nuevo** o **Reclamaciones** 
- Tipo de documento **Cédula de extranjería** o **Permiso por Protección Temporal**  
**Cuando** se cree la evaluación,
**Entonces** deberán aplicarse las reglas de bloqueo por estado del documento definidas para Migración Colombia. CA‑03. Exclusión por tipo de documento 
**Dado** que la evaluación se crea con un tipo de documento **distinto** a cédula de extranjería o permiso por protección temporal,
**Cuando** se realice la validación previa,
**Entonces** el sistema deberá **continuar el flujo normal de la evaluación**, sin aplicar reglas de bloqueo por estados de Migración Colombia. CA‑04. Bloqueo inmediato por estados definitivos 
**Dado** que, en una consulta previa del estado del documento con Migración Colombia, el cliente obtuvo alguno de los siguientes **estados definitivos bloqueantes**: 
- **Inactivo** 
- **Cancelado** 
- **El número de identificación enviado no existe**  
**Cuando** se cree una nueva evaluación posteriormente,
**Entonces** el sistema deberá: 
- Responder **de forma inmediata** con estado **Rechazado**. 
- **No ejecutar nuevamente** la consulta a Migración Colombia. 
- Asociar el rechazo a la **causal específica** del estado bloqueante. 
- Evitar la continuidad de la evaluación.  CA‑05. Mensajes de rechazo según canal y rol 
**Dado** que una evaluación es rechazada por un estado bloqueante del documento,
**Cuando** el rechazo se origine desde el **servicio de creación de evaluación**,
**Entonces** el mensaje deberá ser: 
*“No es posible continuar con el proceso. La validación del documento de identidad con Registraduría Nacional (cédula de ciudadanía) o Migración Colombia (Cédula de Extranjería, Permiso Especial de Permanencia o Permiso por Protección Temporal) no ha sido exitosa.”* 
**Y cuando** el rechazo se visualice en el **Módulo de Clientes SARLAFT**,
**Entonces**: 
- **Para el tomador**, se deberá mostrar el **estado bloqueante** conforme a la definición actual. 
- **Para figuras distintas al tomador**, se deberá mostrar el mensaje:  
*“La consulta del estado del documento con Migración Colombia no ha sido exitosa: (estado bloqueante)”* CA‑06. Persistencia temporal del bloqueo (1 mes) 
**Dado** que el estado definitivo obtenido es **Inactivo**, **Cancelado** o **El número de identificación enviado no existe**,
**Cuando** el estado sea registrado por primera vez,
**Entonces** el sistema deberá: 
- Almacenar el estado por un período de **un (1) mes calendario**. 
- Rechazar automáticamente cualquier nueva evaluación creada durante ese mes por la misma causal.  
**Y** al iniciar el mes siguiente,
**Entonces** se deberá permitir nuevamente la creación de evaluaciones y la ejecución de la consulta del estado del documento. CA‑07. Estados que no generan bloqueo 
**Dado** que la consulta del estado del documento retorne alguno de los siguientes estados: 
- **Vigente** 
- **Número de documento errado** 
- **Tipo de documento errado**  
**Cuando** se cree la evaluación,
**Entonces** el sistema **no deberá aplicar la regla de bloqueo**,
**Y** deberá permitir la continuidad normal de la evaluación y de la consulta correspondiente. CA‑08. Reutilización del estado definitivo (herencia) 
**Dado** que el cliente ya tiene almacenado un **estado definitivo bloqueante vigente**,
**Cuando** se cree una nueva evaluación (por cualquier mecanismo habilitado),
**Entonces** el sistema deberá: 
- Reutilizar el estado previamente almacenado. 
- Identificar que se trata de una **consulta heredada**. 
- Rechazar la evaluación sin realizar una nueva consulta a Migración Colombia.  CA‑09. Persistencia obligatoria del primer estado definitivo 
**Dado** que es la **primera vez** que se obtiene un estado definitivo bloqueante para un cliente,
**Cuando** se procese la respuesta del servicio de Experian,
**Entonces** el sistema deberá guardar como mínimo: 
- Tipo de documento 
- Número de documento 
- Primer apellido 
- Estado definitivo 
- Fecha de la consulta inicial 
- Fuente de la información (Migración Colombia – Experian)  CA‑10. Trazabilidad de consultas y reutilización 
**Dado** que se obtenga un estado definitivo bloqueante,
**Cuando** se registre la información,
**Entonces** el sistema deberá permitir identificar: 
- Si el estado corresponde a una **primera consulta** o a una **reutilización (heredado)**. 
- Los datos básicos del cliente (tipo_id, número_id, primer apellido). 
- El estado bloqueante y la fecha de consulta.  CA‑11. Independencia del mecanismo de creación 
**Dado** que la evaluación se cree desde: 
- Módulo de clientes SARLAFT, o 
- Servicio de creación de evaluación expuesto a aplicativos de negocio o API de terceros,  
**Cuando** se valide el estado previo del documento,
**Entonces** las reglas de bloqueo deberán aplicarse **de manera uniforme**, sin depender del canal de origen.
