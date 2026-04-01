"""
check_peps_parents.py — Verificar los padres de las páginas PEPS encontradas
"""
import requests
from confluence_config import BASE_URL, HEADERS

page_ids = ["1804861539", "2314240187", "1861058683", "1860862179", "1860829373"]

for pid in page_ids:
    # API v1 includes ancestors
    url = f"{BASE_URL}/wiki/rest/api/content/{pid}?expand=ancestors,space,version"
    r = requests.get(url, headers=HEADERS, timeout=20).json()
    title = r.get("title", "?")
    ancestors = r.get("ancestors", [])
    space = r.get("space", {}).get("key", "?")
    parent = ancestors[-1]["title"] if ancestors else "ROOT"
    parent_id = ancestors[-1]["id"] if ancestors else "ROOT"
    print(f"[{pid}] {title}")
    print(f"  space={space}, parent=[{parent_id}] {parent}")
    for a in ancestors:
        print(f"    ancestor: [{a['id']}] {a['title']}")
