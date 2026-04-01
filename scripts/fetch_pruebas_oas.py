"""Extract full content and attachments for both Pruebas OAS pages"""
import sys, json
sys.path.insert(0, r"D:\Sarlaft 4.0\scripts")
from confluence_config import BASE_URL, HEADERS
import requests

def get_body(page_id):
    r = requests.get(f"{BASE_URL}/wiki/rest/api/content/{page_id}",
                     params={"expand": "body.storage,version,ancestors"}, headers=HEADERS)
    r.raise_for_status()
    d = r.json()
    return {"value": d["body"]["storage"]["value"], "page": d}

def get_attachments(page_id):
    r = requests.get(f"{BASE_URL}/wiki/rest/api/content/{page_id}/child/attachment",
                     params={"limit": 200}, headers=HEADERS)
    r.raise_for_status()
    return r.json()

def get_footer_comments(page_id):
    r = requests.get(f"{BASE_URL}/wiki/rest/api/content/{page_id}/child/comment",
                     params={"expand": "body.storage,version", "limit": 50}, headers=HEADERS)
    r.raise_for_status()
    return r.json()

def get_inline_comments(page_id):
    r = requests.get(f"{BASE_URL}/wiki/rest/api/search",
                     params={"cql": f"parent = {page_id} AND type = comment",
                             "limit": 50, "expand": "body.storage,version"},
                     headers=HEADERS)
    r.raise_for_status()
    return r.json()

for pid, label in [("3819175965", "PruebasOrdenAdministrativaSoat"), ("3826089992", "PruebasRegresionSARLAFT_OAS")]:
    print(f"\n{'='*60}")
    print(f"PAGE: {label} (id={pid})")
    
    body = get_body(pid)
    print(f"\n--- BODY (storage) ---")
    print(body.get('value', '')[:5000])
    
    atts = get_attachments(pid)
    print(f"\n--- ATTACHMENTS ({len(atts.get('results', []))}) ---")
    for a in atts.get('results', []):
        dl = a.get('_links', {}).get('download', '')
        print(f"  id={a['id']}  title={a['title']}  mediaType={a.get('metadata',{}).get('mediaType','')}  download={dl}")
    
    fc = get_footer_comments(pid)
    print(f"\n--- FOOTER COMMENTS ({fc.get('size', 0)}) ---")
    for c in fc.get('results', []):
        print(f"  id={c['id']}  by={c.get('version',{}).get('by',{}).get('displayName','')}  at={c.get('version',{}).get('when','')}")
        print(f"  body: {c.get('body',{}).get('storage',{}).get('value','')[:300]}")
    
    ic = get_inline_comments(pid)
    print(f"\n--- INLINE COMMENTS ({ic.get('totalSize',0)}) ---")
    for x in ic.get('results', []):
        print(f"  {x['content']['id']}")
