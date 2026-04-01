# Bitácora de Enlaces — Hallazgos y Correcciones Pendientes

> **Propósito:** Registrar los hallazgos de enlaces entre archivos `.md` que requieren corrección, ya sea porque apuntan a archivos que no existen o porque apuntan a URLs de Confluence cuando ya existe un `.md` local equivalente.
>
> **Última actualización:** 2026-04-01

---

## 1. Enlaces rotos (apuntan a `.md` que NO existen)

| # | Archivo origen | Línea | Enlace roto | Texto del enlace | Corrección sugerida |
|---|---------------|-------|-------------|-------------------|---------------------|
| 1 | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftBatch/index.md` | L5 | `../index.md` | Documentación Técnica | Crear `Sarlaft40/DocumentacionTecnica/index.md` al documentar la sección padre |

---

## 2. Enlaces que apuntan a Confluence pero YA tienen `.md` local

Estos enlaces en la cabecera `> **Fuente Confluence:**` son **intencionales** como trazabilidad y NO requieren corrección. Esta sección documenta únicamente los enlaces **dentro del cuerpo** del contenido que deberían apuntar a archivos locales en vez de a Confluence.

| # | Archivo origen | Texto del enlace | URL Confluence | `.md` local existente | Estado |
|---|---------------|-------------------|----------------|----------------------|--------|
| — | *No se encontraron enlaces en cuerpo que apunten a Confluence teniendo `.md` local* | — | — | — | ✅ |

> **Nota:** Todos los enlaces a Confluence detectados están en las cabeceras de trazabilidad (`> **Fuente Confluence:**`) o en columnas de referencia cruzada del catálogo de servicios (`Confluence` column en `ServiciosWeb/index.md`). Estos son intencionales.

---

## 3. Secciones de Confluence aún NO documentadas en `.md`

Las siguientes páginas de Confluence están referenciadas desde la documentación existente pero **aún no se han extraído** como secciones independientes. Son candidatas para futuras extracciones con el agente Confluence Sura.

| # | Sección en Confluence | Referenciado desde | Prioridad | Estado |
|---|----------------------|--------------------|-----------|--------|
| 1 | [7. Webhook (Assessment)](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/3222994946/7.+Webhook+Assessment) | `MicroservicioWebhook/index.md` L15, `MicroservicioWebhook/WebhookSarlaft.md` L17 | Media | Pendiente |
| 2 | [Documentación Técnica](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1746830371) (página padre) | `Sarlaft40/DocumentacionTecnica/MicroservicioSarlaftBatch/index.md` L5 | Baja | Pendiente — sección índice padre |

---

## 4. Archivo `docs/index.md` faltante

No existe un archivo `docs/index.md` a nivel raíz que sirva como punto de entrada general a toda la documentación. El archivo `MicroservicioSarlaftAPI/ConsumoNuevosEndpoints.md` intenta navegar a `../index.md` (que sería `docs/index.md`) y falla.

**Acción recomendada:** Crear `docs/index.md` como índice general que enlace a:
- `MicroservicioSarlaftAPI/index.md`
- `MicroservicioWebhook/index.md`
- `MicroservicioSarlaftBatch/index.md`
- Los demás documentos sueltos (`AtributosCalidadDesarrollo.md`, `ConfiguracionInfraestructura.md`, etc.)

---

## Registro de correcciones aplicadas

| Fecha | Archivo corregido | Descripción del cambio |
|-------|-------------------|------------------------|
| 2026-04-01 | `MicroservicioWebhook/index.md` | Enlace "7. Webhook (Assessment)" cambiado de URL Confluence a `./DisenoArquitectura.md` |
| 2026-04-01 | `MicroservicioWebhook/WebhookSarlaft.md` | Enlace "7. Webhook (Assessment)" cambiado de URL Confluence a `./DisenoArquitectura.md` |
| 2026-04-01 | `MicroservicioSarlaftAPI/ConsumoNuevosEndpoints.md` | L4: Enlace `../index.md` corregido a URL Confluence padre `Servicios+Web+-+SarlaftAPI` |

---

## Cómo usar esta bitácora

1. **Al crear nuevos `.md`:** Verificar si algún enlace roto de la sección 1 ahora puede resolverse y actualizar los archivos origen.
2. **Al extraer nuevas secciones de Confluence:** Revisar la sección 3 y marcar como completada la sección documentada.
3. **Después de cada corrección:** Agregar una entrada en "Registro de correcciones aplicadas".
4. **Para re-escanear:** Ejecutar en terminal:

```powershell
$base = "D:\Proyectos\Sarlaft\Documentacion\Sarlaft\docs"
$mdFiles = Get-ChildItem $base -Recurse -Filter "*.md" | Where-Object { $_.Name -ne "PromptDocumentarConfluence.md" -and $_.Name -ne "BitacoraEnlaces.md" }
foreach ($f in $mdFiles) {
    $lines = Get-Content $f.FullName
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $ms = [regex]::Matches($lines[$i], '\[([^\]]+)\]\((\.\.?/[^\)]+\.md[^\)]*)\)')
        foreach ($m in $ms) {
            $lp = $m.Groups[2].Value -replace '#.*$',''
            $rp = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($f.DirectoryName, $lp))
            if (-not (Test-Path $rp)) {
                $rf = $f.FullName.Replace("$base\","")
                Write-Host "BROKEN | $rf | L$($i+1) | $lp | $($m.Groups[1].Value)"
            }
        }
    }
}
```
