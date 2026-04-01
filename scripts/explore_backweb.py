"""Mapea recursivamente el árbol de páginas de Microservicio Backweb."""
import requests, json
from confluence_config import BASE_URL, HEADERS

ROOT_ID = "2398027809"

def get_children(page_id, indent=0):
    cql = f'ancestor = {page_id} AND type = page'
    r = requests.get(
        BASE_URL+'/wiki/rest/api/search',
        headers=HEADERS,
        params={'cql': cql, 'limit': 50, 'expand': 'ancestors'}
    )
    results = r.json().get('results', [])
    # Solo hijos directos
    direct = [x for x in results if x['content'].get('ancestors') and
              x['content']['ancestors'][-1]['id'] == page_id]
    if not direct:
        # Fallback sin filtro de ancestro directo
        direct = results
    return direct

def traverse(page_id, title, indent=0):
    prefix = '  ' * indent
    print(f'{prefix}[{page_id}] {title}')
    children = get_children(page_id)
    for c in children:
        traverse(c['content']['id'], c['content']['title'], indent+1)

# Primero obtener el titulo real del root
r = requests.get(BASE_URL+f'/wiki/rest/api/content/{ROOT_ID}', headers=HEADERS, params={'expand': 'version'})
root = r.json()
print('=== ÁRBOL DE PÁGINAS ===')
traverse(ROOT_ID, root.get('title', 'Microservicio Backweb'))
