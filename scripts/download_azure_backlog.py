"""
Descarga las HUs del backlog de Azure DevOps:
  https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_backlogs/backlog/
  do-soluci_corporativas-Fortalecimiento%20SARLAFT/Historias

Organiza la salida por Épica → Feature → Historia de Usuario
y genera un archivo Markdown en docs/core/Backlog_HU.md
"""

import base64
import json
import os
import sys
import time
import textwrap
from typing import Optional

import requests

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
ORG       = "SuraColombia"
PROJECT   = "Gerencia_Tecnologia"
TEAM      = "do-soluci_corporativas-Fortalecimiento SARLAFT"
PAT       = os.getenv("ADO_PAT", "3KDIrWMhH2CsFRo2VcVqfTffqiRT4jW3PQ7RU4tC97XJxpLBIUS4JQQJ99CDACAAAAA5G0YpAAASAZDO16Bk")
API_VER   = "7.1"
OUT_FILE  = os.path.join(os.path.dirname(__file__), "..", "docs", "core", "Backlog_HU.md")
BATCH     = 200   # máx. IDs por llamada a workitemsbatch

_b64 = base64.b64encode(f":{PAT}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {_b64}",
    "Content-Type":  "application/json",
    "Accept":        "application/json",
}

BASE = f"https://dev.azure.com/{ORG}"
VSRM = f"https://vsrm.dev.azure.com/{ORG}"


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def get(url: str, params: dict = None) -> dict:
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    if r.status_code == 401:
        print("❌  401 Unauthorized — PAT inválido o sin permisos suficientes.")
        sys.exit(1)
    r.raise_for_status()
    return r.json()


def post(url: str, body: dict) -> dict:
    r = requests.post(url, headers=HEADERS, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_work_items_batch(ids: list[int]) -> list[dict]:
    """Trae detalles de hasta BATCH work-items por llamada."""
    fields = [
        "System.Id",
        "System.Title",
        "System.WorkItemType",
        "System.State",
        "System.AreaPath",
        "System.IterationPath",
        "System.AssignedTo",
        "System.Parent",
        "Microsoft.VSTS.Common.Priority",
        "Microsoft.VSTS.Scheduling.StoryPoints",
        "System.Description",
        "System.Tags",
        "Microsoft.VSTS.Common.AcceptanceCriteria",
    ]
    result = []
    for i in range(0, len(ids), BATCH):
        chunk = ids[i : i + BATCH]
        body = {"ids": chunk, "fields": fields}
        url  = f"{BASE}/{PROJECT}/_apis/wit/workitemsbatch?api-version={API_VER}"
        data = post(url, body)
        result.extend(data.get("value", []))
        time.sleep(0.1)   # cortesía con el API
    return result


def wiql_hu(area_path: str) -> list[int]:
    """Trae IDs de Historias de Usuario en el área del equipo."""
    # Limpiamos la ruta de área para WIQL
    safe_area = area_path.replace("'", "''")
    query = {
        "query": (
            "SELECT [System.Id] FROM WorkItems "
            f"WHERE [System.TeamProject] = '{PROJECT}' "
            f"  AND [System.AreaPath] UNDER '{safe_area}' "
            "  AND [System.WorkItemType] IN ('Historia de Usuario', 'User Story', 'Historia') "
            "  AND [System.State] <> 'Eliminado' "
            "ORDER BY [System.Id] ASC"
        )
    }
    url  = f"{BASE}/{PROJECT}/_apis/wit/wiql?api-version={API_VER}"
    data = post(url, query)
    return [wi["id"] for wi in data.get("workItems", [])]


def get_area_path_for_team() -> str:
    """Obtiene el área de iteración asociada al equipo."""
    url = f"{BASE}/{PROJECT}/{requests.utils.quote(TEAM)}/_apis/work/teamsettings/teamfieldvalues?api-version={API_VER}"
    try:
        data = get(url)
        values = data.get("values", [])
        if values:
            return values[0].get("value", f"{PROJECT}\\{TEAM}")
    except Exception:
        pass
    return PROJECT


def get_parent_chain(item_id: int, cache: dict) -> tuple[Optional[dict], Optional[dict]]:
    """
    Dado un work-item, sube por la cadena de padres hasta encontrar Feature y Épica.
    Devuelve (feature_dict, epic_dict) — puede ser None si no existe.
    """
    feature = None
    epic    = None

    def fetch_single(wid: int) -> Optional[dict]:
        if wid in cache:
            return cache[wid]
        try:
            data = get(
                f"{BASE}/{PROJECT}/_apis/wit/workitems/{wid}",
                params={"fields": "System.Id,System.Title,System.WorkItemType,System.Parent,"
                                   "Microsoft.VSTS.Scheduling.StoryPoints,System.State,"
                                   "Microsoft.VSTS.Common.Priority",
                        "api-version": API_VER},
            )
            cache[wid] = data.get("fields", {})
            cache[wid]["_id"] = wid
            return cache[wid]
        except Exception:
            return None

    current_id = item_id
    depth = 0
    while depth < 5:
        item = cache.get(current_id)
        if not item:
            break
        parent_id = item.get("System.Parent")
        if not parent_id:
            break
        parent = fetch_single(parent_id)
        if not parent:
            break
        wtype = parent.get("System.WorkItemType", "")
        if "Feature" in wtype or "Característica" in wtype:
            feature = parent
        elif "Epic" in wtype or "Épica" in wtype or "Epica" in wtype:
            epic = parent
            break
        # si el padre del feature es una épica
        if feature:
            grandparent_id = parent.get("System.Parent")
            if grandparent_id:
                grandparent = fetch_single(grandparent_id)
                if grandparent:
                    gt = grandparent.get("System.WorkItemType", "")
                    if "Epic" in gt or "Épica" in gt or "Epica" in gt:
                        epic = grandparent
            break
        current_id = parent_id
        depth += 1
    return feature, epic


def clean_html(text: Optional[str]) -> str:
    """Limpieza básica de HTML para Markdown."""
    if not text:
        return ""
    import re
    # Reemplazar etiquetas comunes
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<p[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<li[^>]*>", "\n- ", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<ul[^>]*>|</ul>|<ol[^>]*>|</ol>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)   # quitar resto de tags
    text = text.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&#160;", " ")
    # Colapsar líneas en blanco múltiples
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def make_ado_url(item_id: int) -> str:
    return f"https://dev.azure.com/{ORG}/{PROJECT}/_workitems/edit/{item_id}"


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

def main():
    print(f"🔎  Obteniendo área del equipo '{TEAM}'…")
    area_path = get_area_path_for_team()
    print(f"    Área: {area_path}")

    print("📋  Ejecutando WIQL para Historias de Usuario…")
    hu_ids = wiql_hu(area_path)

    # Si el WIQL de área no devuelve nada, intentar con el nombre del proyecto solo
    if not hu_ids:
        print("    Sin resultados con área de equipo, intentando con proyecto completo…")
        query = {
            "query": (
                "SELECT [System.Id] FROM WorkItems "
                f"WHERE [System.TeamProject] = '{PROJECT}' "
                "  AND [System.WorkItemType] IN ('Historia de Usuario', 'User Story', 'Historia') "
                "  AND [System.State] <> 'Eliminado' "
                "  AND [System.Tags] CONTAINS 'SARLAFT' "
                "ORDER BY [System.Id] ASC"
            )
        }
        url  = f"{BASE}/{PROJECT}/_apis/wit/wiql?api-version={API_VER}"
        data = post(url, query)
        hu_ids = [wi["id"] for wi in data.get("workItems", [])]

    print(f"    Encontradas {len(hu_ids)} historias.")
    if not hu_ids:
        print("⚠️  No se encontraron historias. Verifique el área del equipo.")
        sys.exit(0)

    print("⬇️  Descargando detalles de work-items…")
    items_raw = fetch_work_items_batch(hu_ids)

    # cache id → fields
    cache: dict = {}
    for item in items_raw:
        flds = item.get("fields", {})
        flds["_id"] = item["id"]
        cache[item["id"]] = flds

    # ── Construir jerarquía Épica > Feature > HU ──────────────────────────
    print("🗂️  Construyendo jerarquía Épica → Feature → Historia…")

    # Primero, recopilar todos los parent IDs únicos que necesitamos pre-cargar
    parent_ids_needed = set()
    for flds in cache.values():
        pid = flds.get("System.Parent")
        if pid and pid not in cache:
            parent_ids_needed.add(pid)

    if parent_ids_needed:
        print(f"    Pre-cargando {len(parent_ids_needed)} padres (Features/Épicas)…")
        parents_raw = fetch_work_items_batch(list(parent_ids_needed))
        for item in parents_raw:
            flds = item.get("fields", {})
            flds["_id"] = item["id"]
            cache[item["id"]] = flds

        # También pre-cargar padres de Features (las Épicas)
        grandparent_ids = set()
        for pid in parent_ids_needed:
            if pid in cache:
                gid = cache[pid].get("System.Parent")
                if gid and gid not in cache:
                    grandparent_ids.add(gid)
        if grandparent_ids:
            print(f"    Pre-cargando {len(grandparent_ids)} abuelos (Épicas)…")
            gp_raw = fetch_work_items_batch(list(grandparent_ids))
            for item in gp_raw:
                flds = item.get("fields", {})
                flds["_id"] = item["id"]
                cache[item["id"]] = flds

    # Estructura: epic_id → { "data": ..., "features": { feature_id → { "data": ..., "stories": [...] } } }
    tree        = {}   # epic_id → {...}
    no_epic     = {"data": {"System.Title": "Sin Épica", "_id": 0}, "features": {}}
    no_feature  = lambda epic_id: {"data": {"System.Title": "Sin Feature", "_id": 0}, "stories": []}

    def epic_bucket(epic_data):
        eid = epic_data["_id"] if epic_data else 0
        if eid not in tree:
            tree[eid] = {"data": epic_data or {"System.Title": "Sin Épica", "_id": 0}, "features": {}}
        return tree[eid]

    def feature_bucket(epic_bucket_ref, feature_data):
        fid = feature_data["_id"] if feature_data else 0
        eb  = epic_bucket_ref["features"]
        if fid not in eb:
            eb[fid] = {"data": feature_data or {"System.Title": "Sin Feature", "_id": 0}, "stories": []}
        return eb[fid]

    for hu_id in hu_ids:
        flds = cache.get(hu_id)
        if not flds:
            continue
        feature, epic = get_parent_chain(hu_id, cache)
        eb  = epic_bucket(epic)
        fb  = feature_bucket(eb, feature)
        fb["stories"].append(flds)

    # ── Escribir Markdown ────────────────────────────────────────────────
    print(f"📝  Generando Markdown en {OUT_FILE}…")
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

    lines = []
    lines.append("# Backlog — Historias de Usuario")
    lines.append(f"\n**Proyecto:** {PROJECT}  ")
    lines.append(f"**Equipo:** {TEAM}  ")
    lines.append(f"**Fecha de descarga:** 2026-04-07  ")
    lines.append(f"**Total Historias:** {len(hu_ids)}\n")
    lines.append("---\n")

    epics_sorted = sorted(tree.values(), key=lambda e: e["data"].get("_id", 0))

    for epic_entry in epics_sorted:
        epic_d = epic_entry["data"]
        epic_id    = epic_d.get("_id", 0)
        epic_title = epic_d.get("System.Title", "Sin Épica")
        epic_state = epic_d.get("System.State", "")

        if epic_id:
            lines.append(f"## 🗂 Épica [{epic_id}]({make_ado_url(epic_id)}) — {epic_title}")
        else:
            lines.append(f"## 🗂 Sin Épica")
        if epic_state:
            lines.append(f"**Estado:** {epic_state}\n")
        else:
            lines.append("")

        features_sorted = sorted(epic_entry["features"].values(), key=lambda f: f["data"].get("_id", 0))

        for feat_entry in features_sorted:
            feat_d = feat_entry["data"]
            feat_id    = feat_d.get("_id", 0)
            feat_title = feat_d.get("System.Title", "Sin Feature")
            feat_state = feat_d.get("System.State", "")
            feat_pts   = feat_d.get("Microsoft.VSTS.Scheduling.StoryPoints", "")

            if feat_id:
                lines.append(f"### Feature [{feat_id}]({make_ado_url(feat_id)}) — {feat_title}")
            else:
                lines.append(f"### Sin Feature")

            meta_feat = []
            if feat_state: meta_feat.append(f"Estado: {feat_state}")
            if feat_pts:   meta_feat.append(f"Puntos: {feat_pts}")
            if meta_feat:
                lines.append(f"_{' | '.join(meta_feat)}_\n")
            else:
                lines.append("")

            stories_sorted = sorted(feat_entry["stories"], key=lambda s: s.get("_id", 0))

            for story in stories_sorted:
                sid    = story.get("_id", "")
                stitle = story.get("System.Title", "Sin título")
                sstate = story.get("System.State", "")
                spts   = story.get("Microsoft.VSTS.Scheduling.StoryPoints", "")
                sprio  = story.get("Microsoft.VSTS.Common.Priority", "")
                sassig = story.get("System.AssignedTo", {})
                siter  = story.get("System.IterationPath", "")
                stags  = story.get("System.Tags", "")
                sdesc  = clean_html(story.get("System.Description", ""))
                sacrit = clean_html(story.get("Microsoft.VSTS.Common.AcceptanceCriteria", ""))

                if isinstance(sassig, dict):
                    sassig = sassig.get("displayName", "")

                lines.append(f"#### HU [{sid}]({make_ado_url(sid)}) — {stitle}")

                meta = []
                if sstate: meta.append(f"**Estado:** {sstate}")
                if spts:   meta.append(f"**Puntos:** {spts}")
                if sprio:  meta.append(f"**Prioridad:** {sprio}")
                if sassig: meta.append(f"**Asignado:** {sassig}")
                if siter:  meta.append(f"**Iteración:** `{siter}`")
                if stags:  meta.append(f"**Tags:** {stags}")
                if meta:
                    lines.append("  \n".join(meta))
                    lines.append("")

                if sdesc:
                    lines.append("**Descripción:**")
                    lines.append(textwrap.indent(sdesc, "> "))
                    lines.append("")

                if sacrit:
                    lines.append("**Criterios de Aceptación:**")
                    lines.append(textwrap.indent(sacrit, "> "))
                    lines.append("")

                lines.append("---")
            lines.append("")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅  Archivo generado: {OUT_FILE}")
    print(f"    Épicas: {len([e for e in tree if e > 0])}")
    print(f"    Features totales: {sum(len(e['features']) for e in tree.values())}")
    print(f"    Historias: {len(hu_ids)}")


if __name__ == "__main__":
    main()
