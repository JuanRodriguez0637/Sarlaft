# HU 1041011 — [Proceso de actualización]: Notificaciones a los Directores y Gerentes de los clientes pendientes

[Épica 1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001) › [Feature 1082320 — [Proceso de actualización]: Notificaciones a la Red Comercial](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082320) › HU 1041011 — [Proceso de actualización]: Notificaciones a los Directores y Gerentes de los clientes pendientes

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1041011](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041011) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base; Pendiente |
| **Creado** | 2026-02-11 |
| **Última modificación** | 2026-03-30 |

## Jerarquía

- **Épica:** [1033001 — Proceso de actualización](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033001)  
  Estado: New  
- **Feature:** [1082320 — [Proceso de actualización]: Notificaciones a la Red Comercial](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082320)  
  Estado: New  

## Descripción

**** Como PO/Analista de SARLAFT,
 quiero que el sistema identifique a los clientes en estado “Desactualizado” y notifique de manera mensual a los Directores y Gerentes de Sucursales la cantidad de clientes desactualizados por asesor,
 para garantizar el seguimiento oportuno del proceso de actualización SARLAFT y facilitar la gestión comercial y de cumplimiento. 
 
 **Descripción Funcional **
 El sistema debe ejecutar un proceso mensual que identifique y notifique a los responsables comerciales sobre los clientes en estado Desactualizado, de acuerdo con las reglas normativas y la estructura jerárquica comercial.
 
 **1. Identificación y notificación mensual (cada 30 días)**
 El sistema debe identificar como Desactualizados a los clientes cuyo tiempo desde la última actualización exceda los umbrales normativos: **** 
- Clientes de riesgo Simplificado y Ordinario: más de 1.095 días (3 años).  
- Clientes de riesgo Intensificado: más de 365 días (1 año).  
**2. Regla de cálculo de días** **
** El proceso se ejecutará una vez al mes, el:
- Tercer día hábil del mes  
- En horario de 8:00 AM a 11:30 AM  Para la ejecución mensual, se deben identificar los clientes desactualizados con referencia al corte del mes anterior.

 Ejemplo:
- Ejecución: tercer día hábil de febrero 2026  
- Corte aplicable: 31 de enero de 2026  
- El sistema debe considerar solo los clientes desactualizados al 31 de enero, sin importar cambios posteriores.  **3. Jerarquía y reglas de notificación**
La notificación debe enviarse según la estructura organizacional, así: 
a. Asesores (Plantilla CCM del Asesor) Reciben:
- **Cifras consolidadas de sus Clientes, incluyendo:** 
- Cantidad de clientes pendientes de actualización por tipo de riesgo 
- 
- Cantidad de clientes de riesgo simplificado  
- Cantidad de clientes de riesgo ordinario   
- Cantidad de clientes de riesgo intensificado  
- Porcentaje de avance total de clientes a actualizar por asesor      **
** **b. Directores de Oficina (Plantilla CCM del director)
**Reciben:
- **Cifras consolidadas de sus Asesores, incluyendo:
** 
- Código del asesor 
- Nombre del asesor 
- Cantidad de clientes pendientes de actualización    
- **Cifras de clientes pendientes por categoría de riesgo por asesor**
- Cantidad de clientes de riesgo simplificado  
- Cantidad de clientes de riesgo ordinario  
- Cantidad de clientes de riesgo intensificado    **b. Gerentes de Oficina ** (Plantilla CCM del gerente de oficina)
Reciben:
- **Cifras consolidadas de los Directores de su oficina (estos consolidan la sumatoria de todos los asesores bajo cada director)** 
- Nombre del director 
- Cantidad de clientes pendientes de sus asesores  
- **Cifras de clientes pendientes por categoría de riesgo por director**
- Cantidad de clientes de riesgo simplificado  
- Cantidad de clientes de riesgo ordinario  
- Cantidad de clientes de riesgo intensificado    **c. Gerentes Regionales (Plantilla CCM del gerente regional)
**Reciben:
- **Cifras consolidadas de los Gerentes de Oficina de su Regional (esto representa las cifras totales de clientes desactualizados por oficina)** 
- Nombre de los Gerentes de oficina  
- Cantidad de clientes pendientes de sus oficinas  
- **Cifras de clientes pendientes por categoría de riesgo por Gerente de Oficina**
- Cantidad de clientes de riesgo simplificado  
- Cantidad de clientes de riesgo ordinario  
- Cantidad de clientes de riesgo intensificado  
  **4. Reglas de exclusión
**No se debe notificar si:
- El cliente pasó a estado Actualizado antes del corte mensual.  
- No se envían correos duplicados por el mismo periodo.  **5. Logs de auditoría
**El sistema debe registrar:
- Responsable notificado (Director / Gerente de Oficina / Gerente Regional)  
- Oficina y regional asociada  
- Asesores/Directores/Gerentes incluidos  
- Cantidad de clientes desactualizados  
- Fecha y hora del envío  
- Corte asociado  
- Evidencia del envío CCM (exitoso, pendiente, fallido, con errores)

## Criterios de Aceptación

1. Identificación de clientes desactualizados 
**CA‑1.1** El sistema debe identificar clientes como "Desactualizados" cuando su última fecha de actualización supere el umbral normativo según su nivel de riesgo: 
- Simplificado u Ordinario → más de 1.095 días 
- Intensificado → más de 365 días  
**CA‑1.2** El cálculo debe realizarse tomando únicamente la fecha de corte correspondiente al mes inmediatamente anterior. 
**CA‑1.3** Los clientes que pasen a estado "Actualizado" antes del corte **no deben ser incluidos** en el proceso.     2. Ejecución mensual del proceso 
**CA‑2.1** El proceso debe ejecutarse automáticamente el **tercer día hábil del mes**.
**CA‑2.2** El proceso debe ejecutarse únicamente en la franja horaria **8:00 AM a 11:30 AM**.
**CA‑2.3** La ejecución del proceso debe tomar la lista de clientes desactualizados **al cierre del mes anterior**, independientemente de cambios posteriores.     3. Reglas de notificación por jerarquía **Directores de Oficina** 
**CA‑3.1** El Director debe recibir una notificación CCM con la información de *sus asesores exclusivamente*.
**CA‑3.2** La plantilla del Director debe contener: 
- Código del asesor 
- Nombre del asesor 
- Cantidad total de clientes desactualizados por asesor 
- Cantidades por categoría de riesgo (simplificado, ordinario, intensificado)  **Gerentes de Oficina** 
**CA‑3.3** El Gerente de Oficina debe recibir una notificación CCM con la información de *sus Directores*.
**CA‑3.4** La plantilla del Gerente de Oficina debe contener: 
- Nombre del Director 
- Total de clientes desactualizados de los asesores bajo ese Director 
- Cantidades por categoría de riesgo (simplificado, ordinario, intensificado)  **Gerentes Regionales** 
**CA‑3.5** El Gerente Regional debe recibir una notificación CCM con la información de *sus Gerentes de Oficina*.
**CA‑3.6** La plantilla del Gerente Regional debe contener: 
- Nombre del Gerente de Oficina 
- Total de clientes desactualizados de la oficina 
- Cantidades por categoría de riesgo (simplificado, ordinario, intensificado)      4. Reglas de exclusión 
**CA‑4.1** Ningún responsable (Director, Gerente de Oficina, Gerente Regional) debe recibir **más de una notificación por mes**. 
**CA‑4.2** El sistema no debe enviar notificaciones duplicadas para un mismo período mensual. 
**CA‑4.3** Clientes actualizados antes del corte no deben ser contabilizados.     5. Auditoría y registro 
**CA‑5.1** El sistema debe registrar cada notificación enviada, incluyendo: 
- Responsable notificado 
- Oficina y regional asociada 
- Asesores / Directores / Gerentes incluidos 
- Cantidad total de clientes desactualizados 
- Fecha y hora del envío 
- Fecha de corte utilizada 
- Estado del envío CCM (exitoso, pendiente, fallido, con errores)  
**CA‑5.2** Los logs deben ser consultables por el equipo SARLAFT y por auditoría.
