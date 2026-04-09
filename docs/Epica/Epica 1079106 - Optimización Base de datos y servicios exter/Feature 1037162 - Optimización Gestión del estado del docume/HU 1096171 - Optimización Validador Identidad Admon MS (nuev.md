# HU 1096171 — [Optimización]:  Validador Identidad Admon MS (nuevo micro Back) - Servicios gestion estado cliente

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1037162 — [Optimización]: Gestión del estado del documento del cliente](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037162) › HU 1096171 — [Optimización]:  Validador Identidad Admon MS (nuevo micro Back) - Servicios gestion estado cliente

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1096171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1096171) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-24 |
| **Última modificación** | 2026-03-24 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1037162 — [Optimización]: Gestión del estado del documento del cliente](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1037162)  
  Estado: New  

## Descripción

Yo como analista sarlaft Quiero: 
- Crear las clases de dominio para la gestión del estado del cliente y la parametria de estados por tipo y vigencia. 
- Crear servicio web para Consultar Clientes por Documento (tipo y nro de documento) donde se filtren los bloqueos/estados de registraduria/migracion/datos basicos/cuestionario que tenga activos. Respuesta paginada por base de datos. 
- Crear servicio web para desactivar un bloqueo o varios bloqueos del cliente  (tipo y nro de documento) en algun bloqueos/estados de registraduria/migracion/datos basicos/cuestionario que tenga activos. 
- Configurar autenticacion/autorizacion con seus, asignar permisos solo a los perfiles indicados 
- Realizar trazas de auditoria en splunk para las actualizaciones. 
- Relizar validaciones de formato y obligatorioedad de los campos 
- Pruebas de soapui, jmeter y programar pruebas de seguridad.

## Criterios de Aceptación

- Crear las clases de dominio para la gestión del estado del cliente y la parametria de estados por tipo y vigencia. 
- Crear servicio web para Consultar Clientes por Documento (tipo y nro de documento) donde se filtren los bloqueos/estados de registraduria/migracion/datos basicos/cuestionario que tenga activos. Respuesta paginada por base de datos. 
- Crear servicio web para desactivar un bloqueo o varios bloqueos del cliente  (tipo y nro de documento) en algun bloqueos/estados de registraduria/migracion/datos basicos/cuestionario que tenga activos. 
- Configurar autenticacion/autorizacion con seus, asignar permisos solo a los perfiles indicados 
- Realizar trazas de auditoria en splunk para las actualizaciones. 
- Relizar validaciones de formato y obligatorioedad de los campos 
- Pruebas de soapui, jmeter y programar pruebas de seguridad.
