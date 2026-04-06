import os
import re
from urllib.parse import unquote

base = r'd:\Sarlaft 4.0\docs\Sarlaft40\DocumentacionTecnica\DisenoArquitectura'
broken = []
ok_count = 0

for root, dirs, files in os.walk(base):
    for fname in sorted(files):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(root, fname)
        rel_file = fpath.replace(base + os.sep, '')
        with open(fpath, encoding='utf-8') as f:
            content = f.read()
        # Find all markdown links [text](target)
        links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', content)
        for text, target in links:
            # Skip http/https/mailto links
            if target.startswith('http') or target.startswith('mailto'):
                continue
            # Remove anchor
            target_clean = target.split('#')[0]
            if not target_clean:
                continue
            # URL decode
            target_decoded = unquote(target_clean)
            # Resolve path relative to file
            abs_path = os.path.normpath(os.path.join(root, target_decoded))
            if os.path.exists(abs_path):
                ok_count += 1
            else:
                broken.append((rel_file, text, target, abs_path))

print(f'=== ENLACES ROTOS ({len(broken)}) ===')
for rel, text, target, abs_path in broken:
    print(f'  ARCHIVO: {rel}')
    print(f'  TEXTO:   {text}')
    print(f'  TARGET:  {target}')
    print(f'  BUSCA:   {abs_path}')
    print()

print(f'Total OK: {ok_count}, Total rotos: {len(broken)}')
