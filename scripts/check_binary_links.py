"""
Verifica que todos los enlaces a archivos binarios (PDF, Word, Excel, imágenes)
en los archivos .md de docs/ apunten a archivos que realmente existen.
"""
import os
import re
import urllib.parse

DOCS_BASE = r"D:\Sarlaft 4.0\docs"
BIN_EXTS = {".pdf", ".docx", ".doc", ".xlsx", ".xls", ".xlsm",
            ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg",
            ".pptx", ".ppt"}
LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)|\[[^\]]*\]\(([^)]+)\)")


def check_links():
    ok_list = []
    broken_list = []

    for root, dirs, files in os.walk(DOCS_BASE):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            md_path = os.path.join(root, fname)
            with open(md_path, encoding="utf-8", errors="replace") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, 1):
                for m in LINK_RE.finditer(line):
                    raw = m.group(1) or m.group(2)
                    if not raw:
                        continue
                    if raw.startswith("http") or raw.startswith("#") or raw.startswith("mailto:"):
                        continue
                    path_part = raw.split("#")[0].split("?")[0]
                    ext = os.path.splitext(path_part)[1].lower()
                    if ext not in BIN_EXTS:
                        continue
                    decoded = urllib.parse.unquote(path_part)
                    abs_path = os.path.normpath(os.path.join(root, decoded))
                    entry = {
                        "md": md_path.replace(DOCS_BASE + os.sep, ""),
                        "line": i,
                        "link": raw,
                        "abs": abs_path,
                    }
                    if os.path.exists(abs_path):
                        ok_list.append(entry)
                    else:
                        broken_list.append(entry)

    total = len(ok_list) + len(broken_list)
    print(f"Total enlaces binarios encontrados: {total}")
    print(f"OK:    {len(ok_list)}")
    print(f"ROTOS: {len(broken_list)}")

    if broken_list:
        print("\n=== ENLACES ROTOS ===\n")
        for e in broken_list:
            print(f"  Archivo: {e['md']}  (línea {e['line']})")
            print(f"  Enlace:  {e['link']}")
            print(f"  Ruta:    {e['abs']}")
            print()
    else:
        print("\nTodos los enlaces binarios funcionan correctamente.")

    return broken_list


if __name__ == "__main__":
    check_links()
