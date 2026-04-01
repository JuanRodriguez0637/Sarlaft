# Pruebas automatizadas Motor

> **Fuente Confluence:** [Pruebas automatizadas Motor](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3735683077/Pruebas+automatizadas+Motor)
> **Última modificación:** 2024-05-15 — Juan David Tamayo Molina (Unlicensed) · versión 3
> **Sección:** [Pruebas automatizadas Motor](./index.md)

## Informe de actualización de automatización Motores de Reglas SARLAFT.

### **Fecha elaboración:** [11-04-2024]

#### **Actualización:** [14-05-2024]

#### **HU:**[464280](https://dev.azure.com/SuraColombia/Portafolios/_workitems/edit/464280)

#### **Elaborado por:**Juan David Tamayo Molina

### Resumen

En la revisión reciente de las reglas de motores utilizadas en nuestros sistemas de automatización, se ha identificado una significativa brecha temporal entre la creación inicial de estas automatizaciones y su última actualización estructural. Este lapso ha dado lugar a cambios sustanciales en las reglas de los motores, afectando directamente la eficacia y eficiencia de los procesos automatizados. Se considera que la totalidad de las reglas requieren una revisión exhaustiva para determinar su vigencia, necesidad de actualización o eliminación. Además, se ha detectado una alta dependencia del conocimiento específico del negocio, lo que complica significativamente el mantenimiento autónomo de los motores por parte de los automatizadores.

#### Introducción

La automatización de procesos ha sido un pilar fundamental en la optimización de operaciones dentro de la organización. Sin embargo, el entorno tecnológico es altamente dinámico, y las reglas que gobiernan estos procesos automatizados no son la excepción. Se ha identificado una brecha considerable entre el momento de creación y la estructuración de las automatizaciones, lo que ha llevado a discrepancias con las reglas actuales de los motores. Este desafío se ve exacerbado por la complejidad inherente al conocimiento específico del negocio requerido para la gestión efectiva de estas automatizaciones.

##### Hallazgos Claves

_**Brecha Temporal Significativa y Cambios en Reglas:**_ Existe una gran brecha de tiempo desde la creación hasta la última actualización de las automatizaciones, con un estimado de más de 5200 reglas que requieren revisión, ya sea para su respectivo mantenimiento (actualización), adición de nuevas reglas o eliminación de reglas que probablemente ya no se usen_._ La ultima actualización del repositorio fue el 30 de noviembre del 2022, lo cual es es un periodo de tiempo prolongado en donde se han producido múltiples cambios.

_**Alta Dependencia del Conocimiento del Negocio:**_ La efectividad en la actualización y mantenimiento de los motores de automatización se ve significativamente limitada por la complejidad y la necesidad de un conocimiento del negocio profundo. Esto representa un desafío considerable para los automatizadores, quienes pueden encontrar dificultades para realizar mantenimientos sin el apoyo constante de un analista funcional que posea un entendimiento completo del contexto del negocio

_**Desafíos Técnicos con Librerías:**_ Se ha identificado una discrepancia entre la versión de la librería “_org.reactivecommons:async-service-bus-starter:1.1.28-BETA_” que se encuentra de forma remota en el repositorio utilizada en el entorno de desarrollo, y “_org.reactivecommons:async-service-bus-starter:1.1.39-BETA_” que es la necesaria para ejecutar las aplicaciones de forma local. Esta librería se usa para:

- Permite interactuar con los Motores de decisiones.

- Es obligatoria para compilar el proyecto y en los tiempos de ejecución del proyecto.

- Además corresponde a un tipo de artefacto de Azure, que Sarlaft utilizó para la mensajería asíncrona.

Este desajuste puede llevar a inconsistencias en el comportamiento de las aplicaciones y complicar el proceso de desarrollo de pruebas automatizadas. En caso de realizar el cambio SE DEBE TENER EN CUENTA que se pueden encontrar las siguientes limitaciones:

- **Deprecación:** Funciones o clases podrían haber sido marcadas como obsoletas o eliminadas.

- **Compatibilidad:** Error de compatibilidad con otras librerías o frameworks que se integren con su uso.

##### Metodología

La metodología propuesta se expande para incluir pasos específicos destinados a abordar la complejidad derivada de la necesidad de conocimiento del negocio:

- **Formación y Colaboración:** Promover sesiones de capacitación entre automatizadores y analistas funcionales para facilitar la transferencia de conocimiento del negocio TOTAL para el mantenimiento efectivo de las automatizaciones.

- **Identificación, Categorización y Análisis Detallado de Reglas:** Como se mencionó anteriormente, con un énfasis adicional en la colaboración intergrupal para asegurar una comprensión completa del impacto del negocio.

- **Implementación y Pruebas:** Implementar cambios con una apoyo y validación estrecha por parte de analistas funcionales, para asegurar la alineación con los requisitos y objetivos del negocio.

##### Desafíos Técnicos y Recomendaciones Específicas

_**Revisión y Estandarización de Librerías**_: Es crucial realizar una revisión técnica de las librerías utilizadas en los proyectos, particularmente de “_org.reactivecommons:async-service-bus-starter:1.1.28-BETA_”. Se debe garantizar que todas las instancias del proyecto utilicen la misma versión para evitar problemas de compatibilidad y facilitar un entorno de desarrollo coherente. [Ver inciso: _**Desafíos Técnicos con Librerías**_].

_**Gestión de Repositorios:**_ Dada la importancia de separar claramente los entornos de desarrollo y prueba, se recomienda la creación de un nuevo repositorio dedicado exclusivamente a la automatización de pruebas. Esto permitirá que la rama master y las ramas de características (feature/) permanezcan enfocadas, mientras que el nuevo repositorio puede ser utilizado para realizar pruebas más experimentales o de integración sin afectar el flujo.

Por lineamientos existe un repositorio de pruebas automatizadas dedicado para el repo de sarlaft brms, se recomienda realizar la migración desde la rama **feature/pruebas-motor**del repositorio sarlaft PAhasta la**rama master**del repositorio de sarlaft brms.

Además es esencial contar con un pipeline dedicado para la ejecución de pruebas automatizadas, con el fin de optimizar su implementación, asegurar la consistencia en los resultados y mejorar la eficiencia general del proceso de pruebas. Esta infraestructura permitirá gestionar, coordinar y monitorear las pruebas de manera centralizada, facilitando la identificación temprana de problemas y garantizando la calidad continua del software.

##### Conclusiones y Recomendaciones Generales

Dada la complejidad del mantenimiento de los motores de automatización, exacerbada por la necesidad de un conocimiento profundo del negocio, se recomienda enfocarse en estrategias de colaboración y capacitación entre los equipos de automatización y los analistas funcionales. La revisión de las más de 5200 reglas estimadas debe llevarse a cabo con una perspectiva integrada que considere tanto la tecnología como el contexto del negocio, asegurando así que las automatizaciones no solo sean técnicamente sólidas sino también relevantes y alineadas con los objetivos del negocio.

Este informe ahora abarca de manera integral tanto los desafíos de negocio como técnicos, ofreciendo un panorama claro de las acciones necesarias para mejorar la gestión de las reglas de automatización y el mantenimiento del software. La implementación de estas recomendaciones asegurará que tanto los equipos de desarrollo como los analistas funcionales puedan trabajar de manera más eficiente y efectiva, manteniendo al mismo tiempo la integridad y la coherencia técnica de las aplicaciones automatizadas.

##### Webgrafía

- **Repositorio pruebas automatizadas:** [892-sarlaft-pa - Rama: feature/pruebas-motor](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-pa?path=%2F&version=GBfeature%2Fpruebas-motor&_a=contents)

- **Repositorio desarrollo:** [892-sarlaft-brms-ms - Rama: feature/HU_378894_cambio_comunicacion_motor_v1](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-ms?path=/infraestructure/driven-adapters/brms-drools/src/main/resources)

- **Repositorio Sarlaft Brms PA:**[https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-pa](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/892-sarlaft-brms-pa)
