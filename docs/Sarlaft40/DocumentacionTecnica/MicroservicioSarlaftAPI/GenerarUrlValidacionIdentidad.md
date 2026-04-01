# Generar Url Validación Identidad

> **Fuente Confluence:** [Generar Url Validación Identidad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4927455233)
> **Última modificación:** 2025-08-14 — Mauricio Marin Martinez · versión 1
> **Sección:** [Microservicio SarlaftAPI](./index.md)
- **Objetivo:** Permite generar la url de validación de identidad cuando la evaluación esta pendiente para determino dni.
- **Endpoint: GET** `/sarlaftserv/v1/clientes/identidades/formulario`
- **Params:** `evaluacionId`, `dni`
- **Perfil de Seus4:** `PF_CONSUMSERVSARLAFTAPI`, `PF_CONSUMSERVSARLAFT`
- **Ejemplo Request:** `/sarlaftserv/v1/clientes/identidades/formulario?evaluacionId=412ca3d9-900c-4628-b1cf-9d74513b97c7&dni=C1015397023`

**Ejemplo Json Response Exitoso:**

```json
{
    "url": "https://sarlaft.labsura.com/redirect/validar-identidad/4c31e64e-884d-45e5-a2c1-654334e5f40a/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJTYXJsYWZ0Iiwic3ViIjoiU0FSTEFGVCIsImlzcyI6IlN1cmEuY29tIiwiZXhwIjoxNzU2NDg1MDc2LCJpYXQiOjE3NTUxODkwNzZ9.t5v9VcrawKZ7cgqs6CEFEzba8cVZl84TORu8DCuHfjE"
}
```text

- **Ejemplo Json Response con error 400 evaluación no encontrada:**

```json
{
    "errors": [
        {
            "id": "negocio-043",
            "tipo": "NEGOCIO",
            "mensaje": "Información no valida:  Identificador de la evaluación",
            "detalle": "El identificador de la evaluación no se ha encontrado"
        }
    ]
}
```text

- **Ejemplos Json Response con error 400 dni no pertenece a la evaluacion**

```json
{
    "errors": [
        {
            "id": "negocio-041",
            "tipo": "NEGOCIO",
            "mensaje": "Información inconsistente: sarlaft",
            "detalle": "El Dni no se encuentra asociado a la evaluación Sarlaft"
        }
    ]
}
```text

- **Ejemplos Json Response con error 400 error datos de entrada**

```json
{
    "errors": [
        {
            "id": "formato-014",
            "tipo": "FORMATO",
            "mensaje": "Formato incorrecto: Identificación del cliente",
            "detalle": "Debe ingresar un dni válido"
        }
    ]
}
```

Iniciativa: [https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/847704](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/847704)
