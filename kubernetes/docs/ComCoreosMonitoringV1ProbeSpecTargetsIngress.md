# ComCoreosMonitoringV1ProbeSpecTargetsIngress

Ingress defines the set of dynamically discovered ingress objects which hosts are considered for probing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_selector** | [**ComCoreosMonitoringV1ProbeSpecTargetsIngressNamespaceSelector**](ComCoreosMonitoringV1ProbeSpecTargetsIngressNamespaceSelector.md) |  | [optional] 
**relabeling_configs** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | RelabelConfigs to apply to samples before ingestion. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config | [optional] 
**selector** | [**ComCoreosMonitoringV1ProbeSpecTargetsIngressSelector**](ComCoreosMonitoringV1ProbeSpecTargetsIngressSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


