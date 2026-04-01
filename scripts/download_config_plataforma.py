#!/usr/bin/env python3
"""
download_config_plataforma.py
Genera la documentación local de "Configuración Plataforma Base Sarlaft"
extrayendo contenido de Confluence (espacio EPA).

Páginas:
  [2389114940] Configuración Plataforma Base Sarlaft  (raíz)
  [2388918331] Instalación del Agente Dynatrace en AKS Sarlaft
  [1880817708] Instalación RabbitMQ en AKS Sarlaft

Output: D:\\Sarlaft 4.0\\docs\\ConfiguracionPlataformaBase\\
"""
import html as html_lib
import re
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from confluence_config import BASE_URL, HEADERS, DL_HEADERS, DOCS_ROOT

# ─── Rutas ────────────────────────────────────────────────────────────────────
BASE_DIR   = Path(DOCS_ROOT) / "ConfiguracionPlataformaBase"
IMG_DIR    = BASE_DIR / "img"
ATT_DIR    = BASE_DIR / "attachments"
PDF_ROOT   = Path(DOCS_ROOT) / "pdf"
DOCX_ROOT  = Path(DOCS_ROOT) / "docx"
XLSX_ROOT  = Path(DOCS_ROOT) / "xlsx"

# Solo crear carpetas propias de la sección; pdf/docx/xlsx se crean bajo demanda
# dentro de download_bin → dest.parent.mkdir(parents=True, exist_ok=True)
BASE_DIR.mkdir(parents=True, exist_ok=True)

ROOT_ID     = "2389114940"
DYNATRACE_ID = "2388918331"
RABBITMQ_ID  = "1880817708"

SECTION     = "Configuración Plataforma Base Sarlaft"
BASE_WEBUI  = f"{BASE_URL}/wiki/spaces/EPA/pages"

# ─── API helpers ──────────────────────────────────────────────────────────────
def api_get(path: str, **params) -> dict:
    r = requests.get(f"{BASE_URL}/wiki{path}", headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def get_page(pid: str) -> dict:
    return api_get(
        f"/rest/api/content/{pid}",
        expand="body.storage,version,ancestors,space",
    )


def get_comments(pid: str) -> list:
    try:
        return api_get(
            f"/rest/api/content/{pid}/child/comment",
            depth="all", expand="body.storage,version", limit=50,
        ).get("results", [])
    except Exception as exc:
        print(f"  [WARN] Comentarios {pid}: {exc}")
        return []


def get_attachments_api(pid: str) -> list:
    try:
        return api_get(
            f"/rest/api/content/{pid}/child/attachment",
            limit=100, expand="version",
        ).get("results", [])
    except Exception as exc:
        print(f"  [WARN] Adjuntos {pid}: {exc}")
        return []


def download_bin(dl_path: str, dest: Path) -> bool:
    url = dl_path if dl_path.startswith("http") else (
        BASE_URL + dl_path if dl_path.startswith("/wiki")
        else BASE_URL + "/wiki" + dl_path
    )
    try:
        r = requests.get(url, headers=DL_HEADERS, stream=True, timeout=60)
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        return True
    except Exception as exc:
        print(f"  [ERR DL] {dest.name}: {exc}")
        return False


# ─── Detectar adjuntos referenciados en el body (storage format) ──────────────
def find_referenced_attachments(body: str) -> set:
    """Extrae nombres de archivo referenciados via ac:image / ri:attachment / view-file."""
    refs = set()
    # ac:image y view-file → ri:attachment ri:filename="..."
    for m in re.finditer(r'ri:filename="([^"]+)"', body):
        refs.add(m.group(1))
    return refs


# ─── Conversión Storage HTML → Markdown ──────────────────────────────────────
def _convert_table(m: re.Match) -> str:
    table_html = m.group(0)
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", table_html, re.S)
    if not rows:
        return ""
    md_rows = []
    header_cols = 0
    for i, row in enumerate(rows):
        th = re.findall(r"<th[^>]*>(.*?)</th>", row, re.S)
        td = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
        cells = th if th else td
        clean = [
            re.sub(r"<[^>]+>", "", html_lib.unescape(c))
            .strip().replace("\n", " ").replace("|", "\\|")
            for c in cells
        ]
        if not clean:
            continue
        if i == 0:
            header_cols = len(clean)
        else:
            # MD056: uniformar columnas
            while len(clean) < header_cols:
                clean.append("")
            clean = clean[:header_cols]
        md_rows.append("| " + " | ".join(clean) + " |")
        if i == 0:
            md_rows.append("| " + " | ".join(["---"] * len(clean)) + " |")
    return "\n" + "\n".join(md_rows) + "\n" if md_rows else ""


def _infer_lang(code: str) -> str:
    code = code.strip()
    if re.search(r'\bpackage\b|\bimport\b|\bpublic class\b|@Bean', code):
        return "java"
    if re.search(r'^(spring:|azure:|server:|management:)', code, re.M):
        return "yaml"
    if code.lstrip().startswith("{") or code.lstrip().startswith("["):
        return "json"
    if re.search(r'\bimplementation\b|\bdependencies\s*\{', code):
        return "groovy"
    if re.search(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE TABLE)\b', code, re.I):
        return "sql"
    if re.search(r'^(apiVersion:|kind:|metadata:|spec:)', code, re.M):
        return "yaml"
    if re.search(r'^(az |kubectl )', code, re.M):
        return "shell"
    return "text"


def storage_to_md(raw: str, img_dir_rel: str = "./img", att_dir_rel: str = "./attachments") -> str:
    """Convierte Confluence storage format a Markdown."""
    if not raw:
        return ""
    md = raw

    # ── Macros Confluence (ANTES de procesar HTML genérico) ──────────────────

    # 1. ac:image → ![filename](./img/filename)
    def _ac_image(m: re.Match) -> str:
        inner = m.group(1)
        fn_m = re.search(r'ri:filename="([^"]+)"', inner)
        fname = fn_m.group(1) if fn_m else "imagen"
        return f"\n![{fname}]({img_dir_rel}/{fname})\n"
    md = re.sub(r"<ac:image[^>]*>(.*?)</ac:image>", _ac_image, md, flags=re.S)

    # 2. view-file macro → [filename](./attachments/filename)
    def _view_file(m: re.Match) -> str:
        inner = m.group(1)
        fn_m = re.search(r'ri:filename="([^"]+)"', inner)
        fname = fn_m.group(1) if fn_m else "attachment"
        return f"\n[{fname}]({att_dir_rel}/{fname})\n"
    md = re.sub(
        r'<ac:structured-macro ac:name="view-file"[^>]*>(.*?)</ac:structured-macro>',
        _view_file, md, flags=re.S,
    )

    # 3. Eliminar otras macros de Confluence que no aportan contenido
    md = re.sub(r"<ac:[^>]+/>", "", md, flags=re.S)
    md = re.sub(r"<ac:parameter[^>]*>.*?</ac:parameter>", "", md, flags=re.S)
    md = re.sub(r"<ac:[^>]*>.*?</ac:[^>]*>", "", md, flags=re.S)
    md = re.sub(r"<ri:[^>]+/>", "", md, flags=re.S)

    # ── Tablas ────────────────────────────────────────────────────────────────
    md = re.sub(r"<table[^>]*>.*?</table>", _convert_table, md, flags=re.S)

    # ── Negritas / itálicas ───────────────────────────────────────────────────
    md = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", md, flags=re.S)
    md = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", md, flags=re.S)
    md = re.sub(r"<em[^>]*>(.*?)</em>", r"_\1_", md, flags=re.S)
    md = re.sub(r"<i[^>]*>(.*?)</i>", r"_\1_", md, flags=re.S)
    md = re.sub(r"<u[^>]*>(.*?)</u>", r"**\1**", md, flags=re.S)

    # ── Headings ─────────────────────────────────────────────────────────────
    for n in range(6, 0, -1):
        level = min(n + 1, 6)
        md = re.sub(
            rf"<h{n}[^>]*>(.*?)</h{n}>",
            lambda m, lv=level: f"\n{'#' * lv} {re.sub(r'<[^>]+>', '', m.group(1)).strip()}\n",
            md, flags=re.S,
        )

    # ── Código inline ─────────────────────────────────────────────────────────
    md = re.sub(r"<code[^>]*>(.*?)</code>", lambda m: f"`{html_lib.unescape(re.sub(r'<[^>]+>', '', m.group(1)))}`", md, flags=re.S)

    # ── Bloques pre ──────────────────────────────────────────────────────────
    def _pre(m: re.Match) -> str:
        code = html_lib.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        lang = _infer_lang(code)
        return f"\n```{lang}\n{code}\n```\n"
    md = re.sub(r"<pre[^>]*>(.*?)</pre>", _pre, md, flags=re.S)

    # ── Links ─────────────────────────────────────────────────────────────────
    def _link(m: re.Match) -> str:
        href = m.group(1)
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        # MD034: URLs ya están en [text](href) → OK
        return f"[{text or href}]({href})"
    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', _link, md, flags=re.S)

    # ── Listas ────────────────────────────────────────────────────────────────
    # Listas ordenadas: convertir <li> dentro de <ol>
    def _ol_block(m: re.Match) -> str:
        inner = m.group(1)
        items = re.findall(r"<li[^>]*>(.*?)</li>", inner, re.S)
        lines = []
        for idx, it in enumerate(items, 1):
            text = re.sub(r"<[^>]+>", " ", it).strip()
            text = html_lib.unescape(re.sub(r"\s+", " ", text))
            lines.append(f"{idx}. {text}")
        return "\n\n" + "\n".join(lines) + "\n\n"

    def _ul_block(m: re.Match) -> str:
        inner = m.group(1)
        items = re.findall(r"<li[^>]*>(.*?)</li>", inner, re.S)
        lines = []
        for it in items:
            text = re.sub(r"<[^>]+>", " ", it).strip()
            text = html_lib.unescape(re.sub(r"\s+", " ", text))
            lines.append(f"- {text}")
        return "\n\n" + "\n".join(lines) + "\n\n"

    md = re.sub(r"<ol[^>]*>(.*?)</ol>", _ol_block, md, flags=re.S)
    md = re.sub(r"<ul[^>]*>(.*?)</ul>", _ul_block, md, flags=re.S)

    # ── Párrafos / saltos / divs ──────────────────────────────────────────────
    md = re.sub(r"<p[^>]*/?>", "\n", md)
    md = re.sub(r"</p>", "\n", md)
    md = re.sub(r"<br\s*/?>", "\n", md)
    md = re.sub(r"<hr\s*/?>", "\n---\n", md)
    md = re.sub(r"<div[^>]*>", "", md)
    md = re.sub(r"</div>", "\n", md)
    md = re.sub(r"<span[^>]*>", "", md)
    md = re.sub(r"</span>", "", md)

    # ── Eliminar tags restantes ───────────────────────────────────────────────
    md = re.sub(r"<[^>]+>", "", md)

    # ── Entidades HTML ────────────────────────────────────────────────────────
    md = html_lib.unescape(md)

    # ── MD010: tabs → espacios ────────────────────────────────────────────────
    md = md.replace("\t", "    ")

    # ── MD012: máximo 1 línea en blanco consecutiva ───────────────────────────
    md = re.sub(r"\n{3,}", "\n\n", md)

    # ── MD009: quitar espacios finales (excepto 2 espacios intencionales) ─────
    md = re.sub(r" +$", "", md, flags=re.M)

    # ── MD032: ítems de lista rotos (guion solo en su línea) ──────────────────
    md = re.sub(r"\n-\s*\n([^\n])", lambda m2: f"\n- {m2.group(1)}", md)

    # ── heading-order ─────────────────────────────────────────────────────────
    _h_prev = 1
    _h_out = []
    for _hl in md.split("\n"):
        _hm = re.match(r"^(#{1,6})(\s)", _hl)
        if _hm:
            _lvl = len(_hm.group(1))
            if _lvl > _h_prev + 1:
                _lvl = _h_prev + 1
                _hl = "#" * _lvl + _hm.group(2) + _hl[len(_hm.group(1)) + 1:]
            _h_prev = _lvl
        _h_out.append(_hl)
    md = "\n".join(_h_out)

    return md.strip()


# ─── Descarga de adjuntos referenciados ──────────────────────────────────────
def download_referenced(pid: str, body: str) -> dict:
    """Descarga solo adjuntos referenciados en el body. Retorna {fname: rel_path}."""
    refs = find_referenced_attachments(body)
    atts = get_attachments_api(pid)
    att_map = {}

    for att in atts:
        fname = att.get("title", "")
        dl    = att.get("_links", {}).get("download", "")
        if fname not in refs or not dl:
            if fname not in refs:
                print(f"  [SKIP orphan] {fname}")
            continue

        ext = Path(fname).suffix.lower()
        if ext in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            dest = IMG_DIR / fname
            rel  = f"./img/{fname}"
        elif ext in {".yaml", ".yml", ".json", ".xml"}:
            dest = ATT_DIR / fname
            rel  = f"./attachments/{fname}"
        elif ext == ".pdf":
            dest = PDF_ROOT / fname
            rel  = f"../pdf/{fname}"
        elif ext in {".docx", ".doc"}:
            dest = DOCX_ROOT / fname
            rel  = f"../docx/{fname}"
        elif ext in {".xlsx", ".xls"}:
            dest = XLSX_ROOT / fname
            rel  = f"../xlsx/{fname}"
        else:
            dest = ATT_DIR / fname
            rel  = f"./attachments/{fname}"

        if dest.exists():
            print(f"  [EXISTS] {fname}")
        else:
            ok = download_bin(dl, dest)
            if not ok:
                continue
            print(f"  [DL] {fname} → {dest}")
        att_map[fname] = rel

    return att_map


# ─── Construir header del .md ─────────────────────────────────────────────────
def md_header(title: str, web_path: str, date: str, author: str, ver: int, section_link: str) -> str:
    url = f"{BASE_URL}/wiki{web_path}"
    return (
        f"# {title}\n\n"
        f"> **Fuente Confluence:** [{title}]({url})  \n"
        f"> **Última modificación:** {date} — {author} · versión {ver}  \n"
        f"> **Sección:** [{SECTION}]({section_link})\n\n"
    )


# ─── Generar index.md (página raíz) ──────────────────────────────────────────
def generate_index(root: dict, children: list[tuple[str, str, str, int]]) -> str:
    """
    root: datos de la página raíz
    children: [(title, filename, date, ver), ...]
    """
    title  = root["title"]
    ver    = root["version"]["number"]
    author = root["version"]["by"]["displayName"]
    date   = (root["version"]["when"] or "")[:10]
    webui  = root["_links"]["webui"]

    header = md_header(title, webui, date, author, ver, "./index.md")

    rows = []
    for c_title, c_file, c_date, c_ver in children:
        rows.append(f"| [{c_title}](./{c_file}) | {c_date} | {c_ver} |")

    table = (
        "## Páginas\n\n"
        "| Página | Última modificación | Versión |\n"
        "|--------|--------------------|---------|\n"
        + "\n".join(rows)
        + "\n"
    )

    return header + table + "\n"


# ─── Procesar página de contenido ────────────────────────────────────────────
def process_page(pid: str, md_filename: str, section_link: str = "./index.md") -> None:
    print(f"\n[PROC] {pid} → {md_filename}")
    p    = get_page(pid)
    body = p["body"]["storage"]["value"]
    title  = p["title"]
    ver    = p["version"]["number"]
    author = p["version"]["by"]["displayName"]
    date   = (p["version"]["when"] or "")[:10]
    webui  = p["_links"]["webui"]

    att_map = download_referenced(pid, body)

    body_md = storage_to_md(body)

    # Reemplazar referencias de imagen (ya incluidas en storage_to_md) por att_map si existe
    # (por si hubo colisión de nombre)

    header = md_header(title, webui, date, author, ver, section_link)
    content = header + body_md + "\n"

    # MD047: newline al final
    if not content.endswith("\n"):
        content += "\n"

    out = BASE_DIR / md_filename
    out.write_text(content, encoding="utf-8")
    print(f"  [WRITE] {out} ({len(content)} chars)")
    return p


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("Configuración Plataforma Base Sarlaft — generando docs")
    print("=" * 60)

    # 1) Raíz
    print("\n[1/3] Página raíz (índice)")
    root = get_page(ROOT_ID)

    # 2) Sub-páginas
    children_info = []
    for pid, fname in [
        (DYNATRACE_ID, "InstalacionAgenteDynatraceEnAKSSarlaft.md"),
        (RABBITMQ_ID,  "InstalacionRabbitMQEnAKSSarlaft.md"),
    ]:
        print(f"\n[PROC] {pid} → {fname}")
        p    = get_page(pid)
        body = p["body"]["storage"]["value"]
        title  = p["title"]
        ver    = p["version"]["number"]
        author = p["version"]["by"]["displayName"]
        date   = (p["version"]["when"] or "")[:10]
        webui  = p["_links"]["webui"]

        att_map = download_referenced(pid, body)
        body_md = storage_to_md(body)

        header = md_header(title, webui, date, author, ver, "./index.md")
        content = header + body_md + "\n"
        if not content.endswith("\n"):
            content += "\n"

        out = BASE_DIR / fname
        out.write_text(content, encoding="utf-8")
        print(f"  [WRITE] {out} ({len(content)} chars)")

        children_info.append((title, fname, date, ver))

    # 3) index.md
    print("\n[3/3] Generando index.md")
    index_content = generate_index(root, children_info)
    if not index_content.endswith("\n"):
        index_content += "\n"
    idx = BASE_DIR / "index.md"
    idx.write_text(index_content, encoding="utf-8")
    print(f"  [WRITE] {idx} ({len(index_content)} chars)")

    # 4) Resumen
    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)
    files = list(BASE_DIR.rglob("*"))
    md_files = [f for f in files if f.is_file() and f.suffix == ".md"]
    bin_files = [f for f in files if f.is_file() and f.suffix != ".md"]
    print(f"  Páginas procesadas : 3")
    print(f"  Archivos .md       : {len(md_files)}")
    print(f"  Adjuntos           : {len(bin_files)}")
    for f in sorted(files):
        if f.is_file():
            rel = f.relative_to(BASE_DIR)
            print(f"    {rel}  ({f.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
