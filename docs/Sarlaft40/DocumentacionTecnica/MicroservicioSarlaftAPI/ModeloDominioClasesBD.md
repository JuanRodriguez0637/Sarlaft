# Modelo Dominio, Clases y BD - SarlaftAPI

> **Fuente Confluence:** [Modelo Dominio, Clases y BD - SarlaftAPI](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1809908116)
> **Última modificación:** 2021-07-16 — Diana Muñoz · versión 4
> **Sección:** [Microservicio SarlaftAPI](./index.md)
## Modelo de Dominio

Define las entidades de negocio principales y sus relaciones en el sistema SARLAFT 4.0.

![Modelo de Dominio](./attachments/domain_diagram.jpg)

---

## Modelo de Clases

Representa la estructura orientada a objetos del proyecto (clases Java del dominio).

![Modelo de Clases](./attachments/class_diagram.jpg)

---

## Modelo de Base de Datos

Describe las tablas, columnas y relaciones del esquema de persistencia en PostgreSQL.

![Modelo BD - versión completa](./attachments/domain_model_-DB.jpg)

![Modelo BD - diagrama adicional](./attachments/db_diagram.jpg)

---

## Archivo DrawIO

El archivo fuente editable (`.xml`) se descargó en: [img/domain_model_.xml](./attachments/domain_model_.xml)

También disponible en SharePoint:  
[domain_model_.xml en SharePoint](https://suramericana-my.sharepoint.com/:u:/g/personal/ldmunoz_sura_com_co/EV1E6FrlpFBKmWmGcUqhXKwB9njsduoUFQLg9kAd56qSVQ?e=ZOMay0)

---

## Referencias

- [Configuración Base de Datos R2DBC](./EstructuraProyecto/ConfiguracionBaseDatosR2DBC.md) — detalles de la configuración R2DBC sobre PostgreSQL
- [Estructura Proyecto](./EstructuraProyecto/index.md) — organización hexagonal del código
