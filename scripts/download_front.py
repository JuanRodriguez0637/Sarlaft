"""
download_front.py — Descarga y documenta la sección 'Front' de Confluence.

Jerarquía Confluence:
  Sarlaft 4.0 → Documentación Técnica → Front [1985511647]
    ├── Diseño MonoRepositorio. [2233073714]
    ├── Configuración ambiente [2233466927]
    │     └── Configuración Ambiente - Pasos importantes [3467214883]
    ├── Despliegue [2505998354]
    ├── Despliegue con Plantillas [3968991251]
    └── Errores [3242721320]
          └── error:0308010C:digital envelope routines::unsupported [3242819613]

Salida local:
  docs/Front/
    ├── index.md
    ├── DisenoMonoRepositorio.md
    ├── ConfiguracionAmbiente/
    │     ├── index.md
    │     └── ConfiguracionAmbientePasosImportantes.md
    ├── Despliegue.md
    ├── DespliegueConPlantillas.md
    └── Errores/
          ├── index.md
          └── ErrorDigitalEnvelopeRoutines.md
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
FRONT_ROOT = os.path.join(DOCS_ROOT, "Front")
TODAY = date.today().strftime("%Y-%m-%d")

IMG_FRONT = os.path.join(FRONT_ROOT, "img")

PDF_DIR  = os.path.join(DOCS_ROOT, "pdf")
DOCX_DIR = os.path.join(DOCS_ROOT, "docx")
XLSX_DIR = os.path.join(DOCS_ROOT, "xlsx")

for folder in [FRONT_ROOT, IMG_FRONT]:
    os.makedirs(folder, exist_ok=True)

# ---------------------------------------------------------------------------
# Jerarquía de páginas
# ---------------------------------------------------------------------------
PAGE_TREE = {
    "id": "1985511647",
    "title": "Front",
    "file": "index.md",
    "children": [
        {
            "id": "2233073714",
            "title": "Diseño MonoRepositorio.",
            "file": "DisenoMonoRepositorio.md",
            "children": []
        },
        {
            "id": "2233466927",
            "title": "Configuración ambiente",
            "file": "ConfiguracionAmbiente/index.md",
            "children": [
                {
                    "id": "3467214883",
                    "title": "Configuración Ambiente - Pasos importantes",
                    "file": "ConfiguracionAmbiente/ConfiguracionAmbientePasosImportantes.md",
                    "children": []
                }
            ]
        },
        {
            "id": "2505998354",
            "title": "Despliegue",
            "file": "Despliegue.md",
            "children": []
        },
        {
            "id": "3968991251",
            "title": "Despliegue con Plantillas",
            "file": "DespliegueConPlantillas.md",
            "children": []
        },
        {
            "id": "3242721320",
            "title": "Errores",
            "file": "Errores/index.md",
            "children": [
                {
                    "id": "3242819613",
                    "title": "error:0308010C:digital envelope routines::unsupported",
                    "file": "Errores/ErrorDigitalEnvelopeRoutines.md",
                    "children": []
                }
            ]
        }
    ]
}

# ---------------------------------------------------------------------------
# Mapa page_id → ruta .md relativa a FRONT_ROOT (para resolver links internos)
# ---------------------------------------------------------------------------
def _build_id_map(node: dict, result: dict = None) -> dict:
    if result is None:
        result = {}
    result[node["id"]] = node["file"]
    for child in node.get("children", []):
        _build_id_map(child, result)
    return result

PAGE_ID_MAP: dict = _build_id_map(PAGE_TREE)

# ---------------------------------------------------------------------------
# HTML → Markdown
# ---------------------------------------------------------------------------
def html_to_md(raw: str, img_rel_path: str = "img", out_dir: str = FRONT_ROOT) -> str:
    """Converts Confluence storage/view HTML to Markdown."""
    if not raw:
        return ""
    md = raw

    # ── Macros Confluence ─────────────────────────────────────────────────
    def macro_box(m):
        name = m.group(1).lower()
        body = m.group(2) if m.group(2) else ""
        icons = {"info": "ℹ️", "warning": "⚠️", "note": "📝", "tip": "💡", "panel": "📋"}
        icon = icons.get(name, "📌")
        body_clean = re.sub(r'<[^>]+>', '', body).strip()
        lines = body_clean.split('\n')
        result = "\n"
        for i, line in enumerate(lines):
            if i == 0:
                result += f"> {icon} **{name.upper()}**: {line}\n"
            else:
                result += f"> {line}\n"
        return result

    md = re.sub(
        r'<ac:structured-macro[^>]*ac:name="(info|warning|note|tip|panel)"[^>]*>'
        r'(.*?)</ac:structured-macro>',
        macro_box, md, flags=re.S | re.I
    )

    # Código dentro de macros code
    def code_macro(m):
        lang_match = re.search(r'ac:name="([^"]+)"', m.group(1))
        lang = lang_match.group(1) if lang_match else ""
        body = re.search(r'<!\[CDATA\[(.*?)\]\]>', m.group(0), re.S)
        code_body = body.group(1) if body else re.sub(r'<[^>]+>', '', m.group(0))
        code_body = html_lib.unescape(code_body)
        lang = infer_lang(lang, code_body)
        return f"\n```{lang}\n{code_body.strip()}\n```\n"

    md = re.sub(
        r'<ac:structured-macro[^>]*ac:name="code"[^>]*>(.*?)</ac:structured-macro>',
        code_macro, md, flags=re.S | re.I
    )
    # Eliminar restantes macros estructuradas
    md = re.sub(r'<ac:structured-macro[^>]*>.*?</ac:structured-macro>', '', md, flags=re.S)
    md = re.sub(r'<ac:parameter[^>]*>.*?</ac:parameter>', '', md, flags=re.S)
    md = re.sub(
        r'<ac:plain-text-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-body>',
        lambda m2: f"\n```text\n{html_lib.unescape(m2.group(1)).strip()}\n```\n",
        md, flags=re.S
    )
    md = re.sub(r'<ac:rich-text-body[^>]*>(.*?)</ac:rich-text-body>', r'\1', md, flags=re.S)

    # Imágenes Confluence adjuntas
    md = re.sub(
        r'<ac:image[^>]*>\s*<ri:attachment\s+ri:filename="([^"]+)"[^/]*/?\s*></ac:image>',
        lambda m2: f"![{m2.group(1)}]({img_rel_path}/{m2.group(1)})",
        md, flags=re.S | re.I
    )
    md = re.sub(
        r'<ac:image[^>]*>.*?<ri:attachment\s+ri:filename="([^"]+)".*?</ac:image>',
        lambda m2: f"![{m2.group(1)}]({img_rel_path}/{m2.group(1)})",
        md, flags=re.S | re.I
    )
    # Imágenes externas
    md = re.sub(
        r'<ac:image[^>]*>.*?<ri:url\s+ri:value="([^"]+)".*?</ac:image>',
        lambda m2: f"![imagen]({m2.group(1)})",
        md, flags=re.S | re.I
    )

    # Links internos Confluence
    md = re.sub(
        r'<ac:link[^>]*>\s*<ri:page\s+ri:content-title="([^"]+)"[^/]*/?\s*>'
        r'(?:\s*<ac:plain-text-link-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-link-body>)?'
        r'\s*</ac:link>',
        lambda m2: f"[{m2.group(2) or m2.group(1)}]({m2.group(1).replace(' ', '_')}.md)",
        md, flags=re.S | re.I
    )
    md = re.sub(r'<ac:link[^>]*>.*?</ac:link>', '', md, flags=re.S)

    # ── Formato de texto ──────────────────────────────────────────────────
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>',           r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>',          r'_\1_',  md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>',            r'_\1_',  md, flags=re.S)
    md = re.sub(r'<u[^>]*>(.*?)</u>',            r'<u>\1</u>', md, flags=re.S)
    md = re.sub(r'<del[^>]*>(.*?)</del>',        r'~~\1~~', md, flags=re.S)
    md = re.sub(r'<s[^>]*>(.*?)</s>',            r'~~\1~~', md, flags=re.S)

    # ── Headings (shift +1 para que # sea el título del doc) ─────────────
    for n in range(6, 0, -1):
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>',
                    rf'\n{"#" * (n + 1)} \1\n', md, flags=re.S)

    # ── Código ────────────────────────────────────────────────────────────
    def fenced_code(m):
        lang = (m.group(1) or "").strip()
        body = html_lib.unescape(re.sub(r'<[^>]+>', '', m.group(2) or ""))
        lang = infer_lang(lang, body)
        return f"\n```{lang}\n{body.strip()}\n```\n"

    md = re.sub(
        r'<code[^>]*data-language="([^"]*)"[^>]*>(.*?)</code>',
        fenced_code, md, flags=re.S
    )
    md = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>',
                lambda m2: f"\n```{infer_lang('', html_lib.unescape(re.sub(r'<[^>]+>', '', m2.group(1))))}\n{html_lib.unescape(re.sub(r'<[^>]+>', '', m2.group(1))).strip()}\n```\n",
                md, flags=re.S)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>',
                lambda m2: f"\n```text\n{html_lib.unescape(re.sub(r'<[^>]+>', '', m2.group(1))).strip()}\n```\n",
                md, flags=re.S)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.S)

    # ── Links externos ────────────────────────────────────────────────────
    def replace_link(m):
        href = m.group(1)
        text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        # Link interno Confluence: /wiki/spaces/.../pages/<id>/...
        id_match = re.search(r'/wiki/spaces/[^/]+/pages/(\d+)', href)
        if id_match:
            pid = id_match.group(1)
            if pid in PAGE_ID_MAP:
                target_file = PAGE_ID_MAP[pid]
                rel = os.path.relpath(
                    os.path.join(FRONT_ROOT, target_file), out_dir
                ).replace("\\", "/")
                return f"[{text or target_file}]({rel})"
        return f"[{text or href}]({href})"

    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
                replace_link, md, flags=re.S)

    # ── Imágenes HTML estándar ─────────────────────────────────────────────
    # Convertir URLs de adjuntos Confluence a rutas locales img/
    def _img_src_to_local(src: str) -> str:
        att_match = re.search(r'/download/attachments/\d+/([^?&]+)', src)
        if att_match:
            return f"{img_rel_path}/{att_match.group(1)}"
        return src

    def _img_tag_full(m):
        alt = m.group(1) or ""
        src = _img_src_to_local(m.group(2))
        return f"![{alt}]({src})"

    def _img_tag_src_only(m):
        src = _img_src_to_local(m.group(1))
        fname = src.split("/")[-1]
        return f"![{fname}]({src})"

    md = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*/?>',
                _img_tag_full, md, flags=re.S)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',
                _img_tag_src_only, md, flags=re.S)

    # ── Listas ────────────────────────────────────────────────────────────
    md = re.sub(r'<ul[^>]*>', '\n', md)
    md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<ol[^>]*>', '\n', md)
    md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.S)

    # ── Tablas HTML → Markdown ─────────────────────────────────────────────
    def convert_table(tm):
        table_html = tm.group(0)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.S)
        if not rows:
            return ""
        result_rows = []
        header_cols = 0
        header_done = False
        for row in rows:
            cells_th = re.findall(r'<th[^>]*>(.*?)</th>', row, re.S)
            cells_td = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            cells = cells_th if cells_th else cells_td
            clean_cells = []
            for c in cells:
                clean = re.sub(r'<[^>]+>', '', c)
                clean = html_lib.unescape(clean).strip().replace('\n', ' ')
                clean_cells.append(clean)
            if not clean_cells:
                continue
            if not header_done:
                header_cols = len(clean_cells)
            # Pad row to header width
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

    # ── Tags restantes ────────────────────────────────────────────────────
    md = re.sub(r'<[^>]+>', '', md)

    # ── Entidades HTML ────────────────────────────────────────────────────
    md = html_lib.unescape(md)

    # ── Listas rotas: "-" solitario en su propia línea (MD032) ───────────
    md = re.sub(r'\n- *\n([^\n])', lambda m2: f"\n- {m2.group(1)}", md)

    # ── MD032 (b): non-list/non-blank → ítem de lista (insertar línea en blanco)
    _lp = re.compile(r'^[-*+]\s|\d+\.\s')
    _lines = md.split('\n')
    _out = []
    for _i, _ln in enumerate(_lines):
        _out.append(_ln)
        if _i < len(_lines) - 1:
            _nxt = _lines[_i + 1]
            if _ln.strip() and not _lp.match(_ln.strip()) and _lp.match(_nxt.strip()):
                _out.append('')
    md = '\n'.join(_out)

    # ── heading-order: normalizar jerarquía ──────────────────────────────
    # Si el body Confluence empieza en h3 (→ ####), ajustar a ## para no
    # saltar niveles debajo del # título que se prepone en process_node.
    # prev_level arranca en 1 (el # es el título del doc).
    _h_prev = 1
    _h_lines = []
    for _hl in md.split('\n'):
        _hm = re.match(r'^(#{1,6})(\s)', _hl)
        if _hm:
            _lvl = len(_hm.group(1))
            if _lvl > _h_prev + 1:
                _lvl = _h_prev + 1
                _hl = '#' * _lvl + _hm.group(2) + _hl[len(_hm.group(1)) + 1:]
            _h_prev = _lvl
        _h_lines.append(_hl)
    md = '\n'.join(_h_lines)

    # ── Limpiar espacios múltiples ────────────────────────────────────────
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = re.sub(r'\t', '    ', md)
    return md.strip()


def infer_lang(hint: str, body: str) -> str:
    if hint:
        return hint
    b = body.strip()
    if re.match(r'^\s*(package|import|@|public\s+class|public\s+interface)', b):
        return "java"
    if re.match(r'^\s*(spring:|azure:|server:|app:|logging:)', b):
        return "yaml"
    if re.match(r'^\s*[\[{]', b):
        return "json"
    if re.match(r'^\s*(dependencies\s*\{|plugins\s*\{|implementation)', b):
        return "groovy"
    if re.search(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE\s+TABLE)\b', b, re.I):
        return "sql"
    if re.match(r'^\s*(GET|POST|PUT|DELETE|PATCH)\s+/', b):
        return "http"
    return "text"


# ---------------------------------------------------------------------------
# Descargador binario
# ---------------------------------------------------------------------------
def download_binary(download_path: str, dest_file: str) -> bool:
    url = f"{BASE_URL}/wiki{download_path}"
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
# Adjuntos
# ---------------------------------------------------------------------------
MEDIA_MAP = {
    "application/pdf": PDF_DIR,
    "application/vnd.openxmlformats-officedocument.wordprocessingml": DOCX_DIR,
    "application/msword": DOCX_DIR,
    "application/vnd.openxmlformats-officedocument.spreadsheetml": XLSX_DIR,
    "application/vnd.ms-excel": XLSX_DIR,
    "image/": IMG_FRONT,
}


def get_body_storage(page_id: str) -> str:
    """Retorna el body en formato storage (para detectar adjuntos referenciados)."""
    url = f"{BASE_URL}/wiki/rest/api/content/{page_id}?expand=body.storage"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json().get("body", {}).get("storage", {}).get("value", "")


def process_attachments(page_id: str, out_dir: str, body_storage: str = "") -> list:
    """Descarga adjuntos referenciados en body_storage. Retorna links Markdown."""
    url = f"{BASE_URL}/wiki/rest/api/content/{page_id}/child/attachment?limit=100"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        atts = resp.json().get("results", [])
    except Exception as e:
        print(f"  [ERROR adjuntos {page_id}]: {e}")
        return []

    links = []
    for att in atts:
        filename   = att.get("title", "")
        media_type = att.get("metadata", {}).get("mediaType", "")  # v1 API nesting
        dl_path    = att.get("_links", {}).get("download", "")

        # Solo descargar si está referenciado en el cuerpo
        if body_storage and filename not in body_storage:
            print(f"  [HUÉRFANO ignorado] {filename}")
            continue

        dest_folder = None
        for prefix, folder in MEDIA_MAP.items():
            if media_type.startswith(prefix):
                dest_folder = folder
                break

        if not dest_folder:
            # JSON/otros → carpeta attachments junto al .md
            att_dir = os.path.join(out_dir, "attachments")
            os.makedirs(att_dir, exist_ok=True)
            dest_folder = att_dir

        os.makedirs(dest_folder, exist_ok=True)
        dest_file = os.path.join(dest_folder, filename)

        ok = True
        if not os.path.exists(dest_file):
            ok = download_binary(dl_path, dest_file)
            if ok:
                print(f"  [DESCARGADO] {filename}")
        else:
            print(f"  [YA EXISTE]  {filename}")

        if ok:
            rel = os.path.relpath(dest_file, out_dir).replace("\\", "/")
            if media_type.startswith("image/"):
                links.append(f"![{filename}]({rel})")
            else:
                links.append(f"- [{filename}]({rel})")

    return links


# ---------------------------------------------------------------------------
# Cuerpo de la página (v1 API con expand para author displayName)
# ---------------------------------------------------------------------------
def get_page_info(page_id: str) -> dict:
    """Retorna dict con title, body_view, version_num, author, when."""
    url = (f"{BASE_URL}/wiki/rest/api/content/{page_id}"
           f"?expand=version,body.view")
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    version = data.get("version", {})
    return {
        "title": data.get("title", ""),
        "body_view": data.get("body", {}).get("view", {}).get("value", ""),
        "version_num": version.get("number", ""),
        "author": version.get("by", {}).get("displayName", ""),
        "when": (version.get("when") or "")[:10],
    }


# ---------------------------------------------------------------------------
# Comentarios
# ---------------------------------------------------------------------------
def get_comments(page_id: str) -> list:
    """Retorna lista de dicts de comentarios footer (v1 API)."""
    url = (f"{BASE_URL}/wiki/rest/api/content/{page_id}/child/comment"
           f"?expand=body.view,version&limit=50")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.json().get("results", [])
    except Exception:
        return []


def render_comments(comments: list) -> str:
    if not comments:
        return ""
    out = "\n---\n\n## Comentarios de Confluence\n\n"
    for i, c in enumerate(comments, 1):
        version = c.get("version", {})
        author  = version.get("by", {}).get("displayName", "")
        when    = (version.get("when") or "")[:10]
        cid     = c.get("id", "")
        body_html = c.get("body", {}).get("view", {}).get("value", "")
        body_md   = html_to_md(body_html)
        out += f"### Comentario {i}\n\n"
        out += f"> **Autor:** {author}  \n"
        out += f"> **Fecha:** {when}  \n"
        out += f"> **ID comentario:** {cid}\n\n"
        out += body_md + "\n\n"
    return out


# ---------------------------------------------------------------------------
# Tabla de contenidos para páginas con hijos
# ---------------------------------------------------------------------------
def generate_toc(node: dict) -> str:
    if not node.get("children"):
        return ""
    toc = "## Contenido\n\n"
    for child in node["children"]:
        child_file = child["file"]
        child_dir  = os.path.dirname(child_file)
        child_base = os.path.basename(child_file)
        # Ruta relativa desde el directorio del nodo actual
        node_dir = os.path.dirname(node["file"])
        try:
            rel = os.path.relpath(
                os.path.join(FRONT_ROOT, child_file),
                os.path.join(FRONT_ROOT, node_dir)
            ).replace("\\", "/")
        except ValueError:
            rel = child_base
        toc += f"- [{child['title']}]({rel})\n"
        for gc in child.get("children", []):
            gc_file = gc["file"]
            try:
                rel_gc = os.path.relpath(
                    os.path.join(FRONT_ROOT, gc_file),
                    os.path.join(FRONT_ROOT, node_dir)
                ).replace("\\", "/")
            except ValueError:
                rel_gc = os.path.basename(gc_file)
            toc += f"  - [{gc['title']}]({rel_gc})\n"
    return toc + "\n"


# ---------------------------------------------------------------------------
# Procesamiento recursivo
# ---------------------------------------------------------------------------
results_log = []


def section_link(node_file: str) -> str:
    """Genera el link '**Sección:**' según posición del archivo."""
    parts = node_file.replace("\\", "/").split("/")
    if len(parts) == 1:
        # es index.md en la raíz de Front → no hay padre
        return "[Front](./index.md)"
    elif parts[-1] == "index.md":
        # es index.md en sub-carpeta → apunta al padre
        return "[Front](../index.md)"
    elif len(parts) == 2:
        # Página directamente en Front/
        return "[Front](./index.md)"
    else:
        # Página en sub-carpeta
        return f"[{parts[-2]}](./index.md)"


def process_node(node: dict) -> None:
    page_id  = node["id"]
    rel_file = node["file"]
    out_file = os.path.join(FRONT_ROOT, rel_file)
    out_dir  = os.path.dirname(out_file)
    os.makedirs(out_dir, exist_ok=True)

    # Ruta relativa de imágenes desde out_dir
    img_rel = os.path.relpath(IMG_FRONT, out_dir).replace("\\", "/")

    print(f"\n[{page_id}] {node['title']} → {rel_file}")

    try:
        info = get_page_info(page_id)
        body_storage = get_body_storage(page_id)
        att_links    = process_attachments(page_id, out_dir, body_storage)
        body_md      = html_to_md(info["body_view"], img_rel_path=img_rel, out_dir=out_dir)
        comments     = get_comments(page_id)

        # ── Cabecera obligatoria ──────────────────────────────────────────
        conf_url = f"{BASE_URL}/wiki/spaces/EPA/pages/{page_id}"
        content  = f"# {info['title']}\n\n"
        content += f"> **Fuente Confluence:** [{info['title']}]({conf_url})\n"
        content += f"> **Última modificación:** {info['when']} — {info['author']} · versión {info['version_num']}\n"
        content += f"> **Sección:** {section_link(rel_file)}\n\n"

        # ── TOC si tiene hijos ────────────────────────────────────────────
        toc = generate_toc(node)
        if toc:
            content += toc
            content += "---\n\n"

        # ── Adjuntos no imagen ────────────────────────────────────────────
        file_links = [l for l in att_links if not l.startswith("!")]
        if file_links:
            content += "## Archivos Adjuntos\n\n"
            content += "\n".join(file_links) + "\n\n---\n\n"

        # ── Cuerpo ────────────────────────────────────────────────────────
        content += body_md

        # ── Imágenes no incrustadas en el cuerpo ─────────────────────────
        img_links = [l for l in att_links if l.startswith("!")]
        if img_links and "![" not in body_md:
            content += "\n\n## Imágenes\n\n"
            content += "\n\n".join(img_links)

        # ── Comentarios ──────────────────────────────────────────────────
        content += render_comments(comments)

        # ── Trailing newline ──────────────────────────────────────────────
        if not content.endswith("\n"):
            content += "\n"

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)
        size = os.path.getsize(out_file)
        print(f"  [OK] {size} bytes → {out_file}")
        results_log.append({"id": page_id, "title": info["title"], "file": rel_file, "ok": True, "bytes": size})

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"  [ERROR] {e}")
        results_log.append({"id": page_id, "title": node["title"], "file": rel_file, "ok": False, "error": str(e)})

    for child in node.get("children", []):
        process_node(child)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Descargando sección 'Front' de Confluence")
    print(f"Destino: {FRONT_ROOT}")
    print(f"Fecha:   {TODAY}")
    print("=" * 60)

    process_node(PAGE_TREE)

    ok  = sum(1 for r in results_log if r["ok"])
    err = sum(1 for r in results_log if not r["ok"])

    print("\n" + "=" * 60)
    print(f"RESUMEN: {ok} páginas OK, {err} errores")
    print("=" * 60)
    print("\n=== Archivos generados ===")
    for r in results_log:
        status = "OK" if r["ok"] else "ERROR"
        extra  = f"{r.get('bytes', 0):,} bytes" if r["ok"] else r.get("error", "")
        print(f"  [{status}] {r['file']}  ({extra})")


if __name__ == "__main__":
    main()
