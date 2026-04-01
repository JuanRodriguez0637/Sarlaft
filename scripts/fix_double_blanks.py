import re

# Fix DisenoArquitectura.md - double blank at end
p = r'D:\Sarlaft 4.0\docs\MicroservicioBackweb\DisenoArquitectura.md'
with open(p, encoding='utf-8') as f:
    c = f.read()
c = re.sub(r'\n{2,}$', '\n', c)
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    f.write(c)
print('DisenoArquitectura done. Ends with:', repr(c[-5:]))

# Fix ServicioCambiarEstadoEntidad.md
p2 = r'D:\Sarlaft 4.0\docs\MicroservicioBackweb\ServiciosWeb\ServicioCambiarEstadoEntidad.md'
with open(p2, encoding='utf-8') as f:
    c2 = f.read()
# Collapse triple+ newlines to double
c2 = re.sub(r'\n{3,}', '\n\n', c2)
# Fix broken attachment link
c2 = c2.replace(
    '[request (1).json](../attachments/request%20(1).json).json?version=1&modificationDate=1665152834496&cacheVersion=1&api=v2)',
    '[request (1).json](../attachments/request%20(1).json)'
)
# Fix Perfil Seus4 double space
c2 = c2.replace('**Perfil Seus4:**  PF_SARLAFTADM', '**Perfil Seus4:** `PF_SARLAFTADM`')
if not c2.endswith('\n'):
    c2 += '\n'
with open(p2, 'w', encoding='utf-8', newline='\n') as f:
    f.write(c2)
print('ServicioCambiarEstado done')
