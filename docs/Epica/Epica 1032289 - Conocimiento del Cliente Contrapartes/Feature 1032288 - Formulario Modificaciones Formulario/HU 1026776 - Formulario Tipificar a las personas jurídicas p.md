# HU 1026776 — [Formulario]: Tipificar a las personas jurídicas por tipo de sociedad

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1026776 — [Formulario]: Tipificar a las personas jurídicas por tipo de sociedad

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1026776](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026776) |
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

Como Analista SARLAFT
 Quiero que el sistema tipifique automáticamente a las Personas Jurídicas por tipo de sociedad y clasificación, a partir del análisis de la razón social registrada
Para asegurar una identificación consistente del tipo societario del cliente, soportar correctamente los procesos de conocimiento del cliente y fortalecer el análisis de riesgo, sin depender de una tipificación manual. 
  
**Tipificar a las empresas por tipo de
sociedad**

- Cuando se esté evaluando una Persona Jurídica (en
cualquier formulario, flujo o etapa donde exista este tipo de cliente), el
sistema debe tipificar automáticamente el tipo de sociedad y su clasificación
con base en la razón social registrada. 
- La identificación debe realizarse aplicando las
reglas de coincidencia de denominaciones definidas, priorizando coincidencias
exactas por fragmento. 
- El
sistema debe analizar la razón social de la Persona Jurídica y buscar
coincidencias con las denominaciones establecidas para identificar:  
- Clasificación  
- Tipo
de sociedad   
**Reglas de elección** Si existen múltiples
coincidencias:
 
- Seleccionar
     la coincidencia más específica. 
- Si
     persiste empate, generar un log con las inconsistencias. Luego,
     permitir actualizar el tipo de sociedad correcto. 
- Si
     no existe coincidencia, asignar: 
- Clasificación:
“Otros” 
- Tipo
de Sociedad: “Otros”  
- Los
casos tipificado como “otros” debe crearse un archivo que permita realizar
validación de la tipificación asignada.  **Catálogo de coincidencias por denominación** 
- La identificación debe realizarse con base en la matriz
completa de denominaciones, que incluye: 
- Sociedad
comercial 
- Estructuras
sin personería jurídica 
- Empresas
sin ánimo de lucro 
- Entidad
estatal 
- Otros    **
** **Sociedad comercial**​
 
 
  
  
**Tipo
  de sociedad** 
  
  
  
**Denominaciones** 
  
 
 
  
  
**Sociedad
  Anónima** 
  
  
  
"S.A.", "SA", "S.A",
  "SA." 
  
 
 
  
  
**Sociedad
  por Acciones Simplificada (S.A.S.)** 
  
  
  
"S.A.S.", "SAS", "S.AS",
  "S.A.S", "S.AS.", "SAS.", "SA.S",
  "SA.S." 
  
 
 
  
  
**Sociedad
  Limitada** 
  
  
  
"LTDA.", "Limitada", "LTDA" 
  
 
 
  
  
**Sociedad
  Unipersonal (E.U.)** 
  
  
  
"Empresa Unipersonal", "E.U.",
  "EU", "E.U", "EU." 
  
 
 
  
  
**Colectiva** 
  
  
  
"& Cía.", "& Compañía",
  "Hnos.", "Hermanos", "e Hijos" 
  
 
 
  
  
**En
  comandita simple** 
  
  
  
"S. en C.", "S en C", "S. en
  C", "S en C." 
  
 
 
  
  
**En
  comandita por acciones (S.C.A.)** 
  
  
  
"S.C.A.", "S.C.A", "S.CA",
  "S.CA.", "SC.A.", "SC.A", "SCA",
  "SCA." 
  
 
   **Estructura sin personería jurídica** 
 
  
  
**Tipo** 
  
  
  
**Denominaciones** 
  
 
 
  
  
**Patrimonio
  autónomo / Fiducia** 
  
  
  
"Fiducia", "Fiduciaria",
  "Fide", "Fidu", "Fideicomisos",
  "Fideicomiso" 
  
 
 
  
  
**Fondos
  de capital privado (FCP)** 
  
  
  
"Fondo" 
  
 
 
  
  
**Fondos
  de inversión colectiva (FIC)** 
  
  
  
"Fondo" 
  
 
 
  
  
**Fondos
  de deuda pública** 
  
  
  
"Fondo" 
  
 
 
  
  
**Fondos
  de pensiones y cesantías** 
  
  
  
"Fondo" 
  
 
 
  
  
**Consorcio** 
  
  
  
"Consorcio" 
  
 
 
  
  
**Unión
  temporal (UT)** 
  
  
  
"Unión temporal" 
  
   **
** ** ****Empresas sin ánimo de
lucro** 
 
  
  
**Tipo** 
  
  
  
**Denominaciones** 
  
 
 
  
  
**Cooperativas** 
  
  
  
"Coop", "Cooperativa",
  "Cooperativas" 
  
 
 
  
  
**Asociaciones** 
  
  
  
"Aso", "Asoas",
  "Asociacione" 
  
 
 
  
  
**Iglesias
  católicas** 
  
  
  
"Iglesia", "Parroquia",
  "Capilla", "Basílica", "Catedral" 
  
 
 
  
  
**Propiedad
  horizontal / asociaciones similares** 
  
  
  
"Unidad residencial", "Unidad resid",
  "Conjunto", "Residencial", "Edificio",
  "Unidad", "Urbanización", "Urbaniz",
  "Manzana" 
  
 
 
  
  
**Fondo
  de empleados** 
  
  
  
"Fondo mutuo", "F.M.I." 
  
 
 
  
  
**Corporaciones/Asociaciones
  tipo caja** 
  
  
  
"Caja", "Caja de", "Caja de
  compensación" 
  
 
 
  
  
**Fundaciones** 
  
  
  
"Fundación" 
  
 
 
  
  
**Organización
  no gubernamental** 
  
  
  
"ONG", "Organización" 
  
 
** **  **Entidad estatal** **
** 
 
  
  
**Tipo** 
  
  
  
**Denominaciones** 
  
 
 
  
  
**Colegios
  y universidades públicas** 
  
  
  
"Colegio", "Institución",
  "Universidad" 
  
 
 
  
  
**Entidades
  públicas** 
  
  
  
"Alcaldía", "Municipio",
  "Departamento", "Cámara", "Fiscalía",
  "Policía", "Ministerio", "Corporación",
  "Municipal", "Departamental", "Tribunal",
  "Aeropuerto", "Lotería", "Plaza de",
  "Terminal", "E.S.P.", "Contraloría",
  "Procuraduría", "Juzgado", "Notaría",
  "Superintendencia", "Registraduría", "Senado" 
  
 
 
  
  
**Empresas
  sociales del estado (E.S.E.)** 
  
  
  
"E.S.E.", "ESE" 
  
 
** **  
 **Alcance operacional:**
 
- 
Una vez esta modificación entre en operación, no se realizará tipificación
retroactiva de las personas jurídicas guardadas en la base de datos. 
- Campos actualizados automáticamente: El sistema debe llenar automáticamente los campos: Clasificación y Tipo de Sociedad 
- Edición: No se permite edición del campo una vez haya sido tipificado.

## Criterios de Aceptación

1. Alcance y activación del proceso CA‑01 Aplicación a Persona Jurídica 
**Dado** que el cliente es una **Persona Jurídica**
**Cuando** el cliente es evaluado en **cualquier formulario, flujo o etapa** del sistema
**Entonces** el sistema ejecuta automáticamente el proceso de **tipificación por tipo de sociedad y clasificación**. CA‑02 Ejecución automática 
**Dado** una Persona Jurídica con razón social registrada
**Cuando** el sistema procesa la información del cliente
**Entonces** la tipificación se realiza **de forma automática**, sin intervención manual del usuario. 2. Análisis de la razón social CA‑03 Uso de la razón social como insumo 
**Dado** una Persona Jurídica
**Cuando** se ejecuta la tipificación
**Entonces** el sistema analiza la **razón social registrada** como único insumo para identificar: 
- Clasificación 
- Tipo de sociedad.  CA‑04 Uso del catálogo de denominaciones 
**Dado** el proceso de análisis
**Cuando** se realiza la identificación
**Entonces** el sistema utiliza **exclusivamente** la **matriz completa de denominaciones definida**, que incluye: 
- Sociedad comercial 
- Estructuras sin personería jurídica 
- Empresas sin ánimo de lucro 
- Entidad estatal 
- Otros.  3. Reglas de coincidencia CA‑05 Coincidencia por denominación 
**Dado** la razón social del cliente
**Cuando** se evalúa contra la matriz de denominaciones
**Entonces** el sistema identifica coincidencias por **fragmentos de texto** contenidos en la razón social. CA‑06 Priorización de coincidencias exactas por fragmento 
**Dado** que existen coincidencias posibles
**Cuando** se evalúan los resultados
**Entonces** el sistema **prioriza las coincidencias exactas por fragmento** sobre coincidencias parciales o genéricas. 4. Reglas de elección del resultado CA‑07 Selección de coincidencia más específica 
**Dado** que existen **múltiples coincidencias** válidas
**Cuando** el sistema selecciona el resultado
**Entonces** se asigna la coincidencia **más específica** según la definición del catálogo. CA‑08 Manejo de empates 
**Dado** que persiste un empate entre coincidencias
**Cuando** el sistema no puede determinar una única tipificación
**Entonces**: 
- Se genera un **log** registrando la inconsistencia 
- Se permite la **actualización posterior del tipo de sociedad correcto**.  CA‑09 Ausencia de coincidencias 
**Dado** que no se identifica ninguna coincidencia en la razón social
**Cuando** finaliza el análisis
**Entonces** el sistema asigna automáticamente: 
- **Clasificación:** “Otros” 
- **Tipo de sociedad:** “Otros”.  5. Gestión de casos “Otros” CA‑10 Registro de tipificaciones “Otros” 
**Dado** un cliente tipificado como **Clasificación = Otros** y **Tipo de sociedad = Otros**
**Cuando** se completa el proceso
**Entonces** el sistema incluye el registro en un **archivo de validación** para revisión posterior. CA‑11 Contenido del archivo de validación 
**Dado** el archivo de validación de casos “Otros”
**Cuando** se genera
**Entonces** el archivo contiene información suficiente para permitir la **validación de la tipificación asignada**. 6. Persistencia y uso del resultado CA‑12 Almacenamiento del resultado 
**Dado** una tipificación exitosa
**Cuando** el sistema finaliza el proceso
**Entonces** la **clasificación** y el **tipo de sociedad** quedan almacenados y asociados al cliente. CA‑13 Disponibilidad para procesos SARLAFT 
**Dado** un cliente tipificado
**Cuando** se ejecutan procesos posteriores de conocimiento del cliente o análisis SARLAFT
**Entonces** el sistema utiliza la **tipificación asignada** como insumo válido. 7. Trazabilidad y control CA‑14 Trazabilidad de la tipificación 
**Dado** un proceso de tipificación ejecutado
**Cuando** se almacena el resultado
**Entonces** el sistema conserva trazabilidad que permita identificar como mínimo: 
- Razón social analizada 
- Regla o denominación aplicada 
- Resultado de la tipificación 
- Fecha y hora del proceso 
- Origen del proceso (sistema).  CA‑15 No dependencia de intervención manual 
**Dado** la ejecución del proceso
**Cuando** se tipifica una Persona Jurídica
**Entonces** la tipificación **no depende** de una selección manual inicial por parte del usuario.
