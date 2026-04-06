import os
import re
from urllib.parse import unquote

base = r'd:\Sarlaft 4.0\docs\Sarlaft40\DocumentacionTecnica\DisenoArquitectura'
broken_imgs = []
ok_count = 0

for root, dirs, files in os.walk(base):
    for fname in sorted(files):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(root, fname)
        rel_file = fpath.replace(base + os.sep, '')
        with open(fpath, encoding='utf-8') as f:
            content = f.read()
        imgs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
        for alt, target in imgs:
            if target.startswith('http'):
                continue
            target_decoded = unquote(target)
            abs_path = os.path.normpath(os.path.join(root, target_decoded))
            if not os.path.exists(abs_path):
                broken_imgs.append((rel_file, alt, target, abs_path))
            else:
                ok_count += 1

print(f'Imagenes OK: {ok_count}, Imagenes rotas: {len(broken_imgs)}')
for rel, alt, target, absp in broken_imgs:
    print(f'  [{rel}]')
    print(f'  alt="{alt}"')
    print(f'  target={target}')
    print(f'  buscado en: {absp}')
    print()
