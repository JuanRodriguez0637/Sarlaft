"""
fix_docs_lint.py — Corrige errores de markdownlint en los .md de docs/
Reglas: MD009, MD010, MD022, MD032, MD034, MD041
"""
import os
import re
import glob

TARGET = r"D:\Sarlaft 4.0\docs\*.md"

# ---------------------------------------------------------------------------
def fix_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    lines = re.split(r"\r?\n", original)

    # ---- Detectar si el archivo está dentro de un bloque de código
    def in_code_fence(line_index, arr):
        count = 0
        for i in range(line_index):
            if re.match(r"^```", arr[i]):
                count += 1
        return count % 2 == 1

    # ---- 1. MD041: primera línea debe ser H1
    if lines and not re.match(r"^# ", lines[0]):
        # Inferir título desde nombre de archivo
        title = os.path.splitext(os.path.basename(path))[0].replace("_", " ")
        lines = [f"# {title}", ""] + lines

    # ---- 2. MD010: reemplazar hard tabs por espacios
    result = []
    for line in lines:
        result.append(line.replace("\t", "    "))
    lines = result

    # ---- 3. MD009: eliminar trailing spaces
    lines = [l.rstrip() for l in lines]

    # ---- 4. MD034: envolver bare URLs en angle brackets <url>
    # Sólo fuera de bloques de código y si no están ya en <url>, (url), o [text](url)
    URL_PAT = re.compile(r'https?://[^\s<>\)\]]+')
    result = []
    in_code = False
    for line in lines:
        if re.match(r"^```", line):
            in_code = not in_code
        if not in_code:
            def replacer(m, _line=line):
                start = m.start()
                char_before = _line[start - 1] if start > 0 else None
                # Ya está en (url) de un link markdown o en <url>
                if char_before in ('(', '<'):
                    return m.group(0)
                return f"<{m.group(0)}>"
            line = URL_PAT.sub(replacer, line)
        result.append(line)
    lines = result

    # ---- 4b. MD025: un solo H1 — cambiar H1 adicionales a H2 (idempotente)
    result = []
    first_h1 = False
    for line in lines:
        if re.match(r"^# ", line):
            if first_h1:
                line = "##" + line[1:]   # # Titulo → ## Titulo
            else:
                first_h1 = True
        result.append(line)
    lines = result

    # ---- 4c. heading-order: los encabezados solo pueden profundizar de 1 en 1
    # Usa un stack para calcular el nuevo nivel de cada encabezado
    def _compute_heading_remap(orig_levels):
        new_lvls = []
        stack = [(0, 0)]  # (nivel_original, nivel_nuevo)
        for orig in orig_levels:
            while stack and stack[-1][0] >= orig:
                stack.pop()
            if not stack:
                stack = [(0, 0)]
            parent_new = stack[-1][1]
            new_lvl = parent_new + 1
            new_lvls.append(new_lvl)
            stack.append((orig, new_lvl))
        return new_lvls

    in_code = False
    heading_positions = []  # (line_index, original_level, rest_of_heading_text)
    for i, line in enumerate(lines):
        if re.match(r"^```", line):
            in_code = not in_code
        if not in_code:
            m = re.match(r"^(#{1,6}) (.*)", line)
            if m:
                heading_positions.append((i, len(m.group(1)), m.group(2)))

    if heading_positions:
        orig_levels = [h[1] for h in heading_positions]
        new_levels = _compute_heading_remap(orig_levels)
        for (idx, orig_lvl, text), new_lvl in zip(heading_positions, new_levels):
            if new_lvl != orig_lvl:
                lines[idx] = "#" * new_lvl + " " + text

    # ---- 5. MD022: líneas en blanco alrededor de headings
    arr = lines[:]
    lines = []
    for i, line in enumerate(arr):
        if re.match(r"^#{1,6}\s", line) and i > 0:
            if lines and lines[-1] != "":
                lines.append("")
        lines.append(line)
        if re.match(r"^#{1,6}\s", line) and i + 1 < len(arr) and arr[i + 1] != "":
            lines.append("")

    # ---- 5b. MD029: normalizar prefijos de listas ordenadas a estilo 1/1/1
    # Detecta inicio de lista ordenada y renumera cada ítem a 1.
    result = []
    in_code = False
    in_ol = False
    for line in lines:
        if re.match(r"^```", line):
            in_code = not in_code
        if not in_code:
            ol_match = re.match(r"^(\s*)(\d+)(\. .+)", line)
            if ol_match:
                in_ol = True
                line = ol_match.group(1) + "1" + ol_match.group(3)
            else:
                in_ol = False
        result.append(line)
    lines = result

    # ---- 6. MD032: líneas en blanco alrededor de listas
    LIST_PAT = re.compile(r"^\s*[-*+]\s|^\s*[-*+]$|^\s*\d+\.\s")
    arr = lines[:]
    lines = []
    for i, line in enumerate(arr):
        is_list   = bool(LIST_PAT.match(line))
        prev_list  = i > 0 and bool(LIST_PAT.match(arr[i - 1]))
        prev_blank = i > 0 and arr[i - 1].strip() == ""
        if is_list and not prev_list and not prev_blank and i > 0:
            lines.append("")
        lines.append(line)
        if is_list and i + 1 < len(arr):
            next_list  = bool(LIST_PAT.match(arr[i + 1]))
            next_blank = arr[i + 1].strip() == ""
            if not next_list and not next_blank:
                lines.append("")

    # ---- 7b. MD037: eliminar espacios dentro de énfasis ** y _
    result = []
    in_code = False
    for line in lines:
        if re.match(r"^```", line):
            in_code = not in_code
        if not in_code:
            # ** texto ** → **texto**
            line = re.sub(r'\*\*\s+([^*\n]+?)\s+\*\*', r'**\1**', line)
            # * texto * → *texto*  (solo si no es lista)
            if not LIST_PAT.match(line):
                line = re.sub(r'(?<!\*)\*\s+([^*\n]+?)\s+\*(?!\*)', r'*\1*', line)
            # _ texto _ → _texto_
            line = re.sub(r'(?<![_\w])_\s+([^_\n]+?)\s+_(?![_\w])', r'_\1_', line)
        result.append(line)
    lines = result

    # ---- 7c. MD026: eliminar punto final en headings
    result = []
    for line in lines:
        if re.match(r"^#{1,6}\s", line):
            line = re.sub(r'\.\s*$', '', line)
        result.append(line)
    lines = result

    # ---- 7d. MD031: líneas en blanco alrededor de bloques de código
    arr = lines[:]
    lines = []
    for i, line in enumerate(arr):
        if re.match(r"^```", line):
            in_fence = sum(1 for j in range(i) if re.match(r"^```", arr[j])) % 2 == 0
            if in_fence:
                # Apertura: necesita línea en blanco antes
                if lines and lines[-1] != "":
                    lines.append("")
            else:
                # Cierre: necesita línea en blanco después
                lines.append(line)
                if i + 1 < len(arr) and arr[i + 1] != "":
                    lines.append("")
                continue
        lines.append(line)

    # ---- 7. MD012: máximo 1 línea en blanco consecutiva
    arr = lines[:]
    lines = []
    blank_count = 0
    for line in arr:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 1:
                lines.append("")
        else:
            blank_count = 0
            lines.append(line)

    # Eliminar blancos al final + asegurar salto final
    while lines and lines[-1].strip() == "":
        lines.pop()
    lines.append("")

    fixed_text = "\n".join(lines)
    if fixed_text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed_text)
        return True
    return False


# ---------------------------------------------------------------------------
def main():
    total = fixed = 0
    for filepath in sorted(glob.glob(TARGET)):
        total += 1
        changed = fix_file(filepath)
        status = "[FIXED]" if changed else "[OK]   "
        print(f"{status} {os.path.basename(filepath)}")
        if changed:
            fixed += 1
    print(f"\n=== Completado: {fixed}/{total} archivos corregidos ===")


if __name__ == "__main__":
    main()
