---
title: "Sarlafts Candidatos para Actualizar"
confluence_id: 3713728533
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3713728533"
last_modified: "2024-05-07"
author: "Mauricio Marin Martinez"
version: 3
---

# Sarlafts Candidatos para Actualizar

> **Fuente Confluence:** [Sarlafts Candidatos para Actualizar](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3713728533)
> **Última modificación:** 2024-05-07 — Mauricio Marin Martinez · versión 3
> **Sección:** [Proceso de Actualización](./index.md)

Los candidatos a actualizar surgen de la necesidad de encontrar los clientes cuyos sarlafts se encuentren vencidos, por esta razon, se realiza la siguiente agrupacion de clientes a los cuales se les debe crear evaluacion de actualizacion cumpliendo con las siguientes definiciones:

| **GRUPO** | **Inclusión/exclusión del query** | **DESCRIPCIÓN** | **REGLA DE NEGOCIO** | **VARIABLES BD** |
|---|---|---|---|---|
| Grupo A: Regla por norma de SARLAFT | Tener en cuenta en el conjunto de datos del query | Clientes con evaluaciones de negocio nuevo y/o reclamaciones que son candidatas a actualizar | Clientes con riesgo simplificado: >1035 y <1095 días en la fecha de creación de la evaluación de negocio y/o reclamaciones | `tsaf_riesgo`: `cdtiporiesgo`\`tsaf_evaluacion`: `fecreacion`\`tsaf_evaluacion`: `cdoperacion` |
| ^^^ | ^^^ | ^^^ | Clientes con riesgo ordinario: >1035 y <1095 días en la fecha de creación de la evaluación de negocio y/o reclamaciones | `tsaf_riesgo`: `cdtiporiesgo`\`tsaf_evaluacion`: `fecreacion`\`tsaf_evaluacion`: `cdoperacion` |
| ^^^ | ^^^ | ^^^ | Clientes con riesgo intensificado: >305 y <365 días en la fecha de creación de la evaluación de negocio y/o reclamaciones | `tsaf_riesgo`: `cdtiporiesgo`\`tsaf_evaluacion`: `fecreacion`\`tsaf_evaluacion`: `cdoperacion` |
| Grupo B: Clientes con riesgo distinto al de la norma | No se tiene en cuenta en el conjunto de datos del query | Clientes con estados distintos a los definidos de la norma | Clientes con riesgo `NO_APLICA` | `tsaf_riesgo`: `cdtiporiesgo` |
| Grupo C: Clientes con riesgo a homologar | Tener en cuenta en el conjunto de datos del query | Clientes con riesgo que es distinto a la norma y se debe homologar | Clientes con riesgo `INTENSIFICADO_MONITOREO` son categorizados con riesgo `INTENSIFICADO`\Clientes con riesgo NULL o VACIO son categorizados con riesgo `ORDINARIO` | `tsaf_riesgo`: `cdtiporiesgo` |
| Grupo B: Clientes con sarlaft finalizado | Tener en cuenta en el conjunto de datos del query | Clientes con evaluaciones de negocio nuevo y/o reclamaciones que son candidatas a actualizar | Clientes con evaluaciones de negocio nuevo y/o reclamaciones con estado: `FINALIZADO`, `FINALIZADO_SIN_CARGA` | `tsaf_evaluacion`: `cdestado`\`tsaf_evaluacion`: `cdoperacion` |
| Grupo C: Figuras de los clientes a actualizar | Tener en cuenta en el conjunto de datos del query | ^^^ | Aplica para el tomador\Aplica para el beneficiario, asegurado, afianzado, afiliado que tengan el campo `opcomplinformacion` en TRUE\que tengan evaluaciones de negocio nuevo y/o reclamaciones | `tsaf_figura`: `dsfigura`\`tsaf_sarlaft`: `opcomplinformacion` en TRUE\`tsaf_evaluacion`: `cdoperacion` |
| Grupo D: Figuras de los clientes que no se actualizan | No se tiene en cuenta en el conjunto de datos del query | Clientes con figuras de la evaluación de negocio nuevo y/o reclamaciones | No aplica para el representante legal, accionista, apoderado y consorcio que tengan evaluaciones de negocio nuevo y/o reclamaciones | `tsaf_figura`: `dsfigura`\`tsaf_evaluacion`: `cdoperacion` |
| Grupo E: Regla de vencidos por actualización TEMPORAL | Tener en cuenta en el conjunto de datos del query | Clientes con evaluaciones de actualización vencidas por fecha de creación sin crear una nueva evaluación de actualización. Solo temporal para el desatrase. | Clientes con riesgo simplificado: >=1095 días en la fecha de actualización de la evaluación de actualización | `tsaf_riesgo`: `cdtiporiesgo`\`tsaf_evaluacion`: `cdestado`\`tsaf_evaluacion`: `cdoperacion`\`tsaf_sarlaft`: `feactualizacion` |
| ^^^ | ^^^ | ^^^ | Clientes con riesgo ordinario: >=1095 días en la fecha de actualización de la evaluación de actualización | `tsaf_riesgo`: `cdtiporiesgo`\`tsaf_evaluacion`: `cdestado`\`tsaf_evaluacion`: `cdoperacion`\`tsaf_sarlaft`: `feactualizacion` |
| ^^^ | ^^^ | ^^^ | Clientes con riesgo intensificado: >=365 días en la fecha de actualización de la evaluación de actualización | `tsaf_riesgo`: `cdtiporiesgo`\`tsaf_evaluacion`: `cdestado`\`tsaf_evaluacion`: `cdoperacion`\`tsaf_sarlaft`: `feactualizacion` |
| Grupo F: Regla de vencidos por falta de gestión | No se tiene en cuenta en el conjunto de datos del query | Clientes con evaluaciones de actualización creada con estado PENDIENTE y que no han sido gestionadas. Esta regla se adiciona una vez se ejecute las pruebas del grupo B y se estabilice en PDN las desactualizadas. | Clientes con evaluación de actualización creada y que supera los días de vencimiento, tiene estado de la evaluación de actualización `PENDIENTE` y no se le crea una nueva evaluación de actualización.\Clientes con riesgo simplificado: >=1095 días en la fecha de actualización de la evaluación de actualización\Clientes con riesgo ordinario: >=1095 días en la fecha de actualización de la evaluación de actualización\Clientes con riesgo simplificado: >=365 días en la fecha de actualización de la evaluación de actualización | `tsaf_evaluacion`: `cdestado`\`tsaf_evaluacion`: `cdoperacion`\`tsaf_sarlaft`: `feactualizacion`\`tsaf_riesgo`: `cdtiporiesgo` |
| Grupo G: Regla de los clientes en otros procesos vigentes | Tener en cuenta en el conjunto de datos del query | Clientes con evaluaciones de negocio nuevo y/o reclamaciones en estado `PENDIENTE` con fecha superior a 15 días. | | |
| Grupo H: Regla de los clientes con errores | Tener en cuenta en el conjunto de datos del query | Clientes que al intentar una evaluación de actualización y presento un error técnico o inconsistencias | Dnis de clientes que al intentar crear una evaluación de actualización entonces genere un error técnico. Excluir los casos que no hay vinculación del cliente. | `tsaf_proceso_actualizacion`: `dscausa_error` |
| Grupo I: Regla de los clientes que tienen evaluaciones de actualización canceladas o rechazadas | Tener en cuenta en el conjunto de datos del query | Clientes con evaluaciones de actualización `CANCELADAS` o `RECHAZADAS` | Clientes que se les crea una evaluación de actualización y tiene estado de `RECHAZADO` o `CANCELADO` la evaluación de actualización | `tsaf_evaluacion`: `cdestado` (`RECHAZADO`, `CANCELADO`)\`tsaf_evaluacion`: `cdoperacion` (`AC`) |
| Grupo J: Regla de los clientes que tienen evaluaciones de negocio nuevo y/o reclamaciones con estado distinto a finalizado | No se tiene en cuenta en el conjunto de datos del query | Clientes con evaluaciones de negocio nuevo y/o reclamaciones con estado `CANCELADO`, `RECHAZADO`, `PENDIENTE_ACCIÓN MANUAL`, `PENDIENTE` | Clientes que se les crea una evaluación de negocio nuevo y/o reclamaciones y la evaluación tiene estado de: `CANCELADO`, `RECHAZADO`, `PENDIENTE_ACCIÓN MANUAL`, `PENDIENTE` | `tsaf_evaluacion`: `cdestado` (`CANCELADO`, `RECHAZADO`, `PENDIENTE_ACCIÓN MANUAL`, `PENDIENTE`)\`tsaf_evaluacion`: `cdoperacion` (`01` Y `RE`) |
| Grupo K: Regla de clientes que ya tienen evaluación de actualización pendiente y no están vencidos | No se tiene en cuenta en el conjunto de datos del query | Clientes que se les creo una evaluación de actualización y esta en estado `PENDIENTE` y no han llegado al rango de vencimiento por riesgo (riesgo simplificado: >=1095, riesgo ordinario: >=1095 y riesgo intensificado: >=365) | Clientes que estén en la tabla de actualización de sarlaft con estado `PENDIENTE` o `PENDIENTE_VALIDACION` | `sarlaft_actualizacion_data`: `cdestado`\`tsaf_proceso_actualización`: `cdestado` |
| Grupo K: Regla de clientes de la migración | Tener en cuenta en el conjunto de datos del query | Clientes que se les creo una evaluación de migración de clientes desde la base de datos del modelo de clientes y que tengan evaluación en estado `PENDIENTE` | Clientes que tengan una evaluación de migración con estado pendiente | `tsaf_evaluacion`: `cdestado` (`PENDIENTE`)\`tsaf_evaluacion`: `cdoperacion` (`MI`) |

El detalle de esta implementacion y sus observaciones se encuentran en el siguiente archivo adjunto:

[Reglas query actualización.xlsx](./attachments/Reglas%20query%20actualizaci%C3%B3n.xlsx)

Teniendo como insumo las definiciones descritas anteriormente, se tiene la siguiente sentencia sql:

```sql
select tsa.nmsarlaft, tsa.cdestado, tsa.fecreacion, tsa.feactualizacion, tsa.dni_cliente, tsa.nmevaluacion, tr3.cdtiporiesgo, tfa.dsfigura
            from  sarlaft.tsaf_sarlaft tsa 
            inner join sarlaft.tsaf_figura tfa on tsa.nmsarlaft = tfa.nmsarlaft 
            inner join sarlaft.tsaf_riesgo tr3 on tsa.nmsarlaft = tr3.nmsarlaft
            inner join sarlaft.tsaf_evaluacion tev on tsa.nmevaluacion = tev.nmevaluacion 
            where tfa.dsfigura <> 'REPRESENTANTE_LEGAL' and tfa.dsfigura <> 'ACCIONISTA' and tfa.dsfigura <> 'CONSORCIO' and tfa.dsfigura <> 'APODERADO'
            and 
           (tfa.dsfigura = 'TOMADOR' or ((tfa.dsfigura = 'BENEFICIARIO' or tfa.dsfigura = 'ASEGURADO' or tfa.dsfigura = 'AFIANZADO') and tsa.opcomplinformacion = 'TRUE' ))
            and tr3.cdtiporiesgo <> 'NO_APLICA'
            and
            (
	            (
		           tev.cdoperacion in ('01','RE','AC')
		           and 
		           (tsa.cdestado = 'FINALIZADO' or tsa.cdestado = 'FINALIZADO_SIN_CARGA') 
		           and 
		           (
		           (tr3.cdtiporiesgo = 'SIMPLIFICADO' and DATE_PART('day', current_date - tsa.fecreacion) > '1035') or
		           (tr3.cdtiporiesgo = 'ORDINARIO' and DATE_PART('day', current_date - tsa.fecreacion) > '1035') or
		           (tr3.cdtiporiesgo like 'INTENSIFICADO%' and DATE_PART('day', current_date - tsa.fecreacion) > '305')
		           )
		        )
	           or
	           (
	           	(tev.cdoperacion = 'MI') and (tsa.cdestado = 'PENDIENTE')        
	           )
	           or
	           (
	            (tev.cdoperacion = 'AC') and (tsa.cdestado = 'CANCELADO' or tsa.cdestado = 'RECHAZADO' )          
	           )
	           
           )
           and 
          	not exists
           (
           select 1
            from sarlaft.tsaf_sarlaft tsa2 
            inner join sarlaft.tsaf_figura tfa2 on tsa2.nmsarlaft = tfa2.nmsarlaft 
            inner join sarlaft.tsaf_riesgo tr32 on tsa2.nmsarlaft = tr32.nmsarlaft
            inner join sarlaft.tsaf_proceso_actualizacion tpa on tsa2.dni_cliente=tpa.dni_cliente  
            where tfa2.dsfigura <> 'REPRESENTANTE_LEGAL' and tfa2.dsfigura <> 'ACCIONISTA' and tfa2.dsfigura <> 'CONSORCIO' and tfa2.dsfigura <> 'APODERADO'
            and 
           (tfa2.dsfigura = 'TOMADOR' or ((tfa2.dsfigura = 'BENEFICIARIO' or tfa2.dsfigura = 'ASEGURADO' or tfa2.dsfigura = 'AFIANZADO') and tsa2.opcomplinformacion = 'TRUE' ))
            and tr32.cdtiporiesgo <> 'NO_APLICA'
            and 
            (tpa.cdestado = 'PENDIENTE' or tpa.cdestado = 'PENDIENTE_VALIDACION' or (
            		(tpa.cdestado = 'FINALIZADO' )
            		and (
	            	(tr32.cdtiporiesgo = 'SIMPLIFICADO' and DATE_PART('day', current_date - tsa2.fecreacion) <= '1035') or
	            	(tr32.cdtiporiesgo = 'ORDINARIO' and DATE_PART('day', current_date - tsa2.fecreacion) <= '1035') or
			        (tr32.cdtiporiesgo like 'INTENSIFICADO%' and DATE_PART('day', current_date - tsa2.fecreacion) <= '305')
		        	))
		        )
		         and tsa.dni_cliente=tsa2.dni_cliente 
 		        
		     )
		     order by  tsa.dni_cliente, tr3.cdtiporiesgo limit 5000
```

Nota: Es de tener en cuenta que se estan aplicando las reglas para todos los sarlaft vencidos de manera temporal, es decir, el deber ser es para:

| Regla |
|---|
| Clientes con riesgo simplificado: >1035 y <1095 días en la fecha de creación de la evaluación de negocio y/o reclamaciones |
| Clientes con riesgo ordinario: >1035 y <1095 días en la fecha de creación de la evaluación de negocio y/o reclamaciones |
| Clientes con riesgo intensificado: >305 y <365 días en la fecha de creación de la evaluación de negocio y/o reclamaciones |

Y se decidio de manera temporal, tener en cuenta todos los sarlaft vencidos con estas condiciones:

| Regla temporal |
|---|
| Clientes con riesgo simplificado: >=1095 días en la fecha de actualización de la evaluación de actualización |
| Clientes con riesgo ordinario: >=1095 días en la fecha de actualización de la evaluación de actualización |
| Clientes con riesgo simplificado: >=365 días en la fecha de actualización de la evaluación de actualización |

Nota: Existen condiciones que se deben ajustar teniendo en cuenta la ejecucion de la operacion, ver observaciones de la columna F del excel adjunto.
