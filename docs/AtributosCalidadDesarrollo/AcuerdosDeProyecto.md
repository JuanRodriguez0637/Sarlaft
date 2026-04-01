# Acuerdos de Proyecto

> **Fuente Confluence:** [Acuerdos de Proyecto](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2617999383/Acuerdos+de+Proyecto)  
> **Última modificación:** 2022-02-18 — Diana Muñoz · versión 1  
> **Sección:** [Atributos de Calidad Desarrollo](./index.md)

## Entregables por cada Desarrollo

Es responsabilidad de cada miembro del equipo de desarrollo al implementar una HU:

- Comentario en Jira con la URL del PR donde se realiza la implementación: componentes de microservicio, webapp, archivo de configuración, es decir todos los archivos que se modificaron. Incluyendo cargas de seus, scripts de bases de datos y nuevas parametrizaciones en caso de ser necesario.
- Nombre del PR: tenga el código de la HU, código de bug (si aplica), en el caso del front el nombre de la aplicación (redirect, webcomponent). Descripción del cambio realizado.
  - **Estándar Back:** para título `[HU ó Bug]-[Nombre]` — Ej: `TSTAR-31-Validación Listas Vinculantes por DNI`
    - En la descripción poner el objetivo del cambio realizado.
  - **Estándar Front:** para título `[HU ó Bug]-[Aplicación]-[Nombre]` — Ej: `TSTAR-31-Redirect-Formulario PN`
    - En la descripción poner el objetivo del cambio realizado.
- Evidencias en Jira del funcionamiento en ambiente desarrollo / laboratorio.
- Actualizar estado real de la HU en Jira: progreso, disponible para pruebas.
- Tanto en las HUs de Usuario y Técnica, asignar el responsable de la revisión par técnica (Paso 1).
- Cuando la HU pase a disponible para pruebas, en caso de ser una HU de usuario asignarla a Laura Camila (Validar el proceso con Eli Zapata).
- Cuando la HU pase a disponible para pruebas, en caso de ser una HU técnica asignarla al compañerito que realizará la revisión par. El responsable de la revisión par debe asignarse en la planning, y contabilizar los puntos asignados para esta actividad.
- Las subtareas de revisión par y pruebas de seguridad deben crearse en el refinamiento.
- Las HUs que tienen cambios de front y back, se crean dos subtareas, una del lado de front y otra del lado del back, para la revisión par técnica.
- Si la HU es técnica, se puede documentar en una sola subtarea las revisiones par.
- Asignar en el PR a Jorge o a Diana una vez tenga completa la primera revisión par técnica.
- Adicional a la documentación que ya realizamos, realizar una documentación de diseño e implementación en Confluence. Se deja a criterio, pero la idea es que exista la documentación de implementación; si no existe, crear la página y contexto.

---

## Pasos del Proceso de Entrega

**HU Usuario:**

1. Revisión Par Técnica *(paso nuevo)*
2. Revisión y aprobación del PR
3. Certificación por parte de QA y PO

**HU Técnica:**

1. Revisión Par Técnica *(paso nuevo)*
2. Revisión y aprobación del PR
3. Revisión Par (Incluyendo Criterios de Aceptación)
4. Certificación por parte de Jhon.

---

## Checklist Revisión Par Técnica (primer paso)

- El PR debe dar una solución a una HU o Bug que se encuentre dentro de la versión a PDN próxima a salir.
- HU debidamente documentada en Confluence.
- Revisar la inclusión de nuevas librerías: si realmente es necesario y que la licencia sea Opensource, que no haya líneas comentadas en los `Gradle`.
- Revisar modificación de los archivos de configuración: es necesario, que no haya líneas comentadas, que no se apunte a ambientes diferentes; si se ajusta algún archivo, verificar que se realicen los PR para `dev`, `labo` y `master` del proyecto conf.
- Buenas prácticas de desarrollo: identificar opciones de mejora y sugerir cambios — algunos pueden ser opcionales, otras no. NO sería opcional: códigos que afecten el desempeño, seguridad, afectación de la arquitectura hexagonal del Lego de Sura, no aplicar programación reactiva.
- No se deben ajustar las interfaces de servicios web sin previo acuerdo del equipo (validar a quién afectaría un posible cambio).
- Verificar las reglas de nombramiento de campos y tablas en la BD ([Estándar nombramiento Base de Datos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1813545175)), verificar si el cambio es realmente necesario.
- Si existe un cambio a nivel de base de datos que requiera ajustar el tamaño de los campos, notificar el cambio para aplicarlo en todos los ambientes, dejar script como insumo en la HU en Jira.
- Verificar si el cambio requiere nuevas parametrizaciones en base de datos; estas se incluyan en el archivo `_update.sql`.
- En los nuevos servicios web verificar que los datos de entrada tengan validaciones de calidad: tamaño y formato.
- Cumplimiento de cobertura y deuda técnica en SonarQube (Back) *(Aún pendiente implementar análisis sonar por PR)*. Asociar revisión de sonar a los pull request en Azure.

---

## Checklist Revisión Par (tercer paso de HUs Técnicas)

- Verificar que se haya realizado la revisión par del primer paso.
- Verificar que funciona el cambio en el ambiente de laboratorio, verificar los criterios de aceptación. Se deja evidencia de las pruebas realizadas en laboratorio en la subtarea revisión par en la HU Jira.
