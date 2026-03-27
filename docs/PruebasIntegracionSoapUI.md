# Pruebas de Integración SoapUI

**Sarlaft 4.0 Pruebas SOAPUI**

**URL Repositorio**** SARLAFT API****:**
https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-pa
**Branches:** **dev**: Ambiente Desarrollo, **lab**: Ambiente Laboratorio, **master**: Ambiente de Producción.
Cada actualización debe agregarse en cada uno de los brach. En ambiente de producción deben eliminarse pruebas que sean de tipo de ingreso, actualización o eliminación de datos. En producción la idea es tener pruebas livianas de consulta o comúnmente conocidas como pruebas de humo, que permitan conocer que el servicio esta arriba y esta respondiendo.
Para cada servicio web expuesto debe realizarse pruebas funcionales en soapui como parte de la entrega de la HU. Para adicionar pruebas de integración al proyecto de pruebas soapui puede seguir los siguientes pasos:
- Abra el proyecto de pruebas en la herramienta SoapUI

- Sobre el nombre del proyecto de click derecho y seleccione la opción: New REST Service from URI

- Ingrese la url del servicio rest

- Adicione el header de seguridad Authorization con valor Basic SU1QTUFTSVZPUzpJTVBNQVNJVk9T

- Pruebe el correcto consumo del servicio

- Sobre el request seleccione click derecho con la opción Add to TestCase

- Seleccione la TestSuite existente y adicione un nuevo test case

- Ingrese el nombre del test case

- Adicione el nombre del primer TestStep del TestCase

- Se puede visualizar el teststep

- Adicione los assertions en el teststep

- Adicione los assertions que considere pertinentes, estos asserts dictaminaran si la prueba fue exitosa o no

- Por último corra toda la TestSuite del proyecto para verificar su correcto funcionamiento
