import json, os

PAGES_DIR = "d:/Sarlaft 4.0/scripts/incidents_pages"

PAGE_IDS = [
    ("1742800723", "Documentación de Incidentes"),
    ("5174624323", "Limpiar Base de datos en laboratorio"),
    ("5174689830", "Solicitud de request and respose"),
    ("5174788164", "Problemas con el link de validación de identidad"),
    ("5174886473", "Solucionar INC asignados en BMC Helix"),
    ("5624856625", "Error en el aplicativo de Banca (Negocio en estado PENDIENTE)"),
]

for pid, title in PAGE_IDS:
    page = json.load(open(os.path.join(PAGES_DIR, f"{pid}.json"), encoding='utf-8'))
    body = page.get('body', {}).get('storage', {}).get('value', '')
    print(f"\n{'='*70}")
    print(f"PAGE: {title} (ID={pid})")
    print(f"{'='*70}")
    print(body)
    print()
