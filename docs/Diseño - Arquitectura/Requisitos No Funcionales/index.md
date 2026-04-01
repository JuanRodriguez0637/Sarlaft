# Requisitos No Funcionales

> **Fuente Confluence:** [Requisitos No Funcionales](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1804927175/Requisitos+No+Funcionales)  
> **Última modificación:** 2021-03-26 — Diana Muñoz · versión 2  
> **Sección:** [Requisitos No Funcionales](./index.md)

El aplicativo de Sarlaft 4.0 esta desarrollado con una arquitectura cuyos drivers de calidad, corresponden a los siguientes atributos de calidad

[https://miro.com/app/board/o9J_lWUU2no=/?utm_source=notification&utm_medium=email&utm_campaign=daily-updates&utm_content=go-to-board](https://miro.com/app/board/o9J_lWUU2no=/?utm_source=notification&utm_medium=email&utm_campaign=daily-updates&utm_content=go-to-board) 

 

| CRÍTICOS | Escalabilidad | El aplicativo de Sarlaft será incorporado como un paso obligatorio en los procesos de expedición, renovación y reclamación en todos los productos o ramos de Seguros obligatorios y voluntarios y por ende, debe ser capaz de atender todas las solicitudes que se reciban de las aplicaciones de negocio que se integren con el aplicativo de Sarlaft. |
| --- | --- | --- |
| Disponinibilidad | Se requiere disponibilidad 24/7 para cubrir las disponibilidades que tienen las aplicaciones de negocio que usarían el aplicativo de Sarlaft. |
| Interoperabilidad | El aplicativo de Sarlaft se integrará con múltiples plataformas de negocio por lo cual se debe contar con un API de servicios que permita consumir la experiencia de Sarlaft en todas las aplicaciones de negocio que requieran usar la plataforma. |
| Seguridad | Sarlaft solicitará y almacenará información sensible de los clientes la cual se debe proteger por medio de control de acceso a usuarios no autorizados, cifrado   y encriptación de datos durante el tránsito y en reposo. |
| Integridad de la Información | Se debe garantizar la consistencia de la información recolectada de los clientes según las disposiciones de la Superintendencia Financiera para evitar consecuencias negativas por auditorias que  la Superintendencia pueda realizar a la implementación de Sarlaft 4.0 |
| Modularidad | El aplicativo de Sarlaft debe contar con mecanismo de protección contra el impacto sobre cambios externos, generalmente solicitados por la Superintendencia Financiera de Colombia. |
| NO CRÍTICOS | Operabilidad | El aplicativo de Sarlaft debe contar mecanismos de autogestión para el 90% o más de las tareas de mantenimiento, se puedan hacer vía parametrización delegada a los usuarios funcionales. |
| Auditabilidad | Todas las transacciones que se realicen el aplicativo de Sarlaft, deben ser auditadas indicando la fecha de operación, tipo de operación y usuario que ejecuta la operación |
| Idoneidad Funcional | El aplicativo de Sarlaft debe implementar todos los requisitos funcionales necesarios para lograr la implementación del Sarlaft en la organización y cumplir las disposiciones legales de la superintendencia financiera de Colombia. |
| Flexibilidad de la UI | La experiencia del usuario de Sarlaft debe estar enriquecida con controles interactivos y flujo de navegación amigable que faciliten al máximo el uso del aplicativo. |