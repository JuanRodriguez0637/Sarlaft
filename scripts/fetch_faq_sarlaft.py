"""
Script: fetch_faq_sarlaft.py
Fetches page body, attachments, and comments for "Preguntas frecuentes - Sarlaft".
"""
import requests
import json
import sys

sys.path.insert(0, r"d:\Sarlaft 4.0\scripts")
from confluence_config import HEADERS, BASE_URL

PAGE_ID = "1928167429"

# 1. Get page metadata + body (storage)
r = requests.get(
    f"{BASE_URL}/wiki/rest/api/content/{PAGE_ID}",
    headers=HEADERS,
    params={"expand": "body.storage,version,ancestors,metadata.labels"},
    timeout=30
)
r.raise_for_status()
page = r.json()
print("=== PAGE METADATA ===")
print(f"Title: {page['title']}")
print(f"Version: {page['version']['number']} | By: {page['version']['by']['displayName']} | When: {page['version']['when']}")
print(f"Ancestors: {' > '.join(a['title'] for a in page.get('ancestors', []))}")
print(f"URL: {BASE_URL}/wiki{page['_links']['webui']}")

print("\n=== BODY (STORAGE) ===")
body = page["body"]["storage"]["value"]
print(body[:5000])
if len(body) > 5000:
    print(f"\n... [total len = {len(body)}] ...")

# 2. Get attachments
r2 = requests.get(
    f"{BASE_URL}/wiki/api/v2/pages/{PAGE_ID}/attachments",
    headers=HEADERS,
    params={"limit": 50},
    timeout=30
)
r2.raise_for_status()
att = r2.json()
print(f"\n=== ATTACHMENTS ({len(att.get('results', []))}) ===")
for a in att.get("results", []):
    print(f"  ID={a['id']} | {a['title']} | {a.get('mediaType','')} | {a.get('fileSize','')} bytes")
    print(f"    Download: {a.get('_links',{}).get('download','')}")

# 3. Get footer comments
r3 = requests.get(
    f"{BASE_URL}/wiki/api/v2/pages/{PAGE_ID}/footer-comments",
    headers=HEADERS,
    params={"body-format": "storage", "limit": 50},
    timeout=30
)
r3.raise_for_status()
comments = r3.json()
print(f"\n=== FOOTER COMMENTS ({len(comments.get('results', []))}) ===")
for c in comments.get("results", []):
    cid = c.get("id")
    print(f"  Comment ID={cid}")
    print(f"  Body: {c.get('body',{}).get('storage',{}).get('value','')[:500]}")
