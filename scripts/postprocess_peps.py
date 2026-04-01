"""
postprocess_peps.py — Post-procesa los .md de MicroservicioPEPS:
  1. Reemplaza URLs de imágenes Confluence por rutas locales relativas
  2. Descarga archivos JSON adjuntos e incrusta su contenido como bloques de código
"""
import os
import re
import json
import requests
from pathlib import Path
from confluence_config import BASE_URL, HEADERS, DL_HEADERS, DOCS_ROOT

PEPS_ROOT = os.path.join(DOCS_ROOT, "MicroservicioPEPS")
IMG_PEPS  = os.path.join(PEPS_ROOT, "imagenes")

# Mapeo de nombres de imagen → nombre de archivo local (ya descargados)
LOCAL_IMAGES = {f.lower(): f for f in os.listdir(IMG_PEPS)}

# Páginas con JSON adjuntos a incrustar
JSON_PAGES = {
    "1814200586": {  # Servicio Marcar Cliente PEPS
        "file": os.path.join(PEPS_ROOT, "ServiciosWeb_PepsMS", "ServicioMarcarClientePEPS.md"),
        "jsons": [
            ("request_assessment.json", "request_assessment"),
            ("request_mark.json",       "request_mark"),
            ("request.json",            "request"),
        ]
    },
    "1813971266": {  # Servicio Consulta PEPS
        "file": os.path.join(PEPS_ROOT, "ServiciosWeb_PepsMS", "ServicioConsultaPEPS.md"),
        "jsons": [
            ("request_mark.json",       "request_mark"),
            ("request_checkpeps.json",  "request_checkpeps"),
        ]
    }
}


def fix_image_urls_in_file(md_file: str) -> int:
    """
    Reemplaza URLs de Confluence de imágenes por rutas locales relativas.
    Devuelve el número de reemplazos.
    """
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    md_dir = os.path.dirname(md_file)
    count = 0

    # Patrón: ![alt](https://...atlassian.net/wiki/download/attachments/<id>/<filename>?...)
    pattern = re.compile(
        r'!\[([^\]]*)\]\((https?://[^)]*atlassian\.net/wiki/download/attachments/[^)]+/([^)?]+)\?[^)]*)\)'
    )

    def replace_img(m):
        nonlocal count
        alt = m.group(1)
        full_url = m.group(2)
        filename = m.group(3)

        # Buscar el archivo local (case-insensitive)
        local_name = LOCAL_IMAGES.get(filename.lower())
        if local_name:
            rel_path = os.path.relpath(
                os.path.join(IMG_PEPS, local_name), md_dir
            ).replace("\\", "/")
            count += 1
            return f"![{alt or local_name}]({rel_path})"
        else:
            # Mantener URL original si no tenemos la imagen
            return m.group(0)

    new_content = pattern.sub(replace_img, content)

    if count > 0:
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  [IMGS FIJADAS: {count}] {os.path.relpath(md_file, PEPS_ROOT)}")

    return count


def fetch_json_attachment(page_id: str, filename: str) -> str | None:
    """Descarga el contenido de un attachment JSON desde Confluence."""
    # Listar adjuntos de la página
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/attachments?limit=50"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        atts = resp.json().get("results", [])
    except Exception as e:
        print(f"  [ERROR listar adjuntos {page_id}]: {e}")
        return None

    for att in atts:
        if att.get("title", "").lower() == filename.lower():
            dl_path = att.get("_links", {}).get("download", "")
            if dl_path:
                dl_url = f"{BASE_URL}/wiki{dl_path}"
                try:
                    r = requests.get(dl_url, headers=DL_HEADERS, timeout=30)
                    r.raise_for_status()
                    return r.text
                except Exception as e:
                    print(f"  [ERROR descarga JSON {filename}]: {e}")
                    return None
    return None


def embed_json_in_file(page_id: str, md_file: str, jsons: list) -> None:
    """
    Añade sección de ejemplos JSON al final del .md si no existe.
    jsons: lista de (filename, label)
    """
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    section = "\n\n## Ejemplos JSON (Adjuntos)\n\n"
    added = False

    for filename, label in jsons:
        if f"```json" in content and label in content:
            print(f"  [YA EXISTE JSON] {filename}")
            continue

        print(f"  Descargando JSON: {filename}...")
        json_text = fetch_json_attachment(page_id, filename)
        if json_text:
            try:
                # Formatear el JSON limpiamente
                parsed = json.loads(json_text)
                formatted = json.dumps(parsed, ensure_ascii=False, indent=2)
            except Exception:
                formatted = json_text

            section += f"### `{filename}`\n\n"
            section += f"```json\n{formatted}\n```\n\n"
            added = True
            print(f"  [JSON EMBEBIDO] {filename}")
        else:
            print(f"  [NO ENCONTRADO] {filename}")

    if added:
        content += section
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(content)


def main():
    print("=" * 60)
    print("Post-procesando archivos MicroservicioPEPS")
    print("=" * 60)

    # 1. Corregir URLs de imágenes en todos los .md
    print("\n--- Corrigiendo URLs de imágenes ---")
    total_fixes = 0
    for root, dirs, files in os.walk(PEPS_ROOT):
        for fname in files:
            if fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                total_fixes += fix_image_urls_in_file(fpath)
    print(f"Total reemplazos de imágenes: {total_fixes}")

    # 2. Embeber JSON en páginas de servicios
    print("\n--- Embebiendo ejemplos JSON en servicios ---")
    for page_id, info in JSON_PAGES.items():
        md_file = info["file"]
        if os.path.exists(md_file):
            print(f"\n[{page_id}] {os.path.basename(md_file)}")
            embed_json_in_file(page_id, md_file, info["jsons"])
        else:
            print(f"[NO ENCONTRADO] {md_file}")

    print("\n=== Post-procesamiento completado ===")


if __name__ == "__main__":
    main()
