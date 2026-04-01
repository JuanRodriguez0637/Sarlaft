# Tipo de formulario y requisitos | Proceso Actualizacion

> **Fuente Confluence:** [Tipo de formulario y requisitos | Proceso Actualizacion](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2870804541/Tipo+de+formulario+y+requisitos+Proceso+Actualizacion)
> **Última modificación:** 2022-08-23 — Alejandra Zuleta Gonzalez (Unlicensed) · versión 3
> **Sección:** [Actualización](./index.md)

**Tipo de comunicación:**Query. Se recibe con el nombre: `Evaluacion.sarlaft.actualizacion.formulario`

- Json entrada:

```text
{
  "id": "bd3f120f-c89a-4465-b248-7d223e536e0b",
  "sarlafts": [
    {
      "id": "bd3f120f-c89a-4465-b248-7d223e536e0b",
      "tipoPersona": "N",
      "tipoRiesgo": "ORDINARIO"
    }
  ]
}
```text

- Json salida:

```text
{
  "id": "bd3f120f-c89a-4465-b248-7d223e536e0b",
  "sarlafts": [
    {
      "id": "bd3f120f-c89a-4465-b248-7d223e536e0b",
      "tipoPersona": "N",
      "tipoRiesgo": "ORDINARIO",
      "tipoFormulario": "ORDINARIO_PN",
      "requisitos": [
        {
          "id": "bd3f120f-c89a-4465-b248-7d223e536e0b",
          "codigo": "1330",
          "nombre": "requisito1",
          "estado": "PENDIENTE",
          "vigencia": 30
        }
      ]
    }
  ],
  "error": null
}
```
