#!/usr/bin/env python3
"""Revisa el contenido del JSON extraído."""
import json
from pathlib import Path

data = json.loads(Path("scripts/config_plataforma_data.json").read_text(encoding="utf-8"))
for pid, p in data.items():
    title = p["title"]
    atts = p["attachments"]
    body = p["body"]
    print(f"=== [{pid}] {title} ===")
    print(f"  Attachments ({len(atts)}):")
    for a in atts:
        print(f"    - {a['title']} | {a['download']}")
    print(f"  Body length: {len(body)}")
    print(f"  Body preview:\n{body[:800]}")
    print()
