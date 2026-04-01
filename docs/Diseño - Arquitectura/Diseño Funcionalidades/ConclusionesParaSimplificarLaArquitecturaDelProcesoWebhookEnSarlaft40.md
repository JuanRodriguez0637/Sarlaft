# Conclusiones para simplificar la arquitectura del proceso webhook en Sarlaft 4.0

> **Fuente Confluence:** [Conclusiones para simplificar la arquitectura del proceso webhook en Sarlaft 4.0](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3743219726/Conclusiones+para+simplificar+la+arquitectura+del+proceso+webhook+en+Sarlaft+4.0)  
> **Última modificación:** 2024-05-15 — Julián Andrés Curubo García · versión 2  
> **Sección:** [Diseño Funcionalidades](./index.md)

Tras el análisis de las dos posibles soluciones planteadas, se llega a las siguientes conclusiones:

- 
Se ha decidido implementar la [solución#1](/wiki/spaces/EPA/pages/3742892047/Propuesta+1+-+Omitir+la+comunicaci+n+que+pasa+por+Azure+Service+Bus), que consiste en eliminar la comunicación a través del Azure Service Bus entre los microservicios sarlaftapi y sarlaftwebhook, sustituyendo el intercambio de queries y comandos.

- 
Se elimina el punto de fallo del microservicio de sarlaftwebhook.

- 
Se elimina el cuello de botella de atender el query por parte del microservicio de sarlaftapi.

- 
Los cambios realizados en el microservicio de sarlaftapi no requerirían pruebas de seguridad dinámicas lo cual elimina la espera que implica que sean programadas.

- 
Al trasladarse la responsabilidad que tiene actualmente el microservicio sarlaftwebhook (pensando en ser eliminado en un futuro) al microservicio sarlaftapi, podría aumentar los tiempos de las transacciones sobre todo con los servicios de assessment y guardar formulario.

- 
Aumenta la complejidad accidental en el microservicio de sarlaftapi.