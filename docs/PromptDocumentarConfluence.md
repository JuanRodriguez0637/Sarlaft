# Prompt: Documentar sección de Confluence localmente

## Contexto

- Instancia de Confluence: https://segurosti.atlassian.net/wiki
- Espacio: EPA ("07) Dominio Soluciones Corporativas")
- Las credenciales están en el archivo `.vscode/mcp.json` del workspace
- Directorio base del proyecto: `D:\Proyectos\Sarlaft\Documentacion\Sarlaft\docs\`

## Sección a documentar

- Ruta en Confluence: **Sarlaft 4.0 → Documentación Técnica → Microservicio SarlaftAPI → Log Errores Splunk SarlaftApi**
- Buscar la página principal usando CQL y obtener su ID

---

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
  - `/rest/api/content/<id>/child/comment` con `depth=all`, `expand=body.storage,version`
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
- Descarga usando curl con autenticación Basic Auth (email + token del mcp.json):
  - URL base: `https://segurosti.atlassian.net/wiki` + `_links.download`
- Guarda según tipo:
  - `docs/docx/` → archivos Word
  - `docs/pdf/` → archivos PDF
  - `docs/xlsx/` → archivos Excel
  - `<Subseccion>/img/` → imágenes (PNG, JPG, etc.)
  - `<Subseccion>/attachments/` → archivos JSON y otros
- Crea las carpetas si no existen
- Nombra los archivos descriptivamente (ej: `ProcesoMasivoRequest.json` en vez de `Request.json`)

## 5. Generación de archivos Markdown

- **Un archivo `.md` por cada página** de Confluence — nunca mezclar información de páginas distintas
- Respeta la jerarquía de carpetas:

```
MicroservicioSarlaftAPI/<Subseccion>/index.md        — índice de la subsección
MicroservicioSarlaftAPI/<Subseccion>/<Pagina>.md      — una por sub-página
MicroservicioSarlaftAPI/<Subseccion>/img/             — imágenes
MicroservicioSarlaftAPI/<Subseccion>/attachments/     — JSON y otros adjuntos
```

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
  - Macros `ac:image` → `![alt](./img/<filename>)`
  - Links internos de Confluence → referencias relativas entre los .md creados
  - Nombres técnicos (tablas BD, campos, endpoints, perfiles) → backticks: `` `nombre` ``

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

---

> **Nota:** Este prompt es reutilizable para cualquier subsección del Microservicio SarlaftAPI (Servicios Web, Procesos Carga Masiva, Estructura Proyecto, etc.) — solo cambia `<NOMBRE_SECCION>` por el título de la página raíz en Confluence.
