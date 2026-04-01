"""
confluence_explorer.py — Explorar páginas de Confluence
Uso:
  python confluence_explorer.py [pageId] [action]
  action: children | content | attachments | tree   (default: children)
  pageId default: 1804697669 (Diseño - Arquitectura)
"""
import sys
import requests
from confluence_config import BASE_URL, HEADERS


def get_children(page_id: str) -> list:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/children?limit=50"
    return requests.get(url, headers=HEADERS).json().get("results", [])


def get_page(page_id: str) -> dict:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}?body-format=storage"
    return requests.get(url, headers=HEADERS).json()


def get_attachments(page_id: str) -> list:
    url = f"{BASE_URL}/wiki/api/v2/pages/{page_id}/attachments?limit=50"
    return requests.get(url, headers=HEADERS).json().get("results", [])


def print_tree(page_id: str, indent: str = "") -> None:
    page = requests.get(f"{BASE_URL}/wiki/api/v2/pages/{page_id}", headers=HEADERS).json()
    print(f"{indent}[{page_id}] {page.get('title', '?')}")
    for child in get_children(page_id):
        print_tree(child["id"], indent + "  ")


def main():
    page_id = sys.argv[1] if len(sys.argv) > 1 else "1804697669"
    action  = sys.argv[2] if len(sys.argv) > 2 else "children"

    if action == "children":
        for child in get_children(page_id):
            print(f"{child['id']} | {child['title']}")

    elif action == "content":
        page = get_page(page_id)
        print(f"TITULO: {page.get('title')}")
        print("---BODY---")
        print(page.get("body", {}).get("storage", {}).get("value", ""))

    elif action == "attachments":
        for a in get_attachments(page_id):
            dl = a.get("_links", {}).get("download", "")
            print(f"{a['id']} | {a['title']} | {a.get('mediaType','')} | {dl}")

    elif action == "tree":
        print_tree(page_id)

    else:
        print(f"Acción desconocida: {action}. Usa: children | content | attachments | tree")


if __name__ == "__main__":
    main()
