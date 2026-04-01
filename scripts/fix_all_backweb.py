"""
fix_all_backweb.py — Corrige TODOS los problemas de lint en docs/MicroservicioBackweb/
También puede usarse para cualquier sección pasando la ruta como argumento:
  python fix_all_backweb.py "D:\\Sarlaft 4.0\\docs\\MicroservicioSarlaftAPI"

Problemas a corregir:
  MD032 - broken list items: solitario "-" seguido de contenido en linea aparte
  MD040 - code fences sin lenguaje
  MD047 - sin trailing newline
  MD010 - hard tabs
  MD012 - multiples lineas en blanco consecutivas
"""
import re
import os
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else r"D:\Sarlaft 4.0\docs\MicroservicioBackweb"

def fix_file(path):
    with open(path, "rb") as f:
        raw = f.read()
    # Normalize line endings to LF
    c = raw.replace(b"\r\n", b"\n").decode("utf-8")
    original = c

    # ── MD010: tabs → 4 espacios (solo fuera de code fences) ─────────────
    # Reemplazar tabs dentro de code fences también es correcto (ya estan en code)
    c = c.replace("\t", "    ")

    # ── MD032: broken list items ──────────────────────────────────────────
    # Patron: linea que es solo "-\n" seguida de contenido (no codigo, no otra lista)
    # Convertir "-\n<texto>" a "- <texto>"
    c = re.sub(r"\n-\n([^\n-])", lambda m: "\n- " + m.group(1), c)
    # Limpiar items que quedaron como "- \n" (dash space newline) por el replace anterior
    # y que ahora generan "- -" o similares - revisar multiples pasadas
    for _ in range(5):
        c = re.sub(r"\n-\n([^\n-])", lambda m: "\n- " + m.group(1), c)

    # ── MD040: code fences sin lenguaje ───────────────────────────────────
    # Detectar bloques ``` sin lenguaje e inferir por contenido
    def add_language(m):
        content = m.group(1)
        stripped = content.strip()
        # Inferir lenguaje
        if re.search(r"^\s*(package|import|@|public\s+(class|interface)|protected|private)", stripped, re.M):
            lang = "java"
        elif re.search(r"^\s*(spring:|azure:|server:|logging:|management:)", stripped, re.M):
            lang = "yaml"
        elif stripped.startswith("{") or stripped.startswith("["):
            lang = "json"
        elif re.search(r"^\s*(implementation|dependencies|plugins|apply plugin)", stripped, re.M):
            lang = "groovy"
        elif re.search(r"SELECT|INSERT|UPDATE|DELETE|CREATE TABLE", stripped, re.I):
            lang = "sql"
        elif re.search(r"^(GET|POST|PUT|DELETE|PATCH)\s+/", stripped, re.M):
            lang = "http"
        else:
            lang = "text"
        return f"```{lang}\n{content}```"

    c = re.sub(r"```\n(.*?)```", add_language, c, flags=re.S)

    # ── MD012: múltiples líneas en blanco consecutivas → máximo 1 ────────
    c = re.sub(r"\n{3,}", "\n\n", c)

    # ── MD047: trailing newline ───────────────────────────────────────────
    if not c.endswith("\n"):
        c += "\n"

    if c != original.replace("\t", "    "):
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(c)
        return True
    return False


changed = []
for dirpath, _, files in os.walk(ROOT):
    for fname in sorted(files):
        if fname.endswith(".md"):
            fpath = os.path.join(dirpath, fname)
            if fix_file(fpath):
                rel = os.path.relpath(fpath, ROOT)
                changed.append(rel)
                print(f"  FIXED: {rel}")
            else:
                rel = os.path.relpath(fpath, ROOT)
                print(f"  OK:    {rel}")

print(f"\nTotal modificados: {len(changed)}")
