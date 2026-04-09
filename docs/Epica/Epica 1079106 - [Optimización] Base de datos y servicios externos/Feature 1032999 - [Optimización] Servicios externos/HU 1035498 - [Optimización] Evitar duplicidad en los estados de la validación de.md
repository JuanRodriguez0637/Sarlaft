# HU 1035498 — [Optimización]: Evitar duplicidad en los estados de la validación de identidad- Datos básicos

[Épica 1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106) › [Feature 1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999) › HU 1035498 — [Optimización]: Evitar duplicidad en los estados de la validación de identidad- Datos básicos

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1035498](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1035498) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-05 |
| **Última modificación** | 2026-03-16 |

## Jerarquía

- **Épica:** [1079106 — [Optimización]: Base de datos y servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1079106)  
  Estado: New  
- **Feature:** [1032999 — [Optimización]: Servicios externos](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032999)  
  Estado: New  

## Descripción

Como Analista SARLAFT quiero que, antes de iniciar el flujo de validación de identidad que realiza la consulta datos básicos, el sistema evalúe estados bloqueantes para impedir el inicio del flujo cuando se presente alguna condición que lo invalide y emitir mensajes claros, evitando costos y fricción innecesaria. **
** **Alcance** 
- **Tipo de operación:** negocio nuevo y reclamaciones 
- **Tipo de persona: **Natural 
- **Tipos de documentos: **cédula de ciudadanía, cédula de extranjería y permiso por protección temporal 
- **Momento de notificación:** 
- Cuando un cliente realice por primera vez el flujo de validación de identidad y, durante el diligenciamiento del cuestionario, el servicio de Experian retorne alguno de los estados bloqueantes, cualquier nueva evaluación que se cree posteriormente deberá responder de forma inmediata con estado **Rechazado**, asociándolo a dicha causal.   
- **Mecanismos para crear evaluaciones** 
- Modulo de clientes sarlaft 
- Servicio de crear evaluación que se expone a los aplicativos de negocio y la API de terceros  
- **Mecanismos para activar el flujo de validación de identidad** 
- Enlace del formulario notificado por medio del modulo de clientes Sarlaft - Crear evaluación 
- Botón de copiar y pegar el enlace en un navegador que se extrae en el modulo de clientes Sarlaft - consultar cliente - tipo de operación - negocio nuevo y reclamaciones 
- Botón para reenviar formulario cuando se consulta un cliente en el modulo de clientes sarlaft - consultar cliente - tipo de operación - reclamaciones 
- Enlace del formulario para validar identidad cuando se completa el diligenciamiento del formulario 
- Flujo integrado en el webcomponent 
- Flujo integrado en la API de terceros    **** **Estados bloqueantes (para el cuestionario)** 
- 
- EXCEDIDO NÚMERO DE INTENTOS DE VALIDACIÓN 
- NO EXISTE IDENTIFICACIÓN 
- NO FUE POSIBLE REALIZAR LA VALIDACIÓN      **Reglas de negocio**   
- **R1. Alcance de documento: **Aplica exclusivamente para Cédula de Ciudadanía, cédula de extranjería y permiso por protección temporal. Otros tipos de documento siguen flujo normal.** 
- **R2. Filtro previo obligatorio:** Si el estado coincide con cualquiera de los cinco bloqueantes, no debe dar continuidad a la evaluación y se debe rechazar la evaluación por esa evidencia. Teniendo en cuenta: 
- Mensaje en el servicio que crea la evaluación: **"No es posible continuar con el proceso. El proceso de validación de identidad no ha sido exitoso" (Definido actualmente) 
- **Mensaje en el modulo de clientes sarlaft: **"El proceso de validación de identidad no ha sido exitoso: (Detallar el estado bloqueante)"  
- **R3. Estados definitivos: **Los estados listados son bloqueantes y definitivos. Deben almacenarse y reutilizarse en toda reconsulta según las reglas de filtros previos:** 
- Cuando el estado es EXCEDIDO NÚMERO DE INTENTOS DE VALIDACIÓN, NO EXISTE IDENTIFICACIÓN y NO FUE POSIBLE REALIZAR LA VALIDACIÓN se debe almacenar solo por 1 mes y rechazar las nuevas evaluaciones por esa causal durante ese mes. 
- Ejemplo: **El 4 de febrero del 2026 a las 2:00 pm el cliente "NO EXISTE IDENTIFICACIÓN "; si el cliente vuelve a intentar entre las 4 al 28 de febrero del 2026, se debe rechazar la evaluación por esa causal. El día 01 de marzo del 2026, se permite volver a realizar el flujo de validación de identidad.   
- **R5. Estados sin bloqueo: **Los estados a los que no aplica la regla de bloqueo deberán conservar el estado de la evaluación asignado, sin generar cambios en su resultado. 
- **R6: Persistencia obligatoria: **La primera vez que se obtenga un estado definitivo, se debe guardar con los definidos actualmente en el diccionario del webhook.

## Criterios de Aceptación

**CA-01. **Evaluación de filtro previo: Antes de iniciar la validación de datos básicos, el sistema debe verificar si el estado actual coincide con alguno de los tres estados bloqueantes. 
**CA-02. **Bloqueo del flujo: Si existe coincidencia con un bloqueante, el sistema no debe iniciar el flujo de validación y debe devolver el mensaje estandarizado correspondiente. 
**CA-03. **No escalamiento: Al bloquear por estado, el sistema no debe realizar llamadas a servicios externos ni continuar con pasos subsiguientes. 
**CA-04. **Trazabilidad del bloqueo: Se debe registrar en bitácora: tipo_id, numero_id, canal, estado_bloqueante, accion = BLOQUEO_FLUJO_DATOS_BASICOS, timestamp, usuario/servicio, correlacion/id_sesion. 
**CA-05. **Reglas de reintento (si aplican): Cuando el bloqueo sea por intentos excedidos, el sistema debe informar cuándo se habilitaría un nuevo intento (fecha/hora estimada), si la política existe. 
**CA-06. **Estados no bloqueantes: Si el estado no coincide con la lista bloqueante, el flujo de validación de datos básicos debe iniciar normalmente.
