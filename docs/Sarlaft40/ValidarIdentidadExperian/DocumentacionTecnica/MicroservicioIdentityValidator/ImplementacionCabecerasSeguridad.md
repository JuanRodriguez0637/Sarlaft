---
title: "Implementación de Cabeceras de Seguridad - identityValidator"
confluence_id: 4007985201
confluence_url: "https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4007985201"
last_modified: "2025-08-04"
author: "632dd1a5234d44d406d0f129"
version: 2
---

# Implementación de Cabeceras de Seguridad - identityValidator

> **Fuente Confluence:** [Implementación de Cabeceras de Seguridad - identityValidator](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4007985201)
> **Última modificación:** 2025-08-04 — versión 2
> **Sección:** [Microservicio - identity validator](./index.md)

Las cabeceras de seguridad permiten asegurar las comunicaciones y verificar la autenticidad de las peticiones. A continuación, se listan algunas de las cabeceras implementadas:

- `Content-Security-Policy`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `X-XSS-Protection`
- `Strict-Transport-Security (max-age)`

### Explicación de los Atributos

- ***Content-Security-Policy (CSP)***: Es una capa adicional de seguridad que ayuda a detectar y mitigar ciertos tipos de ataques, incluyendo Cross Site Scripting (XSS) e inyecciones de datos. La política define qué fuentes de contenido son válidas para el navegador. Los valores posibles son: `"default-src 'self'; script-src 'self'; frame-ancestors 'none'; style-src 'self'; form-action 'self'"`
- ***X-Frame-Options***: La cabecera `X-Frame-Options` protege contra ataques de clickjacking al controlar si una página puede ser mostrada dentro de un `<frame>`, `<iframe>`, o `<object>`. Los valores posibles son `DENY`, `SAMEORIGIN`, o `ALLOW-FROM uri`.
- ***X-Content-Type-Options***: Evita que los navegadores interpreten archivos MIME de una manera incorrecta. Cuando el valor es `nosniff`, la cabecera asegura que el navegador seguirá el tipo de contenido declarado por el servidor.
- ***X-XSS-Protection***: Configura la política del navegador para la detección y bloqueo de ataques XSS. Un valor de `1; mode=block` activará esta protección y bloqueará la página si se detecta un ataque.
- ***Strict-Transport-Security (max-age)***: (HSTS) instruye a los navegadores para que sólo accedan al sitio a través de HTTPS durante un período de tiempo especificado por `max-age` (en segundos). Esto ayuda a prevenir ataques de tipo man-in-the-middle.
- ***Strict-Transport-Security (includeSubDomains)***: Indica a los navegadores que la política HSTS también debe aplicarse a todos los subdominios del dominio actual.

![image-20250804-194750.png](./attachments/image-20250804-194750.png)

![image-20250804-194839.png](./attachments/image-20250804-194839.png)

![image-20250804-194912.png](./attachments/image-20250804-194912.png)

La razón por la cual **las cabeceras de seguridad enviadas por el backend** (como `X-Frame-Options`, `Content-Security-Policy`, etc.) **aparecen visibles en la respuesta al método** `OPTIONS` **pero no en la respuesta del** `POST` en el navegador, tiene que ver principalmente con:

---

## 🔐 Comportamiento de los navegadores y CORS

Cuando haces una solicitud `POST` **cross-origin** (es decir, desde un origen distinto al del backend o con ciertos encabezados especiales), el navegador realiza una **preflight request** usando el método `OPTIONS`. Esta solicitud sirve para preguntar al backend **si está permitido hacer la solicitud real** (`POST`), y en qué condiciones.

---

## 🔎 ¿Por qué se ven las cabeceras en `OPTIONS` y no en `POST`?

### 1. **Cabeceras de seguridad como** `X-Frame-Options`**,** `Content-Security-Policy`**, etc.**

Estas cabeceras **sí las devuelve el backend en ambas respuestas** (OPTIONS y POST), pero:

- El navegador **no expone todas las cabeceras** al JavaScript del frontend por defecto.
- Solo expone al frontend aquellas cabeceras listadas en `Access-Control-Expose-Headers`.

Entonces:

- Si el backend **responde con esas cabeceras de seguridad en** `POST`, **sí están allí**, pero **no las verás** desde JavaScript (como en `fetch().headers`) **a menos que se expongan explícitamente**.
- En cambio, en la respuesta `OPTIONS`, al tratarse de la verificación previa, algunas herramientas de desarrollador del navegador pueden mostrar más claramente esas cabeceras como parte del control CORS.

---

### 2. **El navegador protege al usuario**

Las cabeceras como:

- `Strict-Transport-Security`
- `Content-Security-Policy`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `X-XSS-Protection` (obsoleta pero aún se ve en algunos sistemas)

…son **cabeceras orientadas a la seguridad del navegador**, no al frontend como tal. Por eso:

- **Se aplican directamente por el navegador**, no están pensadas para que el frontend lea o use.
- **No se exponen en** `fetch().headers` **a menos que uses** `Access-Control-Expose-Headers`.

---

## ✅ ¿Cómo hacer que se vean desde el frontend?

Si por alguna razón necesitas que esas cabeceras se expongan y puedan ser vistas desde JavaScript en el frontend, el backend debe incluir esta cabecera:

```http
Access-Control-Expose-Headers: X-Frame-Options, Strict-Transport-Security, X-Content-Type-Options, Content-Security-Policy, X-XSS-Protection
```

Esto le indica al navegador:

> "Está bien que JavaScript en el cliente pueda acceder a estas cabeceras".

---

## 🧪 ¿Cómo verificar si están?

En las herramientas de desarrollo del navegador:

1. Ve a la pestaña "Red" (Network).
2. Haz clic en la petición `POST`.
3. Mira las cabeceras de respuesta completas (no solo las accesibles desde JS).

Ahí verás si realmente el backend las está devolviendo.

---

## 📌 En resumen:

| Comportamiento | Explicación |
|---|---|
| Las cabeceras se ven en `OPTIONS` pero no en `POST` | Porque el navegador muestra más información en el preflight, y no expone ciertas cabeceras por seguridad |
| ¿El backend sí las envía en `POST`? | Sí, pero el navegador no las deja ver desde JavaScript a menos que uses `Access-Control-Expose-Headers` |
| ¿Son necesarias para el frontend? | No para lógica JS, pero sí para proteger el navegador (clickjacking, XSS, etc.) |

---

### 📌 ¿Por qué se ve primero un `OPTIONS` y luego un `POST`?

Cuando haces una solicitud `POST` desde el **frontend** a otro dominio (por ejemplo, de `frontend.miapp.com` a `api.miempresa.com`), el navegador quiere asegurarse de que ese dominio (la API) **permita solicitudes desde el origen del frontend**. Para eso, **envía primero una petición** `OPTIONS` antes de hacer la `POST`.

Esta petición previa se llama **preflight request** y su propósito es:

> Verificar si el servidor acepta la solicitud real (por ejemplo, POST con JSON y cabeceras personalizadas) **desde el origen de tu app**.

---

### 🔍 ¿Cuándo se dispara una preflight (OPTIONS)?

Una petición `OPTIONS` se dispara automáticamente por el navegador cuando se cumplen ciertos criterios, como:

- El método HTTP es **diferente de GET, HEAD o POST simple** (por ejemplo `PUT`, `DELETE` o `POST` con JSON).
- Se usan **cabeceras personalizadas**, como `Authorization`, `Content-Type: application/json`, etc.
- Se usan **tipos de contenido** distintos de `application/x-www-form-urlencoded`, `multipart/form-data` o `text/plain`.

---

### 🔐 ¿Cómo responde el servidor a ese `OPTIONS`?

El servidor debe responder con cabeceras como:

```http
Access-Control-Allow-Origin: https://frontend.miapp.com
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization
```

Si no lo hace, la petición `POST` **no se enviará** y el navegador bloqueará la solicitud.

---

### ✅ Solución común (desde el backend)

Asegúrate de que tu backend:

- Responda a solicitudes `OPTIONS`.
- Devuelva las cabeceras **CORS** adecuadas.
- Permita los métodos y cabeceras que usas.
