# Servicio Marcar Cliente PEPS

> **Fuente Confluence:** [https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814200586](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814200586)
> **Espacio:** EPA
> **Última modificación Confluence:** 2022-11-02 | Versión 2

- **Objetivo:** Permite marcar un cliente como peps, en caso de no existir la persona en el modelo de clientes de sura, esta es creada para poder realizar la marcación. En caso de que el cliente ya se encuentra marcado como peps, el servicio devolverá true, acudiendo al principio de idempotencia.
- **Endpoint:** `/pepsserv/pep/mark`
- **Perfil de Seus4:** `PF_CONSUMSERVPEPSAPI`
- **Ejemplo Json Request:**

[request.json](./attachments/request.json)
[request_mark.json](./attachments/request_mark.json)

- **Dependencias:**
  - Base de Datos `PDN` y `PDNHA`
  - Servicio de Consulta de Personas en Servicios WebSIC
    - URL: [https://sic.suranet.com/ServiciosWebSic/services/ActualizacionModeloClientesWS](http://appslab.suranet.com:80/ServiciosWebSic/services/ActualizacionModeloClientesWS)
  - Servicio de Ingreso de Personas en Servicios WebSIC
    - URL: [https://sic.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl](https://sic.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl)

---

## Adjuntos

| Archivo | Descripción |
|---------|-------------|
| [request.json](./attachments/request.json) | Ejemplo JSON Request |
| [request_mark.json](./attachments/request_mark.json) | Ejemplo JSON Request (mark) |
| [request_assessment.json](./attachments/request_assessment.json) | JSON Request (assessment) |
