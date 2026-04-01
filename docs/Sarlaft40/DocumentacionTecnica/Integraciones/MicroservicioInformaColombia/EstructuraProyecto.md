# Estructura Proyecto - Microservicio InformaColombia

> **Fuente Confluence:** [Estructura Proyecto - Microservicio InformaColombia](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2363457678/Estructura+Proyecto+-+Microservicio+InformaColombia)
> **Última modificación:** 2022-06-22 — Diana Muñoz · versión 3
> **Sección:** [Microservicio InformaColombia](./index.md)

El microservicio InformaColombia está construido a partir del generador de legos de Sura, se basa en

arquitectura hexagonal, generando los siguientes componentes:
![imagen-20210901-214208.png](./attachments/imagen-20210901-214208.png)
El proyecto está dividido en los siguientes subproyectos (Figura 2):
![imagen-20210901-214405.png](./attachments/imagen-20210901-214405.png)
1. **applications-app-service**: contiene configuraciones generales del aplicativo, importa los módulos de las otras capas que siguen la Clean Architecture (Dominio e Infraestructura). Es la encargada de la interacción con el framework utilizado, sus complementos y la configuración de la ejecución de la Azure Function. En el archivo de configuración application.yaml se encuentran las propiedades parametrizables para la suscripción y escucha del comando de entrada (rabbitmq) y el nombre del comando escuchado. Además, se tiene la configuración para la publicación del mensaje de salida en el RabbitMqSura (host, username, password, port, virtualhost, exchange, routingkey).
2. **domain**: La capa de dominio es la capa más interna del proyecto y es la encargada de dar las directivas del proceso teniendo en cuenta la lógica de negocio:

**a. model**: representa los objetos de dominio (negocio) del aplicativo, sus características y comportamientos.

**b. use-case**: contiene el único caso de uso (actividad) que se ejecuta en la aplicación desde el proxy de la capa de infraestructura. Interactúa con los modelos para la validación de los campos obligatorios en el mensaje de salida.

** 3. infrastructure**:

**a. driver-adapters-web-client: **adaptador que permite el consumo de servicios REST.

**b. driven-adapters-async-query-handler: **adaptador que permite la subscripción y escucha del query de entrada.

**c. entry-points-subs-events: **paquete donde se configura la azure function y el timmer que la dispara.
