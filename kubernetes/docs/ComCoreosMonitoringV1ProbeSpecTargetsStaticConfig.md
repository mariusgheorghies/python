# ComCoreosMonitoringV1ProbeSpecTargetsStaticConfig

staticConfig defines the static list of targets to probe and the relabeling configuration. If `ingress` is also defined, `staticConfig` takes precedence. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **dict(str, str)** | Labels assigned to all metrics scraped from the targets. | [optional] 
**relabeling_configs** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | RelabelConfigs to apply to the label set of the targets before it gets scraped. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config | [optional] 
**static** | **list[str]** | The list of hosts to probe. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


