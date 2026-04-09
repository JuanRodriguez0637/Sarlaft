# HU 1076668 — [Optimización]: Depuración evaluaciones BD Sarlaft -  Onboarding y Configuracion Datafactory

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1035141 — [Optimización]: Depuración evaluaciones BD Sarlaft - Proceso automático](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141) › HU 1076668 — [Optimización]: Depuración evaluaciones BD Sarlaft -  Onboarding y Configuracion Datafactory

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1076668](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1076668) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-03-16 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1035141 — [Optimización]: Depuración evaluaciones BD Sarlaft - Proceso automático](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035141)  
  Estado: New  

## Descripción

Como Analista SARLAFT
  quiero que se realice un Onboarding y Configuracion Datafactory para depuración evaluaciones BD Sarlaft para: 
- Aprendizaje y contextualizacion de azure datafactory 
- Limpieza de linked services en datafactory y actualización de los mismos para integrarse con la base de datos de east y west de sarlaft4, utilizando keyvault para las 
- urls de conexión, sobre todo host, usuario y password 
- Configuración de pipelines de despliegue entre desarrollo, laboratorio y producción.

## Criterios de Aceptación

**** **CA1 – Onboarding y contextualización de Azure Data Factory** 
- Se debe realizar una sesión de onboarding donde se explique arquitectura, componentes y usos relevantes de Azure Data Factory para SARLAFT. 
- Se debe entregar material, diagramas o documentación que permita la contextualización del proceso de depuración de evaluaciones SARLAFT dentro de ADF. 
- El Analista SARLAFT debe poder identificar los elementos clave del Data Factory (pipelines, datasets, linked services, triggers) al finalizar la sesión.  **CA2 – Limpieza y actualización de linked services** 
- Los linked services existentes deben ser revisados, eliminando configuraciones obsoletas o duplicadas. 
- Deben actualizarse los linked services necesarios para conectar ADF con las bases de datos east y west de sarlaft4. 
- Las credenciales (host, usuario, password) no deben quedar en texto plano; deben almacenarse en Azure KeyVault. 
- Los linked services actualizados deben usar referencias a KeyVault para todas las URLs y secretos de conexión. 
- Se debe validar conectividad exitosa entre ADF y las bases de datos sarlaft4 east y west.  **CA3 – Integración con KeyVault** 
- El Data Factory debe tener permisos adecuados (RBAC / políticas de acceso) para consultar secretos en KeyVault. 
- Todos los secretos utilizados en las conexiones deben estar incluidos en KeyVault antes del despliegue. 
- Se debe probar que los pipelines acceden correctamente a los secretos sin errores de autenticación.  **CA4 – Configuración de pipelines de despliegue** 
- Se debe configurar el flujo de despliegue entre ambientes: desarrollo → laboratorio → producción. 
- La promoción entre ambientes debe realizarse de forma controlada, manteniendo las referencias a KeyVault en cada entorno. 
- Los pipelines configurados deben ejecutar correctamente en cada ambiente, sin requerir ajustes manuales. 
- La estructura de carpetas, naming y versionamiento debe quedar documentada para uso del equipo SARLAFT.  **CA5 – Validación funcional del proceso** 
- Los pipelines deben ejecutarse exitosamente usando las conexiones actualizadas. 
- Se debe comprobar que las evaluaciones SARLAFT reciben la información depurada conforme a la configuración realizada. 
- Los logs de ejecución deben ser consultables y trazables por el Analista SARLAFT.  **CA6 – Entregables finales** 
- Debe entregarse un documento o wiki con:

- Arquitectura de Data Factory para SARLAFT. 
- Linked services vigentes y su integración con KeyVault. 
- Flujo de despliegue entre entornos (dev–lab–prod). 
- Recomendaciones de operación y mantenimiento.   
- Debe quedar evidencia del onboarding realizado y de las pruebas funcionales.
