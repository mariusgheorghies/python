# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs

WebhookConfig configures notifications via a generic receiver supporting the webhook payload. See https://prometheus.io/docs/alerting/latest/configuration/#webhook_config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig.md) |  | [optional] 
**max_alerts** | **int** | Maximum number of alerts to be sent per webhook message. When 0, all alerts are included. | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**url** | **str** | The URL to send HTTP POST requests to. &#x60;urlSecret&#x60; takes precedence over &#x60;url&#x60;. One of &#x60;urlSecret&#x60; and &#x60;url&#x60; should be defined. | [optional] 
**url_secret** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecUrlSecret**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecUrlSecret.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


