"""
explore_clientes.py — Mapea el árbol completo de Microservicio SarlaftClientesMS
"""
import requests, json, sys
sys.path.insert(0, 'scripts')
from confluence_config import BASE_URL, HEADERS

ROOT_ID = "2701656178"  # Microservicio SarlaftClientesMS

def get_children(page_id, indent=0):
    url = f"{BASE_URL}/wiki/rest/api/content/{page_id}/child/page"
    r = requests.get(url, headers=HEADERS, params={"limit": 100, "expand": "version"})
    data = r.json()
    pages = data.get("results", [])
    for p in pages:
        pid = p["id"]
        title = p["title"]
        print("  " * indent + f"├── [{pid}] {title}")
        get_children(pid, indent + 1)

# Get root page info
r = requests.get(f"{BASE_URL}/wiki/rest/api/content/{ROOT_ID}", headers=HEADERS,
                 params={"expand": "version,ancestors"})
root = r.json()
print(f"[{ROOT_ID}] {root['title']}")
print(f"  Version: {root['version']['number']} | By: {root['version']['by']['displayName']}")
print(f"  URL: {BASE_URL}/wiki{root['_links']['webui']}")
print()
get_children(ROOT_ID)
