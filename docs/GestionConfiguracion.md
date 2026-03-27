# Gestión de la Configuración

## Lineamientos para desplegar cambios

1. Para cada desarrollo se debe crear un feature con la estructura: `{nro HU}-nombre descriptivo`. Ej: `TSTAR-32-WSConsultaClientes`
2. Para desplegar en desarrollo y laboratorio, crear un pull request sobre **develop**. Nunca sobre master.
3. No eliminar el feature hasta que los cambios hayan sido desplegados y testeados.
4. Antes de solicitar un pull request, verificar sincronización con los últimos cambios de develop.
5. Los conflictos con develop deben ser resueltos por el desarrollador en su feature.
6. Cumplir con el mínimo de pruebas unitarias al **95%** antes de PR (Jenkins frena el despliegue si no se cumple).
7. Revisar Sonar tras el despliegue para identificar deuda técnica y pruebas faltantes.
8. Cada cambio en back debe incluir pruebas SoapUI y pruebas de desempeño en JMeter.
9. Actualizar el archivo `application.yml` en cada ambiente si fue modificado en el feature.

**Cobertura local:** ejecutar `gradle build test`. Reporte en:
- `adm_y_fin-sarlaft-api-ms\domain\model\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\domain\usecase\build\reports\jacoco\test\html`
- `adm_y_fin-sarlaft-api-ms\infraestructure\driven-adapters\jpa-repository\build\reports\jacoco\test\html`

Sonar: https://sonar.suramericana.com.co/dashboard?id=sarlaftapi

> **Mínimo 85% de cobertura y máximo 30 minutos de deuda técnica.**

---

**Sarlaft****  4.0**** GESTION DE LA CONFIGURACIÓN**

**Repositorio:**
El repositorio para todos los componentes del proyecto Sarlaft 4.0 es GIT el cual se encuentra localizado en la nube de Azure
Todos los repositorios del proyecto inician con
Actualmente se cuenta con los siguientes repositorios:
**Sarlaft**** API:**  Microservicio de api

| adm_y_fin-sarlaft-api-ms | Repositorio para el microservicio principal del api de sarlaft https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-api-ms |
| --- | --- |
| adm_y_fin-sarlaft-api-conf | Repositorio de configuración para el microservicio principal del api de sarlaft https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-api-conf |
| adm_y_fin-sarlaft-pa | Repositorio de configuración para las pruebas automatizadas del microservicio de sarlaft api https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-pa |

**PEPSMS:** Microservicio de PEPS

| adm_y_fin-sarlaft-peps-ms | Repositorio para el microservicio peps https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-peps-ms |
| --- | --- |
| adm_y_fin-sarlaft-peps-conf | Repositorio de configuración para el microservicio de peps https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-peps-conf |
| adm_y_fin-sarlaft-peps-pa | Repositorio de configuración para las pruebas automatizadas del microservicio de de peps https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-peps-pa |

**Infraestructura como código**
https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-iac

**Funciones**
Los repositorios para las funciones de azure tendrán el siguiente formato -nombreFuncion-mi
**Cliente GIT:**
El aplicativo cliente de GIT utilizado es Sourcetree.

**GitFlow****:**
Para mayor eficiencia y coordinación del equipo de trabajo se manejará GitFlow como flujo de trabajo
Configure GitFlow localmente, seleccionando el icono Git-flow en el menú superior derecho, seleccione la opción OK

Crear un feature, seleccionando el icono Git-flow en el menú superior derecho y luego la opción
**Star**** New ****Feature**

Ingrese el nombre de feature, se recomienda utilizar el número de la HU que se estará desarrollando, seguido de un nombre sencillo y explicativo

Seleccione la opción de push sobre el feature para subirlo al repositorio

Se recomienda siempre actualizar los cambios de develop, para ir solucionando posibles conflictos.
**Crear ****Pull**** ****Request**
El mecanismo de pull request se utiliza para poder integrar los cambios en la rama de develop y así     ser desplegado por medio de Jenkins en los diferentes ambientes. Por lineamientos de la compañía no se puede dar push directamente sobre develop o master.
Abra en el navegador el repositorio correspondiente, donde desea subir los cambios terminados en su feature. Por ejemplo:
https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-api-ms
En el menú lateral izquierdo seleccione la opción Pull requests

Seleccione la opción **Create**** a ****pull**** ****request**, sobre el feature indicado.
Seleccione **develop**

Para la corrección de incidentes de producción se recomienda utilizar Hotfix.

Agregue al menos un compañero del equipo para la revisión par, aprobación del feature y posteriormente merge

Seleccione la opción Create, de esta forma llegará un correo electrónico a la persona encargada de la revisión. Una vez se haya aprobado el pull request,  se realizará un merge automático con la rama de develop.

Lineamientos para desplegar cambios en el aplicativo:
Para cada desarrollo se debe crear un feature cuyo nombre tenga la estructura: {nro HU}-nombre descriptivo. Ej: TSTAR-32-WSConsultaClientes
Para desplegar los cambios en ambiente de desarrollo y laboratorio, por favor crear un pull request sobre develop. Nunca sobre master, dado que se debe rechazar el pull request y volver a crear uno nuevo.
No elimine su feature hasta que sus cambios hayan sido desplegados y testeados correctamente.
Antes de solicitar un pull request verifique que esta sincronizado con los últimos cambios de develop para evitar conflictos.
En caso de existir conflictos con develop, estos deben ser solucionados por el desarrollador en el feature correspondiente.
Para solicitar un pull request por favor cumplir con los lineamientos de pruebas unitarias al 85%, dado que, si no cumple con el porcentaje mínimo, Jenkins frena el despliegue y por lo tanto afectamos el equipo de desarrollo.
Una vez se ha desplegado el feature, revisar el aplicativo de sonar, con el fin de identificar deuda técnica susceptible de resolverse y pruebas unitarias faltantes
Cada cambio en un proyecto back debe estar acompañado de pruebas soapui y pruebas de desempeño en Jmeter.
Actualice el archivo de application.yml en cada uno de los ambientes, en caso de ser modificado bajo el feature.
