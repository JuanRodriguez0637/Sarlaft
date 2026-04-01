"""Regenera BaseJpaConfig.md desde Confluence."""
import requests, re, html as html_lib
from confluence_config import BASE_URL, HEADERS

page_id = '3632300037'

# View body
rv = requests.get(BASE_URL+f'/wiki/api/v2/pages/{page_id}?body-format=view', headers=HEADERS)
data = rv.json()
title = data['title']
body_html = data['body']['view']['value']
ver = data['version']['number']
dated = (data['version']['createdAt'] or '')[:10]

# Storage for attachment refs
rs = requests.get(BASE_URL+f'/wiki/api/v2/pages/{page_id}?body-format=storage', headers=HEADERS)
storage = rs.json()['body']['storage']['value']
refs = set(re.findall(r'ri:filename="([^"]+)"', storage, re.I))
print('Refs:', refs)

def html_to_md(raw):
    if not raw:
        return ""
    md = raw

    def code_macro(m):
        lang_match = re.search(r'ac:name="language"[^>]*>(.*?)</ac:parameter>', m.group(0), re.S | re.I)
        lang = lang_match.group(1).strip() if lang_match else ""
        cdata_match = re.search(r'<!\[CDATA\[(.*?)\]\]>', m.group(0), re.S)
        body = cdata_match.group(1) if cdata_match else ""
        return f"\n```{lang}\n{body.strip()}\n```\n"

    md = re.sub(r'<ac:structured-macro[^>]*ac:name="code"[^>]*>.*?</ac:structured-macro>', code_macro, md, flags=re.S|re.I)

    def macro_box(m):
        name = m.group(1).lower()
        body = re.sub(r'<[^>]+>', '', m.group(2) or '').strip()
        icons = {"info": "ℹ️", "warning": "⚠️", "note": "📝", "tip": "💡", "panel": "📋"}
        return f"\n> {icons.get(name,'📌')} **{name.upper()}:** {body}\n"
    md = re.sub(r'<ac:structured-macro[^>]*ac:name="(info|warning|note|tip|panel)"[^>]*>(.*?)</ac:structured-macro>', macro_box, md, flags=re.S|re.I)
    md = re.sub(r'<ac:structured-macro[^>]*>.*?</ac:structured-macro>', '', md, flags=re.S)
    md = re.sub(r'<ac:plain-text-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-body>', r'\n```\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<ac:rich-text-body[^>]*>(.*?)</ac:rich-text-body>', r'\1', md, flags=re.S)
    md = re.sub(r'<ac:image[^>]*>.*?<ri:attachment\s+ri:filename="([^"]+)".*?</ac:image>', lambda m: f"![{m.group(1)}](img/{m.group(1)})", md, flags=re.S|re.I)
    md = re.sub(r'<ac:link[^>]*>\s*<ri:page\s+ri:content-title="([^"]+)"[^/]*/?\s*>(?:\s*<ac:plain-text-link-body[^>]*><!\[CDATA\[(.*?)\]\]></ac:plain-text-link-body>)?\s*</ac:link>', lambda m: f"[{m.group(2) or m.group(1)}]({m.group(1).replace(' ','_')}.md)", md, flags=re.S|re.I)
    md = re.sub(r'<ac:link[^>]*>.*?</ac:link>', '', md, flags=re.S)
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', md, flags=re.S)
    md = re.sub(r'<em[^>]*>(.*?)</em>', r'_\1_', md, flags=re.S)
    md = re.sub(r'<i[^>]*>(.*?)</i>', r'_\1_', md, flags=re.S)
    for n in range(1, 7):
        md = re.sub(rf'<h{n}[^>]*>(.*?)</h{n}>', rf'\n{"#"*(n+1)} \1\n', md, flags=re.S)
    md = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', md, flags=re.S)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.S)
    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', lambda m: f"[{re.sub(r'<[^>]+>','',m.group(2)).strip() or m.group(1)}]({m.group(1)})", md, flags=re.S)
    md = re.sub(r'<ul[^>]*>', '\n', md); md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<ol[^>]*>', '\n', md); md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.S)
    def convert_table(m):
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', m.group(0), re.S)
        result = []; hd = False
        for row in rows:
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.S)
            clean = [html_lib.unescape(re.sub(r'<[^>]+>','',c)).strip().replace('\n',' ') for c in cells]
            if not clean: continue
            result.append("| "+" | ".join(clean)+" |")
            if not hd:
                result.append("| "+" | ".join(["---"]*len(clean))+" |")
                hd = True
        return "\n"+"\n".join(result)+"\n"
    md = re.sub(r'<table[^>]*>.*?</table>', convert_table, md, flags=re.S)
    md = re.sub(r'<p[^>]*>', '\n', md); md = re.sub(r'</p>', '\n', md)
    md = re.sub(r'<br\s*/?>', '\n', md); md = re.sub(r'<hr\s*/?>', '\n---\n', md)
    md = re.sub(r'<div[^>]*>', '\n', md); md = re.sub(r'</div>', '\n', md)
    md = re.sub(r'<span[^>]*>', '', md); md = re.sub(r'</span>', '', md)
    md = re.sub(r'<[^>]+>', '', md)
    md = html_lib.unescape(md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    return md.strip()

body_md = html_to_md(body_html)

content = f"# {title}\n\n"
content += f"> **Fuente Confluence:** [{title}]({BASE_URL}/wiki/spaces/EPA/pages/{page_id})\n"
content += f"> **Última modificación:** {dated} · versión {ver}\n"
content += f"> **Sección:** [Microservicio Backweb](./index.md)\n\n"
content += body_md + "\n"

out = r"D:\Sarlaft 4.0\docs\MicroservicioBackweb\BaseJpaConfig.md"
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print(f"OK - {len(content)} bytes -> {out}")
