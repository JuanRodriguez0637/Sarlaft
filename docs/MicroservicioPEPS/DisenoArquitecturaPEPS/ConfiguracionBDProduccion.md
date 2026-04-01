# Configuración base de datos en producción

> **Fuente Confluence:** [https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4516380673](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4516380673)
> **Fecha extracción:** 2026-03-30

La configuración de la base de datos a oracle

`datasource-pdn`

`datasource-pdnha`

Se ajusta con `LOAD_BALANCE=ON` para que se aplique correctamente el balanceo al acceder a la base de datos en producción.

El microservicio debe estar en la ultima versión de java 8.
