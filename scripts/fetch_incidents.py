import subprocess, json, os, sys

TOKEN = "ATATT3xFfGF0esKEuh1KrY54F4svPmwtTMbbUUp5Yf3Z6y-WqFXPOz2iXGaZ3yWTd8G5Ifa6SvOSwcc19QlZHnywmhF5U_Ot1kpKwhIT75YhNXce_lp6VmGmKMoGhcay3n1kBkQZm5ZIKyRrchJjWCFAvFLERtlFGm8JLSafp16bR2OrY5CGCu8=E4F531A9"
USER = "juan.hoyos@ceiba.com.co"
BASE = "https://segurosti.atlassian.net/wiki"
OUT_DIR = "d:/Sarlaft 4.0/scripts/incidents_pages"
os.makedirs(OUT_DIR, exist_ok=True)

PAGE_IDS = [
    "1742800723",  # parent: Documentación de Incidentes
    "5174624323",  # Limpiar Base de datos en laboratorio
    "5174689830",  # Solicitud de request and respose
    "5174788164",  # Problemas con el link de validación de identidad
    "5174886473",  # Solucionar INC asignados en BMC Helix
    "5624856625",  # Error en el aplicativo de Banca (Negocio en estado PENDIENTE)
]

def fetch(page_id, expand="version,ancestors,body.storage,children.page"):
    url = f"{BASE}/rest/api/content/{page_id}?expand={expand}"
    result = subprocess.run(
        ["curl.exe", "-s", "-u", f"{USER}:{TOKEN}", url],
        capture_output=True, text=True, encoding='utf-8'
    )
    return json.loads(result.stdout)

for pid in PAGE_IDS:
    print(f"Fetching {pid}...")
    data = fetch(pid)
    out_path = os.path.join(OUT_DIR, f"{pid}.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    title = data.get('title', '?')
    ver = data.get('version', {})
    body_len = len(data.get('body', {}).get('storage', {}).get('value', ''))
    print(f"  {title} | v{ver.get('number')} | {ver.get('when')} | {ver.get('by', {}).get('displayName')} | body={body_len}b")

print("Done.")
