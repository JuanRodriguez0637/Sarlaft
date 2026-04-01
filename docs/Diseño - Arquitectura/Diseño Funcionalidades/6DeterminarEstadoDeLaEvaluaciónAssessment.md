# 6. Determinar estado de la evaluación (Assessment)

> **Fuente Confluence:** [6. Determinar estado de la evaluación (Assessment)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3222831120/6.+Determinar+estado+de+la+evaluaci+n+Assessment)  
> **Última modificación:** 2023-06-13 — Diana Muñoz · versión 3  
> **Sección:** [Diseño Funcionalidades](./index.md)

Una evaluación finaliza en el momento que cada uno de sus Saralft tiene el estado FINALIZADO (o CANCELADO en casos especiales), para hacer este analisis se utiliza el caso de uso DeterminarEstadoEvaluacionUseCase en el microservicio de SarlaftApi

Un Sarlaft finaliza cuando todas sus evidencias se encuentran en estado EXITOSO o FALLA_TECNICA, el formulario ha sido completado y los requisitos se encuentran en estado ADJUNTO o FINALIZADO.
