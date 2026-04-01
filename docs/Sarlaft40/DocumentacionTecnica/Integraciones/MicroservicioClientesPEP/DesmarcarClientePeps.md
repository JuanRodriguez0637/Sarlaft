# Desmarcar cliente peps.

> **Fuente Confluence:** [Desmarcar cliente peps.](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2968715406/Desmarcar+cliente+peps.)
> **Última modificación:** 2022-11-02 — juan camilo muñoz burgos (Unlicensed) · versión 1
> **Sección:** [Microservicio - Clientes PEP](./index.md)

**Objetivo**:

Desmarcar un cliente como pep.

**Endpoint: **/pepsserv/pep/uncheck

**Perfil Seus4: **PF_CONSUMSERVPEPSAPI

**Comunicación:**

**Descripción**: Servicio que permite desmarcar a un cliente peps, es decir, elimina de la caché el respectivo DNI del cliente y marca las preguntas 3, 5 y 7 de la base de datos de riesgos consultables con la opción 2 (NO) y asignando una fecha de baja, para indicar que el cliente ya no pertenece a la lista de PEPS de la compañía.

**Request:**

{ "dniClient": "C18762181", "application": "9995", "requestDni": "C0000002"}**Response:**

{ "uncheck": true, "message": null}

**Dependencias :**

Base de datos Oracle
