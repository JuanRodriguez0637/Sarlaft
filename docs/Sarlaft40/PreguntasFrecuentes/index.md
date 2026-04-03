# Preguntas frecuentes - Sarlaft

> **Fuente Confluence:** [Preguntas frecuentes - Sarlaft](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/1928167429/Preguntas+frecuentes+-+Sarlaft)
> **Última modificación:** 2021-04-29 — Jaime Andrés Sossa Quiceno · versión 3
> **Sección:** 07) Dominio Soluciones Corporativas / Sarlaft 4.0

## ¿Cuáles son los campos mínimos para enviar a sarlaft?

Estos campos se pueden encontrar en la documentación de sarlaft en Confluence:

[Documento Diseño Técnico](../DocumentacionTecnica/DisenoArquitectura/DocumentoDisenoTecnico/index.md)

## ¿Qué pasa si no envió los campos opcionales?

Dentro de los campos opcionales existen campos que cada solución podría enviar y esto podría cambiar el tipo de formulario que debe llenar. Ejemplo Si movilidad envía el campo opcional X para cierto tipo de transacción se le pedirá el formulario simplificado pero si no lo envía se pedirá el ordinario.

## ¿Cuáles son los campos "obligatorios" por solución dentro de los opcionales para cada solución?

Los campos obligatorios se encuentan este documento tecnico [Documento Diseño Técnico](../DocumentacionTecnica/DisenoArquitectura/DocumentoDisenoTecnico/index.md). Laura Camila unificará por parte del equipo de sarlaft cuales son esos "obligatorios" por solución en un documento.

## ¿Existen servicios de catálogos?

## ¿Como envió las preguntas PEPS para Sarlaft?

Existen dos opciones: 1. Si la solución sabe que solo llenará un formulario simplificado entonces puede solicitar estas preguntas en tu pantalla y envías estas por el servicio. 2. Si la solución puede llenar simplificado u ordinario o intensificado entonces puede delegar que el formulario de Sarlaft sea quien solicite estas preguntas PEPS.

## ¿Si en mi proceso de Sarlaft no estoy obligado a esperar la respuesta de Sarlaft, como puedo validar si ya lleno los formularios?

Se puede consumir un servicio web que informa a partir de un ID evaluación si el formulario ya fue diligenciado o no.

Los webhook expuestos para Sarlaft deben ser REST con autenticación Seus, ¿Que sucede si mi plataforma no tiene autenticación Seus o capacidad de exponer servicios REST?

Se sugiere buscar la manera de tener una capa intermedia que habilite las tecnologías sugeridas por el equipo de Sarlaft. En caso que esto no sea posible se sugiere validar con Sarlaft cual es la particularidad y si esta puede ser parametrizada (no se tiene autenticación Seus pero si se puede tener autenticación Basic), en caso tal que técnicamente no se encuentre una solución, se puede validar con el equipo de Sarlaft si es posible consumir un servicio que notifique el estado de Sarlaft, con la particularidad que el consumidor debe consumir este servicio cada X tiempo hasta recibir una respuesta.

## ¿El webhook será llamado cuando el proceso de Sarlaft se rechace?

Si, existen validaciones restrictivas que no permitirá vincular (expedir) el negocio, pues de acuerdo al análisis de Sarlaft esta persona puede hacer un lavado de activos.

## ¿Cuándo Sarlaft rechace un proceso como procede la solución?

Cuando sea Sarlaft quien rechace el negocio, este devuelve un mensaje indicando que no se puede proceder en la venta el cual será pintado al cliente.

## ¿El webhook será llamado en casos de alerta, ej: la registraduría indica que la cedula es falsa, o que la persona es PEP?

Si, el webhook será llamado para notificar este tipo de alertas, cada negocio debe decidir si estas alertas afectan o no su proceso de venta.

## ¿Si existen varias personas en una solicitud(tomador y beneficiarios) a quien se le pide el Sarlaft?

Depende de cada solución, se deben enviar todos los parámetros obligatorios de Sarlaft y cada una de las personas de las póliza, ya Sarlaft determina a cuales de las tres personas le pide llenar el formulario.

## ¿Si existen varias personas en una solicitud y Sarlaft determina que necesita información de los beneficiarios pero el tomador no la sabe, entonces que sucede?

Una de las preguntas para el tomador es si conoce la información de los beneficiarios y si puede validar la identidad, si responde que sí, entonces se le pedirá esta información de lo contrario se continua el proceso solo con la información del tomador.

## ¿Si existen varias personas en una solicitud y Sarlaft determina que necesita información de los beneficiarios el tomador no la sabe, el tomador puede llenar la información?

Una de las preguntas para el tomador es si conoce la información de los beneficiarios y si puede validar la identidad, si responde que sí, entonces se le pedirá esta información de lo contrario se continua el proceso solo con la información del tomador.

## Cuando se invoca el primer servicio que me notifica que formularios debo llenar, también me retorna un listado de controles, ¿que se deben hacer con esos controles?

Dependiendo de cada solución, algunas soluciones puede mostrar el control en pantalla otras deciden no hacerlo.

## Cuando existe un control que requiere una aprobación por otra persona de la compañía, ¿Que se debe hacer?

Este proceso ya existe, cada solución determina como gestionar estos controles para permitir la vinculación.

## ¿Si al llamar el webhook Sarlaft rechaza mi solicitud, es posible editar la solicitud y volver a enviarla?

Depende de la respuesta dada por Salarft, si el freno ocurre por que el cliente es un riesgo consultable moral o la cedula es falsa no se debe permitir expedir para esa persona, pero si se cambia la persona con la limitante y al volver hacer el proceso de sarlaft este es exitoso entonces se puede expedir.

## ¿Si el modelo de venta que requiere sarlaft tiene ventas masivas (varios riesgos y varios asegurados), debo solicitar sarlaft para todos los asegurados y tomador?

Depende, cuando existe una relación laboral entre el tomador de la póliza y los asegurados, no es necesario solicitar diligenciar sarlaft para los asegurados, pero si no existe esta relación laboral se debe solicitar diligenciar sarlaft para las dos figuras de la póliza.

## ¿Si estoy modificando una poliza existente es necesario sarlaft?

No, el sarlaft no aplica para modificaciones, pero la solución debe garantizar que se solicite la validación de riesgos consultables en modificaciones.
