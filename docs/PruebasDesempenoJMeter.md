# Pruebas de Desempeño JMeter

**Sarlaft 4.0 Pruebas ****JMeter**

**URL Repositorio:**
https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-sarlaft-pa
**Branches:** **dev**: Ambiente Desarrollo, **lab**: Ambiente Laboratorio, **master**: Ambiente de Producción.
Cada actualización debe agregarse en cada uno de los brach. En ambiente de producción deben eliminarse pruebas que sean de tipo de ingreso, actualización o eliminación de datos. En producción la idea es tener pruebas livianas de consulta o comúnmente conocidas como pruebas de humo, que permitan conocer que el servicio está arriba y está respondiendo.
Para cada servicio web expuesto debe realizarse pruebas de desempeño en JMeter como parte de la entrega de la HU. Para adicionar pruebas de desempeño al proyecto, puede seguir los siguientes pasos:
- En JMeter abra el proyecto rendimiento_SarlaftAPI.jmx

- En User Defined Variables seleccione la opción ADD, e ingrese una nueva variable con el path del nuevo servicio, por ejemplo: pathInitUpdate con el valor del path del servicio: sarlaftserv/assessment/update

- Seleccione click derecho sobre algún Thread Group del menú lateral izquierdo y seleccione la opción Duplicate

- Cambie el nombre del ThreadGroup.

- Cambie el nombre de la tarea de consumo

- Actualice el json del Body que será el request del servicio y el nombre de la variable del path creada, por ejemplo en este caso: pathInitUpdate

- En el menú lateral izquierdo seleccione la opción Response Assertion, e ingrese el assert correspondiente a cada servicio

- No olvide guardar el proyecto

- Inicie las pruebas y verifique su correcto funcionamiento
