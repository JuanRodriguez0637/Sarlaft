"""
fix_seccion_links.py — Corrige el link ./index.md → ../index.md en todos los
index.md que están dentro de subdirectorios (bajo docs/).

Regla:
  - Archivos afectados: cualquier index.md en docs/<Seccion>/<SubDir>/index.md
    (profundidad ≥ 2 relativa a docs/).
  - NO se tocan: los index.md de primer nivel (docs/<Seccion>/index.md), ya que
    allí ./index.md apunta a sí mismo intencionalmente (no hay padre que navegar).
  - NO se tocan: páginas normales (.md que no son index.md) porque su ./index.md
    sí apunta correctamente al index de su subcarpeta.
  - Solo se modifica la línea que contiene **Sección:** [...](./index.md).
"""

import os
import re
from pathlib import Path

DOCS_ROOT = Path(r"D:\Sarlaft 4.0\docs")

SECCION_RE = re.compile(r'(\*\*Sección:\*\*.*?\()\./index\.md(\))', re.I)

fixed_files = []
skipped_files = []

for root, dirs, files in os.walk(DOCS_ROOT):
    # Skip non-index.md files
    if "index.md" not in files:
        continue

    index_path = Path(root) / "index.md"

    # Calculate depth relative to DOCS_ROOT
    try:
        rel = index_path.relative_to(DOCS_ROOT)
    except ValueError:
        continue

    # rel.parts = ('Seccion', 'SubDir', 'index.md')
    # depth of the *directory* = len(parts) - 1  (last part is the filename)
    depth = len(rel.parts) - 1  # number of directory levels under docs/

    if depth < 2:
        # Top-level section index (docs/Section/index.md) — skip
        skipped_files.append(str(rel))
        continue

    # Read file
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "(./index.md)" not in content:
        print(f"  NO CHANGE (no ./index.md pattern): {rel}")
        continue

    # Check how many leading ../ we need: always 1 (we go one level up)
    new_content = SECCION_RE.sub(r'\1../index.md\2', content)

    if new_content == content:
        print(f"  NO CHANGE (regex no match):         {rel}")
        continue

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    fixed_files.append(str(rel))
    print(f"  FIXED: {rel}")

print()
print(f"Total fixed:   {len(fixed_files)}")
print(f"Total skipped (top-level): {len(skipped_files)}")
for s in skipped_files:
    print(f"  (kept) {s}")
