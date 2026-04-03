# Servicio Matricular País Gafi

> **Fuente Confluence:** [Servicio Matricular País Gafi](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4902944769)
> **Última modificación:** 2025-08-04 — Mauricio Marin Martinez · versión 2
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite matricular países Gafi en la tabla `tsaf_paises_gafi` en el cual se encuentra la parametrización de los países de las categorías Gafi Gris, Gafi Negro o Sin Categoria.

- **Endpoint:** `POST /sarlaftbackweb/paisesgafi`

- **Perfil de Seus4:** `PF_SARLAFTADM`

- **Ejemplo Json Request:**

```json
{     
    "codigo": "894",
    "bloqueante":"S"
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
    "mensajeError": "No se pudo matricular el país"
}
```

*Código*: Pertenece al código del país, relacionado con los catálogos de países

*Bloqueante*: Indica si el país ingresado es bloqueante o no de acuerdo a lo siguiente:

Gafi Gris: Bloqueante `N` sin fecha de baja\
Gafi Negro: Bloqueante `S` sin fecha de baja\
Sin Categoria: Se asigna fecha de baja, se envía `NA` en el servicio

- **Ejemplo Json Response con error 500:**

```json
{
    "errors": [
        {
            "id": "tecnico-001",
            "tipo": "TECNICO",
            "mensaje": "Se ha presentado un error no controlado en el proceso de Sarlaft",
            "detalle": "Se ha presentado un error no controlado en el proceso de Sarlaft"
        }
    ]
}
```

- **Ejemplo Json Response con error 400:**

```json
{
    "errors": [
        {
            "id": "formato-001",
            "tipo": "FORMATO",
            "mensaje": "Dato de entrada incorrecto",
            "detalle": "Dato de entrada incorrecto: bloqueante:Valor inválido para bloqueante. Solo se permite N, S, NA. codigo:El código del país solo debe contener números. "
        }
    ]
}
```

Iniciativa: [https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/612207](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/612207)
