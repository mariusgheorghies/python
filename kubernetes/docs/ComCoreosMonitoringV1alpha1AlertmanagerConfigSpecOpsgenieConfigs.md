# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecOpsgenieConfigs

OpsGenieConfig configures notifications via OpsGenie. See https://prometheus.io/docs/alerting/latest/configuration/#opsgenie_config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiKey**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiKey.md) |  | [optional] 
**api_url** | **str** | The URL to send OpsGenie API requests to. | [optional] 
**description** | **str** | Description of the incident. | [optional] 
**details** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders.md) | A set of arbitrary key/value pairs that provide further detail about the incident. | [optional] 
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig.md) |  | [optional] 
**message** | **str** | Alert text limited to 130 characters. | [optional] 
**note** | **str** | Additional alert note. | [optional] 
**priority** | **str** | Priority level of alert. Possible values are P1, P2, P3, P4, and P5. | [optional] 
**responders** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecResponders]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecResponders.md) | List of responders responsible for notifications. | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**source** | **str** | Backlink to the sender of the notification. | [optional] 
**tags** | **str** | Comma separated list of tags attached to the notifications. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


