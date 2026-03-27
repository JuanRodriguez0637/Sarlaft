# Configuración Infraestructura

Proceso para crear infraestructura en AZURE
Sarlaft CS

- Solicitud de cuentas Azure.

- Una vez se halla definido el centro de costos, cotización mensual y líder de TI responsable de la infraestructura se procede a crear un catálogo por cada ambiente para la solicitud de la cuenta en Azure.

Ingresamos a:  Servicios de TI >> Nube

Llenamos los datos solicitados:

Seleccionamos el ambiente, Esto lo debemos hacer por catálogos separados.

- Creación de Repositorios para infraestructura como código.
Debido a que la configuración de la infraestructura se hace mediante IaC (Infrastructure as code) se deben crear los repositorios donde se encontraran las fuentes asociada a la configuración de Azure usando Terraform.
Para crear estos repositorios en Azure se deben seguir los estándares de nombramiento definimos. Ejemplo:

Ver:
Una vez nos entreguen el repositorio se deben crear los diferentes feature correspondiente los ambientes de Desarrollo, Laboratorio y Producción:

- Uso del Lego para creación de infraestructura con Terraform
- Descargarse la última versión del Lego
https://artifactory.suramericana.com.co/ui/repos/tree/General/sura-share%2Fsura%2Flnf%2Flegoapp
- Descargar e instalar AzureCli 64Bits
- Descargar Terraform 64Bits y configurar variable de entorno a la carpeta donde se encuentra el .EXE.
- Se recomienda descargar la versión 0.13.7
- https://releases.hashicorp.com/terraform/0.13.7/
- ya que versiones mas recientes presentan problemas con algunas funciones en la configuración del proyecto de tarraform principal.
- Seguir los pasos descritos en:
https://segurosti.atlassian.net/wiki/spaces/AR/pages/799015790/Infraestructura+como+c+digo+en+Azure
- Montar cada código fuente generado por el lego en las diferentes ramas del repositorio -iac del paso 1. Toca ejecutar el generador por cada ambiente.

El Lego generara una carpeta llamada terraform y otra kubernetes. Se deben tomar todos los archivos de la carpeta terraform y subir al repo -iac correspondiente.

- Solicitud de Direccionamiento de IP para la nube.
- Ingresamos a la siguiente URL: 
https://appadminip.suramericana.com.co

- Seleccionamos la opción Direccionamiento IP para la nube.

- Llenamos el formulario de solicitud y le damos crear.

- Este proceso se debe realizar por cada ambiente.

- Validamos la creación de la IP.

- En caso de que falle la creación de la IP, se recomienda validar en la opción de consulta

- Consultamos las IPs creadas

- Modificar IP en Terraform.
- Consultamos la IP creada en el punto 4 de acuerdo con el Ambiente a configurar.

- Registro de IP en archivo de terraform.
Abrimos el archivo **terraform.tfvars**** **de la carpeta 00-globals. Cambiamos el campo por la nueva IP + “/24”.

Adicional se debe agregar **C****entro de costos y ****A****mbiente**.
Desarrollo = **dllo**
Laboratorio= **lab**
Producción= **pdb**

- Agregar subscription_id a los diferentes pasos en terraform.
Ya que un usuario puede tener acceso a varias subscripciones es importante que se diferencien las configuraciones en terraform para evitar sobreescribir estas en una infraestructura no deseada.
Se debe modificar todos los archivos **main.tf** exceptuando el que esta en **00-globals.**

Se debe adicionar la suscripción de la siguiente forma:

Este número de suscripción lo podemos encontrar en las propiedades de la cuenta:

- Definimos como privados los servicios expuestos en el Apigateway
Adicionando la línea:       *private-is-main    = true*
En el modulo **agw** del archivo **main.tf **que se encuentra en la carpeta de **04-ephemeral-aks**

- Subimos la infraestructura a Azure usando Terraform.

Adicionar versión de kubernetes.
kubernetes-version-prefix           = "1.20"

Solicitar creación de conexión express Router.
Esto se realiza por cada ambiente
https://suramericana.sharepoint.com/sites/INGENIERIATELCO/Lists/Conectividad%20a%20Nubes/AllItems.aspx

Luego de que ejecuten la solicitud deberíamos poder ver:

Solicitar los dns del front y back para el application gateway (DNS interno) y el content netwok delivery (dns externo).
Por catalogo accedemos a Conectividad y colaboración:

Una vez nos creen el DNS debemos registrarlo en el ApiGateway de la siguiente manera:

Luego que este creado:
Validar:

Activar DNS :

Error tamaño:
En caso de Estar generando mal el custom domain podría salir este error:

Solución temporal, Disminuir el tamaño de los nombre.
