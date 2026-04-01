"""
fix_peps_lint.py — Corrige errores de linting en docs/MicroservicioPEPS/*.md

Reglas corregidas:
  - heading-order     : saltos de nivel (H1 → H4 → H5) → normalizar
  - MD032             : listas sin líneas en blanco alrededor
  - MD010             : tabs → 4 espacios
  - MD040             : bloques de código sin lenguaje
  - MD047             : archivo sin newline final
  - Bonus             : items "-\\n**texto**" fusionados en "- **texto**"
"""
import os
import re
from pathlib import Path

PEPS_ROOT = r"D:\Sarlaft 4.0\docs\MicroservicioPEPS"


# ── Helpers ──────────────────────────────────────────────────────────────────

def fix_tabs(text: str) -> str:
    """MD010: reemplaza tabs por 4 espacios."""
    return text.replace("\t", "    ")


def fix_trailing_newline(text: str) -> str:
    """MD047: asegura exactamente un newline al final."""
    return text.rstrip("\n") + "\n"


def fix_broken_list_items(text: str) -> str:
    """
    Convierte el patrón '-\\n**texto**' producido por el extractor en '- **texto**'.
    Luego colapsa líneas en blanco dentro de bloques de lista y asegura MD032.
    """
    # Paso 1: Fusionar '-' solitario con la siguiente línea de contenido
    # Patrón: línea que es solo '-' seguida de línea con contenido (no vacía)
    text = re.sub(r'^-\s*\n(\S)', r'- \1', text, flags=re.MULTILINE)

    # Paso 2: Dentro de un bloque de lista contiguo, eliminar líneas en blanco
    # entre ítems para que no generen sub-listas separadas (MD032 lo tolera
    # solo si hay una línea en blanco FUERA del bloque).
    # Estrategia: colapsar "\n\n- " → "\n- " cuando ya estamos en una lista.
    # Lo hacemos iterativamente para los bloques continuos.
    text = re.sub(r'(\n- [^\n]+)\n\n(- )', r'\1\n\2', text)
    # Repetir una vez más por si quedan casos
    text = re.sub(r'(\n- [^\n]+)\n\n(- )', r'\1\n\2', text)

    # Paso 3: MD032 – garantizar línea en blanco ANTES del primer ítem de lista
    # (si la línea anterior no es ya una línea en blanco ni un encabezado)
    text = re.sub(r'([^\n])\n(- )', r'\1\n\n\2', text)

    # Paso 4: MD032 – garantizar línea en blanco DESPUÉS del último ítem de lista
    # (si la siguiente línea no es ya un ítem de lista ni está en blanco)
    text = re.sub(r'(^- [^\n]+)\n([^-\n\s])', r'\1\n\n\2', text, flags=re.MULTILINE)

    return text


def fix_heading_order(text: str) -> str:
    """
    heading-order: en cada archivo normaliza los niveles para que no salten
    más de un nivel respecto al H1 inicial.
    Aplica solo cuando hay H4/H5 inmediatamente bajo un H1 (sin H2/H3 antes).
    Estrategia simple para los archivos generados: remapear todos los heading
    levels según el mínimo encontrado bajo H1.
    """
    lines = text.split("\n")
    result = []
    # Detectar si hay salto (H1 seguido directamente por H4+)
    levels_used = set()
    for line in lines:
        m = re.match(r'^(#{1,6})\s', line)
        if m:
            levels_used.add(len(m.group(1)))

    if not levels_used:
        return text

    # Si hay H1 y H4/H5 pero NO H2/H3 en el archivo → necesita remapeo
    has_h1      = 1 in levels_used
    has_h4_plus = bool(levels_used & {4, 5, 6})
    has_h2_h3   = bool(levels_used & {2, 3})

    if has_h1 and has_h4_plus and not has_h2_h3:
        # Calcular offset: el nivel mínimo distinto de 1 → debería ser 2
        min_other = min(l for l in levels_used if l != 1)
        offset = min_other - 2  # cuánto hay que restar a cada nivel > 1

        new_lines = []
        for line in lines:
            m = re.match(r'^(#{1,6})(\s.*)', line)
            if m:
                lvl = len(m.group(1))
                if lvl > 1:
                    new_lvl = max(2, lvl - offset)
                    line = "#" * new_lvl + m.group(2)
            new_lines.append(line)
        return "\n".join(new_lines)

    return text


# Mapa de patrones de contenido → lenguaje para code blocks sin especificar
CODE_LANG_PATTERNS = [
    # YAML: empieza con clave: valor estilo spring
    (re.compile(r'^(spring:|soap-client:|server:|logging:|management:)', re.M), "yaml"),
    # Java: anotaciones Spring o declaraciones de clase/función típicas
    (re.compile(r'@(Configuration|Bean|Primary|Value|EnableJpaRepositories|EnableTransactionManagement)\b'), "java"),
    (re.compile(r'\bpublic\s+(class|interface|LocalContainerEntityManagerFactoryBean|DataSource|PlatformTransactionManager)\b'), "java"),
    # SQL
    (re.compile(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE TABLE|ALTER TABLE)\b', re.I), "sql"),
    # XML
    (re.compile(r'<\?xml|<beans|<configuration'), "xml"),
    # JSON: objetos o arrays JSON
    (re.compile(r'^\s*\{[\s\S]*"[^"]+"\s*:', re.M), "json"),
    # Bash/shell
    (re.compile(r'^(#!|export |source |cd |ls |curl |wget )', re.M), "bash"),
]


def detect_language(code: str) -> str:
    """Detecta el lenguaje de un bloque de código sin especificar."""
    for pattern, lang in CODE_LANG_PATTERNS:
        if pattern.search(code):
            return lang
    return "text"


def fix_fenced_code_language(text: str) -> str:
    """
    MD040: añade lenguaje a bloques ``` sin especificar.
    No modifica bloques que ya tienen lenguaje.
    """
    def replace_block(m):
        opening = m.group(1)  # la línea de apertura, ej: "```" o "```java"
        code    = m.group(2)
        closing = m.group(3)

        # Si ya tiene lenguaje, no tocar
        if opening.strip() != "```":
            return m.group(0)

        lang = detect_language(code)
        return f"```{lang}\n{code}{closing}"

    # Patrón: línea con sólo ``` seguida de contenido y cierre ```
    return re.sub(r'(```[a-z]*)\n([\s\S]*?)(```)', replace_block, text)


def fix_file(filepath: str) -> tuple[bool, list]:
    """Aplica todas las correcciones a un archivo. Retorna (modificado, lista_cambios)."""
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    text = original
    changes = []

    # 1. Tabs → espacios
    fixed = fix_tabs(text)
    if fixed != text:
        changes.append("MD010: tabs → espacios")
        text = fixed

    # 2. Heading order
    fixed = fix_heading_order(text)
    if fixed != text:
        changes.append("heading-order: niveles normalizados")
        text = fixed

    # 3. Broken list items ("-\n**texto**") y MD032
    fixed = fix_broken_list_items(text)
    if fixed != text:
        changes.append("MD032/items: listas corregidas y rodeadas de líneas en blanco")
        text = fixed

    # 4. Code blocks sin lenguaje
    fixed = fix_fenced_code_language(text)
    if fixed != text:
        changes.append("MD040: lenguaje añadido a bloques de código")
        text = fixed

    # 5. Trailing newline
    fixed = fix_trailing_newline(text)
    if fixed != text:
        changes.append("MD047: newline final añadido")
        text = fixed

    if text == original:
        return False, []

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    return True, changes


def main():
    print("=" * 60)
    print(f"Corrigiendo lint en: {PEPS_ROOT}")
    print("=" * 60)

    md_files = sorted(Path(PEPS_ROOT).rglob("*.md"))

    if not md_files:
        print("No se encontraron archivos .md")
        return

    total_modified = 0
    for fpath in md_files:
        rel = fpath.relative_to(PEPS_ROOT)
        modified, changes = fix_file(str(fpath))
        if modified:
            total_modified += 1
            print(f"\n[MODIFICADO] {rel}")
            for c in changes:
                print(f"  • {c}")
        else:
            print(f"[OK]         {rel}")

    print(f"\n{'='*60}")
    print(f"Total modificados: {total_modified} / {len(md_files)} archivos")


if __name__ == "__main__":
    main()
