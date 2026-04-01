# Servicio Resultado Carga Masiva Excel

> **Fuente Confluence:** [Servicio Resultado Carga Masiva Excel](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2653683726)
> **Última modificación:** 2022-08-08 — Diego Alejandro Vélez González · versión 3
> **Sección:** [Procesos Carga Masiva](./index.md)
- **Objetivo:** Obtener el archivo con el resultado de la carga masiva.
- **Endpoint:** `/sarlaftserv/file/getResult`
- **Perfil de Seus4:** `PF_CONSUMSERVSARLAFTAPI`
- **Method:** `POST`

**Ejemplo Request:**

> **Nota:** El id de la carga debe estar registrado en cache en la cual contiene información del documento que se debe descargar. Información → [Carga Excel Carga Masiva](../ServiciosWeb/CargaExcelCargaMasiva.md)

![Ejemplo Request](./attachments/ServicioResultadoCargaMasiva_request.png)

**Ejemplo Response:**

> **Nota:** Al consumirse el servicio desde un navegador descargara directamente el archivo.

![Ejemplo Response](./attachments/ServicioResultadoCargaMasiva_response.png)

**Parámetros Body:**

- **idCarga:** Indicador de la carga masiva.
