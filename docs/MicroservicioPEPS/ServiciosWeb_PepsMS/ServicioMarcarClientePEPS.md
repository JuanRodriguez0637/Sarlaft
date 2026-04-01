# Servicio Marcar Cliente PEPS

> **Fuente Confluence:** [https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814200586](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814200586)
> **Fecha extracción:** 2026-03-30

- **Objetivo:** Permite marcar un cliente como peps, en caso de no existir la persona en el modelo de clientes de sura, esta es creada para poder realizar la marcación. En caso de que el cliente ya se encuentra marcado como peps, el servicio devolverá true, acudiendo al principio de idempotencia.

- **Endpoint:** /pepsserv/pep/mark

- **Perfil de Seus4: **PF_CONSUMSERVPEPSAPI

- **Ejemplo Json Request:**

[/wiki/download/attachments/1814200586/request.json?version=1&modificationDate=1667409102428&cacheVersion=1&api=v2](/wiki/download/attachments/1814200586/request.json?version=1&modificationDate=1667409102428&cacheVersion=1&api=v2)[/wiki/download/attachments/1814200586/request_mark.json?version=2&modificationDate=1616783226685&cacheVersion=1&api=v2](/wiki/download/attachments/1814200586/request_mark.json?version=2&modificationDate=1616783226685&cacheVersion=1&api=v2)

- **Dependencias:**

Base de Datos PDN y PDNHA

- Servicio de Consulta de Personas en Servicios WebSIC

URL: [https://sic.suranet.com](https://sic.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl)[/ServiciosWebSic/services/ActualizacionModeloClientesWS](http://appslab.suranet.com:80/ServiciosWebSic/services/ActualizacionModeloClientesWS)

- Servicio de Ingreso de Personas en Servicios WebSIC

URL: [https://sic.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl](https://sic.suranet.com/ServiciosWebSic/services/ConsultaModeloClientesWS?wsdl)

## Ejemplos JSON (Adjuntos)

### `request_assessment.json`

```json
{
  "assessmentId": "7e89f801-cfa2-469b-8c5d-bec8ad35c690",
  "requestDni": "C9709055",
  "operationCode": "1",
  "beneficiaryAnswer": true,
  "applicationCode": "1",
  "borrower": {
    "client": {
      "personType": "N",
      "email": "mail_1@mail.com.co",
      "cellphone": "3102345670",
      "companyName": null,
      "document": {
        "type": "C",
        "number": "1049676100",
        "expedition": "2007-05-27"
      },
      "person": {
        "firstName": "Nestor",
        "secondName": "Fernando",
        "firstSurname": "Arevalo",
        "secondSurname": "Espitia",
        "country": "01"
      },
      "relations": [
        {
          "pepRelationship": true,
          "type": "FAMILY",
          "document": {
            "type": "C",
            "number": "1049900800"
          },
          "person": {
            "firstName": "Sandra",
            "secondName": "Milena",
            "firstSurname": "Arevalo",
            "secondSurname": "Espitia"
          }
        }
      ]
    }
  },
  "beneficiaries": [
    {
      "client": {
        "personType": "N",
        "email": "mail2@mail.com.co",
        "cellphone": "3219006000",
        "companyName": null,
        "manager": true,
        "document": {
          "type": "C",
          "number": "1090800800",
          "expedition": "2000-05-27"
        },
        "person": {
          "firstName": "Diana",
          "firstSurname": "Gomez",
          "secondSurname": null,
          "country": "01"
        }
      },
      "evidences": [
        {
          "dni": "C1090800800",
          "result": "SUCCESSFUL",
          "type": "CIFIN",
          "observations": null
        }
      ]
    },
    {
      "client": {
        "personType": "N",
        "email": "mail3@mail.com.co",
        "cellphone": "3146677888",
        "companyName": null,
        "document": {
          "type": "C",
          "number": "40056098",
          "expedition": "2007-05-27"
        },
        "person": {
          "firstName": "Isabel",
          "secondName": "Lucia",
          "firstSurname": "Mejia",
          "secondSurname": "Mejia",
          "country": "01"
        }
      }
    }
  ],
  "insured": [
    {
      "client": {
        "personType": "N",
        "email": "mail4@mail.com.co",
        "cellphone": "3200007999",
        "companyName": "",
        "document": {
          "type": "C",
          "number": "1045777123",
          "expedition": "2001-05-27"
        },
        "person": {
          "firstName": "Carla",
          "firstSurname": "Diaz",
          "country": "01"
        }
      }
    },
    {
      "client": {
        "personType": "N",
        "email": "mail5@mail.com.co",
        "cellphone": "3101546121",
        "companyName": null,
        "document": {
          "type": "C",
          "number": "10009987",
          "expedition": "2000-05-27"
        },
        "person": {
          "firstName": "Mario",
          "secondName": null,
          "firstSurname": "Duarte",
          "secondSurname": null,
          "country": "01"
        }
      }
    }
  ],
  "policies": [
    {
      "branchCode": "1",
      "productCode": "1",
      "channelCode": "1",
      "insuredValue": 500000,
      "bonusValue": 500000,
      "wayPaying": "CASH",
      "wayCollecting": "PSE",
      "business": "COLLECTIVE"
    }
  ]
}
```text

### `request_mark.json`

```json
{
  "requestDni": "C43260574",
  "application": "118",
  "client": {
    "documentType": "A",
    "documentNumber": "8001973840",
    "firstName": null,
    "secondName": null,
    "firstSurname": null,
    "secondSurname": null
  }
}
```text

### `request.json`

```json
{
  "requestDni": "C43260574",
  "application": "118",
  "client": {
    "documentType": "TT",
    "documentNumber": "1239876",
    "firstName": "ANA",
    "secondName": "PAULINA",
    "firstSurname": "BLANCO",
    "secondSurname": "TORRES CQLII"
  }
}
```
