# Instalación del Agente Dynatrace en AKS Sarlaft

> **Fuente Confluence:** [Instalación del Agente Dynatrace en AKS Sarlaft](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/2388918331/Instalaci+n+del+Agente+Dynatrace+en+AKS+Sarlaft)
> **Última modificación:** 2021-09-20 — Jhon Edison Mesa Bedoya · versión 4
> **Sección:** [Configuración Plataforma Base Sarlaft](./index.md)

Basado en: [https://www.dynatrace.com/support/help/setup-and-configuration/setup-on-container-platforms/kubernetes/deploy-oneagent-on-kubernetes-for-application-only-monitoring/#tabgroup-annotations--namespace-annotations](https://www.dynatrace.com/support/help/setup-and-configuration/setup-on-container-platforms/kubernetes/deploy-oneagent-on-kubernetes-for-application-only-monitoring/#tabgroup-annotations--namespace-annotations)

1. **LABORATORIO AKS**

   **PREREQUISTOS:**

   a. Abrir una consola de windows y conectarse al AKS a modificar asi:

   *az account set --subscription f6278fb3-d372-470e-b355-70025248eb80*

   *az aks get-credentials --resource-group rg-sarlaft-lab-001 --name aks-sarlaft*

Pasos seguidos para desplegar el agente en el AKS:

a. Crear el namespace de Dynatrace: `kubectl create namespace dynatrace`

b. Instalar el Agente OneAgent:

`kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml`

nota: Para verificar que este tomando logs, ejecutar:

`kubectl -n dynatrace logs -f deployment/dynatrace-oneagent-operator`

c. Adicionar el Token para logueo en las cuentas de Dynatrace en Sura. Cambiar PAAS_TOKEN por el token asignado en el equipo de Monitoreo

`kubectl -n dynatrace create secret generic oneagent --from-literal="paasToken=PAAS_TOKEN"`

d. Marcar el namespaace de sarlaft (nombre=default) para envío de logs a Dynatrace

`kubectl label namespace default oneagent.dynatrace.com/instance=oneagentapm`

e. Anotar namespace de sarlaft (nombre=default) para inyectar el agente en los contenedores asociados en el namespace

`kubectl annotate namespace default oneagent.dynatrace.com/inject=true`

f. Activar el logueo a Dynatrace laboratorio Sura por medio del archivo de configuración

`kubectl apply -f cr-apm-sarlaft-lab.yaml`

[cr-apm-sarlaft-lab.yaml](./attachments/cr-apm-sarlaft-lab.yaml)

**2. PRODUCCIÓN AKS**

**PREREQUISTOS:**

a. Abrir una consola de windows y conectarse al AKS a modificar asi:

*az account set --subscription ddd54223-6562-4c9f-ad31-92a04e786760*

*az aks get-credentials --resource-group rg-sarlaft-pdn-001 --name aks-sarlaft*

Pasos seguidos para desplegar el agente en el AKS:

a. Crear el namespace de Dynatrace: `kubectl create namespace dynatrace`

b. Instalar el Agente OneAgent:

`kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml`

nota: Para verificar que este tomando logs, ejecutar:

`kubectl -n dynatrace logs -f deployment/dynatrace-oneagent-operator`

c. Adicionar el Token para logueo en las cuentas de Dynatrace en Sura. Cambiar PAAS_TOKEN por el token asignado en el equipo de Monitoreo

`kubectl -n dynatrace create secret generic oneagent --from-literal="paasToken=PAAS_TOKEN"`

d. Marcar el namespaace de sarlaft (nombre=default) para envío de logs a Dynatrace

`kubectl label namespace default oneagent.dynatrace.com/instance=oneagentapm`

e. Anotar namespace de sarlaft (nombre=default) para inyectar el agente en los contenedores asociados en el namespace

`kubectl annotate namespace default oneagent.dynatrace.com/inject=true`

f. Activar el logueo a Dynatrace laboratorio Sura por medio del archivo de configuración

`kubectl apply -f cr-apm-sarlaft-pdn.yaml`

[cr-apm-sarlaft-pdn.yaml](./attachments/cr-apm-sarlaft-pdn.yaml)
