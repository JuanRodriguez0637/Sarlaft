import requests, json
from confluence_config import BASE_URL, HEADERS

cql = 'space = EPA AND title = "Microservicio Backweb" AND type = page'
r = requests.get(BASE_URL+'/wiki/rest/api/search', headers=HEADERS, params={'cql': cql, 'limit': 10})
data = r.json()
for res in data.get('results', []):
    print('ID:', res['content']['id'], '|', res['content']['title'])
if not data.get('results'):
    print('Sin resultados. Status:', r.status_code)
    print(json.dumps(data, indent=2, ensure_ascii=False)[:2000])
