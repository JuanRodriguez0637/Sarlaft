# Bitácora de Enlaces — Hallazgos y Correcciones Pendientes

> **Propósito:** Registrar los hallazgos de enlaces entre archivos `.md` que requieren corrección, ya sea porque apuntan a archivos que no existen o porque apuntan a URLs de Confluence cuando ya existe un `.md` local equivalente.
>
> **Última actualización:** 2026-04-02 (auditoría global: 334 archivos, 1281 enlaces)

---

## 1. Enlaces rotos (apuntan a `.md` que NO existen)

| # | Archivo origen | Línea | Enlace roto | Texto del enlace | Estado |
|---|---------------|-------|-------------|-------------------|--------|
| 1 | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftBatch/index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — creado `Sarlaft40/DocumentacionTecnica/index.md` |
| 2 | `Sarlaft40/DocumentacionTecnica/DisenoArquitectura/index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — mismo archivo |
| 3 | `Sarlaft40/DocumentacionDeIncidentes/index.md` | L5 | `../index.md` | Sarlaft 4.0 | ✅ Resuelto — creado `Sarlaft40/index.md` |
| 4 | `Sarlaft40/DocumentacionTecnica/Front/index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — mismo archivo que #1 |
| 5 | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftClientesMS/index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — mismo archivo que #1 |
| 6 | `Sarlaft40/DocumentacionTecnica/MicroservicioBackweb/index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — mismo archivo que #1 |
| 7 | `Sarlaft40/DocumentacionTecnica/GestionConfiguracion/index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — mismo archivo que #1 |
| 8 | `Sarlaft40/DocumentacionTecnica/index.md` | L4 | `../index.md` | Sarlaft 4.0 | ✅ Resuelto — creado `Sarlaft40/index.md` |
| 9 | `PreguntasFrecuentes/index.md` | L11,L19 | `../Diseño%20-%20Arquitectura/...` | Documento Diseño Técnico | ✅ Resuelto — corregido a `../Sarlaft40/DocumentacionTecnica/DisenoArquitectura/DocumentoDisenoTecnico/index.md` |
| 10 | 13× `Motor de Evaluación/*/index.md` | L5 | `../index.md` | Motor de Evaluación | ❌ Pendiente — requiere crear `Motor de Evaluación/index.md` (sección no documentada bajo convención Sarlaft40) |

---

## 2. Enlaces que apuntan a Confluence pero YA tienen `.md` local

Estos enlaces en la cabecera `> **Fuente Confluence:**` son **intencionales** como trazabilidad y NO requieren corrección. Esta sección documenta únicamente los enlaces **dentro del cuerpo** del contenido que deberían apuntar a archivos locales en vez de a Confluence.

| # | Archivo origen | Texto del enlace | URL Confluence | `.md` local existente | Estado |
|---|---------------|-------------------|----------------|----------------------|--------|
| — | *No se encontraron enlaces en cuerpo que apunten a Confluence teniendo `.md` local* | — | — | — | ✅ |

> **Nota:** Todos los enlaces a Confluence detectados están en las cabeceras de trazabilidad (`> **Fuente Confluence:**`) o en columnas de referencia cruzada del catálogo de servicios (`Confluence` column en `ServiciosWeb/index.md`). Estos son intencionales.

---

## 3. Sección: Atributos de Calidad Desarrollo

> Validación ejecutada: 2026-04-02 — 14 archivos `.md` escaneados, 27 enlaces relativos verificados, 0 rotos.

### Enlaces válidos (27)

| Archivo | Enlace | Destino | Estado |
|---------|--------|---------|--------|
| `index.md` L26 | `./PruebasUnitarias.md` | PruebasUnitarias.md | ✅ |
| `index.md` L27 | `./DocumentacionConfluence.md` | DocumentacionConfluence.md | ✅ |
| `index.md` L28 | `./DeudaTecnica.md` | DeudaTecnica.md | ✅ |
| `index.md` L29 | `./AcuerdosDeProyecto.md` | AcuerdosDeProyecto.md | ✅ |
| `index.md` L30 | `./PruebasIntegracionSoapUI.md` | PruebasIntegracionSoapUI.md | ✅ |
| `index.md` L31 | `./PruebasDesempenoJMeter.md` | PruebasDesempenoJMeter.md | ✅ |
| `index.md` L32 | `./PruebasRegresionSarlaftSOAT.md` | PruebasRegresionSarlaftSOAT.md | ✅ |
| `PruebasUnitarias.md` L5 | `./index.md` | index.md | ✅ |
| `DocumentacionConfluence.md` L5 | `./index.md` | index.md | ✅ |
| `DocumentacionConfluence.md` L9 | `./attachments/image-20210326-154318.png` | imagen existente | ✅ |
| `DeudaTecnica.md` L5 | `./index.md` | index.md | ✅ |
| `AcuerdosDeProyecto.md` L5 | `./index.md` | index.md | ✅ |
| `PruebasIntegracionSoapUI.md` L5 | `./index.md` | index.md | ✅ |
| `PruebasIntegracionSoapUI.md` L9 | `./attachments/PruebasSoapUI.docx` | adjunto existente | ✅ |
| `PruebasDesempenoJMeter.md` L5 | `./index.md` | index.md | ✅ |
| `PruebasDesempenoJMeter.md` L9 | `./attachments/PruebasDesempeno.docx` | adjunto existente | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L5 | `./index.md` | index.md | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L33 | `./attachments/EvidenciaGlobalWebRegresion.pdf` | adjunto existente | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L34 | `./attachments/EvidenciasEscenarios_SOAT.docx` | adjunto existente | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L35 | `./attachments/Regresion_CotizadorAutos_062024.docx` | adjunto existente | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L36 | `./attachments/Regresion_SEL_distintoSOAT_062024.docx` | adjunto existente | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L37 | `./attachments/Regresion_SIS_Suramasivos_062024.docx` | adjunto existente | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L39 | `./attachments/image-20240620-194416.png` | imagen existente | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L45 | `./Regresion_CotizadorAutos.md` | Regresion_CotizadorAutos.md | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L46 | `./Regresion_EvidenciasEscenarios.md` | Regresion_EvidenciasEscenarios.md | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L47 | `./Regresion_SEL_SOAT.md` | Regresion_SEL_SOAT.md | ✅ |
| `PruebasRegresionSarlaftSOAT.md` L48 | `./Regresion_SIS_Suramasivos.md` | Regresion_SIS_Suramasivos.md | ✅ |

### Enlaces externos (Confluence / otros)

| Archivo | Texto del enlace | URL | Nota |
|---------|------------------|-----|------|
| `AcuerdosDeProyecto.md` L55 | Estándar nombramiento Base de Datos | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1813545175` | ⚠️ La URL apunta a pageId 1813545175 que es la propia página **Atributos de Calidad Desarrollo** (página padre). Probablemente un error en la fuente de Confluence — el enlace debería apuntar a una página diferente con el estándar de BD. **No corregir**, reportar como error de fuente. |
| `PruebasRegresionSarlaftSOAT.md` L9 | Tarea 538482: Pruebas sistema SARLAFT sin SOAT | `https://dev.azure.com/SuraColombia/Portafolios/_workitems/edit/538482` | Enlace a Azure DevOps — no requiere corrección |

### Enlaces rotos

| Archivo | Enlace | Esperado | Problema |
|---------|--------|----------|----------|
| — | — | — | **No se encontraron enlaces rotos** ✅ |

### Referencias a `./img/` (legacy)

No se encontraron referencias a `./img/` en ningún archivo `.md`. La carpeta `img/` contiene `image-20240620-194416.png` que ya está copiada en `attachments/`. No se requiere acción.

---

## 3b. Sección: Diseño - Arquitectura

> Validación ejecutada: 2026-04-02 — 34 archivos `.md` escaneados, 125 enlaces internos verificados OK, 7 corregidos, 1 roto pendiente (padre), 74 enlaces externos catalogados.

### Enlaces rotos corregidos (7)

| Archivo | Línea | Enlace original | Problema | Corrección |
|---------|-------|----------------|----------|------------|
| `DisenoFuncionalidades/03ValidacionesAssessment.md` | L90 | `Sarlaft_Laura-ValidacionIdentidadSarlaft%20(1)-...jpg` | Paréntesis sin codificar rompe sintaxis MD | `%28` / `%29` en vez de `(` / `)` |
| `DisenoFuncionalidades/03ValidacionesAssessment.md` | L123 | `Sarlaft_Laura-ValidacionIdentidadarlaft%20(1)-...jpg` | Paréntesis sin codificar | `%28` / `%29` |
| `DisenoFuncionalidades/03ValidacionesAssessment.md` | L129 | `Sarlaft_Laura-ValidacionIdentidadarlaft2%20(1)-...jpg` | Paréntesis sin codificar | `%28` / `%29` |
| `DisenoFuncionalidades/09ConsultaInformacionDeClienteGetClient.md` | L11 | `Sarlaft_Laura-PrecargaCliente2%20(1)-...jpg` | Paréntesis sin codificar | `%28` / `%29` |
| `DisenoFuncionalidades/10ValidacionYHabilitacionClientePEPs.md` | L25 | `Sarlaft_Laura-FlujoPEPS%20(2)-...jpg` | Paréntesis sin codificar | `%28` / `%29` |
| `DisenoFuncionalidades/10ValidacionYHabilitacionClientePEPs.md` | L45 | `Sarlaft_Laura-FlujoPEPS_Marcacion%20(1)-...jpg` | Paréntesis sin codificar | `%28` / `%29` |
| `DisenoFuncionalidades/11RequisitosDeSarlaft.md` | L25 | `Sarlaft_Laura-FlujoRequisitos1%20(1)-...jpg` | Paréntesis sin codificar | `%28` / `%29` |

### Enlace roto pendiente (1)

| Archivo | Línea | Enlace | Texto | Nota |
|---------|-------|--------|-------|------|
| `index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — creado `Sarlaft40/DocumentacionTecnica/index.md` (2026-04-02) |

### Enlaces externos — Confluence EPA (24 únicos, no resueltos)

| # | Página origen | Texto del enlace | URL Confluence | Prioridad |
|---|--------------|-----------------|----------------|-----------|
| 1 | `DisenoFuncionalidades/02EntradasAEvaluacionAssessment.md` | Servicio Proceso Masivo | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2093350926` | Media |
| 2 | `DisenoFuncionalidades/02EntradasAEvaluacionAssessment.md` | Interfaz Procesos Masivos | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070163` | Media |
| 3 | `DisenoFuncionalidades/02EntradasAEvaluacionAssessment.md` | Servicio Validacion Radicado | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2619802061` | Media |
| 4 | `DisenoFuncionalidades/03ValidacionesAssessment.md` | Microservicio - Clientes PEP | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1861058683` | Media |
| 5 | `DisenoFuncionalidades/03ValidacionesAssessment.md` | Microservicio PEPS | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1804861539` | Media |
| 6 | `DisenoFuncionalidades/03ValidacionesAssessment.md` | Query consulta Cliente PEPS | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1864597599` | Baja |
| 7 | `DisenoFuncionalidades/03ValidacionesAssessment.md` | Consulta Cliente RRCC | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1860862186` | Baja |
| 8 | `DisenoFuncionalidades/03ValidacionesAssessment.md` | Microservicio - Identity | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2787475565` | Media |
| 9 | `DisenoFuncionalidades/03ValidacionesAssessment.md` | Microservicio - CCM | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2345730088` | Media |
| 10 | `DisenoFuncionalidades/03ValidacionesAssessment.md` | Servicio Adicionar Evidencias | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1814003981` | Baja |
| 11 | `DisenoFuncionalidades/07WebhookAssessment.md` | Descripción de Interfaces Principales | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070150` | Media |
| 12 | `DisenoFuncionalidades/07WebhookAssessment.md` | Interfaz Procesos Masivos | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1955070163` | Media |
| 13 | `DisenoFuncionalidades/13ConsultasModeloRedComercial.md` | Servicio Web Consultar Oficinas Asesor. | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2565079101` | Baja |
| 14 | `DisenoFuncionalidades/13ConsultasModeloRedComercial.md` | Servicio Web Consulta Información Oficinas Asesor | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2612002880` | Baja |
| 15 | `DisenoFuncionalidades/13ConsultasModeloRedComercial.md` | Consultar Información de Contacto del Asesor | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2584870913` | Baja |
| 16 | `DisenoFuncionalidades/14ConsultasModuloDeClientes.md` | Servicio Consultar evaluaciones de un tomador | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2427879670` | Baja |
| 17 | `DisenoFuncionalidades/14ConsultasModuloDeClientes.md` | Servicio Resultado Evaluación | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2398191643` | Baja |
| 18 | `DisenoFuncionalidades/14ConsultasModuloDeClientes.md` | Servicio Finalizar Evaluación | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2903408641` | Baja |
| 19 | `DisenoFuncionalidades/15ParametrizacionEntidades.md` | Servicio Consultar Entidades | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2893152310` | Baja |
| 20 | `DisenoFuncionalidades/15ParametrizacionEntidades.md` | Servicio Cambiar estado entidad | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2935160848` | Baja |
| 21 | `DisenoFuncionalidades/15ParametrizacionEntidades.md` | Servicio Matricular Entidad | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2928377889` | Baja |
| 22 | `DisenoFuncionalidades/18ConsultarCatalogos.md` | Servicio Web - Catálogos | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3387031595` | Baja |
| 23 | `EstandarNombramientoBaseDeDatos.md` | Azure Database for PostgreSQL | `https://segurosti.atlassian.net/wiki/spaces/AR/pages/1381761738` | Baja |
| 24 | `InformacionDeSecretos.md` | Gestión de secretos en la nube | `https://segurosti.atlassian.net/wiki/spaces/AR/pages/2974187588` | Baja |

### Enlaces externos — Confluence EPA (trazabilidad en cabecera, intencionales)

| Archivo | URL | Nota |
|---------|-----|------|
| Todos los 34 `.md` | `> **Fuente Confluence:** [título](url)` | Enlaces de trazabilidad en cabecera — NO requieren corrección |

### Enlaces externos — otros servicios

| Archivo | Texto | URL | Tipo |
|---------|-------|-----|------|
| `AccesoALaCache.md` | Azure Cache for Redis | `https://azure.microsoft.com/es-mx/services/cache/` | Azure docs |
| `ContextualizacionDeArquitectura.md` | ExplicacionArquitecturaBase.mp4 | SharePoint video | SharePoint |
| `RequisitosNoFuncionales.md` | Miro board | `https://miro.com/app/board/...` | Miro |
| `DocumentoDisenoTecnico/RespuestasDeErrorPropuestaAunNoImplementada.md` | Lineamientos para servicios REST | `https://segurosti.atlassian.net/wiki/spaces/AR/pages/256672056` | Confluence AR |
| `DisenoFuncionalidades/12CrearEvaluacionPorFormulario.md` | visorappslab.labsura.com | URL interna | App interna |
| `DisenoFuncionalidades/12CrearEvaluacionPorFormulario.md` | sarlaft.labsura.com | URL interna | App interna |
| `DisenoFuncionalidades/14ConsultasModuloDeClientes.md` | siclab.segurossura.com.co | URL interna | App interna |

---

## 3c. Sección: MicroservicioSarlaftClientesMS

> Validación ejecutada: 2026-04-02 — 8 archivos `.md` escaneados, 25 enlaces relativos verificados, 24 válidos, 1 roto pendiente (padre).

### Enlaces válidos (24)

| Archivo | Línea | Enlace | Texto del enlace | Estado |
|---------|-------|--------|-------------------|--------|
| `ConfiguracionAmbiente.md` | L5 | `./index.md` | Microservicio SarlaftClientesMS | ✅ |
| `ConfiguracionHealthCheck.md` | L5 | `./index.md` | Microservicio SarlaftClientesMS | ✅ |
| `ConfiguracionHealthCheck.md` | L13 | `./attachments/image-20240207-200559.png` | imagen | ✅ |
| `ConfiguracionHealthCheck.md` | L19 | `./attachments/image-20240208-174721.png` | imagen | ✅ |
| `ConfiguracionHealthCheck.md` | L23 | `./attachments/image-20240208-174751.png` | imagen | ✅ |
| `ConfiguracionHealthCheck.md` | L27 | `./attachments/image-20240208-174917.png` | imagen | ✅ |
| `EstructuraProyecto.md` | L5 | `./index.md` | Microservicio SarlaftClientesMS | ✅ |
| `EstructuraProyecto.md` | L9 | `./attachments/image-20220509-200124.png` | Componentes del microservicio | ✅ |
| `EstructuraProyecto.md` | L13 | `./attachments/image-20220509-200606.png` | Subproyectos del microservicio | ✅ |
| `index.md` | L11 | `./EstructuraProyecto.md` | Estructura del Proyecto | ✅ |
| `index.md` | L12 | `./ConfiguracionAmbiente.md` | Configuración Ambiente | ✅ |
| `index.md` | L13 | `./Comunicaciones/index.md` | Comunicaciones | ✅ |
| `index.md` | L14 | `./ConfiguracionHealthCheck.md` | Configuración HealthCheck | ✅ |
| `index.md` | L18 | `./Comunicaciones/index.md` | Comunicaciones | ✅ |
| `index.md` | L19 | `./Comunicaciones/ConsultarClientesFuentesExternasNoMasivo.md` | Consultar clientes NoMasivo | ✅ |
| `index.md` | L20 | `./Comunicaciones/CompletarInformacionClientesEvaluacionMasiva.md` | Completar información Masiva | ✅ |
| `index.md` | L21 | `./Comunicaciones/ConsultarClientesFuentesExternasActualizacion.md` | Consultar clientes Actualización | ✅ |
| `Comunicaciones/CompletarInformacionClientesEvaluacionMasiva.md` | L5 | `./index.md` | Comunicaciones | ✅ |
| `Comunicaciones/ConsultarClientesFuentesExternasActualizacion.md` | L5 | `./index.md` | Comunicaciones | ✅ |
| `Comunicaciones/ConsultarClientesFuentesExternasNoMasivo.md` | L5 | `./index.md` | Comunicaciones | ✅ |
| `Comunicaciones/index.md` | L5 | `../index.md` | Microservicio SarlaftClientesMS | ✅ |
| `Comunicaciones/index.md` | L11 | `./ConsultarClientesFuentesExternasNoMasivo.md` | Consultar clientes NoMasivo | ✅ |
| `Comunicaciones/index.md` | L12 | `./CompletarInformacionClientesEvaluacionMasiva.md` | Completar información Masiva | ✅ |
| `Comunicaciones/index.md` | L13 | `./ConsultarClientesFuentesExternasActualizacion.md` | Consultar clientes Actualización | ✅ |

### Enlace roto pendiente (1)

| Archivo | Línea | Enlace | Texto | Destino esperado | Nota |
|---------|-------|--------|-------|------------------|------|
| `index.md` | L5 | `../index.md` | Documentación Técnica | `Sarlaft40/DocumentacionTecnica/index.md` | ✅ Resuelto — creado `Sarlaft40/DocumentacionTecnica/index.md` (2026-04-02) |

### Enlaces externos (15 — todos intencionales)

| Tipo | Cantidad | Nota |
|------|----------|------|
| Trazabilidad Confluence (cabecera `> **Fuente Confluence:**`) | 8 | Intencionales — no requieren corrección |
| Azure DevOps (repos, pipelines) | 4 | URLs de infraestructura |
| URLs internas (healthcheck endpoints) | 2 | URLs de servicio |
| SonarQube | 1 | URL de calidad de código |

### Enlaces rotos

| Archivo | Enlace | Esperado | Problema |
|---------|--------|----------|----------|
| — | — | — | **Ningún enlace roto a archivos locales** ✅ |

---

## 4. Secciones de Confluence aún NO documentadas en `.md`

Las siguientes páginas de Confluence están referenciadas desde la documentación existente pero **aún no se han extraído** como secciones independientes. Son candidatas para futuras extracciones con el agente Confluence Sura.

| # | Sección en Confluence | Referenciado desde | Prioridad | Estado |
|---|----------------------|--------------------|-----------|--------|
| 1 | [7. Webhook (Assessment)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3222994946/7.+Webhook+Assessment) | `MicroservicioWebhook/index.md` L15, `MicroservicioWebhook/WebhookSarlaft.md` L17 | Media | ✅ Resuelto — enlace corregido a `../DisenoArquitectura/DisenoFuncionalidades/07WebhookAssessment.md` (2026-04-02) |
| 2 | [Documentación Técnica](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1746830371) (página padre) | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftBatch/index.md` L5 | Baja | ✅ Resuelto — creado `Sarlaft40/DocumentacionTecnica/index.md` con tabla de 14 subsecciones (2026-04-02) |
| 3 | [Respuestas de error (propuesta aun no implementada)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages?title=Respuestas%20de%20error%20%28propuesta%20aun%20no%20implementada%29) | `Integraciones/FrontSarlaft/WebComponent/CambiosIntegracionSOAT.md` L19 | Baja | ✅ Resuelto — enlace corregido a `../../../DisenoArquitectura/DocumentoDisenoTecnico/RespuestasDeErrorPropuestaAunNoImplementada.md` (2026-04-02) |
| 4 | [Creación token JWT](https://segurosti.atlassian.net/wiki/spaces/EPA/pages?title=Creaci%C3%B3n%20token%20JWT) | `Integraciones/FrontSarlaft/WebComponent/Integracion.md` L24 | Media | ✅ Resuelto — enlace corregido a `../../../MicroservicioSarlaftAPI/ServiciosWeb/CreacionTokenJWT/index.md` (2026-04-02) |
| 5 | [Servicio Web Consultar Oficinas Asesor](https://segurosti.atlassian.net/wiki/spaces/EPA/pages?title=Servicio%20Web%20Consultar%20Oficinas%20Asesor.) | `Integraciones/MicroservicioAsesores/ComunicacionServicioOficinasAsesor.md` L8 | Baja | Pendiente — búsqueda por título |
| 6 | [Servicio Consulta de Clientes](https://segurosti.atlassian.net/wiki/spaces/EPA/pages?title=Servicio%20Consulta%20de%20Clientes) | `Integraciones/MicroservicioAzureClientes/IntegracionConsultaClienteSalesforce.md` L13 | Baja | ✅ Resuelto — enlace corregido a `../../MicroservicioSarlaftAPI/ServiciosWeb/ServicioConsultaClientes.md` (2026-04-02) |
| 7 | [Manual de Integración asíncrona con CCM](https://segurosti.atlassian.net/wiki/spaces/EPA/pages?title=Manual%20de%20Integraci%C3%B3n%20as%C3%ADncrona%20con%20CCM) | `Integraciones/MicroservicioCCM/index.md` L9 | Media | Pendiente — página de espacio externo |
| 8 | [Logs de Experian en Splunk](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3641311258) | `DocumentacionDeIncidentes/SolicitudDeRequestAndRespose.md` L53, `DocumentacionDeIncidentes/ProblemasConElLinkDeValidacionDeIdentidad.md` L11 | Media | Pendiente — página en espacio EPA |
| 9 | [Tipos de Identificación](https://segurosti.atlassian.net/wiki/spaces/EAV/pages/4592009228) (espacio EAV) | `DocumentacionDeIncidentes/LimpiarBaseDeDatosEnLaboratorio.md` L28 | Baja | Pendiente — página en espacio EAV (externo) |

---

## 5. Archivo `docs/index.md` faltante

~~No existe un archivo `docs/index.md` a nivel raíz que sirva como punto de entrada general a toda la documentación.~~ Se crearon los índices padre necesarios:
- `Sarlaft40/index.md` — enlaza a DocumentacionTecnica y DocumentacionDeIncidentes
- `Sarlaft40/DocumentacionTecnica/index.md` — enlaza a las 14 subsecciones

Estos resolvieron todos los enlaces `../index.md` bajo `Sarlaft40/` (11 enlaces corregidos).

---

## Registro de correcciones aplicadas

| Fecha | Archivo corregido | Descripción del cambio |
|-------|-------------------|------------------------|
| 2026-04-01 | `MicroservicioSarlaftAPI/ConsumoNuevosEndpoints.md` | L4: Enlace `../index.md` corregido a URL Confluence padre `Servicios+Web+-+SarlaftAPI` |
| 2026-04-01 | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftAPI/` | **Re-documentación completa:** 56 páginas movidas desde `MicroservicioSarlaftAPI/` a la ruta correcta según jerarquía Confluence. Cabeceras actualizadas con versión, autor y fecha. 13 enlaces rotos corregidos por cambio de profundidad de carpetas. 22 adjuntos descargados. |
| 2026-04-01 | `Sarlaft40/DocumentacionTecnica/Integraciones/` | **Documentación nueva:** 100 páginas extraídas (15 microservicios + Front Sarlaft). 149 adjuntos descargados (imágenes, PDFs, DOCX, XLSX, JSON). 0 enlaces rotos tras correcciones de nombres con paréntesis y hash. |
| 2026-04-01 | `Sarlaft40/DocumentacionTecnica/MicroservicioWebhook/` | **Migración adjuntos:** 18 imágenes movidas de `img/` a `attachments/`. Referencias actualizadas en 7 archivos `.md`. Carpeta `img/` eliminada. |
| 2026-04-02 | `Sarlaft40/DocumentacionTecnica/ConfiguracionPlataformaBase/` | **Validación enlaces:** 3 archivos `.md` escaneados, 18 enlaces verificados (12 relativos + 6 externos), 0 rotos. 7 adjuntos correctamente referenciados (2 YAML + 4 PNG + 1 YAML). |
| 2026-04-02 | `AtributosCalidadDesarrollo/` | **Validación enlaces:** 14 archivos `.md` escaneados, 27 enlaces relativos verificados, 0 rotos. 9 adjuntos correctamente referenciados. 1 enlace externo Confluence reportado como error de fuente (pageId 1813545175 apunta a página padre en vez de "Estándar nombramiento BD"). |
| 2026-04-02 | `Sarlaft40/DocumentacionTecnica/DisenoArquitectura/` | **Validación enlaces:** 34 archivos `.md` escaneados, 132 enlaces internos verificados (125 OK + 7 corregidos), 1 roto pendiente (`../index.md`), 74 externos catalogados. 7 imágenes con paréntesis en nombre corregidas (`%28`/`%29`). |
| 2026-04-02 | `MicroservicioWebhook/index.md`, `MicroservicioWebhook/WebhookSarlaft.md` | Enlace Confluence a "7. Webhook (Assessment)" corregido a ruta local `../DisenoArquitectura/DisenoFuncionalidades/07WebhookAssessment.md` |
| 2026-04-02 | `Integraciones/FrontSarlaft/WebComponent/CambiosIntegracionSOAT.md` | Enlace Confluence a "Respuestas de error" corregido a ruta local `../../../DisenoArquitectura/DocumentoDisenoTecnico/RespuestasDeErrorPropuestaAunNoImplementada.md` |
| 2026-04-02 | `Sarlaft40/DocumentacionDeIncidentes/` | **Validación enlaces:** 6 archivos `.md` escaneados, 43 enlaces verificados (17 relativos + 26 externos). 1 roto (`../index.md`), 2 no resueltos (Confluence EPA/EAV). |
| 2026-04-02 | `Sarlaft40/DocumentacionTecnica/Front/` | **Validación enlaces:** 8 archivos `.md` escaneados, 57 enlaces verificados (37 relativos + 20 externos). ~~1 roto~~ → ✅ resuelto (creado `DocumentacionTecnica/index.md`). 20 adjuntos OK. |
| 2026-04-02 | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftClientesMS/` | **Validación enlaces:** 8 archivos `.md` escaneados, 25 enlaces relativos verificados (24 OK, 1 roto pendiente `../index.md`). 15 enlaces externos catalogados (trazabilidad + infra). 6 adjuntos de imagen verificados OK. |
| 2026-04-02 | `Sarlaft40/DocumentacionTecnica/MicroservicioBackweb/` | **Re-documentación completa:** 28 páginas extraídas desde `MicroservicioBackweb/` legacy y regeneradas en ruta correcta `Sarlaft40/DocumentacionTecnica/MicroservicioBackweb/`. 15 imágenes + 1 JSON descargados en `attachments/`. Imágenes movidas de `img/` a `attachments/`. 1 enlace con paréntesis corregido (`request (1).json` → angle-bracket syntax). 1 roto pendiente (`../index.md` → sección padre). |
| 2026-04-02 | `Sarlaft40/DocumentacionTecnica/index.md` | **Creado:** Índice padre con tabla de 14 subsecciones. Resuelve 7 enlaces rotos `../index.md` (Batch, DisenoArq, Front, GestionConfig, Backweb, ClientesMS, MicroservicioPEPS). |
| 2026-04-02 | `Sarlaft40/index.md` | **Creado:** Índice padre de Sarlaft 4.0 con 2 secciones. Resuelve enlace roto en `DocumentacionDeIncidentes/index.md` L5. |
| 2026-04-02 | `Integraciones/FrontSarlaft/WebComponent/Integracion.md` | Enlace Confluence “Creación token JWT” corregido a ruta local `../../../MicroservicioSarlaftAPI/ServiciosWeb/CreacionTokenJWT/index.md` |
| 2026-04-02 | `Integraciones/MicroservicioAzureClientes/IntegracionConsultaClienteSalesforce.md` | Enlace Confluence “Servicio Consulta de Clientes” corregido a ruta local `../../MicroservicioSarlaftAPI/ServiciosWeb/ServicioConsultaClientes.md` |
| 2026-04-02 | `PreguntasFrecuentes/index.md` | 2 enlaces Confluence “Documento Diseño Técnico” (L11, L19) corregidos de `../Diseño - Arquitectura/...` a `../Sarlaft40/DocumentacionTecnica/DisenoArquitectura/DocumentoDisenoTecnico/index.md` |
| 2026-04-02 | **Auditoría global** | Escaneo completo: **334 archivos `.md`**, **1281 enlaces relativos** verificados. **13 rotos** — todos del mismo patrón: 13× `Motor de Evaluación/*/index.md` → `../index.md` (falta `Motor de Evaluación/index.md`). Los 9 rotos previos de sección 1 (#1-#9) todos resueltos gracias a la creación de `Sarlaft40/DocumentacionTecnica/index.md`, `Sarlaft40/index.md` y la corrección de `PreguntasFrecuentes/index.md`. Carpeta legacy `MicroservicioSarlaftClientesMS/` eliminada. |

---

## Validación: Documentación de Incidentes — 2026-04-02

> Validación ejecutada: 2026-04-02 — 6 archivos `.md` escaneados, 43 enlaces verificados (17 relativos + 26 externos), 1 roto, 2 no resueltos.

### Enlaces relativos verificados (17)

| Archivo fuente | Línea | Enlace | Tipo | Estado |
|---|---|---|---|---|
| `index.md` | L5 | `../index.md` | Relativo (.md) | ✅ OK — `Sarlaft40/index.md` creado (2026-04-02) |
| `index.md` | L15 | `./SolicitudDeRequestAndRespose.md` | Relativo (.md) | ✅ OK |
| `index.md` | L16 | `./SolucionarINCAsignadosEnBMCHelix.md` | Relativo (.md) | ✅ OK |
| `index.md` | L17 | `./LimpiarBaseDeDatosEnLaboratorio.md` | Relativo (.md) | ✅ OK |
| `index.md` | L18 | `./ProblemasConElLinkDeValidacionDeIdentidad.md` | Relativo (.md) | ✅ OK |
| `index.md` | L19 | `./ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` | Relativo (.md) | ✅ OK |
| `index.md` | L34–L38 | 5× enlaces duplicados a subpáginas (tabla) | Relativo (.md) | ✅ OK (5/5) |
| `SolicitudDeRequestAndRespose.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `SolucionarINCAsignadosEnBMCHelix.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `SolucionarINCAsignadosEnBMCHelix.md` | L18 | `./attachments/image-20251201-154141.png` | Relativo (imagen) | ✅ OK |
| `SolucionarINCAsignadosEnBMCHelix.md` | L20 | `./attachments/image-20251201-154154.png` | Relativo (imagen) | ✅ OK |
| `LimpiarBaseDeDatosEnLaboratorio.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `ProblemasConElLinkDeValidacionDeIdentidad.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` | L9 | `./attachments/image-20260226-224639.png` | Relativo (imagen) | ✅ OK |
| `ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` | L15 | `./attachments/image-20260226-224911.png` | Relativo (imagen) | ✅ OK |
| `ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` | L21 | `./attachments/image-20260226-225247.png` | Relativo (imagen) | ✅ OK |
| `ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` | L179 | `./attachments/image-20260226-225735.png` | Relativo (imagen) | ✅ OK |

### Enlace roto (1)

| Archivo | Línea | Enlace | Texto | Corrección sugerida |
|---------|-------|--------|-------|---------------------|
| `index.md` | L5 | `../index.md` | Sarlaft 4.0 | ✅ Resuelto — creado `Sarlaft40/index.md` (2026-04-02) |

### Enlaces externos — Confluence no resueltos (2 páginas únicas, 3 ocurrencias)

| Archivo fuente | Línea | Texto del enlace | URL Confluence | Nota |
|---|---|---|---|---|
| `SolicitudDeRequestAndRespose.md` | L53 | Logs de Experian en Splunk | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3641311258` | ⚠️ No resuelto — página EPA no documentada localmente |
| `ProblemasConElLinkDeValidacionDeIdentidad.md` | L11 | Acceso a los índices de Splunk | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3641311258` | ⚠️ Misma página que "Logs de Experian" |
| `LimpiarBaseDeDatosEnLaboratorio.md` | L28 | tipos de identificación | `https://segurosti.atlassian.net/wiki/spaces/EAV/pages/4592009228` | ⚠️ No resuelto — página en espacio EAV externo |

> **Nota:** La URL `pages/3641311258` también aparece en `SolicitudDeRequestAndRespose.md` L13 como "Guía para la solicitud de permisos de perfil en Splunk" — misma página con texto diferente.

### Enlaces externos — Confluence trazabilidad (intencionales, 6)

| Archivo | URL | Nota |
|---------|-----|------|
| `index.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1742800723` | Cabecera trazabilidad — no requiere corrección |
| `SolicitudDeRequestAndRespose.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5174689830` | Cabecera trazabilidad |
| `SolucionarINCAsignadosEnBMCHelix.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5174886473` | Cabecera trazabilidad |
| `LimpiarBaseDeDatosEnLaboratorio.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5174624323` | Cabecera trazabilidad |
| `ProblemasConElLinkDeValidacionDeIdentidad.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5174788164` | Cabecera trazabilidad |
| `ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/5624856625` | Cabecera trazabilidad |

### Enlaces externos — otros servicios (17)

| Archivo | Texto | URL | Tipo |
|---------|-------|-----|------|
| `index.md` L27 | Insumos operación Sarlaft | SharePoint | SharePoint |
| `index.md` L28 | Información básica Sarlaft | SharePoint | SharePoint |
| `SolicitudDeRequestAndRespose.md` L13 | Guía para la solicitud de permisos... | Confluence EPA `3641311258` | Confluence (ref a misma pág. de "Logs Experian") |
| `SolicitudDeRequestAndRespose.md` L16 | holmeslab.suramericana.com.co | URL interna | Splunk Lab |
| `SolicitudDeRequestAndRespose.md` L19 | sherlock.suramericana.com.co | URL interna | Splunk Prod |
| `SolicitudDeRequestAndRespose.md` L50 | Traductor de códigos en Azure DevOps | Azure DevOps Git | Azure DevOps |
| `SolicitudDeRequestAndRespose.md` L56 | respuesta a la solicitud de request... | SharePoint video | SharePoint |
| `SolucionarINCAsignadosEnBMCHelix.md` L11 | Consola de especialista | BMC Helix | App interna |
| `SolucionarINCAsignadosEnBMCHelix.md` L12 | Dynatrace | Dynatrace | Monitoreo |
| `SolucionarINCAsignadosEnBMCHelix.md` L33 | servicesesb.datacredito.com.co (DHServicePlus) | DataCrédito | Servicio externo |
| `SolucionarINCAsignadosEnBMCHelix.md` L33 | servicesesb.datacredito.com.co (HcplWSClientes) | DataCrédito | Servicio externo |
| `SolucionarINCAsignadosEnBMCHelix.md` L42 | solución de incidentes asignados... | SharePoint video | SharePoint |
| `LimpiarBaseDeDatosEnLaboratorio.md` L23 | Limpieza en base de datos | SharePoint video | SharePoint |
| `ProblemasConElLinkDeValidacionDeIdentidad.md` L28 | Video explicativo problemas... | SharePoint video | SharePoint |
| `ErrorEnElAplicativoDeBancaNegocioEnEstadoPendiente.md` L19 | Bug 374809 Azure DevOps | Azure DevOps | Azure DevOps |

**Resumen:** 43 enlaces verificados, 1 roto (`../index.md`), 2 no resueltos (Confluence), 16 OK relativos, 26 externos con formato válido.

---

## Validación: Front — 2026-04-02

> Validación ejecutada: 2026-04-02 — 8 archivos `.md` escaneados, 57 enlaces verificados (37 relativos internos + 20 externos), 1 roto, 0 no resueltos.

### Enlaces relativos verificados (37)

| Archivo fuente | Línea | Enlace | Tipo | Estado |
|---|---|---|---|---|
| `index.md` | L5 | `../index.md` | Relativo (.md) | ✅ OK — `Sarlaft40/DocumentacionTecnica/index.md` creado (2026-04-02) |
| `index.md` | L9 | `DisenoMonoRepositorio.md` | Relativo (.md) | ✅ OK |
| `index.md` | L10 | `ConfiguracionAmbiente/index.md` | Relativo (.md) | ✅ OK |
| `index.md` | L11 | `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | Relativo (.md) | ✅ OK |
| `index.md` | L12 | `Despliegue.md` | Relativo (.md) | ✅ OK |
| `index.md` | L13 | `DespliegueConPlantillas.md` | Relativo (.md) | ✅ OK |
| `index.md` | L14 | `Errores/index.md` | Relativo (.md) | ✅ OK |
| `index.md` | L15 | `Errores/ErrorDigitalEnvelopeRoutines.md` | Relativo (.md) | ✅ OK |
| `index.md` | L37 | `./attachments/web-component-usage.png` | Relativo (imagen) | ✅ OK |
| `index.md` | L52 | `./attachments/assets-structure.png` | Relativo (imagen) | ✅ OK |
| `DisenoMonoRepositorio.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `DisenoMonoRepositorio.md` | L9 | `./attachments/image-20210707-205046.png` | Relativo (imagen) | ✅ OK |
| `DisenoMonoRepositorio.md` | L36 | `./attachments/image-20210707-210030.png` | Relativo (imagen) | ✅ OK |
| `DisenoMonoRepositorio.md` | L40 | `./attachments/image-20210707-210251.png` | Relativo (imagen) | ✅ OK |
| `Despliegue.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `Despliegue.md` | L15 | `./attachments/image-20211123-164954.png` | Relativo (imagen) | ✅ OK |
| `Despliegue.md` | L21 | `./attachments/image-20211123-165041.png` | Relativo (imagen) | ✅ OK |
| `DespliegueConPlantillas.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `DespliegueConPlantillas.md` | L55 | `./attachments/image-20240815-135858.png` | Relativo (imagen) | ✅ OK |
| `DespliegueConPlantillas.md` | L61 | `./attachments/image-20240815-135954.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L5 | `../index.md` | Relativo (.md) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L9 | `ConfiguracionAmbientePasosImportantes.md` | Relativo (.md) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L37 | `../Errores/ErrorDigitalEnvelopeRoutines.md` | Relativo (.md) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L45 | `./attachments/image-20240530-123417.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L49 | `./attachments/image-20240529-175740.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L53 | `./attachments/image-20240529-175916.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L55 | `./attachments/image-20240517-123121.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/index.md` | L57 | `./ConfiguracionAmbientePasosImportantes.md` | Relativo (.md) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L20 | `./attachments/image-20240517-125341.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L24 | `./attachments/image-20240529-180633.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L29 | `./attachments/image-20240529-180756.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L35 | `./attachments/image-20240529-181349.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L39 | `./attachments/image-20240517-164015.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L58 | `./attachments/image-20240103-154651.png` | Relativo (imagen) | ✅ OK |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` | L62 | `./attachments/image-20240103-154829.png` | Relativo (imagen) | ✅ OK |
| `Errores/index.md` | L5 | `../index.md` | Relativo (.md) | ✅ OK |
| `Errores/index.md` | L9 | `ErrorDigitalEnvelopeRoutines.md` | Relativo (.md) | ✅ OK |
| `Errores/ErrorDigitalEnvelopeRoutines.md` | L5 | `./index.md` | Relativo (.md) | ✅ OK |
| `Errores/ErrorDigitalEnvelopeRoutines.md` | L7 | `./attachments/image-20230628-175950.png` | Relativo (imagen) | ✅ OK |
| `Errores/ErrorDigitalEnvelopeRoutines.md` | L17 | `../ConfiguracionAmbiente/index.md` | Relativo (.md) | ✅ OK |

### Enlace roto (1)

| Archivo | Línea | Enlace | Texto | Corrección sugerida |
|---------|-------|--------|-------|---------------------|
| `index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — creado `Sarlaft40/DocumentacionTecnica/index.md` (2026-04-02) |

### Enlaces externos — Confluence trazabilidad (intencionales, 8)

| Archivo | URL | Nota |
|---------|-----|------|
| `index.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1985511647` | Cabecera trazabilidad |
| `DisenoMonoRepositorio.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2233073714` | Cabecera trazabilidad |
| `Despliegue.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2505998354` | Cabecera trazabilidad |
| `DespliegueConPlantillas.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3968991251` | Cabecera trazabilidad |
| `ConfiguracionAmbiente/index.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2233466927` | Cabecera trazabilidad |
| `ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3467214883` | Cabecera trazabilidad |
| `Errores/index.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3242721320` | Cabecera trazabilidad |
| `Errores/ErrorDigitalEnvelopeRoutines.md` L3 | `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3242819613` | Cabecera trazabilidad |

### Enlaces externos — otros servicios (12)

| Archivo | Texto | URL | Tipo |
|---------|-------|-----|------|
| `Despliegue.md` L11 | Configuraciones de Pipelines | `https://dev.azure.com/.../adm_y_fin-sarlaft-fr-conf` | Azure DevOps |
| `DespliegueConPlantillas.md` L43 | Redirect pipeline | `https://dev.azure.com/...definitionId=4111` | Azure DevOps |
| `DespliegueConPlantillas.md` L46 | Sarlaft pipeline | `https://dev.azure.com/...definitionId=4504` | Azure DevOps |
| `DespliegueConPlantillas.md` L49 | Web component pipeline | `https://dev.azure.com/...definitionId=4505` | Azure DevOps |
| `DespliegueConPlantillas.md` L53 | Repositorio de pipelines | `https://dev.azure.com/.../892-sarlaft-fr` | Azure DevOps |
| `DespliegueConPlantillas.md` L59 | Enviroments | `https://dev.azure.com/.../892-sarlaft-fr` | Azure DevOps |
| `ConfiguracionAmbiente/index.md` L15 | Node.js v16.16.0 (LTS) | `https://nodejs.org/en/blog/release/v16.16.0` | Docs externa |
| `ConfiguracionAmbiente/index.md` L19 | Visual Studio Code | `https://code.visualstudio.com/` | Docs externa |
| `ConfiguracionAmbiente/index.md` L20 | Web Storm | `https://www.jetbrains.com/es-es/webstorm/` | Docs externa |
| `ConfiguracionAmbiente/index.md` L30 | Repositorio principal | `https://dev.azure.com/.../892-sarlaft-fr` | Azure DevOps |
| `ConfiguracionAmbiente/index.md` L31 | Repositorio configuración | `https://dev.azure.com/.../892-sarlaft-fr-conf` | Azure DevOps |
| `Errores/ErrorDigitalEnvelopeRoutines.md` L16 | Node.js v16.16.0 (LTS) | `https://nodejs.org/en/blog/release/v16.16.0` | Docs externa |
| `index.md` L33 | mf-arquetipo | `http://inboggit01.suramericana.com.co:8080/gitbucket/TIDIGITAL/mf-arquetipo` | Git interno |

**Resumen:** 57 enlaces verificados, 1 roto (`../index.md`), 0 Confluence no resueltos, 36 OK relativos, 20 externos con formato válido.

---

## Validación: Microservicio Backweb — 2026-04-02

> Validación ejecutada: 2026-04-02 — 28 archivos `.md` escaneados, 44 enlaces relativos verificados (43 OK, 1 roto pendiente), 0 enlaces externos no resueltos.

### Resumen de archivos generados

| Carpeta | Archivos `.md` | Adjuntos | Total |
|---------|---------------|----------|-------|
| `MicroservicioBackweb/` | 12 (index + 10 directos + DisenoArquitectura vacío) | 15 imágenes | 27 |
| `MicroservicioBackweb/ServiciosWeb/` | 17 (index + 16 servicios) | 1 JSON | 18 |
| **Total** | **29** | **16** | **45** |

### Enlace roto pendiente (1) — RESUELTO

| Archivo | Línea | Enlace | Texto | Estado |
|---------|-------|--------|-------|--------|
| `index.md` | L5 | `../index.md` | Documentación Técnica | ✅ Resuelto — creado `Sarlaft40/DocumentacionTecnica/index.md` |

### Enlaces internos verificados — todos OK

Todos los enlaces relativos (`./` y `../`) en los 28 archivos `.md` verificados. **0 rotos.**

### Correcciones aplicadas

| Archivo | Corrección |
|---------|------------|
| `ServiciosWeb/ServicioCambiarEstadoEntidad.md` L26 | Enlace a `request (1).json` corregido a `<./attachments/request (1).json>` (angle-bracket syntax por paréntesis en nombre) |

---

## Cómo usar esta bitácora

1. **Al crear nuevos `.md`:** Verificar si algún enlace roto de la sección 1 ahora puede resolverse y actualizar los archivos origen.
2. **Al extraer nuevas secciones de Confluence:** Revisar la sección 3 y marcar como completada la sección documentada.
3. **Después de cada corrección:** Agregar una entrada en "Registro de correcciones aplicadas".
4. **Para re-escanear:** Ejecutar en terminal:

```powershell
$base = "D:\Proyectos\Sarlaft\Documentacion\Sarlaft\docs"
$mdFiles = Get-ChildItem $base -Recurse -Filter "*.md" | Where-Object { $_.Name -ne "PromptDocumentarConfluence.md" -and $_.Name -ne "BitacoraEnlaces.md" }
foreach ($f in $mdFiles) {
    $lines = Get-Content $f.FullName
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $ms = [regex]::Matches($lines[$i], '\[([^\]]+)\]\((\.\.?/[^\)]+\.md[^\)]*)\)')
        foreach ($m in $ms) {
            $lp = $m.Groups[2].Value -replace '#.*$',''
            $rp = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($f.DirectoryName, $lp))
            if (-not (Test-Path $rp)) {
                $rf = $f.FullName.Replace("$base\","")
                Write-Host "BROKEN | $rf | L$($i+1) | $lp | $($m.Groups[1].Value)"
            }
        }
    }
}
```
