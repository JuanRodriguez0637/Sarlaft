# HU 1029972 — [Monitoreo]: Lista de control (ONU, OFAC, Grupos terroristas) - Infolaft

[Épica 1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585) › [Feature 1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784) › HU 1029972 — [Monitoreo]: Lista de control (ONU, OFAC, Grupos terroristas) - Infolaft

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1029972](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029972) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Ciencia de datos |
| **Creado** | 2026-02-02 |
| **Última modificación** | 2026-02-06 |

## Jerarquía

- **Épica:** [1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585)  
  Estado: New  
- **Feature:** [1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784)  
  Estado: New  

## Descripción

Como Analista SARLAFT
 
 

quiero que el sistema ejecute de forma automática y diaria un proceso batch de
monitoreo contra la Lista de Control,

para validar el 100 % de la
base de clientes, aplicar reglas de marcación, mantenimiento o desmarcación, y generar
logs completos, garantizando trazabilidad auditable y cumplimiento normativo
SARLAFT, sin intervención manual. 
**
** 
**Naturaleza del
Proceso – Lista de Control** 
 
  
  
**Atributo** 
  
  
  
**Definición** 
  
 
 
  
  
**Tipo** 
  
  
  
Batch 
  
 
 
  
  
**Ejecución** 
  
  
  
Automática 
  
 
 
  
  
**Frecuencia** 
  
  
  
Diario 
  
 
 
  
  
**Momento** 
  
  
  
Ventana definida (sin afectar producción) 
  
 
 
  
  
**Alcance** 
  
  
  
100 %
  de los clientes vigentes de la compañía. 
  
 
 
  
  
**Resultado** 
  
  
  
Archivo de logs + actualización de marcas de Lista de
  Control 
  
 
 
  
  
**Margen de tolerancia** 
  
  
  
El margen de tolerancia para volver a consultar un cliente
  es de 24 horas, contado a partir de la última ejecución exitosa del proceso 
  
 
 
  
  
**Trazabilidad** 
  
  
  
Obligatoria y auditable 
  
 
  
**Descripción
Funcional – Lista de Control** 
**Alcance del Proceso** 
El proceso batch debe: 
 
- La
     consulta de los clientes vigentes en la lista de control debe ejecutarse
     automáticamente todos los días. 
 
- Tomar
     la totalidad de clientes vigentes y ejecutar según las siguientes ejecuciones:
     
 
  
- Cobertura
      de la 1.ª ejecución: 100 %
      de los clientes de la compañía. 
  
- Cobertura
      de la 2.ª ejecución: consulta solo los “nuevos registros” de la lista
      de control con los clientes vigentes de la compañía. 
 
 
- Validar
     cada cliente exclusivamente contra la causal “Lista de Control” (ONU,
     OFAC, Grupos Terroristas). 
 
- Aplicar
     reglas de coincidencia y decisión. 
- El proceso marca, mantiene, actualiza fechas y genera logs completos.
 
- Si la fuente de consulta falla: 
- Reintenta automáticamente según política de reintentos  
- Registra el error en log técnico con el estado final. 
- Continúa con los demás clientes (no bloquea todo el batch).  
 
- Actualizar
     las marcas correspondientes en los sistemas definidos. 
 
- Generar
     un archivo consolidado de logs con los resultados. 
 
- Guardar
     trazabilidad auditable por cliente y por lista. 
 
- Generar
     métricas de los clientes procesados.  
**
** 
**Reglas de
Coincidencia – Lista de Control** 
**Marcación** 
Se genera una marca directa cuando: 
 
- Existe
     coincidencia exacta entre cliente y lista, según: 
 
  
- Tipo
      de documento 
  
- Número
      de documento 
  
- Nombres
      completos o razón social 
 
 
- La
     fuente confirma que el cliente figura activamente en la Lista de Control. 
 
- Si
     se identifican nuevos tipos o números de documento asociados al cliente: 
 
  
- Se
      valida si existen vinculaciones vigentes. 
  
- Se
      adiciona el resultado al log. 
  
  
 **Tipo de
Coincidencia y Acción** 
 
  
  
**Tipo de coincidencia** 
  
  
  
**Acción** 
  
 
 
  
  
Coincidencia por 1 dato (número ID) 
  
  
  
Generar log 
  
 
 
  
  
Coincidencia por 2 datos (nombres completos) 
  
  
  
Generar log 
  
 
 
  
  
Coincidencia exacta (tipo ID + número ID + nombres) 
  
  
  
Marca directa + log 
  
 
 
  
  
Error en la consulta 
  
  
  
Reintentar hasta tres veces + log técnico 
  
 
  
**Estado “Se mantiene” cuando:** 
 
- El
     cliente estaba marcado previamente. 
 
- La
     fuente confirma que: 
 
  
- Sigue
      figurando en la Lista de Control. 
  
- No
      hay cambios relevantes en programa o condición. 
  
**Decisión SARLAFT – Lista de Control** 
 
  
  
**Elemento** 
  
  
  
**Definición** 
  
 
 
  
  
Lista 
  
  
  
Lista de Control (ONU, OFAC, Grupos Terroristas) 
  
 
 
  
  
Decisión 
  
  
  
Marca / mantiene 
  
 
 
  
  
Manejo coincidencia parcial 
  
  
  
Genera log 
  
 
 
  
  
Aplicativo de conexión 
  
  
  
API Infolaft 
  
 
 
  
  
Aplicativo donde queda la marca 
  
  
  
Riesgos consultables 
  
 
 
  
  
Datos de consulta 
  
  
  
Tipo ID, Número ID, Nombres completos o Razón Social 
  
 
  
**Trazabilidad Obligatoria – Lista de Control** 
Por cada cliente y consulta el batch debe registrar: 
 
- Fecha
     de consulta 
 
- Fuente
     consultada 
 
- Datos
     enviados 
 
- Resultado
     obtenido 
 
- Acción
     tomada (marca / mantiene / log) 
 
- Responsable
     (sistema) 
 
- Identificador
     del proceso batch 
 
- Archivo
     de logs  
**Contenido mínimo del Log – Lista de Control** 
 
- DNI
     del cliente: Tipo de Id y número de ID 
- Nombres completos o razón social 
- Tipo de persona: 
- Natural 
- Jurídico   
- Estado vinculación 
- **Vigente: **Tiene al menos una vinculación 
- **No vigente:** No tiene vinculaciones  
 
- Figura: Tomador, Asegurado, Beneficiario, Afianzado, Afiliado, Proveedor, Empleado, Administrador 
- Vinculaciones:  
- Ramo, producto, plan 
- Valor prima anual, valor asegurado cobertura principal 
- Indicador tipo de régimen EPS 
- Indicador de fondo de ahorro, valor del fondo de ahorro alcanzado y valor de abono al fondo de ahorro 
- Fecha de inicio de vigencia  
 
- Tipo
     de coincidencia: Coincidencia por 1 dato, Coincidencia por 2 datos, Coincidencia exacta y Error en la consulta 
 
- Tipo
     y nombre de la lista: Lista de control 
- Fecha de consulta 
- Es la fecha en que corre el proceso en batch con la fuente de consulta  
 
- Fecha
     de marcación 
- Fecha en que se marca el cliente porque hay coincidencia exacta 
- La fecha queda vacia cuando hay coincidencia por 1 dato, Coincidencia por 2 datos y Error en la consulta  
 
- Estado: Marca  o Mantiene 
 
- Causal 
- Es el programa o sanción al que pertenece el cliente 
- Si tiene mas de un programa o sanción se debe relacionar en un solo campo  
 
- Documentos
     asociados 
- Tipo id, número id 
- Nombres completos o razón social  
 
- Fuente
     de consulta: Indicar el nombre de la API que se tiene integrada 
 
- Errores
     técnicos (si aplica)  
 **Contenido mínimo del Log de errores – Lista de Control** 
- Fecha de consulta: Es la fecha en que corre el proceso en batch con la fuente de consulta 
- Fuente de consulta: Indicar el nombre de la API que se tiene integrada 
- Cliente: Tipo ID y número de ID 
- Motivo del error 
- Número
     de reintentos 
- Estado final: Indicar si se logro realizar la consulta del cliente  
 
**Control de Cobertura – Lista de Control** 
El proceso debe generar métricas automáticas de: 
 
- Total
     de clientes procesados 
 
- Clientes
     marcados por Lista de Control 
 
- Clientes
     con log 
 
- Clientes
     con error 
 
- % de
     cobertura del batch

## Criterios de Aceptación

1) Criterios de Aceptación Funcionales  1.1. Orquestación y frecuencia 
- 
**Ejecución automática diaria** 
- **Dado** que existe una ventana de ejecución definida, 
- **Cuando** llega el horario configurado, 
- **Entonces** el proceso **se inicia sin intervención manual** y registre trazabilidad.   
- 
**Ventana sin afectar producción** 
- **Dado** que la ventana fue configurada, 
- **Cuando** corre el batch, 
- **Entonces** no bloquea procesos transaccionales de producción y no requiere paros.   
- 
**Tolerancia de 24h por cliente** 
- **Dado** un cliente cuya **última consulta exitosa** fue **hace menos de 24h**, 
- **Cuando** corre el batch, 
- **Entonces** **no se reconsulta** a ese cliente, se registra **“omitido por tolerancia 24h”** en métricas y trazabilidad.    1.2. Cobertura y alcance de la consulta 
- 
**1.ª ejecución = 100% vigentes** 
- **Dado** que es la primera ejecución, 
- **Cuando** corre el batch, 
- **Entonces** consulta el **100% de clientes vigentes** y lo evidencia con conteo clientes_vigentes_total = clientes_procesados + omitidos_por_tolerancia (0 en primera corrida).   
- 
**2.ª y siguientes = delta de la Lista de Control** 
- **Dado** que ya existe al menos una ejecución previa, 
- **Cuando** corre el batch, 
- **Entonces** consulta únicamente los **“nuevos registros”** (delta) de la **Lista de Control** y **los cruza** contra el **universo de clientes vigentes**. 
- Si la fuente no entregara delta en un día, **el proceso no falla**: registra evento informativo y continúa con la lógica (sin bloquear).   
- 
**Causal aplicable** 
- **Dado** un cliente vigente, 
- **Cuando** el sistema consulte, 
- **Entonces** **solo valida contra la causal “Lista de Control”** (ONU, OFAC, Grupos Terroristas), no otras listas.    1.3. Reglas de coincidencia y decisión 
- 
**Normalización para coincidencia exacta** 
- **Dado** los datos de entrada (tipo ID, número ID, nombres completos/razón social), 
- **Cuando** aplique “coincidencia exacta”, 
- **Entonces** compara:

- tipo_id = igualdad exacta (catálogo controlado), 
- numero_id = igualdad exacta (tras normalizar ceros a la izquierda/guiones/espacios), 
- nombres/razon_social = igualdad exacta **case-insensitive**, **sin tildes** y sin dobles espacios.     
- 
**Acciones por tipo de coincidencia** 
- **Coincidencia por 1 dato** (p.ej., número ID): **Genera log** (sin marca). 
- **Coincidencia por 2 datos** (p.ej., nombres completos): **Genera log** (sin marca). 
- **Coincidencia exacta** (tipo ID + número ID + nombres): **Marca directa** + **log**. 
- **Error en la consulta**: **reintenta hasta 3 veces** y **genera log técnico**.   
- 
**Mantener marca (“Se mantiene”)** 
- **Dado** un cliente **ya marcado** por Lista de Control, 
- **Cuando** la fuente confirma que **sigue figurando** sin cambios relevantes, 
- **Entonces** el **estado se mantiene**, se actualiza fecha_última_validación, se registra en log.   
- 
**Desmarcación**   
- **Dado** un cliente **marcado previamente**, 
- **Cuando** la fuente confirme que **ya no figura activamente**, 
- **Entonces** el sistema **desmarca** y genera **log** con causal, fecha_desmarcación y evidencia de fuente.  
- **Nuevos documentos asociados**  
- **Dado** que la fuente devuelve **tipos/números de documento adicionales** para el mismo sujeto, 
- **Cuando** se detecten, 
- **Entonces** el sistema **valida si existen vinculaciones vigentes** en la compañía y **adiciona el resultado al log**.  1.4. Reintentos y continuidad del batch 
- **Política de reintentos**  
- **Dado** un error de consulta a la fuente (timeout, 5xx, etc.), 
- **Cuando** ocurre, 
- **Entonces** el sistema **reintenta hasta 3 veces** (p. ej., backoff 1m–2m–5m) y registra **cada intento**.  
- **No bloqueo del batch**  
- **Dado** que un cliente presenta error definitivo, 
- **Cuando** se exceden los reintentos, 
- **Entonces** el sistema **registra el error**, **marca el estado final del cliente** como “no consultado” y **continúa** con los demás clientes (no se cae el proceso completo).  1.5. Actualización de marcas en sistemas destino 
- **Marca/Mantiene/Desmarca en “Riesgos consultables”**  
- **Dado** el resultado de decisión (marca/mantiene/desmarca), 
- **Cuando** se determina, 
- **Entonces** se **actualiza el estado** en el aplicativo **Riesgos consultables**, con fecha_estado, causal (programa/sanción) y **usuario responsable = sistema**.  
- **Idempotencia de actualización**  
- **Dado** una re-ejecución del mismo batch por contingencia, 
- **Cuando** el sistema reprocese, 
- **Entonces** **no duplica** marcas ni logs, usando una clave de idempotencia (por ejemplo cliente_id + lista + fecha_consulta + batch_id).  1.6. Trazabilidad y logs obligatorios 
- **Trazabilidad por cliente y por lista**  
- **Dado** cualquier cliente procesado, 
- **Cuando** finaliza su consulta, 
- **Entonces** el sistema registra **mínimo**:

- fecha_consulta (fecha/hora del batch), 
- fuente_consultada (p. ej., **API Infolaft**), 
- datos_enviados (tipo ID, número ID, nombres/razón social), 
- resultado_obtenido, 
- acción_tomada (marca / mantiene / desmarca / log), 
- responsable = sistema, 
- batch_id.    
- **Archivo consolidado de logs (negocio)**  
- **Dado** que termina el batch, 
- **Cuando** se genera la salida, 
- **Entonces** existe **un archivo consolidado** (CSV/Parquet/JSON, definible) con el **contenido mínimo** detallado en la historia (ver Sección 2.1 abajo), **con nombres de campos estandarizados**, **sin registros duplicados** y con **firma de integridad** (hash + batch_id).  
- **Log técnico de errores**  
- **Dado** que hubo errores, 
- **Cuando** se cierra el batch, 
- **Entonces** existe **un archivo/log técnico** con el **contenido mínimo** de error (ver Sección 2.2), incluyendo **número de reintentos** y **estado final**.  1.7. Métricas y control de cobertura 
- **Métricas automáticas**  
- **Dado** que finaliza el batch, 
- **Cuando** se calculan métricas, 
- **Entonces** se registran y publican:

- total_clientes_procesados 
- clientes_marcados_lista_control 
- clientes_con_log (parciales y exactos) 
- clientes_con_error 
- %cobertura_batch = total_clientes_procesados / total_clientes_vigentes * 100 
- omitidos_por_tolerancia_24h (reportado aparte, **no** se incluyen en el denominador de procesados).    
- **Exportación/consulta de métricas**  
- **Dado** que se generan métricas, 
- **Cuando** las solicita un usuario autorizado, 
- **Entonces** pueden descargarse/consultarse por batch_id y **rango de fechas**.  1.8. Seguridad, auditoría y cumplimiento 
- **Responsabilidad del sistema**  
- **Dado** cualquier actualización de marca, 
- **Cuando** se audita, 
- **Entonces** la trazabilidad muestra responsable = sistema (usuario técnico de servicio) y batch_id.  
- **Integridad y no repudio**  
- **Dado** el archivo de logs, 
- **Cuando** se verifique, 
- **Entonces** el hash de integridad coincide con el contenido, y el archivo conserva batch_id, fecha y versión del esquema.  1.9. Validaciones y calidad de datos 
- **Validación de insumos del cliente**  
- **Dado** que un cliente no tiene **tipo ID** o **número ID** válidos, 
- **Cuando** se intente consultar, 
- **Entonces** no se envía a la fuente, se registra **log técnico** con motivo “datos incompletos” y el cliente cuenta como **error**.  
- **Catálogos controlados**  
- **Dado** los tipos de documento, 
- **Cuando** se mapean, 
- **Entonces** el sistema usa un catálogo controlado (**sin valores libres**) y documenta las transformaciones de normalización.   2) Contenidos mínimos de los logs (esquemas funcionales) 2.1. Log de negocio (por cliente y consulta) 
- **DNI del cliente:** tipo_id, numero_id 
- **Estado de vinculación:** vigente (Sí/No) 
- **Figuras:** tomador/asegurado/beneficiario/afianzado/afiliado/proveedor/empleado/administrador (múltiples) 
- **Vinculaciones:** ramo, producto, plan 
- **Valores clave:** prima_anual, valor_asegurado_cobertura_principal 
- **Indicadores:** regimen_eps (Sí/No), indicador_fondo_ahorro (Sí/No), valor_fondo_ahorro, valor_abono_fondo_ahorro 
- **Fecha inicio vigencia** 
- **Tipo de coincidencia:** 1_dato | 2_datos | exacta | error_consulta 
- **Tipo/nombre de la lista:** Lista de Control (ONU/OFAC/Grupos Terroristas) 
- **Fecha de consulta** (del batch) 
- **Fecha de marcación** (solo si coincidencia exacta; **vacía** para 1 dato / 2 datos / error) 
- **Estado de decisión:** Marca | Mantiene | Desmarca | Solo log 
- **Causal (programa/sanción):** concatenada si hay varias 
- **Documentos asociados:** lista de {tipo_id, numero_id} agregados por la fuente 
- **Nombres/Razón social** 
- **Fuente de consulta:** p. ej. API Infolaft 
- **Responsable:** sistema 
- **batch_id** y **idempotency_key**  
**Criterio de aceptación:** Todos los campos anteriores están presentes, con tipado consistente, sin nulos injustificados, y con un registro por **cliente x ejecución**. 2.2. Log técnico de errores 
- **Fecha de consulta** 
- **Fuente de consulta** 
- **Cliente:** tipo_id, numero_id 
- **Motivo del error** (timeout, 5xx, datos incompletos, credencial inválida, etc.) 
- **Número de reintentos** 
- **Estado final** (consultado | no_consultado) 
- **batch_id** y **trace_id** (si aplica)  
**Criterio de aceptación:** Todo error queda en este log con **al menos** los campos anteriores y relacionable al log de negocio por batch_id y cliente. 3) Métricas y cobertura (definiciones verificables) 
- total_clientes_procesados: cantidad con consulta ejecutada (excluye omitidos por tolerancia). 
- clientes_marcados_lista_control: total con **decisión = Marca**. 
- clientes_con_log: total con registros por **coincidencia 1 o 2 datos** (sin marca). 
- clientes_con_error: total con **estado final = no_consultado**. 
- %cobertura_batch = (total_clientes_procesados / total_clientes_vigentes) * 100 
- omitidos_por_tolerancia_24h: clientes saltados por regla de 24h (se reporta aparte).  
**Criterio de aceptación:** Las métricas se calculan, persisten y pueden consultarse por batch_id y rango de fechas. El denominador de cobertura son **vigentes** al momento del batch.
