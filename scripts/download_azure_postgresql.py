"""
Descarga la página 'Azure Database for PostgreSQL' (ID 1381761738, space AR)
y la guarda como AzurePostgreSQL_EstandarNombramiento.md en docs/arquitectura/referencias/
"""
import requests
import base64
import re
import html as html_lib
import os

EMAIL = "juan.hoyos@ceiba.com.co"
TOKEN = "ATATT3xFfGF0esKEuh1KrY54F4svPmwtTMbbUUp5Yf3Z6y-WqFXPOz2iXGaZ3yWTd8G5Ifa6SvOSwcc19QlZHnywmhF5U_Ot1kpKwhIT75YhNXce_lp6VmGmKMoGhcay3n1kBkQZm5ZIKyRrchJjWCFAvFLERtlFGm8JLSafp16bR2OrY5CGCu8=E4F531A9"
BASE_URL = "https://segurosti.atlassian.net"
PAGE_ID = "1381761738"
OUT_PATH = r"D:\Sarlaft 4.0\docs\Diseño - Arquitectura\referencias\AzurePostgreSQL_EstandarNombramiento.md"

creds = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()
HEADERS = {"Authorization": f"Basic {creds}", "Accept": "application/json"}


def html_to_md(raw: str) -> str:
    md = raw
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>', r'_\1_', md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>', r'_\1_', md, flags=re.S)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.S)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', md, flags=re.S)
    for n in range(1, 7):
        def heading_repl(m, level=n):
            return f'\n{"#" * level} {m.group(1)}\n'
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>', heading_repl, md, flags=re.S)
    def link_repl(m):
        href, text = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
        return f"[{text or href}]({href})"
    md = re.sub(r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>', link_repl, md, flags=re.S)
    md = re.sub(r'<ul[^>]*>', '\n', md)
    md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<ol[^>]*>', '\n', md)
    md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.S)
    md = re.sub(r'<table[^>]*>', '\n', md)
    md = re.sub(r'</table>', '\n', md)
    md = re.sub(r'<t(?:head|body|foot)[^>]*>|</t(?:head|body|foot)>', '', md)
    md = re.sub(r'<tr[^>]*>', '|', md)
    md = re.sub(r'</tr>', '\n', md)
    md = re.sub(r'<th[^>]*>(.*?)</th>', r' **\1** |', md, flags=re.S)
    md = re.sub(r'<td[^>]*>(.*?)</td>', r' \1 |', md, flags=re.S)
    md = re.sub(r'<br\s*/?>', '\n', md)
    md = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', md, flags=re.S)
    md = re.sub(r'<[^>]+>', '', md)
    md = html_lib.unescape(md)
    md = md.replace('\u00a0', ' ')
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def main():
    url = f"{BASE_URL}/wiki/rest/api/content/{PAGE_ID}?expand=body.storage,title,version"
    r = requests.get(url, headers=HEADERS, timeout=30)
    if r.status_code != 200:
        print(f"ERROR: {r.status_code} - {r.text[:200]}")
        return

    data = r.json()
    title = data.get("title", "Azure Database for PostgreSQL")
    version = data.get("version", {}).get("number", "?")
    body = data.get("body", {}).get("storage", {}).get("value", "")

    content = html_to_md(body)

    conf_url = f"https://segurosti.atlassian.net/wiki/spaces/AR/pages/{PAGE_ID}"
    md = f"# {title}\n\n"
    md += f">**Fuente:** [Ver en Confluence]({conf_url})  \n"
    md += f">**Space:** AR - Dominio Transformación Tecnológica  \n"
    md += f">**Versión:** {version}  \n\n"
    md += content + "\n"

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Guardado: {OUT_PATH}")
    print(f"Tamaño: {len(md)} caracteres, {len(md.splitlines())} líneas")


if __name__ == "__main__":
    main()
