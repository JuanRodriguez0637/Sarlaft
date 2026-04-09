# HU 1025877 — [Formulario]: Modificar el campo de actividad económica

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1025877 — [Formulario]: Modificar el campo de actividad económica

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1025877](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1025877) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Anticipo; Equipo Base |
| **Creado** | 2026-01-29 |
| **Última modificación** | 2026-02-12 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)  
  Estado: New  

## Descripción

Yo como Analista de SARLAFT
Quiero que el sistema permita buscar y seleccionar la Actividad Económica Principal y la Actividad Económica Secundaria por código y/o nombre, utilizando la clasificación CIIU versión 4 vigente,
Para garantizar la correcta identificación de la actividad económica del cliente, el cumplimiento normativo y la trazabilidad de la información en los procesos de conocimiento del cliente.  
 
 **Alcance / Consideraciones Funcionales** 
- Aplica para: 
- Persona Natural y Persona Jurídica.  
- Formularios asociados a tipos de riesgo:

- Ordinario 
- Intensificado  
- Deben existir dos campos claramente diferenciados: 
- Actividad económica principal (campo obligatorio). 
- Actividad económica secundaria (campo opcional).    
 **Reglas de Negocio** 
- Ambos campos deben utilizar exclusivamente el catálogo oficial CIIU 4 vigente. 
- El sistema debe permitir:

- Buscar por código, nombre o ambos. 
- Visualizar en los resultados el código CIIU + nombre de la actividad.  
- El usuario solo podrá seleccionar actividades existentes en el catálogo (no se permite ingreso manual). 
- La Actividad Económica Principal es obligatoria:

- El sistema debe mostrar un mensaje de obligatoriedad debajo del campo cuando no esté diligenciado. 
- La Actividad Económica Secundaria es opcional.  
- Si el cliente tiene una actividad económica registrada previamente en base de datos, el sistema debe:

- Precargar automáticamente el valor correspondiente en el formulario. 
- Si el cliente no tiene actividad económica registrada, el campo debe mostrarse vacío para su diligenciamiento. 
- Si en la base de datos el cliente tiene registrada una clasificación CIIU versión 3, no debe precargarse automáticamente (Criterio Aceptación) 
- En este caso, el sistema debe solicitar al usuario el diligenciamiento manual de la CIIU 4 vigente. 
- Ambos valores seleccionados deben:

- Guardarse en base de datos de forma estructurada (código y descripción). 
- Ser trazables para efectos de auditoría, seguimiento y control SARLAFT.

## Criterios de Aceptación

1) Disponibilidad y alcance 
CA‑01. Aplicación por tipo de persona y riesgo 
- Dado formularios para Persona Natural y Persona Jurídica de Riesgo Ordinario e Intensificado, 
- Cuando se cargan los formularios, 
- Entonces se muestran dos campos diferenciados:

- Actividad económica principal (obligatoria) 
- Actividad económica secundaria (opcional).    
CA‑02. Catálogo obligatorio CIIU 4 vigente 
- Dado que los campos utilizan catálogo, 
- Cuando el usuario interactúa con cualquiera de los dos campos, 
- Entonces el sistema usa exclusivamente el catálogo oficial CIIU versión 4 vigente para buscar y seleccionar (sin ingreso manual).  2) Búsqueda y selección (UX funcional) 
CA‑03. Búsqueda por código y/o nombre 
- Dado un usuario en el campo de Actividad económica, 
- Cuando ingresa texto o código, 
- Entonces el sistema permite buscar por código, por nombre o por ambos.  
CA‑04. Formato de resultados 
- Dado que se muestran resultados, 
- Cuando la lista de sugerencias aparece, 
- Entonces cada ítem se visualiza como [código CIIU] – [nombre de la actividad].  
CA‑05. Selección restringida al catálogo 
- Dado que el catálogo es controlado, 
- Cuando el usuario intenta escribir un valor libre o no listado, 
- Entonces no puede seleccionarlo; solo se puede elegir una opción existente del catálogo.  3) Reglas de obligatoriedad y validaciones 
CA‑06. Principal obligatoria 
- Dado el campo Actividad económica principal, 
- Cuando el usuario intenta guardar o avanzar sin haber seleccionado un valor, 
- Entonces el sistema bloquea la acción y muestra un mensaje de obligatoriedad debajo del campo.  
CA‑07. Secundaria opcional 
- Dado el campo Actividad económica secundaria, 
- Cuando el usuario decide no diligenciarlo, 
- Entonces el sistema permite guardar y avanzar sin error.  4) Precarga y compatibilidad de versiones 
CA‑08. Precarga cuando existe CIIU 4 
- Dado que en base de datos el cliente ya tiene registrada una actividad económica en CIIU 4, 
- Cuando se abre el formulario, 
- Entonces el sistema precarga automáticamente el valor correspondiente en el/los campo(s) (principal/ secundario, según aplique).  
CA‑09. Sin precarga cuando existe CIIU 3 
- Dado que en base de datos el cliente tiene registrada una clasificación CIIU versión 3, 
- Cuando se abre el formulario, 
- Entonces no se precarga actividad, 
- Y el sistema solicita al usuario diligenciar manualmente (vía catálogo) una actividad en CIIU 4 vigente.  
CA‑10. Campos vacíos si no existe registro previo 
- Dado que el cliente no tiene actividad económica registrada, 
- Cuando se abre el formulario, 
- Entonces los campos se muestran vacíos para su diligenciamiento.  5) Persistencia y estructura de datos 
CA‑11. Almacenamiento estructurado 
- Dado una selección válida en principal y/o secundaria, 
- Cuando el usuario guarda el formulario, 
- Entonces el sistema persiste cada actividad de forma estructurada con código CIIU y descripción (nombre), asociadas al cliente.  
CA‑12. Integridad de catálogos 
- Dado que se almacena código CIIU, 
- Cuando se valida la consistencia, 
- Entonces el código debe existir en el catálogo CIIU 4 vigente; de lo contrario, se rechaza el guardado y se muestra mensaje de error.  6) Trazabilidad y auditoría 
CA‑13. Trazabilidad mínima por cambio 
- Dado una selección o actualización de actividad económica, 
- Cuando se confirma el guardado, 
- Entonces se registra trazabilidad con al menos: cliente, campo afectado (principal/secundaria), código/descr. CIIU, fecha/hora, origen/formulario, responsable (usuario/sistema).  
CA‑14. Consulta de trazabilidad 
- Dado un requerimiento de control o auditoría, 
- Cuando se solicite la evidencia de la actividad económica del cliente, 
- Entonces el sistema permite consultar el histórico de cambios relacionados a estos campos (no editable).  7) Mensajería funcional 
CA‑15. Mensaje de obligatoriedad (principal) 
- Dado que principal es obligatorio, 
- Cuando el usuario no lo diligencia, 
- Entonces se muestra un mensaje claro bajo el campo (p. ej., “La actividad económica principal (CIIU 4) es obligatoria”).  
CA‑16. Mensaje por selección inválida 
- Dado que se intenta guardar con un valor no perteneciente al catálogo, 
- Cuando se valide el formulario, 
- Entonces se muestra un mensaje indicando que debe seleccionarse una actividad del catálogo CIIU 4 vigente.  8) Rendimiento y experiencia mínima (funcional) 
CA‑17. Tiempo de respuesta de búsqueda 
- Dado que el usuario escribe en el campo, 
- Cuando busca por código o nombre, 
- Entonces los resultados deben aparecer en un tiempo razonable para el uso operativo
