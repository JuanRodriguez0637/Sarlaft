---
title: "Pruebas"
confluence_id: 2471919690
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2471919690"
last_modified: "2021-10-28"
author: "5da8927fa627f40c2f3c20ac"
version: 4
---

# Pruebas

> **Fuente Confluence:** [Pruebas](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2471919690)
> **Última modificación:** 2021-10-28 — versión 4
> **Sección:** [Front (Web Component)](./index.md)

> **📝 Nota:** En esta documento se indica lo relacionado a las pruebas y validaciones que se tienen de la solución

## Pruebas unitarias

Para generar la revisión de las pruebas y generar los reportes html se debe ejecutar este comando:

```
npm run test
```

Debe abrir una nueva ventana del navegador así:

![image-20211028-191716.png](./attachments/image-20211028-191716.png)

> **📝 Nota:** Se debe validar que todas las pruebas pasen y no se generen warnings

![image-20211028-191904.png](./attachments/image-20211028-191904.png)

---

Para ejecutar las pruebas como se hace en los despliegues se debe ejecutar este comando:

```
npm run test-headless
```

## Análisis de código estático

### Sonar

Es posible hacer un análisis estático del código con sonar, donde se validan reglas generales, para esto se debe ejecutar el comando:

NOTA: para que funcione se debe tener JRE, conexión a la VPN y permisos en sonar de sura

```
npm run sonar
```

luego que termine debe salir un log así

![image-20211028-193411.png](./attachments/image-20211028-193411.png)

Entrar a sonar https://sonar.suramericana.com.co/ usuario runner password runner

Y buscar el nombre de proyecto configurado en el archivo "sonar-project.properties" la variable `sonar.projectName` al momento de crear este documento `local-identityvalidatorfr`

![image-20211028-193732.png](./attachments/image-20211028-193732.png)

> **📝 Nota:** Este análisis solo es preventivo, ya que las reglas configuradas en sura son diferentes

### Eslint

Se recomienda instalar el plugin de Eslint en el IDE que esté utilizando. Adicional se puede hacer una revisión con esta herramienta con el comando:

```
npm run lint
```

Lo cual debe generar un reporte de lo encontrado así:

![image-20211028-194523.png](./attachments/image-20211028-194523.png)
