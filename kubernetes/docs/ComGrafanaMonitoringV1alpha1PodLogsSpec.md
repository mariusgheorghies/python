# ComGrafanaMonitoringV1alpha1PodLogsSpec

Spec holds the specification of the desired behavior for the PodLogs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_label** | **str** | The label to use to retrieve the job name from. | [optional] 
**namespace_selector** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecNamespaceSelector**](ComGrafanaMonitoringV1alpha1PodLogsSpecNamespaceSelector.md) |  | [optional] 
**pipeline_stages** | [**list[ComGrafanaMonitoringV1alpha1PodLogsSpecPipelineStages]**](ComGrafanaMonitoringV1alpha1PodLogsSpecPipelineStages.md) | Pipeline stages for this pod. Pipeline stages support transforming and filtering log lines. | [optional] 
**pod_target_labels** | **list[str]** | PodTargetLabels transfers labels on the Kubernetes Pod onto the target. | [optional] 
**relabelings** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | RelabelConfigs to apply to logs before delivering. Grafana Agent Operator automatically adds relabelings for a few standard Kubernetes fields and replaces original scrape job name with __tmp_logs_job_name.   More info: https://grafana.com/docs/loki/latest/kubernetes.clients/promtail/configuration/#relabel_configs | [optional] 
**selector** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecSelector**](ComGrafanaMonitoringV1alpha1PodLogsSpecSelector.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


