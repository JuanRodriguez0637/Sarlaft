# Regresión - SEL Distinto a SOAT

> **Origen:** Contenido extraído del adjunto [Regresion_SEL_distintoSOAT_062024.docx](./attachments/Regresion_SEL_distintoSOAT_062024.docx) de la página [Pruebas de Regresión SARLAFT – SOAT Orden Administrativa](./PruebasRegresionSarlaftSOAT.md)
> **Nota:** Este archivo no corresponde a una página nativa de Confluence.

**APLICATIVO: SEL- DISTINTO A SOAT**

## ESCENARIO 1: Validación exitosa con la registraduría para viajes

| ESCENARIO 1: Validación exitosa con la registraduría para viajes | ESCENARIO 1: Validación exitosa con la registraduría para viajes |
| --- | --- |
| Variables de ingreso | Tomador: E735353 LALE DEMOZ DA SILVA ALDO ANTONIO Asegurado: C32712682 BARRIOS SAMPER ISABEL Asesor: 6886 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Cotización |  |
| Resultado esperado | Diligenciar el formulario ORDINARIO Realizar validación de identidad para el asegurado por EXPERIAN usando OTP Y/O cuestionario Realizar validación de identidad para el tomador por medio de FIRMA REMOTA  Expedir negocio |
| Estado evaluación | Evaluación EXITOSA |

## ESCENARIO 2: Validación exitosa con migración en falla técnica

| ESCENARIO 2: Validación exitosa con migración en falla técnica | ESCENARIO 2: Validación exitosa con migración en falla técnica |
| --- | --- |
| Variables de ingreso | Tomador: Raul Carba CE 297935 Asesor: 6886 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Cotización | 1da547e6-5e22-445b-af9d-b00d2c45c01c |
| Resultado esperado | Ingresar datos básicos para la compra del seguro Validar Sarlaft simplificado y falla técnica en migración por estado del documento en NULL Expedir negocio |
| Estado evaluación | Evaluación EXITOSA |

## ESCENARIO 3: Validación no exitosa por datos errados en registraduría

| ESCENARIO 3: Validación de riesgo simplificado para Arrendamiento | ESCENARIO 3: Validación de riesgo simplificado para Arrendamiento |
| --- | --- |
| Variables de ingreso | Tomador: E735353 LALE DEMOZ DA SILVA ALDO ANTONIO Asegurado: C32712682 BARRIOS SAMPER ISABEL Asesor: 6886 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Cotización |  |
| Resultado esperado | Diligenciar el formulario ORDINARIO Realizar validación de identidad para el asegurado por EXPERIAN usando OTP Y/O cuestionario Realizar validación de identidad para el tomador por medio de FIRMA REMOTA  Expedir negocio |
| Estado evaluación | Evaluación EXITOSA |

**753**

## ESCENARIO 4: Validación de rechazo por PEPS

| ESCENARIO 4: Validación de rechazo por PEPS | ESCENARIO 4: Validación de rechazo por PEPS |
| --- | --- |
| Variables de ingreso | Tomador: Januaria Alcocer Peña Cédula de Ciudadanía: 63456656 Asegurado: Gabino Raul Berrocal Ruiz C78695795 y Heriberto Enrique Ahumada Maury C8666542 Asesor: 6886 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Cotización |  |
| Resultado esperado | Diligenciar el formulario ORDINARIO Realizar validación de identidad para el asegurado por EXPERIAN usando OTP Y/O cuestionario Realizar validación de identidad para el tomador por medio de FIRMA REMOTA  Expedir negocio |
| Estado evaluación | Evaluación EXITOSA |
