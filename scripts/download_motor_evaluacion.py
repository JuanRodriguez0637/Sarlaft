#!/usr/bin/env python3
"""
download_motor_evaluacion.py
Descarga y documenta TODAS las secciones bajo "Motor de Evaluación" de Confluence.

Espacio : EPA
Página raíz: Motor de Evaluación (ID: 1809941005)
Output  : D:\\Sarlaft 4.0\\docs\\Motor de Evaluación\\
"""

import os
import re
import sys
import html as html_lib
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

import requests

sys.path.insert(0, str(Path(__file__).parent))
from confluence_config import BASE_URL, HEADERS, DL_HEADERS, DOCS_ROOT

# ─── Rutas base ───────────────────────────────────────────────────────────────
MOTOR_ROOT = Path(DOCS_ROOT) / "Motor de Evaluación"
PDF_ROOT   = Path(DOCS_ROOT) / "pdf"
DOCX_ROOT  = Path(DOCS_ROOT) / "docx"
XLSX_ROOT  = Path(DOCS_ROOT) / "xlsx"

# pdf/docx/xlsx se crean bajo demanda en download_bin → dest.parent.mkdir
MOTOR_ROOT.mkdir(parents=True, exist_ok=True)

# ─── Secciones (hijas directas de Motor de Evaluación 1809941005) ─────────────
SECTIONS = [
    ("1810203073", "Diseño - Motor Evaluación"),
    ("1809941012", "Configuración Ambiente - Motor Evaluación"),
    ("1809941019", "Estructura Proyecto - Motor Evaluación"),
    ("2365718886", "Riesgo"),
    ("2371059800", "Tipo de formulario y requisitos"),
    ("2365456692", "Validaciones por figura"),
    ("2878308532", "Actualización"),
    ("2879062422", "ApiTerceros"),
    ("3360948332", "Servicios Web - SarlaftEngine"),
    ("3735683077", "Pruebas automatizadas Motor"),
    ("3779330147", "Modificación de Agentes Corredores y Reglas de Negocio"),
    ("3890151437", "Regla Tablas Paramétricas PJ_SOAT - Motor Evaluación"),
    ("3988389894", "Motor Evaluación - Retirar evidencia de IDENTITY para asesores"),
]


# ─── Helpers de nombre ────────────────────────────────────────────────────────
def to_pascal(title: str) -> str:
    """'Tipo de formulario y requisitos' → 'TipoDeFormularioYRequisitos'"""
    clean = re.sub(r'[<>:"/\\|?*&@#\(\)\[\]{}]', ' ', title)
    parts = re.split(r'[\s\-_/\.·]+', clean)
    result = ""
    for p in parts:
        if p:
            result += p[0].upper() + p[1:]
    return result or "Pagina"


def safe_folder(name: str) -> str:
    """Elimina caracteres no válidos en Windows para nombres de carpeta."""
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()


# ─── API helpers ──────────────────────────────────────────────────────────────
def api_get(path: str, **params) -> dict:
    """GET a REST API v1 de Confluence. `path` relativo a BASE_URL/wiki."""
    url = f"{BASE_URL}/wiki{path}"
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def get_page(page_id: str) -> dict:
    return api_get(
        f"/rest/api/content/{page_id}",
        expand="body.view,version,ancestors,space",
    )


def get_children_page(page_id: str) -> list:
    results = []
    start = 0
    limit = 50
    while True:
        data = api_get(
            f"/rest/api/content/{page_id}/child/page",
            limit=limit, start=start, expand="version",
        )
        batch = data.get("results", [])
        results.extend(batch)
        if len(batch) < limit:
            break
        start += limit
    return results


def get_all_descendants(page_id: str, depth: int = 0) -> list:
    """Retorna [(id, title, depth), ...] para todos los descendientes."""
    items = []
    for ch in get_children_page(page_id):
        items.append((ch["id"], ch["title"], depth))
        items.extend(get_all_descendants(ch["id"], depth + 1))
    return items


def get_comments(page_id: str) -> list:
    try:
        data = api_get(
            f"/rest/api/content/{page_id}/child/comment",
            depth="all", expand="body.view,version", limit=50,
        )
        return data.get("results", [])
    except Exception as e:
        print(f"    [WARN] Comentarios {page_id}: {e}")
        return []


def get_attachments(page_id: str) -> list:
    try:
        data = api_get(
            f"/rest/api/content/{page_id}/child/attachment",
            limit=100, expand="version",
        )
        return data.get("results", [])
    except Exception as e:
        print(f"    [WARN] Adjuntos {page_id}: {e}")
        return []


def download_bin(dl_path: str, dest: Path) -> bool:
    """Descarga un archivo binario desde Confluence."""
    if dl_path.startswith("http"):
        url = dl_path
    elif dl_path.startswith("/wiki"):
        url = BASE_URL + dl_path
    else:
        url = BASE_URL + "/wiki" + dl_path
    try:
        r = requests.get(url, headers=DL_HEADERS, stream=True, timeout=60)
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"    [ERR DL] {dest.name}: {e}")
        return False


# ─── HTML → Markdown ──────────────────────────────────────────────────────────
def _convert_table(m: re.Match) -> str:
    table_html = m.group(0)
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.S)
    if not rows:
        return ""
    md_rows = []
    for i, row in enumerate(rows):
        th = re.findall(r'<th[^>]*>(.*?)</th>', row, re.S)
        td = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
        cells = th if th else td
        clean = [
            re.sub(r'<[^>]+>', '', html_lib.unescape(c))
            .strip().replace('\n', ' ').replace('|', '\\|')
            for c in cells
        ]
        if not clean:
            continue
        md_rows.append("| " + " | ".join(clean) + " |")
        if i == 0:
            md_rows.append("| " + " | ".join(["---"] * len(clean)) + " |")
    return "\n" + "\n".join(md_rows) + "\n" if md_rows else ""


def html_to_md(raw: str) -> str:
    if not raw:
        return ""
    md = raw

    # Tablas — procesar completas antes de aplicar otros patrones
    md = re.sub(r'<table[^>]*>.*?</table>', _convert_table, md, flags=re.S)

    # Negritas / itálicas
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>',           r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>',          r'_\1_',  md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>',            r'_\1_',  md, flags=re.S)

    # Headings (bump 1 nivel pues H1 es el título de la página)
    for n in range(6, 0, -1):
        level = min(n + 1, 6)
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>',
                    rf'\n{"#" * level} \1\n', md, flags=re.S)

    # Código inline / bloques pre
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.S)
    md = re.sub(
        r'<pre[^>]*>(.*?)</pre>',
        lambda m: f'\n```\n{html_lib.unescape(re.sub(r"<[^>]+>", "", m.group(1)))}\n```\n',
        md, flags=re.S,
    )

    # Macros info/warning/note/tip → blockquote
    md = re.sub(
        r'<div[^>]*class="[^"]*confluence-information-macro-body[^"]*"[^>]*>(.*?)</div>',
        lambda m: '\n> ' + re.sub(r'<[^>]+>', '', html_lib.unescape(m.group(1))).strip().replace('\n', '\n> ') + '\n',
        md, flags=re.S,
    )
    md = re.sub(
        r'<div[^>]*class="[^"]*aui-message[^"]*"[^>]*>(.*?)</div>',
        lambda m: '\n> ' + re.sub(r'<[^>]+>', '', html_lib.unescape(m.group(1))).strip().replace('\n', '\n> ') + '\n',
        md, flags=re.S,
    )

    # Links
    def _link(m: re.Match) -> str:
        href = m.group(1)
        text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        return f"[{text or href}]({href})"
    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', _link, md, flags=re.S)

    # Imágenes
    md = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*/?>',
                r'![\1](\2)', md, flags=re.S)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>',
                r'![\2](\1)', md, flags=re.S)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',
                r'![imagen](\1)', md, flags=re.S)

    # Listas
    md = re.sub(r'<[uo]l[^>]*>', '\n', md)
    md = re.sub(r'</[uo]l>',     '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.S)

    # Párrafos / saltos / divs
    md = re.sub(r'<p[^>]*>',  '\n', md)
    md = re.sub(r'</p>',      '\n', md)
    md = re.sub(r'<br\s*/?>', '\n', md)
    md = re.sub(r'<hr\s*/?>', '\n---\n', md)
    md = re.sub(r'<div[^>]*>', '', md)
    md = re.sub(r'</div>',    '\n', md)
    md = re.sub(r'<span[^>]*>', '', md)
    md = re.sub(r'</span>',   '', md)

    # Eliminar tags restantes
    md = re.sub(r'<[^>]+>', '', md)

    # Entidades HTML
    md = html_lib.unescape(md)

    # Normalizar líneas en blanco consecutivas
    md = re.sub(r'\n{3,}', '\n\n', md)

    # MD032 (a): guion solitario seguido de contenido en línea aparte
    md = re.sub(r'\n- *\n([^\n])', lambda m2: f'\n- {m2.group(1)}', md)

    # MD032 (b): non-list/non-blank → ítem de lista (insertar línea en blanco)
    _lp = re.compile(r'^[-*+]\s|\d+\.\s')
    _lns = md.split('\n'); _out2 = []
    for _i, _ln in enumerate(_lns):
        _out2.append(_ln)
        if _i < len(_lns) - 1:
            _nxt = _lns[_i + 1]
            if _ln.strip() and not _lp.match(_ln.strip()) and _lp.match(_nxt.strip()):
                _out2.append('')
    md = '\n'.join(_out2)

    # heading-order: normalizar jerarquía (evita saltos h1→h3+)
    _h_prev = 1; _h_out = []
    for _hl in md.split('\n'):
        _hm = re.match(r'^(#{1,6})(\s)', _hl)
        if _hm:
            _lvl = len(_hm.group(1))
            if _lvl > _h_prev + 1:
                _lvl = _h_prev + 1
                _hl = '#' * _lvl + _hm.group(2) + _hl[len(_hm.group(1)) + 1:]
            _h_prev = _lvl
        _h_out.append(_hl)
    md = '\n'.join(_h_out)
    return md.strip()


# ─── Adjuntos ─────────────────────────────────────────────────────────────────
def process_attachments(page_id: str, section_dir: Path) -> dict:
    """Descarga adjuntos y retorna {filename: rel_md_path}."""
    atts = get_attachments(page_id)
    att_map = {}

    for att in atts:
        media = att.get("mediaType", "")
        fname = att.get("title", "")
        dl    = att.get("_links", {}).get("download", "")
        if not dl or not fname:
            continue

        if media.startswith("image/"):
            dest_dir = section_dir / "img"
            rel      = f"./img/{fname}"
        elif media.startswith("application/pdf"):
            dest_dir = PDF_ROOT
            rel      = f"../../pdf/{fname}"
        elif "word" in media or "msword" in media:
            dest_dir = DOCX_ROOT
            rel      = f"../../docx/{fname}"
        elif "spreadsheet" in media or "excel" in media:
            dest_dir = XLSX_ROOT
            rel      = f"../../xlsx/{fname}"
        else:
            dest_dir = section_dir / "attachments"
            rel      = f"./attachments/{fname}"

        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / fname

        if not dest.exists():
            ok = download_bin(dl, dest)
            if ok:
                print(f"    [DL] {fname}")
            else:
                continue
        else:
            print(f"    [EXISTS] {fname}")

        att_map[fname] = rel

    return att_map


def fix_img_refs(md: str, att_map: dict) -> str:
    """Reemplaza URLs de imágenes de Confluence con rutas locales relativas."""
    def _repl(m: re.Match) -> str:
        alt, src = m.group(1), m.group(2)
        src_dec = unquote(src)
        for fname, rel in att_map.items():
            if fname in src_dec or fname in src:
                return f"![{alt or fname}]({rel})"
        return m.group(0)
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', _repl, md)


# ─── Comentarios ──────────────────────────────────────────────────────────────
def build_comments_md(page_id: str, section_dir: Path) -> str:
    comments = get_comments(page_id)
    if not comments:
        return ""

    lines = ["\n\n---\n\n## Comentarios de Confluence\n"]

    for i, c in enumerate(comments, 1):
        c_id   = c.get("id", "?")
        ver    = c.get("version", {})
        author = ver.get("by", {}).get("displayName", "?")
        when   = (ver.get("when") or "")[:10] or "?"
        body_h = c.get("body", {}).get("view", {}).get("value", "")
        body_m = html_to_md(body_h)

        lines.append(f"\n### Comentario {i}\n")
        lines.append(
            f"> **Autor:** {author}  \n"
            f"> **Fecha:** {when}  \n"
            f"> **ID comentario:** `{c_id}`\n"
        )
        lines.append(body_m)

        # Adjuntos del comentario
        c_atts = get_attachments(c_id)
        if c_atts:
            att_dir = section_dir / "attachments"
            att_dir.mkdir(exist_ok=True)
            lines.append("\n#### Adjuntos del comentario\n")
            lines.append("| Archivo | Tipo |\n|---------|------|\n")
            for att in c_atts:
                fname = att.get("title", "")
                media = att.get("mediaType", "")
                dl    = att.get("_links", {}).get("download", "")
                dest  = att_dir / fname
                if dl and not dest.exists():
                    download_bin(dl, dest)
                lines.append(f"| [`{fname}`](./attachments/{fname}) | `{media}` |\n")

    return "\n".join(lines)


# ─── Construir .md de una página ──────────────────────────────────────────────
def build_page_md(
    page: dict,
    section_dir: Path,
    section_title: str,
    parent_link: str = "./index.md",
) -> str:
    page_id   = page["id"]
    title     = page["title"]
    ver       = page.get("version", {})
    ver_n     = ver.get("number", "?")
    by        = ver.get("by", {}).get("displayName", "?")
    when      = (ver.get("when") or "")[:10] or "?"
    web_ui    = BASE_URL + "/wiki" + page.get("_links", {}).get("webui", f"/spaces/EPA/pages/{page_id}")
    body_html = page.get("body", {}).get("view", {}).get("value", "")

    att_map  = process_attachments(page_id, section_dir)
    body_md  = html_to_md(body_html)
    body_md  = fix_img_refs(body_md, att_map)
    comm_md  = build_comments_md(page_id, section_dir)

    header = (
        f"# {title}\n\n"
        f"> **Fuente Confluence:** [{title}]({web_ui})  \n"
        f"> **Última modificación:** {when} — {by} · versión {ver_n}  \n"
        f"> **Sección:** [{section_title}]({parent_link})\n\n"
    )

    att_section = ""
    if att_map:
        att_section = "## Archivos adjuntos\n\n| Archivo | Enlace |\n|---------|--------|\n"
        for fname, rel in att_map.items():
            att_section += f"| `{fname}` | [{fname}]({rel}) |\n"
        att_section += "\n"

    return header + att_section + body_md + comm_md


# ─── Procesar una sección ─────────────────────────────────────────────────────
def process_section(section_id: str, section_title: str) -> list:
    print(f"\n{'='*60}")
    print(f"SECCIÓN: {section_title}  [{section_id}]")
    print("=" * 60)

    folder      = safe_folder(section_title)
    section_dir = MOTOR_ROOT / folder
    (section_dir / "img").mkdir(parents=True, exist_ok=True)
    (section_dir / "attachments").mkdir(parents=True, exist_ok=True)

    root  = get_page(section_id)
    descs = get_all_descendants(section_id)
    print(f"  Páginas: 1 raíz + {len(descs)} hijas")

    # ── index.md (página raíz de la sección) ──
    print(f"  → index.md  [{section_title}]")
    root_md = build_page_md(root, section_dir, section_title, "./index.md")

    if descs:
        root_md += "\n\n## Sub-páginas\n\n| Página | Nivel |\n|--------|-------|\n"
        for pid, ptitle, depth in descs:
            fname  = to_pascal(ptitle)
            indent = "&nbsp;&nbsp;" * depth
            root_md += f"| {indent}[{ptitle}](./{fname}.md) | {depth} |\n"

    (section_dir / "index.md").write_text(root_md, encoding="utf-8")

    # ── Una página .md por cada descendiente ──
    created   = [("index", section_title)]
    seen_names = {"index"}

    for pid, ptitle, depth in descs:
        fname = to_pascal(ptitle)
        if fname in seen_names:
            fname = f"{fname}_{pid}"
        seen_names.add(fname)
        created.append((fname, ptitle))

        print(f"  → {fname}.md  [{ptitle}]")
        try:
            page = get_page(pid)
            md   = build_page_md(page, section_dir, section_title, "./index.md")
            (section_dir / f"{fname}.md").write_text(md, encoding="utf-8")
        except Exception as e:
            print(f"    [ERROR] {ptitle}: {e}")

    print(f"  [OK] {len(created)} archivo(s) generados en {section_dir}")
    return created


# ─── Main ─────────────────────────────────────────────────────────────────────
def main() -> None:
    t0 = datetime.now()
    print("=" * 60)
    print("Motor de Evaluación — Descarga Confluence")
    print(f"Output: {MOTOR_ROOT}")
    print("=" * 60)

    summary = []
    for sid, stitle in SECTIONS:
        try:
            pages = process_section(sid, stitle)
            summary.append((stitle, pages, True))
        except Exception as e:
            import traceback
            print(f"\n[ERROR SECCIÓN] {stitle}: {e}")
            traceback.print_exc()
            summary.append((stitle, [], False))

    # ── Índice maestro ──
    now = datetime.now().strftime("%Y-%m-%d")
    idx = (
        "# Motor de Evaluación — Índice\n\n"
        "> **Fuente Confluence:** [Motor de Evaluación]"
        "(https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1809941005)  \n"
        f"> **Fecha extracción:** {now}\n\n"
        "## Secciones\n\n"
        "| Sección | Páginas | Estado |\n|---------|---------|--------|\n"
    )
    for stitle, pages, ok in summary:
        folder = safe_folder(stitle)
        status = "OK" if ok else "ERROR"
        idx += f"| [{stitle}](./{folder}/index.md) | {len(pages)} | {status} |\n"

    (MOTOR_ROOT / "_INDICE.md").write_text(idx, encoding="utf-8")

    elapsed = int((datetime.now() - t0).total_seconds())
    print(f"\n{'='*60}")
    print(f"COMPLETADO en {elapsed}s")
    print(f"Índice maestro: {MOTOR_ROOT / '_INDICE.md'}")
    print("=" * 60)


if __name__ == "__main__":
    main()
