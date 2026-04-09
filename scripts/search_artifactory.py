import urllib.request, base64, json, urllib.parse

user = "juan.rodriguez@ceiba.com.co"
token = "ATATT3xFfGF0vhrDmoammNGl3Q6JEMWauDVgraW7PVcDE4zidIbS0nqdVjlvMg1AMRMyiBJtEdu7jtQGfNWo1ZxQicO-033KlrZXZq8CgsT7ds1f_pft3qLzSmsZfFD1B2D53whjezMlKVdhtoMwo-9OcAGQLqjkjjMpqIvje3O7grQevXA-o3s=C39BE740"
creds = base64.b64encode((user + ":" + token).encode()).decode()

queries = [
    'space = EPA AND type = page AND title ~ "artifactory"',
    'space = EPA AND type = page AND title ~ "onboarding"',
    'space = EPA AND type = page AND title ~ "configuracion desarrollador"',
    'space = EPA AND type = page AND title ~ "setup ambiente"',
    'space = EPA AND type = page AND text ~ "ARTIFACTORY_TOKEN"',
    'space = EPA AND type = page AND text ~ "token artifactory"',
]

found = False
for cql in queries:
    url = "https://segurosti.atlassian.net/wiki/rest/api/search?cql=" + urllib.parse.quote(cql) + "&limit=5"
    req = urllib.request.Request(url, headers={"Authorization": "Basic " + creds})
    with urllib.request.urlopen(req) as r:
        d = json.load(r)
    if d.get("totalSize", 0) > 0:
        found = True
        print(f"CQL: {cql}")
        for x in d.get("results", []):
            print(f"  {x['content']['id']} - {x['content']['title']}")

if not found:
    print("No se encontraron paginas relacionadas con Artifactory token en el espacio EPA.")
