"""
download_attachments.py — Descarga adjuntos puntuales ya conocidos
"""
import os
import requests
from confluence_config import BASE_URL, DL_HEADERS, DOCS_ROOT

FILES = [
    {
        "url": "/wiki/download/attachments/1801159177/DocumentacionTecnicaSarlaft_1.4.pdf"
               "?version=1&modificationDate=1616722886954&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "pdf", "DocumentacionTecnicaSarlaft_1.4.pdf"),
    },
    {
        "url": "/wiki/download/attachments/1801159177/DocumentacionTecnicaSarlaft_1.5.pdf"
               "?version=1&modificationDate=1618515881594&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "pdf", "DocumentacionTecnicaSarlaft_1.5.pdf"),
    },
    {
        "url": "/wiki/download/attachments/3214016543/OrganizacionDocumentacion.pdf"
               "?version=1&modificationDate=1686930987996&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "pdf", "OrganizacionDocumentacion.pdf"),
    },
    {
        "url": "/wiki/download/attachments/1866629127/CacheRedis.docx"
               "?version=2&modificationDate=1618409454195&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "docx", "CacheRedis.docx"),
    },
    {
        "url": "/wiki/download/attachments/3737911299/"
               "Simplificar%20Arquitectura%20webhook%20en%20Sarlaft%204.pdf"
               "?version=2&modificationDate=1715951789475&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "pdf", "SimplificarArquitecturaWebhook.pdf"),
    },
    {
        "url": "/wiki/download/attachments/3737911299/"
               "Diagrama%20de%20la%20arquitectura%20actual%20del%20proceso%20webhook%20en%20Sarlaft%204.docx"
               "?version=2&modificationDate=1715951789220&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "docx", "DiagramaArquitecturaActualWebhook.docx"),
    },
    {
        "url": "/wiki/download/attachments/3224436826/DocumentacionSarlaft.xlsx"
               "?version=3&modificationDate=1726521332193&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "xlsx", "DocumentacionSarlaft.xlsx"),
    },
    {
        "url": "/wiki/download/attachments/3307601991/respuestasErroresSarlaft4.xlsx"
               "?version=2&modificationDate=1692995714983&cacheVersion=1&api=v2",
        "dest": os.path.join(DOCS_ROOT, "xlsx", "respuestasErroresSarlaft4.xlsx"),
    },
]


def main():
    for item in FILES:
        name = os.path.basename(item["dest"])
        if os.path.exists(item["dest"]):
            print(f"[YA EXISTE] {name}")
            continue
        try:
            resp = requests.get(BASE_URL + item["url"], headers=DL_HEADERS, stream=True)
            resp.raise_for_status()
            os.makedirs(os.path.dirname(item["dest"]), exist_ok=True)
            with open(item["dest"], "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"[DESCARGADO] {name}")
        except Exception as e:
            print(f"[ERROR] {name}: {e}")
    print("Listo.")


if __name__ == "__main__":
    main()
