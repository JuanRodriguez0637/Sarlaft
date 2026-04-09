# HU 1046415 — Formulario]: Back - Parametrizar los códigos de los requisitos por tipo de sociedad

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288) › HU 1046415 — Formulario]: Back - Parametrizar los códigos de los requisitos por tipo de sociedad

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1046415](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1046415) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-16 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1032288 — [Formulario]: Modificaciones Formulario](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032288)  
  Estado: New  

## Descripción

Yo como Analista Sarlaft 
Quiero que, se parametricen los nuevos códigos de requisitos en la tabla tsaf_tipo_requisito.Parametrizar en el storage account las propiedades documentales de P8 de cada requisito, estas se debes solicitar al equipo de gestión documentales y adicionar campo de usuario que actualiza a la tabla de tsaf_requisito, almacenar el usuario de seus que realiza la carga del documento. En caso de realizarse por api, almacenar el código de aplicación asociado a la evaluación. 
Motor:
- Actualizar el servicio del motor para adicionar los campos de clasificación y tipo de la PJ. 
- Actualizar las reglas de asignación de requisitos para tener en cuenta los campos de clasificación y tipo de la PJ.

## Criterios de Aceptación

**1. Parametrización de nuevos códigos de requisitos en tsaf_tipo_requisito** CA1 – Registro de nuevos códigos Dado que se requieren nuevos códigos de requisito
 Cuando se parametrice la tabla tsaf_tipo_requisito
 Entonces los nuevos códigos deben ser creados con sus atributos obligatorios (código, nombre, estado, vigencia, tipo, clasificación si aplica). CA2 – Validación de duplicados Dado que la tabla contiene requisitos previamente registrados
 Cuando se intente crear un nuevo código
 Entonces el sistema debe validar que no exista un código duplicado
 y en caso de existir, bloquear el registro y emitir mensaje de error. **
** **2. Parametrización de propiedades documentales P8 en Storage Account** CA3 – Propiedades documentales disponibles Dado que cada requisito debe tener asociadas sus propiedades documentales P8
 Cuando se reciban las propiedades desde el equipo de Gestión Documental
 Entonces estas deben ser parametrizadas en el Storage Account según el estándar corporativo. CA4 – Propiedades obligatorias Dado que un requisito tiene propiedades P8 definidas
 Cuando se parametrice en el Storage Account
 Entonces el sistema debe registrar al menos: Tipo documental Serie y subserie Retención Código P8 Metadatos obligatorios Estado **3. Actualización del campo de usuario en tsaf_requisito** CA5 – Registro de usuario SEUS Dado que un documento se carga desde el formulario (interfaz)
 Cuando el usuario realice la carga
 Entonces el sistema debe almacenar en tsaf_requisito el usuario SEUS que realizó la carga. CA6 – Registro por API Dado que la carga del documento se realice mediante API
 Cuando se ejecute el proceso
 Entonces el sistema deberá almacenar: Código de la aplicación asociada a la evaluación Usuario técnico si aplica Identificador de trazabilidad del consumo 
 **4. Actualización del Motor de Reglas** **4.1 Inclusión de campos de clasificación y tipo de PJ** CA7 – Consulta del motor con nuevos campos Dado que una persona jurídica tiene datos de clasificación y tipo
 Cuando el motor procese la evaluación
 Entonces debe incluir y considerar estos campos en la estructura de entrada/salida del servicio. CA8 – Compatibilidad hacia atrás Dado que existen evaluaciones históricas sin los campos nuevos
 Cuando el motor reciba solicitudes de versiones previas
 Entonces no debe fallar y debe manejar los valores ausentes como opcionales. **4.2 Actualización de reglas SARLAFT de asignación de requisitos** CA9 – Reglas actualizadas Dado que las reglas deben asignar requisitos con base en la clasificación y tipo de PJ
 Cuando el motor determine los requisitos aplicables
 Entonces debe considerar obligatoriamente los nuevos campos para: Selección de requisitos Herencia de requisitos Evaluación de obligatoriedad CA10 – Consistencia lógica Dado que un cliente haya sido evaluado previamente
 Cuando se aplique nuevamente la lógica del motor con los campos nuevos
 Entonces la asignación de requisitos debe mantenerse consistente con las reglas aprobadas por SARLAFT. 
 **5. Trazabilidad y Control** CA11 – Registro de auditoría Dado que se parametriza o actualiza un requisito, propiedad documental o regla
 Cuando se ejecute la operación
 Entonces debe almacenarse trazabilidad mínima: Usuario (SEUS o aplicación) Fecha y hora Acción ejecutada Requisito afectado Resultado del proceso CA12 – Pruebas de regresión Dado que el motor fue modificado
 Cuando se habiliten los nuevos campos y reglas
 Entonces las evaluaciones actuales y pasadas deben continuar ejecutándose sin errores.
