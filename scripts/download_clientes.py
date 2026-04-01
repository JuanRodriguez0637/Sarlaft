"""
download_clientes.py — Descarga y documenta 'Microservicio SarlaftClientesMS' de Confluence.

Jerarquía Confluence (espacio EPA):
  Microservicio SarlaftClientesMS [2701656178]
    ├── Estructura del Proyecto - Microservicio SarlaftClientes [2719285328]
    ├── Configuración Ambiente - Microservicio SarlaftClientes [2719612975]
    ├── Comunicaciones - Microservicio SarlaftClientes [2718597252]
    │     ├── Consultar clientes en fuentes de externas y actualizar base de datos de Sarlaft 4.0 - NoMasivo [2719023220]
    │     ├── Completar información de Clientes para Evaluación Masiva. [2740584506]
    │     └── Consultar clientes en fuentes de externas (Proceso de actualización) [2873163781]
    └── Configuración HealtchCheck con librería actuator - sarlaftclientes [3532554423]

Salida local:
  docs/MicroservicioSarlaftClientesMS/
    ├── index.md
    ├── EstructuraProyecto.md
    ├── ConfiguracionAmbiente.md
    ├── ConfiguracionHealthCheck.md
    ├── Comunicaciones/
    │     ├── index.md
    │     ├── ConsultarClientesFuentesExternasNoMasivo.md
    │     ├── CompletarInformacionClientesEvaluacionMasiva.md
    │     └── ConsultarClientesFuentesExternasActualizacion.md
    ├── img/
    └── attachments/
"""
import os
import re
import html as html_lib
from datetime import date
from pathlib import Path

import requests
import sys
sys.path.insert(0, os.path.dirname(__file__))
from confluence_config import BASE_URL, HEADERS, DL_HEADERS, DOCS_ROOT

# ---------------------------------------------------------------------------
# Configuración de rutas
# ---------------------------------------------------------------------------
CL_ROOT  = os.path.join(DOCS_ROOT, "MicroservicioSarlaftClientesMS")
IMG_DIR  = os.path.join(CL_ROOT, "img")
ATT_DIR  = os.path.join(CL_ROOT, "attachments")
PDF_DIR  = os.path.join(DOCS_ROOT, "pdf")
DOCX_DIR = os.path.join(DOCS_ROOT, "docx")
XLSX_DIR = os.path.join(DOCS_ROOT, "xlsx")
TODAY    = date.today().strftime("%Y-%m-%d")

for folder in [CL_ROOT]:
    os.makedirs(folder, exist_ok=True)

# ---------------------------------------------------------------------------
# Jerarquía de páginas
# ---------------------------------------------------------------------------
PAGE_TREE = {
    "id": "2701656178",
    "title": "Microservicio SarlaftClientesMS",
    "file": "index.md",
    "children": [
        {
            "id": "2719285328",
            "title": "Estructura del Proyecto - Microservicio SarlaftClientes",
            "file": "EstructuraProyecto.md",
            "children": []
        },
        {
            "id": "2719612975",
            "title": "Configuración Ambiente - Microservicio SarlaftClientes",
            "file": "ConfiguracionAmbiente.md",
            "children": []
        },
        {
            "id": "2718597252",
            "title": "Comunicaciones - Microservicio SarlaftClientes",
            "file": "Comunicaciones/index.md",
            "children": [
                {
                    "id": "2719023220",
                    "title": "Consultar clientes en fuentes de externas y actualizar base de datos de Sarlaft 4.0 - NoMasivo",
                    "file": "Comunicaciones/ConsultarClientesFuentesExternasNoMasivo.md",
                    "children": []
                },
                {
                    "id": "2740584506",
                    "title": "Completar información de Clientes para Evaluación Masiva.",
                    "file": "Comunicaciones/CompletarInformacionClientesEvaluacionMasiva.md",
                    "children": []
                },
                {
                    "id": "2873163781",
                    "title": "Consultar clientes en fuentes de externas (Proceso de actualización)",
                    "file": "Comunicaciones/ConsultarClientesFuentesExternasActualizacion.md",
                    "children": []
                },
            ]
        },
        {
            "id": "3532554423",
            "title": "Configuración HealtchCheck con librería actuator - sarlaftclientes",
            "file": "ConfiguracionHealthCheck.md",
            "children": []
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
        if not lang:
            body_strip = body.strip()
            if re.search(r'\bpackage\b|\bimport\b.*\bjava\b|@Bean|public class', body_strip):
                lang = "java"
            elif re.search(r'^(spring|azure|server|app|management):', body_strip, re.M):
                lang = "yaml"
            elif body_strip.startswith('{') or body_strip.startswith('['):
                lang = "json"
            elif re.search(r'implementation|dependencies\s*\{|plugins\s*\{', body_strip):
                lang = "groovy"
            elif re.search(r'\bSELECT\b|\bINSERT\b|\bCREATE TABLE\b', body_strip, re.I):
                lang = "sql"
            else:
                lang = "text"
        return f"\n```{lang}\n{body.strip()}\n```\n"

    md = re.sub(
        r'<ac:structured-macro[^>]*ac:name="code"[^>]*>.*?</ac:structured-macro>',
        code_macro, md, flags=re.S | re.I
    )

    # Eliminar otras macros no procesadas
    md = re.sub(r'<ac:structured-macro[^>]*>.*?</ac:structured-macro>', '', md, flags=re.S)
    md = re.sub(r'<ac:parameter[^>]*>.*?</ac:parameter>', '', md, flags=re.S)
    md = re.sub(r'<ac:plain-text-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-body>',
                r'\n```text\n\1\n```\n', md, flags=re.S)
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

    # ── Headings (shift +1 para respetar jerarquía: h1→##, h2→###, …) ────
    for n in range(1, 7):
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>',
                    rf'\n{"#" * (n + 1)} \1\n', md, flags=re.S)

    # ── Bloques de código ─────────────────────────────────────────────────
    def code_block(m):
        lang = m.group(1) or ""
        body = m.group(2) or ""
        body = html_lib.unescape(re.sub(r'<[^>]+>', '', body))
        if not lang:
            body_strip = body.strip()
            if re.search(r'\bpackage\b|\bimport\b.*\bjava\b|@Bean|public class', body_strip):
                lang = "java"
            elif body_strip.startswith('{') or body_strip.startswith('['):
                lang = "json"
            else:
                lang = "text"
        return f"\n```{lang}\n{body.strip()}\n```\n"

    md = re.sub(
        r'<code\s+[^>]*data-language="([^"]*)"[^>]*>(.*?)</code>',
        code_block, md, flags=re.S
    )
    md = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>',
                r'\n```text\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>',
                r'\n```text\n\1\n```\n', md, flags=re.S)
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
        header_cols = 0
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
            # Pad row to header width (MD056)
            if not header_done:
                header_cols = len(clean_cells)
            else:
                while len(clean_cells) < header_cols:
                    clean_cells.append("")
            row_str = "| " + " | ".join(clean_cells) + " |"
            result_rows.append(row_str)
            if not header_done:
                sep = "| " + " | ".join(["---"] * header_cols) + " |"
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
    md = re.sub(r'\t', '    ', md)           # MD010: tabs → 4 spaces
    md = re.sub(r'\n{3,}', '\n\n', md)       # MD012: max 2 blank lines
    md = re.sub(r'[ \t]+\n', '\n', md)
    # MD032: fix broken list items (- on its own line followed by content)
    md = re.sub(r'^-\s*\n(\S)', r'- \1', md, flags=re.M)
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
    refs.update(re.findall(r'ri:filename="([^"]+)"', storage_body, re.I))
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
        ext = filename.lower().rsplit(".", 1)[-1] if "." in filename else ""
        if media_type.startswith("image/") or ext in ("png", "jpg", "jpeg", "gif", "svg", "webp"):
            img_subdir = os.path.join(out_dir, "img")
            os.makedirs(img_subdir, exist_ok=True)
            dest_file = os.path.join(img_subdir, filename)
            rel_path  = f"img/{filename}"
        elif media_type == "application/pdf" or ext == "pdf":
            dest_file = os.path.join(PDF_DIR, filename)
            rel_path  = os.path.relpath(PDF_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        elif "wordprocessingml" in media_type or media_type == "application/msword" or ext == "docx":
            dest_file = os.path.join(DOCX_DIR, filename)
            rel_path  = os.path.relpath(DOCX_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        elif "spreadsheetml" in media_type or "ms-excel" in media_type or ext in ("xlsx", "xls"):
            dest_file = os.path.join(XLSX_DIR, filename)
            rel_path  = os.path.relpath(XLSX_DIR, out_dir).replace("\\", "/") + f"/{filename}"
        else:
            att_subdir = os.path.join(out_dir, "attachments")
            os.makedirs(att_subdir, exist_ok=True)
            dest_file = os.path.join(att_subdir, filename)
            rel_path  = f"attachments/{filename}"

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
        body_md   = html_to_md(body_html)
        ver       = c.get("version", {})
        author    = ver.get("authorId", "desconocido")
        date_str  = (ver.get("createdAt") or "")[:10]
        cid       = c.get("id", "?")

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
        parent_dir = os.path.dirname(os.path.join(CL_ROOT, node["file"]))
        child_full = os.path.join(CL_ROOT, child_file)
        rel = os.path.relpath(child_full, parent_dir).replace("\\", "/")
        toc += f"- [{child['title']}]({rel})\n"
        for gc in child.get("children", []):
            gc_full = os.path.join(CL_ROOT, gc["file"])
            rel_gc  = os.path.relpath(gc_full, parent_dir).replace("\\", "/")
            toc += f"  - [{gc['title']}]({rel_gc})\n"
    return toc


# ---------------------------------------------------------------------------
# Procesamiento recursivo de una página
# ---------------------------------------------------------------------------
results_log = []


def process_node(node: dict) -> None:
    page_id      = node["id"]
    rel_file     = node["file"]
    has_children = bool(node.get("children"))

    out_file = os.path.join(CL_ROOT, rel_file)
    out_dir  = os.path.dirname(out_file)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n[{page_id}] {node['title']} → {rel_file}")

    try:
        # 1) Contenido
        page    = get_page_view(page_id)
        title   = page["title"]
        body_md = html_to_md(page["body"], page_id)

        # 2) Adjuntos referenciados (via storage body)
        storage_body = get_page_storage(page_id)
        referenced   = get_referenced_attachments(storage_body)
        att_map      = process_attachments(page_id, referenced, out_dir)

        # Reemplazar rutas de imágenes en body_md si hay mapeo
        for fname, rel_path in att_map.items():
            body_md = body_md.replace(f"img/{fname}", rel_path)
            body_md = body_md.replace(f"attachments/{fname}", rel_path)

        # Reemplazar URLs externas de Confluence que apuntan a adjuntos descargados
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
        comments    = get_footer_comments(page_id)
        comments_md = render_comments(comments)

        # ── Construir cabecera ──────────────────────────────────────────
        parent_title = node.get("parent_title", "Microservicio SarlaftClientesMS")
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

        # MD047: newline at end of file
        if not content.endswith("\n"):
            content += "\n"

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
        child["parent_title"] = node.get("title", "Microservicio SarlaftClientesMS")
        process_node(child)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Descargando: Microservicio SarlaftClientesMS")
    print(f"Destino:     {CL_ROOT}")
    print(f"Fecha:       {TODAY}")
    print("=" * 60)

    process_node(PAGE_TREE)

    ok  = sum(1 for r in results_log if r["ok"])
    err = sum(1 for r in results_log if not r["ok"])

    print("\n" + "=" * 60)
    print(f"RESUMEN: {ok} páginas OK, {err} errores")
    print("=" * 60)

    # Verificación de archivos
    print("\n=== Archivos generados ===")
    for root_dir, dirs, files in os.walk(CL_ROOT):
        level  = root_dir.replace(CL_ROOT, "").count(os.sep)
        indent = "  " * level
        rel_root = os.path.relpath(root_dir, CL_ROOT)
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
