"""Explore hierarchy of Pruebas Orden Administrativa Soat pages"""
import sys
sys.path.insert(0, r"D:\Sarlaft 4.0\scripts")
from confluence_config import BASE_URL, HEADERS
import requests, json

def get_page(page_id, expand="version,ancestors,space"):
    r = requests.get(f"{BASE_URL}/wiki/rest/api/content/{page_id}",
                     params={"expand": expand}, headers=HEADERS)
    r.raise_for_status()
    return r.json()

def get_children(page_id):
    r = requests.get(f"{BASE_URL}/wiki/rest/api/search",
                     params={"cql": f"ancestor = {page_id} AND type = page",
                             "limit": 100, "expand": "version,ancestors"},
                     headers=HEADERS)
    r.raise_for_status()
    return r.json()

# Main page
main_id = "3819175965"
page = get_page(main_id)
print(f"=== MAIN PAGE ===")
print(f"ID: {page['id']}")
print(f"Title: {page['title']}")
print(f"Version: {page['version']['number']} by {page['version']['by']['displayName']} at {page['version']['when']}")
print(f"Space: {page['space']['key']}")
print(f"URL: {BASE_URL}/wiki{page['_links']['webui']}")
print(f"\nAncestors:")
for a in page.get('ancestors', []):
    print(f"  {a['id']} - {a['title']}")

print(f"\n=== CHILDREN of {main_id} ===")
children = get_children(main_id)
print(f"Total children: {children.get('totalSize', 0)}")
for x in children.get('results', []):
    c = x['content']
    print(f"  id={c['id']}  title={c['title']}")

# Second page
other_id = "3826089992"
page2 = get_page(other_id)
print(f"\n=== OTHER PAGE ===")
print(f"ID: {page2['id']}")
print(f"Title: {page2['title']}")
print(f"Version: {page2['version']['number']} by {page2['version']['by']['displayName']} at {page2['version']['when']}")
print(f"URL: {BASE_URL}/wiki{page2['_links']['webui']}")
print(f"\nAncestors:")
for a in page2.get('ancestors', []):
    print(f"  {a['id']} - {a['title']}")

print(f"\n=== CHILDREN of {other_id} ===")
children2 = get_children(other_id)
print(f"Total children: {children2.get('totalSize', 0)}")
for x in children2.get('results', []):
    c = x['content']
    print(f"  id={c['id']}  title={c['title']}")
