# Servicio Evaluación Validación Sarlaft

>**Fuente:**[Ver en Confluence](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814233305)
>**Fecha extracción:**2026-03-27

**Objetivo:**Permite realizar las validaciones mínimas para clasificar el riesgo de un cliente y determinar el tipo de sarlaft que debe diligenciar de acuerdo a la naturaleza del cliente y del producto.Se denomina como un proceso de evaluación dado que según el resultado de información del tomador, se indica que información debe solicitarse para los asegurados y beneficiarios.

Taambien permite realizar el proceso de reclamaciones adjuntos encontraremos las 2 peticiones que de REPN Y REPJ, correspondiente mente para reclamaciones de PN y PJ

**Endpoint:**/sarlaftserv/assessment

**Perfil de Seus4:**PF_CONSUMSERVSARLAFTAPI

**Nuevo Endpoint:**POST /sarlaftserv/v1/evaluaciones

**Perfil de Seus4:**aun no creado para consumo interno a SURA.

**Ejemplo Json Request:**

[![imagen](https://segurosti.atlassian.net/wiki/download/thumbnails/1814233305/AsessmentREPJ.json?version=6&modificationDate=1644335921066&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/1814233305/AsessmentREPJ.json?version=6&modificationDate=1644335921066&cacheVersion=1&api=v2)[![imagen](https://segurosti.atlassian.net/wiki/download/thumbnails/1814233305/AsessmentREPN.json?version=5&modificationDate=1644335917726&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/1814233305/AsessmentREPN.json?version=5&modificationDate=1644335917726&cacheVersion=1&api=v2)[![imagen](https://segurosti.atlassian.net/wiki/download/thumbnails/1814233305/TomadorPJ.json?version=1&modificationDate=1628694835521&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/1814233305/TomadorPJ.json?version=1&modificationDate=1628694835521&cacheVersion=1&api=v2)[![imagen](https://segurosti.atlassian.net/wiki/download/thumbnails/1814233305/Assessemt.json?version=3&modificationDate=1627481523529&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/1814233305/Assessemt.json?version=3&modificationDate=1627481523529&cacheVersion=1&api=v2)

**Dependencias:**

Base de Datos Saralft

Motor de Reglas - API

Validaciones de Peps - Mensajería

Validación de Listas Vinculantes  - Mensajería

Nota: Para el cotizador de vida se agrego un nuevo campo de tipoFormulario en el cual devuelve el tipo de formulario por salraft, especialmente para este egv.
