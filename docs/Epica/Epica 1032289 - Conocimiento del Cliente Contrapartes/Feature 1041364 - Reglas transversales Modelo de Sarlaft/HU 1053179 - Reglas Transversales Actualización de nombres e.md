# HU 1053179 — [Reglas Transversales]: Actualización de nombres en tablas paramétricas - Front

[Épica 1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289) › [Feature 1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364) › HU 1053179 — [Reglas Transversales]: Actualización de nombres en tablas paramétricas - Front

---

## Información General

| Campo | Valor |
|-------|-------|
| **ID** | [1053179](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1053179) |
| **Estado** | New |
| **Iteración** | `Gerencia_Tecnologia\2025 [11 días hábiles]` |
| **Área** | `Gerencia_Tecnologia\do-soluci_corporativas-Fortalecimiento SARLAFT` |
| **Tags** | Equipo Base |
| **Creado** | 2026-02-23 |
| **Última modificación** | 2026-03-02 |

## Jerarquía

- **Épica:** [1032289 — [Conocimiento del Cliente]: Contrapartes](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1032289)  
  Estado: New  
- **Feature:** [1041364 — [Reglas transversales]: Modelo de Sarlaft](https://dev.azure.com/SuraColombia/Gerencia_Tecnologia/_workitems/edit/1041364)  
  Estado: New  

## Descripción

Como administrador del módulo de Clientes SARLAFT,
 quiero que en el Motor de Reglas, dentro de las Tablas Paramétricas, se actualicen los nombres del “Tipo de tabla” en todas las vistas donde se consulta, filtra o matricula,
para que los usuarios administradores visualicen los valores actualizados “Vigiladas, Multilaterales y Universidades", en lugar de las opciones actuales “Financieras”, “Aseguradoras” y “FP”, manteniendo intactas las demás opciones del catálogo. 
 **Descripción Funcional del Cambio** 
El cambio debe aplicarse en tres zonas del módulo de Clientes SARLAFT dentro de Configuración → Motor de reglas → Tablas paramétricas:   **1. Opción “Consultar”** 
- En el filtro Tipo de tabla, los valores deben actualizarse a:

- Vigiladas, Multilaterales y Universidades   
- El resto del catálogo debe mantenerse sin modificaciones.    **2. Resultados de la consulta** 
- Cuando el usuario aplique un filtro y se muestre la tabla de resultados:

- En la columna Tipo de tabla, deben aparecer el campo actualizado “Vigiladas, Multilaterales y Universidades" 
- Las demás columnas se mantienen sin cambios.      **3. Opción “Matricular”** 
- En el formulario “Matricular”, el campo Tipo de tabla debe mostrar el campo actualizado “Vigiladas, Multilaterales y Universidades" 
- El resto de tipos de tabla existentes y vigentes debe conservar su definición actual.    **Control de Acceso** 
- Este cambio solo debe estar disponible para usuarios con el perfil administrador del módulo de Clientes SARLAFT. 
- Perfiles diferentes al administrador no deben ver ni modificar este catálogo.

## Criterios de Aceptación

**1. Actualización del catálogo de “Tipo de tabla”** 
- **CA-1.1**: El sistema debe reemplazar los valores actuales **“Financieras”, “Aseguradoras” y “FP”** por los nuevos valores:

- Vigiladas, Multilaterales y Universidades   
- **CA-1.2**: El resto de opciones del catálogo de “Tipo de tabla” debe permanecer sin cambios.    **2. Vista “Consultar” → Filtro “Tipo de tabla”** 
- **CA-2.1**: En el filtro *Tipo de tabla*, solo deben visualizarse los nombres actualizados. 
- **CA-2.2**: Si un usuario administrador selecciona alguno de los nuevos valores, la búsqueda debe traer únicamente los registros asociados a dicho tipo.    **3. Resultados de consulta** 
- **CA-3.1**: Al ejecutar una búsqueda, la columna **Tipo de tabla** en la cuadrícula de resultados debe mostrar exclusivamente los nombres actualizados:

- Vigiladas, Multilaterales y Universidades   
- **CA-3.2**: Los registros históricos con los antiguos valores deben mostrarse con los nuevos nombres, sin modificar IDs de las entidades matriculadas. 
- **CA-3.3**: El resto de columnas de la tabla deben visualizarse sin alteraciones ni cambios funcionales.    **4. Vista “Matricular” → Formulario de creación** 
- **CA-4.1**: En el formulario “Matricular”, el campo **Tipo de tabla** debe mostrar los valores actualizados. 
- **CA-4.2**: El usuario administrador debe poder matricular nuevas entidades seleccionando la nueva opción. 
- **CA-4.3**: Las demás opciones del catálogo deben continuar con su definición actual. 
- **CA-4.4**: Al guardar un registro matriculado con las nuevas opciones, este debe reflejarse correctamente en la vista de consulta.    **5. Consistencia en todas las vistas** 
- **CA-5.1**: No debe existir ningún lugar del módulo donde aparezcan los antiguos términos “Financieras”, “Aseguradoras” o “FP”.    **6. Control de acceso** 
- **CA-6.1**: Únicamente usuarios con perfil Administrador del módulo de Clientes SARLAFT deben poder:

- Ver estas opciones 
- Modificar registros 
- Matricular nuevas entidades   
- **CA-6.2:** Usuarios sin rol administrador:

- No deben visualizar la funcionalidad de editar o matricular. 
- Sí pueden visualizar los valores actualizados en consultas, si la política del módulo lo permite.
