import os
import re
import json

base = r'd:\Proyectos\Sarlaft\DocV2\docs\Epica'
results = {}

for root, dirs, files in os.walk(base):
    for f in files:
        if not (f.startswith('HU ') and f.endswith('.md')):
            continue
        m = re.match(r'HU (\d+)', f)
        if not m:
            continue
        hu_id = m.group(1)
        if hu_id in results:
            continue
        path = os.path.join(root, f)
        rel = path.replace(base, '').strip('\\').split('\\')
        epica = rel[0] if len(rel) > 0 else ''
        feature = rel[1] if len(rel) > 1 else ''
        # Extract Epica ID
        em = re.match(r'Epica (\d+)', epica)
        epica_id = em.group(1) if em else ''
        epica_name = re.sub(r'^Epica \d+ - ', '', epica).strip('[]')
        # Extract Feature ID
        fm = re.match(r'Feature (\d+)', feature)
        feature_id = fm.group(1) if fm else ''
        feature_name = re.sub(r'^Feature \d+ - ', '', feature).strip('[]')

        try:
            with open(path, encoding='utf-8') as fh:
                lines = [fh.readline() for _ in range(40)]
        except Exception:
            lines = []

        title = ''
        state = ''
        puntos = ''
        for line in lines:
            if line.startswith('# ') and not title:
                title = line.strip().lstrip('# ')
            if '**Estado**' in line and not state:
                parts2 = line.strip().split('|')
                if len(parts2) >= 3:
                    state = parts2[2].strip()
            if 'Story Points' in line or 'Puntos' in line or 'puntos' in line:
                pm = re.search(r'\|\s*(\d+)\s*\|', line)
                if pm:
                    puntos = pm.group(1)

        results[hu_id] = {
            'id': hu_id,
            'titulo': title,
            'estado': state,
            'puntos': puntos,
            'epica_id': epica_id,
            'epica_name': epica_name,
            'feature_id': feature_id,
            'feature_name': feature_name,
        }

print("Total unique HUs:", len(results))
for k in sorted(results.keys(), key=int):
    r = results[k]
    print(r['id'] + '|' + r['estado'] + '|' + r['epica_id'] + '|' + r['feature_id'] + '|' + r['feature_name'] + '|' + r['titulo'])
