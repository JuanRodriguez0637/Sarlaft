"""Muestra el árbol real usando /child/page para hijos directos."""
import requests, json
from confluence_config import BASE_URL, HEADERS

def get_direct_children(page_id):
    r = requests.get(
        BASE_URL+f'/wiki/rest/api/content/{page_id}/child/page',
        headers=HEADERS,
        params={'limit': 50, 'expand': 'version'}
    )
    return r.json().get('results', [])

def traverse(page_id, title, indent=0):
    prefix = '  ' * indent
    print(f'{prefix}[{page_id}] {title}')
    children = get_direct_children(page_id)
    for c in children:
        traverse(c['id'], c['title'], indent+1)

ROOT_ID = "2398027809"
r = requests.get(BASE_URL+f'/wiki/rest/api/content/{ROOT_ID}', headers=HEADERS, params={'expand': 'version'})
root = r.json()
print('=== ÁRBOL DIRECTO ===')
traverse(ROOT_ID, root.get('title', 'Microservicio Backweb'))
