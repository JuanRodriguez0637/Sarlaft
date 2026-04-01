#!/usr/bin/env python3
"""Explora la estructura de 'Configuración Plataforma Base Sarlaft' en Confluence."""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from confluence_config import BASE_URL, HEADERS
import requests


def api_get(path, **params):
    r = requests.get(f"{BASE_URL}/wiki{path}", headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def get_children(page_id):
    results = []
    start = 0
    while True:
        data = api_get(f"/rest/api/content/{page_id}/child/page", limit=50, start=start, expand="version")
        batch = data.get("results", [])
        results.extend(batch)
        if len(batch) < 50:
            break
        start += 50
    return results


def get_all_descendants(page_id, depth=0):
    items = []
    for ch in get_children(page_id):
        items.append((ch["id"], ch["title"], depth))
        items.extend(get_all_descendants(ch["id"], depth + 1))
    return items


# 1) Buscar por título
cql = 'space = "EPA" AND title = "Configuración Plataforma Base Sarlaft" AND type = page'
r = requests.get(f"{BASE_URL}/wiki/rest/api/search", headers=HEADERS, params={"cql": cql, "limit": 20}, timeout=30)
r.raise_for_status()
results = r.json().get("results", [])
print(f"=== Búsqueda: '{cql}' ===")
for res in results:
    c = res["content"]
    print(f"  [{c['id']}] {c['title']}  → {c['_links']['webui']}")

if not results:
    print("No encontrado por título exacto. Intentando búsqueda parcial...")
    cql2 = 'space = "EPA" AND title ~ "Configuraci" AND title ~ "Plataforma" AND type = page'
    r2 = requests.get(f"{BASE_URL}/wiki/rest/api/search", headers=HEADERS, params={"cql": cql2, "limit": 20}, timeout=30)
    r2.raise_for_status()
    for res in r2.json().get("results", []):
        c = res["content"]
        print(f"  [{c['id']}] {c['title']}  → {c['_links']['webui']}")

# 2) Si encontró algo, explorar árbol
for res in results:
    c = res["content"]
    page_id = c["id"]
    print(f"\n=== Árbol desde [{page_id}] {c['title']} ===")
    desc = get_all_descendants(page_id)
    print(f"  (raíz propia)")
    for d_id, d_title, d_depth in desc:
        indent = "  " * (d_depth + 1)
        print(f"{indent}[{d_id}] {d_title}")
    
    # Guardar árbol
    tree_data = {"root": {"id": page_id, "title": c["title"]}, "descendants": [
        {"id": d[0], "title": d[1], "depth": d[2]} for d in desc
    ]}
    out = Path(__file__).parent / "config_plataforma_tree.json"
    out.write_text(json.dumps(tree_data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nÁrbol guardado en: {out}")
