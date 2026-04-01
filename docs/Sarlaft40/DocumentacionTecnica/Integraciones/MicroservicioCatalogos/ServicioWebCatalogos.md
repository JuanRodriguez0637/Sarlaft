# Servicio Web - Catálogos

> **Fuente Confluence:** [Servicio Web - Catálogos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3387031595/Servicio+Web+-+Cat%C3%A1logos)
> **Última modificación:** 2023-10-27 — Julián Andrés Curubo García · versión 2
> **Sección:** [Microservicio - Catálogos](./index.md)

- **Objetivo: **Servicio para obtener los valores de los catálogos solicitados. Este servicio se expone en reemplazo de la comunicación request reply que se tenia por medio del service bus, donde se integran las funcionalidades del query “`List.parameters.find`".
- **Endpoint:** /sarlaftcatalogos/api/catalogos
- **Perfil de Seus4: **NO aplica. Este servicio se expone interno al cluster del aks, por lo tanto se convierte en una comunicación back to back.
- **Ejemplo parámetros de entrada:**
  /sarlaftcatalogos/api/catalogos?codigoCatalogo=TIPOSDOCUMENTOS&pais=57&departamento=&tipoPersona=![image-20231027-172940.png](./attachments/image-20231027-172940.png)
- **Ejemplo response:**
```
{
    "meta": null,
    "data": [
        {
            "type": "Catalogo",
            "id": "TIPOSDOCUMENTOS",
            "attributes": [
                {
                    "codigo": "C",
                    "descripcion": "CEDULA"
                },
                {
                    "codigo": "E",
                    "descripcion": "CEDULA EXTRANJERIA"
                },
                {
                    "codigo": "TC",
                    "descripcion": "CERTIFICADO NACIDO VIVO"
                },
                {
                    "codigo": "D",
                    "descripcion": "DIPLOMATICO"
                },
                {
                    "codigo": "X",
                    "descripcion": "DOC.IDENT. DE EXTRANJEROS"
                },
                {
                    "codigo": "F",
                    "descripcion": "ID. FISCAL PARA EXTRANJEROS"
                },
                {
                    "codigo": "A",
                    "descripcion": "NIT"
                },
                {
                    "codigo": "N",
                    "descripcion": "NUIP"
                },
                {
                    "codigo": "P",
                    "descripcion": "PASAPORTE"
                },
                {
                    "codigo": "TP",
                    "descripcion": "PASAPORTE ONU"
                },
                {
                    "codigo": "TT",
                    "descripcion": "PERMISO POR PROTECCION TEMPORL"
                },
                {
                    "codigo": "R",
                    "descripcion": "REGISTRO CIVIL"
                },
                {
                    "codigo": "TS",
                    "descripcion": "SALVOCONDUCTO DE PERMANENCIA"
                },
                {
                    "codigo": "T",
                    "descripcion": "TARJ.IDENTIDAD"
                }
            ]
        }
    ],
    "included": null
}
```

- **Documentación swagger:** /sarlaftcatalogos/swagger-ui.html
![image-20231027-173006.png](./attachments/image-20231027-173006.png)
