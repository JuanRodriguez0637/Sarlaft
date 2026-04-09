# HU 1102574 — [Admon Riesgo]: Generar evaluaciones SARLAFT a partir de información parcial del cliente

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000) › HU 1102574 — [Admon Riesgo]: Generar evaluaciones SARLAFT a partir de información parcial del cliente

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1102574](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1102574) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-04-01 |
| **Última modificación** | 2026-04-06 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000)  
  Estado: New  

## Descripción

Como Analista SARLAFT Quiero crear evaluaciones SARLAFT para clientes cuya información se encuentra disponible de forma separada Para asegurar que los clientes cuenten con una evaluación SARLAFT completa y conforme a SARLAFT 4.0, aun cuando los insumos de información no provengan de un flujo único o integrado. 
 **Alcance funcional** 
- La funcionalidad debe permitir la **creación de evaluaciones SARLAFT** para clientes que cuentan con información separada, recolectada desde diferentes fuentes internas. 
- Para estos clientes, la composición de la evaluación, incluye:
- Información relacionada con el formulario  
- Información general del cliente 
- Persona natural: tipo id, numero id, nombres, apellidos, fecha de expedición del documento, fecha de nacimiento, país de nacimiento, número de celular y correo electrónico. 
- Persona jurídica: tipo id, numero id, razón social, fecha de constitución, país de constitución, número de celular y correo electrónico.  
- Información financiera 
- Ingresos, egresos, activos, pasivos, actividad económica, ocupación y declaración de origen de bienes  
- Información de direcciones 
- Departamento, ciudad, municipio y dirección  
- Reglas del formulario 
- Si el riesgo es simplificado y tiene completa la información "general del cliente" entonces marcar como FINALIZADO. 
- Si el riesgo es ordinaria y tiene completa la información "general del cliente", "direcciones" y "financiera" entonces marcar como FINALIZADO.
 
- Si el riesgo es ordinaria y tiene completa la información "general del cliente", "direcciones" y "financiera" entonces marcar como PENDIENTE.
 
- Si no cumple ninguna de las reglas definidas entonces marcar como PENDIENTE.     
- Tipo de riesgo 
- Simplificado 
- Ordinario 
- Intensificado 
- Intensificado monitoreo 
- No aplica   
- Evidencias y resultados asociados a: 
- Listas (RRCC) -> Resultado fallido o exitoso 
- Estado del documento (*document_pn*)  -> Vigente, cancelado, fallecido etc. 
- Indicador (PEP)  -> Resultado fallido o exitoso 
- País y categoría de las Listas GAFI  -> Resultado fallido o exitoso 
- Experian  -> Exitoso, fallido o pendiente 
- Si no cuenta con alguna de las evidencias mencionadas se debe ejecutar las que tengan estado pendiente  
- Estados según las evidencias 
- Rechazado: Se asigna cuando alguna de las evidencias tiene estado fallido 
- Pendiente: Se asigna cuando alguna de las evidencias tiene estado pendiente 
- Finalizado: Se asigna cuando alguna de las evidencias tiene estado exitoso  
- Figuras evaluadas La creación de la evaluación debe aplicar a las siguientes figuras: 
- Tomador 
- Asegurado 
- Beneficiario 
- Afiliado 
- Si es persona jurídica, asociar: 
- Representante legal 
- Accionista   
- Tipo de persona 
- Persona Natural 
- Persona Jurídica     **Comportamiento del proceso ** 
- El sistema debe:

- Crear la evaluación SARLAFT con: 
- La información disponible del formulario 
- Ejecutar las validaciones mínimas faltantes 
- Guardar la evaluación en la base de datos 
- Incluir una marca que indique la creación de evaluación parcial proveniente de la "Administración del riesgo". 
- Emisión de mensajes de inconsistencias y errores cuando aplique  
- Si la evaluación no se encuentra completa, no se debe crear el registro. En estos casos, se deberá registrar la observación: “Evaluación incompleta”. La información deberá quedar disponible para su visualización a través de tableros de seguimiento.
  
- Ejecutarse diariamente durante un periodo que no afecte la operación diaria 
- En caso de presentarse errores durante la ejecución, se deberá registrar la auditoría correspondiente, indicando el motivo del error, con el fin de visualizar las fallas técnicas y permitir el relanzamiento de las peticiones. En estos casos, se deberá registrar la observación: “Evaluación con falla técnica”.

## Criterios de Aceptación

1. Creación de evaluaciones con información separada 
**Dado** un cliente cuya información se encuentra recolectada desde diferentes fuentes internas
**Cuando** el Analista SARLAFT ejecuta la funcionalidad
**Entonces** el sistema debe permitir la **creación de una evaluación SARLAFT** utilizando la información disponible, aun cuando no provenga de un flujo único o integrado. 2. Información mínima incluida en la evaluación 
**Dado** que se crea una evaluación SARLAFT
**Entonces** la evaluación debe componerse únicamente de la información disponible de acuerdo con el tipo de persona: 
- 
**Persona Natural**: 
- Tipo de identificación 
- Número de identificación 
- Nombres 
- Apellidos 
- Fecha de expedición del documento 
- Fecha de nacimiento 
- País de nacimiento 
- Número de celular 
- Correo electrónico   
- 
**Persona Jurídica**: 
- Tipo de identificación 
- Número de identificación 
- Razón social 
- Fecha de constitución 
- País de constitución 
- Número de celular 
- Correo electrónico    3. Información financiera y de direcciones 
**Dado** que la información existe en las fuentes internas
**Entonces** la evaluación debe incluir: 
- Información financiera: ingresos, egresos, activos, pasivos, actividad económica, ocupación y declaración de origen de bienes. 
- Información de direcciones: departamento, ciudad, municipio y dirección.  4. Figuras evaluadas 
**Dado** que se crea una evaluación SARLAFT
**Entonces** la evaluación debe poder crearse para las siguientes figuras: 
- Tomador 
- Asegurado 
- Beneficiario 
- Afiliado  5. Evaluaciones para personas jurídicas 
**Dado** que el cliente es una persona jurídica
**Entonces** la evaluación debe permitir asociar: 
- Representante legal 
- Accionistas  6. Tipos de riesgo soportados 
**Dado** que se crea una evaluación SARLAFT
**Entonces** el tipo de riesgo asignado debe corresponder a uno de los siguientes valores: 
- Simplificado 
- Ordinario 
- Intensificado 
- Intensificado monitoreo 
- No aplica  7. Reglas de estado según información del formulario 
**Dado** que se crea una evaluación
**Cuando** se evalúa la información disponible
**Entonces** el sistema debe asignar el estado de la evaluación según las siguientes reglas: 
- 
**Simplificado**: 
- Si la información general del cliente está completa → **FINALIZADO**   
- 
**Ordinario**: 
- Si la información general del cliente, direcciones y financiera está completa → **FINALIZADO** 
- Si no se cumple lo anterior → **PENDIENTE**   
- 
**Cualquier otro caso**: 
- Si no cumple ninguna regla definida → **PENDIENTE**    8. Evidencias SARLAFT y resultados 
**Dado** que se crea la evaluación
**Entonces** la evaluación debe contemplar evidencias y resultados asociados a: 
- Listas (RRCC): exitoso o fallido 
- Estado del documento (document_pn): vigente, cancelado, fallecido, etc. 
- Indicador PEP: exitoso o fallido 
- País y categoría listas GAFI: exitoso o fallido 
- Experian: exitoso, fallido o pendiente  9. Ejecución de evidencias pendientes 
**Dado** que alguna evidencia no se encuentra disponible
**Entonces** el sistema debe **ejecutar aquellas evidencias que se encuentren en estado pendiente**. 10. Estado de la evaluación según evidencias 
**Dado** que existen resultados de evidencias
**Entonces** el estado de la evaluación debe asignarse de la siguiente manera: 
- **Rechazado**: si alguna evidencia es fallida 
- **Pendiente**: si alguna evidencia está pendiente 
- **Finalizado**: si las evidencias son exitosas  11. Comportamiento del proceso 
**Dado** que se ejecuta la funcionalidad
**Entonces** el sistema debe: 
- Crear la evaluación SARLAFT con la información disponible del formulario. 
- Ejecutar las validaciones mínimas faltantes. 
- Guardar la evaluación en la base de datos. 
- Incluir una marca que identifique la evaluación como **creación parcial proveniente de la “Administración del riesgo”**. 
- Emitir mensajes de inconsistencias y errores cuando aplique.  12. Evaluación incompleta 
**Dado** que la evaluación no se encuentra completa
**Entonces**: 
- El sistema **no debe crear el registro** de la evaluación. 
- Debe registrar la observación **“Evaluación incompleta”**. 
- La información debe quedar disponible para su **visualización en tableros de seguimiento**.  13. Ejecución periódica 
**Dado** que la funcionalidad se encuentra activa
**Entonces** el proceso debe **ejecutarse diariamente**, en un periodo que **no afecte la operación diaria**. 14. Manejo de errores técnicos 
**Dado** que se presenta un error durante la ejecución
**Entonces**: 
- Se debe guardar la auditoría correspondiente con el **motivo del error**. 
- La información debe permitir **visualizar las fallas técnicas y relanzar las peti**
