"""
download_backweb.py — Descarga y documenta 'Microservicio Backweb' de Confluence.

Jerarquía Confluence (espacio EPA):
  Microservicio Backweb [2398027809]
    ├── Servicios Web - Microservicio Backweb [2398486540]
    │     ├── Servicio Resultado Evaluación [2398191643]
    │     ├── Servicio Consultar evaluaciones de un tomador. [2427879670]
    │     ├── Servicio de consulta Oficinas Por Asesor [2676228312]
    │     ├── Servicio Consultar url de formulario. [2659942401]
    │     ├── Servicio para obtener URL Modulo consulta (SEUS 4) [2836725968]
    │     ├── Servicio Consultar Entidades [2893152310]
    │     ├── Servicio cancelar evaluación [2896625843]
    │     ├── Servicio Finalizar Evaluación [2903408641]
    │     ├── Servicio Matricular Entidad [2928377889]
    │     ├── Servicio Cambiar estado entidad [2935160848]
    │     ├── Desmarcar cliente peps [2968715399]
    │     ├── Servicio Matricular Salario Mínimo [4222550059]
    │     ├── Servicio Consultar Salario Mínimo [4221992968]
    │     ├── Servicio Matricular País Gafi [4902944769]
    │     ├── Servicio Consultar País Gafi por Código [4903010314]
    │     └── Servicio Consultar Países Gafi por Código y Categoría [4903010325]
    ├── Diseño Arquitectura [2398159023]
    ├── Estructura Proyecto - Microservicio Backweb [2397339707]
    ├── Backweb Log de Errores en Splunk [2432270358]
    ├── Configuración Ambiente - Microservicio Backweb [2398715932]
    ├── Datasource - Conexiones Multiples [3537108995]
    ├── BaseJpaConfig [3632300037]
    ├── JpaConfig [3538321427]
    ├── ReadOnlyJpaConfig [3539337222]
    ├── Anotación - ReadOnlyRepository [3539238915]
    └── Configuración HealtchCheck con librería actuator - SarlaftBackWeb [3598778517]

Salida local:
  docs/MicroservicioBackweb/
    ├── index.md
    ├── EstructuraProyecto.md
    ├── DisenoArquitectura.md
    ├── LogErroresSplunk.md
    ├── ConfiguracionAmbiente.md
    ├── DatasourceConexionesMultiples.md
    ├── BaseJpaConfig.md
    ├── JpaConfig.md
    ├── ReadOnlyJpaConfig.md
    ├── AnotacionReadOnlyRepository.md
    ├── ConfiguracionHealthCheck.md
    ├── ServiciosWeb/
    │     ├── index.md
    │     ├── ServicioResultadoEvaluacion.md
    │     ├── ServicioConsultarEvaluacionesTomador.md
    │     ├── ServicioConsultaOficinasAsesor.md
    │     ├── ServicioConsultarUrlFormulario.md
    │     ├── ServicioObtenerUrlModuloConsultaSEUS4.md
    │     ├── ServicioConsultarEntidades.md
    │     ├── ServicioCancelarEvaluacion.md
    │     ├── ServicioFinalizarEvaluacion.md
    │     ├── ServicioMatricularEntidad.md
    │     ├── ServicioCambiarEstadoEntidad.md
    │     ├── DesmarcarClientePeps.md
    │     ├── ServicioMatricularSalarioMinimo.md
    │     ├── ServicioConsultarSalarioMinimo.md
    │     ├── ServicioMatricularPaisGafi.md
    │     ├── ServicioConsultarPaisGafiPorCodigo.md
    │     └── ServicioConsultarPaisesGafiCodigoCat.md
    ├── img/
    └── attachments/
"""
import os
import re
import html as html_lib
from datetime import date
from pathlib import Path

import requests
from confluence_config import BASE_URL, HEADERS, DL_HEADERS, DOCS_ROOT

# ---------------------------------------------------------------------------
# Configuración de rutas
# ---------------------------------------------------------------------------
BW_ROOT  = os.path.join(DOCS_ROOT, "MicroservicioBackweb")
IMG_DIR  = os.path.join(BW_ROOT, "img")
ATT_DIR  = os.path.join(BW_ROOT, "attachments")
PDF_DIR  = os.path.join(DOCS_ROOT, "pdf")
DOCX_DIR = os.path.join(DOCS_ROOT, "docx")
XLSX_DIR = os.path.join(DOCS_ROOT, "xlsx")
TODAY    = date.today().strftime("%Y-%m-%d")

for folder in [BW_ROOT, IMG_DIR, ATT_DIR]:
    os.makedirs(folder, exist_ok=True)

# ---------------------------------------------------------------------------
# Jerarquía de páginas
# ---------------------------------------------------------------------------
PAGE_TREE = {
    "id": "2398027809",
    "title": "Microservicio Backweb",
    "file": "index.md",
    "children": [
        {
            "id": "2397339707",
            "title": "Estructura Proyecto - Microservicio Backweb",
            "file": "EstructuraProyecto.md",
            "children": []
        },
        {
            "id": "2398159023",
            "title": "Diseño Arquitectura",
            "file": "DisenoArquitectura.md",
            "children": []
        },
        {
            "id": "2398715932",
            "title": "Configuración Ambiente - Microservicio Backweb",
            "file": "ConfiguracionAmbiente.md",
            "children": []
        },
        {
            "id": "2432270358",
            "title": "Backweb Log de Errores en Splunk",
            "file": "LogErroresSplunk.md",
            "children": []
        },
        {
            "id": "3537108995",
            "title": "Datasource - Conexiones Multiples",
            "file": "DatasourceConexionesMultiples.md",
            "children": []
        },
        {
            "id": "3538321427",
            "title": "JpaConfig",
            "file": "JpaConfig.md",
            "children": []
        },
        {
            "id": "3539337222",
            "title": "ReadOnlyJpaConfig",
            "file": "ReadOnlyJpaConfig.md",
            "children": []
        },
        {
            "id": "3539238915",
            "title": "Anotación - ReadOnlyRepository",
            "file": "AnotacionReadOnlyRepository.md",
            "children": []
        },
        {
            "id": "3632300037",
            "title": "BaseJpaConfig",
            "file": "BaseJpaConfig.md",
            "children": []
        },
        {
            "id": "3598778517",
            "title": "Configuración HealtchCheck con librería actuator - SarlaftBackWeb",
            "file": "ConfiguracionHealthCheck.md",
            "children": []
        },
        {
            "id": "2398486540",
            "title": "Servicios Web - Microservicio Backweb",
            "file": "ServiciosWeb/index.md",
            "children": [
                {
                    "id": "2398191643",
                    "title": "Servicio Resultado Evaluación",
                    "file": "ServiciosWeb/ServicioResultadoEvaluacion.md",
                    "children": []
                },
                {
                    "id": "2427879670",
                    "title": "Servicio Consultar evaluaciones de un tomador.",
                    "file": "ServiciosWeb/ServicioConsultarEvaluacionesTomador.md",
                    "children": []
                },
                {
                    "id": "2659942401",
                    "title": "Servicio Consultar url de formulario.",
                    "file": "ServiciosWeb/ServicioConsultarUrlFormulario.md",
                    "children": []
                },
                {
                    "id": "2676228312",
                    "title": "Servicio de consulta Oficinas Por Asesor",
                    "file": "ServiciosWeb/ServicioConsultaOficinasAsesor.md",
                    "children": []
                },
                {
                    "id": "2836725968",
                    "title": "Servicio para obtener URL Modulo consulta (SEUS 4)",
                    "file": "ServiciosWeb/ServicioObtenerUrlModuloConsultaSEUS4.md",
                    "children": []
                },
                {
                    "id": "2893152310",
                    "title": "Servicio Consultar Entidades",
                    "file": "ServiciosWeb/ServicioConsultarEntidades.md",
                    "children": []
                },
                {
                    "id": "2896625843",
                    "title": "Servicio cancelar evaluación",
                    "file": "ServiciosWeb/ServicioCancelarEvaluacion.md",
                    "children": []
                },
                {
                    "id": "2903408641",
                    "title": "Servicio Finalizar Evaluación",
                    "file": "ServiciosWeb/ServicioFinalizarEvaluacion.md",
                    "children": []
                },
                {
                    "id": "2928377889",
                    "title": "Servicio Matricular Entidad",
                    "file": "ServiciosWeb/ServicioMatricularEntidad.md",
                    "children": []
                },
                {
                    "id": "2935160848",
                    "title": "Servicio Cambiar estado entidad",
                    "file": "ServiciosWeb/ServicioCambiarEstadoEntidad.md",
                    "children": []
                },
                {
                    "id": "2968715399",
                    "title": "Desmarcar cliente peps",
                    "file": "ServiciosWeb/DesmarcarClientePeps.md",
                    "children": []
                },
                {
                    "id": "4222550059",
                    "title": "Servicio Matricular Salario Mínimo",
                    "file": "ServiciosWeb/ServicioMatricularSalarioMinimo.md",
                    "children": []
                },
                {
                    "id": "4221992968",
                    "title": "Servicio Consultar Salario Mínimo",
                    "file": "ServiciosWeb/ServicioConsultarSalarioMinimo.md",
                    "children": []
                },
                {
                    "id": "4902944769",
                    "title": "Servicio Matricular País Gafi",
                    "file": "ServiciosWeb/ServicioMatricularPaisGafi.md",
                    "children": []
                },
                {
                    "id": "4903010314",
                    "title": "Servicio Consultar País Gafi por Código",
                    "file": "ServiciosWeb/ServicioConsultarPaisGafiPorCodigo.md",
                    "children": []
                },
                {
                    "id": "4903010325",
                    "title": "Servicio Consultar Países Gafi por Código y Categoría",
                    "file": "ServiciosWeb/ServicioConsultarPaisesGafiCodigoCat.md",
                    "children": []
                },
            ]
        },
    ]
}


# ---------------------------------------------------------------------------
# HTML → Markdown
# ---------------------------------------------------------------------------
def html_to_md(raw: str, page_id: str = "") -> str:
    if not raw:
        return ""
    md = raw

    # ── Macros Confluence: info / warning / note / tip / panel ────────────
    def macro_box(m):
        name = m.group(1).lower()
        body = m.group(2) if m.group(2) else ""
        icons = {"info": "ℹ️", "warning": "⚠️", "note": "📝", "tip": "💡", "panel": "📋"}
        icon = icons.get(name, "📌")
        body_clean = re.sub(r'<[^>]+>', '', body).strip()
        lines = [f"> {icon} **{name.upper()}**: {line}" if i == 0 else f"> {line}"
                 for i, line in enumerate(body_clean.split('\n'))]
        return "\n" + "\n".join(lines) + "\n"

    md = re.sub(
        r'<ac:structured-macro[^>]*ac:name="(info|warning|note|tip|panel)"[^>]*>'
        r'(.*?)</ac:structured-macro>',
        macro_box, md, flags=re.S | re.I
    )

    # Macro code con lenguaje
    def code_macro(m):
        lang = ""
        lang_match = re.search(r'ac:name="language"[^>]*>(.*?)</ac:parameter>', m.group(0), re.S | re.I)
        if lang_match:
            lang = lang_match.group(1).strip()
        cdata_match = re.search(r'<!\[CDATA\[(.*?)\]\]>', m.group(0), re.S)
        body = cdata_match.group(1) if cdata_match else ""
        return f"\n```{lang}\n{body.strip()}\n```\n"

    md = re.sub(
        r'<ac:structured-macro[^>]*ac:name="code"[^>]*>.*?</ac:structured-macro>',
        code_macro, md, flags=re.S | re.I
    )

    # Eliminar otras macros no procesadas
    md = re.sub(r'<ac:structured-macro[^>]*>.*?</ac:structured-macro>', '', md, flags=re.S)
    md = re.sub(r'<ac:parameter[^>]*>.*?</ac:parameter>', '', md, flags=re.S)
    md = re.sub(r'<ac:plain-text-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-body>',
                r'\n```\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<ac:rich-text-body[^>]*>(.*?)</ac:rich-text-body>',
                r'\1', md, flags=re.S)

    # ── Imágenes Confluence (adjuntos de la página) ───────────────────────
    md = re.sub(
        r'<ac:image[^>]*>\s*<ri:attachment\s+ri:filename="([^"]+)"[^/]*/?\s*></ac:image>',
        lambda m: f"![{m.group(1)}](img/{m.group(1)})",
        md, flags=re.S | re.I
    )
    md = re.sub(
        r'<ac:image[^>]*>.*?<ri:attachment\s+ri:filename="([^"]+)".*?</ac:image>',
        lambda m: f"![{m.group(1)}](img/{m.group(1)})",
        md, flags=re.S | re.I
    )

    # ── Links Confluence internos → referencias relativas ─────────────────
    md = re.sub(
        r'<ac:link[^>]*>\s*<ri:page\s+ri:content-title="([^"]+)"[^/]*/?\s*>'
        r'(?:\s*<ac:plain-text-link-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-link-body>)?'
        r'\s*</ac:link>',
        lambda m: f"[{m.group(2) or m.group(1)}]({m.group(1).replace(' ', '_')}.md)",
        md, flags=re.S | re.I
    )
    md = re.sub(r'<ac:link[^>]*>.*?</ac:link>', '', md, flags=re.S)

    # ── view-file macro → link a attachment ──────────────────────────────
    md = re.sub(
        r'<ri:attachment\s+ri:filename="([^"]+)"[^/]*/?>',
        lambda m: f"[{m.group(1)}](attachments/{m.group(1)})",
        md, flags=re.S | re.I
    )

    # ── Formato de texto ──────────────────────────────────────────────────
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>',           r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>',          r'_\1_',  md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>',            r'_\1_',  md, flags=re.S)
    md = re.sub(r'<u[^>]*>(.*?)</u>',            r'<u>\1</u>', md, flags=re.S)
    md = re.sub(r'<del[^>]*>(.*?)</del>',        r'~~\1~~', md, flags=re.S)
    md = re.sub(r'<s[^>]*>(.*?)</s>',            r'~~\1~~', md, flags=re.S)

    # ── Headings ──────────────────────────────────────────────────────────
    for n in range(1, 7):
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>',
                    rf'\n{"#" * (n + 1)} \1\n', md, flags=re.S)

    # ── Bloques de código ─────────────────────────────────────────────────
    def code_block(m):
        lang = m.group(1) or ""
        body = m.group(2) or ""
        body = html_lib.unescape(re.sub(r'<[^>]+>', '', body))
        return f"\n```{lang}\n{body.strip()}\n```\n"

    md = re.sub(
        r'<code\s+[^>]*data-language="([^"]*)"[^>]*>(.*?)</code>',
        code_block, md, flags=re.S
    )
    md = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>',
                r'\n```\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>',
                r'\n```\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.S)

    # ── Links externos ────────────────────────────────────────────────────
    def replace_link(m):
        href = m.group(1)
        text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        return f"[{text or href}]({href})"

    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
                replace_link, md, flags=re.S)

    # ── Imágenes HTML estándar ────────────────────────────────────────────
    md = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*/?>',
                r'![\1](\2)', md, flags=re.S)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',
                r'![imagen](\1)', md, flags=re.S)

    # ── Listas ────────────────────────────────────────────────────────────
    md = re.sub(r'<ul[^>]*>', '\n', md)
    md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<ol[^>]*>', '\n', md)
    md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.S)

    # ── Tablas HTML → Markdown ────────────────────────────────────────────
    def convert_table(m):
        table_html = m.group(0)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.S)
        if not rows:
            return ""
        result_rows = []
        header_done = False
        for row in rows:
            cells_th = re.findall(r'<th[^>]*>(.*?)</th>', row, re.S)
            cells_td = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            cells = cells_th or cells_td
            clean_cells = []
            for c in cells:
                clean = re.sub(r'<[^>]+>', '', c)
                clean = html_lib.unescape(clean).strip().replace('\n', ' ')
                clean_cells.append(clean)
            if not clean_cells:
                continue
            row_str = "| " + " | ".join(clean_cells) + " |"
            result_rows.append(row_str)
            if not header_done:
                sep = "| " + " | ".join(["---"] * len(clean_cells)) + " |"
                result_rows.append(sep)
                header_done = True
        return "\n" + "\n".join(result_rows) + "\n"

    md = re.sub(r'<table[^>]*>.*?</table>', convert_table, md, flags=re.S)

    # ── Párrafos y estructura ─────────────────────────────────────────────
    md = re.sub(r'<p[^>]*>',  '\n', md)
    md = re.sub(r'</p>', '\n', md)
    md = re.sub(r'<br\s*/?>', '\n', md)
    md = re.sub(r'<hr\s*/?>', '\n---\n', md)
    md = re.sub(r'<div[^>]*>', '\n', md)
    md = re.sub(r'</div>', '\n', md)
    md = re.sub(r'<span[^>]*>', '', md)
    md = re.sub(r'</span>', '', md)
    md = re.sub(r'<section[^>]*>', '\n', md)
    md = re.sub(r'</section>', '\n', md)

    # ── Eliminar tags restantes ───────────────────────────────────────────
    md = re.sub(r'<[^>]+>', '', md)

    # ── Entidades HTML ────────────────────────────────────────────────────
    md = html_lib.unescape(md)

    # ── Limpiar espacios ──────────────────────────────────────────────────
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    return md.strip()


# ---------------------------------------------------------------------------
# Descarga binario desde Confluence
# ---------------------------------------------------------------------------
def download_binary(download_path: str, dest_file: str) -> bool:
    url = f"{BASE_URL}/wiki{download_path}" if download_path.startswith("/") else download_path
    try:
        resp = requests.get(url, headers=DL_HEADERS, stream=True, timeout=60)
        resp.raise_for_status()
        with open(dest_file, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"    [ERROR descarga] {dest_file}: {e}")
        return False


# ---------------------------------------------------------------------------
# Obtiene body de una página en formato storage (para detectar adjuntos ref.)
# ---------------------------------------------------------------------------
def get_page_storage(page_id: str) -> str:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}?body-format=storage"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json().get("body", {}).get("storage", {}).get("value", "")


# ---------------------------------------------------------------------------
# Obtiene body de una página (view format) + metadatos
# ---------------------------------------------------------------------------
def get_page_view(page_id: str) -> dict:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}?body-format=view"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return {
        "title":   data.get("title", ""),
        "body":    data.get("body", {}).get("view", {}).get("value", ""),
        "version": data.get("version", {}).get("number", "?"),
        "date":    (data.get("version", {}).get("createdAt") or "")[:10],
        "author":  data.get("version", {}).get("authorId", ""),
        "url":     f"{BASE_URL}/wiki/spaces/EPA/pages/{page_id}",
    }


# ---------------------------------------------------------------------------
# Extrae nombres de adjuntos referenciados en el storage body
# ---------------------------------------------------------------------------
def get_referenced_attachments(storage_body: str) -> set:
    refs = set()
    # ac:image / ri:attachment
    refs.update(re.findall(r'ri:filename="([^"]+)"', storage_body, re.I))
    # view-file macro
    refs.update(re.findall(r'ac:name="filename"[^>]*>\s*([^<]+)\s*<', storage_body, re.I))
    return refs


# ---------------------------------------------------------------------------
# Procesa adjuntos (solo los referenciados en el cuerpo)
# ---------------------------------------------------------------------------
def process_attachments(page_id: str, referenced: set, out_dir: str) -> dict:
    """
    Descarga adjuntos referenciados.
    Retorna dict: {filename: rel_path_from_out_dir}
    """
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/attachments?limit=200"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        atts = resp.json().get("results", [])
    except Exception as e:
        print(f"  [ERROR adjuntos {page_id}]: {e}")
        return {}

    result = {}
    for att in atts:
        filename   = att.get("title", "")
        media_type = att.get("mediaType", "")
        dl_path    = att.get("_links", {}).get("download", "")

        # Si hay referencias explícitas, solo descargar las referenciadas
        if referenced and filename not in referenced:
            continue

        # Determinar destino según tipo
        if media_type.startswith("image/"):
            dest_file = os.path.join(IMG_DIR, filename)
            rel_path  = os.path.relpath(IMG_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        elif media_type == "application/pdf":
            dest_file = os.path.join(PDF_DIR, filename)
            rel_path  = os.path.relpath(PDF_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        elif "wordprocessingml" in media_type or media_type == "application/msword":
            dest_file = os.path.join(DOCX_DIR, filename)
            rel_path  = os.path.relpath(DOCX_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        elif "spreadsheetml" in media_type or "ms-excel" in media_type:
            dest_file = os.path.join(XLSX_DIR, filename)
            rel_path  = os.path.relpath(XLSX_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        elif media_type in ("application/json", "text/plain", "text/xml", "application/xml"):
            dest_file = os.path.join(ATT_DIR, filename)
            rel_path  = os.path.relpath(ATT_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        else:
            dest_file = os.path.join(ATT_DIR, filename)
            rel_path  = os.path.relpath(ATT_DIR, out_dir).replace("\\", "/") + f"/{filename}"

        if not os.path.exists(dest_file):
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            ok = download_binary(dl_path, dest_file)
            if ok:
                print(f"  [DESCARGADO] {filename} ({media_type})")
        else:
            print(f"  [YA EXISTE]  {filename}")

        result[filename] = rel_path

    return result


# ---------------------------------------------------------------------------
# Extrae comentarios footer de una página
# ---------------------------------------------------------------------------
def get_footer_comments(page_id: str) -> list:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/footer-comments?body-format=view&limit=50"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.json().get("results", [])
    except Exception as e:
        print(f"  [WARN comentarios {page_id}]: {e}")
        return []


def render_comments(comments: list) -> str:
    if not comments:
        return ""
    lines = ["\n---\n\n## Comentarios de Confluence\n"]
    for i, c in enumerate(comments, 1):
        body_html = c.get("body", {}).get("view", {}).get("value", "")
        body_md  = html_to_md(body_html)
        ver      = c.get("version", {})
        author   = ver.get("authorId", "desconocido")
        date_str = (ver.get("createdAt") or "")[:10]
        cid      = c.get("id", "?")

        lines.append(f"### Comentario {i}\n")
        lines.append(f"> **Autor:** {author}  ")
        lines.append(f"> **Fecha:** {date_str}  ")
        lines.append(f"> **ID:** {cid}\n")
        if body_md:
            lines.append(body_md)
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Genera TOC para páginas índice
# ---------------------------------------------------------------------------
def generate_toc(node: dict) -> str:
    toc = "## Contenido\n\n"
    for child in node.get("children", []):
        child_file = child["file"]
        # Ruta relativa desde la carpeta del padre
        parent_dir = os.path.dirname(os.path.join(BW_ROOT, node["file"]))
        child_full = os.path.join(BW_ROOT, child_file)
        rel = os.path.relpath(child_full, parent_dir).replace("\\", "/")
        toc += f"- [{child['title']}]({rel})\n"
        for gc in child.get("children", []):
            gc_full = os.path.join(BW_ROOT, gc["file"])
            rel_gc  = os.path.relpath(gc_full, parent_dir).replace("\\", "/")
            toc += f"  - [{gc['title']}]({rel_gc})\n"
    return toc


# ---------------------------------------------------------------------------
# Procesamiento recursivo de una página
# ---------------------------------------------------------------------------
results_log = []


def process_node(node: dict) -> None:
    page_id  = node["id"]
    rel_file = node["file"]
    has_children = bool(node.get("children"))

    out_file = os.path.join(BW_ROOT, rel_file)
    out_dir  = os.path.dirname(out_file)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n[{page_id}] {node['title']} → {rel_file}")

    try:
        # 1) Contenido
        page     = get_page_view(page_id)
        title    = page["title"]
        body_md  = html_to_md(page["body"], page_id)

        # 2) Adjuntos referenciados (via storage body)
        storage_body = get_page_storage(page_id)
        referenced   = get_referenced_attachments(storage_body)
        att_map      = process_attachments(page_id, referenced, out_dir)

        # Reemplazar rutas de imágenes en body_md si hay mapeo
        for fname, rel_path in att_map.items():
            body_md = body_md.replace(f"img/{fname}", rel_path)
            body_md = body_md.replace(f"attachments/{fname}", rel_path)

        # Reemplazar URLs externas de Confluence que apuntan a adjuntos descargados
        # Patrón: ![alt](https://...atlassian.net/wiki/download/attachments/{id}/{fname}?...)
        def replace_confluence_img_url(m):
            url = m.group(2)
            for fname, rel_path in att_map.items():
                if fname in url:
                    return f"![{m.group(1)}]({rel_path})"
            return m.group(0)
        body_md = re.sub(
            r'!\[([^\]]*)\]\((https://[^)]*atlassian\.net/wiki/download/[^)]+)\)',
            replace_confluence_img_url, body_md
        )

        # 3) Comentarios
        comments = get_footer_comments(page_id)
        comments_md = render_comments(comments)

        # ── Construir cabecera ──────────────────────────────────────────
        parent_title = node.get("parent_title", "Microservicio Backweb")
        content  = f"# {title}\n\n"
        content += f"> **Fuente Confluence:** [{title}]({page['url']})\n"
        content += f"> **Última modificación:** {page['date']} · versión {page['version']}\n"
        content += f"> **Sección:** [{parent_title}](./index.md)\n\n"

        # ToC si tiene hijos
        if has_children:
            content += generate_toc(node)
            content += "\n---\n\n"

        # Adjuntos no-imagen
        file_links = [
            f"- [{fname}]({rp})"
            for fname, rp in att_map.items()
            if not rp.split("/")[-1].lower().endswith(
                (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")
            )
        ]
        if file_links:
            content += "## Archivos Adjuntos\n\n"
            content += "\n".join(file_links) + "\n\n---\n\n"

        content += body_md

        # Comentarios
        if comments_md:
            content += "\n" + comments_md

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] → {out_file}")
        results_log.append({"id": page_id, "title": title, "file": rel_file, "ok": True})

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"  [ERROR] {page_id}: {e}")
        results_log.append({
            "id": page_id, "title": node["title"],
            "file": rel_file, "ok": False, "error": str(e)
        })

    # Hijos
    for child in node.get("children", []):
        child["parent_title"] = node.get("title", "Microservicio Backweb")
        process_node(child)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Descargando: Microservicio Backweb")
    print(f"Destino:     {BW_ROOT}")
    print(f"Fecha:       {TODAY}")
    print("=" * 60)

    process_node(PAGE_TREE)

    ok  = sum(1 for r in results_log if r["ok"])
    err = sum(1 for r in results_log if not r["ok"])

    print("\n" + "=" * 60)
    print(f"RESUMEN: {ok} páginas OK, {err} errores")
    print("=" * 60)

    # Verificación de archivos
    base = BW_ROOT
    print("\n=== Archivos generados ===")
    for root_dir, dirs, files in os.walk(base):
        level = root_dir.replace(base, "").count(os.sep)
        indent = "  " * level
        rel_root = os.path.relpath(root_dir, base)
        print(f"{indent}{rel_root}/")
        for f in sorted(files):
            size = os.path.getsize(os.path.join(root_dir, f))
            print(f"{'  ' * (level+1)}{f}  ({size} bytes)")

    if err:
        print("\n=== Errores ===")
        for r in results_log:
            if not r["ok"]:
                print(f"  [{r['id']}] {r['title']}: {r.get('error', '?')}")


if __name__ == "__main__":
    main()
