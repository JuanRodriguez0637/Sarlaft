#!/usr/bin/env python3
"""Extrae contenido, comentarios y adjuntos de las páginas de Configuración Plataforma Base Sarlaft."""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from confluence_config import BASE_URL, HEADERS
import requests


def get_page(pid):
    r = requests.get(
        f"{BASE_URL}/wiki/rest/api/content/{pid}",
        headers=HEADERS,
        params={"expand": "body.storage,version,ancestors"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def get_comments(pid):
    r = requests.get(
        f"{BASE_URL}/wiki/rest/api/content/{pid}/child/comment",
        headers=HEADERS,
        params={"depth": "all", "expand": "body.storage,version", "limit": 50},
        timeout=30,
    )
    r.raise_for_status()
    return r.json().get("results", [])


def get_attachments(pid):
    r = requests.get(
        f"{BASE_URL}/wiki/rest/api/content/{pid}/child/attachment",
        headers=HEADERS,
        params={"limit": 100, "expand": "version"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json().get("results", [])


pages = ["2389114940", "2388918331", "1880817708"]
result = {}

for pid in pages:
    p = get_page(pid)
    c = get_comments(pid)
    a = get_attachments(pid)
    result[pid] = {
        "id": pid,
        "title": p["title"],
        "version": p["version"]["number"],
        "author": p["version"]["by"]["displayName"],
        "date": p["version"]["when"],
        "webui": p["_links"]["webui"],
        "body": p["body"]["storage"]["value"],
        "comments": [
            {
                "id": x["id"],
                "author": x["version"]["by"]["displayName"],
                "date": x["version"]["when"],
                "body": x["body"]["storage"]["value"],
            }
            for x in c
        ],
        "attachments": [
            {
                "id": x["id"],
                "title": x["title"],
                "download": x["_links"].get("download", ""),
            }
            for x in a
        ],
    }
    print(
        f"[{pid}] {p['title']} | v{p['version']['number']} | {len(c)} comments | {len(a)} attachments"
    )

out = Path(__file__).parent / "config_plataforma_data.json"
out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print("Saved:", out)
