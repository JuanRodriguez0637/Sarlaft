# HU 1029992 — [Monitoreo]: Consulta estado Persona jurídica con Informacolombia

[Épica 1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585) › [Feature 1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784) › HU 1029992 — [Monitoreo]: Consulta estado Persona jurídica con Informacolombia

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1029992](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1029992) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Ciencia de datos |
| **Creado** | 2026-02-02 |
| **Última modificación** | 2026-03-18 |

## Jerarquía

- **Épica:** [1036585 — Monitoreo y Señales de Alerta](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1036585)  
  Estado: New  
- **Feature:** [1026784 — [Monitoreo]: Proceso en Batch Automático de Listas SARLAFT](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1026784)  
  Estado: New  

## Descripción

Como Analista SARLAFT 
quiero que el sistema ejecute de forma automática y diaria un proceso batch de
monitoreo de listas LAFT sin intervención manual, 

para validar toda la base de clientes, aplicar reglas de marcado/desmarcado y
generar un archivo con logs completos, asegurando trazabilidad auditable y
cumplimiento normativo SARLAFT. 
**Naturaleza del Proceso ** 
 
  
  
**Atributo** 
  
  
  
**Definición** 
  
 
 
  
  
Tipo 
  
  
  
Batch 
  
 
 
  
  
Ejecución 
  
  
  
Automática 
  
 
 
  
  
Frecuencia 
  
  
  
Periódico (depende de la lista) 
  
 
 
  
  
Momento 
  
  
  
Ventana definida (No afectar producción) 
  
 
 
  
  
Alcance 
  
  
  
100% de los clientes de la compañía 
  
 
 
  
  
Resultado 
  
  
  
Archivo de logs + actualización de marcas 
  
 
 
  
  
Trazabilidad 
  
  
  
Obligatoria y auditable 
  
  
**Reglas Generales del Batch** 
 
- El
     proceso debe validar diariamente al 100% de los clientes. 
 
- La
     trazabilidad de cada consulta es obligatoria. 
 
- El
     proceso: 
 
  
- Marca 
  
- Desmarca 
  
- Actualiza
      fechas 
  
- Genera
      logs 
 
 
- Si
     una fuente falla: 
 
  
- Reintenta
      automáticamente 
  
- Registra
      el error 
  
- Continúa
      con los demás clientes 
  
**Descripción Funcional del Proceso Batch** 
**Alcance** 
El proceso batch debe: 
 
- Ejecutarse
     automáticamente todos los días. 
 
- Tomar
     la totalidad de clientes vigentes de la compañía. 
 
- Validar
     cada cliente contra: 
 
  
- Listas
      de control 
  
- PEP 
  
- DIAN 
  
- ADRES 
  
- Informacolombia 
  
- Países
      GAFI 
 
 
- Aplicar
     reglas de coincidencia y decisión. 
 
- Actualizar
     las marcas en los sistemas correspondientes. 
 
- Generar
     un archivo consolidado con logs. 
 
- Guardar
     trazabilidad auditable por cliente y por lista.  
  
**Reglas de Coincidencia (Aplicadas en Batch)** 
**Marcación** 
Una marca se genera cuando: 
 
- Existe
     coincidencia exacta entre los datos del cliente y los datos de la lista,
     según la definición de cada lista: 
 
  
- Tipo
      de documento 
  
- Número
      de documento 
  
- Nombres
      completos o razón social 
  
- País
      de nacimiento o constitución (para GAFI) 
 
 
- La
     fuente consultada confirma que el cliente figura activamente en la lista. 
 
- Si
     en la lista de control se identifican nuevos tipos y números de documentos
     asociados a un cliente entonces se debe validar si tiene vinculaciones
     vigentes. Adicionar resultado al log.  
 
  
  
**Tipo
  de coincidencia** 
  
  
  
**Acción** 
  
 
 
  
  
Coincidencia por 1 dato (número ID) 
  
  
  
Generar log 
  
 
 
  
  
Coincidencia por 2 datos (nombres completos) 
  
  
  
Generar log 
  
 
 
  
  
**Coincidencia exacta (tipo ID + número ID + nombres o
  código de país)** 
  
  
  
Marca directa + log 
  
 
 
  
  
Error en la consulta 
  
  
  
Reintentar + log TI 
  
 
**Desmarcación** 
Una desmarcación ocurre cuando: 
 
- El
     cliente estaba marcado en una ejecución anterior. 
 
- El
     cliente estaba marcado y no tiene vinculaciones activas. 
 
- En
     la consulta actual: 
 
  
- La
      fuente (API) indica que el cliente ya no aparece en la lista. 
  
- El
      país, programa o condición que originó la marca fue retirado o
      actualizado. 
  
**El estado “Se mantiene” aplica cuando:** 
 
- El
     cliente estaba marcado previamente. 
 
- La
     fuente confirma que: 
 
  
- Sigue
      figurando en la lista. 
  
- No
      hay cambios relevantes en: 
  
   
- Tipo
       de programa o sanción 
   
- Condición
       PEP 
   
- País
       de alto riesgo 
   
- Documentos
       asociados 
  
  
**Decisiones por Tipo de Lista (Automáticas)** 
 
  
  
**Lista****** 
  
  
  
**Decisión SARLAFT****** 
  
  
  
**Aplicativo de conexión****** 
  
  
  
**Aplicativo donde queda la marca****** 
  
  
  
**Datos de consulta****** 
  
 
 
  
  
**Lista de control (ONU, OFAC, Grupos
  terroristas)****** 
  
  
  
Marca /
  mantiene / desmarca

  Log cuando coincidencia parcial  
  
  
  
**API
  Infolaft** 
  
  
  
**Riesgos
  consultables** 
  
  
  
Tipo de ID

  Número de ID

  Nombres completos o Razón social 
  
 
 
  
  
**Lista Informacolombia****** 
  
  
  
No se marca

  Genera log  
  
  
  
**API Informacolombia** 
  
  
  
**SARLAFT** 
  
  
  
Tipo de ID

  Número de ID 
  
 
 
  
  
**Lista PEP****** 
  
  
  
Marca / mantiene / desmarca

  Conecta a retipificación si aplica 
  
Log cuando coincidencia parcial 
  
  
  
**PEPS – Infolaft (API)** 
  
  
  
**SARLAFT** 
  
  
  
Tipo de ID

  Número de ID 
  
 
 
  
  
**Lista Proveedores
  Fachada (DIAN)****** 
  
  
  
Marca / mantiene / desmarca  
  
Log cuando coincidencia parcial 
  
  
  
**API Infolaft – Proveedores ficticios** 
  
  
  
**Riesgos consultables** 
  
  
  
Tipo de ID

  Número de ID (confirmar con Infolaft) 
  
 
 
  
  
**Lista IPS Fachada
  (ADRES)****** 
  
  
  
Marca / mantiene / desmarca 
  
Log cuando coincidencia parcial 
  
  
  
**Archivo Excel ADRES** (parametrizable) 
  
  
  
**Riesgos consultables** 
  
  
  
Tipo de ID

  Número de ID 
  
 
 
  
  
**Lista Países de Alto
  Riesgo (GAFI)****** 
  
  
  
Marca / mantiene / desmarca por país 
  
Log cuando coincidencia parcial 
  
  
  
**(Fuente por definir)** 
  
  
  
**SARLAFT** 
  
  
  
Código de país de nacimiento o constitución 
  
 
  
**Trazabilidad Obligatoria (por Cliente y Lista)** 
El batch debe registrar: 
 
- Fecha
     de consulta 
 
- Fuente
     consultada 
 
- Datos
     enviados a la consulta 
 
- Resultado
     obtenido 
 
- Acción
     tomada (marca / no marca / log / alerta) 
 
- Responsable
     (sistema) 
 
- Identificador
     del proceso batch  
**Archivo de logs** 
- Se genera automáticamente al finalizar el batch
diario 
- Contenido según la información de:  
**Resultado de monitoreo** 
 
- DNI
     cliente 
 
- Figura
     (Tomador, Asegurado, Beneficiario, Proveedor, Empleado) 
 
- Vinculación 
 
- Tipo
     de coincidencia 
 
- Tipo
     de lista 
 
- Nombre
     de la lista 
 
- Fecha
     de marcación 
 
- Fecha
     de desmarcación 
 
- Estado
     (Nuevas marcas / Mantienen / Desmarcados) 
 
- Causal
     (Programa, cargo PEP, etc.) 
 
- Empleado
     o proveedor 
 
- Tipo
     de régimen EPS 
 
- País
     nacimiento / constitución 
 
- Tipos
     y números de documento asociados 
 
- Fuente
     consultada 
 
- Fecha
     de consulta 
 
- Resultado
     de la consulta 
 
- Acción
     tomada 
 
- Observaciones
     / inconsistencias  
**Errores técnicos (TI)** 
 
- Fecha 
 
- Fuente 
 
- Cliente 
 
- Motivo
     del error 
 
- Número
     de reintentos 
 
- Estado
     final  
**Control de cobertura** 
 
- Total
     de clientes procesados 
 
- Clientes
     con marca 
 
- Clientes
     con log 
 
- Clientes
     con error 
 
- %
     cobertura del batch

## Criterios de Aceptación

1) Naturaleza del Proceso (Batch Automático) 
 
- Ejecución
     automática: El proceso se ejecuta sin intervención humana dentro de la ventana
     diaria definida (no afecta producción). 
 
- Frecuencia:
     El proceso corre una vez al día todos los días calendario. 
 
- Cobertura:
     El proceso toma el 100% de los clientes vigentes de la compañía (todas las
     figuras y vinculaciones activas). 
 
- Resultado
     mínimo: Al finalizar, el sistema actualiza marcas y genera un archivo de
     logs accesible para SARLAFT. 
 
- Id
     de ejecución: Cada corrida queda identificada con un ID de lote único con
     fecha y hora.  
  
2) Alcance funcional del Batch 
 
- Fuentes/Listas
     incluidas: El proceso valida cada cliente contra:

     Lista de control (ONU/OFAC/grupos terroristas), PEP (Infolaft), DIAN
     (proveedores ficticios), ADRES (IPS fachada), Informacolombia, Países GAFI. 
 
- Reglas
     de decisión: Para cada lista, el sistema marca, desmarca, mantiene o
     registra log, según las reglas definidas. 
 
- Persistencia:
     El sistema escribe la marca/desmarcación/mantenimiento en el aplicativo
     correspondiente (SARLAFT o Riesgos consultables), el mismo día de la
     ejecución.  
  
3) Reglas de Coincidencia (aplicación uniforme en todas las
listas) 
 
- Coincidencia
     por 1 dato (número de ID): El sistema no marca; genera log en el archivo
     diario con la fuente, fecha y datos enviados. 
 
- Coincidencia
     por 2 datos (nombres completos): El sistema no marca; genera log en el
     archivo diario. 
 
- Coincidencia
     exacta (tipo ID + número ID + nombres) o código de país (GAFI): El sistema
     marca al cliente y registra log de soporte. 
 
- Errores
     de consulta: El sistema reintenta automáticamente (política de reintentos
     definida) y registra log técnico con motivo y estado final. El error no
     bloquea el procesamiento de otros clientes. 
 
- Documentos
     adicionales (lista de control): Si la fuente reporta nuevos tipos/números
     de documento asociados al cliente, el sistema valida vinculaciones
     vigentes y adiciona el resultado al log.  
  
4) Marcación (cuándo se marca y qué se guarda) 
 
- Cuándo
     se marca: 
 
  
- Existe
      coincidencia exacta según los datos exigidos por la lista. 
  
- La
      fuente confirma que el cliente figura activamente. 
 
 
- Qué
     se guarda al marcar: 
 
  
- Nombre
      y tipo de lista, fecha de marcación, fecha de consulta, causal/motivo
      (programa, cargo PEP, país de riesgo, sanción), documentos asociados
      (tipo y número), fuente. 
 
 
- Evidencia:
     El evento de marcación aparece en el archivo de logs del día y en la trazabilidad
     del cliente.  
  
5) Desmarcación (cuándo se desmarca y qué se guarda) 
 
- Cuándo
     se desmarca: 
 
  
- El
      cliente estaba marcado y la fuente indica que ya no figura. 
  
- El
      cliente estaba marcado y no tiene vinculaciones activas. 
 
 
- Qué
     se guarda al desmarcar: 
 
  
- Fecha
      de desmarcación, fecha de consulta, causal (retiro de lista, sin
      vinculaciones, actualización de programa/país). 
 
 
- Evidencia:
     La desmarcación aparece en el archivo de logs del día y en la trazabilidad
     del cliente (se conserva histórico).  
  
6) Se mantiene (cuándo aplica y qué se guarda) 
 
- Cuándo
     aplica: 
 
  
- El
      cliente estaba marcado. 
  
- La
      fuente confirma que sigue figurando, sin cambios relevantes en:
      programa/sanción, condición PEP, país de alto riesgo o documentos
      asociados. 
 
 
- Qué
     se guarda: 
 
  
- Fecha
      de última consulta, estado “Se mantiene” en el archivo de logs y
      trazabilidad. 
  
  
7) Decisiones por Tipo de Lista (automáticas y con su
conexión) 
 
- Lista
     de control (ONU/OFAC/grupos terroristas) 
 
  
- Conexión:
      API Infolaft. 
  
- Marca
      en: Riesgos consultables. 
  
- Decisión:
      Marca / Mantiene / Desmarca. Log cuando coincidencia parcial (1 o 2
      datos). 
  
- Datos:
      Tipo ID, Número ID, Nombres completos/Razón social. 
 
 
- Lista
     Informacolombia 
 
  
- Conexión:
      API Informacolombia. 
  
- Marca
      en: SARLAFT. 
  
- Decisión:
      No marca; solo Log. 
  
- Datos:
      Tipo ID, Número ID. 
 
 
- Lista
     PEP (Infolaft) 
 
  
- Conexión:
      PEPS – API Infolaft. 
  
- Marca
      en: SARLAFT. 
  
- Decisión:
      Marca / Mantiene / Desmarca. Si hay coincidencia parcial por nombres → Log.
      Si aplica, retipificación. 
  
- Datos:
      Tipo ID, Número ID. 
 
 
- Lista
     Proveedores Ficticios (DIAN – Infolaft) 
 
  
- Conexión:
      API Infolaft – Proveedores ficticios. 
  
- Marca
      en: Riesgos consultables. 
  
- Decisión:
      Marca / Mantiene / Desmarca. Coincidencia parcial → Log. 
  
- Datos:
      Tipo ID, Número ID (confirmar con Infolaft). 
 
 
- Lista
     IPS Fachada (ADRES) 
 
  
- Conexión:
      Archivo Excel ADRES parametrizable. 
  
- Marca
      en: Riesgos consultables. 
  
- Decisión:
      Marca / Mantiene / Desmarca. Coincidencia parcial → Log. 
  
- Datos:
      Tipo ID, Número ID. 
 
 
- Lista
     Países de Alto Riesgo (GAFI) 
 
  
- Conexión:
      Fuente por definir. 
  
- Marca
      en: SARLAFT. 
  
- Decisión:
      Marca / Mantiene / Desmarca por país. Coincidencia parcial → Log. 
  
- Datos:
      Código de país de nacimiento/constitución. 
  
  
8) Trazabilidad (obligatoria y auditable) 
 
- Registro
     por cliente y lista incluye como mínimo: fecha de consulta, fuente, datos
     enviados, resultado, acción tomada (marca/no marca/log/alerta), responsable
     = sistema, ID de lote. 
 
- Disponibilidad:
     La traza debe poder consultarse por fecha, cliente, lista y lote. 
 
- Integridad:
     La trazabilidad no se sobrescribe; cada corrida añade su registro.  
  
9) Archivo de Logs (evidencia operativa diaria) 
 
- Generación:
     El archivo se genera automáticamente al finalizar el batch del día. 
 
- Contenido
     mínimo – Resultados de monitoreo:

     DNI cliente, Figura, Vinculación, Tipo de coincidencia, Tipo de lista, Nombre
     de la lista, Fecha de marcación, Fecha de desmarcación, Estado (Nuevas
     marcas / Mantienen / Desmarcados), Causal (programa, cargo PEP, país,
     sanción), Empleado/Proveedor, Tipo de régimen EPS, País
     nacimiento/constitución, Documentos asociados, Fuente consultada, Fecha de
     consulta, Resultado de la consulta, Acción tomada,
     Observaciones/inconsistencias. 
 
- Errores
     técnicos (hoja separada): Fecha, Fuente, Cliente, Motivo del error, Número
     de reintentos, Estado final. 
 
- Control
     de cobertura (hoja separada): Total de clientes procesados, Clientes con
     marca, Clientes con log, Clientes con error, % cobertura del batch.  
  
10) Manejo de errores y continuidad 
 
- Reintentos
     automáticos: Ante errores de consulta, el sistema reintenta según política
     definida y registra cada intento. 
 
- Continuidad:
     Una falla en una fuente no detiene la ejecución del resto de clientes ni
     de otras listas. 
 
- Registro:
     Todo error deja huella en el archivo de errores y en la trazabilidad.  
  
11) Disponibilidad del resultado 
 
- Oportunidad:
     El archivo de logs y las marcas actualizadas deben estar disponibles el
     mismo día de la ejecución. 
 
- Acceso:
     El archivo queda accesible para descarga desde la pantalla de consulta
     (histórico por fecha/lote).  
  
12) Controles de calidad y consistencia (funcionales) 
 
- Cobertura
     = 100%: El control de cobertura debe reportar 100% de clientes de la base
     vigente del día. 
 
- Consistencia
     de datos: Tipos de documento y países se validan contra catálogos
     parametrizados (formato y códigos). 
 
- Duplicidad:
     No se crean marcas duplicadas para el mismo cliente-lista-lote.
