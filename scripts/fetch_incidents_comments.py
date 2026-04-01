import subprocess, json, os

TOKEN = "ATATT3xFfGF0esKEuh1KrY54F4svPmwtTMbbUUp5Yf3Z6y-WqFXPOz2iXGaZ3yWTd8G5Ifa6SvOSwcc19QlZHnywmhF5U_Ot1kpKwhIT75YhNXce_lp6VmGmKMoGhcay3n1kBkQZm5ZIKyRrchJjWCFAvFLERtlFGm8JLSafp16bR2OrY5CGCu8=E4F531A9"
USER = "juan.hoyos@ceiba.com.co"
BASE = "https://segurosti.atlassian.net/wiki"
OUT_DIR = "d:/Sarlaft 4.0/scripts/incidents_pages"

PAGE_IDS = [
    "1742800723", "5174624323", "5174689830",
    "5174788164", "5174886473", "5624856625",
]

def fetch_url(url):
    result = subprocess.run(
        ["curl.exe", "-s", "-u", f"{USER}:{TOKEN}", url],
        capture_output=True, text=True, encoding='utf-8'
    )
    return json.loads(result.stdout)

# Fetch footer comments and inline comments for each page
for pid in PAGE_IDS:
    print(f"\n=== Page {pid} ===")

    # Footer comments
    url_fc = f"{BASE}/api/v2/pages/{pid}/footer-comments?body-format=storage&limit=50"
    fc = fetch_url(url_fc)
    fc_results = fc.get('results', [])
    out = os.path.join(OUT_DIR, f"{pid}_footer_comments.json")
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(fc, f, ensure_ascii=False, indent=2)
    print(f"  Footer comments: {len(fc_results)}")
    for c in fc_results:
        print(f"    ID={c.get('id')} | author={c['version']['by']['displayName']} | {c['version']['when']}")

    # Inline comments via CQL
    url_ic = f"{BASE}/rest/api/search?cql=parent%3D{pid}+AND+type%3Dcomment&limit=50&expand=version,body.storage"
    ic = fetch_url(url_ic)
    ic_results = ic.get('results', [])
    out_ic = os.path.join(OUT_DIR, f"{pid}_inline_comments.json")
    with open(out_ic, 'w', encoding='utf-8') as f:
        json.dump(ic, f, ensure_ascii=False, indent=2)
    print(f"  Inline comments (CQL): {len(ic_results)}")
    for c in ic_results:
        cc = c.get('content', {})
        ver = cc.get('version', {})
        print(f"    ID={cc.get('id')} | {ver.get('when')} | {ver.get('by', {}).get('displayName')}")

print("\nDone.")
