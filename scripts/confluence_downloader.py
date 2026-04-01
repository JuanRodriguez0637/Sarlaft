"""
confluence_downloader.py — Descarga todas las páginas de Diseño - Arquitectura a .md
Incluye: contenido, adjuntos (imágenes, PDF, DOCX, XLSX) e índice.
"""
import os
import re
import html as html_lib
from datetime import date
from collections import OrderedDict

import requests
from confluence_config import BASE_URL, HEADERS, DL_HEADERS, DOCS_ROOT, ARCHI_ROOT, IMG_ROOT

# ---------------------------------------------------------------------------
# Carpetas
# ---------------------------------------------------------------------------
for folder in [ARCHI_ROOT, os.path.join(DOCS_ROOT, "pdf"),
               os.path.join(DOCS_ROOT, "docx"), os.path.join(DOCS_ROOT, "xlsx"), IMG_ROOT]:
    os.makedirs(folder, exist_ok=True)

# ---------------------------------------------------------------------------
# Páginas: ID → nombre de archivo (sin .md)
# ---------------------------------------------------------------------------
PAGES = OrderedDict([
    ("1804697669", "Diseño_Arquitectura"),
    ("1804927175", "RequisitosNoFuncionales"),
    ("1804861588", "DiagramasArquitectura"),
    ("1801126348", "ContextualizacionArquitectura"),
    ("1801159177", "DocumentoDiseñoTecnico"),
    ("3307601991", "RespuestasDeError"),
    ("1856537007", "EstandarNombramientoBD"),
    ("1866629127", "AccesoCache"),
    ("3214016543", "DiseñoFuncionalidades"),
    ("3214049307", "F01_ProcesoEvaluacion"),
    ("3213164787", "F02_EntradasEvaluacion"),
    ("3214082137", "F03_Validaciones"),
    ("3221782545", "F03a_EstadosEvidencias"),
    ("3222274070", "F04_ComunicacionMotor"),
    ("3222634497", "F05_DeterminarSiRequiereSarlaft"),
    ("3222831120", "F06_DeterminarEstadoEvaluacion"),
    ("3222994946", "F07_Webhook"),
    ("3737911299", "F07a_SimplificarArqWebhook"),
    ("3742531593", "F07a1_ArquitecturaActualWebhook"),
    ("3742892047", "F07a2_Propuesta1_OmitirServiceBus"),
    ("3743580178", "F07a3_Propuesta2_MantenerServiceBus"),
    ("3743219726", "F07a4_ConclusionesWebhook"),
    ("3224436826", "F08_ResumenInfoMicroservicios"),
    ("3226009603", "F09_ConsultaCliente_getClient"),
    ("3226599489", "F10_ValidacionClientePEPs"),
    ("3648421917", "F10a_ValidacionClientePEPs_Propuesta"),
    ("3228303479", "F11_RequisitosSarlaft"),
    ("3235053604", "F12_CrearEvaluacionFormulario"),
    ("3234791499", "F13_ConsultasRedComercial"),
    ("3235282962", "F14_ConsultasModuloClientes"),
    ("3234791531", "F15_ParametrizacionEntidades"),
    ("3236888621", "F17_DesmarcarClientePEPs"),
    ("3675586561", "F18_ConsultarCatalogos"),
    ("4703420517", "InformacionSecretos"),
])

# ---------------------------------------------------------------------------
# HTML → Markdown
# ---------------------------------------------------------------------------
def html_to_md(raw: str) -> str:
    if not raw:
        return ""
    md = raw

    # Negritas / itálicas
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>',           r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>',          r'_\1_',  md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>',            r'_\1_',  md, flags=re.S)

    # Headings
    for n in range(1, 7):
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>', rf'\n{"#"*n} \1\n', md, flags=re.S)

    # Código
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`',           md, flags=re.S)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>',   r'\n```\n\1\n```\n', md, flags=re.S)

    # Links
    def replace_link(m):
        href, text = m.group(1), m.group(2)
        return f"[{href}]({href})" if not text.strip() else f"[{text}]({href})"
    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', replace_link, md, flags=re.S)

    # Imágenes Confluence
    md = re.sub(
        r'<ac:image[^>]*>.*?<ri:attachment ri:filename="([^"]*)".*?</ac:image>',
        r'![imagen](\1)', md, flags=re.S)
    md = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]*)"[^>]*/?>',
                r'![\1](\2)', md, flags=re.S)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',
                r'![imagen](\1)', md, flags=re.S)

    # Listas
    md = re.sub(r'<ul[^>]*>',  '\n', md); md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<ol[^>]*>',  '\n', md); md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.S)

    # Tablas
    md = re.sub(r'<table[^>]*>', '\n', md); md = re.sub(r'</table>', '\n', md)
    md = re.sub(r'<t(?:head|body|foot)[^>]*>', '', md)
    md = re.sub(r'</t(?:head|body|foot)>', '', md)
    md = re.sub(r'<tr[^>]*>', '|', md);    md = re.sub(r'</tr>', '\n', md)
    md = re.sub(r'<th[^>]*>(.*?)</th>', r' **\1** |', md, flags=re.S)
    md = re.sub(r'<td[^>]*>(.*?)</td>', r' \1 |',     md, flags=re.S)

    # Párrafos / saltos
    md = re.sub(r'<p[^>]*>',  '\n', md); md = re.sub(r'</p>', '\n', md)
    md = re.sub(r'<br\s*/?>', '\n', md)
    md = re.sub(r'<hr\s*/?>', '\n---\n', md)
    md = re.sub(r'<div[^>]*>', '\n', md); md = re.sub(r'</div>', '\n', md)
    md = re.sub(r'<span[^>]*>', '', md);  md = re.sub(r'</span>', '', md)

    # Eliminar tags restantes
    md = re.sub(r'<[^>]+>', '', md)

    # Entidades HTML
    md = html_lib.unescape(md)

    # Normalizar espacios en blanco
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()

# ---------------------------------------------------------------------------
# Descarga un archivo binario
# ---------------------------------------------------------------------------
def download_file(wiki_path: str, dest_file: str) -> None:
    url = f"{BASE_URL}/wiki{wiki_path}"
    resp = requests.get(url, headers=DL_HEADERS, stream=True)
    resp.raise_for_status()
    with open(dest_file, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

# ---------------------------------------------------------------------------
# Procesa adjuntos de una página
# ---------------------------------------------------------------------------
MEDIA_MAP = {
    "application/pdf": (os.path.join(DOCS_ROOT, "pdf"),  "../../pdf"),
    "application/vnd.openxmlformats-officedocument.wordprocessingml": (os.path.join(DOCS_ROOT, "docx"), "../../docx"),
    "application/msword": (os.path.join(DOCS_ROOT, "docx"), "../../docx"),
    "application/vnd.openxmlformats-officedocument.spreadsheetml": (os.path.join(DOCS_ROOT, "xlsx"), "../../xlsx"),
    "application/vnd.ms-excel": (os.path.join(DOCS_ROOT, "xlsx"), "../../xlsx"),
    "image/jpeg":  (IMG_ROOT, "imagenes"),
    "image/png":   (IMG_ROOT, "imagenes"),
    "image/gif":   (IMG_ROOT, "imagenes"),
    "image/svg+xml": (IMG_ROOT, "imagenes"),
}

def process_attachments(page_id: str) -> list[str]:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/attachments?limit=50"
    try:
        atts = requests.get(url, headers=HEADERS).json().get("results", [])
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

        if dest_folder:
            dest_file = os.path.join(dest_folder, filename)
            ok = True
            if not os.path.exists(dest_file):
                try:
                    download_file(dl_path, dest_file)
                    print(f"  [DESCARGADO] {filename}")
                except Exception as e:
                    print(f"  [ERROR] {filename}: {e}")
                    ok = False
            else:
                print(f"  [YA EXISTE] {filename}")
            if ok:
                links.append(f"- [{filename}]({rel_folder}/{filename})")
    return links

# ---------------------------------------------------------------------------
# Procesamiento principal
# ---------------------------------------------------------------------------
results = {}
today = date.today().strftime("%Y-%m-%d")

for page_id, file_name in PAGES.items():
    print(f"\n[{page_id}] {file_name} ...")
    try:
        page      = requests.get(
            f"{BASE_URL}/wiki/api/v2/pages/{page_id}?body-format=view",
            headers=HEADERS).json()
        title     = page.get("title", file_name)
        body_html = page.get("body", {}).get("view", {}).get("value", "")
        body_md   = html_to_md(body_html)
        att_links = process_attachments(page_id)

        content  = f"# {title}\n\n"
        content += f"> **Fuente:** [Ver en Confluence]({BASE_URL}/wiki/spaces/EPA/pages/{page_id})\n"
        content += f"> **Fecha extracción:** {today}\n\n"
        if att_links:
            content += "## Archivos Adjuntos\n\n"
            content += "\n".join(att_links) + "\n\n---\n\n"
        content += body_md

        out_path = os.path.join(ARCHI_ROOT, f"{file_name}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {title}")
        results[page_id] = {"title": title, "file": out_path, "ok": True}
    except Exception as e:
        print(f"  [ERROR {page_id}]: {e}")
        results[page_id] = {"title": file_name, "file": "", "ok": False}

# ---------------------------------------------------------------------------
# Índice
# ---------------------------------------------------------------------------
print("\nGenerando índice...")
TREE = """\
```text
Diseño - Arquitectura
├── RequisitosNoFuncionales.md
├── DiagramasArquitectura.md
├── ContextualizacionArquitectura.md
├── DocumentoDiseñoTecnico.md
│   └── RespuestasDeError.md
├── EstandarNombramientoBD.md
├── AccesoCache.md
├── DiseñoFuncionalidades.md
│   ├── F01_ProcesoEvaluacion.md
│   ├── F02_EntradasEvaluacion.md
│   ├── F03_Validaciones.md
│   │   └── F03a_EstadosEvidencias.md
│   ├── F04_ComunicacionMotor.md
│   ├── F05_DeterminarSiRequiereSarlaft.md
│   ├── F06_DeterminarEstadoEvaluacion.md
│   ├── F07_Webhook.md
│   │   └── F07a_SimplificarArqWebhook.md
│   │       ├── F07a1_ArquitecturaActualWebhook.md
│   │       ├── F07a2_Propuesta1_OmitirServiceBus.md
│   │       ├── F07a3_Propuesta2_MantenerServiceBus.md
│   │       └── F07a4_ConclusionesWebhook.md
│   ├── F08_ResumenInfoMicroservicios.md
│   ├── F09_ConsultaCliente_getClient.md
│   ├── F10_ValidacionClientePEPs.md
│   │   └── F10a_ValidacionClientePEPs_Propuesta.md
│   ├── F11_RequisitosSarlaft.md
│   ├── F12_CrearEvaluacionFormulario.md
│   ├── F13_ConsultasRedComercial.md
│   ├── F14_ConsultasModuloClientes.md
│   ├── F15_ParametrizacionEntidades.md
│   ├── F17_DesmarcarClientePEPs.md
│   └── F18_ConsultarCatalogos.md
└── InformacionSecretos.md
```"""

idx  = f"# Diseño - Arquitectura — Índice\n\n"
idx += f"> **Fuente Confluence:** [{BASE_URL}/wiki/spaces/EPA/pages/1804697669]({BASE_URL}/wiki/spaces/EPA/pages/1804697669)\n"
idx += f"> **Fecha extracción:** {today}\n\n"
idx += f"## Estructura de páginas\n\n{TREE}\n\n## Archivos generados\n\n"

for page_id, r in results.items():
    status = "✅" if r["ok"] else "❌"
    fname  = os.path.basename(r["file"]) if r["file"] else ""
    if r["ok"]:
        idx += f"{status} [{r['title']}]({fname})\n"
    else:
        idx += f"{status} {r['title']} _(error)_\n"

with open(os.path.join(ARCHI_ROOT, "_INDICE.md"), "w", encoding="utf-8") as f:
    f.write(idx)

print(f"Índice: {os.path.join(ARCHI_ROOT, '_INDICE.md')}")
print("\n=== COMPLETADO ===")
