"""
verify_scope.py — Verifica si páginas referenciadas están dentro de Diseño - Arquitectura
"""
import requests
from confluence_config import BASE_URL, HEADERS

# IDs referenciadas desde los .md de Diseño - Arquitectura
REFERENCED_IDS = [
    "1814233305", "2093350926", "1955070163", "2619802061",
    "1861058683", "1804861539", "1864597599", "2476834835",
    "1860862186", "2787475565", "2370961900", "2456289281",
    "2345730088", "1814003981", "1955070150", "256672056",
]

# IDs que forman la sección Diseño - Arquitectura
DISENYO_IDS = {
    "1804697669","1804927175","1804861588","1801126348","1801159177","3307601991",
    "1856537007","1866629127","3214016543","3214049307","3213164787","3214082137",
    "3221782545","3222274070","3222634497","3222831120","3222994946","3737911299",
    "3742531593","3742892047","3743580178","3743219726","3224436826","3226009603",
    "3226599489","3648421917","3228303479","3235053604","3234791499","3235282962",
    "3234791531","3236888621","3675586561","4703420517",
}


def main():
    print("=== Verificando pertenencia de páginas referenciadas ===\n")
    print(f"{'PageId':<15} {'ParentId':<15} {'En sección?':<12} Título")
    print("-" * 90)

    for pid in REFERENCED_IDS:
        try:
            page = requests.get(f"{BASE_URL}/wiki/api/v2/pages/{pid}", headers=HEADERS).json()
            parent_id = page.get("parentId", "?")
            en_seccion = "✅ SI" if (parent_id in DISENYO_IDS or pid in DISENYO_IDS) else "❌ NO"
            print(f"{pid:<15} {parent_id:<15} {en_seccion:<12} {page.get('title','?')}")
        except Exception as e:
            print(f"{pid:<15} {'ERROR':<15} {'?':<12} {e}")


if __name__ == "__main__":
    main()
