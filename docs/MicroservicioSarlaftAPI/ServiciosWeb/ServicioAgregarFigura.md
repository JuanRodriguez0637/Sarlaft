# Servicio Agregar Figura

**Fuente Confluence:** [Servicio Agregar Figura](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2252832800)
**Sección:** [Servicios Web](../index.md)

---

- **Objetivo:** Permite agregar una persona con unas figuras en especifico a una evaluación existente, si la persona ya existe en la evaluación se actualizan los datos siempre y cuando la persona no halla sido cancelada en esta evaluación
- **Endpoint:** /sarlaftserv/assessment/figure/add
- **Perfil de Seus4:** PF_CONSUMSERVSARLAFTAPI
- **Ejemplo Json Request:**

[`requestBeneficiario.json`](./ServicioAgregarFigura/requestBeneficiario.json) | [`requestAcionista.json`](./ServicioAgregarFigura/requestAcionista.json) | [`requestConsorcio.json`](./ServicioAgregarFigura/requestConsorcio.json)

- **Descripción del flujo:** para el flujo de adicionar figura a un proceso de evaluación se tienen en cuenta varias secciones del objeto request que se hace al servicio, el objeto cliente es una parte importante del request adicionar figura pues los clientes se clasifican en **TipoPersona** (*N, J*), personas Naturales y personas Jurídicas, las cuales a su vez pueden pertenecer a un tipo de figura/rol que representan dentro de una evaluación **Figura.Tipo** (*APODERADO, BENEFICIARIO, TOMADOR, ASEGURADO, AFILIADO, AFIANZADO, REPRESENTANTE_LEGAL, ACCIONISTA, CONSORCIO*).

- **Notas:**

1. Solo se permite agregar figuras nuevas a evaluaciones que no tengan estado *CANCELADO, FINALIZADO, RECHAZADO*. Para el caso de evaluaciones de tipo carga masiva si permite agregar la figura así la evaluación tenga estado *FINALIZADO*.
2. En caso que se quiera agregar al proceso de evaluación una figura de tipo *REPRESENTANTE_LEGAL, ACCIONISTA* ó *CONSORCIO*, esta quedará asociada a un cliente existente en la evaluación. Para generar la nueva asociación se deben ingresar en el objeto request los campos **dniClientePadre** (Dni del cliente al que se quiere asociar la nueva figura) y **tipoEmpresa** (*PYMES, ESAL, SAS, CONSORCIO*) que hace referencia al tipo de empresa de la figura padre.
3. Al agregar una figura de tipo *REPRESENTANTE_LEGAL, ACCIONISTA* ó *CONSORCIO*, en la respuesta del servicio el campo requiereDirectivos (*true, false*) indica si hacen falta directivos teniendo en cuenta los mínimos requeridos según el tipo de empresa Ingresado. Para el resto de figuras el campo requiereDirectivos tendrá un valor de *null*.
4. Solo se pueden crear asociaciones a clientes que sean de TipoPersona (**J**).

- **Dependencias:**
  - Base de Datos Sarlaft
  - Aplicaciones Externas.
