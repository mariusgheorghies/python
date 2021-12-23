# ComCoreosMonitoringV1ProbeSpecTargetsStaticConfig

StaticConfig defines static targets which are considers for probing. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **dict(str, str)** | Labels assigned to all metrics scraped from the targets. | [optional] 
**relabeling_configs** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | RelabelConfigs to apply to samples before ingestion. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config | [optional] 
**static** | **list[str]** | Targets is a list of URLs to probe using the configured prober. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


