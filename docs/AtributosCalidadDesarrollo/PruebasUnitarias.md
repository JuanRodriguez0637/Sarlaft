# Pruebas Unitarias

> **Fuente Confluence:** [Pruebas Unitarias](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814003808/Pruebas+Unitarias)  
> **Última modificación:** 2021-03-26 — Diana Muñoz · versión 1  
> **Sección:** [Atributos de Calidad Desarrollo](./index.md)

## Conocer Porcentaje de Cobertura en Ambiente Local

Es muy importante que cada desarrollador valide localmente antes de realizar el pull request, el porcentaje de cobertura del código. Para esto ejecute la siguiente tarea de gradle: **`gradle build test`**

Con esta ejecución dentro de cada proyecto quedará el reporte de pruebas unitarias en:

- `adm_y_fin-sarlaft-api-ms\domain\model\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\domain\usecase\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\infraestructure\driven-adapters\jpa-repository\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\infraestructure\entry-points\reactive-web\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\infraestructure\helpers\jpa-repository-commons\build\reports\tests\test`

Al momento del despliegue el porcentaje de cobertura se puede ver en:

<https://sonar.suramericana.com.co/dashboard?id=sarlaftapi>

**Es muy importante mantener una cobertura de pruebas mínimo del 85 %.**
