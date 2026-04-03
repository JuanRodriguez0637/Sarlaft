---
title: "Parametrización de un nuevo subramo o producto"
confluence_id: 5227118615
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5227118615"
last_modified: "2025-12-15"
author: "Antiguo usuario (Deleted)"
version: 1
---

# Parametrización de un nuevo subramo o producto

> **Fuente Confluence:** [Parametrización de un nuevo subramo o producto](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5227118615)
> **Última modificación:** 2025-12-15 — Antiguo usuario (Deleted) · versión 1
> **Sección:** [Documentación de Solicitudes](./index.md)

## Objetivo

Definir el proceso estándar para la parametrización de nuevos productos o subramos en el módulo administrativo de Sarlaft

## Insumos Base

Los scripts y tablas que deben utilizarse para realizar la parametrización se encuentran en los [**insumos operación sarlaft**](https://suramericana.sharepoint.com/sites/MESA7-CALIDADDEINFORMACIN/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FMESA7%2DCALIDADDEINFORMACIN%2FShared%20Documents%2FGeneral%2FProyecto%20SARLAFT%204%2E0%2FDocumentacionDesarrollo%2FInsumos%20Base&viewid=95cc38c2%2D5a58%2D4e15%2Da124%2Dbcdac91ae443&csf=1&web=1&e=Zp6moh&CID=757b6b95%2D8b8f%2D489a%2D974e%2D5b8ce96328e4&FolderCTID=0x012000CD5B148735D16E46A8957895F03860C0). Estos incluyen:

- Scripts de inserción para la parametrización.
- Tablas del modelo Sarlaft donde se registran parámetros y relaciones.

## Pasos del Procedimiento

### Validación previa

- Confirmar que el nuevo producto o subramo está aprobado por el área de negocio.
- Verificar que los códigos no existan previamente en la base de datos.
- Validar que el script que se utilizará es correcto (conversar con el/la encargad(a) de sarlaft).

### Ejecución de la parametrización

- Utilizar los scripts que se encuentran en el **punto 4** definidos en los insumos base para:
  - Registrar el nuevo subramo con su descripción y código.
  - Relacionar el subramo con la compañía, canal y ramo correspondiente.

### Validación posterior

- Confirmar que los registros se insertaron correctamente.
- Validar que los nuevos elementos aparecen en el módulo administrativo.

## 6. Consideraciones

- Mantener consistencia en nomenclatura y códigos.
- Posiblemente los cambios no se reflejen inmediatamente en el front, entonces esperar un día a que se refresque la caché.
