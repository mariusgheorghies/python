# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs

EmailConfig configures notifications via Email.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_identity** | **str** | The identity to use for authentication. | [optional] 
**auth_password** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecAuthPassword**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecAuthPassword.md) |  | [optional] 
**auth_secret** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecAuthSecret**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecAuthSecret.md) |  | [optional] 
**auth_username** | **str** | The username to use for authentication. | [optional] 
**_from** | **str** | The sender address. | [optional] 
**headers** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders.md) | Further headers email header key/value pairs. Overrides any headers previously set by the notification implementation. | [optional] 
**hello** | **str** | The hostname to identify to the SMTP server. | [optional] 
**html** | **str** | The HTML body of the email notification. | [optional] 
**require_tls** | **bool** | The SMTP TLS requirement. Note that Go does not support unencrypted connections to remote SMTP endpoints. | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**smarthost** | **str** | The SMTP host through which emails are sent. | [optional] 
**text** | **str** | The text body of the email notification. | [optional] 
**tls_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecTlsConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecTlsConfig.md) |  | [optional] 
**to** | **str** | The email address to send notifications to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


