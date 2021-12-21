# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecVictoropsConfigs

VictorOpsConfig configures notifications via VictorOps. See https://prometheus.io/docs/alerting/latest/configuration/#victorops_config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiKey1**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiKey1.md) |  | [optional] 
**api_url** | **str** | The VictorOps API URL. | [optional] 
**custom_fields** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders.md) | Additional custom fields for notification. | [optional] 
**entity_display_name** | **str** | Contains summary of the alerted problem. | [optional] 
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig1**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig1.md) |  | [optional] 
**message_type** | **str** | Describes the behavior of the alert (CRITICAL, WARNING, INFO). | [optional] 
**monitoring_tool** | **str** | The monitoring tool the state message is from. | [optional] 
**routing_key** | **str** | A key used to map the alert to a team. | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**state_message** | **str** | Contains long explanation of the alerted problem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


