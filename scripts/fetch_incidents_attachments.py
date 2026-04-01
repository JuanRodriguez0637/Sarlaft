import subprocess, json, os, re

TOKEN = "ATATT3xFfGF0esKEuh1KrY54F4svPmwtTMbbUUp5Yf3Z6y-WqFXPOz2iXGaZ3yWTd8G5Ifa6SvOSwcc19QlZHnywmhF5U_Ot1kpKwhIT75YhNXce_lp6VmGmKMoGhcay3n1kBkQZm5ZIKyRrchJjWCFAvFLERtlFGm8JLSafp16bR2OrY5CGCu8=E4F531A9"
USER = "juan.hoyos@ceiba.com.co"
BASE = "https://segurosti.atlassian.net/wiki"
PAGES_DIR = "d:/Sarlaft 4.0/scripts/incidents_pages"

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

for pid in PAGE_IDS:
    # Load body
    page = json.load(open(os.path.join(PAGES_DIR, f"{pid}.json"), encoding='utf-8'))
    body = page.get('body', {}).get('storage', {}).get('value', '')

    # Find referenced attachments in body
    referenced = set(re.findall(r'ri:filename="([^"]+)"', body))
    referenced |= set(re.findall(r'ri:attachment[^>]+ri:filename="([^"]+)"', body))

    print(f"\n=== Page {pid}: {page['title']} ===")
    print(f"  Referenced attachments in body: {list(referenced) if referenced else '(none)'}")

    # List all attachments on page
    url_att = f"{BASE}/api/v2/pages/{pid}/attachments?limit=50"
    att_data = fetch_url(url_att)
    attachments = att_data.get('results', [])
    out_path = os.path.join(PAGES_DIR, f"{pid}_attachments.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(att_data, f, ensure_ascii=False, indent=2)
    print(f"  Total attachments on page: {len(attachments)}")
    for a in attachments:
        is_ref = a['title'] in referenced
        print(f"    {'[REF]' if is_ref else '[---]'} {a['title']} | {a.get('mediaType', '?')} | download: {a['_links'].get('download', '?')[:80]}")

print("\nDone.")
