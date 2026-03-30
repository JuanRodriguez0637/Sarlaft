# Sarlaft 4.0 — Documentación Técnica

Repositorio de documentación técnica, de negocio y configuraciones del proyecto **Fortalecimiento Sarlaft 4.0** de Suramericana.

## Estructura del proyecto

```
docs/
├── MicroservicioSarlaftAPI/          # Documentación del microservicio principal
│   ├── EstructuraProyecto/           # Estructura de subproyectos y configuración BD
│   ├── ProcesoEvaluacion/            # Flujos de evaluación, P8, requisitos, estados
│   ├── ProcesosCargaMasiva/          # Carga masiva de figuras y resultados Excel
│   ├── ServiciosWeb/                 # Todos los endpoints REST documentados
│   │   ├── ConsumoNuevosEndpoints/
│   │   ├── CreacionTokenJWT/
│   │   ├── ServicioTerceros/
│   │   └── ...                       # ~20 servicios con requests/responses JSON
│   └── img/                          # Diagramas de dominio, clases y BD
├── AtributosCalidadDesarrollo.md
├── ConfiguracionInfraestructura.md
├── DocumentacionTecnicaSarlaft.md
├── EscenarioValidacion_WeSuraSuraEnLinea.md
├── EvaluacionReclamaciones.md
├── GestionConfiguracion.md
├── InterfazConsultaEstadoSarlaft.md
├── InterfazProcesosMasivos.md
├── PruebasDesempenoJMeter.md
├── PruebasIntegracionSoapUI.md
├── PruebasRegresionSOAT.md
├── Regresion_CotizadorAutos.md
├── Regresion_EvidenciasEscenarios.md
├── Regresion_SEL_SOAT.md
├── Regresion_SIS_Suramasivos.md
├── docx/                             # Documentos Word exportados
├── pdf/                              # Documentos PDF exportados
└── xlsx/                             # Archivos Excel (carga masiva, resultados)

.github/
└── agents/
    └── Confluence Sura.agent.md      # Agente IA para extracción de Confluence
```

## Ramas

| Rama | Descripción |
|------|-------------|
| `Documentacion` | Rama principal con la documentación base del proyecto |
| `MicroservicioSarlaftAPI` | Documentación completa del microservicio SarlaftAPI |
| `MicroservicioWebhook` | Configuraciones de seguridad y plantillas `.vscode` |

## Configuración del entorno local

### Requisitos previos

- [VS Code](https://code.visualstudio.com/)
- [Node.js](https://nodejs.org/) (para ejecutar el MCP server de Confluence)
- Acceso al espacio **EPA** en [segurosti.atlassian.net](https://segurosti.atlassian.net)
- [API Token de Atlassian](https://id.atlassian.com/manage-profile/security/api-tokens)

### 1. Configurar archivos `.vscode`

Los archivos de configuración local están protegidos por `.gitignore` para no subir credenciales al repositorio. Se proporcionan plantillas `.example`:

```powershell
# Copiar las plantillas
Copy-Item .vscode/mcp.json.example .vscode/mcp.json
Copy-Item .vscode/settings.json.example .vscode/settings.json
```

### 2. Configurar credenciales del MCP Confluence

Edita `.vscode/mcp.json` y reemplaza los placeholders con tus credenciales:

```json
{
  "servers": {
    "confluence": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@aashari/mcp-server-atlassian-confluence"
      ],
      "env": {
        "ATLASSIAN_SITE_URL": "https://segurosti.atlassian.net",
        "ATLASSIAN_USER_EMAIL": "tu.email@empresa.com",
        "ATLASSIAN_API_TOKEN": "tu-api-token-aqui"
      }
    }
  }
}
```

| Variable | Descripción |
|----------|-------------|
| `ATLASSIAN_SITE_URL` | URL de la instancia de Confluence (ya configurada) |
| `ATLASSIAN_USER_EMAIL` | Tu email corporativo con acceso a Confluence |
| `ATLASSIAN_API_TOKEN` | Token generado en [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens) |

> **Importante:** Nunca subas `.vscode/mcp.json` al repositorio. El `.gitignore` ya lo protege.

### 3. Obtener un API Token de Atlassian

1. Ve a [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Haz clic en **Create API token**
3. Ponle un nombre descriptivo (ej: `VS Code MCP Confluence`)
4. Copia el token generado y pégalo en `.vscode/mcp.json`

## Agente Confluence Sura

El repositorio incluye un agente personalizado de GitHub Copilot para extraer documentación desde Confluence y convertirla a Markdown.

### ¿Qué hace?

- Extrae páginas, comentarios y adjuntos del espacio **EPA** en Confluence
- Genera archivos `.md` con estructura jerárquica
- Descarga imágenes, JSON, y otros adjuntos referenciados
- Mantiene trazabilidad con links a las páginas fuente

### ¿Cómo usarlo?

En VS Code con GitHub Copilot Chat, invoca al agente con:

```
@Confluence Sura documentar Log Errores Splunk SarlaftApi
```

```
@Confluence Sura documentar Servicios Web
```

```
@Confluence Sura documentar Procesos Carga Masiva
```

El agente seguirá un flujo de 8 pasos:
1. **Exploración** — Busca la sección en Confluence y mapea páginas hijas
2. **Extracción** — Obtiene el contenido de cada página
3. **Comentarios** — Extrae comentarios con autor y fecha
4. **Adjuntos** — Descarga archivos referenciados (imágenes, JSON, etc.)
5. **Markdown** — Genera un `.md` por cada página de Confluence
6. **Comentarios en MD** — Agrega sección de comentarios al final
7. **Índice** — Crea `index.md` con tabla de sub-páginas
8. **Verificación** — Lista todos los archivos creados

### Estructura de salida

```
docs/MicroservicioSarlaftAPI/<Subseccion>/
├── index.md                    # Índice de la subsección
├── <Pagina>.md                 # Una por cada sub-página
├── img/                        # Imágenes descargadas
└── attachments/                # JSON y otros adjuntos
```

## Seguridad

- Los archivos `.vscode/mcp.json` y `.vscode/settings.json` están en `.gitignore`
- Solo las plantillas `.example` (sin credenciales) se incluyen en el repositorio
- Las credenciales de Confluence se manejan localmente por cada desarrollador
- Nunca incluir tokens, passwords o emails reales en commits
