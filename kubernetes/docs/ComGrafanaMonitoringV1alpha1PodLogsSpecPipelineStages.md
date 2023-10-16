# ComGrafanaMonitoringV1alpha1PodLogsSpecPipelineStages

PipelineStageSpec defines an individual pipeline stage. Each stage type is mutually exclusive and no more than one may be set per stage.   More information on pipelines can be found in the Promtail documentation: https://grafana.com/docs/loki/latest/kubernetes.clients/promtail/pipelines/
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cri** | [**object**](.md) | CRI is a parsing stage that reads log lines using the standard CRI logging format. Supply cri: {} to enable. | [optional] 
**docker** | [**object**](.md) | Docker is a parsing stage that reads log lines using the standard Docker logging format. Supply docker: {} to enable. | [optional] 
**drop** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecDrop**](ComGrafanaMonitoringV1alpha1PodLogsSpecDrop.md) |  | [optional] 
**json** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecJson**](ComGrafanaMonitoringV1alpha1PodLogsSpecJson.md) |  | [optional] 
**label_allow** | **list[str]** | LabelAllow is an action stage that only allows the provided labels to be included in the label set that is sent to Loki with the log entry. | [optional] 
**label_drop** | **list[str]** | LabelDrop is an action stage that drops labels from the label set that is sent to Loki with the log entry. | [optional] 
**labels** | **dict(str, str)** | Labels is an action stage that takes data from the extracted map and modifies the label set that is sent to Loki with the log entry.   The key is REQUIRED and represents the name for the label that will be created. Value is optional and will be the name from extracted data to use for the value of the label. If the value is not provided, it defaults to match the key. | [optional] 
**limit** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecLimit**](ComGrafanaMonitoringV1alpha1PodLogsSpecLimit.md) |  | [optional] 
**match** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecMatch**](ComGrafanaMonitoringV1alpha1PodLogsSpecMatch.md) |  | [optional] 
**metrics** | [**dict(str, ComGrafanaMonitoringV1alpha1PodLogsSpecMetrics)**](ComGrafanaMonitoringV1alpha1PodLogsSpecMetrics.md) | Metrics is an action stage that supports defining and updating metrics based on data from the extracted map. Created metrics are not pushed to Loki or Prometheus and are instead exposed via the /metrics endpoint of the Grafana Agent pod. The Grafana Agent Operator should be configured with a MetricsInstance that discovers the logging DaemonSet to collect metrics created by this stage. | [optional] 
**multiline** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecMultiline**](ComGrafanaMonitoringV1alpha1PodLogsSpecMultiline.md) |  | [optional] 
**output** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecOutput**](ComGrafanaMonitoringV1alpha1PodLogsSpecOutput.md) |  | [optional] 
**pack** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecPack**](ComGrafanaMonitoringV1alpha1PodLogsSpecPack.md) |  | [optional] 
**regex** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecRegex**](ComGrafanaMonitoringV1alpha1PodLogsSpecRegex.md) |  | [optional] 
**replace** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecReplace**](ComGrafanaMonitoringV1alpha1PodLogsSpecReplace.md) |  | [optional] 
**template** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecTemplate**](ComGrafanaMonitoringV1alpha1PodLogsSpecTemplate.md) |  | [optional] 
**tenant** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecTenant**](ComGrafanaMonitoringV1alpha1PodLogsSpecTenant.md) |  | [optional] 
**timestamp** | [**ComGrafanaMonitoringV1alpha1PodLogsSpecTimestamp**](ComGrafanaMonitoringV1alpha1PodLogsSpecTimestamp.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


