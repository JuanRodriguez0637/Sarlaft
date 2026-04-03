# Servicio Matricular Salario Mínimo

> **Fuente Confluence:** [Servicio Matricular Salario Mínimo](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4222550059)
> **Última modificación:** 2024-11-19 — Johnathan Monsalve Bello · versión 6
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite matricular el salario mínimo vigente en la base de datos, el cual sirve como insumo para las reglas del motor. Esta funcionalidad permite modificar los valores del salario mínimo que el motor debe contemplar para tomar las decisiones de las variables de los valores asegurados y primas.

- **Endpoint:** POST `/sarlaftbackweb/salariosminimos`

- **Perfil de Seus4:** `PF_SARLAFTADM`

- **Ejemplo Json Request:**

```json
{
    "valorSalario": 1300000
}
```

- **Ejemplo Json Response exitoso:**

```json
{
    "actualizado": true,
    "mensajeError": null
}
```

- **Ejemplo Json Response con error:**

```json
{
    "actualizado": false,
    "mensajeError": "No se pudo matricular el salario mínimo"
}
```

Al momento de matricular un salario nuevo este queda con estado `ACTIVO` e inmediatamente actualiza los registros anteriores a un estado `INACTIVO`, esto con el fin de controlar que sea solo un único registro que tenga estado activo ya que el motor consulta el salario que se encuentre almacenado con estado activo y por consiguiente es el salario vigente.

Se implementa una regla de negocio que solo permita registrar 10 parametrizaciones por año, y cuando se exceda ese limite se lance un mensaje de error. Ejemplo:

- **Ejemplo Json Response con error por limite excedido:**

```json
{
    "actualizado": false,
    "mensajeError": "Se ha excedido el número de parametrizaciones permitidas"
}
```

Adicional se valida si el salario nuevo es igual al salario vigente, entonces no se registre el valor y se devuelva un mensaje de éxito.
