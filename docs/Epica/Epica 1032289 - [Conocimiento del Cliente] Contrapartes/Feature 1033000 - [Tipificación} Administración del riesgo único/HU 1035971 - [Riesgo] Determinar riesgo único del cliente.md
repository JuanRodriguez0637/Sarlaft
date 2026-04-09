# HU 1035971 — [Riesgo]: Determinar riesgo único del cliente

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000) › HU 1035971 — [Riesgo]: Determinar riesgo único del cliente

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1035971](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035971) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Ciencia de datos |
| **Creado** | 2026-02-05 |
| **Última modificación** | 2026-02-10 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1033000 — [Tipificación}: Administración del riesgo único](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1033000)  
  Estado: New  

## Descripción

Como Analista SARLAFT,
quiero que el sistema asigne, verifique y actualice diariamente el nivel de riesgo único del cliente (simplificado, ordinario, intensificado),
para identificar la tipificación correcta con base en el riesgo más alto entre sus vinculaciones y características, mantener herencia cuando corresponda, detonar controles y alertas (PEP, validación de identidad, requisitos, aprobación PEP), y generar una salida operativa que soporte la gestión y la auditoría del proceso. 
 **Alcance funcional** 
- Identificación del estado del cliente y sus vinculaciones  
- Determinar el riesgo más alto aplicable al cliente (intensificado > ordinario > simplificado). 
- Ejecutar retipificación cuando apliquen eventos (PEP, GAFI, listas, cúmulos, segmentación). 
- Mantener herencia de riesgo para las validaciones . 
- Verificar pendientes (formulario, validación de identidad, requisitos, aprobación PEP) y notificar a procesos asociados. 
- No afectar reglas especiales (corredores, banca, ARL). 
- Ejecución diaria y generación de archivo de resultados.   1) Identificación del cliente activo 
- Tomar clientes del modelo SARLAFT y verificar vinculaciones vigentes en la tabla de vinculaciones.  
- **Primera corrida: **El sistema deberá tomar todos los clientes provenientes del modelo SARLAFT y validar todas sus vinculaciones vigentes, aplicando la lógica para las figuras de: tomador, asegurado, beneficiario, afianzado, afiliado, representante legal, accionistas, junta directiva y apoderados. 
- **A partir de la segunda corrida en adelante: **El sistema deberá **identificar únicamente la diferencia** entre los **clientes vigentes** y las **vinculaciones vigentes** respecto a la corrida anterior, procesando solo aquellos clientes que:  
- Entraron o salieron del estado de vinculado, 
- Cambiaron de figura o se incorporaron nuevas vinculaciones, 
- Presentan variaciones que deban ser evaluadas para tipificación o retipificación del riesgo.      
- Si no tiene vinculaciones vigentes: No se debe retirar los clientes pues le aplicará reglas de tipificación. 
- Si sí tiene vinculaciones: Traer ramo, producto, plan, valores asegurados, prima anual, indicador fondo de ahorro, valor del fondo de ahorro, canal, oficina y asesor de la vinculación vigente y comparar con la evaluación que posea el riesgo más alto (para detectar cambio de asesor/canal/oficina).  2) Reglas para riesgo intensificado (alto) 
Se eleva o mantiene intensificado cuando exista cualquiera de las siguientes condiciones: 
- PEP→ retipificación inmediata. 
- Modelo de segmentación: score alto (cargado vía Excel) según regla del motor.

- Excel con (tipo_id, número_id, score). 
- Se recarga cada 6 meses. 
- El score del cliente puede cambiar en cada carga.   
- Jurisdicción GAFI: país de nacimiento/constitución en lista gris → retipificación inmediata. 
- Listas de control: cualquier coincidencia → → retipificación inmediata. 
- Producto / montos (SMLMV):

- Vida individual: > 845 SMLMV (≈ $1.479.514.725) → intensificado. 
- Rentas: > 100 SMLMV (≈ $175.090.500) → intensificado. 
- Cúmulos por producto/ramo
- Movilidad – Persona Natural:

a) Un vehículo ≥ 300 SMLMV, o b) cúmulo en autos > 600 SMLMV. 
- Movilidad – Persona Jurídica:

a) Un vehículo ≥ 300 SMLMV, o b) cúmulo en autos > 2000 SMLMV. 
- Hogar: valor asegurado ≥ 2000 SMLMV.      
**Gestión operativa cuando sube a intensificado** 
- Si venía en simplificado/ordinario → elevar a intensificado. 
- Notificar en un log los clientes que cambiaron. 
- Acciones:

- Ordinario → “actualícelo en próxima operación”. 
- Intensificado → incluir URL del formulario para gestión con el asesor.   
- Si deja de cumplir condiciones (baja de riesgo) → aplica herencia (ver más abajo).  3) Reglas para riesgo ordinario (medio) 
- Cobertura básica > 135 SMLMV y prima anual > 6 SMLMV. 
- Productos que clasifiquen como riesgo medio:

- Rentas < 100 SMLMV, 
- Vida con la variable de fondo de ahorro.   
- Aprobados por junta: Juvenil, Colectivo autos.  
**Comportamiento** 
- Si está en simplificado y cumple una condición → elevar a ordinario 
- Mantener ordinario si ya está en ordinario y no ha tenido cambio de riesgo. 
- Si está intensificado, aunque cumpla condición de ordinario → se mantiene intensificado.  4) Reglas para riesgo simplificado (bajo) 
- Cobertura básica ≤ 135 SMLMV y prima anual < 6 SMLMV. 
- Licitación pública (marca). 
- Coaseguro aceptado. 
- Salud (individual o colectivo). 
- SOAT. 
- ARL.  
Comportamiento 
- Mantener simplificado si cumple estas condiciones. 
- Si está en intensificado/ordinario y cumple una condición de ordinario, se mantiene en su nivel superior (no baja automáticamente). 
- Si pierde condiciones de simplificado → continuar tipificación para decidir medio o alto.  5) Herencia de riesgo  
- Si el cliente cancela un producto u ocurre una variación que reduce el riesgo de alto a bajo/medio, se mantiene el riesgo alto heredado por 1 año. 
- Si el cliente se mantiene en riesgo simplificado y ordinario debe mantener la herencia en 3 años 
- Si el cliente se mantiene en riesgo intensificado debe mantener la herencia 1 año.  6) Pendientes y controles 
- Si el cliente queda PEP, verificar control PEP aprobado.

- Si NO lo tiene y le aplica retipificación, marcar pendiente y notifique al proceso de actualización.   
- Si el cliente se desmarca en PEP, retipificar al nivel que resulte de sus vinculaciones actuales. 
- Si el cliente tiene su país de nacimiento o constitución de la lista gris marcar pendiente y notifique al proceso de actualización. 
- Si tipifica de simplificado a ordinario marcar pendiente y notifique al proceso de actualización. 
- Si tipifica de simplificado a intensificado marcar pendiente y notifique al proceso de actualización.
 
- Si tipifica de ordinario a intensificado marcar pendiente y notifique al proceso de actualización.
 
- Si un cliente esta en listas de control, no se envía al proceso de actualización  7) Reglas especiales 
- No afectar reglas de corredores, banca, SOAT y ARL (mantener comportamiento vigente respecto a la tipificación de clientes)  8) Frecuencia 
- Diaria teinendo en cuenta la validación de clientes vigentes.  9) Entrega de resultados  
- En un log (archivo) entregar los resultados de la tipificación de clientes que tengan pendientes controles con los datos de: 
- Datos básicos 
- Datos de vinculación 
- Resultado de tipificación 
- Causal de tipificación 
- Fecha de actualización 
- Controles pendientes

## Criterios de Aceptación

**1. Identificación del cliente activo y sus vinculaciones** 
1.1 El sistema debe tomar diariamente el universo de clientes provenientes del modelo SARLAFT.

1.2 En la primera corrida, el sistema debe validar **todas las vinculaciones vigentes** de cada cliente considerando las figuras: tomador, asegurado, beneficiario, afianzado, afiliado, representante legal, accionistas y apoderados.

1.3 A partir de la segunda corrida, el sistema debe procesar únicamente los clientes que presenten cambios respecto a la corrida anterior, incluyendo: 
- ingreso o salida del estado de vinculado, 
- cambio de figura o incorporación de nuevas vinculaciones, 
- variaciones relevantes para tipificación o retipificación del riesgo.

1.4 Si el cliente no tiene vinculaciones vigentes, el sistema debe **mantenerlo en el universo** para aplicar reglas de tipificación y herencia.

1.5 Si el cliente sí tiene vinculaciones vigentes, el sistema debe extraer: ramo, producto, plan, valores asegurados, prima anual, indicador de fondo de ahorro, valor del fondo de ahorro, canal, oficina y asesor.

1.6 El sistema debe comparar esta información con la vinculación que posea el riesgo más alto para detectar cambios en oficina, canal o asesor.  **2. Determinación del nivel de riesgo único** 
2.1 El sistema debe asignar el nivel de riesgo único del cliente conforme a la regla jerárquica:
**intensificado > ordinario > simplificado**.

2.2 El sistema debe seleccionar siempre el nivel de riesgo **más alto** entre: 
- vinculaciones vigentes, 
- características individuales, 
- condiciones especiales (PEP, GAFI, listas, segmentación, cúmulos, productos y montos).  **3. Retipificación por eventos** 
El sistema debe realizar **retipificación inmediata** cuando se presente cualquiera de los siguientes eventos: 
3.1 Condición **PEP**.

3.2 Cliente ubicado en jurisdicción GAFI lista gris por país de nacimiento o constitución.

3.3 Coincidencia en listas de control.

3.4 Score alto del modelo de segmentación cargado vía Excel (actualizado cada 6 meses).

3.5 Montos superiores a los umbrales de riesgo alto para vida individual, rentas, movilidad (PN/PJ), o hogar.

3.6 Cúmulos que superen los límites definidos para cada producto/ramo. **4. Reglas para clasificación intensificada** 
El sistema debe elevar o mantener al cliente en **riesgo intensificado** cuando cumpla al menos una de las condiciones definidas en: 
- PEP 
- Segmentación (score alto) 
- Jurisdicción GAFI lista gris 
- Listas de control 
- Productos/montos superiores a los umbrales 
- Cúmulos superiores a límites definidos  
4.1 Si el cliente pasa de simplificado u ordinario a intensificado, el sistema debe registrar el cambio en un log.

4.2 Para clientes intensificados se debe incluir en el resultado operativo la URL del formulario correspondiente para gestión del asesor.

4.3 Si deja de cumplir condiciones de intensificado, el sistema debe aplicar **herencia** según reglas definidas. **5. Reglas para clasificación ordinaria** 
El sistema debe clasificar al cliente como ordinario cuando: 
5.1 La cobertura básica sea >135 SMLMV **y** la prima anual >6 SMLMV.

5.2 El cliente tenga productos catalogados como riesgo medio: 
- Rentas <100 SMLMV 
- Vida con fondo de ahorro 
- Juvenil 
- Colectivo autos  
Comportamiento: 
- Si está en simplificado y cumple condiciones → subir a ordinario. 
- Si ya está en ordinario y no hay cambios → mantener. 
- Si está en intensificado → mantener intensificado (no baja).  **6. Reglas para clasificación simplificada** 
El sistema debe clasificar al cliente como simplificado cuando cumpla al menos uno de estos criterios: 
- Cobertura básica ≤135 SMLMV y prima anual <6 SMLMV 
- Licitación pública 
- Coaseguro aceptado 
- Salud (colectivo o individual) 
- SOAT 
- ARL  
Comportamiento: 
- Si el cliente cumple condiciones de simplificado → se mantiene simplificado. 
- Si cumple condiciones de ordinario/intensificado → prevalece el nivel superior. 
- Si pierde simplificado → debe ser evaluado nuevamente para definir si pasa a medio o alto.  **7. Herencia de riesgo** 
7.1 Si el cliente reduce su riesgo desde alto hacia medio/bajo por cancelación o variación, debe mantener **riesgo alto heredado durante 1 año**.

7.2 Si el cliente permanece en simplificado u ordinario, debe mantener la herencia durante **3 años**.

7.3 Si permanece en intensificado, la herencia se mantiene por **1 año**.

7.4 El sistema debe impedir la reducción del nivel de riesgo mientras esté vigente la herencia. **8. Pendientes y controles** 
El sistema debe detectar y marcar pendientes cuando corresponda: 
8.1 Si el cliente queda PEP, debe verificar si cuenta con aprobación PEP. 
- Si no la tiene → marcar pendiente y notificar a proceso de actualización.  
8.2 Si el cliente se desmarca como PEP → retipificar según condiciones actuales. 
8.3 Si el cliente tiene país en lista gris → marcar pendiente y notificar. 
8.4 Si el cliente tipifica de: 
- simplificado → ordinario 
- simplificado → intensificado 
- ordinario → intensificado

Debe marcarse pendiente y notificarse a proceso de actualización.  
8.5 Si el cliente está en listas de control, **no** debe enviarse al proceso de actualización (pero sí registrarse su estado). 
8.6 Los pendientes deben incluirse en la salida operativa diaria. **9. Reglas especiales** 
9.1 El sistema no debe modificar la tipificación de clientes pertenecientes a: 
- corredores 
- banca 
- ARL 
- SOAT  
9.2 Deben mantenerse las reglas vigentes y el sistema debe ignorar cualquier causal que pueda alterar su nivel. **10. Ejecución diaria** 
10.1 El proceso debe ejecutarse diariamente considerando los clientes vigentes y sus cambios.

10.2 El sistema debe garantizar consistencia entre la corrida del día y la del día anterior (control de delta). **11. Entrega de resultados** 
11.1 El sistema debe generar un archivo de resultados (log o Excel) con los clientes que: 
- hayan cambiado de nivel, 
- tengan pendientes, 
- presenten causales que impacten controles, 
- deban ser gestionados por procesos asociados.  
11.2 El archivo debe contener como mínimo: 
- Datos básicos del cliente 
- Datos de vinculación vigente 
- Nivel de riesgo asignado 
- Causal de tipificación o retipificación 
- Fecha de actualización 
- Controles pendientes
