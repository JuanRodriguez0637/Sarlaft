# HU 1082241 — [Formulario]: Adicionar figura de junta directiva en Datos Directivos - Back

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1035467 — [Formulario]: Adicionar figura de junta directiva en Datos Directivos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035467) › HU 1082241 — [Formulario]: Adicionar figura de junta directiva en Datos Directivos - Back

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1082241](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1082241) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-03-19 |
| **Última modificación** | 2026-03-19 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1035467 — [Formulario]: Adicionar figura de junta directiva en Datos Directivos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035467)  
  Estado: New  

## Descripción

Yo como negocio Sarlaft Quiero:  
- 
CAPA DE DOMINIO (domain/model)Agregar el nuevo tipo de figura al enum Figura.Tipo en Figura.java:14-17Actualizar FiguraFactory para soportar la creación de la nueva figuraActualizar validaciones de negocio relacionadas con el tipo de figura  
- 
CASOS DE USO (domain/usecase)Actualizar AgregarFiguraUseCase para incluir lógica de negocio específica de la nueva figuraActualizar EliminarFiguraUseCase para manejar la eliminación de la nueva figuraActualizar PrepararAgregarFiguraUseCase para validaciones previasActualizar PrepararEliminarFiguraUseCase para validaciones de eliminaciónActualizar ValidarFiguras con reglas de validación específicasRevisar ValidarDirectivosUseCase si la figura aplica para personas jurídicasActualizar GuardarFormularioUseCase y GuardarFormularioPJUseCase según tipo de personaAdicionar regla al determinar el estado de la evaluación para que si una evaluación con PJ, no tiene el rol de Junta Directiva asociada a esta, debe cumplir con el mínimo de% de participación de accionistas. >50.Modificar el servicio web de getForm y /formularios para devolver la clasificación ,tipo de las PJ y si aplica el formulario de JuntaDirectiva (decision solo con la clasificación de la PJ)En el servicio de agregar figura, se cree ese log en splunk, asi sea solo intentando, y luego indique si se agrego la persona como PJ.En el servicio de eliminar figura, se cree ese log en splunk, cuando se elimine alguien de junta de la evaluación.En determinar estado de la evaluación loguear en splunk, si la PJ tenia excepción de junta directiva dado sus accionistas y porcentaje de participación.  
- 
CAPA DE ENTRADA - API REST (infraestructure/entry-points/reactive-web)Actualizar AgregarFiguraServiceActualizar EliminarFiguraServiceAjustar servicios /sarlaftserv/form/save - /v1/formularios  
- 
PROCESAMIENTO MASIVO (infraestructure/helpers/file-process-commons)Actualizar ActualizarCuentoInformacionMasivoUseCase si aplicaActualizar CompletarFormClientesUseCase para formularios masivos

## Criterios de Aceptación

- 
CAPA DE DOMINIO (domain/model) 
Agregar el nuevo tipo de figura al enum Figura.Tipo en Figura.java:14-17Actualizar FiguraFactory para soportar la creación de la nueva figuraActualizar validaciones de negocio relacionadas con el tipo de figura  
- 
CASOS DE USO (domain/usecase)Actualizar AgregarFiguraUseCase para incluir lógica de negocio específica de la nueva figuraActualizar EliminarFiguraUseCase para manejar la eliminación de la nueva figuraActualizar PrepararAgregarFiguraUseCase para validaciones previasActualizar PrepararEliminarFiguraUseCase para validaciones de eliminaciónActualizar ValidarFiguras con reglas de validación específicasRevisar ValidarDirectivosUseCase si la figura aplica para personas jurídicasActualizar GuardarFormularioUseCase y GuardarFormularioPJUseCase según tipo de personaAdicionar regla al determinar el estado de la evaluación para que si una evaluación con PJ, no tiene el rol de Junta Directiva asociada a esta, debe cumplir con el mínimo de% de participación de accionistas. >50.Modificar el servicio web de getForm y /formularios para devolver la clasificación ,tipo de las PJ y si aplica el formulario de JuntaDirectiva (decision solo con la clasificación de la PJ)En el servicio de agregar figura, se cree ese log en splunk, asi sea solo intentando, y luego indique si se agrego la persona como PJ.En el servicio de eliminar figura, se cree ese log en splunk, cuando se elimine alguien de junta de la evaluación.En determinar estado de la evaluación loguear en splunk, si la PJ tenia excepción de junta directiva dado sus accionistas y porcentaje de participación.  
- 
CAPA DE ENTRADA - API REST (infraestructure/entry-points/reactive-web)Actualizar AgregarFiguraServiceActualizar EliminarFiguraServiceAjustar servicios /sarlaftserv/form/save - /v1/formularios  
- 
PROCESAMIENTO MASIVO (infraestructure/helpers/file-process-commons)Actualizar ActualizarCuentoInformacionMasivoUseCase si aplicaActualizar CompletarFormClientesUseCase para formularios masivos
