# Implementación de Cabeceras de Seguridad

> **Fuente Confluence:** [Implementación de Cabeceras de Seguridad](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4007952431/Implementaci%C3%B3n+de+Cabeceras+de+Seguridad)
> **Última modificación:** 2024-09-02 — Julián Andrés Curubo García · versión 3
> **Sección:** [Microservicio SarlaftAPI](./index.md)

---

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

![image-20240902-223852.png](./img/image-20240902-223852.png)
