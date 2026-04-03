---
title: "Guía Básica Azure"
confluence_id: 2624749588
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2624749588"
last_modified: "2022-02-24"
author: "Camila White (Unlicensed)"
version: 2
---

# Guía Básica Azure

> **Fuente Confluence:** [Guía Básica Azure](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2624749588)
> **Última modificación:** 2022-02-24 — Camila White (Unlicensed) · versión 2
> **Sección:** [Ingesta de datos Teradata](./index.md)

En este documento se realizará una explicación sencilla de como crear los elementos en los servicios de Azure usados para el transporte de información desde Azure PostgreSQL a Teradata.

### Azure Key Vault

Lo primero a tener en cuenta es la creación de un secreto desde Key Vault. Para esto, se requiere entrar al servicio, luego a la opción Secrets y seleccionar Generate/Import.

![Key Vault - Secrets](./attachments/image-20220224-211720.png)

Ingresar el nombre del secreto que se desea crear, el valor a almacenar y por último dar click en crear.

![Crear secreto](./attachments/image-20220224-214948.png)

### Databricks

Para crear un notebook/directorio en databricks, dar click en alguna de las flechas seleccionadas (dependiendo de donde se desee crear)

![Databricks - crear notebook](./attachments/image-20220224-215225.png)

Y seleccionar del menú la opción deseada.

![Databricks - menú opciones](./attachments/image-20220224-220058.png)

### Data Factory

Ingresar al servicio de Data Factory

![Data Factory - inicio](./attachments/image-20220224-220404.png)

#### Linked Services

Lo primero a crear son los linked services necesarios para conectar Data Factory con otros servicios

![Linked Services](./attachments/image-20220224-221240.png)

Seleccionar el servicio necesario, en este caso la demostración será con el servicio Azure Data Lake Storage.

![Seleccionar servicio](./attachments/image-20220224-221549.png)

Ingresar los datos requeridos para la creación

![Crear linked service](./attachments/image-20220224-221714.png)

y luego dar click en crear.

#### Datasets

Ir a la vista de autor de Data Factory

![Vista autor Data Factory](./attachments/image-20220224-222150.png)

y crear un nuevo data set

![Nuevo dataset](./attachments/image-20220224-222234.png)

Seleccionar el servicio al que se le quiere crear el dataset y continuar

![Seleccionar servicio dataset](./attachments/image-20220224-222327.png)

Ingresar el nombre del nuevo dataset y el linked service correspondiente

![Configurar dataset](./attachments/image-20220224-222441.png)
