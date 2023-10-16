# ComCoreosMonitoringV1ProbeSpecTargetsIngress

ingress defines the Ingress objects to probe and the relabeling configuration. If `staticConfig` is also defined, `staticConfig` takes precedence.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_selector** | [**ComCoreosMonitoringV1ProbeSpecTargetsIngressNamespaceSelector**](ComCoreosMonitoringV1ProbeSpecTargetsIngressNamespaceSelector.md) |  | [optional] 
**relabeling_configs** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | RelabelConfigs to apply to the label set of the target before it gets scraped. The original ingress address is available via the &#x60;__tmp_prometheus_ingress_address&#x60; label. It can be used to customize the probed URL. The original scrape job&#39;s name is available via the &#x60;__tmp_prometheus_job_name&#x60; label. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config | [optional] 
**selector** | [**ComCoreosMonitoringV1ProbeSpecTargetsIngressSelector**](ComCoreosMonitoringV1ProbeSpecTargetsIngressSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


