# Servicio Web - InformaColombia PJ

> **Fuente Confluence:** [Servicio Web - InformaColombia PJ](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3386769498/Servicio+Web+-+InformaColombia+PJ)
> **Última modificación:** 2023-10-27 — Julián Andrés Curubo García · versión 3
> **Sección:** [Microservicio InformaColombia](./index.md)

- **Objetivo: **Servicio para consultar la informacion de una persona jurídica. Este servicio se expone en reemplazo de la comunicación request reply que se tenia por medio del service bus, donde se integran las funcionalidades del query “`Clients.pj.findByDni`".
- **Endpoint:** sarlaftclientpj/api/clientes
- **Perfil de Seus4: **NO aplica. Este servicio se expone interno al cluster del aks, por lo tanto se convierte en una comunicación back to back.
- **Ejemplo parámetros de entrada:**
  /sarlaftclientpj/api/clientes/123456![image-20231027-164416.png](./attachments/image-20231027-164416.png)
- **Ejemplo response:**
```
{
    "meta": null,
    "data": [
        {
            "type": "Cliente",
            "id": "123456",
            "attributes": {
                "dni": null,
                "razonSocial": null,
                "actividadEconomica": null,
                "estadoEmpresa": null,
                "telefono": null,
                "correo": null,
                "dsDireccion": null,
                "ciudad": null,
                "departamento": null,
                "formaJuridica": null,
                "representanteLegal": null,
                "fechaConstitucion": null,
                "accionistas": null,
                "ingresosOperacionales": 0.0,
                "activos": 0.0,
                "pasivos": 0.0,
                "juntaDirectiva": null
            }
        }
    ],
    "included": null
}
```

- **Documentación swagger:** /sarlaftclientpj/swagger-ui.html
![image-20231027-164454.png](./attachments/image-20231027-164454.png)
