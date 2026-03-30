# Carga Masiva Figuras a Evaluación

**Fuente Confluence:** [Carga Masiva Figuras a Evaluación](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2394554377)  
**Sección:** [Procesos Carga Masiva](./index.md)

---

## Descripción

- **Objetivo:** En la plataforma SARLAFT 4.0 se construye la funcionalidad para cargar figuras de manera masiva para una evaluación.

- **Descripción:** El proceso inicia cuando el usuario realiza una petición al servicio de carga masiva `sarlaftserv/file/add` y sube el archivo Excel con las figuras que se quieren agregar a la evaluación.

  Flujo del proceso:
  1. Se verifica que no esté pendiente alguna carga con ese mismo Id de evaluación.
  2. Se registra el id de evaluación en caché para iniciar el proceso asíncrono.
  3. El documento se sube al Storage Account.
  4. Se ejecuta el comando `Process.file.addRoles` para iniciar el proceso de validación del archivo.
  5. Se valida la estructura de los campos requeridos para realizar correctamente la adición de las figuras.
  6. Para la validación se consulta el proceso que está en estado iniciado y se toma el id de evaluación.
  7. Se descarga el documento Excel desde el Storage Account (nombre = id de evaluación).
  8. Se recorre el archivo validando los datos y se validan:
     - `DOCUMENT_PN`
     - `RRCC`
     - Que la figura no se encuentre ya agregada (evitar duplicados)
  9. Si las validaciones son correctas → se usa el UseCase `AgregarFiguraUseCase`.
  10. Si las validaciones NO son correctas → no se agrega la figura; se registra un log en Excel con la validación que no cumplió.
  11. Si la validación `DOCUMENT_PN` queda en estado `FALLA_TECNICA` → sí se agrega la figura.
  12. En caché se registra el progreso: procesados, exitosos y fallidos.
  13. Al final se genera un Excel de resultado y se carga al Storage Account en el blob container **respuestascg**.

## Plantilla de Carga Masiva

Archivo `Documento carga masiva.xlsx` — adjunto en la página de Confluence.

## Archivo de Resultado

Archivo `Resultado SARLAFT Cceb16304-ab93-48e8-bbae-878ab1296aa6.xls` — adjunto en la página de Confluence como ejemplo.
