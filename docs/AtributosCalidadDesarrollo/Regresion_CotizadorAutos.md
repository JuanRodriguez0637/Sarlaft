# Regresión - Cotizador Autos

**APLICATIVO: ****COTIZADOR AUTOS**

## ESCENARIO 1: Consulta con la registraduría errada por apellido

| ESCENARIO 1: Consulta con la registraduría errada por apellido | ESCENARIO 1: Consulta con la registraduría errada por apellido |
| --- | --- |
| Variables de ingreso | Tomador: Olga Mabel Zapata Henao Cédula de Ciudadanía: 24098380 Asesor: 6886 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Cotización | 04006886240612706895 |
| Resultado esperado | Se rechaza la evaluación pues el apellido esta errado y la consulta con la registraduría es RECHAZADA. |
| Estado evaluación | Evaluación RECHAZADA |

## ESCENARIO 2: Validación de identidad exitosa para el riesgo intensificado

| ESCENARIO 2: Validación de identidad exitosa para el riesgo intensificado | ESCENARIO 2: Validación de identidad exitosa para el riesgo intensificado |
| --- | --- |
| Variables de ingreso | Tomador: C 71703142 MARIN SANCHEZ NELSON DE JESUS Asesor: 6886 Persona natural Marcar cliente PEP para riesgo INTENSIFICADO |
| Cotización | 04006886240612074313 |
| Resultado esperado | Diligenciar formulario de riesgo INTENSIFICADO Levantar el control PEP Rechazar validación de identidad por medio de FIRMA REMOTA Realizar validación de identidad exitosa por EXPRIAN |
| Estado evaluación | Evaluación RECHAZADA |

## ESCENARIO 3: Consulta con la registraduría en falla técnica

| ESCENARIO 3: Consulta con la registraduría en falla técnica | ESCENARIO 3: Consulta con la registraduría en falla técnica |
| --- | --- |
| Variables de ingreso | Tomador: Jorge Angel Marin Penagos Cédula de Ciudadanía: 17128750 Asesor: 6886 Persona natural Valores asegurados del riesgo SIMPLIFICADO |
| Cotización | 04006886240612128593 |
| Resultado esperado | Envío de solicitud de FIRMA REMOTA No habilita formulario por riesgo simplificado Consulta con la registraduría en FALLA TÉCNICA |
| Estado evaluación | Evaluación EXITOSA |
