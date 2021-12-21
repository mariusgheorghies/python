# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecInhibitRules

InhibitRule defines an inhibition rule that allows to mute alerts when other alerts are already firing. See https://prometheus.io/docs/alerting/latest/configuration/#inhibit_rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equal** | **list[str]** | Labels that must have an equal value in the source and target alert for the inhibition to take effect. | [optional] 
**source_match** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch.md) | Matchers for which one or more alerts have to exist for the inhibition to take effect. The operator enforces that the alert matches the resource’s namespace. | [optional] 
**target_match** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch.md) | Matchers that have to be fulfilled in the alerts to be muted. The operator enforces that the alert matches the resource’s namespace. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


