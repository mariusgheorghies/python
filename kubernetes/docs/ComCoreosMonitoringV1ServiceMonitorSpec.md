# ComCoreosMonitoringV1ServiceMonitorSpec

Specification of desired Service selection for target discovery by Prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_metadata** | [**ComCoreosMonitoringV1ServiceMonitorSpecAttachMetadata**](ComCoreosMonitoringV1ServiceMonitorSpecAttachMetadata.md) |  | [optional] 
**endpoints** | [**list[ComCoreosMonitoringV1ServiceMonitorSpecEndpoints]**](ComCoreosMonitoringV1ServiceMonitorSpecEndpoints.md) | A list of endpoints allowed as part of this ServiceMonitor. | 
**job_label** | **str** | JobLabel selects the label from the associated Kubernetes service which will be used as the &#x60;job&#x60; label for all metrics.   For example: If in &#x60;ServiceMonitor.spec.jobLabel: foo&#x60; and in &#x60;Service.metadata.labels.foo: bar&#x60;, then the &#x60;job&#x3D;\&quot;bar\&quot;&#x60; label is added to all metrics.   If the value of this field is empty or if the label doesn&#39;t exist for the given Service, the &#x60;job&#x60; label of the metrics defaults to the name of the Kubernetes Service. | [optional] 
**label_limit** | **int** | Per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_name_length_limit** | **int** | Per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_value_length_limit** | **int** | Per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**namespace_selector** | [**ComCoreosMonitoringV1ServiceMonitorSpecNamespaceSelector**](ComCoreosMonitoringV1ServiceMonitorSpecNamespaceSelector.md) |  | [optional] 
**pod_target_labels** | **list[str]** | PodTargetLabels transfers labels on the Kubernetes &#x60;Pod&#x60; onto the created metrics. | [optional] 
**sample_limit** | **int** | SampleLimit defines per-scrape limit on number of scraped samples that will be accepted. | [optional] 
**selector** | [**ComCoreosMonitoringV1ServiceMonitorSpecSelector**](ComCoreosMonitoringV1ServiceMonitorSpecSelector.md) |  | 
**target_labels** | **list[str]** | TargetLabels transfers labels from the Kubernetes &#x60;Service&#x60; onto the created metrics. | [optional] 
**target_limit** | **int** | TargetLimit defines a limit on the number of scraped targets that will be accepted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


