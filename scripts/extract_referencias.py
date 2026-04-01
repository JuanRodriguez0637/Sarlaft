"""
extract_referencias.py — Extrae páginas referenciadas + adjuntos faltantes + índice
"""
import os
import re
import html as html_lib
from datetime import date
from collections import OrderedDict

import requests
from confluence_config import (
    BASE_URL, HEADERS, DL_HEADERS,
    DOCS_ROOT, ARCHI_ROOT, REF_ROOT, IMG_ROOT,
)

for folder in [REF_ROOT, os.path.join(DOCS_ROOT, "pdf"),
               os.path.join(DOCS_ROOT, "docx"), os.path.join(DOCS_ROOT, "xlsx"), IMG_ROOT]:
    os.makedirs(folder, exist_ok=True)

# ---------------------------------------------------------------------------
# HTML → Markdown (igual que confluence_downloader.py)
# ---------------------------------------------------------------------------
def html_to_md(raw: str) -> str:
    if not raw:
        return ""
    md = raw
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>',           r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>',          r'_\1_',  md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>',            r'_\1_',  md, flags=re.S)
    for n in range(1, 7):
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>', rf'\n{"#"*n} \1\n', md, flags=re.S)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`',           md, flags=re.S)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>',   r'\n```\n\1\n```\n', md, flags=re.S)
    def replace_link(m):
        href, text = m.group(1), m.group(2)
        return f"[{href}]({href})" if not text.strip() else f"[{text}]({href})"
    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', replace_link, md, flags=re.S)
    md = re.sub(r'<ac:image[^>]*>.*?<ri:attachment ri:filename="([^"]*)".*?</ac:image>',
                r'![imagen](\1)', md, flags=re.S)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>',  r'![imagen](\1)', md, flags=re.S)
    md = re.sub(r'<ul[^>]*>',  '\n', md); md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<ol[^>]*>',  '\n', md); md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.S)
    md = re.sub(r'<table[^>]*>', '\n', md); md = re.sub(r'</table>', '\n', md)
    md = re.sub(r'<t(?:head|body|foot)[^>]*>', '', md)
    md = re.sub(r'</t(?:head|body|foot)>', '', md)
    md = re.sub(r'<tr[^>]*>', '|', md);    md = re.sub(r'</tr>', '\n', md)
    md = re.sub(r'<th[^>]*>(.*?)</th>', r' **\1** |', md, flags=re.S)
    md = re.sub(r'<td[^>]*>(.*?)</td>', r' \1 |',     md, flags=re.S)
    md = re.sub(r'<p[^>]*>',  '\n', md); md = re.sub(r'</p>', '\n', md)
    md = re.sub(r'<br\s*/?>', '\n', md);  md = re.sub(r'<hr\s*/?>', '\n---\n', md)
    md = re.sub(r'<div[^>]*>', '\n', md); md = re.sub(r'</div>', '\n', md)
    md = re.sub(r'<span[^>]*>', '', md);  md = re.sub(r'</span>', '', md)
    md = re.sub(r'<[^>]+>', '', md)
    md = html_lib.unescape(md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()

# ---------------------------------------------------------------------------
# Adjuntos - ruta relativa a referencias/ (imagen en ../imagenes)
# ---------------------------------------------------------------------------
MEDIA_MAP = {
    "application/pdf": (os.path.join(DOCS_ROOT, "pdf"),  "../../pdf"),
    "application/vnd.openxmlformats-officedocument.wordprocessingml": (os.path.join(DOCS_ROOT, "docx"), "../../docx"),
    "application/msword": (os.path.join(DOCS_ROOT, "docx"), "../../docx"),
    "application/vnd.openxmlformats-officedocument.spreadsheetml": (os.path.join(DOCS_ROOT, "xlsx"), "../../xlsx"),
    "application/vnd.ms-excel": (os.path.join(DOCS_ROOT, "xlsx"), "../../xlsx"),
    "image/jpeg":    (IMG_ROOT, "../imagenes"),
    "image/png":     (IMG_ROOT, "../imagenes"),
    "image/gif":     (IMG_ROOT, "../imagenes"),
    "image/svg+xml": (IMG_ROOT, "../imagenes"),
}

def download_bin(wiki_path: str, dest_file: str) -> None:
    url = f"{BASE_URL}/wiki{wiki_path}"
    resp = requests.get(url, headers=DL_HEADERS, stream=True)
    resp.raise_for_status()
    with open(dest_file, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

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
                    download_bin(dl_path, dest_file)
                    print(f"  [DL] {filename}")
                except Exception as e:
                    print(f"  [ERR DL] {filename}: {e}")
                    ok = False
            else:
                print(f"  [exists] {filename}")
            if ok:
                links.append(f"- [{filename}]({rel_folder}/{filename})")
    return links

def extract_page(page_id: str, out_file: str, space_key: str = "EPA") -> bool:
    print(f"\n[{page_id}] -> {os.path.basename(out_file)} ...")
    try:
        page    = requests.get(
            f"{BASE_URL}/wiki/api/v2/pages/{page_id}?body-format=view",
            headers=HEADERS).json()
        title   = page.get("title", page_id)
        body_md = html_to_md(page.get("body", {}).get("view", {}).get("value", ""))
        att_links = process_attachments(page_id)
        today = date.today().strftime("%Y-%m-%d")
        content  = f"# {title}\n\n"
        content += f"> **Fuente:** [Ver en Confluence]({BASE_URL}/wiki/spaces/{space_key}/pages/{page_id})\n"
        content += f"> **Fecha extracción:** {today}\n\n"
        if att_links:
            content += "## Archivos Adjuntos\n\n" + "\n".join(att_links) + "\n\n---\n\n"
        content += body_md
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {title}")
        return True
    except Exception as e:
        print(f"  [ERROR]: {e}")
        return False

# ---------------------------------------------------------------------------
# 1. Páginas referenciadas
# ---------------------------------------------------------------------------
REF_PAGES = OrderedDict([
    ("1814233305", {"file": "ServicioEvaluacionValidacionSarlaft.md", "space": "EPA"}),
    ("2093350926", {"file": "ServicioProcesoMasivo.md",               "space": "EPA"}),
    ("1955070163", {"file": "InterfazProcesosMasivos.md",             "space": "EPA"}),
    ("2619802061", {"file": "ServicioValidacionRadicado.md",          "space": "EPA"}),
    ("1861058683", {"file": "Microservicio_ClientesPEP.md",           "space": "EPA"}),
    ("1804861539", {"file": "Microservicio_PEPS.md",                  "space": "EPA"}),
    ("1864597599", {"file": "QueryConsultaClientePEPS.md",            "space": "EPA"}),
    ("2476834835", {"file": "ServicioRecategorizacionEvaluacion.md",  "space": "EPA"}),
    ("1860862186", {"file": "ConsultaClienteRRCC.md",                 "space": "EPA"}),
    ("2787475565", {"file": "Microservicio_Identity.md",              "space": "EPA"}),
    ("2370961900", {"file": "ValidarIdentidad_Experian.md",           "space": "EPA"}),
    ("2456289281", {"file": "IV001_ValidarDocumentoIdentidad.md",     "space": "EPA"}),
    ("2345730088", {"file": "Microservicio_CCM.md",                   "space": "EPA"}),
    ("1814003981", {"file": "ServicioAdicionarEvidencias.md",         "space": "EPA"}),
    ("1955070150", {"file": "DescripcionInterfacesPrincipales.md",    "space": "EPA"}),
    ("256672056",  {"file": "LineamientosServiciosREST.md",           "space": "AR"}),
])

print("=== Extrayendo páginas referenciadas ===")
for pid, info in REF_PAGES.items():
    out = os.path.join(REF_ROOT, info["file"])
    extract_page(pid, out, info["space"])

# ---------------------------------------------------------------------------
# 2. Adjuntos faltantes
# ---------------------------------------------------------------------------
print("\n=== Descargando adjuntos faltantes ===")
EXTRA_FILES = [
    {
        "path": "/wiki/download/attachments/1866629127/CacheRedis.docx"
                "?version=2&modificationDate=1618409454195&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "docx", "CacheRedis.docx"),
    },
    {
        "path": "/wiki/download/attachments/3737911299/"
                "Simplificar%20Arquitectura%20webhook%20en%20Sarlaft%204.pdf"
                "?version=2&modificationDate=1715951789475&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "pdf", "SimplificarArquitecturaWebhook.pdf"),
    },
    {
        "path": "/wiki/download/attachments/3737911299/"
                "Diagrama%20de%20la%20arquitectura%20actual%20del%20proceso%20webhook%20en%20Sarlaft%204.docx"
                "?version=2&modificationDate=1715951789220&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "docx", "DiagramaArquitecturaActualWebhook.docx"),
    },
    {
        "path": "/wiki/download/attachments/3224436826/DocumentacionSarlaft.xlsx"
                "?version=3&modificationDate=1726521332193&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "xlsx", "DocumentacionSarlaft.xlsx"),
    },
    {
        "path": "/wiki/download/attachments/3307601991/respuestasErroresSarlaft4.xlsx"
                "?version=2&modificationDate=1692995714983&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "xlsx", "respuestasErroresSarlaft4.xlsx"),
    },
]
for item in EXTRA_FILES:
    name = os.path.basename(item["dest"])
    if os.path.exists(item["dest"]):
        print(f"  [exists] {name}")
    else:
        try:
            download_bin(item["path"], item["dest"])
            print(f"  [DL] {name}")
        except Exception as e:
            print(f"  [ERR] {name}: {e}")

# ---------------------------------------------------------------------------
# 3. Índice de referencias
# ---------------------------------------------------------------------------
print("\nGenerando índice de referencias...")
today = date.today().strftime("%Y-%m-%d")
idx  = "# Referencias — Páginas enlazadas desde Diseño - Arquitectura\n\n"
idx += "> Páginas de Confluence referenciadas en la sección Diseño - Arquitectura que contienen información complementaria.\n"
idx += f"> **Fecha extracción:** {today}\n\n"
idx += "## Páginas del espacio EPA (Sarlaft 4.0)\n\n"

EPA_META = [
    ("ServicioEvaluacionValidacionSarlaft.md",  "Servicio Evaluación Validación Sarlaft",             "F02_EntradasEvaluacion.md, F03_Validaciones.md"),
    ("ServicioProcesoMasivo.md",                "Servicio Proceso Masivo",                             "F02_EntradasEvaluacion.md"),
    ("InterfazProcesosMasivos.md",              "Interfaz Procesos Masivos",                           "F02_EntradasEvaluacion.md, F07_Webhook.md"),
    ("ServicioValidacionRadicado.md",           "Servicio Validacion Radicado",                        "F02_EntradasEvaluacion.md"),
    ("Microservicio_ClientesPEP.md",            "Microservicio - Clientes PEP",                        "F03_Validaciones.md"),
    ("Microservicio_PEPS.md",                   "Microservicio PEPS",                                  "F03_Validaciones.md"),
    ("QueryConsultaClientePEPS.md",             "Query consulta Cliente PEPS",                         "F03_Validaciones.md"),
    ("ServicioRecategorizacionEvaluacion.md",   "Servicio Recategorización Evaluación Sarlaft",        "F03_Validaciones.md"),
    ("ConsultaClienteRRCC.md",                  "Consulta Cliente RRCC",                               "F03_Validaciones.md"),
    ("Microservicio_Identity.md",               "Microservicio - Identity",                            "F03_Validaciones.md"),
    ("ValidarIdentidad_Experian.md",            "Validar identidad (Experian)",                        "F03_Validaciones.md"),
    ("IV001_ValidarDocumentoIdentidad.md",      "IV001: Validar documento de identidad con Registraduría", "F03_Validaciones.md"),
    ("Microservicio_CCM.md",                    "Microservicio - CCM",                                 "F03_Validaciones.md"),
    ("ServicioAdicionarEvidencias.md",          "Servicio Adicionar Evidencias",                       "F03_Validaciones.md"),
    ("DescripcionInterfacesPrincipales.md",     "Descripción de Interfaces Principales",               "F07_Webhook.md"),
]
for fname, title, referencia in EPA_META:
    exists = "✅" if os.path.exists(os.path.join(REF_ROOT, fname)) else "❌"
    idx += f"{exists} [{title}]({fname}) — _referenciado desde: {referencia}_\n"

idx += "\n## Páginas de otros espacios\n\n"
lr = "LineamientosServiciosREST.md"
exists = "✅" if os.path.exists(os.path.join(REF_ROOT, lr)) else "❌"
idx += f"{exists} [Lineamientos para servicios REST (espacio AR)]({lr}) — _referenciado desde: RespuestasDeError.md_\n"

with open(os.path.join(REF_ROOT, "_INDICE_REFERENCIAS.md"), "w", encoding="utf-8") as f:
    f.write(idx)

print(f"Índice: {os.path.join(REF_ROOT, '_INDICE_REFERENCIAS.md')}")
print("\n=== COMPLETADO ===")
