"""
download_peps.py — Descarga y documenta la sección 'Microservicio PEPS' de Confluence.

Jerarquía Confluence:
  Sarlaft 4.0 → Documentación Técnica → Microservicio PEPS [1804861539]
    ├── Diseño y Arquitectura PEPS MS [1800700343]
    │     └── Configuración base de datos en producción [4516380673]
    ├── Configuración Ambiente - PEPSMS [1801126290]
    ├── Estructura Proyecto - PEPSMS [1809908172]
    └── Servicios Web - PepsMS [1804927095]
          ├── Servicio Marcar Cliente PEPS [1814200586]
          └── Servicio Consulta PEPS [1813971266]

Salida local:
  docs/MicroservicioPEPS/
    ├── index.md
    ├── DisenoArquitecturaPEPS/
    │     ├── index.md
    │     └── ConfiguracionBDProduccion.md
    ├── ConfiguracionAmbiente_PEPSMS.md
    ├── EstructuraProyecto_PEPSMS.md
    └── ServiciosWeb_PepsMS/
          ├── index.md
          ├── ServicioMarcarClientePEPS.md
          └── ServicioConsultaPEPS.md
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
PEPS_ROOT = os.path.join(DOCS_ROOT, "MicroservicioPEPS")
TODAY = date.today().strftime("%Y-%m-%d")

# Carpeta para imágenes dentro de MicroservicioPEPS
IMG_PEPS = os.path.join(PEPS_ROOT, "imagenes")

# Carpetas compartidas de adjuntos (igual que los otros scripts)
PDF_DIR  = os.path.join(DOCS_ROOT, "pdf")
DOCX_DIR = os.path.join(DOCS_ROOT, "docx")
XLSX_DIR = os.path.join(DOCS_ROOT, "xlsx")

for folder in [PEPS_ROOT, IMG_PEPS]:
    os.makedirs(folder, exist_ok=True)

# ---------------------------------------------------------------------------
# Jerarquía de páginas: (page_id, output_path_relative_to_PEPS_ROOT, is_section_root)
# is_section_root=True → genera index.md con hijos, False → genera archivo individual
# ---------------------------------------------------------------------------
PAGE_TREE = {
    "id": "1804861539",
    "title": "Microservicio PEPS",
    "file": "index.md",   # relative to PEPS_ROOT
    "children": [
        {
            "id": "1800700343",
            "title": "Diseño y Arquitectura PEPS MS",
            "file": "DisenoArquitecturaPEPS/index.md",
            "children": [
                {
                    "id": "4516380673",
                    "title": "Configuración base de datos en producción",
                    "file": "DisenoArquitecturaPEPS/ConfiguracionBDProduccion.md",
                    "children": []
                }
            ]
        },
        {
            "id": "1801126290",
            "title": "Configuración Ambiente - PEPSMS",
            "file": "ConfiguracionAmbiente_PEPSMS.md",
            "children": []
        },
        {
            "id": "1809908172",
            "title": "Estructura Proyecto - PEPSMS",
            "file": "EstructuraProyecto_PEPSMS.md",
            "children": []
        },
        {
            "id": "1804927095",
            "title": "Servicios Web - PepsMS",
            "file": "ServiciosWeb_PepsMS/index.md",
            "children": [
                {
                    "id": "1814200586",
                    "title": "Servicio Marcar Cliente PEPS",
                    "file": "ServiciosWeb_PepsMS/ServicioMarcarClientePEPS.md",
                    "children": []
                },
                {
                    "id": "1813971266",
                    "title": "Servicio Consulta PEPS",
                    "file": "ServiciosWeb_PepsMS/ServicioConsultaPEPS.md",
                    "children": []
                }
            ]
        }
    ]
}


# ---------------------------------------------------------------------------
# HTML → Markdown (mejorado con soporte para macros Confluence)
# ---------------------------------------------------------------------------
def html_to_md(raw: str, page_id: str = "") -> str:
    if not raw:
        return ""
    md = raw

    # ── Macros de Confluence ──────────────────────────────────────────────
    # ac:structured-macro: info / warning / note / tip → blockquotes
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
    # Eliminar otras macros Confluence no procesadas
    md = re.sub(r'<ac:structured-macro[^>]*>.*?</ac:structured-macro>', '', md, flags=re.S)
    md = re.sub(r'<ac:parameter[^>]*>.*?</ac:parameter>', '', md, flags=re.S)
    md = re.sub(r'<ac:plain-text-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-body>',
                r'\n```\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<ac:rich-text-body[^>]*>(.*?)</ac:rich-text-body>',
                r'\1', md, flags=re.S)

    # Imágenes Confluence (adjuntos de la página)
    md = re.sub(
        r'<ac:image[^>]*>\s*<ri:attachment\s+ri:filename="([^"]+)"[^/]*/?\s*></ac:image>',
        lambda m: f"![{m.group(1)}](imagenes/{m.group(1)})",
        md, flags=re.S | re.I
    )
    md = re.sub(
        r'<ac:image[^>]*>.*?<ri:attachment\s+ri:filename="([^"]+)".*?</ac:image>',
        lambda m: f"![{m.group(1)}](imagenes/{m.group(1)})",
        md, flags=re.S | re.I
    )

    # Links Confluence internos → referencias relativas placeholder
    md = re.sub(
        r'<ac:link[^>]*>\s*<ri:page\s+ri:content-title="([^"]+)"[^/]*/?\s*>'
        r'(?:\s*<ac:plain-text-link-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-link-body>)?'
        r'\s*</ac:link>',
        lambda m: f"[{m.group(2) or m.group(1)}]({m.group(1).replace(' ', '_')}.md)",
        md, flags=re.S | re.I
    )
    md = re.sub(r'<ac:link[^>]*>.*?</ac:link>', '', md, flags=re.S)

    # ── Formato de texto ─────────────────────────────────────────────────
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>',           r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>',          r'_\1_',  md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>',            r'_\1_',  md, flags=re.S)
    md = re.sub(r'<u[^>]*>(.*?)</u>',            r'<u>\1</u>', md, flags=re.S)
    md = re.sub(r'<del[^>]*>(.*?)</del>',        r'~~\1~~', md, flags=re.S)
    md = re.sub(r'<s[^>]*>(.*?)</s>',            r'~~\1~~', md, flags=re.S)

    # ── Headings ─────────────────────────────────────────────────────────
    for n in range(1, 7):
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>',
                    rf'\n{"#" * (n + 1)} \1\n', md, flags=re.S)

    # ── Código ───────────────────────────────────────────────────────────
    # Bloques de código con lenguaje
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
        for i, row in enumerate(rows):
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
            # Insert separator after first row (header)
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
# Descarga un archivo binario
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
# Procesa adjuntos de una página
# ---------------------------------------------------------------------------
MEDIA_MAP = {
    "application/pdf": (PDF_DIR, "../../pdf"),
    "application/vnd.openxmlformats-officedocument.wordprocessingml": (DOCX_DIR, "../../docx"),
    "application/msword": (DOCX_DIR, "../../docx"),
    "application/vnd.openxmlformats-officedocument.spreadsheetml": (XLSX_DIR, "../../xlsx"),
    "application/vnd.ms-excel": (XLSX_DIR, "../../xlsx"),
    "image/jpeg":    (IMG_PEPS, "imagenes"),
    "image/png":     (IMG_PEPS, "imagenes"),
    "image/gif":     (IMG_PEPS, "imagenes"),
    "image/svg+xml": (IMG_PEPS, "imagenes"),
    "image/webp":    (IMG_PEPS, "imagenes"),
}


def process_attachments(page_id: str, out_dir: str) -> list:
    """
    Descarga adjuntos de la página.
    out_dir: directorio donde está el .md de esta página (para calcular ruta relativa correcta).
    Devuelve lista de strings markdown con links a cada adjunto.
    """
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/attachments?limit=100"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        atts = resp.json().get("results", [])
    except Exception as e:
        print(f"  [ERROR adjuntos {page_id}]: {e}")
        return []

    links = []
    for att in atts:
        media_type = att.get("mediaType", "")
        filename   = att.get("title", "")
        dl_path    = att.get("_links", {}).get("download", "")

        dest_folder = rel_folder = None
        for prefix, (folder, rel) in MEDIA_MAP.items():
            if media_type.startswith(prefix):
                dest_folder, rel_folder = folder, rel
                break

        if not dest_folder:
            print(f"  [IGNORADO] {filename} ({media_type})")
            continue

        # Para imágenes, las copiamos también al directorio de la página
        if media_type.startswith("image/"):
            # Guardar en imagenes/ de PEPS_ROOT y usar ruta relativa desde out_dir
            dest_file = os.path.join(IMG_PEPS, filename)
            # Calcular ruta relativa del out_dir a imagenes/
            rel_from_page = os.path.relpath(IMG_PEPS, out_dir).replace("\\", "/")
            ref = f"{rel_from_page}/{filename}"
        else:
            dest_file = os.path.join(dest_folder, filename)
            # Calcular ruta relativa desde out_dir a la carpeta de adjuntos
            rel_from_page = os.path.relpath(dest_folder, out_dir).replace("\\", "/")
            ref = f"{rel_from_page}/{filename}"

        ok = True
        if not os.path.exists(dest_file):
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            ok = download_binary(dl_path, dest_file)
            if ok:
                print(f"  [DESCARGADO] {filename}")
        else:
            print(f"  [YA EXISTE]  {filename}")

        if ok:
            if media_type.startswith("image/"):
                links.append(f"![{filename}]({ref})")
            else:
                links.append(f"- [{filename}]({ref})")

    return links


# ---------------------------------------------------------------------------
# Obtiene el cuerpo HTML de una página (view format)
# ---------------------------------------------------------------------------
def get_page_body(page_id: str) -> tuple:
    """Retorna (title, body_html)"""
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}?body-format=view"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    title = data.get("title", "")
    body_html = data.get("body", {}).get("view", {}).get("value", "")
    return title, body_html


# ---------------------------------------------------------------------------
# Genera una tabla de contenidos para páginas con hijos (index.md)
# ---------------------------------------------------------------------------
def generate_toc(node: dict) -> str:
    toc = "## Contenido\n\n"
    for child in node.get("children", []):
        child_file = os.path.basename(child["file"])
        # Si el hijo es un index.md de sub-carpeta
        if child_file == "index.md":
            child_dir = os.path.dirname(child["file"])
            # La ruta relativa desde la carpeta padre
            rel = os.path.join(os.path.basename(child_dir), "index.md").replace("\\", "/")
        else:
            rel = child_file
        toc += f"- [{child['title']}]({rel})\n"
        # Sub-hijos
        for grandchild in child.get("children", []):
            sub_file = grandchild["file"]
            grandchild_base = os.path.basename(sub_file)
            child_dir_base = os.path.basename(os.path.dirname(child["file"])) or ""
            if child_dir_base and child_file == "index.md":
                rel_sub = f"{child_dir_base}/{grandchild_base}"
            else:
                rel_sub = grandchild_base
            toc += f"  - [{grandchild['title']}]({rel_sub})\n"
    return toc


# ---------------------------------------------------------------------------
# Procesamiento recursivo de una página
# ---------------------------------------------------------------------------
results_log = []


def process_node(node: dict, parent_out_dir: str = None) -> None:
    page_id = node["id"]
    rel_file = node["file"]
    has_children = bool(node.get("children"))

    # Ruta completa del archivo de salida
    out_file = os.path.join(PEPS_ROOT, rel_file)
    out_dir  = os.path.dirname(out_file)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n[{page_id}] {node['title']} → {rel_file}")

    try:
        title, body_html = get_page_body(page_id)
        body_md = html_to_md(body_html, page_id)
        att_links = process_attachments(page_id, out_dir)

        # Construir encabezado del .md
        content = f"# {title}\n\n"
        content += f"> **Fuente Confluence:** [{BASE_URL}/wiki/spaces/EPA/pages/{page_id}]"
        content += f"({BASE_URL}/wiki/spaces/EPA/pages/{page_id})\n"
        content += f"> **Fecha extracción:** {TODAY}\n\n"

        # Si es página con hijos, añadir tabla de contenidos primero
        if has_children:
            content += generate_toc(node)
            content += "\n---\n\n"

        # Separar imágenes del resto de adjuntos para el cuerpo
        img_links = [l for l in att_links if l.startswith("!")]
        file_links = [l for l in att_links if not l.startswith("!")]

        if file_links:
            content += "## Archivos Adjuntos\n\n"
            content += "\n".join(file_links) + "\n\n---\n\n"

        content += body_md

        # Añadir imágenes al final si no están ya en el cuerpo
        if img_links:
            has_inline_images = "![" in body_md
            if not has_inline_images:
                content += "\n\n## Imágenes\n\n"
                content += "\n\n".join(img_links) + "\n"

        # Escribir archivo
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] → {out_file}")
        results_log.append({"id": page_id, "title": title, "file": rel_file, "ok": True})

    except Exception as e:
        print(f"  [ERROR] {page_id}: {e}")
        import traceback
        traceback.print_exc()
        results_log.append({"id": page_id, "title": node["title"], "file": rel_file, "ok": False, "error": str(e)})

    # Procesar hijos recursivamente
    for child in node.get("children", []):
        process_node(child, out_dir)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Descargando sección 'Microservicio PEPS' de Confluence")
    print(f"Destino: {PEPS_ROOT}")
    print(f"Fecha:   {TODAY}")
    print("=" * 60)

    process_node(PAGE_TREE)

    # ── Generar resumen ──────────────────────────────────────────────────
    ok_count  = sum(1 for r in results_log if r["ok"])
    err_count = sum(1 for r in results_log if not r["ok"])

    print("\n" + "=" * 60)
    print(f"RESUMEN: {ok_count} páginas OK, {err_count} errores")
    print("=" * 60)

    # ── Verificación recursiva de archivos generados ──────────────────────
    print("\n=== Archivos generados ===")
    for root, dirs, files in os.walk(PEPS_ROOT):
        level = root.replace(PEPS_ROOT, "").count(os.sep)
        indent = "  " * level
        rel_root = os.path.relpath(root, PEPS_ROOT)
        print(f"{indent}{rel_root}/")
        sub_indent = "  " * (level + 1)
        for f in sorted(files):
            print(f"{sub_indent}{f}")

    if err_count > 0:
        print("\n=== Errores ===")
        for r in results_log:
            if not r["ok"]:
                print(f"  [{r['id']}] {r['title']}: {r.get('error', '?')}")


if __name__ == "__main__":
    main()
