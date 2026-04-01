# Servicio Web - Sarlaftclientpn

> **Fuente Confluence:** [Servicio Web - Sarlaftclientpn](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3386638444/Servicio+Web+-+Sarlaftclientpn)
> **Última modificación:** 2023-10-27 — Julián Andrés Curubo García · versión 3
> **Sección:** [Microservicio Azure - Clientes PN](./index.md)

- **Objetivo: **Consultar el perfil de un cliente en la base de datos de Experian. Este servicio se expone en reemplazo de la comunicación request reply que se tenia por medio del service bus, donde se integran las funcionalidades del query “`Clients.pn.findByDni`".
- **Endpoint:** sarlaftclientpn/api/clientes
- **Perfil de Seus4: **NO aplica. Este servicio se expone interno al cluster del aks, por lo tanto se convierte en una comunicación back to back.
- **Ejemplo parámetros de entrada:**
  /sarlaftclientpn/api/clientes?tipoDocumento=C&numeroDocumento=1048015272&primerApellido=VARGAS
  ![image-20231027-163002.png](./attachments/image-20231027-163002.png)
- **Ejemplo response:**
```
{
    "meta": null,
    "data": [
        {
            "type": "Cliente",
            "id": "C1048015272:VARGAS",
            "attributes": {
                "nombre": null,
                "tipoDocumento": null,
                "numeroDocumento": null,
                "tipoPersona": null,
                "actividadEconomica": null,
                "direcciones": null,
                "telefono": null,
                "correo": null,
                "representanteLegal": null,
                "valorAsegurado": null,
                "sector": null,
                "primerNombre": null,
                "segundoNombre": null,
                "primerApellido": null,
                "segundoApellido": null,
                "fechaExpedicion": null,
                "celular": null,
                "ingresos": null,
                "egresos": null,
                "nacionalidad": null
            }
        }
    ],
    "included": null
}
```

- **Documentación swagger:** /sarlaftclientpn/swagger-ui.html
![image-20231027-163034.png](./attachments/image-20231027-163034.png)
