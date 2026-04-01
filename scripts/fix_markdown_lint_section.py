"""
fix_markdown_lint_section.py — Corrige problemas de lint en cualquier sección de docs/.
Uso:
  python fix_markdown_lint_section.py "D:\\Sarlaft 4.0\\docs\\MicroservicioSarlaftAPI"

Problemas corregidos:
  MD009 - trailing spaces (1 espacio final → 0)
  MD010 - hard tabs → 4 espacios
  MD012 - múltiples líneas en blanco consecutivas → máximo 1
  MD032 - broken list items ("-" solitario seguido de contenido en línea aparte)
  MD034 - bare URLs/emails → envueltos en < >
  MD040 - code fences sin lenguaje (infiere java/yaml/json/groovy/sql/http/text)
  MD047 - sin trailing newline
  MD056 - filas de tabla con menos columnas que el encabezado → rellena con celdas vacías
  MD060 - separadores de tabla sin espacios (|---|) → (| --- |)
"""
import re
import os
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else r"D:\Sarlaft 4.0\docs\MicroservicioBackweb"


# ── Procesamiento por líneas (respeta code fences) ───────────────────────────

def process_lines(lines: list[str]) -> list[str]:
    """Aplica MD009, MD034, MD056, MD060 línea por línea, ignorando bloques de código."""
    in_fence = False
    fence_marker = ""
    result = []

    # Primero detectamos el número de columnas de la tabla activa (para MD056)
    # Necesitamos dos pasadas: una para identificar tablas, otra para parchearlas
    # Hacemos una sola pasada guardando tabla activa
    active_header_cols = 0

    for line in lines:
        stripped = line.rstrip("\n")

        # ── Detectar inicio/fin de code fence ────────────────────────────
        fence_match = re.match(r'^(`{3,}|~{3,})', stripped)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = marker
                result.append(line)
                continue
            elif stripped.startswith(fence_marker):
                in_fence = False
                fence_marker = ""
                result.append(line)
                continue

        if in_fence:
            result.append(line)
            continue

        # ── MD060: separadores de tabla |---|---| → | --- | --- | ────────
        if is_separator_row(stripped):
            stripped = fix_separator_spacing(stripped)
            # NO reset active_header_cols — el separador no cambia el conteo de columnas del encabezado
            result.append(stripped + "\n")
            continue

        # ── Detectar encabezado de tabla para MD056 ───────────────────────
        if is_table_row(stripped):
            cols = count_table_cols(stripped)
            if active_header_cols == 0:
                # Primera fila = encabezado — fijar número de columnas
                active_header_cols = cols
            else:
                # Fila de datos: rellenar si tiene menos columnas (MD056)
                if cols < active_header_cols:
                    stripped = pad_table_row(stripped, active_header_cols)
            # MD034: bare URLs dentro de celdas de tabla
            stripped = fix_bare_urls(stripped)
            # MD009: strip trailing space
            stripped = stripped.rstrip()
            result.append(stripped + "\n")
            continue
        else:
            # Salimos de la tabla
            active_header_cols = 0

        # ── MD009: eliminar espacios finales (excepto 2 que forman <br>) ──
        # Marcamos 2 espacios finales como hardbreak — los preservamos
        if stripped.endswith("  "):
            # Preserve intentional double-space line breaks
            pass
        else:
            stripped = stripped.rstrip()

        # ── MD034: bare URLs/emails → <url> ──────────────────────────────
        stripped = fix_bare_urls(stripped)

        result.append(stripped + "\n")

    return result


def is_separator_row(line: str) -> bool:
    """True si la línea es un separador de tabla markdown (|---|---|)."""
    s = line.strip()
    if not s.startswith("|") and not s.endswith("|"):
        return False
    cells = re.split(r'\|', s.strip("|"))
    if not cells:
        return False
    return all(re.match(r'^\s*:?-+:?\s*$', c) for c in cells if c.strip())


def fix_separator_spacing(line: str) -> str:
    """MD060: |---|:---| → | --- | :--- |"""
    s = line.strip()
    cells = s.strip("|").split("|")
    fixed = []
    for cell in cells:
        c = cell.strip()
        if re.match(r'^:?-+:?$', c):
            fixed.append(f" {c} ")
        else:
            fixed.append(cell)
    return "|" + "|".join(fixed) + "|"


def is_table_row(line: str) -> bool:
    """True si la línea parece una fila de tabla markdown (empieza con |)."""
    return line.strip().startswith("|") and "|" in line.strip()[1:]


def count_table_cols(line: str) -> int:
    s = line.strip().strip("|")
    return len(s.split("|"))


def pad_table_row(line: str, expected_cols: int) -> str:
    """MD056: añade celdas vacías hasta alcanzar expected_cols."""
    s = line.strip()
    # Quitar | inicial y final para contar
    inner = s.strip("|")
    cells = inner.split("|")
    while len(cells) < expected_cols:
        cells.append("  ")
    return "| " + " | ".join(c if c.strip() else "  " for c in cells) + " |"


def fix_bare_urls(line: str) -> str:
    """MD034: envuelve URLs/emails desnudos en < >."""
    # No tocar líneas que ya son pure link definitions [text]: url
    if re.match(r'^\s*\[.*?\]:\s*https?://', line):
        return line

    result = []
    i = 0
    while i < len(line):
        ch = line[i]

        # Code span: saltar
        if ch == '`':
            j = line.find('`', i + 1)
            end = j + 1 if j != -1 else len(line)
            result.append(line[i:end])
            i = end
            continue

        # Ya envuelto <...>: saltar
        if ch == '<':
            j = line.find('>', i + 1)
            if j != -1:
                result.append(line[i:j + 1])
                i = j + 1
                continue

        # Markdown link [text](url): saltar el ](url) completo
        if ch == '[':
            close = line.find('](', i + 1)
            if close != -1:
                paren_end = line.find(')', close + 2)
                if paren_end != -1:
                    result.append(line[i:paren_end + 1])
                    i = paren_end + 1
                    continue

        # URL desnuda http(s)://
        if line[i:i+7] in ('http://', 'https:/'):
            m = re.match(r'https?://[^\s<>()\[\]`"\']+', line[i:])
            if m:
                url = m.group(0)
                # Strip trailing punctuation that is likely not part of the URL
                url = url.rstrip('.,;:!?)')
                result.append(f'<{url}>')
                i += len(m.group(0))
                # Re-add any stripped trailing chars
                stripped_chars = m.group(0)[len(url):]
                result.append(stripped_chars)
                continue

        # Email desnudo (solo palabras@dominio.tld que no estén ya en <>)
        email_m = re.match(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', line[i:])
        if email_m and i > 0 and line[i - 1] not in ('<', '(', '[', '"', "'"):
            email = email_m.group(0)
            result.append(f'<{email}>')
            i += len(email)
            continue

        result.append(ch)
        i += 1

    return ''.join(result)


# ── Procesamiento completo de un archivo ─────────────────────────────────────

def fix_file(path: str) -> bool:
    with open(path, "rb") as f:
        raw = f.read()
    c = raw.replace(b"\r\n", b"\n").decode("utf-8")
    original = c

    # ── MD010: tabs → 4 espacios ─────────────────────────────────────────
    c = c.replace("\t", "    ")

    # ── MD032: broken list items ("-" solitario → "- contenido") ─────────
    for _ in range(5):
        c = re.sub(r"\n-\n([^\n\-])", lambda m: "\n- " + m.group(1), c)

    # ── MD040: code fences sin lenguaje ───────────────────────────────────
    def add_language(m):
        content = m.group(1)
        stripped = content.strip()
        if re.search(r"^\s*(package|import|@|public\s+(class|interface)|protected|private)", stripped, re.M):
            lang = "java"
        elif re.search(r"^\s*(spring:|azure:|server:|logging:|management:|app:)", stripped, re.M):
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

    # ── MD012: máximo 1 línea en blanco consecutiva ───────────────────────
    c = re.sub(r"\n{3,}", "\n\n", c)

    # ── Procesamiento línea por línea (MD009, MD034, MD056, MD060) ────────
    lines = c.splitlines(keepends=True)
    # Ensure last line ends with \n for splitlines to work correctly
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    lines = process_lines(lines)
    c = "".join(lines)

    # ── MD012: segunda pasada tras ediciones por línea ─────────────────────
    c = re.sub(r"\n{3,}", "\n\n", c)

    # ── MD047: exactamente un newline al final ────────────────────────────
    c = c.rstrip("\n") + "\n"

    if c != original:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(c)
        return True
    return False


# ── Main ─────────────────────────────────────────────────────────────────────

changed = []
for dirpath, _, files in os.walk(ROOT):
    for fname in sorted(files):
        if fname.endswith(".md"):
            fpath = os.path.join(dirpath, fname)
            try:
                if fix_file(fpath):
                    rel = os.path.relpath(fpath, ROOT)
                    changed.append(rel)
                    print(f"  FIXED: {rel}")
                else:
                    rel = os.path.relpath(fpath, ROOT)
                    print(f"  OK:    {rel}")
            except Exception as e:
                print(f"  ERROR: {os.path.relpath(fpath, ROOT)} — {e}")

print(f"\nTotal modificados: {len(changed)}")
