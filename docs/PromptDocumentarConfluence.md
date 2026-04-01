# Prompt: Documentar sección de Confluence localmente

## Contexto

- Instancia de Confluence: https://segurosti.atlassian.net/wiki
- Espacio: EPA ("07) Dominio Soluciones Corporativas")
- Las credenciales están en el archivo `.env` del workspace (variables `CONF_USERNAME`, `CONF_TOKEN`, `CONF_BASE_URL`)
- Directorio base del proyecto: `D:\Proyectos\Sarlaft\Documentacion\Sarlaft\docs\`

## Convención de carpetas

La estructura de carpetas local **replica la jerarquía de páginas en Confluence**, convirtiendo cada nivel del breadcrumb en un directorio con nombre en **PascalCase** (sin espacios, sin tildes, sin caracteres especiales).

**Regla:** El usuario envía la ruta de Confluence con `→` como separador. Cada segmento se convierte en una carpeta:

| Ruta Confluence | Carpeta local |
|----------------|---------------|
| `Sarlaft 4.0` | `Sarlaft40/` |
| `Sarlaft 4.0 → Documentación Técnica` | `Sarlaft40/DocumentacionTecnica/` |
| `Sarlaft 4.0 → Documentación Técnica → Microservicio SarlaftAPI` | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftAPI/` |
| `Sarlaft 4.0 → Documentación Técnica → Mircroservicio sarlaftBatch` | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftBatch/` |
| `Sarlaft 4.0 → Documentación Técnica → Microservicio Webhook` | `Sarlaft40/DocumentacionTecnica/MicroservicioWebhook/` |

**Conversión de nombres:**
- Espacios → eliminados y PascalCase (`Documentación Técnica` → `DocumentacionTecnica`)
- Tildes → sin tilde (`Documentación` → `Documentacion`)
- Versiones numéricas → pegadas (`Sarlaft 4.0` → `Sarlaft40`)
- Solo se crean los folders **a partir de la ruta que envió el usuario** — no se crean carpetas para niveles superiores que no fueron solicitados

**Ruta completa local:** `docs/<RutaConvertida>/`

## Sección a documentar

- Ruta en Confluence: **Sarlaft 4.0 → Documentación Técnica → Microservicio SarlaftAPI → Log Errores Splunk SarlaftApi**
- Buscar la página principal usando CQL y obtener su ID

---

## 0. Verificación de documentación existente

Antes de comenzar la extracción, **verificar si ya existe un folder local** con documentación para la misma sección:

1. Calcular la ruta destino según la convención de carpetas (ej: `docs/Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftBatch/`)
2. Buscar también en `docs/` si existe un folder con nombre equivalente (ej: `docs/MicroservicioSarlaftBatch/`) — puede haber documentación previa que no seguía la jerarquía completa
3. Si **existe documentación previa**:
   - Leer los `.md` existentes para entender qué ya está documentado
   - **Re-actualizar** los archivos existentes con el contenido actual de Confluence en lugar de crear desde cero — aplicar todas las reglas del prompt (cabecera, formato, fidelidad HTML→Markdown)
   - Comparar la versión del `.md` local con la versión actual en Confluence — si cambió, actualizar el contenido
   - Agregar páginas nuevas que no estuvieran documentadas
   - Mover archivos al folder correcto si la ruta no coincide con la convención de carpetas
   - Descargar adjuntos faltantes y eliminar referencias a adjuntos que ya no existen en Confluence
4. Si **NO existe documentación previa** → proceder normalmente con la extracción completa

## 1. Exploración de estructura

- Busca la página principal de la sección usando la API de Confluence (CQL: `space = "EPA" AND title = "<NOMBRE_SECCION>" AND type = page`)
- Obtén el árbol completo de páginas hijas y sub-páginas (`ancestor = <id_pagina>`)
- Verifica si hay sub-sub-páginas (hijas de hijas)
- Mapea la jerarquía completa antes de empezar a documentar

## 2. Extracción de contenido

- Extrae el contenido (`body.storage`) de cada página y sub-página
- Para cada página, identifica:
  - Tablas, listas, fragmentos de código
  - Links a otras páginas de Confluence o externos
  - Archivos adjuntos (DOCX, PDF, XLSX, imágenes, JSON)
  - Macros de Confluence relevantes (pagetree, code, info, warning, view-file)

## 3. Extracción de comentarios

- Para **cada página**, consulta los comentarios footer:
  - `/api/v2/pages/<id>/footer-comments` con `body-format=storage`
- Busca también comentarios inline vía CQL: `parent = <id> AND type = comment`
- Para cada comentario encontrado, registra:
  - **Autor** (`version.by.displayName`)
  - **Fecha** (`version.when`)
  - **ID del comentario**
  - **Texto** (convertido de HTML a Markdown)
  - **Adjuntos referenciados** en el comentario (macros `view-file` / `ri:attachment`)

## 4. Descarga de archivos adjuntos

- Lista los adjuntos de **cada página** (`/rest/api/content/<id>/child/attachment`)
- Lista los adjuntos del **comentario** si los referencia (`/rest/api/content/<id_comentario>/child/attachment`)
  - Si los adjuntos del comentario no están en el comentario mismo, búscalos en la página padre
- Descarga usando curl con autenticación Basic Auth (email + token del `.env`):
  - URL base: `https://segurosti.atlassian.net/wiki` + `_links.download`
- Guarda todo en `<Subseccion>/attachments/` → imágenes (PNG, JPG, etc.), DOCX, PDF, XLSX, JSON y cualquier otro adjunto
- Crea las carpetas si no existen
- Nombra los archivos descriptivamente (ej: `ProcesoMasivoRequest.json` en vez de `Request.json`)
- **NO descargar adjuntos huérfanos:** solo descargar imágenes y archivos que estén referenciados en el cuerpo de la página (`body.storage`) o en comentarios. Si un adjunto existe en Confluence pero no aparece en ningún macro `ac:image`, `ri:attachment` o `view-file` del contenido, ignorarlo.

## 5. Generación de archivos Markdown

- **Un archivo `.md` por cada página** de Confluence — nunca mezclar información de páginas distintas
- Respeta la jerarquía de carpetas:

```
docs/
└── Sarlaft40/
    └── DocumentacionTecnica/
        └── MicroservicioSarlaftAPI/
            ├── index.md                  — índice de la sección principal
            ├── <Pagina>.md               — una por sub-página directa
            ├── <Subseccion>/             — carpeta por cada sub-sección con hijas
            │   ├── index.md
            │   ├── <Pagina>.md
            │   └── attachments/           — todos los adjuntos (imágenes, DOCX, PDF, XLSX, JSON, etc.)
            └── attachments/              — todos los adjuntos de la sección raíz
```

La carpeta raíz se determina convirtiendo la ruta Confluence enviada por el usuario según la convención de carpetas descrita arriba.

- Cada `.md` debe incluir al inicio:

```markdown
# <Título de la página>

> **Fuente Confluence:** [<Título>](<URL completa>)  
> **Última modificación:** <fecha> — <autor> · versión <N>  
> **Sección:** [<Padre>](./index.md)
```

- Convierte HTML/storage format a Markdown limpio:
  - Tablas HTML → tablas Markdown
  - Bloques de código → fenced code blocks con lenguaje correcto
  - Macros `info`/`warning`/`note` → blockquotes
  - Macros `view-file` → links a archivos descargados en `./attachments/`
  - Macros `ac:image` → `![alt](./attachments/<filename>)`
  - Links internos de Confluence → referencias relativas entre los .md creados
  - Nombres técnicos (tablas BD, campos, endpoints, perfiles) → backticks: `` `nombre` ``

### 5.1 Resolución de links internos (`ac:link` / `ri:page`) — CRÍTICO

Los macros `ac:link` con `ri:page` referencian páginas de Confluence **por título**. Para cada uno:

1. **Buscar el ID de la página destino** con CQL: `space = "EPA" AND title = "<content-title>" AND type = page`
2. **Construir la URL completa** de Confluence: `https://segurosti.atlassian.net/wiki/spaces/EPA/pages/<id>/<titulo_encoded>`
3. **Verificar si ya existe un `.md` local** para esa página dentro de la documentación generada
4. Si existe `.md` local → usar **referencia relativa** al `.md` (ej: `[Título](./EstructuraProyecto.md)`)
5. Si NO existe `.md` local → usar **URL de Confluence** Y registrar en `docs/BitacoraEnlaces.md` sección 3 ("Secciones aún NO documentadas") con la página origen, línea y prioridad

**NUNCA dejar un `ac:link` como texto plano sin hipervínculo.** Siempre debe resolverse a un link funcional (local o Confluence).

### 5.2 Fidelidad en la conversión HTML → Markdown — CRÍTICO

La conversión debe ser **fiel al formato original** de Confluence. No transformar ni reinterpretar la estructura:

- Si Confluence usa `<ol>` con `<li>` que contienen `<p>` con prefijos como **a.**, **b.**, **c.** → mantener como párrafos indentados con prefijo en negrita, **NO** convertir a sub-listas con viñetas (`-`)
- Si Confluence usa una lista numerada `<ol>` → usar lista numerada Markdown (`1.`, `2.`, `3.`)
- Si Confluence usa una lista con viñetas `<ul>` → usar viñetas Markdown (`-`)
- Si los sub-items son párrafos `<p>` dentro de un `<li>`, mantenerlos como párrafos indentados, no como sub-viñetas
- Imágenes con `<ac:caption>` → agregar texto de caption como línea en cursiva debajo: `*Texto caption*`

**Ejemplo concreto — sub-ítems dentro de `<li>` con `<br />`:**

Cuando el HTML de Confluence tiene sub-ítems separados por `<br />` dentro de un `<li>`, como:

```html
<li><p><strong>domain</strong>: descripción...<br />
<strong>a.</strong> <strong>model</strong>: texto...<br />
<strong>b.</strong> <strong>use-case</strong>: texto...</p></li>
```

Usar line breaks con `\` al final de cada línea, **NO** viñetas con `- `:

```markdown
<!-- ✅ CORRECTO -->
2. **domain**: descripción...\
   **a.** **model**: texto...\
   **b.** **use-case**: texto...

<!-- ❌ INCORRECTO — genera bullets/viñetas no deseadas -->
2. **domain**: descripción...
   - **a.** **model**: texto...
   - **b.** **use-case**: texto...
```

## 6. Sección de comentarios en el Markdown

- Si una página tiene comentarios, agregar una sección al final del `.md`:

```markdown
---

## Comentarios de Confluence

### Comentario 1

> **Autor:** <nombre>  
> **Fecha:** <fecha>  
> **ID comentario:** <id>

<contenido convertido a Markdown>

### Adjuntos del comentario

| Archivo | Descripción |
|---------|-------------|
| [`nombre.json`](./attachments/nombre.json) | Descripción |
```

## 7. Archivo índice de la subsección

El `index.md` de la subsección debe incluir:

- Descripción general
- Tabla con todas las sub-páginas, descripción y fecha de última modificación
- Links relativos a cada `.md`

## 8. Reglas importantes

- **Un .md por página de Confluence** — nunca mezclar
- **Solo contenido original:** NO agregar notas, interpretaciones, resúmenes o inferencias propias. El Markdown debe reflejar **exclusivamente** lo que existe en la página de Confluence (cuerpo + comentarios). Si una página solo tiene una tabla, el `.md` solo tiene esa tabla — sin sección "Notas" inventada.
- Nombres de archivo en **PascalCase**, sin espacios
- Si una página solo tiene macro `pagetree`, el `.md` es un índice con links
- Los backticks se preservan: campos BD, endpoints, mensajes, perfiles van con `` ` ``
- Al final, verificar con un **listado recursivo** que todos los archivos fueron creados correctamente:

```powershell
Get-ChildItem $base -Recurse -File | Select-Object @{N='Ruta';E={$_.FullName.Replace("$base\",'')}}, @{N='Bytes';E={$_.Length}} | Sort-Object Ruta | Format-Table -AutoSize
```

## 9. Validación de enlaces (Bitácora)

Después de generar la documentación, ejecutar una **validación post-proceso** de enlaces:

1. **Escanear enlaces rotos** en los `.md` recién creados y en toda la documentación:
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

2. **Si se detectan enlaces rotos**, registrarlos en `docs/BitacoraEnlaces.md` sección 1 con: archivo origen, línea, enlace roto, texto del enlace y corrección sugerida.

3. **Revisar la bitácora existente** (`docs/BitacoraEnlaces.md`):
   - ¿Algún enlace roto previo se resuelve con los `.md` recién creados? → Corregir el enlace y registrar en "Correcciones aplicadas"
   - ¿La sección 3 ("Secciones aún NO documentadas") lista alguna página que acabamos de documentar? → Marcarla como completada

4. **Preguntar al usuario**: _"Se encontraron N hallazgos en la bitácora que podrían resolverse con la documentación recién extraída. ¿Desea que aplique las correcciones?"_

5. Si el usuario acepta, aplicar las correcciones y actualizar la bitácora (sección "Registro de correcciones aplicadas").

## 10. Actualizar README.md

Después de generar toda la documentación, **actualizar el archivo `README.md`** en la raíz del repositorio:

1. Leer el `README.md` actual
2. Actualizar la sección **"Estructura del proyecto"** para reflejar las nuevas carpetas y archivos creados
3. Si la subsección documentada es nueva, agregarla al árbol de directorios con su descripción
4. Si ya existía, verificar que la descripción esté vigente
5. No eliminar secciones existentes del README — solo agregar o actualizar
6. Reportar los cambios realizados en el `README.md`
---

## Lecciones aprendidas

| # | Lección | Detalle |
|---|---------|--------|
| 1 | **Adjuntos siempre locales a la subsección** | Nunca usar carpetas centralizadas (`docs/docx/`, `docs/pdf/`, `docs/xlsx/`) ni separar imágenes en `img/`. **Todo adjunto** (imágenes, DOCX, PDF, XLSX, JSON, etc.) debe vivir en `<Subseccion>/attachments/` — una sola carpeta por subsección. Los enlaces relativos quedan cortos (`./attachments/archivo.xlsx`, `./attachments/imagen.png`) y no dependen de la profundidad del árbol. Las rutas largas con `../` son frágiles: se rompen al reorganizar carpetas. |
| 2 | **Encoding UTF-8 explícito** | Al generar `.md` con scripts (Python/PowerShell), siempre forzar `encoding='utf-8'`. Si el contenido viene de la API de Confluence, puede llegar como Latin-1 re-codificado; aplicar `fix_encoding()` (Latin-1 → UTF-8) antes de escribir. |
| 3 | **Eliminar cabeceras legacy antes de regenerar** | Al re-documentar páginas que ya tienen `.md` previo, primero eliminar las cabeceras antiguas (`**Fuente Confluence:**`, `**Sección:**`, `**Página padre:**`) para evitar duplicados. |
| 4 | **Validar enlaces después de cada generación** | Ejecutar siempre el script de validación de enlaces (Paso 9) inmediatamente después de generar los `.md`. No dejarlo para el final — los enlaces rotos se acumulan y son más difíciles de corregir en lote. |
| 5 | **URL-decode en validación de enlaces** | El validador de enlaces debe aplicar `Uri.UnescapeDataString()` a las rutas antes de verificar con `Test-Path`, porque los `.md` pueden contener `%20`, `%25`, etc. |

---

> **Nota:** Este prompt es reutilizable para cualquier subsección del Microservicio SarlaftAPI (Servicios Web, Procesos Carga Masiva, Estructura Proyecto, etc.) — solo cambia `<NOMBRE_SECCION>` por el título de la página raíz en Confluence.
