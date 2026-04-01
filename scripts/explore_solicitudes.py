"""
Script para explorar la sección 'Documentación de Solicitudes' en Confluence EPA
"""
import requests
import json
from confluence_config import HEADERS, BASE_URL


def search_page(title):
    cql = f'space = "EPA" AND title = "{title}" AND type = page'
    r = requests.get(
        f"{BASE_URL}/wiki/rest/api/search",
        headers=HEADERS,
        params={"cql": cql, "expand": "version,ancestors"},
    )
    return r.json()


def get_children(page_id):
    cql = f'ancestor = {page_id} AND type = page'
    r = requests.get(
        f"{BASE_URL}/wiki/rest/api/search",
        headers=HEADERS,
        params={"cql": cql, "expand": "version,ancestors", "limit": 100},
    )
    return r.json()


def main():
    # Try different title variants
    titles = [
        "Documentación de Solicitudes",
        "Documentacion de Solicitudes",
        "Documentaci\u00f3n de Solicitudes",
    ]

    found = None
    for title in titles:
        data = search_page(title)
        results = data.get("results", [])
        if results:
            found = results[0]["content"]
            print(f"Found page: {found['title']} (id={found['id']})")
            print(f"Ancestors: {[a['title'] for a in found.get('ancestors', [])]}")
            break

    if not found:
        print("Page not found, trying broader search...")
        cql = 'space = "EPA" AND title ~ "Solicitudes" AND type = page'
        r = requests.get(
            f"{BASE_URL}/wiki/rest/api/search",
            headers=HEADERS,
            params={"cql": cql, "expand": "version,ancestors", "limit": 20},
        )
        data = r.json()
        for res in data.get("results", []):
            c = res["content"]
            print(f"  - [{c['id']}] {c['title']} | ancestors: {[a['title'] for a in c.get('ancestors', [])]}")
        return

    # Get children
    print(f"\n=== Children of '{found['title']}' (id={found['id']}) ===")
    children_data = get_children(found["id"])
    children = children_data.get("results", [])
    print(f"Total children found: {len(children)}")

    # Build tree
    tree = {}
    for res in children:
        c = res["content"]
        ancestors = [a["title"] for a in c.get("ancestors", [])]
        parent = ancestors[-1] if ancestors else "root"
        if parent not in tree:
            tree[parent] = []
        tree[parent].append({"id": c["id"], "title": c["title"]})

    print(json.dumps(tree, indent=2, ensure_ascii=False))

    # Save full data
    with open("scripts/solicitudes_tree.json", "w", encoding="utf-8") as f:
        json.dump({
            "root": {"id": found["id"], "title": found["title"]},
            "children": [{"id": r["content"]["id"], "title": r["content"]["title"],
                          "ancestors": [a["title"] for a in r["content"].get("ancestors", [])],
                          "version": r["content"].get("version", {})}
                         for r in children]
        }, f, indent=2, ensure_ascii=False)
    print("\nTree saved to scripts/solicitudes_tree.json")


if __name__ == "__main__":
    main()
