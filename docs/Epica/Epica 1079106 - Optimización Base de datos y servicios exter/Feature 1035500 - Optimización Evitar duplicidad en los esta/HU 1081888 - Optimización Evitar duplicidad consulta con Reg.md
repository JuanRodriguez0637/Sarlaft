# HU 1081888 — [Optimización]: Evitar duplicidad consulta con Registraduría - Front -  ValidadorIdentidad MS

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1035500 — [Optimización]: Evitar duplicidad en los estados de la consulta con Registraduría](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035500) › HU 1081888 — [Optimización]: Evitar duplicidad consulta con Registraduría - Front -  ValidadorIdentidad MS

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1081888](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1081888) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Creado** | 2026-03-19 |
| **Última modificación** | 2026-03-19 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1035500 — [Optimización]: Evitar duplicidad en los estados de la consulta con Registraduría](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035500)  
  Estado: New  

## Descripción

Yo como negocio sarlaft Quiero: 
- -Configurar el micro para conectarse a azure redis cache 
- -Configurar el micro para conectarse a la nueva base de datos de validador de identidad 
- -Para la validacion de registraduria consultar en cache el tiempo de rechazo por parametria para registraduria, si no esta en cache, cargarlo de la bd. 
- -Si el cliente con validacion de registraduria tiene rechazo, compararlo con la parametria de rechazos y determinar si debe rechazar automaticamente o debe invocar el servicio de experian. 
- -Si al validar registraduria con experian, se recibe un motivo de rechazo inmediato, almacenar el resultado para el dni del cliente en la base de datos. -Se debe loguear que cuando no se consuma el servicio de registraduria, se loguee la herencia encontrada y la respuesta a generar.

## Criterios de Aceptación

- -Configurar el micro para conectarse a azure redis cache 
- -Configurar el micro para conectarse a la nueva base de datos de validador de identidad 
- -Para la validacion de registraduria consultar en cache el tiempo de rechazo por parametria para registraduria, si no esta en cache, cargarlo de la bd. 
- -Si el cliente con validacion de registraduria tiene rechazo, compararlo con la parametria de rechazos y determinar si debe rechazar automaticamente o debe invocar el servicio de experian. 
- -Si al validar registraduria con experian, se recibe un motivo de rechazo inmediato, almacenar el resultado para el dni del cliente en la base de datos. 
- -Se debe loguear que cuando no se consuma el servicio de registraduria, se loguee la herencia encontrada y la respuesta a generar.
