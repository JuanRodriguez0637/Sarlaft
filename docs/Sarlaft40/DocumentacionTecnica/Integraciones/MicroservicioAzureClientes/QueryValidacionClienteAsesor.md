# Query Validación Cliente Asesor

> **Fuente Confluence:** [Query Validación Cliente Asesor](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2629468320/Query+Validaci%C3%B3n+Cliente+Asesor)
> **Última modificación:** 2023-07-14 — Julián Andrés Curubo García · versión 8
> **Sección:** [Microservicio Azure - Clientes](./index.md)

**Objetivo**:

Consultar el servicio [{host}/vinculaciones/validar-cliente-asesor](http://siclab.segurossura.com.co/vinculaciones/validar-cliente-asesor) para consultar si existe una relación entre cliente y asesor en los negocios de **Compañía generales** (COF03) y **ARL **(COF01).

**Nota:**

Al ser este un Query, este es un procedimiento síncrono, es decir, se debe esperar respuesta del consumo.

**Appname: **mdcmi

**QueryName: **Clients.client.adviser.validate

**Mensaje de entrada:**

```
{
    "dniCliente": "C71679357",
    "codigoAsesor": "23202",
    "codigoCompania": "COF03"
}
```

**Mensaje de salida:**

Caso 1 - Todo transcurre como debe:

```
{
    "validationAproved": true,
    "exception": null,
    "estado": null,
    "mensaje": null,
    "errorTecnico": false,
    "mensajeErrorTecnico": null
}
```

Caso 2 - Hubo error de consumo de servicio:

```
{
    "validationAproved": false,
    "exception": "ExcepcionValorObligatorio",
    "estado": "400 BAD_REQUEST",
    "mensaje": "El DNI del cliente es requerido para realizar la validación.",
    "errorTecnico": false,
    "mensajeErrorTecnico": null
}
```

Caso 3 - Hubo un error interno en la función:

```
{
    "validationAproved": false,
    "exception": null,
    "estado": null,
    "mensaje": null,
    "errorTecnico": true,
    "mensajeErrorTecnico": "Ocurrió un error al momento de conectarse con host"
}
```
