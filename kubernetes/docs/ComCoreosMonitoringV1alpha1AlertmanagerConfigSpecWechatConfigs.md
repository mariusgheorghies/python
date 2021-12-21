# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWechatConfigs

WeChatConfig configures notifications via WeChat. See https://prometheus.io/docs/alerting/latest/configuration/#wechat_config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | [optional] 
**api_secret** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiSecret**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecApiSecret.md) |  | [optional] 
**api_url** | **str** | The WeChat API URL. | [optional] 
**corp_id** | **str** | The corp id for authentication. | [optional] 
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig.md) |  | [optional] 
**message** | **str** | API request data as defined by the WeChat API. | [optional] 
**message_type** | **str** |  | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**to_party** | **str** |  | [optional] 
**to_tag** | **str** |  | [optional] 
**to_user** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


