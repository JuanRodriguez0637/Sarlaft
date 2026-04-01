# Gestión de la Configuración

> **Fuente Confluence:** [Gestión de la Configuración](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1809908067/Gesti%C3%B3n+de+la+Configuraci%C3%B3n)  
> **Última modificación:** 2024-08-06 — Santiago Valencia Ochoa · versión 5  
> **Sección:** 07) Dominio Soluciones Corporativas

---

## Lineamientos para desplegar cambios en el aplicativo

1. Para cada desarrollo se debe crear un feature cuyo nombre tenga la estructura: `{nro HU}-nombre descriptivo`. Ej: `TSTAR-32-WSConsultaClientes`
2. Para desplegar los cambios en ambiente de desarrollo y laboratorio, por favor crear un pull request sobre **develop**. Nunca sobre master, dado que se debe rechazar el pull request y volver a crear uno nuevo.
3. No elimine su feature hasta que sus cambios hayan sido desplegados y testeados correctamente.
4. Antes de solicitar un pull request verifique que está sincronizado con los últimos cambios de develop para evitar conflictos.
5. En caso de existir conflictos con develop, estos deben ser solucionados por el desarrollador en el feature correspondiente.
6. Para solicitar un pull request por favor cumplir con los lineamientos de pruebas unitarias al **95%**, dado que, si no cumple con el porcentaje mínimo, Jenkins frena el despliegue y por lo tanto afectamos al resto del equipo.
7. Una vez se ha desplegado el feature, revisar el aplicativo de sonar, con el fin de identificar deuda técnica susceptible de resolverse y pruebas unitarias faltantes.
8. Cada cambio en un proyecto back debe estar acompañado de pruebas soapui y pruebas de desempeño en Jmeter.
9. Actualice el archivo de `application.yml` en cada uno de los ambientes, en caso de ser modificado bajo el feature.

**Manual de Gestión de Configuración:** [`GestionConfiguracion.docx`](./attachments/GestionConfiguracion.docx)

---

## Conocer Porcentaje de Cobertura en ambiente Local

Es muy importante que cada desarrollador valide localmente antes de realizar el pull request, el porcentaje de cobertura del código. Para esto ejecute la siguiente tarea de gradle: `gradle build test`

Con esta ejecución dentro de cada proyecto quedará el reporte de pruebas unitarias:

- `\adm_y_fin-sarlaft-api-ms\domain\model\build\reports\jacoco\test\html`
- `\adm_y_fin-sarlaft-api-ms\domain\usecase\build\reports\jacoco\test\html`
- `\adm_y_fin-sarlaft-api-ms\infraestructure\driven-adapters\jpa-repository\build\reports\jacoco\test\html`
- `\adm_y_fin-sarlaft-api-ms\infraestructure\entry-points\reactive-web\build\reports\jacoco\test\html`
- `\adm_y_fin-sarlaft-api-ms\infraestructure\helpers\jpa-repository-commons\build\reports\tests\test`

Al momento del despliegue el porcentaje de cobertura se puede ver en: <https://sonar.suramericana.com.co/dashboard?id=sarlaftapi>

> **Es muy importante mantener una cobertura de pruebas mínimo del 85% y una deuda técnica máximo de 30 minutos.**

---

## Sub-secciones

| Sub-sección | Descripción | Última modificación |
|-------------|-------------|---------------------|
| [Configuración Infraestructura](./ConfiguracionInfraestructura/index.md) | Documentación asociada a los pasos y procedimientos necesarios para montar una infraestructura en Azure. | 2021-07-06 |
