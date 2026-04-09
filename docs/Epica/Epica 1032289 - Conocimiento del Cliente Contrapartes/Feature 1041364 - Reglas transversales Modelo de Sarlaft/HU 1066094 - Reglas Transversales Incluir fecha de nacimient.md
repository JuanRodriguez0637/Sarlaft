# HU 1066094 — [Reglas Transversales]: Incluir fecha de nacimiento y  fecha de constitución en la evaluación

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364) › HU 1066094 — [Reglas Transversales]: Incluir fecha de nacimiento y  fecha de constitución en la evaluación

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1066094](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1066094) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base; sin revisar |
| **Creado** | 2026-03-04 |
| **Última modificación** | 2026-03-30 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364)  
  Estado: New  

## Descripción

Como analista Sarlaft Quiero capturar y validar la fecha de nacimiento (persona natural) o la fecha de constitución (persona jurídica)
Para asegurar calidad de datos y cumplimiento normativo, habilitando controles y segmentaciones correctas en la evaluación. 
 Contextos donde aplica 
- Creación de evaluación para negocio nuevo. 
- Creación/actualización de evaluación en pago de reclamación. 
- Caso de negocio en el que si no se recibe el dato en el servicio que crea una evaluación sarlaft entonces el formulario pida la información    Figuras involucradas (todas las que existan en el caso) 
- Tomador (obligatorio). 
- Representante legal (obligatorio, si aplica). 
- Resto de figuras (beneficiario, asegurado, pagador, intermediario/asesor, apoderado, etc.) → opcional, pero:

- Si el campo está vacío desde la creación de la evaluación, entonces se debe mostrar en el formulario (visible y editable) para ambos tipos de persona.      Ubicación en el formulario 
- Grupo: Datos básicos de todas las figuras.    Reglas de Negocio 
- 
Obligatoriedad por figura 
- Tomador: obligatorio (siempre). 
- Representante legal: obligatorio cuando exista figura de representante legal. 
- Otras figuras (beneficiarios, asegurados, etc.): no obligatoria por política, pero el campo debe estar visible si viene vacío al crear la evaluación, para permitir captura manual.   
- 
Tipo de persona y campo visible 
- Persona Natural → Campo: Fecha de nacimiento. 
- Persona Jurídica → Campo: Fecha de constitución.   
- 
Formato de fecha 
- Debe ser el formato establecido por la compañía. *(Por defecto propondremos DD/MM/AAAA con máscara y calendario; si tu estándar es distinto—por ejemplo AAAA-MM-DD—lo parametrizamos).*   
- 
Validaciones de consistencia 
- Fecha de nacimiento:

- No puede ser futura. 
- Edad mínima configurable (sugerido: ≥ 18 años para tomador; parametrizable por producto y canal). 
- Edad máxima referencial (sugerido: ≤ 120 años) para control de calidad de datos.   
- Fecha de constitución:

- No puede ser futura. 
- No puede ser anterior a un umbral razonable (p. ej., 1900-01-01, parametrizable).   
- Coherencia con documentos:

- Si se captura tipo y número de documento, validar rango de fechas coherente (ej. cédula de menor, si aplica políticas).   
- Fechas límite por producto (parametrizable): ciertos ramos pueden restringir edades (p. ej., vida individual).    
- 
Visibilidad condicional 
- Si una figura distinta a tomador/representante no tiene fecha al crear la evaluación, mostrar campo para captura. 
- Si ya existe valor válido, mostrar campo en modo lectura o editable según permisos (definido por perfil).   
- 
Persistencia y auditoría 
- Persistir las fechas en master de cliente/figura y en el snapshot de la evaluación. 
- Registrar usuario, fecha-hora, origen del flujo (negocio nuevo/reclamación) y figur a.   
- 
Impacto en scoring/segmentación 
- Exponer las fechas al motor de segmentación de riesgo y alertas (edad/antigüedad de constitución puede alimentar variables de riesgo).

## Criterios de Aceptación

1. Visualización y Disponibilidad del Campo 1.1. Campo según tipo de persona 
- **CA‑01:** Si la figura es *persona natural*, el sistema debe mostrar el campo **Fecha de nacimiento**. 
- **CA‑02:** Si la figura es *persona jurídica*, el sistema debe mostrar el campo **Fecha de constitución**. 
- **CA‑03:** El campo debe mostrarse en el grupo **"Datos básicos"** de cada figura.    1.2. Figuras obligatorias vs opcionales 
- **CA‑04:** Para **Tomador**, el campo debe ser obligatorio y siempre visible. 
- **CA‑05:** Para **Representante Legal**, el campo debe ser obligatorio cuando exista esta figura. 
- **CA‑06:** Para otras figuras (beneficiario, asegurado, pagador, intermediario, apoderado):

- Si el valor viene vacío en la creación de la evaluación, el campo debe mostrarse visible y editable. 
- Si ya existe un valor válido, debe mostrarse en modo lectura o editable según permisos del usuario.      2. Formato y Captura de la Fecha 
- **CA‑07:** La fecha debe digitatarse según el formato estándar de la compañía (por defecto: **DD/MM/AAAA** con máscara). 
- **CA‑08:** El campo debe incluir **selector calendario**. 
- **CA‑09:** Debe impedir el ingreso de valores no numéricos (excepto separador permitido).    3. Validaciones de Consistencia — Persona Natural 
- **CA‑10:** La fecha de nacimiento no puede ser futura; si lo es, el sistema debe bloquear guardado y mostrar mensaje de error. 
- **CA‑11:** El sistema debe validar la **edad mínima** configurada para el producto/canal.

- Valor por defecto: **≥ 18 años para Tomador**.   
- **CA‑12:** El sistema debe validar una **edad máxima razonable** (por defecto ≤ 120 años).

Si se supera, mostrar mensaje de calidad de datos y bloquear guardado. 
- **CA‑13:** Si existe tipo y número de documento, y estos implican rangos etarios (p. ej. cédula de menor), el sistema debe alertar inconsistencias.    4. Validaciones de Consistencia — Persona Jurídica 
- **CA‑14:** La fecha de constitución no puede ser futura. 
- **CA‑15:** No puede ser anterior al umbral parametrizable (por defecto: **01/01/1900**). 
- **CA‑16:** Si existe NIT y CIIU:

- La fecha de constitución no puede ser **posterior** al inicio de la relación contractual registrada (si aplica). 
- Si lo es, se debe generar **warning**, no error.   
- **CA‑17:** Si el producto tiene restricciones de antigüedad para PJ, deben aplicarse reglas parametrizables por ramo.    5. Reglas de obligatoriedad por figura 
- **CA‑18:** Si la figura es Tomador → el sistema no permite guardar si la fecha está vacía. 
- **CA‑19:** Si la figura es Representante Legal → no permite guardar si la fecha está vacía. 
- **CA‑20:** Para figuras opcionales → permite guardar aun si está vacío, siempre que no se haya definido obligatoriedad específica.
