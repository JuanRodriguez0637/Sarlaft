# HU 1053885 — [Monitoreo]: Consulta de causales IPS y DIAN Fachada desde Riesgos Consultables para evaluaciones SARLAFT

[Épica 1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585) › [Feature 1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784) › HU 1053885 — [Monitoreo]: Consulta de causales IPS y DIAN Fachada desde Riesgos Consultables para evaluaciones SARLAFT

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1053885](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1053885) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | RRCC |
| **Creado** | 2026-02-24 |
| **Última modificación** | 2026-03-17 |

## Jerarquía

- **Épica:** [1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585)  
  Estado: New  
- **Feature:** [1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784)  
  Estado: New  

## Descripción

Como analista SARLAFT responsable del monitoreo de riesgos,
  quiero que el sistema SARLAFT 4.0 consulte automáticamente las causales IPS Fachada y DIAN Fachada desde el aplicativo de Riesgos Consultables asociadas a la causal Moral
para integrarlas como evidencia en RRCC en todas las evaluaciones de riesgo (negocio nuevo, pago de reclamación, pagos, recaudos, actualización y cancelación), aplicando una validación obligatoria y restrictiva para todas las figuras —persona natural o jurídica— y generando rechazo inmediato cuando exista coincidencia por tipo de identificación y número de identificación. **
**  **Descripción Funcional ** 
Cuando el sistema SARLAFT 4.0 procese una evaluación de cualquier tipo (negocio nuevo, pago de reclamación, pagos, recaudos, actualización y cancelación): 
- Debe realizar una consulta automática en Riesgos Consultables para verificar si el cliente evaluado tiene coincidencias en: 
- Causal IPS Fachada 
- Causal DIAN Fachada   
- La consulta debe ejecutarse para todas las figuras: 
- Tomador 
- Asegurado 
- Beneficiario 
- Beneficiario del pago 
- Afianzado 
- Afiliado 
- Apoderado 
- Representante legal (si aplica) 
- Accionistas (para jurídicas) 
- Junta directiva  
- La búsqueda debe realizarse por 
- Tipo de identificación 
- Número de identificación   
- Si existe coincidencia en cualquiera de las dos causales: 
- El sistema debe marcara la figura en la causal RRCC 
- El sistema debe rechazar automáticamente la evaluación sin continuar el flujo. 
- Debe generar el mensaje de rechazo definido.  
- Si no existe coincidencia: 
- La evaluación continúa con su flujo normal según tipo de operación. 
- No se rechaza la evaluación.  
- Si el cliente esta desmarcado de la lista 
- Cuando un cliente sea desmarcado en las listas desde Riesgos Consultables, el sistema debe actualizar automáticamente este cambio.   
- La definición del estado de falla técnica para la consulta hacía riesgos consultables debe continuar como esta definida

## Criterios de Aceptación

**CA-1. Activación de la consulta** 
- CA-1.1: Cuando el sistema SARLAFT 4.0 procese una evaluación de cualquier tipo (negocio nuevo, pago de reclamación, pagos, recaudos, actualización, cancelación), debe ejecutar automáticamente una consulta en Riesgos Consultables.    **CA-2. Alcance de la consulta (causales a verificar)** 
- CA-2.1: La consulta automática debe verificar coincidencias en:

- Causal IPS Fachada 
- Causal DIAN Fachada      **CA-3. Figuras incluidas** 
- CA-3.1: La consulta debe ejecutarse para todas las siguientes figuras:

- Tomador 
- Asegurado 
- Beneficiario 
- Beneficiario del pago 
- Afianzado 
- Afiliado 
- Apoderado 
- Representante legal (si aplica) 
- Accionistas (para jurídicas) 
- Junta directiva      **CA-4. Parámetros de búsqueda** 
- CA-4.1: La búsqueda en Riesgos Consultables debe realizarse por:

- Tipo de identificación 
- Número de identificación      **CA-5. Tratamiento cuando existe coincidencia** 
- CA-5.1: Si existe coincidencia en cualquiera de las dos causales (IPS Fachada o DIAN Fachada), el sistema debe marcar la figura en la causal RRCC. 
- CA-5.2: Si existe coincidencia, el sistema debe rechazar automáticamente la evaluación sin continuar el flujo. 
- CA-5.3: Si existe coincidencia, el sistema debe generar el mensaje de rechazo definido.    **CA-6. Tratamiento cuando no existe coincidencia** 
- CA-6.1: Si no existe coincidencia, la evaluación continúa con su flujo normal según el tipo de operación. 
- CA-6.2: Si no existe coincidencia, no se debe rechazar la evaluación.    **CA-7. Cliente desmarcado en listas** 
- CA-7.1: Cuando un cliente sea desmarcado en las listas desde Riesgos Consultables, el sistema debe actualizar automáticamente este cambio.    **CA-8. Manejo de falla técnica (consulta a Riesgos Consultables)** 
- CA-8.1: La definición del estado de falla técnica para la consulta hacia Riesgos Consultables debe continuar como está definida (sin cambios).
