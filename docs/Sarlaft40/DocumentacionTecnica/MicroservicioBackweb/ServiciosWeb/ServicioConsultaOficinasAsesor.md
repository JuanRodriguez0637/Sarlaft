# Servicio de consulta Oficinas Por Asesor

> **Fuente Confluence:** [Servicio de consulta Oficinas Por Asesor](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2676228312)
> **Última modificación:** 2022-07-07 — Diana Muñoz · versión 3
> **Sección:** [Servicios Web - Microservicio Backweb](./index.md)

- **Objetivo:** Permite consultar por medio del código de asesor los datos de: `nombreasesor`, lista de oficinas (oficina/sucursal/promotora/triada) con los datos de: `codigoOficina`, `nombreOficina`, `codigoCanal`, `tipoOficina`, `indicadorOficinaRadicacion`

- **Endpoint:** `/sarlaftbackweb/adviser/bureau`

- **Perfil de Seus4:** `PF_REDCOMAPICON`

- **Ejemplo Request:**

- **Request Json:**

  ```json
  {
      "codigoAsesor": "10874"
  }
  ```

- **Response:**

  ```json
  {
      "codigoAsesor": "10874",
      "nombreAsesor": "FLOR ALBA AGUIRRE CEBALLOS CQLII",
      "oficinas": [
          {
              "codigoOficina": "2607",
              "nombreOficina": "PROM ARRENDAMIENTO",
              "codigoCanal": "CC011",
              "tipoOficina": "15",
              "indicadorOficinaRadicacion": "false"
          },
          {
              "codigoOficina": "2608",
              "nombreOficina": "PROM PROSEAR SEGUROS",
              "codigoCanal": "CC011",
              "tipoOficina": "15",
              "indicadorOficinaRadicacion": "true"
          },
          {
              "codigoOficina": "2818",
              "nombreOficina": "SUCURSAL CORPORATIVO BOGOTA",
              "codigoCanal": "CC004",
              "tipoOficina": "3",
              "indicadorOficinaRadicacion": "false"
          },
          {
              "codigoOficina": "2819",
              "nombreOficina": "GRAN EMPRESA BOGOTA",
              "codigoCanal": "CC044",
              "tipoOficina": "3",
              "indicadorOficinaRadicacion": "false"
          }
      ]
  }
  ```
