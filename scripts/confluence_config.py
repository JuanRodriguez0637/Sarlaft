"""
Configuración compartida para todos los scripts de Confluence - Sarlaft 4.0
"""
import base64
import os

EMAIL    = "juan.hoyos@ceiba.com.co"
TOKEN    = "ATATT3xFfGF0esKEuh1KrY54F4svPmwtTMbbUUp5Yf3Z6y-WqFXPOz2iXGaZ3yWTd8G5Ifa6SvOSwcc19QlZHnywmhF5U_Ot1kpKwhIT75YhNXce_lp6VmGmKMoGhcay3n1kBkQZm5ZIKyRrchJjWCFAvFLERtlFGm8JLSafp16bR2OrY5CGCu8=E4F531A9"
BASE_URL = "https://segurosti.atlassian.net"

DOCS_ROOT  = r"D:\Sarlaft 4.0\docs"
ARCHI_ROOT = os.path.join(DOCS_ROOT, "Diseño - Arquitectura")
REF_ROOT   = os.path.join(ARCHI_ROOT, "referencias")
IMG_ROOT   = os.path.join(ARCHI_ROOT, "imagenes")

_creds = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {_creds}",
    "Accept": "application/json",
}
DL_HEADERS = {
    "Authorization": f"Basic {_creds}",
}
