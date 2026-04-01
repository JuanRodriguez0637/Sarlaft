import json

data = json.load(open('d:/Sarlaft 4.0/scripts/incidents_tree.json', encoding='utf-8'))
print(f'Total: {data["totalSize"]}')
for r in data['results']:
    c = r['content']
    ancs = ' > '.join(a['title'] for a in c.get('ancestors', []))
    ver = c.get('version', {})
    print(f'  ID={c["id"]} | {c["title"]} | v{ver.get("number","?")} | {ver.get("when","?")} | {ver.get("by",{}).get("displayName","?")}')
    print(f'    ancestors: {ancs}')
