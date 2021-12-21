# ComCoreosMonitoringV1ServiceMonitorSpec

Specification of desired Service selection for target discovery by Prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**list[ComCoreosMonitoringV1ServiceMonitorSpecEndpoints]**](ComCoreosMonitoringV1ServiceMonitorSpecEndpoints.md) | A list of endpoints allowed as part of this ServiceMonitor. | 
**job_label** | **str** | Chooses the label of the Kubernetes &#x60;Endpoints&#x60;. Its value will be used for the &#x60;job&#x60;-label&#39;s value of the created metrics.   Default &amp; fallback value: the name of the respective Kubernetes &#x60;Endpoint&#x60;. | [optional] 
**label_limit** | **int** | Per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_name_length_limit** | **int** | Per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_value_length_limit** | **int** | Per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**namespace_selector** | [**ComCoreosMonitoringV1ServiceMonitorSpecNamespaceSelector**](ComCoreosMonitoringV1ServiceMonitorSpecNamespaceSelector.md) |  | [optional] 
**pod_target_labels** | **list[str]** | PodTargetLabels transfers labels on the Kubernetes &#x60;Pod&#x60; onto the created metrics. | [optional] 
**sample_limit** | **int** | SampleLimit defines per-scrape limit on number of scraped samples that will be accepted. | [optional] 
**selector** | [**ComCoreosMonitoringV1ServiceMonitorSpecSelector**](ComCoreosMonitoringV1ServiceMonitorSpecSelector.md) |  | 
**target_labels** | **list[str]** | TargetLabels transfers labels from the Kubernetes &#x60;Service&#x60; onto the created metrics. All labels set in &#x60;selector.matchLabels&#x60; are automatically transferred. | [optional] 
**target_limit** | **int** | TargetLimit defines a limit on the number of scraped targets that will be accepted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


