import sys, requests
sys.path.insert(0, '.')
from confluence_config import BASE_URL, HEADERS

def get_children(pid):
    url = BASE_URL + '/wiki/rest/api/content/' + pid + '/child/page?limit=50&expand=version'
    r = requests.get(url, headers=HEADERS)
    return r.json().get('results', [])

root_id = '1804697669'
children = get_children(root_id)
print('Hijos directos de Diseño - Arquitectura:')
for c in children:
    cid = c['id']
    subs = get_children(cid)
    print('  [' + cid + '] ' + c['title'] + '  (' + str(len(subs)) + ' hijos)')
    for s in subs:
        sid = s['id']
        sub2 = get_children(sid)
        print('    [' + sid + '] ' + s['title'] + '  (' + str(len(sub2)) + ' hijos)')
        for s2 in sub2:
            s2id = s2['id']
            sub3 = get_children(s2id)
            print('      [' + s2id + '] ' + s2['title'] + '  (' + str(len(sub3)) + ' hijos)')
            for s3 in sub3:
                print('        [' + s3['id'] + '] ' + s3['title'])
