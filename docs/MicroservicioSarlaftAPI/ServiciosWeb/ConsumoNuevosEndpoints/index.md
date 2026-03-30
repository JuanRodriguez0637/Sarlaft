# Consumo de Nuevos Endpoints para el Web Component

**Fuente Confluence:** [Consumo de Nuevos Endpoints para el Web Component](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3784671252)
**Sección:** [Servicios Web](../index.md)

---

Adjunto colección de Postman para probar la nueva API Rest de servicios web modificados:

[Enlace a la colección](https://suramericana.sharepoint.com/:f:/r/sites/MESA7-CALIDADDEINFORMACIN/Shared%20Documents/General/Proyecto%20SARLAFT%204.0/DocumentacionDesarrollo/IniciativaSoat_2024/Documentos%20Complementarios%20SARLAFT/sarlaft/nuevos%20endpoints?csf=1&web=1&e=igXtjV)

[Enlace a los ambientes](https://suramericana.sharepoint.com/:f:/r/sites/MESA7-CALIDADDEINFORMACIN/Shared%20Documents/General/Proyecto%20SARLAFT%204.0/DocumentacionDesarrollo/IniciativaSoat_2024/Documentos%20Complementarios%20SARLAFT/sarlaft?csf=1&web=1&e=JJ7Cu4)

Adjunto Excel especificando el mapeo de los endpoints anteriores en los nuevos endpoints resultantes, importante tener presente que solo se expusieron nuevos servicios o controladores para manejar el objeto de error personalizado y no se hicieron cambios a nivel de validaciones en los casos de uso, así que lo demás debe de funcionar como lo venía haciendo desde antes:

[`Mapeo Nuevas URLs (3).xlsx`](../../../xlsx/Mapeo%20Nuevas%20URLs%20(3).xlsx)

Los endpoints coloreados del color que se indica en la figura no se configuraron debido a que alguien mas los configuro previamente y se aclaro que no había que trabajarlos:

![image-20240604-191935.png](./img/image-20240604-191935.png)

## Listado de Excepciones Identificadas

Las excepciones identificadas para los endpoints:

- assessment/recategorize
- assessment/addevidence
- assessment/getForm
- assessment/figure/add
- assessment/figure/delete
- client/get
- form/save

Se pueden visualizar en el siguiente archivo de Excel coloreadas de amarillo o verde, las que están sin colorear es porque no se encontraron:

[`RespuestasErroresSarlaft4_HT505291_ParteBrayan.xlsx`](../../../xlsx/RespuestasErroresSarlaft4_HT505291_ParteBrayan.xlsx)

Las Excepciones identificadas para estos otros endpoints:

- form/resend
- file/getStatus
- file/add
- file/getResult
- validaridentidad/validate
- massiveform/justification/save
- form/skip

Se pueden visualizar en el siguiente archivo de Excel:

[`EXCEPCIONES_ENCONTRADAS.xlsx`](../../../xlsx/EXCEPCIONES_ENCONTRADAS.xlsx)

## Sub-páginas

- [Logs de los Nuevos Endpoints de Sarlaft API](./LogsNuevosEndpoints.md)
