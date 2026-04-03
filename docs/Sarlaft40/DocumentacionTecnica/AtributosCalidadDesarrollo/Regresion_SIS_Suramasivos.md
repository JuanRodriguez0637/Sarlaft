# Regresión - SIS y Suramasivos

> **Origen:** Contenido extraído del adjunto [Regresion_SIS_Suramasivos_062024.docx](./attachments/Regresion_SIS_Suramasivos_062024.docx) de la página [Pruebas de Regresión SARLAFT – SOAT Orden Administrativa](./PruebasRegresionSarlaftSOAT.md)
> **Nota:** Este archivo no corresponde a una página nativa de Confluence.

**Escenarios regresión Suramasivos**

| ESCENARIO 1 | ESCENARIO 1 |
| --- | --- |
| Variables de ingreso | Tomador: CE 154545 Miguel Moly Asesor: 4999 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Resultado esperado | No es posible continuar con el proceso. La validación del documento de identidad con Registraduría Nacional (cédula de ciudadanía) o Migración Colombia (C. Extranjería, Permiso Especial de Permanencia o Permiso por Protección Temporal) no ha sido exitosa |
| Estado evaluación | Evaluación rechazada |
| Evidencia (PANTALLAZO) |  |

| ESCENARIO 2 | ESCENARIO 2 |
| --- | --- |
| Variables de ingreso | Tomador: Cédula 9476542 Alexander Fredy Vega Rocha Asesor: 4999 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Resultado esperado | Expedir negocio |
| Estado evaluación | Evaluación Exitosa |
| Evidencia (PANTALLAZO) |  |

El escenario exitoso con ese documento del escenario no funciona. Se realiza escenario con documento cedula #

| 1081801364 | ARIAS | RODRIGUEZ | VICTOR HUGO |
| --- | --- | --- | --- |

CORESEG000367028

Escenario exitoso documento:
Pasaporte con país Colombia 1989999265

Se corrige el país y el sistema permite la expedición:

| ESCENARIO 3 | ESCENARIO 3 |
| --- | --- |
| Variables de ingreso | Tomador: PAV1727 JULIAN ORTIZ YAN Asesor: 4999 Persona natural País: Irán Valores asegurados del riesgo SIMPLIFICADO |
| Resultado esperado | No cumple con políticas de SARLAFT. El país de nacimiento/constitución del cliente PAV1727 pertenece a la lista GAFI y no es objetivo para la compañía. |
| Estado evaluación | Evaluación rechazada |
| Evidencia (PANTALLAZO) |  |

El tipo de documento del escenario no lo maneja el canal, se realiza escenario con el documento cédula #80023144 que está marcado como PEP

Posteriormente, se selecciona el país de nacimiento Iran y también se evidencia el control:

EVIDENCIAS SIS
