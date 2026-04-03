---
title: "Adicionar códigos de respuesta asociados al estado FALLIDO de DOCUMENT_PN"
confluence_id: 3816062992
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3816062992"
last_modified: "2024-06-14"
author: "712020:4aad602b-cb7e-4e43-9a12-a37bb1f4a89f"
version: 4
---

# Adicionar códigos de respuesta asociados al estado FALLIDO de DOCUMENT_PN

> **Fuente Confluence:** [Adicionar códigos de respuesta asociados al estado FALLIDO de DOCUMENT_PN](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3816062992)
> **Última modificación:** 2024-06-14 — versión 4
> **Sección:** [IV001: Validar documento de identidad con Registraduría](./index.md)

### 1. Parametrización de Nuevos Códigos de Estado

#### Inserción de Nuevos Parámetros

Se han agregado los siguientes parámetros a la base de datos para registrar distintos estados de respuesta:

```sql
INSERT INTO sarlaft.tsaf_catalogo
(cdcatalogo, febaja, fecreacion, dsnombre, feactualizacion)
VALUES('TIPO_RESPUESTA_REGISTRADURIA', NULL, NOW(), 'Tipo Respuesta Registraduria', NOW());

INSERT INTO sarlaft.tsaf_catalogo
(cdcatalogo, febaja, fecreacion, dsnombre, feactualizacion)
VALUES('TIPO_RESPUESTA_MIGRACION', NULL, NOW(), 'Tipo Respuesta Migracion', NOW());

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Cancelada por muerte o fallecido', '21', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Vigente', '00', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'En trámite', '99', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Cancelado', '6', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Activo', '1', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Inactivo', '2', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Clave vencida', '17', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'No existe este número de identificación en los archivos de validación de la base de datos', '09', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Tipo de documento errado', '04', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Número de documento errado', '05', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Apellido errado', '06', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Clave no habilitada', '18', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Clave de consulta bloqueada', '12', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'No existe este número de identificación en los archivos de validación de la base de datos', '09', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'El apellido no coincide con el registrado en la Registraduría Nacional del Estado Civil', '10', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'El apellido digitado sí coincide con el registrado en la base de datos para ese número de cédula, pero la persona no tiene información comercial en la base de datos de Data Crédito', '14', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'No se pudo realizar la consulta, vuelva a intentar más tarde', '23', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Fin consulta tipo 2- No aplica. Notificar a Data Crédito', '07', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Fin consulta tipo 4- No aplica. Notificar a Data Crédito', '08', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_REGISTRADURIA');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Tipo de documento errado', '04', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Número de documento errado', '05', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'No se pudo realizar la consulta, vuelva a intentar', '23', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');

INSERT INTO sarlaft.tsaf_parametro
(cdsubparametro, dsdescripcion, cdparametro, febaja, fecreacion, feactualizacion, cdcatalogo)
VALUES('', 'Código de suscriptor no existe', '01', NULL, NOW(), NOW(), 'TIPO_RESPUESTA_MIGRACION');
```

### 2. Estados de Respuesta Asociados al Estado FALLIDO

#### Servicio: Consulta con la Registraduría

URL: https://demo-servicesesb.datacredito.com.co/wss/dhws3/services/DHServicePlus

Códigos de Estado:

- `04`: Tipo de documento errado
- `05`: Número de documento errado
- `06`: Apellido errado
- `09`: No existe este número de identificación en los archivos de validación de la base de datos
- `10`: El apellido no coincide con el registrado en la Registraduría Nacional del Estado Civil

#### Servicio: Consulta con Migración

URL: https://demo-servicesesb.datacredito.com.co:444/da/migracion/v1/persona

Códigos de Estado:

- `09`: No existe este número de identificación en los archivos de validación de la base de datos
- `14`: El apellido digitado sí coincide con el registrado en la base de datos para ese número de cédula, pero la persona no tiene información comercial en la base de datos de Data Crédito
- `04`: Tipo de documento errado
- `05`: Número de documento errado

### 3. Códigos Asociados al Estado de FALLA TÉCNICA

#### Registraduría

- `07`: Fin consulta tipo 2 - No aplica. Notificar a Data Crédito
- `08`: Fin consulta tipo 4 - No aplica. Notificar a Data Crédito
- `12`: Clave de consulta bloqueada
- `17`: Clave vencida
- `18`: Clave no habilitada
- `23`: No se pudo realizar la consulta, vuelva a intentar más tarde

#### Migración

- `23`: No se pudo realizar la consulta, vuelva a intentar
- `01`: Código de suscriptor no existe

### 4. Modificaciones en Componentes

Para reflejar estos cambios en la interfaz de usuario y la lógica de backend, se realizaron las siguientes modificaciones:

#### Componentes Modificados:

- **identityvalidatorsms**: Servicio `/api/v1/registry/validate`
- **sarlaftidentity mi**: Respuesta dada al escuchar el comando `Client.validation.finish`
- **sarlaftbackweb**: Adicionar y mapear el nuevo código de respuesta para la evidencia `DOCUMENTO_PN`
- **sarlaftapi ms**: Al escuchar el comando `Client.validation.finish` guardar en el campo `cdestado_documento` el nuevo código de respuesta.
- **front sarlaft**: Modificar pantallas indicadas en la HU para mostrar la causal de registraduría/migración en el campo "Causal registraduría/Migración".

### 5. Creación de un nuevo módulo en sarlaftidentity mi

Además se creó un nuevo módulo para refactorizar el código:

![image-20240614-170338.png](./attachments/image-20240614-170338.png)

La nueva clase:

![image-20240614-170407.png](./attachments/image-20240614-170407.png)

![image-20240614-170417.png](./attachments/image-20240614-170417.png)

### 6. Ejemplo con los códigos de respuesta asociados a DOCUMENT PN:

![image-20240614-170746.png](./attachments/image-20240614-170746.png)

![image-20240614-170759.png](./attachments/image-20240614-170759.png)

- Cuando no coincide con el apellido:

![image-20240614-170832.png](./attachments/image-20240614-170832.png)

- Documento vigente y exitoso:

![image-20240614-170846.png](./attachments/image-20240614-170846.png)

- Cuando es una persona fallecida:

![image-20240614-171142.png](./attachments/image-20240614-171142.png)

- Cuando el documento de cédula extranjería no existe:

![image-20240614-171249.png](./attachments/image-20240614-171249.png)

- Con un documento de Extranjería existente:

![image-20240614-171313.png](./attachments/image-20240614-171313.png)
