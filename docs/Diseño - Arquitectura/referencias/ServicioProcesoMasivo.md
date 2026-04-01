# Servicio Proceso Masivo

>**Fuente:**[Ver en Confluence](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2093350926)
>**Fecha extracción:**2026-03-27

**Objetivo:**Permite validar el estado del sarlaft de un cliente para un proceso de validación, enviando varios negocios en una sola invocación, el tamaño máximo permitido es de 100 pólizas. Es un proceso asíncrono. Aplica para expedición de pólizas colectivas que tienen muchos riesgos o pólizas individuales con una gran cantidad de riesgos.

**Endpoint:**/sarlaftserv/assessment/massive

**Perfil de Seus4:**PF_CONSUMSERVSARLAFTAPI

**Ejemplo Json Request:**

[![imagen](https://segurosti.atlassian.net/wiki/download/thumbnails/2093350926/jsonMasivo_100.json?version=2&modificationDate=1622554032842&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/2093350926/jsonMasivo_100.json?version=2&modificationDate=1622554032842&cacheVersion=1&api=v2)

**Dependencias:**

RabbitMQ Sarlaft

Genera el evento Sarlaft.batch.start
