# Carga Masiva Figuras a Evaluación

> **Fuente Confluence:** [Carga Masiva Figuras a Evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2394554377)
> **Última modificación:** 2022-02-25 — Rodrigo Hurtado Cardona (Unlicensed) · versión 4
> **Sección:** [Procesos Carga Masiva](./index.md)
- **Objetivo:** En la plataforma SARLAFT 4,0 se construye la funcionalidad para cargar figuras de manera masiva para una evaluación.

- **Descripción:** El proceso inicia cuando el usuario realiza una petición al servicio de carga masiva `sarlaftserv/file/add` y sube el archivo Excel con las figuras que se quieren agregar a la evaluación, se verifica que no este pendiente alguna carga con ese mismo Id de evaluación, se registra el id de evaluación en cache para iniciar el proceso asíncrono, el documento se sube al Storage Account, ejecutándose el comando `Process.file.addRoles` para iniciar el proceso de validación de archivo donde se valida la estructura de los campos requeridos para realizar correctamente la adición de las figuras en la evaluación correspondiente. Para la validación se consulta el proceso que esta en estado iniciado y se toma el id de evaluación de ese proceso, posteriormente se descarga el documento excel desde el storage account el cual tiene el mismo nombre del id de evaluación, se recorre el archivo validando los datos que cumplan con un mínimo de condiciones para ser procesados y crear cada figura, después de crear la figura se realizan las validaciones de `DOCUMENT_PN`, `RRCC` y se valida que la figura no se encuentre agregada a la evaluación para evitar registros duplicados, si las validaciones son correctas se usa el proceso de agregar figura que se encuentra en el UseCase `AgregarFiguraUseCase`, en caso contrario si las validaciones no son correctas, no se agrega la figura a la evaluación, la validación de `DOCUMENT_PN` se guarda en cache la evidencia para esa figura para no realizar mas consultas, se registra un log en un archivo de excel donde se especifica la validación que no cumplió esa figura o registro, en caso de que la validación de `DOCUMENT_PN` quede en estado `FALLA_TECNICA`, si se agrega la figura a la evaluación. En la cache se va registrando los registros que se han procesado, los que han sido exitosos y los que han sido fallidos, para ser consultados y mostrar el progreso de la validación del archivo cargado por el usuario. Al final el proceso se genera un excel con el resultado del proceso de la validación y adición de las figuras a la evaluación, dicho archivo se carga de nuevo al storage account en el blob container **respuestascg**.

- **Plantilla de carga masiva:**

  [`DocumentoCargaMasiva.xlsx`](./attachments/DocumentoCargaMasiva.xlsx)

- **Archivo de resultado:**

  [`ResultadoSarlaftCargaMasiva.xls`](./attachments/ResultadoSarlaftCargaMasiva.xls)
