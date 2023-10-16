# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecPagerdutyConfigs

PagerDutyConfig configures notifications via PagerDuty. See https://prometheus.io/docs/alerting/latest/configuration/#pagerduty_config
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | The class/type of the event. | [optional] 
**kubernetes.client** | **str** | Client identification. | [optional] 
**kubernetes.client_url** | **str** | Backlink to the sender of notification. | [optional] 
**component** | **str** | The part or component of the affected system that is broken. | [optional] 
**description** | **str** | Description of the incident. | [optional] 
**details** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHeaders.md) | Arbitrary key/value pairs that provide further detail about the incident. | [optional] 
**group** | **str** | A cluster or grouping of sources. | [optional] 
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig.md) |  | [optional] 
**pager_duty_image_configs** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecPagerDutyImageConfigs]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecPagerDutyImageConfigs.md) | A list of image details to attach that provide further detail about an incident. | [optional] 
**pager_duty_link_configs** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecPagerDutyLinkConfigs]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecPagerDutyLinkConfigs.md) | A list of link details to attach that provide further detail about an incident. | [optional] 
**routing_key** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoutingKey**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoutingKey.md) |  | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**service_key** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecServiceKey**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecServiceKey.md) |  | [optional] 
**severity** | **str** | Severity of the incident. | [optional] 
**url** | **str** | The URL to send requests to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


