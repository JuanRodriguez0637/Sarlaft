# Generar URL Validación Identidad - SarlaftAPI

> **Fuente:** [Confluence - Generar Url Validación Identidad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4927455233/Generar+Url+Validaci%C3%B3n+Identidad)  
> **Página padre:** [Microservicio SarlaftAPI](../index.md)  
> **Iniciativa:** [HU 847704](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/847704)

---

## Descripción del Servicio

| Campo | Valor |
|-------|-------|
| **Objetivo** | Permite generar la URL de validación de identidad cuando la evaluación está pendiente para determinado DNI |
| **Método HTTP** | `GET` |
| **Endpoint** | `/sarlaftserv/v1/clientes/identidades/formulario` |
| **Parámetros** | `evaluacionId`, `dni` |
| **Perfil SEUS4** | `PF_CONSUMSERVSARLAFTAPI`, `PF_CONSUMSERVSARLAFT` |

---

## Ejemplo de Request

```
GET /sarlaftserv/v1/clientes/identidades/formulario?evaluacionId=412ca3d9-900c-4628-b1cf-9d74513b97c7&dni=C1015397023
```

---

## Respuestas

### ✅ Response Exitoso (200)

```json
{
    "url": "https://sarlaft.labsura.com/redirect/validar-identidad/4c31e64e-884d-45e5-a2c1-654334e5f40a/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJTYXJsYWZ0Iiwic3ViIjoiU0FSTEFGVCIsImlzcyI6IlN1cmEuY29tIiwiZXhwIjoxNzU2NDg1MDc2LCJpYXQiOjE3NTUxODkwNzZ9.t5v9VcrawKZ7cgqs6CEFEzba8cVZl84TORu8DCuHfjE"
}
```

### ❌ Error 400 — Evaluación no encontrada

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
```

### ❌ Error 400 — DNI no pertenece a la evaluación

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
```

### ❌ Error 400 — Error en datos de entrada

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
