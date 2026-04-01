"""
explore_peps.py — Explorar la estructura de páginas "Microservicio PEPS" en Confluence
"""
import sys
import json
import requests
from confluence_config import BASE_URL, HEADERS


def search_page(title_query: str) -> list:
    cql = f'title ~ "{title_query}" AND space.key = "EPA" AND type = page'
    url = f"{BASE_URL}/wiki/rest/api/search"
    resp = requests.get(url, headers=HEADERS, params={"cql": cql, "limit": 30}, timeout=30)
    resp.raise_for_status()
    results = []
    for r in resp.json().get("results", []):
        c = r.get("content", {})
        results.append({"id": c.get("id"), "title": c.get("title")})
    return results


def get_page(page_id: str) -> dict:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()


def get_children(page_id: str) -> list:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/children?limit=50"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json().get("results", [])


def print_tree(page_id: str, indent: str = "", level: int = 0) -> list:
    """Recursively print and collect the tree of pages."""
    page = get_page(page_id)
    title = page.get("title", "?")
    print(f"{indent}[{page_id}] {title}")
    nodes = [{"id": page_id, "title": title, "level": level, "children": []}]
    for child in get_children(page_id):
        child_nodes = print_tree(child["id"], indent + "  ", level + 1)
        nodes[0]["children"].append(child_nodes[0])
        nodes.extend(child_nodes[1:] if len(child_nodes) > 1 else [])
    return nodes


def flatten_tree(nodes: list) -> list:
    """Flatten a tree of nodes into a list."""
    result = []
    for node in nodes:
        children = node.get("children", [])
        result.append({"id": node["id"], "title": node["title"], "level": node["level"]})
        result.extend(flatten_tree(children))
    return result


if __name__ == "__main__":
    print("=== Buscando 'Microservicio PEPS' en espacio EPA ===\n")
    results = search_page("Microservicio PEPS")
    if not results:
        print("No se encontraron páginas con ese título. Buscando 'PEPS'...")
        results = search_page("PEPS")

    print(f"Páginas encontradas ({len(results)}):")
    for r in results:
        print(f"  [{r['id']}] {r['title']}")

    if not results:
        print("No se encontraron páginas. Verifica el espacio y las credenciales.")
        sys.exit(1)

    # Mostrar árbol del primer resultado que sea "Microservicio PEPS" o el primero
    main_page = None
    for r in results:
        if "microservicio peps" in r["title"].lower() or r["title"].lower().strip() == "peps":
            main_page = r
            break
    if not main_page:
        main_page = results[0]

    print(f"\n=== Árbol de páginas desde [{main_page['id']}] {main_page['title']} ===\n")
    tree = print_tree(main_page["id"])
    flat = flatten_tree(tree)

    print(f"\n=== Resumen plano ({len(flat)} páginas) ===")
    for n in flat:
        prefix = "  " * n["level"]
        print(f"{prefix}[{n['id']}] {n['title']}")

    # Guardar como JSON para uso posterior
    output_file = "peps_tree.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"root": main_page, "tree": tree, "flat": flat}, f, ensure_ascii=False, indent=2)
    print(f"\nEstructura guardada en: {output_file}")
