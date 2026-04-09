"""
Genera la estructura de carpetas y archivos individuales por HU a partir del backlog:

docs/Sarlaft40/Backlog/
  EPICA_<id>_<titulo>/
    FEATURE_<id>_<titulo>/
      HU_<id>_<titulo>.md
    ...
  SIN_EPICA/
    SIN_FEATURE/
      HU_<id>_<titulo>.md

Reutiliza la lógica de download_azure_backlog.py.
"""

import base64
import json
import os
import re
import sys
import time
import textwrap
from typing import Optional

import requests

# ─────────────────────────────────────────────
# CONFIG (mismos valores que download_azure_backlog.py)
# ─────────────────────────────────────────────
ORG      = "SuraColombia"
PROJECT  = "Gerencia_Tecnologia"
TEAM     = "do-soluci_corporativas-Fortalecimiento SARLAFT"
PAT      = os.getenv("ADO_PAT", "3KDIrWMhH2CsFRo2VcVqfTffqiRT4jW3PQ7RU4tC97XJxpLBIUS4JQQJ99CDACAAAAA5G0YpAAASAZDO16Bk")
API_VER  = "7.1"
BATCH    = 200
OUT_ROOT = os.path.join(os.path.dirname(__file__), "..", "docs", "Sarlaft40", "Backlog")

_b64 = base64.b64encode(f":{PAT}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {_b64}",
    "Content-Type":  "application/json",
    "Accept":        "application/json",
}
BASE = f"https://dev.azure.com/{ORG}"


# ─────────────────────────────────────────────
# HTTP HELPERS
# ─────────────────────────────────────────────

def get(url: str, params: dict = None) -> dict:
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    if r.status_code == 401:
        print("❌  401 Unauthorized — PAT inválido o sin permisos.")
        sys.exit(1)
    r.raise_for_status()
    return r.json()


def post(url: str, body: dict) -> dict:
    r = requests.post(url, headers=HEADERS, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_items_batch(ids: list[int]) -> list[dict]:
    fields = [
        "System.Id", "System.Title", "System.WorkItemType",
        "System.State", "System.AreaPath", "System.IterationPath",
        "System.AssignedTo", "System.Parent",
        "Microsoft.VSTS.Common.Priority",
        "Microsoft.VSTS.Scheduling.StoryPoints",
        "System.Description", "System.Tags",
        "Microsoft.VSTS.Common.AcceptanceCriteria",
    ]
    result = []
    for i in range(0, len(ids), BATCH):
        chunk = ids[i : i + BATCH]
        body  = {"ids": chunk, "fields": fields}
        url   = f"{BASE}/{PROJECT}/_apis/wit/workitemsbatch?api-version={API_VER}"
        data  = post(url, body)
        result.extend(data.get("value", []))
        time.sleep(0.05)
    return result


def get_area_path() -> str:
    url = (f"{BASE}/{PROJECT}/{requests.utils.quote(TEAM)}"
           f"/_apis/work/teamsettings/teamfieldvalues?api-version={API_VER}")
    try:
        data   = get(url)
        values = data.get("values", [])
        if values:
            return values[0].get("value", PROJECT)
    except Exception:
        pass
    return PROJECT


def wiql_hu(area_path: str) -> list[int]:
    safe = area_path.replace("'", "''")
    query = {
        "query": (
            "SELECT [System.Id] FROM WorkItems "
            f"WHERE [System.TeamProject] = '{PROJECT}' "
            f"  AND [System.AreaPath] UNDER '{safe}' "
            "  AND [System.WorkItemType] IN ('Historia de Usuario','User Story','Historia') "
            "  AND [System.State] <> 'Eliminado' "
            "ORDER BY [System.Id] ASC"
        )
    }
    url  = f"{BASE}/{PROJECT}/_apis/wit/wiql?api-version={API_VER}"
    data = post(url, query)
    return [wi["id"] for wi in data.get("workItems", [])]


# ─────────────────────────────────────────────
# JERARQUÍA
# ─────────────────────────────────────────────

def build_cache(ids: list[int]) -> dict:
    """Descarga ítems y sus padres/abuelos en un dict id→fields."""
    items = fetch_items_batch(ids)
    cache: dict = {}
    for item in items:
        f = item.get("fields", {})
        f["_id"] = item["id"]
        cache[item["id"]] = f

    # padres (Features)
    parent_ids = {f.get("System.Parent") for f in cache.values()
                  if f.get("System.Parent") and f.get("System.Parent") not in cache}
    if parent_ids:
        for item in fetch_items_batch(list(parent_ids)):
            f = item.get("fields", {})
            f["_id"] = item["id"]
            cache[item["id"]] = f

    # abuelos (Épicas)
    gp_ids = {cache[pid].get("System.Parent")
              for pid in parent_ids if pid in cache
              if cache[pid].get("System.Parent") and cache[pid].get("System.Parent") not in cache}
    if gp_ids:
        for item in fetch_items_batch(list(gp_ids)):
            f = item.get("fields", {})
            f["_id"] = item["id"]
            cache[item["id"]] = f
    return cache


def resolve_parents(hu_id: int, cache: dict):
    """Devuelve (epic_fields, feature_fields) para una HU."""
    feature = None
    epic    = None
    current = cache.get(hu_id, {})
    for _ in range(5):
        pid = current.get("System.Parent")
        if not pid or pid not in cache:
            break
        parent = cache[pid]
        wtype  = parent.get("System.WorkItemType", "")
        if "Feature" in wtype or "Característica" in wtype:
            feature = parent
            # buscar épica del feature
            gid = parent.get("System.Parent")
            if gid and gid in cache:
                gp = cache[gid]
                gt = gp.get("System.WorkItemType", "")
                if "Epic" in gt or "Épica" in gt or "Epica" in gt:
                    epic = gp
        elif "Epic" in wtype or "Épica" in wtype or "Epica" in wtype:
            epic = parent
        current = parent
    return epic, feature


# ─────────────────────────────────────────────
# NOMBRES DE ARCHIVOS / CARPETAS
# ─────────────────────────────────────────────
MAX_TITLE = 60  # caracteres para el nombre de carpeta/archivo

def slugify(text: str) -> str:
    """Convierte un título en slug seguro para nombre de carpeta/archivo."""
    # Quitar caracteres no alfanuméricos (excepto espacios y guiones)
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    # Reemplazar espacios por _
    text = re.sub(r"\s+", "_", text.strip())
    # Quitar _ repetidos
    text = re.sub(r"_+", "_", text)
    return text[:MAX_TITLE].strip("_")


def epic_folder(e: Optional[dict]) -> str:
    if not e:
        return "SIN_EPICA"
    return f"EPICA_{e['_id']}_{slugify(e.get('System.Title',''))}"


def feature_folder(f: Optional[dict]) -> str:
    if not f:
        return "SIN_FEATURE"
    return f"FEATURE_{f['_id']}_{slugify(f.get('System.Title',''))}"


def hu_filename(hu: dict) -> str:
    return f"HU_{hu['_id']}_{slugify(hu.get('System.Title',''))}.md"


# ─────────────────────────────────────────────
# RENDER HU
# ─────────────────────────────────────────────

def clean_html(text: Optional[str]) -> str:
    if not text:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<p[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"</p>", "", text, flags=re.I)
    text = re.sub(r"<li[^>]*>", "\n- ", text, flags=re.I)
    text = re.sub(r"</li>", "", text, flags=re.I)
    text = re.sub(r"<ul[^>]*>|</ul>|<ol[^>]*>|</ol>", "", text, flags=re.I)
    text = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", text, flags=re.I | re.DOTALL)
    text = re.sub(r"<b[^>]*>(.*?)</b>",           r"**\1**", text, flags=re.I | re.DOTALL)
    text = re.sub(r"<em[^>]*>(.*?)</em>",          r"*\1*",   text, flags=re.I | re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    text = (text.replace("&nbsp;", " ").replace("&lt;", "<")
                .replace("&gt;", ">").replace("&amp;", "&").replace("&#160;", " "))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def ado_url(item_id: int) -> str:
    return f"https://dev.azure.com/{ORG}/{PROJECT}/_workitems/edit/{item_id}"


def render_hu(hu: dict, epic: Optional[dict], feature: Optional[dict]) -> str:
    sid    = hu.get("_id", "")
    title  = hu.get("System.Title", "Sin título")
    state  = hu.get("System.State", "")
    pts    = hu.get("Microsoft.VSTS.Scheduling.StoryPoints", "")
    prio   = hu.get("Microsoft.VSTS.Common.Priority", "")
    assignd= hu.get("System.AssignedTo", {})
    iterp  = hu.get("System.IterationPath", "")
    tags   = hu.get("System.Tags", "")
    desc   = clean_html(hu.get("System.Description", ""))
    acrit  = clean_html(hu.get("Microsoft.VSTS.Common.AcceptanceCriteria", ""))

    if isinstance(assignd, dict):
        assignd = assignd.get("displayName", "")

    lines = []
    lines.append(f"# HU {sid} — {title}\n")

    # Breadcrumb
    bc_parts = []
    if epic:
        bc_parts.append(f"[Épica {epic['_id']}]({ado_url(epic['_id'])}) {epic.get('System.Title','')}")
    if feature:
        bc_parts.append(f"[Feature {feature['_id']}]({ado_url(feature['_id'])}) {feature.get('System.Title','')}")
    bc_parts.append(f"[HU {sid}]({ado_url(sid)})")
    lines.append(" > ".join(bc_parts) + "\n")
    lines.append("---\n")

    # Metadata table
    lines.append("| Atributo | Valor |")
    lines.append("|----------|-------|")
    lines.append(f"| **ID Azure DevOps** | [{sid}]({ado_url(sid)}) |")
    if state:   lines.append(f"| **Estado** | {state} |")
    if pts:     lines.append(f"| **Story Points** | {pts} |")
    if prio:    lines.append(f"| **Prioridad** | {prio} |")
    if assignd: lines.append(f"| **Asignado a** | {assignd} |")
    if iterp:   lines.append(f"| **Iteración** | `{iterp}` |")
    if tags:    lines.append(f"| **Tags** | {tags} |")
    if epic:    lines.append(f"| **Épica** | [{epic.get('System.Title','')}]({ado_url(epic['_id'])}) |")
    if feature: lines.append(f"| **Feature** | [{feature.get('System.Title','')}]({ado_url(feature['_id'])}) |")
    lines.append("")

    if desc:
        lines.append("## Descripción\n")
        lines.append(desc)
        lines.append("")

    if acrit:
        lines.append("## Criterios de Aceptación\n")
        lines.append(acrit)
        lines.append("")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# ÍNDICES
# ─────────────────────────────────────────────

def write_feature_index(path: str, feature: Optional[dict], stories: list[dict], epic: Optional[dict]):
    lines = []
    if feature:
        fid = feature["_id"]
        lines.append(f"# Feature {fid} — {feature.get('System.Title','')}\n")
        lines.append(f"[Ver en Azure DevOps]({ado_url(fid)})\n")
        fstate = feature.get("System.State", "")
        fpts   = feature.get("Microsoft.VSTS.Scheduling.StoryPoints", "")
        if fstate or fpts:
            meta = []
            if fstate: meta.append(f"**Estado:** {fstate}")
            if fpts:   meta.append(f"**Puntos:** {fpts}")
            lines.append("  \n".join(meta) + "\n")
    else:
        lines.append("# Sin Feature\n")

    lines.append("## Historias de Usuario\n")
    lines.append("| ID | Título | Estado | Puntos |")
    lines.append("|----|--------|--------|--------|")
    for s in sorted(stories, key=lambda x: x.get("_id", 0)):
        sid   = s.get("_id", "")
        stit  = s.get("System.Title", "")
        sst   = s.get("System.State", "")
        spts  = s.get("Microsoft.VSTS.Scheduling.StoryPoints", "")
        fname = hu_filename(s)
        lines.append(f"| [{sid}]({ado_url(sid)}) | [{stit}]({fname}) | {sst} | {spts} |")
    lines.append("")

    with open(os.path.join(path, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_epic_index(path: str, epic: Optional[dict], features_map: dict):
    lines = []
    if epic:
        eid = epic["_id"]
        lines.append(f"# Épica {eid} — {epic.get('System.Title','')}\n")
        lines.append(f"[Ver en Azure DevOps]({ado_url(eid)})\n")
        estate = epic.get("System.State", "")
        if estate:
            lines.append(f"**Estado:** {estate}\n")
    else:
        lines.append("# Sin Épica\n")

    lines.append("## Features\n")
    for feat_data, stories in features_map:
        if feat_data:
            fid   = feat_data["_id"]
            ftit  = feat_data.get("System.Title", "")
            fst   = feat_data.get("System.State", "")
            fpts  = feat_data.get("Microsoft.VSTS.Scheduling.StoryPoints", "")
            fname = feature_folder(feat_data)
            lines.append(f"### [{ftit}]({fname}/index.md) — [{fid}]({ado_url(fid)})")
            meta  = []
            if fst:   meta.append(f"Estado: {fst}")
            if fpts:  meta.append(f"Puntos: {fpts}")
            if meta:  lines.append(f"_{' | '.join(meta)}_")
        else:
            lines.append("### Sin Feature")

        lines.append("")
        lines.append("| ID | Título | Estado |")
        lines.append("|----|--------|--------|")
        for s in sorted(stories, key=lambda x: x.get("_id", 0)):
            fdir  = feature_folder(feat_data)
            hfile = hu_filename(s)
            sid   = s.get("_id", "")
            stit  = s.get("System.Title", "")
            sst   = s.get("System.State", "")
            lines.append(f"| [{sid}]({ado_url(sid)}) | [{stit}]({fdir}/{hfile}) | {sst} |")
        lines.append("")

    with open(os.path.join(path, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_root_index(path: str, tree: dict):
    lines = []
    lines.append("# Backlog — Fortalecimiento SARLAFT 4.0\n")
    lines.append(f"**Proyecto:** {PROJECT}  ")
    lines.append(f"**Equipo:** {TEAM}  ")
    lines.append(f"**Fecha:** 2026-04-07\n")
    lines.append("---\n")

    total_hu = sum(
        len(stories)
        for epic_entry in tree.values()
        for _, stories in epic_entry["features"]
    )
    lines.append(f"**Total Historias:** {total_hu}\n")

    for epic_id, epic_entry in sorted(tree.items(), key=lambda x: x[0]):
        epic_d  = epic_entry["epic"]
        ef      = epic_folder(epic_d)
        if epic_d:
            eid   = epic_d["_id"]
            etit  = epic_d.get("System.Title", "")
            lines.append(f"## [{etit}]({ef}/index.md) — [{eid}]({ado_url(eid)})")
        else:
            lines.append(f"## [Sin Épica]({ef}/index.md)")
        lines.append("")
        for feat_data, stories in epic_entry["features"]:
            fdir = feature_folder(feat_data)
            if feat_data:
                fid  = feat_data["_id"]
                ftit = feat_data.get("System.Title", "")
                lines.append(f"- **[{ftit}]({ef}/{fdir}/index.md)** [{fid}]({ado_url(fid)}) — {len(stories)} HUs")
            else:
                lines.append(f"- **[Sin Feature]({ef}/{fdir}/index.md)** — {len(stories)} HUs")
        lines.append("")

    with open(os.path.join(path, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print(f"🔎  Obteniendo área del equipo…")
    area_path = get_area_path()
    print(f"    Área: {area_path}")

    print("📋  Consultando HUs vía WIQL…")
    hu_ids = wiql_hu(area_path)
    print(f"    Encontradas {len(hu_ids)} historias.")

    print("⬇️  Descargando work-items y jerarquía…")
    cache = build_cache(hu_ids)

    print("🗂️  Construyendo árbol Épica → Feature → HU…")
    # tree: { epic_id: { "epic": epic_fields, "features": { feat_id: { "feature": feat_fields, "stories": [...] } } } }
    tree_raw: dict = {}

    for hu_id in hu_ids:
        hu = cache.get(hu_id)
        if not hu:
            continue
        epic, feature = resolve_parents(hu_id, cache)

        eid = epic["_id"]    if epic    else 0
        fid = feature["_id"] if feature else 0

        if eid not in tree_raw:
            tree_raw[eid] = {"epic": epic, "features": {}}
        eb = tree_raw[eid]

        if fid not in eb["features"]:
            eb["features"][fid] = {"feature": feature, "stories": []}
        eb["features"][fid]["stories"].append(hu)

    # ── Crear carpetas y ficheros ────────────────────────────────────────
    os.makedirs(OUT_ROOT, exist_ok=True)
    created_files = 0
    created_dirs  = 0

    # Preparar estructura para índice raíz
    tree_for_index = {}

    for eid, epic_entry in sorted(tree_raw.items()):
        epic_d  = epic_entry["epic"]
        ep_path = os.path.join(OUT_ROOT, epic_folder(epic_d))
        os.makedirs(ep_path, exist_ok=True)
        created_dirs += 1

        features_for_epic = []

        for fid, feat_entry in sorted(epic_entry["features"].items()):
            feat_d   = feat_entry["feature"]
            stories  = feat_entry["stories"]
            ft_path  = os.path.join(ep_path, feature_folder(feat_d))
            os.makedirs(ft_path, exist_ok=True)
            created_dirs += 1

            # Escribir HU individuales
            for story in stories:
                fn    = hu_filename(story)
                fpath = os.path.join(ft_path, fn)
                content = render_hu(story, epic_d, feat_d)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                created_files += 1

            # Índice de feature
            write_feature_index(ft_path, feat_d, stories, epic_d)
            features_for_epic.append((feat_d, stories))

        # Índice de épica
        write_epic_index(ep_path, epic_d, features_for_epic)

        tree_for_index[eid] = {
            "epic":     epic_d,
            "features": features_for_epic,
        }

    # Índice raíz
    write_root_index(OUT_ROOT, tree_for_index)

    print(f"\n✅  Estructura generada en: {OUT_ROOT}")
    print(f"    Carpetas creadas : {created_dirs}")
    print(f"    Archivos HU .md  : {created_files}")
    print(f"    Épicas           : {len(tree_raw)}")
    print(f"    Features totales : {sum(len(e['features']) for e in tree_raw.values())}")


if __name__ == "__main__":
    main()
