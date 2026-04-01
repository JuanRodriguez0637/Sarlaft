# Query consulta información Asesor

> **Fuente Confluence:** [Query consulta información Asesor](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2906751028/Query+consulta+informaci%C3%B3n+Asesor)
> **Última modificación:** 2022-09-19 — juan camilo muñoz burgos (Unlicensed) · versión 1
> **Sección:** [Microservicio Asesores](./index.md)

**Objetivo**:

Consultar la información de contacto de un asesor a partir del código del asesor.

**Descripción**:

El query **Adviser.contact.find **permite consultar la información de contacto de un asesor.

Con el código del asesor se realiza la consulta al servicio de /redcomercial/asesor/infocontacto de redcomercial . La consulta se guardará en caché.

**Ejemplo json request:**

```json
{
  "codigoAsesor": "1111"
}
```

**Ejemplo Json reply:**

```json
{
        "codigoAgente": "",
        "primerNombre": "",
        "segundoNombre": "",
        "primerApellido": "",
        "segundoApellido": "",
        "correo": "",
        "celular": "",
        "dni": "",
        "codigoTipo": "",
        "indicadorAgenteDirecto": false/true
    }
```

**Dependencias Ecosistema Sura:**

- Servicio /redcomercial/asesor/infocontacto del micro de redcomercial
- Cache redis.
