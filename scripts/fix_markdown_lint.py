"""
fix_markdown_lint.py — Corrige errores de markdownlint en los .md generados.
Reglas: MD025, MD009, MD012, MD032, MD037, MD022, MD040, MD004, MD018 + limpieza de artefactos.
"""
import os
import re
import glob

TARGETS = [
    r"D:\Sarlaft 4.0\docs\Diseño - Arquitectura\*.md",
    r"D:\Sarlaft 4.0\docs\Diseño - Arquitectura\referencias\*.md",
    r"D:\Sarlaft 4.0\docs\Motor de Evaluación\*.md",
    r"D:\Sarlaft 4.0\docs\Motor de Evaluación\**\*.md",
]

# ---------------------------------------------------------------------------
def fix_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    lines = re.split(r"\r?\n", original)

    # ---- 1. MD025: demotar headings del body (+1 nivel, máx H6)
    result = []
    header_done = False
    for i, line in enumerate(lines):
        if i == 0:
            result.append(line)
            continue
        if not header_done:
            if re.match(r"^(>|##|---|\s*$)", line):
                result.append(line)
                continue
            else:
                header_done = True
        m = re.match(r"^(#{1,5})(\s.*)$", line)
        if m:
            result.append("#" * (len(m.group(1)) + 1) + m.group(2))
        elif re.match(r"^#{6,}\s", line):
            result.append(re.sub(r"^#{6,}(\s)", r"######\1", line))
        else:
            result.append(line)
    lines = result

    # ---- 2. heading-order: no saltar niveles
    fixed = []
    last_level = 1
    for line in lines:
        m = re.match(r"^(#{1,6})\s", line)
        if m:
            level = len(m.group(1))
            if level > last_level + 1:
                level = last_level + 1
            last_level = level
            text = re.sub(r"^#{1,6}\s+", "", line)
            fixed.append(f"{'#' * level} {text}")
        else:
            fixed.append(line)
    lines = fixed

    # ---- 2b. Fusionar ítems de lista vacíos con la línea siguiente
    # Patrón generado por html_to_md cuando <li> contiene bloques: "- " sola
    merged: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'^(\s*)-\s*$', line) and i + 1 < len(lines):
            next_line = lines[i + 1]
            indent = re.match(r'^(\s*)', line).group(1)
            if next_line.strip() == "":
                # ítem vacío seguido de blanco → descartar el guion
                i += 1
                continue
            elif re.match(r'^\s*[-*+]\s|^\s*\d+\.\s', next_line):
                # siguiente es otro ítem → descartar este guion vacío
                i += 1
                continue
            else:
                # fusionar: "- " + contenido siguiente
                merged.append(f"{indent}- {next_line.strip()}")
                i += 2
                continue
        merged.append(line)
        i += 1
    lines = merged

    # ---- 2c. MD010: reemplazar hard tabs por 4 espacios
    lines = [l.replace('\t', '    ') for l in lines]

    # ---- 3. MD009: eliminar trailing spaces
    lines = [l.rstrip() for l in lines]

    # ---- 4. MD012: máximo 1 línea en blanco consecutiva
    final: list[str] = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 1:
                final.append("")
        else:
            blank_count = 0
            final.append(line)

    # ---- 5. MD032: líneas en blanco alrededor de listas
    LIST_PAT = re.compile(r"^\s*[-*+]\s|^\s*[-*+]$|^\s*\d+\.\s")
    arr = final[:]
    final = []
    for i, line in enumerate(arr):
        is_list  = bool(LIST_PAT.match(line))
        prev_list  = i > 0 and bool(LIST_PAT.match(arr[i - 1]))
        prev_blank = i > 0 and arr[i - 1].strip() == ""
        if is_list and not prev_list and not prev_blank and i > 0:
            final.append("")
        final.append(line)
        if is_list and i + 1 < len(arr):
            next_list  = bool(LIST_PAT.match(arr[i + 1]))
            next_blank = arr[i + 1].strip() == ""
            if not next_list and not next_blank:
                final.append("")

    # ---- 6. MD037: espacios dentro de énfasis + énfasis vacíos + headings vacíos
    in_code = False
    result = []
    for line in final:
        if re.match(r"^```", line):
            in_code = not in_code
        if not in_code:
            line = re.sub(r"\*\*\s+([^*]+?)\s+\*\*", r"**\1**", line)
            line = re.sub(r"\*\*\s+([^*]+?)\*\*",    r"**\1**", line)
            line = re.sub(r"\*\*([^*]+?)\s+\*\*",    r"**\1**", line)
            line = re.sub(r"\*\*\s*\*\*", "", line)
        if re.match(r"^#{1,6}\s*$", line):
            continue
        result.append(line)
    final = result

    # ---- 7. MD022: líneas en blanco alrededor de headings
    arr = final[:]
    final = []
    for i, line in enumerate(arr):
        if re.match(r"^#{1,6}\s", line) and i > 0:
            if final and final[-1] != "":
                final.append("")
        final.append(line)
        if re.match(r"^#{1,6}\s", line) and i + 1 < len(arr) and arr[i + 1] != "":
            final.append("")

    # ---- 8. MD040: bloques de código sin lenguaje → ```text
    arr = final[:]
    final = []
    in_fence = False
    for line in arr:
        if not in_fence and re.match(r"^```\s*$", line):
            final.append("```text")
            in_fence = True
        elif in_fence and re.match(r"^```\s*$", line):
            final.append("```")
            in_fence = False
        elif re.match(r"^```\S", line):
            final.append(line)
            in_fence = True
        elif in_fence and re.match(r"^```", line):
            final.append(line)
            in_fence = False
        else:
            final.append(line)

    # ---- 8b. MD056: normalizar número de columnas en tablas
    # Para cada bloque de tabla, todas las filas deben tener el mismo número de celdas.
    def _fix_table_columns(lines_in: list[str]) -> list[str]:
        out: list[str] = []
        i = 0
        while i < len(lines_in):
            line = lines_in[i]
            # Detectar inicio de tabla (línea con |)
            if re.match(r'\s*\|', line):
                block: list[str] = []
                while i < len(lines_in) and (re.match(r'\s*\|', lines_in[i]) or
                        (block and re.match(r'\s*[-|: ]+$', lines_in[i]))):
                    block.append(lines_in[i])
                    i += 1
                # Contar columnas por fila
                def count_cols(row: str) -> int:
                    # cuenta las celdas entre pipes
                    s = row.strip()
                    if s.startswith('|'): s = s[1:]
                    if s.endswith('|'): s = s[:-1]
                    return len(s.split('|'))
                if block:
                    max_cols = max(count_cols(r) for r in block)
                    fixed_block: list[str] = []
                    for row in block:
                        cols = count_cols(row)
                        if cols < max_cols:
                            s = row.rstrip()
                            # Añadir celdas vacías al final SIN quitar el | de cierre
                            s += ' |' * (max_cols - cols)
                            row = s
                        fixed_block.append(row)
                    out.extend(fixed_block)
                continue
            out.append(line)
            i += 1
        return out
    final = _fix_table_columns(final)

    # ---- 8c. MD058: líneas en blanco alrededor de tablas
    TABLE_PAT = re.compile(r'^\s*\|')
    arr = final[:]
    final = []
    for i, line in enumerate(arr):
        is_table  = bool(TABLE_PAT.match(line))
        prev_table = i > 0 and bool(TABLE_PAT.match(arr[i - 1]))
        prev_blank = i > 0 and arr[i - 1].strip() == ''
        if is_table and not prev_table and not prev_blank and i > 0:
            final.append('')
        final.append(line)
        if is_table and i + 1 < len(arr):
            next_table = bool(TABLE_PAT.match(arr[i + 1]))
            next_blank = arr[i + 1].strip() == ''
            if not next_table and not next_blank:
                final.append('')

    # ---- 9. MD004: * items → - items
    final = [re.sub(r"^(\s*)\* ", r"\1- ", l) for l in final]

    # ---- 10. MD018: espacio tras # + quitar negrita envuelta en heading
    result = []
    for line in final:
        line = re.sub(r"^(#{1,6})([^ #])", r"\1 \2", line)
        line = re.sub(r"^(#{1,6} )\*\*(.+?)\*\*\s*$", r"\1\2", line)
        result.append(line)
    final = result

    # ---- 11. Corregir }```n al final de línea
    result = []
    for line in final:
        if re.search(r"^(.*\S)```[a-z]*$", line) and not re.match(r"^```", line):
            content = re.sub(r"```[a-z]*$", "", line)
            result.append(content)
            result.append("```")
        else:
            result.append(line)
    final = result

    # ---- 12. MD012 segunda pasada
    arr = final[:]
    final = []
    blank_count = 0
    for line in arr:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 1:
                final.append("")
        else:
            blank_count = 0
            final.append(line)

    # Eliminar blancos al final + asegurar salto final
    while final and final[-1].strip() == "":
        final.pop()
    final.append("")

    fixed_text = "\n".join(final)
    if fixed_text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed_text)
        return True
    return False


# ---------------------------------------------------------------------------
def main():
    total = fixed = 0
    seen: set[str] = set()
    for pattern in TARGETS:
        recursive = "**" in pattern
        for filepath in sorted(glob.glob(pattern, recursive=recursive)):
            filepath = os.path.normpath(filepath)
            if filepath in seen:
                continue
            seen.add(filepath)
            total += 1
            changed = fix_file(filepath)
            status = "[FIXED]" if changed else "[OK]   "
            rel = os.path.relpath(filepath, r"D:\Sarlaft 4.0\docs")
            print(f"{status} {rel}")
            if changed:
                fixed += 1
    print(f"\n=== Completado: {fixed}/{total} archivos corregidos ===")


if __name__ == "__main__":
    main()
