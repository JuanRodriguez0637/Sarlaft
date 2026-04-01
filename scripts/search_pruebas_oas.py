"""Search for Pruebas Orden Administrativa Soat page in Confluence"""
import sys
sys.path.insert(0, r"D:\Sarlaft 4.0\scripts")
from confluence_config import BASE_URL, HEADERS
import requests, json

def search(cql):
    r = requests.get(f"{BASE_URL}/wiki/rest/api/search",
                     params={"cql": cql, "limit": 50}, headers=HEADERS)
    r.raise_for_status()
    return r.json()

# Search by exact title
cql1 = 'space = "EPA" AND title = "Pruebas Orden Administrativa Soat / Frente Sarlaft" AND type = page'
data = search(cql1)
print(f"Exact match: {data.get('totalSize',0)}")
for x in data.get('results', []):
    print(f"  id={x['content']['id']}  title={x['content']['title']}")

# Search broader
cql2 = 'space = "EPA" AND title ~ "Pruebas Orden" AND type = page'
data2 = search(cql2)
print(f"\nBroad match 'Pruebas Orden': {data2.get('totalSize',0)}")
for x in data2.get('results', []):
    print(f"  id={x['content']['id']}  title={x['content']['title']}")

# Search broader
cql3 = 'space = "EPA" AND title ~ "Orden Administrativa" AND type = page'
data3 = search(cql3)
print(f"\nBroad match 'Orden Administrativa': {data3.get('totalSize',0)}")
for x in data3.get('results', []):
    print(f"  id={x['content']['id']}  title={x['content']['title']}")
