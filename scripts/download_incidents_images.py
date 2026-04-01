import subprocess, json, os

TOKEN = "ATATT3xFfGF0esKEuh1KrY54F4svPmwtTMbbUUp5Yf3Z6y-WqFXPOz2iXGaZ3yWTd8G5Ifa6SvOSwcc19QlZHnywmhF5U_Ot1kpKwhIT75YhNXce_lp6VmGmKMoGhcay3n1kBkQZm5ZIKyRrchJjWCFAvFLERtlFGm8JLSafp16bR2OrY5CGCu8=E4F531A9"
USER = "juan.hoyos@ceiba.com.co"
BASE = "https://segurosti.atlassian.net/wiki"
IMG_DIR = "d:/Sarlaft 4.0/docs/DocumentacionDeIncidentes/img"
PAGES_DIR = "d:/Sarlaft 4.0/scripts/incidents_pages"

# Images to download: (page_id, filename, download_relative_url)
IMAGES = [
    ("5174886473", "image-20251201-154141.png"),
    ("5174886473", "image-20251201-154154.png"),
    ("5624856625", "image-20260226-224639.png"),
    ("5624856625", "image-20260226-224911.png"),
    ("5624856625", "image-20260226-225247.png"),
    ("5624856625", "image-20260226-225735.png"),
]

for pid, filename in IMAGES:
    att_data = json.load(open(os.path.join(PAGES_DIR, f"{pid}_attachments.json"), encoding='utf-8'))
    for a in att_data.get('results', []):
        if a['title'] == filename:
            dl_path = a['_links']['download']
            url = BASE + dl_path
            out = os.path.join(IMG_DIR, filename)
            print(f"Downloading {filename}...")
            result = subprocess.run(
                ["curl.exe", "-s", "-u", f"{USER}:{TOKEN}", "-L", "-o", out, url],
                capture_output=True
            )
            size = os.path.getsize(out) if os.path.exists(out) else 0
            print(f"  -> {out} ({size} bytes)")
            break

print("Done.")
