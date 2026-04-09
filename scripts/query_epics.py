"""Query 3 priority epics and their child work items from Azure DevOps."""
import requests, base64, json, os, sys

PAT = os.environ.get("ADO_PAT", "")
if not PAT:
    print("Set ADO_PAT env var first")
    sys.exit(1)

ORG = "SuraColombia"
PROJECT = "Gerencia_Tecnologia"

b64 = base64.b64encode(f":{PAT}".encode()).decode()
headers = {
    "Authorization": f"Basic {b64}",
    "Content-Type": "application/json",
}

def get(url, params=None):
    r = requests.get(url, headers=headers, params=params, timeout=30)
    r.raise_for_status()
    return r.json()

def post(url, body):
    r = requests.post(url, headers=headers, json=body, timeout=30)
    r.raise_for_status()
    return r.json()

# Step 1: Get epic details
epic_ids = [1107349, 1079106, 1105971]
id_str = ",".join(map(str, epic_ids))
url = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/wit/workitems?ids={id_str}&$expand=all&api-version=7.1"
data = get(url)

all_child_ids = []
epics_info = {}

for wi in data.get("value", []):
    fields = wi["fields"]
    eid = fields["System.Id"]
    title = fields["System.Title"]
    state = fields["System.State"]
    prio = fields.get("Microsoft.VSTS.Common.Priority", "N/A")

    relations = wi.get("relations", [])
    children = [r for r in relations if r.get("rel") == "System.LinkTypes.Hierarchy-Forward"]
    child_ids = [int(c["url"].split("/")[-1]) for c in children]

    epics_info[eid] = {
        "title": title,
        "state": state,
        "priority": prio,
        "child_ids": child_ids,
    }
    all_child_ids.extend(child_ids)
    print(f"\n=== EPIC {eid}: {title} ===")
    print(f"  State: {state} | Priority: {prio} | Children: {len(child_ids)}")

# Step 2: Get all child work items (Features)
print(f"\n--- Fetching {len(all_child_ids)} child work items ---")
BATCH = 200
feature_info = {}
all_hu_ids = []

for i in range(0, len(all_child_ids), BATCH):
    batch_ids = all_child_ids[i:i+BATCH]
    id_str2 = ",".join(map(str, batch_ids))
    url2 = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/wit/workitems?ids={id_str2}&$expand=all&api-version=7.1"
    data2 = get(url2)
    for wi2 in data2.get("value", []):
        f2 = wi2["fields"]
        fid = f2["System.Id"]
        ftitle = f2["System.Title"]
        ftype = f2["System.WorkItemType"]
        fstate = f2["System.State"]
        relations2 = wi2.get("relations", [])
        hus = [r for r in relations2 if r.get("rel") == "System.LinkTypes.Hierarchy-Forward"]
        hu_ids = [int(c["url"].split("/")[-1]) for c in hus]
        feature_info[fid] = {
            "title": ftitle,
            "type": ftype,
            "state": fstate,
            "hu_ids": hu_ids,
        }
        all_hu_ids.extend(hu_ids)
        print(f"  [{ftype}] {fid}: {ftitle} ({fstate}) -> {len(hu_ids)} children")

# Step 3: Get all HU details
print(f"\n--- Fetching {len(all_hu_ids)} HUs ---")
hu_info = {}
for i in range(0, len(all_hu_ids), BATCH):
    batch_ids = all_hu_ids[i:i+BATCH]
    id_str3 = ",".join(map(str, batch_ids))
    url3 = f"https://dev.azure.com/{ORG}/{PROJECT}/_apis/wit/workitems?ids={id_str3}&fields=System.Id,System.Title,System.State,System.WorkItemType,Microsoft.VSTS.Scheduling.StoryPoints,System.AssignedTo,Microsoft.VSTS.Common.Priority&api-version=7.1"
    data3 = get(url3)
    for wi3 in data3.get("value", []):
        f3 = wi3["fields"]
        hid = f3["System.Id"]
        hu_info[hid] = {
            "title": f3["System.Title"],
            "type": f3["System.WorkItemType"],
            "state": f3["System.State"],
            "story_points": f3.get("Microsoft.VSTS.Scheduling.StoryPoints"),
            "assigned_to": f3.get("System.AssignedTo", {}).get("displayName") if isinstance(f3.get("System.AssignedTo"), dict) else f3.get("System.AssignedTo"),
            "priority": f3.get("Microsoft.VSTS.Common.Priority"),
        }

# Step 4: Output structured info
print("\n\n========== PLAN DE TRABAJO ==========\n")

for eid in epic_ids:
    ei = epics_info.get(eid)
    if not ei:
        print(f"EPIC {eid}: NOT FOUND")
        continue
    print(f"\n{'='*60}")
    print(f"ÉPICA {eid}: {ei['title']}")
    print(f"State: {ei['state']} | Priority: {ei['priority']}")
    print(f"{'='*60}")

    for fid in ei["child_ids"]:
        fi = feature_info.get(fid)
        if not fi:
            print(f"  Feature {fid}: NOT FOUND")
            continue
        print(f"\n  Feature {fid}: {fi['title']} ({fi['state']})")
        print(f"  {'─'*50}")

        for hid in fi.get("hu_ids", []):
            hi = hu_info.get(hid)
            if not hi:
                print(f"    HU {hid}: NOT FOUND")
                continue
            sp = hi["story_points"] or "—"
            assigned = hi["assigned_to"] or "—"
            print(f"    [{hi['state']}] {hid}: {hi['title']}")
            print(f"      SP: {sp} | Asignado: {assigned} | Tipo: {hi['type']}")

# Save as JSON for reference
output = {
    "epics": epics_info,
    "features": {str(k): v for k, v in feature_info.items()},
    "hus": {str(k): v for k, v in hu_info.items()},
}
with open(os.path.join(os.path.dirname(__file__), "epics_plan.json"), "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2, default=str)
print("\n\nSaved to scripts/epics_plan.json")
