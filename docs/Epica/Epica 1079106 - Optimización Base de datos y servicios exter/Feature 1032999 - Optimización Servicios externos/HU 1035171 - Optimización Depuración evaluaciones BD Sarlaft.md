# HU 1035171 — [Optimización]: Depuración evaluaciones BD Sarlaft - histórico

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999) › HU 1035171 — [Optimización]: Depuración evaluaciones BD Sarlaft - histórico

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1035171](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035171) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-05 |
| **Última modificación** | 2026-02-17 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)  
  Estado: New  

## Descripción

Como Analista SARLAFT
quiero ejecutar una depuración histórica única (one‑off) de las evaluaciones de conocimiento del cliente en estado Pendiente y Cancelado, creadas desde el año 2021 hasta el 31 de diciembre de 2024,
para depurar la tabla de evaluaciones conforme a reglas de estado, antigüedad calculada desde la fecha de creación,  garantizando ejecución en ventana no productiva y bitácora completa por registro y por lote. 
 **Alcance funcional**  
- Ejecutar una única depuración histórica sobre la tabla evaluaciones, considerando:

- Operación 
- Negocio nuevo 
- Reclamaciones  
- Estados elegibles:
- Pendiente 
- Cancelado   
- Rango temporal obligatorio:
- Evaluaciones con fecha de creación ≥ 01/01/2021 
- Evaluaciones con fecha de creación ≤ 31/12/2024   
- La fecha de creación de la evaluación es el único criterio temporal para determinar inclusión en el proceso histórico.   
- Ejecutar el proceso en ventana no productiva 
- Fuera de alcance del proceso de depuración (no se eliminan ni modifican): 
- Tabla de **clientes** 
- Tabla de **direcciones** 
- Tabla de **información financiera** 
- Tabla de **asociaciones** 
- Otras tablas que contengan información única

## Criterios de Aceptación

****  Alcance y universo de evaluaciones 
**CA-01.** El proceso debe ejecutarse **una única vez (one‑off)** y aplicar **exclusivamente** sobre la **tabla de evaluaciones de conocimiento del cliente**. 
**CA-02.** El proceso debe considerar únicamente evaluaciones asociadas a las operaciones de: 
- **Negocio nuevo** 
- **Reclamaciones**  
**CA-03.** El proceso debe incluir solo evaluaciones con estado: 
- **Pendiente** 
- **Cancelado**  
**CA-04.** El proceso debe incluir únicamente evaluaciones cuya **fecha de creación** se encuentre dentro del siguiente rango: 
- **Mayor o igual a 01/01/2021** 
- **Menor o igual a 31/12/2024**  
**CA-05.** La **fecha de creación de la evaluación** debe ser el **único criterio temporal** para: 
- Determinar la inclusión de una evaluación en el proceso histórico. 
- Calcular la antigüedad de la evaluación para la toma de decisión.    Ejecución del proceso histórico 
**CA-06.** El proceso de depuración histórica debe ejecutarse **exclusivamente dentro de una ventana no productiva** previamente definida. 
**CA-07.** Durante la ejecución del proceso, no debe existir afectación a: 
- La disponibilidad de los aplicativos de negocio. 
- El desempeño de los procesos transaccionales en línea. 
- La expedición de negocios nuevos. 
- La gestión de reclamaciones. 
- Las consultas en línea del motor SARLAFT. 
- Los procesos críticos de cierre operativo.    **CA-12.** Tomar una Foto de la base de datos antes del borrado y foto después del borrado **CA-13.** Tomar una Foto de los datos de la respuesta del servicio de assessment antes del borrado y después del borrado
