# Respuestas de error (propuesta aun no implementada)

> **Fuente Confluence:** [Respuestas de error (propuesta aun no implementada)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3307601991)  
> **Última modificación:** 2023-11-22 — Diana Muñoz · versión 6  
> **Sección:** [Documento Diseño Técnico](./index.md)

De acuerdo a los lineamientos de servicios rest en cuanto al manejo de errores [Lineamientos para servicios REST - Arquitectura técnica - Confluence (atlassian.net)](https://segurosti.atlassian.net/wiki/spaces/AR/pages/256672056/Lineamientos+para+servicios+REST) se tienen las siguientes definiciones para el manejo de error de los servicios web que expone el aplicativo de Sarlaft 4.0

***Errores Técnicos:*** aquellos errores técnicos y no controlados generaran una respuesta con código HTTP 500, con la siguiente estructura:

```json
{
    "errors": [
        {
            "id": "tecnico-001",
            "tipo": "TECNICO",
            "mensaje": "Error presentado: XXXX",
            "detalle": "XXXXXX"
        }
    ]
}
```text

Donde el campo `id` sea incremental para los diferentes errores presentados. El campo `tipo` TECNICO sea constante, el campo `mensaje` inicie con el prefijo "Error presentado: " y XXX corresponda a la falla particular; el campo `detalle` corresponda de un mensaje aclaratorio.

***Errores Negocio:*** aquellos errores que se originan por incumplir una regla definida por negocio para la funcionalidad que ofrece el servicio web. Estos errores se generaran con código HTTP 400 con la siguiente estructura:

```json
{
    "errors": [
        {
            "id": "negocio-001",
            "tipo": "NEGOCIO",
            "mensaje": "Información incompleta: XXX",
            "detalle": "Identificación XXXX: XXX"
        }
    ]
}
```text

Donde el campo `id` sea incremental para los diferentes errores presentados. El campo `tipo` NEGOCIO sea constante. Para el caso de error por falta de un campo que es obligatorio, el campo `mensaje` inicie con el prefijo "Información incompleta: " y XXX corresponda al nombre de campo en particular; el campo `detalle` corresponda de un mensaje aclaratorio; para el caso que no sea una regla de obligatoriedad se quita el prefijo "Información incompleta".

***Errores Formato:*** aquellos errores que se originan por que un campo no tiene el formato adecuado según las reglas de calidad definidas.

```json
{
    "errors": [
        {
            "id": "formato-001",
            "tipo": "FORMATO",
            "mensaje": "Formato incorrecto: XXX",
            "detalle": "Debe ingresar un XXX valido"
        }
    ]
}
```

Donde el campo `id` sea incremental para los diferentes errores presentados. El campo `tipo` FORMATO sea constante. El campo `mensaje` inicie con el prefijo "Formato incorrecto: " y XXX corresponda al nombre de campo en particular; el campo `detalle` corresponda de un mensaje aclaratorio.

El siguiente excel contiene el listado de servicios expuestos en la aplicación a través de tres microservicios: `sarlaftapi`, `sarlaftadmin` y `sarlaftbatch`. Y las respuestas en los formatos anteriores para los mensajes de los servicios web del microservicio de `sarlaftapi` [respuestasErroresSarlaft4.xlsx](./attachments/respuestasErroresSarlaft4.xlsx)

**Nota:** para el caso de funcionalidades que son expuestas por procesos masivos no se afectaran las respuestas en esta etapa del cambio, solo a nivel de servicio web.

***Propuesta implementación:***

Dado que Sarlaft 4.0 es una aplicación transversal a muchos negocios y esta es consumida por una gran variedad de aplicaciones clientes de estos negocios, se propone que el cambio se realice publicando una segunda versión de los servicios web y de esta forma los aplicativos clientes se vayan migrando a la segunda versión progresivamente.

***Diseño del cambio:***

Crear una nueva excepción `FormatException` para las excepciones relacionadas con error de formato. tipo: Formato\
Las excepciones relacionadas con error de negocio (tipo Negocio) mapearían con `BusinessException`.

En `FormatException` los tipos deben tener los atributos `message`, `id`, `mensajePolitica`, `detalle`. Completar la información según el excel de errores respuestasErroresSarlaft4.xls\
En `BusinessException` adicionar los atributos `id`, `mensajePolitica`, `detalle` adicional al `message` que ya se tiene. Completar la información según el excel de errores respuestasErroresSarlaft4.xls

Para los errores de aplicación (500) crear el mismo mecanismo de mapeo.

Crear la clase `ErrorHandlerAPI` en el paquete `sura.sarlaft4.web.error`. En esta clase configurar `@ControllerAdvice(basePackages = "sura.sarlaft4.web.api.")` adicionando cada paquete nuevo donde se ubiquen las nuevas clases de los servicios web en segunda versión que implementen el cambio de respuesta de mensajes.\
En esta clase crear los métodos que manejen las excepciones en el formato json propuesto para el manejo de errores 400 y 500

`ErrorHandler`: Adicionar un nuevo manejador de la excepción `FormatException`: `handleFormatExceptions`\
Adicionar en la anotación `@ControllerAdvice` el atributo `basePackages` indicando el paquete actual de servicios `sura.sarlaft4.web.` completando el paquete donde están las clases de los servicios web actuales. Con esto se garantiza que las respuestas de error de los servicios actuales no se vean afectadas.
