# ComCoreosMonitoringV1PodMonitorSpec

Specification of desired Pod selection for target discovery by Prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_metadata** | [**ComCoreosMonitoringV1PodMonitorSpecAttachMetadata**](ComCoreosMonitoringV1PodMonitorSpecAttachMetadata.md) |  | [optional] 
**job_label** | **str** | The label to use to retrieve the job name from. | [optional] 
**label_limit** | **int** | Per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_name_length_limit** | **int** | Per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_value_length_limit** | **int** | Per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**namespace_selector** | [**ComCoreosMonitoringV1PodMonitorSpecNamespaceSelector**](ComCoreosMonitoringV1PodMonitorSpecNamespaceSelector.md) |  | [optional] 
**pod_metrics_endpoints** | [**list[ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints]**](ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints.md) | A list of endpoints allowed as part of this PodMonitor. | 
**pod_target_labels** | **list[str]** | PodTargetLabels transfers labels on the Kubernetes Pod onto the target. | [optional] 
**sample_limit** | **int** | SampleLimit defines per-scrape limit on number of scraped samples that will be accepted. | [optional] 
**selector** | [**ComCoreosMonitoringV1PodMonitorSpecSelector**](ComCoreosMonitoringV1PodMonitorSpecSelector.md) |  | 
**target_limit** | **int** | TargetLimit defines a limit on the number of scraped targets that will be accepted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


