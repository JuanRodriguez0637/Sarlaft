# HU 1082042 — [Formulario]: Requisito opcional "Ingresos y retenciones" -  Back Requisitos

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1057319 — [Formulario]: Cambiar a opcional la solicitud del requisito "Ingresos y retenciones"](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1057319) › HU 1082042 — [Formulario]: Requisito opcional "Ingresos y retenciones" -  Back Requisitos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1082042](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082042) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-19 |
| **Última modificación** | 2026-03-19 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1057319 — [Formulario]: Cambiar a opcional la solicitud del requisito "Ingresos y retenciones"](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1057319)  
  Estado: New  

## Descripción

Yo como negocio sarlaft Quiero: 
- 
Ajustar el modelo de bd, la tabla "tsaf_tipo_requisito" para adicionar un campo de opobligatorio.  
- 
Ajustar en el back en el microservicio de saralftapi, que cuando se consulte la evaluación se indique que requisitos son obligatorios y cuales no (soportes) .  
- 
Ajuste pruebas unitarias  
- 
Ajustar pruebas soapui para los ws del back  
- 
Ajustar api terceros, para que indique que no se requiere el requisito de "Certificado de Ingresos y Retenciones" para PN, es decir indicar la obligatoriedad o no de cada soporte.  
- 
Ajustar el proceso de DeterminarEstadoEvaluacion, para que solo valide los requisitos marcados como obligatorios.  
- 
Ajustar el proceso de integración con el app de requisitos(externo a sarlaft) para que no cree el requisito de "Certificado de Ingresos y Retenciones" de forma inmediata, si no crearlo y actualizarlo en el momento que el usuario lo adjunte.

## Criterios de Aceptación

- 
Ajustar el modelo de bd, la tabla "tsaf_tipo_requisito" para adicionar un campo de opobligatorio.  
- 
Ajustar en el back en el microservicio de saralftapi, que cuando se consulte la evaluación se indique que requisitos son obligatorios y cuales no (soportes) .  
- 
Ajuste pruebas unitarias  
- 
Ajustar pruebas soapui para los ws del back  
- 
Ajustar api terceros, para que indique que no se requiere el requisito de "Certificado de Ingresos y Retenciones" para PN, es decir indicar la obligatoriedad o no de cada soporte.  
- 
Ajustar el proceso de DeterminarEstadoEvaluacion, para que solo valide los requisitos marcados como obligatorios.  
- 
Ajustar el proceso de integración con el app de requisitos(externo a sarlaft) para que no cree el requisito de "Certificado de Ingresos y Retenciones" de forma inmediata, si no crearlo y actualizarlo en el momento que el usuario lo adjunte.
