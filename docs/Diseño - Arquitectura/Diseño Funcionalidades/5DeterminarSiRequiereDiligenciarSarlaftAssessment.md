# 5. Determinar si requiere diligenciar Sarlaft (Assessment)

> **Fuente Confluence:** [5. Determinar si requiere diligenciar Sarlaft (Assessment)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3222634497/5.+Determinar+si+requiere+diligenciar+Sarlaft+Assessment)  
> **Última modificación:** 2026-02-01 — Diana Muñoz · versión 2  
> **Sección:** [Diseño Funcionalidades](./index.md)

Dentro de la evaluación para cada sarlaft se determina si la persona a la cual esta asociado debe ser diligenciado, dado que puede pasar que la persona ya tenga un sarlaft vigente para un mismo tipo de riesgo igual o superior, si es el caso, el sistema clona las evidencias del sarlaft vigente, marca que el formulario ya esta finalizado, finaliza los requisitos y cumpliendo todos esos pasos el sarlaft quedaría FINALIZADO.

Esta validación comienza con la consulta de sarlaft vigentes en PrepararEvaluacion : requiereDiligenciarFormulario, el query esta en la clase SarlaftData bajo el nombre “_SarlaftData.findByDniAndVigencia_”.

Con base en el resultado de la consulta se realizan las validaciones en el metodo finalizarFormulario de la clase PrepararEvaluacion, donde se valida si los sarlafts encontrados cumplen los  requisitos mínimos para el sarlaft sea finalizado.

Se realiza una validación previa a esta consulta, para que las entidades de Régimen Especial y Financiera no aplique la consulta, dado que no es necesario pues estas entidades tienen un tratamiento especial en el sarlaft, dado que ellas responden de forma directa antes la Superintendencia Financiera.
