# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecPushoverConfigs

PushoverConfig configures notifications via Pushover. See https://prometheus.io/docs/alerting/latest/configuration/#pushover_config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire** | **str** | How long your notification will continue to be retried for, unless the user acknowledges the notification. | [optional] 
**html** | **bool** | Whether notification message is HTML or plain text. | [optional] 
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig.md) |  | [optional] 
**message** | **str** | Notification message. | [optional] 
**priority** | **str** | Priority, see https://pushover.net/api#priority | [optional] 
**retry** | **str** | How often the Pushover servers will send the same notification to the user. Must be at least 30 seconds. | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**sound** | **str** | The name of one of the sounds supported by device kubernetes.clients to override the user&#39;s default sound choice | [optional] 
**title** | **str** | Notification title. | [optional] 
**token** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecToken**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecToken.md) |  | [optional] 
**url** | **str** | A supplementary URL shown alongside the message. | [optional] 
**url_title** | **str** | A title for supplementary URL, otherwise just the URL is shown | [optional] 
**user_key** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecUserKey**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecUserKey.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


