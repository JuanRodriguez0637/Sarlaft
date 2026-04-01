"""
Explorar la sección Front bajo Documentación Técnica en Confluence EPA
"""
import sys, json
sys.path.insert(0, 'scripts')
from confluence_config import HEADERS, BASE_URL
import requests

def search(cql, limit=50):
    r = requests.get(f'{BASE_URL}/wiki/rest/api/search', headers=HEADERS,
        params={'cql': cql, 'limit': limit, 'expand': 'ancestors'})
    r.raise_for_status()
    return r.json().get('results', [])

def get_children(page_id):
    r = requests.get(f'{BASE_URL}/wiki/rest/api/content/{page_id}/child/page',
        headers=HEADERS, params={'limit': 100, 'expand': 'version,ancestors'})
    r.raise_for_status()
    return r.json().get('results', [])

# 1. Find "Front" page
print("=== Searching for 'Front' page under EPA ===")
results = search('space="EPA" AND title="Front" AND type=page')
for r in results:
    c = r.get('content', {})
    ancestors = c.get('ancestors', [])
    anc_names = ' > '.join(a.get('title','') for a in ancestors)
    print(f"  ID: {c.get('id'):15}  title: {c.get('title')}  path: {anc_names}")

print()
if results:
    page_id = results[0]['content']['id']
    print(f"=== Children of page {page_id} ===")
    children = get_children(page_id)
    for ch in children:
        print(f"  ID: {ch['id']:15}  title: {ch['title']}")
        sub = get_children(ch['id'])
        for s in sub:
            print(f"    ID: {s['id']:15}  title: {s['title']}")
            sub2 = get_children(s['id'])
            for s2 in sub2:
                print(f"      ID: {s2['id']:15}  title: {s2['title']}")
