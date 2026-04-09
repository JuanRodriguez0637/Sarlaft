"""
Descarga las HU's del backlog de Azure DevOps:
  https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_backlogs/backlog/
  do-soluci_corporativas-Fortalecimiento%20SARLAFT/Historias

Genera un archivo .md individual por cada HU, organizado en:
  docs/Epica {id} - {titulo}/Feature {id} - {titulo}/HU {id} - {titulo}.md
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

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
ORG      = "SuraColombia"
PROJECT  = "Gerencia_Tecnologia"
TEAM     = "do-soluci_corporativas-Fortalecimiento SARLAFT"
PAT      = os.getenv("ADO_PAT", "3KDIrWMhH2CsFRo2VcVqfTffqiRT4jW3PQ7RU4tC97XJxpLBIUS4JQQJ99CDACAAAAA5G0YpAAASAZDO16Bk")
API_VER  = "7.1"
DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
BATCH    = 200

_b64 = base64.b64encode(f":{PAT}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {_b64}",
    "Content-Type":  "application/json",
    "Accept":        "application/json",
}

BASE = f"https://dev.azure.com/{ORG}"

WI_FIELDS = [
    "System.Id",
    "System.Title",
    "System.WorkItemType",
    "System.State",
    "System.AreaPath",
    "System.IterationPath",
    "System.AssignedTo",
    "System.Parent",
    "System.Tags",
    "System.Description",
    "Microsoft.VSTS.Common.Priority",
    "Microsoft.VSTS.Scheduling.StoryPoints",
    "Microsoft.VSTS.Common.AcceptanceCriteria",
    "System.CreatedDate",
    "System.ChangedDate",
]


# ──────────────────────────────────────────────
# HTTP HELPERS
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


def fetch_work_items_batch(ids: list) -> list:
    """Descarga detalles de work-items en lotes de BATCH."""
    result = []
    for i in range(0, len(ids), BATCH):
        chunk = ids[i: i + BATCH]
        body = {"ids": chunk, "fields": WI_FIELDS}
        url = f"{BASE}/{PROJECT}/_apis/wit/workitemsbatch?api-version={API_VER}"
        data = post(url, body)
        result.extend(data.get("value", []))
        time.sleep(0.1)
    return result


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def safe_name(text: str, max_len: int = 60) -> str:
    """Convierte un título en un nombre de archivo/carpeta seguro."""
    text = text.strip()
    # Reemplazar caracteres no permitidos en rutas de Windows
    text = re.sub(r'[\\/:*?"<>|\[\]{}]', " ", text)
    # Colapsar espacios múltiples
    text = re.sub(r"\s+", " ", text).strip()
    # Truncar si es muy largo
    if len(text) > max_len:
        text = text[:max_len].rstrip()
    return text


def clean_html(text: Optional[str]) -> str:
    """Convierte HTML básico a Markdown."""
    if not text:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<p[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<li[^>]*>", "\n- ", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<ul[^>]*>|</ul>|<ol[^>]*>|</ol>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    text = (text
            .replace("&nbsp;", " ")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&amp;", "&")
            .replace("&#160;", " ")
            .replace("&quot;", '"'))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def make_ado_url(item_id: int) -> str:
    return f"https://dev.azure.com/{ORG}/{PROJECT}/_workitems/edit/{item_id}"


def display_name(assigned_to) -> str:
    if isinstance(assigned_to, dict):
        return assigned_to.get("displayName", "")
    return str(assigned_to) if assigned_to else ""


# ──────────────────────────────────────────────
# WIQL QUERY
# ──────────────────────────────────────────────

def get_area_path() -> str:
    """Obtiene el área configurada para el equipo."""
    import urllib.parse
    url = (f"{BASE}/{PROJECT}/{urllib.parse.quote(TEAM)}"
           f"/_apis/work/teamsettings/teamfieldvalues?api-version={API_VER}")
    try:
        data = get(url)
        values = data.get("values", [])
        if values:
            return values[0].get("value", PROJECT)
    except Exception:
        pass
    return PROJECT


def wiql_all_in_area(area_path: str) -> list:
    """Obtiene todos los IDs de work-items en el área del equipo."""
    safe_area = area_path.replace("'", "''")
    query = {
        "query": (
            "SELECT [System.Id] FROM WorkItems "
            f"WHERE [System.TeamProject] = '{PROJECT}' "
            f"  AND [System.AreaPath] UNDER '{safe_area}' "
            "  AND [System.State] <> 'Eliminado' "
            "ORDER BY [System.Id] ASC"
        )
    }
    url = f"{BASE}/{PROJECT}/_apis/wit/wiql?api-version={API_VER}"
    data = post(url, query)
    return [wi["id"] for wi in data.get("workItems", [])]


# ──────────────────────────────────────────────
# MARKDOWN GENERATION
# ──────────────────────────────────────────────

def build_hu_markdown(hu: dict, feature: Optional[dict], epic: Optional[dict]) -> str:
    """Construye el contenido Markdown para una HU."""
    sid    = hu.get("_id", "")
    stitle = hu.get("System.Title", "Sin título")
    sstate = hu.get("System.State", "")
    spts   = hu.get("Microsoft.VSTS.Scheduling.StoryPoints", "")
    sprio  = hu.get("Microsoft.VSTS.Common.Priority", "")
    sassig = display_name(hu.get("System.AssignedTo", ""))
    sarea  = hu.get("System.AreaPath", "")
    siter  = hu.get("System.IterationPath", "")
    stags  = hu.get("System.Tags", "")
    sdesc  = clean_html(hu.get("System.Description", ""))
    sacrit = clean_html(hu.get("Microsoft.VSTS.Common.AcceptanceCriteria", ""))
    screated = hu.get("System.CreatedDate", "")[:10] if hu.get("System.CreatedDate") else ""
    schanged = hu.get("System.ChangedDate", "")[:10] if hu.get("System.ChangedDate") else ""

    lines = []

    # Encabezado
    lines.append(f"# HU {sid} — {stitle}")
    lines.append("")

    # Breadcrumb de navegación
    bc_parts = []
    if epic:
        eid = epic.get("_id", "")
        etitle = epic.get("System.Title", "Sin Épica")
        bc_parts.append(f"[Épica {eid} — {etitle}]({make_ado_url(eid)})")
    if feature:
        fid = feature.get("_id", "")
        ftitle = feature.get("System.Title", "Sin Feature")
        bc_parts.append(f"[Feature {fid} — {ftitle}]({make_ado_url(fid)})")
    bc_parts.append(f"HU {sid} — {stitle}")
    lines.append(" › ".join(bc_parts))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Metadata
    lines.append("## Información General")
    lines.append("")
    lines.append(f"| Campo | Valor |")
    lines.append(f"|-------|-------|")
    lines.append(f"| **ID** | [{sid}]({make_ado_url(sid)}) |")
    lines.append(f"| **Estado** | {sstate} |")
    if spts:
        lines.append(f"| **Story Points** | {spts} |")
    if sprio:
        lines.append(f"| **Prioridad** | {sprio} |")
    if sassig:
        lines.append(f"| **Asignado a** | {sassig} |")
    if siter:
        lines.append(f"| **Iteración** | `{siter}` |")
    if sarea:
        lines.append(f"| **Área** | `{sarea}` |")
    if stags:
        lines.append(f"| **Tags** | {stags} |")
    if screated:
        lines.append(f"| **Creado** | {screated} |")
    if schanged:
        lines.append(f"| **Última modificación** | {schanged} |")
    lines.append("")

    # Épica y Feature de referencia
    if epic or feature:
        lines.append("## Jerarquía")
        lines.append("")
        if epic:
            eid = epic.get("_id", "")
            lines.append(f"- **Épica:** [{eid} — {epic.get('System.Title', '')}]({make_ado_url(eid)})  ")
            lines.append(f"  Estado: {epic.get('System.State', '')}  ")
        if feature:
            fid = feature.get("_id", "")
            lines.append(f"- **Feature:** [{fid} — {feature.get('System.Title', '')}]({make_ado_url(fid)})  ")
            lines.append(f"  Estado: {feature.get('System.State', '')}  ")
            fpts = feature.get("Microsoft.VSTS.Scheduling.StoryPoints", "")
            if fpts:
                lines.append(f"  Story Points: {fpts}  ")
        lines.append("")

    # Descripción
    if sdesc:
        lines.append("## Descripción")
        lines.append("")
        lines.append(sdesc)
        lines.append("")

    # Criterios de Aceptación
    if sacrit:
        lines.append("## Criterios de Aceptación")
        lines.append("")
        lines.append(sacrit)
        lines.append("")

    return "\n".join(lines)


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

def main():
    print(f"🔎  Obteniendo área del equipo '{TEAM}'…")
    area_path = get_area_path()
    print(f"    Área: {area_path}")

    print("📋  Ejecutando WIQL en el área del equipo…")
    all_ids = wiql_all_in_area(area_path)
    print(f"    Total work-items en área: {len(all_ids)}")

    if not all_ids:
        print("⚠️  No se encontraron work-items. Verifique el área del equipo.")
        sys.exit(0)

    print("⬇️  Descargando detalles de work-items…")
    items_raw = fetch_work_items_batch(all_ids)

    # cache id → fields
    cache: dict = {}
    for item in items_raw:
        flds = item.get("fields", {})
        flds["_id"] = item["id"]
        cache[item["id"]] = flds

    # Separar por tipo
    hu_ids       = []
    feature_ids  = []
    epic_ids     = []

    for wid, flds in cache.items():
        wtype = flds.get("System.WorkItemType", "")
        if "Historia" in wtype or "User Story" in wtype:
            hu_ids.append(wid)
        elif "Feature" in wtype or "Característica" in wtype:
            feature_ids.append(wid)
        elif "Epic" in wtype or "Épica" in wtype or "Epica" in wtype:
            epic_ids.append(wid)

    print(f"    Épicas: {len(epic_ids)} | Features: {len(feature_ids)} | HUs: {len(hu_ids)}")

    # Para cada HU, obtener padres que falten en el cache
    missing_parents = set()
    for wid in hu_ids:
        flds = cache[wid]
        pid = flds.get("System.Parent")
        if pid and pid not in cache:
            missing_parents.add(pid)

    if missing_parents:
        print(f"    Pre-cargando {len(missing_parents)} padres adicionales…")
        extra = fetch_work_items_batch(list(missing_parents))
        for item in extra:
            flds = item.get("fields", {})
            flds["_id"] = item["id"]
            cache[item["id"]] = flds

        missing_gps = set()
        for pid in missing_parents:
            if pid in cache:
                gid = cache[pid].get("System.Parent")
                if gid and gid not in cache:
                    missing_gps.add(gid)
        if missing_gps:
            print(f"    Pre-cargando {len(missing_gps)} abuelos adicionales…")
            gp_extra = fetch_work_items_batch(list(missing_gps))
            for item in gp_extra:
                flds = item.get("fields", {})
                flds["_id"] = item["id"]
                cache[item["id"]] = flds

    def resolve_hierarchy(hu_id: int):
        """Sube la cadena de padres y devuelve (feature, epic)."""
        flds = cache.get(hu_id, {})
        parent1_id = flds.get("System.Parent")
        feature = None
        epic = None

        if not parent1_id:
            return None, None

        p1 = cache.get(parent1_id)
        if not p1:
            return None, None

        wtype1 = p1.get("System.WorkItemType", "")
        if "Feature" in wtype1 or "Característica" in wtype1:
            feature = p1
            parent2_id = p1.get("System.Parent")
            if parent2_id:
                p2 = cache.get(parent2_id)
                if p2:
                    wtype2 = p2.get("System.WorkItemType", "")
                    if "Epic" in wtype2 or "Épica" in wtype2 or "Epica" in wtype2:
                        epic = p2
        elif "Epic" in wtype1 or "Épica" in wtype1 or "Epica" in wtype1:
            epic = p1

        return feature, epic

    # ── Generar archivos ──────────────────────────────────────────────────
    print(f"\n📁  Generando estructura de archivos en: {os.path.abspath(DOCS_DIR)}")

    created = 0
    skipped = 0

    for hu_id in sorted(hu_ids):
        hu = cache[hu_id]
        feature, epic = resolve_hierarchy(hu_id)

        hu_id_str    = str(hu.get("_id", hu_id))
        hu_title     = hu.get("System.Title", "Sin título")
        hu_folder_name = safe_name(f"HU {hu_id_str} - {hu_title}")

        # Determinar carpeta de la Épica
        if epic:
            epic_id_str   = str(epic.get("_id", "0"))
            epic_title    = epic.get("System.Title", "Sin Épica")
            epic_dir_name = safe_name(f"Epica {epic_id_str} - {epic_title}")
        else:
            epic_dir_name = "Sin Epica"

        # Determinar carpeta de la Feature
        if feature:
            feat_id_str   = str(feature.get("_id", "0"))
            feat_title    = feature.get("System.Title", "Sin Feature")
            feat_dir_name = safe_name(f"Feature {feat_id_str} - {feat_title}")
        else:
            feat_dir_name = "Sin Feature"

        # Ruta completa del archivo
        target_dir  = os.path.join(DOCS_DIR, epic_dir_name, feat_dir_name)
        target_file = os.path.join(target_dir, f"{hu_folder_name}.md")

        os.makedirs(target_dir, exist_ok=True)

        content = build_hu_markdown(hu, feature, epic)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

        created += 1
        rel_path = os.path.relpath(target_file, DOCS_DIR)
        print(f"  ✅  {rel_path}")

    print(f"\n✅  Proceso completado.")
    print(f"    Archivos creados: {created}")
    print(f"    Estructura generada en: docs/")


if __name__ == "__main__":
    main()
