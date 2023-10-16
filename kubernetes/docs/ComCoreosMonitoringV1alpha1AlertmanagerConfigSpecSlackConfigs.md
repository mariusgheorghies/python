# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs

SlackConfig configures notifications via Slack. See https://prometheus.io/docs/alerting/latest/configuration/#slack_config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecActions]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecActions.md) | A list of Slack actions that are sent with each notification. | [optional] 
**api_url** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiURL**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiURL.md) |  | [optional] 
**callback_id** | **str** |  | [optional] 
**channel** | **str** | The channel or user to send notifications to. | [optional] 
**color** | **str** |  | [optional] 
**fallback** | **str** |  | [optional] 
**fields** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecFields]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecFields.md) | A list of Slack fields that are sent with each notification. | [optional] 
**footer** | **str** |  | [optional] 
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig.md) |  | [optional] 
**icon_emoji** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**link_names** | **bool** |  | [optional] 
**mrkdwn_in** | **list[str]** |  | [optional] 
**pretext** | **str** |  | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**short_fields** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**thumb_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**title_link** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


