# Configuración base de datos en producción

> **Fuente Confluence:** [Configuración base de datos en producción](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4516380673)
> **Espacio:** EPA
> **Última modificación Confluence:** 2025-02-28 | Versión 1
> **Sección:** [Diseño y Arquitectura PEPS MS](./index.md)

La configuración de la base de datos a oracle

`datasource-pdn`

`datasource-pdnha`

Se ajusta con `LOAD_BALANCE=ON` para que se aplique correctamente el balanceo al acceder a la base de datos en producción.

El microservicio debe estar en la ultima versión de java 8.
