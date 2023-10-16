# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpec

AlertmanagerConfigSpec is a specification of the desired behavior of the Alertmanager configuration. By definition, the Alertmanager configuration only applies to alerts for which the `namespace` label is equal to the namespace of the AlertmanagerConfig resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inhibit_rules** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecInhibitRules]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecInhibitRules.md) | List of inhibition rules. The rules will only apply to alerts matching the resource’s namespace. | [optional] 
**mute_time_intervals** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecMuteTimeIntervals]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecMuteTimeIntervals.md) | List of MuteTimeInterval specifying when the routes should be muted. | [optional] 
**receivers** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecReceivers]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecReceivers.md) | List of receivers. | [optional] 
**route** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoute**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoute.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


