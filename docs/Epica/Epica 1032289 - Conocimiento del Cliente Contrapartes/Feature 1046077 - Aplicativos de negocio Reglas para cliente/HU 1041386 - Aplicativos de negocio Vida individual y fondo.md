# HU 1041386 — [Aplicativos de negocio]: Vida individual y fondo de ahorro - API

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1046077 — [Aplicativos de negocio]: Reglas para clientes de Vida Individual con Fondo de Ahorro](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046077) › HU 1041386 — [Aplicativos de negocio]: Vida individual y fondo de ahorro - API

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1041386](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041386) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-11 |
| **Última modificación** | 2026-03-13 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1046077 — [Aplicativos de negocio]: Reglas para clientes de Vida Individual con Fondo de Ahorro](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046077)  
  Estado: New  

## Descripción

Como analista SARLAFT, quiero que en la creación de la evaluación se incluya un campo llamado “Fondo de ahorro” en la sección de póliza, para identificar si la póliza pertenece o no a un fondo de ahorro y aplicar las reglas de asignación del tipo de riesgo correspondientes. 
 **Alcance** En la sección **Póliza** de la creación de evaluación SARLAFT (Negocio nuevo y Reclamaciones), el sistema debe mostrar un nuevo campo llamado **“Fondo de ahorro”**. 
Características del campo: 
- Tipo: Selección Sí/No. No se recibe Null, NULL o Vacío en la respuesta. 
- El campo es opcional. Se debe recibir una respuesta.  
- Solo se usa para la asignación del tipo de riesgo cuando el ramo de la póliza sea 080 o 081 (Vida Individual). 
- Guardar el registro de la evaluación con la respuesta del campo "Fondo de ahorro" y la asignación del riesgo definida.  
Cuando se haya seleccionado el ramo y el campo “Fondo de ahorro”, el sistema debe aplicar las reglas de asignación del riesgo descritas a continuación: Regla 1 — Visibilidad y uso del campo 
- El campo Fondo de ahorro debe aparecer siempre en la sección de póliza. 
- El campo es opcional y el aplicativo puede enviar Sí o No.    Regla 2 — Asignación del tipo de riesgo según ramo y respuesta 
Las reglas aplican solo si el ramo de la póliza es 080 o 081 (Vida Individual) y la figura del tomador: 
- Si el campo “Fondo de ahorro” = “Sí” 
- El sistema debe asignar el tipo de riesgo Ordinario y tipo de formulario ordinario.
  
- La regla debe priorizarse sobre de las reglas generales de asignación del riesgo ordinario
 
- Si el riesgo del tomador es intensificado y el campo "Fondo de ahorro" = Si", se mantiene en intensificado 
- Si el riesgo del tomador es "Simplificado" y el campo "Fondo de ahorro" = Si", sube al riesgo ordinario  
- Si el campo “Fondo de ahorro” = “No” 
- El sistema debe continuar con el flujo normal de asignación del riesgo, según las reglas generales del proceso SARLAFT.     Regla 3 — Ramos diferentes a 080 y 081 
- Si el ramo** no** es 080 ni 081, el sistema no debe considerar el campo “Fondo de ahorro” para asignar el riesgo. 
- La asignación deberá realizarse según las reglas generales.

## Criterios de Aceptación

**1. Visualización y comportamiento general del campo**  
- El sistema debe mostrar el campo **“Fondo de ahorro”** en la sección *Póliza* de la creación de evaluación tanto para **Negocio Nuevo** como para **Reclamaciones**. 
- El campo debe permitir seleccionar únicamente **Sí** o **No**.  
- El campo es **opcional**, pero el sistema debe recibir una respuesta válida (Sí o No), sin permitir valores nulos, vacíos o NULL. 
- El campo debe ser visible sin importar el tipo de ramo seleccionado.     **2. Reglas cuando el ramo es 080 o 081 (Vida Individual)**  
Cuando el ramo es **080** o **081**, el sistema debe utilizar el valor del campo para asignar el tipo de riesgo: **2.1. Si “Fondo de ahorro” = “Sí”** 
- El sistema debe asignar el tipo de riesgo **Ordinario**. 
- El sistema debe asignar el **formulario ordinario**. 
- Esta asignación debe tener **prioridad sobre las reglas generales** de asignación del riesgo. 
- Si el tomador tenía riesgo **Intensificado**, este se mantiene en **Intensificado** aunque el campo “Fondo de ahorro” sea “Sí”. 
- Si el tomador tenía riesgo **Simplificado**, el sistema debe cambiarlo a **Ordinario** cuando el campo sea “Sí”.  **2.2. Si “Fondo de ahorro” = “No”** 
- El sistema debe continuar con el **flujo normal de asignación del riesgo**, aplicando las reglas generales del proceso SARLAFT. 
- El sistema no debe realizar ajustes especiales derivados del campo “Fondo de ahorro”.     **3. Reglas cuando el ramo NO es 080 ni 081**  
- El sistema **no debe usar** el valor del campo “Fondo de ahorro” para calcular el tipo de riesgo. 
- La asignación del riesgo debe seguir únicamente las **reglas generales** definidas por SARLAFT.     **4. Registro y trazabilidad**  
- El sistema debe guardar en la evaluación el valor seleccionado en el campo “Fondo de ahorro”. 
- El sistema debe registrar en los **logs de auditoría** la respuesta enviada y el tipo de riesgo asignado como resultado. 
- La decisión del tipo de riesgo debe quedar trazada con la regla aplicada (según ramo y respuesta del campo).     **5. Integridad funcional del flujo**  
- El sistema debe impedir que se envíen valores nulos, vacíos o no válidos en el campo “Fondo de ahorro”.  
- El sistema debe permitir continuar con la evaluación sin necesariamente seleccionar el campo, siempre que el aplicativo envíe una respuesta válida. 
- La asignación del tipo de riesgo debe producirse únicamente cuando se cuente con el ramo, el valor del campo y el resto de datos obligatorios del flujo.
