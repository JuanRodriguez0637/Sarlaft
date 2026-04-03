---
title: "Configuración de ambiente (Front)"
confluence_id: 2460057615
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2460057615"
last_modified: "2023-07-31"
author: "632dd1a5234d44d406d0f129"
version: 9
---

# Configuración de ambiente (Front)

> **Fuente Confluence:** [Configuración de ambiente](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2460057615)
> **Última modificación:** 2023-07-31 — versión 9
> **Sección:** [Front (Web Component)](./index.md)

La aplicación está construida en el framework de [Angular](https://angular.io/) y se utiliza la funcionalidad de [Angular Elements](https://angular.io/guide/elements) para crear un Web Component que luego se puede incrustar en otras aplicaciones.

## Prerrequisitos

- tener instalado nodejs https://nodejs.org/es/ ,se valida con el comando en una consola "node -v"
- tener instalado un IDE como visual studio code (VSC), webstroms, etc (para este manual se utilizo VSC https://code.visualstudio.com/)
- Crear una entrada en el archivo de host `C:\Windows\System32\drivers\etc\` la siguiente entrada:

```
127.0.0.1 		localhost.sura.com.co
```

## Pasos

### Clonar repositorio

```
git clone https://SuraColombia@dev.azure.com/SuraColombia/Gerencia_Tecnologia/_git/adm_y_fin-validadorcliente-identidad-fr
cd adm_y_fin-validadorcliente-identidad-fr
```

### Instalar paquetes NPM

```
npm install
```

### Validar configuración

1- Ajustar a que back esta conectado, esto se revisa en el archivo `environment.dev.ts`, por lo general se prueba contra dllo, así como esta en el repositorio

> **📝 Nota:** Verificar que se tenga conectada la VPN de sura

![image-20211021-195940.png](./attachments/image-20211021-195940.png)

```
urlExperianMs: 'https://sarlaftapi.labsura.com/'
urlExperianMs: 'http://localhost.sura.com.co:8080/'
urlExperianMs: 'http://experianapi.mocklab.io/'
```

> **⚠️ Nota:** Como este componente esta construido para funcionar como WebComponent, cuando se ejecute en local no va a generar ninguna aplicacion web, por lo que hay que tener en cuenta el siguiente ajuste

2- Ajuste de código para pruebas, debería quedar comentado y des comentado el siguiente código:

- `app.module.ts`: debería quedar comentado y des comentado el siguiente código

![image-20211021-201244.png](./attachments/image-20211021-201244.png)

- `app.component.ts`

![image-20211021-201610.png](./attachments/image-20211021-201610.png)

con este ajuste, se pueden modificar los datos de entrada mas comunes que serian los de la variable `informaciongeneral = '{"tipoIdentificacion": "C","numeroIdentificacion": "71263094","primerNombre": "JUAN","segundoNombre": "CAMILO","primerApellido": "ZAPATA","segundoApellido": "ALVAREZ","numeroCelular": "3007749736","fechaExpedicion": "2020-01-01","rol": "RL","producto": "VIDA","ramo": "Vida Grupo","codigoRamo":"041","dniAsesor": "C71263094","celularAsesor": "3007749737" }';`

3. **Generar token**: para consumir los servicios de back se debe generar un token valido, para ello se puede hacer de estas 2 formas:

1-

- Ingresar a la url http://seusdllo.suranet.com/
- usuario y password pedrvevi
- Tomar el token de la cookie, de la variable **appTagDllo**
- ![image-20211028-155134.png](./attachments/image-20211028-155134.png)

  consumir el servicio https://sarlaftapi.dllosura.com/api/v1/security/token metodo GET

  - Con los headers:
    - `X-APPTAG-TOKEN` = token copiado del paso anterior
    - `X-APP` = "SARLAFT"

2- Con postman se pueden ingresar las credenciales del usuario "impmasivos" (el password se debe solicitar al o los analistas encargados)

![image-20211029-014404.png](./attachments/image-20211029-014404.png)

- Con el header:
  - `X-APP` = "SARLAFT"

- Esto nos entrega un token de esta forma:

  ```json
  {
      "token": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJJZGVudGl0eVZhbGlkYXRvciIsInN1YiI6IlNBUkxBRlQiLCJpc3MiOiJTdXJhLmNvbSIsImV4cCI6MTYzNTQ0MDE0MiwiaWF0IjoxNjM1NDM2NTQyfQ.XiMyNl9OCVo8MLsfs_XD8otd56Dh0cTWBhyioSzP40w",
      "aplicacion": "SARLAFT"
  }
  ```

  - Se toma lo que esta en "token" y se copia en `app.component.ts` en la variable token

![image-20211028-160027.png](./attachments/image-20211028-160027.png)

### Ejecutar el proyecto

```
npm run start
```

Si todo funciona correctamente se debe ver un log parecido a este

![image-20211021-200406.png](./attachments/image-20211021-200406.png)

Ir a un navegador a la url http://localhost.sura.com.co:4200/

Se debe ver algo similar a esto

![image-20211028-160240.png](./attachments/image-20211028-160240.png)

### Consumo de servicios de back

Para validar que se consuman los servicios, dar click en el botón, aceptar los términos y dar en el siguiente botón, si sale una pantalla de lo sentimos como esta, posiblemente es por que se deben autorizar los certificados.

![image-20211028-160623.png](./attachments/image-20211028-160623.png)

ir a la consola con F12, y abrir alguna de las url dando click derecho y en la opción abrir en una nueva pestaña

![image-20211028-160744.png](./attachments/image-20211028-160744.png)

y se deben indicar que se procesa a ir a la url

![image-20211028-160822.png](./attachments/image-20211028-160822.png)

luego de eso, volver a la aplicación recargar y hacer el proceso de nuevo (Consumo de servicios de back)

Aquí se confirma que se estén consumiendo

![image-20211028-161101.png](./attachments/image-20211028-161101.png)

## Prueba consumo web component

Si se requiere probar el consumo del WC, se puede hacer lo siguiente:

- Compilar el WC con el comando según el ambiente, por ejemplo desarrollo:

```
npm run build_dev:elements
```

- **Archivos**: Cuando compile correctamente buscar los siguientes 2 archivos en la ruta de `dist/identityvalidatorfr`
  - `webcomponent-main.js`
  - `styles.css`
- en una ruta a parte, por fuera del proyecto crear un archivo html con el siguiente contenido

<details>
<summary>test.html</summary>

```html
<!doctype html>

<html lang="en">

<head>

  <meta charset="utf-8">

  <title>InitialApp</title>

  <base href="/">

  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="icon" type="image/x-icon" href="favicon.ico">

  <link href="styles.css" rel="stylesheet">

</head>

<body>

  <validacionidentidad-app
    token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJJZGVudGl0eVZhbGlkYXRvciIsInN1YiI6IlNBUkxBRlQiLCJpc3MiOiJTdXJhLmNvbSIsImV4cCI6MTYzNTQ1ODE4NCwiaWF0IjoxNjM1NDU0NTg0fQ.bvbt6RHAIK1IYxunbfav98VIyDWdbzbTlGw9L3dTiEQ'
    idaplicacionorigen='SARLAFT' idevaluacionsarlaft='123456' idTransaccion='23423423423' tipollamado='redireccion'
    informaciongeneral='{
      "tipoIdentificacion": "C",
      "numeroIdentificacion": "14544587",
      "primerNombre": "ANDRES",
      "segundoNombre": "PEREZ",
      "primerApellido": "PEREZ",
      "segundoApellido": "ALVAREZ",
      "numeroCelular": "3007149216",
      "fechaExpedicion": "2020-01-01",
      "rol": "RL",
      "producto": "VIDA",
      "ramo": "Vida Grupo",
      "dniAsesor": "C71263093",
      "celularAsesor": "3007749737"
    }' (resultevent)="result($event)">
  </validacionidentidad-app>

  <script type="text/javascript" src="webcomponent-main.js"></script>

</body>

</html>
```

</details>

- ubicarse en la raíz de la nueva ruta e instalar la librería serve (https://www.npmjs.com/package/serve), con este comando

```
npm i -g serve
```

- Buscar y editar el archivo **serve.js** que debería estar en la ruta `{nombreUsuario}\AppData\Roaming\npm\node_modules\serve\bin\`
  - Se debe buscar la palabra localhost y reemplazarla por localhost.sura.com.co
  - Se debe buscar la palabra 5000 y reemplazarla por 4200
- Copiar los archivos del punto "**Archivos**" y dejarlos en la raíz del html
- Volver a la consola y ejecutar el comando "serve"

![image-20211029-030631.png](./attachments/image-20211029-030631.png)

> **⚠️ Nota:** Tener en cuenta pasar un token valido en la variable `token='Bearer ....'`

## Scripts de NPM

Estos son los comandos más usados en `package.json`:

- `npm run build_dev:elements` - Permite construir la aplicación para el entorno de desarrollo, la aplicación construida se alojara en la carpeta `dist/`.
- `npm run build_lab:elements` - Permite construir la aplicación para el entorno de laboratorio, la aplicación construida se alojara en la carpeta `dist/`.
- `npm run build:elements` - Permite construir la aplicación para el entorno de producción, la aplicación construida se alojara en la carpeta `dist/`.
- `npm run test-headless` - Permite ejecutar las pruebas unitarias de la aplicación
- `npm run sonar` - Realiza una solicitud de análisis de código estático en Sonar.
