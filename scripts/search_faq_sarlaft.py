"""
Script: search_faq_sarlaft.py
Searches for "Preguntas frecuentes - Sarlaft" page and its descendants.
"""
import requests
import json
import sys

sys.path.insert(0, r"d:\Sarlaft 4.0\scripts")
from confluence_config import HEADERS, BASE_URL

def search_page(cql):
    r = requests.get(
        f"{BASE_URL}/wiki/rest/api/search",
        headers=HEADERS,
        params={"cql": cql, "expand": "version,ancestors,space", "limit": 50},
        timeout=30
    )
    r.raise_for_status()
    return r.json()

def get_children(page_id):
    r = requests.get(
        f"{BASE_URL}/wiki/rest/api/search",
        headers=HEADERS,
        params={"cql": f"ancestor = {page_id} AND type = page", "expand": "version,ancestors", "limit": 100},
        timeout=30
    )
    r.raise_for_status()
    return r.json()

# 1. Find the main page
result = search_page('space = "EPA" AND title = "Preguntas frecuentes - Sarlaft" AND type = page')
print(f"=== MAIN PAGE SEARCH ({result.get('totalSize', 0)} results) ===")
for r in result.get("results", []):
    pid = r["content"]["id"]
    title = r["content"]["title"]
    ver = r["content"].get("version", {}).get("number", "?")
    by = r["content"].get("version", {}).get("by", {}).get("displayName", "?")
    when = r["content"].get("version", {}).get("when", "?")
    url = BASE_URL + "/wiki" + r.get("url", "")
    print(f"  ID={pid} | {title} | v{ver} | {by} | {when}")
    print(f"  URL: {url}")
    
    # 2. Get children
    children = get_children(pid)
    print(f"\n  === CHILDREN ({children.get('totalSize', 0)}) ===")
    for c in children.get("results", []):
        cid = c["content"]["id"]
        ctitle = c["content"]["title"]
        cv = c["content"].get("version", {}).get("number", "?")
        cby = c["content"].get("version", {}).get("by", {}).get("displayName", "?")
        cwhen = c["content"].get("version", {}).get("when", "?")
        curl = BASE_URL + "/wiki" + c.get("url", "")
        ancestors = " > ".join([a["title"] for a in c["content"].get("ancestors", [])])
        print(f"    ID={cid} | {ctitle} | v{cv} | {cby} | {cwhen}")
        print(f"    Ancestors: {ancestors}")
        print(f"    URL: {curl}")
        
        # 3. Sub-children
        sub = get_children(cid)
        if sub.get("totalSize", 0) > 0:
            print(f"    --- Sub-children ({sub.get('totalSize')}) ---")
            for s in sub.get("results", []):
                sid = s["content"]["id"]
                stitle = s["content"]["title"]
                sv = s["content"].get("version", {}).get("number", "?")
                sby = s["content"].get("version", {}).get("by", {}).get("displayName", "?")
                swhen = s["content"].get("version", {}).get("when", "?")
                print(f"      ID={sid} | {stitle} | v{sv} | {sby} | {swhen}")
