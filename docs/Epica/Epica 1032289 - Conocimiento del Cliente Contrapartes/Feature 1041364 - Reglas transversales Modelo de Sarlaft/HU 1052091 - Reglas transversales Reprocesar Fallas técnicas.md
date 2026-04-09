# HU 1052091 — [Reglas transversales]: Reprocesar Fallas técnicas para la Consulta con la Registraduría y Migración

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364) › HU 1052091 — [Reglas transversales]: Reprocesar Fallas técnicas para la Consulta con la Registraduría y Migración

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1052091](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1052091) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-20 |
| **Última modificación** | 2026-03-19 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364)  
  Estado: New  

## Descripción

Como analista SARLAFT,
   quiero que el sistema ejecute un proceso automático por lote que detecte las consultas realizadas a Registraduría Nacional o Migración con estado *“Falla Técnica”*
para volver a procesarlas con los servicios de Experian, corregir los registros cuya falla no corresponda a errores técnicos y actualizar el estado final de cada consulta, permitiendo controlar y reducir reprocesos pendientes. 
 **Descripción General** 
Se debe construir un proceso automático por lote que: 
- Identifique las consultas cuyo estado sea Falla Técnica en las** **consultas realizadas a Registraduría Nacional o Migración 
- Verifique que la causa de dicha falla corresponda exclusivamente a errores técnicos de consumo entre Sarlaft y Experian (Solo el grupo de los errores de 500 y 502) 
- Si el error corresponde a otra causa diferente a 500 y 502, se debe reclasificar y corregir, evitando que permanezca como *Falla Técnica*. 
- Para los casos válidos, el lote debe reprocesar la consulta con los servicios de Experian.  
- El nuevo procesamiento puede arrojar tres resultados:

- **Fallido** → El proceso no debe ser consultado nuevamente.  
- Debe cambiarse en la evidencia de "Falla técnica " a "Fallido por Reproceso"
  
- **Exitoso** → El proceso no debe ser consultado nuevamente.  
- Debe cambiarse en la evidencia de "Falla técnica " a "Exitoso por Reproceso"  
- **Falla Técnica** → Debe ser incluido nuevamente en el siguiente lote semanal. 
- El número máximo de reintentos para procesar las fallas técnicas es de tres por lote  
- En la evidencia debe cambiarse la evidencia de "Falla técnica" a "Falla técnica por Reproceso" cuando supere el limite de reintentos. 
- Los reintentos que correspondan por time Out no se deben reprocesar y asignar el estado "Falla técnica time Out". 
- Los reintentos que correspondan errores diferentes al 500 y 502 no se deben reprocesar y asignar el estado "Falla técnica otros errores".
 
- Si en el segundo o tercer reintento el resultado cambia a ‘Fallido por Reproceso’, ‘Exitoso por Reproceso’, ‘Falla técnica Time Out’ o ‘Falla técnica – Otros errores’, se debe asignar el estado correspondiente.

El estado ‘Falla técnica por Reproceso’ solo debe asignarse cuando el registro completa los tres reintentos sin haber cambiado previamente a ninguno de los estados mencionados.     
- El proceso debe ejecutarse una vez a la semana, en horario que no afecte la operación productiva. 
- Los resultados de las evidencias con cada estado asignado deben ser cargados a la base de datos y publicados en Datalake para su análisis mediante informes.  
- El proceso debe contar con logs de auditoría, registrando:

- fecha y hora de ejecución del lote 
- cantidad de registros procesados 
- cantidad de registros por tipo de resultado 
- Detalle de los errores cuando superan los reintentos definidos (Se busca identificar que sean errores y no generen cobro a la bolsa de Experian)

## Criterios de Aceptación

**1) Selección de registros para el lote** 
- CA-1.1: El lote identifica las consultas con estado “Falla Técnica” provenientes de la consulta del estado del documento con la Registraduría Nacional o Migración.    **2) Validación de causal de la falla** 
- CA-2.1: El proceso verifica que la causa de la falla corresponda exclusivamente a errores técnicos de consumo entre SARLAFT y Experian. 
- CA-2.2: Si la causa no es técnica, el registro se reclasifica y corrige, evitando que permanezca como “Falla Técnica”.    **3) Reproceso con Experian** 
- CA-3.1: Para los casos válidos (falla técnica confirmada), el lote reprocesa la consulta con los servicios de Experian.    **4) Resultados del reproceso y su tratamiento** 
- CA-4.1: Si el resultado es “Fallido”, entonces:

- No se vuelve a consultar en próximos lotes. 
- En la evidencia, se cambia “Falla técnica” a “Fallido por Reproceso”.   
- CA-4.2: Si el resultado es “Exitoso”, entonces:

- No se vuelve a consultar en próximos lotes. 
- En la evidencia, se cambia “Falla técnica” a “Exitoso por Reproceso”.   
- CA-4.3: Si el resultado es “Falla Técnica”, entonces:

- El registro debe incluirse nuevamente en el siguiente lote semanal.      **5) Límite de reintentos** 
- CA-5.1: El número máximo de reintentos para procesar fallas técnicas es de tres por lote. 
- CA-5.2: Cuando el registro supera el límite de reintentos, en la evidencia se cambia “Falla técnica” a “Falla técnica por Reproceso”.    **6) Frecuencia y ventana de ejecución** 
- CA-6.1: El proceso por lote se ejecuta una vez a la semana. 
- CA-6.2: La ejecución se realiza en horario que no afecte la operación productiva.    **7) Persistencia y publicación de resultados** 
- CA-7.1: Los resultados del proceso se cargan en la base de datos. 
- CA-7.2: Se publican en Datalake para su análisis mediante informes los registros en estado “Fallido” y los de “Falla técnica” que alcanzaron el máximo de reintentos.    **8) Auditoría y logs** 
- CA-8.1: El proceso genera logs de auditoría con:

- Fecha y hora de ejecución del lote. 
- Cantidad de registros procesados. 
- Cantidad de registros por tipo de resultado.   
- CA-8.2: Cuando se superan los reintentos definidos, se registra en auditoría el detalle de los errores (con el objetivo de identificar que sean errores y evitar cobros a la bolsa de Experian).
