# HU 1041366 — [Reglas transversales]: Herencia por tipo de riesgo

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364) › HU 1041366 — [Reglas transversales]: Herencia por tipo de riesgo

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1041366](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041366) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-11 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364)  
  Estado: New  

## Descripción

Como Analista/PO del sistema de Clientes y SARLAFT, quiero verificar y modificar las reglas de herencia asociadas a las evidencias de validación de identidad y cumplimiento (Registraduría, Migración/Experian, PEPS, GAFI y RRCC), para optimizar consumos, evitar duplicidad de consultas, aplicar herencia inteligente de evidencias previas, y asegurar el cumplimiento normativo en el ciclo de vida SARLAFT. **
Nota de alcance: Las reglas descritas aplican a las evidencias de Registraduría, Migración (Experian), PEPS, GAFI y RRCC. 
- SOAT mantiene la excepción: no aplica herencia para validación de identidad (únicamente para ese componente). 
- La consulta con Registraduría aplica a todos los ramos y clientes.    Descripción funcional ** 
El sistema deberá ajustar las **reglas de herencia y optimización** para la generación/uso de evidencias en los siguientes escenarios:     **1) Primera evaluación SARLAFT sin evidencias previas** 
Cuando a un cliente se le genere por primera vez una evaluación SARLAFT y no tenga evidencias previas de: 
- Registraduría, Migración (Experian), Validación de identidad, PEPS, GAFI y RRCC,  
Entonces el sistema debe: 
- Ejecutar la consulta inicial con Experian (para identidad/migración) y con las fuentes/servicios correspondientes para PEPS, GAFI y RRCC. 
- Guardar la evidencia retornada por cada consulta. 
- Si la evidencia de identidad es exitosa:

- Riesgo Simplificado u Ordinario: registrar la evidencia con vigencia de (3) años. 
- Riesgo Intensificado: registrar la evidencia con vigencia de un (1) año.   
- Para PEPS, GAFI y RRCC, se debe validar cada vez que el se genere una evaluación de sarlaft teniendo en cuenta que se tiene un monitoreo de listas.  
**Excepciones y cobertura:** 
- SOAT: no hereda evidencias de validación de identidad (se conserva la regla actual). 
- Registraduría: sí, aplica para todos los ramos y todos los clientes.      **2) Primera evaluación SARLAFT con evidencia previa en estado “Fallido”** 
Cuando se cree la primera evaluación SARLAFT y exista evidencia previa Fallida (en cualquiera de las categorías: identidad/Experian, Registraduría, PEPS, GAFI, RRCC): 
**Entonces el sistema debe:** 
- Evaluar las reglas de optimización para evitar duplicidad para la consulta con la Registraduría, Migración y Validación de identidad. 
- Para las evidencias de PEPS, GAFI y RRCC no se hereda el estado. Se debe volver a hacer la consulta cada vez       **3) Primera evaluación SARLAFT con evidencia previa “Falla técnica” o “Pendiente”** 
Cuando el cliente tenga evidencia previa con estado **Falla técnica** o **Pendiente** (para cualquiera de las categorías: identidad/Experian, Registraduría, **PEPS, GAFI, RRCC**): 
**Entonces:** 
- **No se debe heredar** el estado (no es evidencia válida). 
- **Se debe volver a consultar** a la fuente correspondiente (Experian/Registraduría/listas). 
- Según el nuevo resultado:

- Si pasa de **Falla técnica → Exitosa**: aplicar el **Escenario 1** (guardar y definir vigencia según riesgo/categoría). 
- Si pasa de **Falla técnica → Fallida**: aplicar el **Escenario 2** (reglas de optimización para evitar duplicidad).        **4) Estado del formulario para las evaluaciones**
 
- **Se puede heredar el formulario cuando:**  
- El formulario está finalizado y la clasificación de riesgo se mantiene igual entre la primera y la nueva evaluación:  
- Si en la primera evaluación quedó en Simplificado y en la nueva también es Simplificado. 
- Si en la primera evaluación quedó en Ordinario y en la nueva también es Ordinario. 
- Si en la primera evaluación quedó en Intensificado y en la nueva también es Intensificado  
- La herencia del formulario debe tener la regla según el tipo de riesgo 
- Simplificado y ordinario: Heredar por tres años (1095 días). A partir del día 1096 se debe pedir formulario si se crea una evaluación. 
- intensificado: Heredar por un año (365 días). A partir del día 366 se debe pedir formulario si se crea una evaluación.
  
- Cuando el formulario tenga alguna de las condiciones descritas en los puntos anteriores, la información este completa y los requisitos adjuntos (cuando aplique).   
-  **No se puede heredar el formulario cuando:**   
- El formulario está finalizado, pero la clasificación de riesgo aumenta entre la primera y las siguientes evaluaciones: 
- Si quedó en Simplificado y la nueva evaluación es Ordinario. 
- Si quedó en Ordinario y la nueva evaluación es Intensificado. 
- Si quedó en Simplificado y la nueva evaluación es Intensificado.  
- El formulario tiene la información completa pero no tiene adjunto los requisitos. Aplica para el riesgo ordinario e intensificado.    **5) Consideraciones transversales ** 
- **Cobertura de categorías:** Todas las reglas aplican a Consulta del documento de identidad (Registraduría/Migración-Experian) y a Validaciones mínimas (PEPS, GAFI y RRCC). 
- **Vigencias:** 
- Consulta del documento de Identidad: permanente para Simplificado/Ordinario; 1 año para Intensificado. 
- PEPS/GAFI/RRCC:  Tener en cuentas las nuevas definiciones de las listas de monitoreo  
- **Optimización:** tener en cuenta las reglas de optimización definidas. 
- **Trazabilidad:** guardar fuente, fecha/hora, resultado, vigencia, usuario/proceso, identificadores de solicitud (Logs ya existentes) 
- **SOAT**: no hereda validación de identidad; sí aplica herencia y consultas para PEPS, GAFI y RRCC según políticas corporativas. 
- Registraduría: aplica a todos los ramos.

## Criterios de Aceptación

**1. Primera evaluación SARLAFT sin evidencias previas** 1.1 Ejecución de consultas iniciales 
- Cuando un cliente no tiene evidencias previas de Registraduría, Migración (Experian), Validación de identidad, PEPS, GAFI y RRCC,
el sistema debe ejecutar la consulta inicial con:

- Experian (identidad/migración). 
- PEPS, GAFI y RRCC en sus respectivas fuentes/servicios.      1.2 Registro de evidencias 
- El sistema debe guardar la evidencia retornada por cada consulta ejecutada.    1.3 Vigencia de evidencias exitosas de identidad 
- Si la evidencia de identidad es exitosa, el sistema debe:

- Registrar vigencia de 3 años para riesgo Simplificado u Ordinario. 
- Registrar vigencia de 1 año para riesgo Intensificado.      1.4 Validación de PEPS, GAFI y RRCC 
- El sistema debe generar una nueva validación en cada evaluación SARLAFT, teniendo en cuenta el monitoreo de listas, sin aplicar herencia.    1.5 Excepciones 
- Para SOAT: el sistema no debe heredar evidencias de validación de identidad. 
- La consulta con Registraduría aplica para todos los ramos y clientes.    **2. Primera evaluación SARLAFT con evidencias previas en estado “Fallido”** **
** 2.1 Reglas de optimización 
- Cuando exista evidencia previa Fallida en cualquier categoría,

el sistema debe evaluar las reglas de optimización para evitar duplicidad en:

- Consulta con Registraduría. 
- Consulta con Migración (Experian). 
- Validación de identidad.      2.2 Evidencias PEPS, GAFI y RRCC 
- Las evidencias previas en estado Fallido de PEPS, GAFI y RRCC no deben heredarse. 
- El sistema debe realizar una nueva consulta.    **3. Primera evaluación SARLAFT con evidencia previa “Falla técnica” o “Pendiente”** 3.1 No heredar estados 
- Para cualquier categoría en estado **Falla técnica** o **Pendiente**,

el sistema **no debe heredar** la evidencia.    3.2 Re-ejecución de consultas 
- El sistema debe **volver a consultar** la fuente correspondiente:

- Experian. 
- Registraduría. 
- Servicios de listas PEPS, GAFI y RRCC.      3.3 Manejo de nuevo resultado 
- Si el nuevo resultado es **Exitoso**, el sistema debe aplicar lo definido en el Escenario 1 (registro y vigencia por riesgo). 
- Si el nuevo resultado es **Fallido**, el sistema debe aplicar lo definido en el Escenario 2 (reglas de optimización para evitar duplicidad).    **4. Estado del formulario para las evaluaciones** **
** 4.1 Herencia del formulario cuando el riesgo se mantiene 
El sistema debe permitir heredar el formulario cuando: 
- El formulario está **finalizado**, y 
- La clasificación de riesgo **se mantiene igual** entre ambas evaluaciones:

- Simplificado → Simplificado. 
- Ordinario → Ordinario. 
- Intensificado → Intensificado.      4.2 Vigencias de herencia del formulario 
- Para riesgo Simplificado y Ordinario:

- Herencia válida por 3 años (1095 días). 
- Desde el día 1096, el sistema debe exigir un nuevo formulario.   
- Para riesgo Intensificado:

- Herencia válida por 1 año (365 días). 
- Desde el día 366, el sistema debe exigir un nuevo formulario.      4.3 Requisitos para permitir herencia 
- El sistema debe permitir heredar solo si:

- El formulario está finalizado. 
- La información está completa. 
- Los requisitos obligatorios están adjuntos (cuando aplica).      4.4 Casos en los que NO se debe heredar 
El sistema no debe permitir heredar cuando: 
- El riesgo aumenta entre evaluaciones:

- Simplificado → Ordinario. 
- Ordinario → Intensificado. 
- Simplificado → Intensificado.   
- El formulario, aunque completo, no tiene adjuntos los requisitos obligatorios (para riesgos Ordinario e Intensificado).    **5. Consideraciones transversales** 5.1 Cobertura 
- Todas las reglas aplican a:

- Consulta del documento de identidad (Registraduría / Migración-Experian). 
- Validaciones mínimas (PEPS, GAFI y RRCC).      5.2 Vigencias 
- Documento de identidad:

- Vigencia permanente para Simplificado y Ordinario. 
- Vigencia de 1 año para Intensificado.   
- PEPS, GAFI y RRCC:

- Se deben considerar las definiciones de las listas de monitoreo.      5.3 Optimización 
- El sistema debe aplicar las reglas de optimización definidas para evitar consultas duplicadas.    5.4 Trazabilidad 
- El sistema debe guardar:

- Fuente. 
- Fecha y hora. 
- Resultado. 
- Vigencia. 
- Usuario/proceso. 
- Identificadores de solicitud

(usando los logs ya existentes).      5.5 Excepciones 
- SOAT:

- No hereda validación de identidad. 
- Sí aplica herencia y consultas para PEPS, GAFI y RRCC.   
- Registraduría:

- Aplica para todos los ramos.
