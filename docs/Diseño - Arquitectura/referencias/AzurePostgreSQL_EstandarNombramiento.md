# Azure Database for PostgreSQL

>**Fuente:** [Ver en Confluence](https://segurosti.atlassian.net/wiki/spaces/AR/pages/1381761738)
>**Space:** AR - Dominio Transformación Tecnológica
>**Versión:** 9

## ESTÁNDARES DE ARQUITECTURA DE DATOS PARA BASES DE DATOS POSTGRESQL

### CONSIDERACIONES:

- En azure Postgresql la lógica de desarrollo en base de datos no está permitida por lineamientos de Arquitectura, esto incluye procedimientos almacenados, triggers, etc.

El Acceso a las bases de datos en Azure solo debe realizarse de manera privada de acuerdo a los lineamientos definidos de la compañía. (ver documento lineamientos de Nube)

No se permite el uso de funciones en postgresql dado que se sugiere que la lógica de negocio o aplicación se realice directamente en la aplicación y no en la base de datos.

Los triggers no se recomiendan usar para el manejo de secuencias. Se recomienda usar la función nativa de la base de datos para el manejo de secuencias (nextval)

Identificadores en Postgresql

Identificadores son nombres asociados a columnas, tablas y otros objetos de BD pueden ser: sin comillas o con comillas y tienen estas restricciones

La longitud máxima es 63 caracteres (más de eso se truncan)

Los identificadores sin comillas deben empezar con una letra o el carácter “_”, los demás caracteres pueden ser letras, números o “_”

Identificadores con comillas deben:

Estar encerrados entre comillas dobles (“)

Pueden contener cualquier carácter  como espacios o símbolos

No pueden estar vacíos

Soportan los mismos caracteres de escape que los strings

Una Keyword debe ser un identificador quoted

#### ESTÁNDAR PARA LA NOMENCLATURA DE OBJETOS DE BASE DEDATOS

##### Alcance

El alcance de este documento es definir el estándar de nombramiento de objetos en las bases de datos azure postgresql, para el desarrollo de todas las aplicaciones de la compañía.

##### Definición

Lograr una mejor comprensión de los modelos de datos por parte de todos los analistas de la compañía.

##### Definición de estándares

##### ESTANDAR DE NOMBRAMIENTO DEL RECURSO DE LA BASE DE DATOS.

La base de datos debe crearse con la siguiente notación.

La instancia debe alojar únicamente bases de datos correspondientes a la compañía con la cual fue nombrada.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

psql-com+nombredescriptivo+ambiente+randomsufijo

||

**psql:**indicador base de datos Azure postgresql

**com:**indicador de la compañía (ver plantilla)

**nombredescriptivo:** nombre de la base de datos que indique el producto o aplicación al que le prestara servicio.

**Ambiente:** indicador del ambiente de la base de datos (ver plantilla)

**Randomsufijo:** Este valor se debe enviar el parámetro de acuerdo al ejemplo(random_id.suffix). Este valor es importante dado que se requiere garantizar que el nombre de la base de datos sea único a nivel global.

**Nota:** El signo + no debe ir dentro del nombre

||

| **

**Plantilla de Compañías**
**|**
**Plantilla de Ambientes**
** |

||

`sr` – suramericana, transversal.

`eps` – Maquina que presta servicio a la IPS y EPS Sura.

`arl` – Maquina que presta servicio a la Aseguradora de Riesgos Laborales ARL Sura.

`din` – Maquina que presta servicio a Dinámica.

`seg` – Maquina que presta servicio a las compañías de Seguros.

||

[`p`] Producción

[`l`] Laboratorio

[`d`] Desarrollo

[`sa`] Sitio Alterno

||

 **Ejemplo:**

server-name    = "psql-${var.company-identifier}${var.basename}${var.environment-letter}${random_id.suffix.hex}"

Nota: Si requiere ampliar información con relación a la creación del recurso de postgresql en Azure puede consultarlo en el siguiente link:

[https://bitbucket.org/segurossuracolombia/azurerm-postgresql/src/v1.0/](https://bitbucket.org/segurossuracolombia/azurerm-postgresql/src/v1.0/)

##### ESTANDAR DE NOMBRAMIENTO Y DIMENSIONAMIENTO DE BASE DE DATOS

- Tenga en cuenta lo siguiente:

[https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS)

[https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_upper_case_table_or_column_names](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_upper_case_table_or_column_names)

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc

 No debe contener números.

Evite abreviaciones (puede llevar a una a la interpretación de los nombres)

Evite usar espacios en blanco en los nombres.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

`amb+nombredescriptivo`

||

`amb`: Ambiente en el cual se encuentra la base de datos (ver plantilla de ambientes).

`nombredescriptivo`: Nombre del Producto, aplicación o proyecto que hará uso de la base de datos.

||

**Ejemplo:**  `pdnseus`

Nota:

En azure Postgresql la lógica de desarrollo en base de datos no está permitida por lineamientos de Arquitectura, esto incluye procedimientos almacenados, triggers, etc.

##### ESTÁNDAR DE NOMBRAMIENTO DE ESQUEMAS

Deben crearse en Mayúscula.

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc

 No debe contener números.

Evite abreviaciones (puede llevar a una a la interpretación de los nombres)

Evite usar espacios en blanco en los nombres.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

ESQ+NOMBREDESCRIPTIVO + AMB

||

**AMB**: Ambiente en el cual se encuentra la base de datos (ver plantilla de ambientes).

**NOMBREDESCRIPTIVO**: Nombre del Producto, aplicación o proyecto que hará uso de la base de datos.

||

**Ejemplo:**  ESQSEUSPDN

Nota:

En azure Postgresql únicamente estará permitida la creación de un esquema por base de datos con el objetivo de garantizar la separación de la lógica de las aplicaciones.

##### ESTANDAR DE NOMBRAMIENTO DE OBJETOS EN BASE DE DATOS

###### CONSTRAINTS DE CHEQUEO

- Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Los nombres deben ser en minúscula.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

nombre_tabla_ck##

||

**nombre_tabla**: Nombre de la tabla a la que se le crea  el constraint

**ck**: Identificador de check constraint.

**##:**Consecutivo que indica el n-ésimo constraint de chequeo de la tabla

||

**Ejemplo:**  tcpt_datos_basicos_ck03

 **Nota**: Estas constraints de chequeo deben crearse tanto para campos SN como para campos OP ya que determinarán los valores que pueden ser ingresados al campo.  Para las constrains binarias que ya hagan uso de char debe crear constraint de chequeo, aunque se recomienda el uso de boolean como tipo de dato.

###### LLAVES ÚNICAS

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Los nombres deben ser en minúscula.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

nombre_tabla_uk##

||

**nombre_tabla**: Nombre de la tabla a la que se le crea  el constraint

**uk**: Identificador del constraint de clave única.

**##:**Consecutivo que indica la n-ésima llave única de la tabla

||

  **Ejemplo:**  tcpt_datos_basicos _uk02

**NOTAS:**

No es necesario crear índices dado que postgresql los crea de manera automática.

###### LLAVES FORÁNEAS

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Los nombres deben ser en minúscula.

||

**NOTACIÓN**

||
||

nombre_tabla_referenciante_nombre_tabla_referenciada_fk##

||
||

**DEFINICIÓN DE CAMPOS**

||
||

**nombre_tabla_referenciante**: Nombre de la tabla a la que se le crea el constraint**nombre_tabla_referenciada**: Nombre de la tabla que se referencia con el constraint

**fk**: Identificador del constraint de clave foránea.

**##:**Consecutivo que indica la n-ésima llave foránea de la tabla

||

  **NOTAS:**

Si la longitud del nombre de la clave foránea excede los 30 caracteres, se deben utilizar acrónimos del nombre de las tablas.

No se recomienda crear para las claves foráneas un índice dado que postgresql lo hace de manera automática. Deigual forma se puede crear en los siguientes dos casos:

Si realiza un Join entre las dos tablas

Si se borran filas  o se actualizan columnas primarias en la tabla destino.

Es importante tener presente que a medida que una tabla tiene demasiados índices va a generar un mayor acceso a disco cada vez que se inserta o se elimina un registro, o se presentan updates que involucren columnas que hacen parte de la estructura de un índice y adicionalmente se pueden presentar índices duplicados.

  **Ejemplo:**

tosi_anticipo_mesada_benef_fk02

tcpt_datos_basicos_tper_tipos_personas_fk03

###### LLAVES PRIMARIAS

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Los nombres deben ser en minúscula.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

nombre_tabla_pk

||

**nombre_tabla**: Nombre de la tabla a la que se le crea el constraint**pk**: Identificador del constraint de clave primaria.

||

 **Ejemplo:**  tcpt_datos_basicos_pk

  **ÍNDICES**

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Los nombres deben ser en minúscula.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

nombre_tabla_i##

||

**nombre_tabla**: Nombre de la tabla a la que se le crea el índice

i: Identificador del índice.

**##:**Consecutivo que indica el n-ésimo índice de la tabla

||

 **Ejemplo:**  tpersonas_subgrupos_mvtos _i03

###### Incrementales

Ver documento para crear secuencias: [https://www.postgresql.org/docs/11/sql-createsequence.html](https://www.postgresql.org/docs/11/sql-createsequence.html)

 **Nota**:

Postgresql automáticamente maneja los campos autoincremental , no se deberían utilizar las secuencias de manera especifica para casos de uso de la anterior.

Aunque postgresql soporta campos tipo autoincrementales conocidos (serial types) la recomendación es usar en su lugar las columnas  identity en el estandar SQL [https://www.postgresql.org/docs/11/sql-createtable.html](https://www.postgresql.org/docs/11/sql-createtable.html)

Como no se crea sequencias el estándar de nombramiento que aplica es el estándar de columna.

###### TABLAS

Este no debe exceder los **63 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Debe indicar que información va a almacenar la tabla

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

TNNN_XXXXX

||

**T**: Indicador de tabla

**NNN**: Identificador de la aplicación. (3 letras representativas

**XXXXX**: Nombre nemotécnico que identifica la tabla, debe estar en

plural

||

 **Ejemplo**:

TPER_TIPOS_PERSONAS

###### COLUMNAS

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Debe indicar que información va a almacenar la tabla

Es permitido usar el underscore ( _ ) para nombres compuestos por varias palabras

Debe ser en singular

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

XXNOMBRE_COLUMNA

||

**XX**: Son dos letras que identifican el contenido de la columna así:

**DS**: Descripción

**NM**: Número

**CD**: Código alfanumérico ó numérico FE: Fecha

 **SN**: Respuesta Si o No.

 **PO**: Porcentaje

 **PT**: Valor Numérico (IVA, Impuesto, etc.)

**OP**: Opción, funciona igual que SN pero puede aceptar un  rango de valores diferentes.

**NOMBRE_COLUMNA:**Nombre de la columna

||

 **Ejemplos:**

CDRAMO: Código del ramo (Alfanumérico)

CDSERVICIO: Código del servicio (Numérico)

FEALTA: Fecha de alta.

PORETENCION: Porcentaje de retención.

DSTOMADOR: Nombre del tomador.

PTIVA: Valor del IVA.

OPACCION: Acción a tomar (S, I, D, U )

**Consideraciones especiales:**  La columna nombrada DNI en la cual se almacena un número de identificación (cédula,  NIT, tarjeta de identidad, etc.) se debe nombrar de la siguiente manera:

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

DNI_`<XXXXXX>`

||

**DNI**: Indica que es un documento de identidad

**XXXXXX:**El sujeto que se está identificando (agente, usuario, afiliado, tomador, paciente, etc.)

||

 **Nota**:

En ningún caso se debe utilizar las siglas CD o NM precediendo la sigla DNI.

Las columnas definidas de tipo numerico deben tener longitud definida. Si la columna almacena decimales, se debe indicar su presición.

[https://www.postgresql.org/docs/9.1/datatype-numeric.html](https://www.postgresql.org/docs/9.1/datatype-numeric.html)

Las columnas que almacenen información de tipo alfanumérica deben ser siempre de tipo_**VARCHAR**_ independientemente si es de uno o varios caracteres y se debe especificar su longitud

Las columnas de tipo  OP o SN, siempre se deben definir como _**VARCHAR (1),**_adicionalmente deben tener definido un constraint de chequeo.

Las columnas que vayan a almacenar fechas deben ser definidos como_**DATE**_ ó_**TIMESTAMP**_ para los casos que se requiera almacenar unidades inferiores al segundo

Recomendamos usar el campo  timestamp [ (p) ] [ without time zone ] para no depender de la zona horaria de la base de datos.

La columna que esté haciendo referencia a una tabla deberá llamarse exactamente igual a como se llama la columna primaria de la tabla a la que referencia. Con excepción de aquellos que no cumplen con el estándar de nombramiento de columnas.

  **Ejemplo:**

Para los siguientes ejemplos se toma que la tabla TPER_PERSONAS es una tabla nueva o que la columna CDCARGO es nueva.

 En el ejemplo se observa que el nombre de la columna CDCARGO en la tabla TPER_PERSONAS tiene el mismo nombre que la columna referenciada en la tabla TPER_CARGOS.

1.

 En el ejemplo se observa que el nombre de la columna CDCARGO en la tabla TPER_PERSONAS tiene un nombre diferente a la columna referenciada en la tabla TPER_CARGOS. Asumiendo que la tabla TPER_CARGOS pertenece a una aplicación caja negra (que no cumple con estándar de nombramiento) o que es una tabla muy vieja, se admite que sean diferentes siempre y cuando la nueva columna cumpla con el estándar de nombramiento.

**Notas:**

Si un columna existe en más de un objeto, deberá conservar ese nombre a través de todos los objetos en los que se utilice. Con excepción de aquellos que no cumplen con el estándar de nombramiento de columnas.

Todos las columnas deben tener**comentarios** en la base de datos acerca de su significado (comments), estos deben ser lo más descriptivos posible.

**VISTAS**

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Debe estar en plural

Se puede usar el caracter underscore ( _ ) para crear nombres más lógicos

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

WNNN_NOMBRE_VISTA

||

**W**: Identificador de vista.

**NNN**: Prefijo del nombre de la aplicación. Es 999 cuando se trata de  una vista corporativa (que pueden servir a más de una aplicación)

**NOMBRE_VISTA:** Nombre nemotécnico de la vista

||

**Ejemplo:**  WDIN_Resultados_Laboratorio

**NOTA:** La definición de todas las vistas y sus respectivas columnas, deben incluir documentación en la base de datos (comments). El comment asignado a la vista y sus columnas debe ser idéntico al definido para la tabla en el diccionario de datos.

**Objetos con el mismo nombre en diferentes bases de datos**

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

NOMBRE_OBJETO_NNN

||

**NOMBRE_OBJETO:**Nombre nemotécnico del objeto referenciado**NNN:** Prefijo del nombre de la base de datos donde se encuentra el objeto.

||

 **Ejemplo:**  CUERPOLIZA_BAN

**SNAPSHOTS O VISTAS MATERIALIZADAS**

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

Debe estar en plural

Es permitido usar el underscore ( _ ) para crear nombres más lógicos

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

MNNN_NOMBRE_VISTA

||

**M:** Identificador de vista materializada

**NNN:** Prefijo del nombre de la aplicación. Es 999 cuando se trata de una vista corporativa (que pueden servir a más de una

aplicación)

**NOMBRE_VISTA:**Nombre nemotécnico de la vista materializada

||

 **Ejemplos:**

MPER_AFILIADOS_POS < == Correcto

M_PER_AFILIADOS_POS < == Incorrecto

M_PERAFILIADOSPOS < == Incorrecto

**NOTA:** La definición de todas las vistas materializadas y sus respectivas columnas, deben incluir documentación en la base de datos (comments). El comment asignado a la vista y sus columnas debe ser idéntico al definido para la tabla en el diccionario de datos.

**FUNCIONES**

Solo se pueden implementar con el estándar SQL estandard, no se permite lógica PLSQL – JAVA.

Este no debe exceder los **30 caracteres**

No debe contener caracteres especiales, tales como "%", "$", etc.

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

FN_NNN_<NOMBRE_FUNCION>

||

**FN**: Identificador de función.

**NNN**: Prefijo del nombre de la aplicación.

**NOMBRE_FUNCION:** Nombre nemotécnico de la función

||

 **Ejemplo:**  FN_SCI_CALCULAR_CDRAMO

**NOMBRAMIENTO DE USUARIOS**

El nombramiento de los usuarios para un nuevo esquema será:

Para el caso en que la abreviación para el usuario sea ampliamente conocida o que se caracterice claramente el usuario a crear, es válido crearlo con el siguiente esquema:

  Usuario administrador de instancia

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

ADMPGXXXA

||

**ADM:**Identificador de usuario dueño de esquema

**PG**: IDENTIFICADOR DE azure Postgresql

**XXX**: Identificador del aplicativo para el usuario

**A**: Ambiente

     [P] Producción

     [L] Laboratorio

     [D] Desarrollo

     [SA] Sitio Alterno

||

EJEMPLO: **ADMPGSEUSL**

- **Usuario dueño de esquema:**

||

**NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

ADMXXXAMB

||

**ADM:**Identificador de usuario dueño de esquema

**XXX**: Identificador del aplicativo para el usuario

**AMB**: Ambiente

    [PDN] Producción

    [LAB] Laboratorio

    [DLL] Desarrollo

    [SA] Sitio Alterno

||

EJEMPLO: **ADMSEUSLAB**

- **Usuario de conexión a la aplicación:**

||

 **NOTACIÓN**

||

**DEFINICIÓN DE CAMPOS**

||
||

MODXXXAMB

||

**MOD**: Identificador del aplicativo para el usuario

**XXX**: Identificador del aplicativo para el usuario

**AMB**: Ambiente

     [PDN] Producción

     [LAB] Laboratorio

     [DLL] Desarrollo

     [SA] Sitio Alterno

||

**Ejemplo:MODSEUSLAB**
