"""
Consulta todas las HU's del backlog SARLAFT via Azure DevOps REST API,
analiza su completitud y genera docs/HU_Status.md
"""

import base64
import json
import os
import re
import sys
import time
from typing import Optional

import requests

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
ORG      = "SuraColombia"
PROJECT  = "Gerencia_Tecnologia"
TEAM     = "do-soluci_corporativas-Fortalecimiento SARLAFT"
PAT      = os.getenv("ADO_PAT", "8IQW0HAxAuiFBRVGxsjnszkJlehMa6Fw1HfckQJ9oxkPSJdQszX0JQQJ99CDACAAAAA5G0YpAAASAZDO3vMd")
HU_TYPES = ["Historia", "Historia t\u00e9cnica"]
API_VER  = "7.1"
OUT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "HU_Status.md"))
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
    "System.AssignedTo",
    "System.Parent",
    "System.Tags",
    "System.Description",
    "System.IterationPath",
    "Microsoft.VSTS.Common.Priority",
    "Microsoft.VSTS.Scheduling.StoryPoints",
    "Microsoft.VSTS.Common.AcceptanceCriteria",
    "System.CreatedDate",
    "System.ChangedDate",
]

# ──────────────────────────────────────────────
# CRITERIOS DE COMPLETITUD — dos niveles
#
# NIVEL 1 — Contenido (campos funcionales mínimos):
#   1. Descripción (texto real, no vacío)
#   2. Criterios de Aceptación
#
# NIVEL 2 — Refinamiento completo:
#   3. Story Points estimados
#   4. Asignado a alguien
#   5. Estado distinto de "New"
# ──────────────────────────────────────────────

# Criterios de contenido (obligatorios para estar "completa")
CRITERIOS_CONTENIDO = {
    "descripcion":  "Descripción",
    "criterios":    "Criterios de Aceptación",
}

# Criterios adicionales de refinamiento
CRITERIOS_REFINAMIENTO = {
    "story_points": "Story Points",
    "asignado":     "Asignado",
    "estado":       "Estado ≠ New",
}


def has_text(value: Optional[str], min_len: int = 20) -> bool:
    if not value:
        return False
    clean = re.sub(r"<[^>]+>", "", value).strip()
    clean = clean.replace("&nbsp;", " ").replace("&#160;", " ")
    return len(clean) >= min_len


def evaluate(fields: dict) -> dict:
    """Devuelve dict {criterio: True/False} para una HU."""
    return {
        "descripcion":  has_text(fields.get("System.Description")),
        "criterios":    has_text(fields.get("Microsoft.VSTS.Common.AcceptanceCriteria")),
        "story_points": fields.get("Microsoft.VSTS.Scheduling.StoryPoints") not in (None, "", 0),
        "asignado":     bool(fields.get("System.AssignedTo")),
        "estado":       fields.get("System.State", "New") not in ("New", ""),
    }


def is_complete(result: dict) -> bool:
    """Completa = tiene al menos Descripción + Criterios de Aceptación."""
    return result["descripcion"] and result["criterios"]


def is_refined(result: dict) -> bool:
    """Refinada = además tiene Story Points + Asignado + Estado activo."""
    return is_complete(result) and result["story_points"] and result["asignado"] and result["estado"]


# ──────────────────────────────────────────────
# HTTP
# ──────────────────────────────────────────────

def get_json(url: str, params: dict = None) -> dict:
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    if r.status_code == 401:
        print("❌  401 Unauthorized — PAT inválido o expirado.")
        sys.exit(1)
    r.raise_for_status()
    return r.json()


def post_json(url: str, body: dict) -> dict:
    r = requests.post(url, headers=HEADERS, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_batch(ids: list) -> list:
    result = []
    for i in range(0, len(ids), BATCH):
        chunk = ids[i: i + BATCH]
        body = {"ids": chunk, "fields": WI_FIELDS}
        url = f"{BASE}/{PROJECT}/_apis/wit/workitemsbatch?api-version={API_VER}"
        data = post_json(url, body)
        result.extend(data.get("value", []))
        time.sleep(0.1)
    return result


def get_area_path() -> str:
    import urllib.parse
    url = (f"{BASE}/{PROJECT}/{urllib.parse.quote(TEAM)}"
           f"/_apis/work/teamsettings/teamfieldvalues?api-version={API_VER}")
    try:
        data = get_json(url)
        values = data.get("values", [])
        if values:
            return values[0].get("value", PROJECT)
    except Exception:
        pass
    return PROJECT


def wiql_ids(area_path: str, work_item_type: str) -> list:
    safe_area = area_path.replace("'", "''")
    q = (
        f"SELECT [System.Id] FROM WorkItems "
        f"WHERE [System.TeamProject] = '{PROJECT}' "
        f"  AND [System.AreaPath] UNDER '{safe_area}' "
        f"  AND [System.WorkItemType] = '{work_item_type}' "
        f"  AND [System.State] <> 'Eliminado' "
        f"ORDER BY [System.Id] ASC"
    )
    data = post_json(f"{BASE}/{PROJECT}/_apis/wit/wiql?api-version={API_VER}", {"query": q})
    return [wi["id"] for wi in data.get("workItems", [])]


def display_name(val) -> str:
    if isinstance(val, dict):
        return val.get("displayName", "")
    return str(val) if val else ""


def make_url(wid: int) -> str:
    return f"https://dev.azure.com/{ORG}/{PROJECT}/_workitems/edit/{wid}"


# ──────────────────────────────────────────────
# PARENT RESOLUTION (single level up)
# ──────────────────────────────────────────────

def resolve_parents(hu_cache: dict, all_cache: dict) -> dict:
    """Para cada HU en hu_cache, devuelve {hu_id: (feature_title, epic_title)}."""
    # Pre-fetch parents
    parent_ids = set()
    for flds in hu_cache.values():
        pid = flds.get("System.Parent")
        if pid and pid not in all_cache:
            parent_ids.add(pid)

    if parent_ids:
        for item in fetch_batch(list(parent_ids)):
            f = item.get("fields", {}); f["_id"] = item["id"]
            all_cache[item["id"]] = f

    gp_ids = set()
    for pid in parent_ids:
        if pid in all_cache:
            gid = all_cache[pid].get("System.Parent")
            if gid and gid not in all_cache:
                gp_ids.add(gid)
    if gp_ids:
        for item in fetch_batch(list(gp_ids)):
            f = item.get("fields", {}); f["_id"] = item["id"]
            all_cache[item["id"]] = f

    result = {}
    for hu_id, flds in hu_cache.items():
        feature_title = "—"
        epic_title    = "—"
        feature_id = None; epic_id = None

        pid = flds.get("System.Parent")
        if pid and pid in all_cache:
            p = all_cache[pid]
            wtype = p.get("System.WorkItemType", "")
            if "Feature" in wtype or "Característica" in wtype:
                feature_title = p.get("System.Title", "—")
                feature_id    = pid
                gid = p.get("System.Parent")
                if gid and gid in all_cache:
                    g = all_cache[gid]
                    epic_title = g.get("System.Title", "—")
                    epic_id    = gid
            elif "Epic" in wtype or "Épica" in wtype:
                epic_title = p.get("System.Title", "—")
                epic_id    = pid

        result[hu_id] = (feature_title, feature_id, epic_title, epic_id)
    return result


# ──────────────────────────────────────────────
# MARKDOWN
# ──────────────────────────────────────────────

ICON_OK  = "✅"
ICON_NO  = "❌"

def criteria_icons(res: dict) -> str:
    return " ".join(
        f"{ICON_OK if ok else ICON_NO} {CRITERIOS[k]}"
        for k, ok in res.items()
    )


def main():
    print(f"🔎  Obteniendo área del equipo…")
    area = get_area_path()
    print(f"    Área: {area}")

    print("📋  Consultando HUs…")
    hu_ids = []
    for wtype in HU_TYPES:
        ids_tmp = wiql_ids(area, wtype)
        print(f"    {wtype}: {len(ids_tmp)}")
        hu_ids.extend(ids_tmp)
    hu_ids = sorted(set(hu_ids))
    print(f"    Total encontradas: {len(hu_ids)} HUs")
    if not hu_ids:
        print("⚠️  Sin resultados."); sys.exit(0)

    print("⬇️  Descargando detalles…")
    raw = fetch_batch(hu_ids)

    hu_cache: dict = {}
    all_cache: dict = {}
    for item in raw:
        f = item.get("fields", {}); f["_id"] = item["id"]
        hu_cache[item["id"]] = f
        all_cache[item["id"]] = f

    print("🔗  Resolviendo jerarquía…")
    parents = resolve_parents(hu_cache, all_cache)

    # Evaluar completitud
    rows = []
    for hu_id in sorted(hu_ids):
        flds   = hu_cache.get(hu_id, {})
        res    = evaluate(flds)
        complete = is_complete(res)
        refined  = is_refined(res)
        feat_title, feat_id, epic_title, epic_id = parents.get(hu_id, ("—", None, "—", None))
        rows.append({
            "id":          hu_id,
            "title":       flds.get("System.Title", "—"),
            "state":       flds.get("System.State", "—"),
            "points":      flds.get("Microsoft.VSTS.Scheduling.StoryPoints", ""),
            "assigned":    display_name(flds.get("System.AssignedTo")),
            "iteration":   flds.get("System.IterationPath", "").split("\\")[-1],
            "tags":        flds.get("System.Tags", ""),
            "epic_title":  epic_title,
            "epic_id":     epic_id,
            "feat_title":  feat_title,
            "feat_id":     feat_id,
            "criteria":    res,
            "complete":    complete,
            "refined":     refined,
        })

    total        = len(rows)
    n_complete   = sum(1 for r in rows if r["complete"])
    n_refined    = sum(1 for r in rows if r["refined"])
    n_incomplete = total - n_complete
    pct_content  = round(n_complete / total * 100) if total else 0
    pct_refined  = round(n_refined  / total * 100) if total else 0

    # ── Escribir Markdown ──────────────────────────────────────────────
    print(f"📝  Generando {OUT_FILE}…")
    lines = []

    lines += [
        "# Estado de Completitud — Historias de Usuario",
        "",
        f"> **Fecha:** 2026-04-08  |  **Proyecto:** {PROJECT}  |  **Equipo:** {TEAM}",
        "",
        "## Resumen Ejecutivo",
        "",
        f"| Métrica | Valor |",
        f"|---------|-------|",
        f"| Total HUs | **{total}** |",
        f"| ✅ Con contenido completo | **{n_complete}** ({pct_content}%) |",
        f"| ⭐ Refinadas (SP + Asignado + Estado activo) | **{n_refined}** ({pct_refined}%) |",
        f"| ❌ Sin descripción o criterios | **{n_incomplete}** ({100-pct_content}%) |",
        "",
        "### Niveles de completitud",
        "",
        "| Nivel | Criterios |",
        "|-------|-----------|",
        "| ✅ **Contenido completo** | Descripción + Criterios de Aceptación |",
        "| ⭐ **Refinada** | Contenido completo + Story Points + Asignado + Estado ≠ New |",
        "| ❌ **Incompleta** | Falta Descripción y/o Criterios de Aceptación |",
        "",
        "---",
        "",
    ]

    # ── Tabla resumen por estado ──
    estados: dict = {}
    for r in rows:
        estados.setdefault(r["state"], {"total": 0, "completas": 0})
        estados[r["state"]]["total"] += 1
        if r["complete"]:
            estados[r["state"]]["completas"] += 1

    lines += [
        "## Completitud por Estado",
        "",
        "| Estado | Total | Completas | Incompletas |",
        "|--------|-------|-----------|-------------|",
    ]
    for estado, cnt in sorted(estados.items()):
        inc = cnt["total"] - cnt["completas"]
        lines.append(f"| {estado} | {cnt['total']} | {cnt['completas']} | {inc} |")
    lines += ["", "---", ""]

    # ── Épica por épica ──
    from collections import defaultdict
    by_epic: dict = defaultdict(list)
    for r in rows:
        key = (r["epic_id"] or 0, r["epic_title"])
        by_epic[key].append(r)

    lines += [
        "## Detalle por Épica",
        "",
    ]

    for (epic_id, epic_title), epic_rows in sorted(by_epic.items()):
        n_ok  = sum(1 for r in epic_rows if r["complete"])
        n_ref = sum(1 for r in epic_rows if r["refined"])
        n_total = len(epic_rows)
        epic_link = f"[{epic_id}]({make_url(epic_id)}) — {epic_title}" if epic_id else epic_title
        lines += [
            f"### 🗂 Épica {epic_link}",
            "",
            f"_Contenido completo: {n_ok}/{n_total} | Refinadas: {n_ref}/{n_total}_",
            "",
        ]

        # Agrupar por feature
        by_feat: dict = defaultdict(list)
        for r in epic_rows:
            fkey = (r["feat_id"] or 0, r["feat_title"])
            by_feat[fkey].append(r)

        for (feat_id, feat_title), feat_rows in sorted(by_feat.items()):
            feat_ok  = sum(1 for r in feat_rows if r["complete"])
            feat_ref = sum(1 for r in feat_rows if r["refined"])
            feat_link = f"[{feat_id}]({make_url(feat_id)}) — {feat_title}" if feat_id else feat_title
            lines += [
                f"#### Feature {feat_link}",
                "",
                f"_Contenido completo: {feat_ok}/{len(feat_rows)} | Refinadas: {feat_ref}/{len(feat_rows)}_",
                "",
                f"| ID | Título | Estado | SP | Asignado | Nivel | Faltante |",
                f"|----|--------|--------|----|----------|-------|----------|",
            ]
            for r in sorted(feat_rows, key=lambda x: x["id"]):
                if r["refined"]:
                    icon = "⭐"
                elif r["complete"]:
                    icon = "✅"
                else:
                    icon = "❌"
                faltantes = []
                if not r["criteria"]["descripcion"]:  faltantes.append("Descripción")
                if not r["criteria"]["criterios"]:    faltantes.append("Criterios AC")
                if not r["criteria"]["story_points"]: faltantes.append("Story Points")
                if not r["criteria"]["asignado"]:     faltantes.append("Asignado")
                if not r["criteria"]["estado"]:       faltantes.append("Estado")
                faltantes_str = ", ".join(faltantes) or "—"
                hu_link = f"[{r['id']}]({make_url(r['id'])})"
                title_short = r["title"][:55] + "…" if len(r["title"]) > 55 else r["title"]
                sp = r["points"] if r["points"] != "" else "—"
                assigned_short = r["assigned"].split(" <")[0] if r["assigned"] else "—"
                lines.append(
                    f"| {hu_link} | {title_short} | {r['state']} | {sp} | {assigned_short} | {icon} | {faltantes_str} |"
                )
            lines.append("")

    # ── Sección solo incompletas (faltan descripción o criterios) ──
    incompletas = [r for r in rows if not r["complete"]]
    lines += [
        "---",
        "",
        "## ❌ HUs sin Descripción o Criterios de Aceptación",
        "",
        f"Total: **{len(incompletas)}** HUs con contenido incompleto.",
        "",
        "| ID | Título | Estado | Campos faltantes |",
        "|----|--------|--------|-----------------|",
    ]
    for r in sorted(incompletas, key=lambda x: x["id"]):
        faltantes = []
        if not r["criteria"]["descripcion"]:  faltantes.append("Descripción")
        if not r["criteria"]["criterios"]:    faltantes.append("Criterios AC")
        hu_link = f"[{r['id']}]({make_url(r['id'])})"
        title_short = r["title"][:55] + "…" if len(r["title"]) > 55 else r["title"]
        lines.append(f"| {hu_link} | {title_short} | {r['state']} | {', '.join(faltantes)} |")

    # ── Sección pendientes de refinamiento ──
    sin_refinar = [r for r in rows if r["complete"] and not r["refined"]]
    lines += [
        "",
        "---",
        "",
        "## ⚠️ HUs con contenido OK pero sin refinar (SP / Asignado / Estado)",
        "",
        f"Total: **{len(sin_refinar)}** HUs pendientes de refinamiento.",
        "",
        "| ID | Título | Estado | Pendiente |",
        "|----|--------|--------|-----------|",
    ]
    for r in sorted(sin_refinar, key=lambda x: x["id"]):
        pendiente = []
        if not r["criteria"]["story_points"]: pendiente.append("Story Points")
        if not r["criteria"]["asignado"]:     pendiente.append("Asignado")
        if not r["criteria"]["estado"]:       pendiente.append("Estado")
        hu_link = f"[{r['id']}]({make_url(r['id'])})"
        title_short = r["title"][:55] + "…" if len(r["title"]) > 55 else r["title"]
        lines.append(f"| {hu_link} | {title_short} | {r['state']} | {', '.join(pendiente)} |")

    lines += ["", "---", "", f"_Generado automáticamente el 2026-04-08_", ""]

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n✅  Archivo generado: {OUT_FILE}")
    print(f"    Total: {total} | Con contenido: {n_complete} ({pct_content}%) | Refinadas: {n_refined} ({pct_refined}%) | Incompletas: {n_incomplete}")


if __name__ == "__main__":
    main()
