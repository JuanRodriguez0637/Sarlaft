# Completar información de Clientes para Evaluación Masiva.

> **Fuente Confluence:** [Completar información de Clientes para Evaluación Masiva.](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2740584506)
> **Última modificación:** 2022-05-23 · versión 1
> **Sección:** [Comunicaciones - Microservicio SarlaftClientes](./index.md)

**Comando de entrada:**

```text
Evaluacion.clientes.completar
```text

**Estructura de mensaje y ejemplo:**

```text
{
   "name":"Evaluacion.clientes.completar",
   "commandId":"36e56d02-b08a-445a-bf21-21d1d35bd0ac",
   "data":{
      "idEvaluacion":"a66bed8c-d2b6-4258-bb75-a341e6ea6268",
      "aplicacionOrigen":{
         "nombreAplicacion":"sarlaftapi",
         "comandoRespuesta":"Evaluacion.clientes.terminado",
         "requiereRespuesta":true
      },
      "figuras":[
         {
            "figura":"ASEGURADO"
         },
         {
            "figura":"BENEFICIARIO"
         },
         {
            "figura":"AFIANZADO"
         }
      ]
   }
}
```text

En este comando,  todos los campos son obligatorios, además, el campo **requiereRespuesta **siempre va en **true** debido a que este proceso finaliza con el envío de comando respuesta indicado en **aplicacionOrigen/comandoRespuesta **a la aplicación designada en el campo **aplicacionOrigen/nombreAplicacion**.

Al finalizar el proceso del comando `Evaluacion.clientes.completar` se envía como respuesta el siguiente comando.

Aplicación de destino:

```text
sarlaftapi
```text

**Nombre comando:**

```text
Evaluacion.clientes.terminado
```text

**Estructura del mensaje y ejemplo:**

```text
{
    "name": "Evaluacion.clientes.terminado",
    "commandId": "83c2c969-c477-43de-83e7-ebb70f4adea5",
    "data": {
        "evaluacionId": "a66bed8c-d2b6-4258-bb75-a341e6ea6268"
    }
}
```

Nota: La aplicación de destino podría cambiar siempre y cuando se indique en el campo **aplicacionOrigen/nombreAplicacion** del comando `Evaluacion.clientes.completar`.
