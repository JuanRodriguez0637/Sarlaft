# Atributos de Calidad Desarrollo

Dentro de cada HU del proyecto Sarlaft 4.0 se tienen los siguientes criterios de calidad:

- Pruebas Unitarias mínimo al 85%
- Documentación Confluence
- Deuda técnica en menos de 30 minutos (objetivo: 0 minutos)

Adicional para HUs que expongan servicios web:

- Pruebas Integración SoapUI
- Pruebas de Desempeño JMeter
- Documentación Swagger
- El servicio expuesto debe contar con seguridad de Seus, HTTPS y validación en sus campos de entrada.

---

## Pruebas Unitarias

**Conocer Porcentaje de Cobertura en ambiente Local:**

Es muy importante que cada desarrollador valide localmente antes de realizar el pull request el porcentaje de cobertura del código. Ejecutar la siguiente tarea de gradle: `gradle build test`

Con esta ejecución dentro de cada proyecto quedará el reporte de pruebas unitarias en:

- `adm_y_fin-sarlaft-api-ms\domain\model\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\domain\usecase\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\infraestructure\driven-adapters\jpa-repository\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\infraestructure\entry-points\reactive-web\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\infraestructure\helpers\jpa-repository-commons\build\reports\tests\test`

Al momento del despliegue el porcentaje de cobertura se puede ver en:
https://sonar.suramericana.com.co/dashboard?id=sarlaftapi

> **Es muy importante mantener una cobertura de pruebas mínimo del 85%.**

---

## Documentación Confluence

Es muy importante documentar en este espacio de trabajo de Sarlaft 4.0 todos los componentes nuevos que se desarrollen, incluyendo su diseño y arquitectura, configuración de ambiente, estructura del proyecto, servicios web expuestos, mecanismos de integración y demás ítems importantes.

Para cuando el desarrollo corresponda a un nuevo servicio web, adicionar una página nueva al ítem de **Servicios Web** (correspondiente al módulo donde se desarrolló), e incluir los siguientes datos básicos:

- Objetivo del Servicio Web
- Endpoint
- Perfil de Seus4
- Ejemplo Json Request
- Dependencias:
  - Si tiene dependencia con servicios web externos, poner las URL.
  - Si la dependencia es con base de datos, mencionar cuál es la base de datos.
  - Si la dependencia es con mensajería, poner el JSON de mensaje solicitado y recibido.

---

## Deuda Técnica

La deuda técnica del proyecto se puede observar en Sonar:
https://sonar.suramericana.com.co/dashboard?id=sarlaftapi

El objetivo es tener una deuda técnica máxima de **30 minutos**.

En caso de que la deuda técnica supere este objetivo, Jenkins no permitirá desplegar los cambios.

---

## Acuerdos de Proyecto

### Entregables por cada Desarrollo

Es responsabilidad de cada miembro del equipo de desarrollo al implementar una HU:

- Comentario en Jira con la URL del PR donde se realiza la implementación: componentes de microservicio, webapp, archivo de configuración (incluyendo cargas de seus, scripts de BD y nuevas parametrizaciones si aplica).
- Nombre del PR con el código de la HU, código de bug (si aplica) y descripción del cambio:
  - **Estándar Back:** `[HU o Bug]-[Nombre]` — Ej: `TSTAR-31-Validación Listas Vinculantes por DNI`
  - **Estándar Front:** `[HU o Bug]-[Aplicación]-[Nombre]` — Ej: `TSTAR-31-Redirect-Formulario PN`
- Evidencias en Jira del funcionamiento en ambiente desarrollo / laboratorio.
- Actualizar estado real de la HU en Jira: progreso, disponible para pruebas.
- Asignar el responsable de la revisión par técnica (Paso 1) en HUs de Usuario y Técnica.
- HU de usuario disponible para pruebas → asignar a Laura Camila (validar proceso con Eli Zapata).
- HU técnica disponible para pruebas → asignar al compañero que realizará la revisión par.
- Las subtareas de revisión par y pruebas de seguridad deben crearse en el refinamiento.
- HUs con cambios de front y back → dos subtareas de revisión par (una front, una back).
- Si la HU es técnica, se puede documentar en una sola subtarea las revisiones par.
- Asignar en el PR a Jorge o a Diana una vez tenga completa la primera revisión par técnica.
- Documentación de diseño e implementación en Confluence.

### Pasos del Proceso de entrega

**HU Usuario:**
1. Revisión Par Técnica *(paso nuevo)*
2. Revisión y aprobación del PR
3. Certificación por parte de QA y PO

**HU Técnica:**
1. Revisión Par Técnica *(paso nuevo)*
2. Revisión y aprobación del PR
3. Revisión Par (incluyendo Criterios de Aceptación)
4. Certificación por parte de Jhon

### Checklist Revisión Par Técnica (primer paso)

- El PR debe dar solución a una HU o Bug dentro de la versión a PDN próxima a salir.
- HU debidamente documentada en Confluence.
- Revisar la inclusión de nuevas librerías: verificar que sea necesaria y que la licencia sea Opensource. Sin líneas comentadas en los Gradle.
- Revisar modificación de archivos de configuración: que no haya líneas comentadas, que no se apunte a ambientes diferentes. Si se ajusta algún archivo, verificar PR para dev, labo y master del proyecto conf.
- Buenas prácticas de desarrollo: identificar opciones de mejora y sugerir cambios. **No opcionales:** código que afecte desempeño, seguridad, arquitectura hexagonal del Lego de Sura, o que no aplique programación reactiva.
- No ajustar interfaces de servicios web sin previo acuerdo del equipo.
- Verificar reglas de nombramiento de campos y tablas en BD.
- Si hay cambio en BD que requiera ajustar tamaño de campos, notificar y dejar script en la HU en Jira.
- Verificar si el cambio requiere nuevas parametrizaciones en BD (incluirlas en `_update.sql`).
- En nuevos servicios web verificar validaciones de calidad en datos de entrada: tamaño y formato.
- Cumplimiento de cobertura y deuda técnica en Sonar (Back).

### Checklist Revisión Par (tercer paso de HUs Técnicas)

- Verificar que se haya realizado la revisión par del primer paso.
- Verificar que funciona el cambio en ambiente de laboratorio y los criterios de aceptación.
- Dejar evidencia de las pruebas realizadas en laboratorio en la subtarea revisión par en la HU Jira.
