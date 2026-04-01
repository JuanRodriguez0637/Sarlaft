# Información de secretos

> **Fuente Confluence:** [Información de secretos](https://segurosti.atlassian.net/wiki/spaces/EPA/pages/4703420517/Informaci+n+de+secretos)  
> **Última modificación:** 2025-05-27 — Diana Muñoz · versión 2  
> **Sección:** [Información de secretos](./index.md)

Los siguientes corresponden a los secretos utilizados por todos los microservicios de Sarlaft 4.0

| Componente | Variable Pipeline | SecretoNombre | Microservicios |
| --- | --- | --- | --- |
| Service Bus - Connection String | var_tf_kv_servicebus_cnx | kv-secret-servicebus-cnx | Sarlaftapi, SarlaftWebhook,SarlaftEngine,SarlaftBackWeb, SarlaftBatch, Sarlaft Clientes ms, Catalogos, Batch MI, P8 MI, Webhook MI, Requisitos MI, Clientes MI, Clientes PJ MI, Clientes PN MI, Identity, CCM MI, PEPS MI, Asesores MI, Identityvalidators MS |
| Base de Datos Sarlaft - Password -   username: "modsarlaftp" | var_tf_kv_bdsarlaft_transaccional_pwd | kv-secret-bdsarlaft-transaccional-pwd | Sarlaftapi, SarlaftWebhook,SarlaftEngine,SarlaftBackWeb,SarlaftBatch, Sarlaft Clientes ms, Webhook MII, Clientes PJ MI, CCM MI |
| Usuario Nombrado - Password - Usuario appsarlaft | var_tf_kv_usrsarlaft_pwd | kv-secret-usrsarlaft-pwd | Sarlaftapi, ,SarlaftBatch, P8 MI, Clientes MI,Clientes PN MI, Identity, PEPS MI, Asesores MI |
| Cache Redis - Password | var_tf_kv_cache_redis_pwd | kv-secret-cache-redis-pwd | Sarlaftapi, SarlaftWebhook,SarlaftEngine,SarlaftBackWeb, P8 MI, Webhook MI,  Clientes MI, Clientes PN MI, Asesores MI |
| Base de Datos Sarlaft - Password -  username: "modsarlaftdl" | var_tf_kv_bdsarlaft_lectura_pwd | kv-secret-bdsarlaft-lectura-pwd | SarlaftBackWeb |
| Secreto Token JWT | var_tf_kv_backweb_jwt_secret | kv-secret-backweb-jwt-secret | SarlaftBackWeb |
| RabbitMQ - Password - seguros.sarlaftmsv.usr | var_tf_kv_rabbitmq_sarlaftmsvusr_pwd | kv-secret-rabbitmq-sarlaftmsvusr-pwd | Batch MI |
| RabbitMQ - Password - seguros.sarlaftwebhook.usr | var_tf_kv_rabbitmq_sarlaftwebhook_pwd | kv-secret-rabbitmq-sarlaftwebhook-pwd | Webhook MI |
| Secret JWT - Rest | var_tf_kv_webhookmi_jwt_secret | kv-secret-webhookmi-jwt-secret | Webhook MI |
| Salesforce - Password - usuario - consultaclientes@sura.com.co | var_tf_kv_salesforce_pwd | kv-secret-salesforce-pwd | Clientes MI |
| Salesforce - clave cliente | var_tf_kv_salesforce_clave | kv-secret-salesforce-clave | Clientes MI |
| Informa colombia - key | var_tf_kv_infocolombia_key | kv-secret-infocolombia-key | Clientes PJ MI |
| Base de Datos Oracle PDN - Password - Usuario - MODSARLAFT | var_tf_kv_oracleusr_pwd | kv-secret-oracleusr-pwd | Clientes PN MI |
| RabbitMQ - Password - seguros.sarlaftidentity.usr | var_tf_kv_rabbitmq_sarlaftidentity_pwd | kv-secret-rabbitmq-sarlaftidentity-pwd | Identity |
| RabbitMQ - Password - ssarlaft4.ccm.usr | var_tf_kv_rabbitmq_sarlaftccm_pwd | kv-secret-rabbitmq-sarlaftccm-pwd | CCM MI |
| RabbitMQ - Password - seguros.sarlaftpeps.usr | var_tf_kv_rabbitmq_sarlaftpeps_pwd | kv-secret-rabbitmq-sarlaftpeps-pwd | PEPS MI |
| Base de Datos Vinculaciones - Password - Usuario  consarlaft | var_tf_kv_bdvinculaciones_pwd | kv-secret-bdvinculaciones-pwd | Asesores MI |
| Storage Account - String conexión- stsarlaftiactemppdn | var_tf_kv_straccounttemp_cnx | kv-secret-straccounttemp-cnx | P8 MI, Identityvalidators MS, sarlaftapi |
| RabbitMQ - Password - seguros.identityvalidator.usr | var_tf_kv_rabbitmq_identityvalidator_pwd | kv-secret-rabbitmq-identityvalidator-pwd | Identityvalidators MS |
| Validador - KeyStore - password | var_tf_kv_validador_keystore_pwd | kv-secret-validador-keystore-pwd | Identityvalidators MS |
| Validador - JWT - secret | var_tf_kv_validador_jwt_secret | kv-secret-validador-jwt-secret | Identityvalidators MS |
| Validador - Experian - Registraduria - Okta | var_tf_kv_validador_regokta_pwd | kv-secret-validador-regokta-pwd | Identityvalidators MS |
| Validador - Experian - Registraduria - Service user | var_tf_kv_validador_reg_usr | kv-secret-validador-reg-usr | Identityvalidators MS |
| Validador - Experian - Migracion - password token | var_tf_kv_validador_migra_pwd | kv-secret-validador-migra-pwd | Identityvalidators MS |
| Validador - Experian - Migracion - client secret | var_tf_kv_validador_migracliente_secret | kv-secret-validador-migracliente-secret | Identityvalidators MS |
| Validador - Experian - Profile - password Okta | var_tf_kv_validador_profokta_pwd | kv-secret-validador-profokta-pwd | Identityvalidators MS |
| Validador - Experian - Profile - service password | var_tf_kv_validador_profokta_secret | kv-secret-validador-profokta-secret | Identityvalidators MS |
| Validador - Experian - Identidad - clientSecret | var_tf_kv_validador_ident_secret | kv-secret-validador-ident-secret | Identityvalidators MS |
| Validador - Experian - Identidad - authorizationHeader | var_tf_kv_validador_ident_header | kv-secret-validador-ident-header | Identityvalidators MS |
| Validador - Experian - Identidad - password | var_tf_kv_validador_ident_pwd | kv-secret-validador-ident-pwd | Identityvalidators MS |

Guia base: [Gestión de secretos en la nube](/wiki/spaces/AR/pages/2974187588/Gesti+n+de+secretos+o+valores+sensibles+en+la+nube)