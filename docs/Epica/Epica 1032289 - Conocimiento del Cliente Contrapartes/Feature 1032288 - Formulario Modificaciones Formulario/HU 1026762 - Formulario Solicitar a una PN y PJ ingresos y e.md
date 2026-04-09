# HU 1026762 — [Formulario]: Solicitar a una PN y PJ ingresos y egresos

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1026762 — [Formulario]: Solicitar a una PN y PJ ingresos y egresos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1026762](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026762) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-01-29 |
| **Última modificación** | 2026-02-12 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)  
  Estado: New  

## Descripción

**** Como Analista SARLAFT**  Quiero que el formulario de datos financieros permita capturar y actualizar los valores de Ingresos y Egresos del clientePara contar con información financiera completa, consistente y vigente que soporte los análisis de conocimiento del cliente y el cumplimiento normativo.  
 Incorporación de campos:**
 
Se deben adicionar los campos Ingresos y Egresos en la sección de Datos
financieros del formulario de Persona Jurídica. Tipo de dato: Los campos Ingresos y Egresos deben aceptar únicamente valores numéricos. Validaciones de entrada: No se permite el ingreso de letras, caracteres
especiales ni símbolos en los campos Ingresos y Egresos. Solo se aceptan números. Los campos son obligatorios Nota: El texto debe mostrarse cuando el usuario
interactúe con el campo o al intentar avanzar sin diligenciarlo correctamente,
siguiendo la experiencia definida.  
 **Alcance por tipo de formulario:**
 
- 
La funcionalidad aplica para los formularios de Persona Jurídica y Natural en los tipos
Ordinario e Intensificado. 
- Persistencia de datos: 
- 
Los valores ingresados en los campos Ingresos y Egresos deben ser almacenados
en la base de datos.    **Visualización condicional según base de datos:** 
 
  
- Si
      el valor no existe en la base de datos, el sistema debe solicitarlo al
      usuario en el formulario. 
- Si
      el valor ya existe, el sistema debe mostrarlo de manera prellenada al
      usuario.   
  
 **Actualización de datos:**
 
- 
Cuando existan valores previamente almacenados, el usuario debe poder
modificarlos y guardarlos nuevamente en la base de datos.   **Experiencia de usuario:**
 
- 
La visualización, ubicación, diseño, validaciones y comportamiento de los
campos Ingresos y Egresos deben seguir estrictamente la experiencia definida en
la imagen adjunta.   **Alcance operacional:**
 
- 
Una vez esta modificación entre en operación, no se realizará recolección
retroactiva de información para clientes de Persona Jurídica que no tengan
registrado el dato. Solo se almacenará la información nueva que se capture a
partir de la salida a producción.   **Histórico:**
 
- 
No se requiere gestionar histórico de los campos Ingresos y Egresos.

## Criterios de Aceptación

1. Alcance y visibilidad de la funcionalidad CA‑01 Inclusión de campos en formularios aplicables 
**Dado** un formulario de **Persona Jurídica**
**Cuando** el formulario corresponde a un tipo **Ordinario** o **Intensificado**
**Entonces** el sistema muestra los campos **Ingresos** y **Egresos** en la sección **Datos financieros**. CA‑02 Exclusión de otros tipos de persona 
**Dado** un formulario de **Persona Natural**
**Cuando** se visualiza la sección **Datos financieros**
**Entonces** los campos **Ingresos** y **Egresos** **no** se muestran. 2. Tipo de dato y validaciones de entrada CA‑03 Tipo de dato permitido 
**Dado** los campos **Ingresos** y **Egresos**
**Cuando** el usuario ingresa información
**Entonces** el sistema acepta **únicamente valores numéricos**. CA‑04 Restricción de caracteres no permitidos 
**Dado** los campos **Ingresos** y **Egresos**
**Cuando** el usuario intenta ingresar letras, caracteres especiales o símbolos
**Entonces** el sistema **no permite** el ingreso
**Y** muestra una validación visible conforme a la experiencia definida. CA‑05 Obligatoriedad de los campos 
**Dado** el formulario de Persona Jurídica Ordinario o Intensificado
**Cuando** el usuario intenta **guardar o avanzar** sin diligenciar **Ingresos** o **Egresos**
**Entonces** el sistema **bloquea la acción**
**Y** muestra el mensaje de obligatoriedad correspondiente a cada campo. CA‑06 Momento de visualización del mensaje 
**Dado** los campos **Ingresos** y **Egresos**
**Cuando** el usuario interactúa con el campo o intenta avanzar sin diligenciarlo correctamente
**Entonces** el mensaje de validación se muestra **en el momento adecuado**, siguiendo estrictamente la **experiencia definida en la imagen adjunta**. 3. Visualización condicional y precarga CA‑07 Campos sin información previa 
**Dado** un cliente Persona Jurídica **sin valores registrados** de Ingresos y Egresos
**Cuando** se carga el formulario
**Entonces** el sistema muestra los campos **vacíos**
**Y** solicita obligatoriamente su diligenciamiento. CA‑08 Precarga de información existente 
**Dado** un cliente Persona Jurídica con valores **previamente almacenados**
**Cuando** se carga el formulario
**Entonces** el sistema **precarga automáticamente** los valores de **Ingresos** y **Egresos**
**Y** permite su edición. 4. Actualización y persistencia de la información CA‑09 Actualización de valores existentes 
**Dado** que los campos **Ingresos** y **Egresos** contienen valores precargados
**Cuando** el usuario modifica uno o ambos valores y guarda el formulario
**Entonces** el sistema **actualiza** la información en la base de datos, reemplazando los valores anteriores. CA‑10 Almacenamiento en base de datos 
**Dado** valores válidos ingresados en **Ingresos** y **Egresos**
**Cuando** el usuario guarda el formulario
**Entonces** el sistema **almacena los valores** en la base de datos asociados al cliente. 5. Experiencia de usuario (UX) CA‑11 Cumplimiento estricto de la experiencia definida 
**Dado** la visualización de los campos **Ingresos** y **Egresos**
**Cuando** el usuario interactúa con ellos
**Entonces** su **ubicación, diseño, textos, validaciones visibles y comportamiento** cumplen estrictamente con la experiencia definida en la **imagen de interfaz de usuario adjunta**. 6. Alcance operacional (puesta en producción) CA‑12 Recolección a partir de salida a producción 
**Dado** que la funcionalidad entra en operación
**Cuando** se diligencian los campos **Ingresos** y **Egresos**
**Entonces** el sistema **solo almacena información capturada a partir de la salida a producción**
**Y** no realiza recolección retroactiva para clientes Persona Jurídica sin dato previo. 7. Gestión de histórico CA‑13 Sin gestión de histórico 
**Dado** una actualización de los campos **Ingresos** y **Egresos**
**Cuando** se guarda la información
**Entonces** el sistema conserva **únicamente el último valor vigente**
**Y** no gestiona histórico de modificaciones.
