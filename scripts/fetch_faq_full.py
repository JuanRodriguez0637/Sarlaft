"""
Script: fetch_faq_full.py
Fetches complete body and inline comments for "Preguntas frecuentes - Sarlaft".
"""
import requests
import json
import sys

sys.path.insert(0, r"d:\Sarlaft 4.0\scripts")
from confluence_config import HEADERS, BASE_URL

PAGE_ID = "1928167429"

# 1. Get full body
r = requests.get(
    f"{BASE_URL}/wiki/rest/api/content/{PAGE_ID}",
    headers=HEADERS,
    params={"expand": "body.storage,version,ancestors"},
    timeout=30
)
r.raise_for_status()
page = r.json()
body = page["body"]["storage"]["value"]
print("=== FULL BODY ===")
print(body)

# 2. Inline comments via CQL
r2 = requests.get(
    f"{BASE_URL}/wiki/rest/api/search",
    headers=HEADERS,
    params={"cql": f"parent = {PAGE_ID} AND type = comment", "limit": 50, "expand": "body.storage,version"},
    timeout=30
)
r2.raise_for_status()
comments = r2.json()
print(f"\n=== INLINE COMMENTS ({comments.get('totalSize', 0)}) ===")
for c in comments.get("results", []):
    cid = c["content"]["id"]
    cver = c["content"].get("version", {})
    print(f"  ID={cid} | By: {cver.get('by',{}).get('displayName','?')} | When: {cver.get('when','?')}")
    print(f"  Body: {c['content'].get('body',{}).get('storage',{}).get('value','')}")
