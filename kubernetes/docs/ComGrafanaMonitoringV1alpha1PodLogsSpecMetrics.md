# ComGrafanaMonitoringV1alpha1PodLogsSpecMetrics

MetricsStageSpec is an action stage that allows for defining and updating metrics based on data from the extracted map. Created metrics are not pushed to Loki or Prometheus and are instead exposed via the /metrics endpoint of the Grafana Agent pod. The Grafana Agent Operator should be configured with a MetricsInstance that discovers the logging DaemonSet to collect metrics created by this stage.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to take against the metric. Required.   Must be either \&quot;inc\&quot; or \&quot;add\&quot; for type: counter or type: histogram. When type: gauge, must be one of \&quot;set\&quot;, \&quot;inc\&quot;, \&quot;dec\&quot;, \&quot;add\&quot;, or \&quot;sub\&quot;.   \&quot;add\&quot;, \&quot;set\&quot;, or \&quot;sub\&quot; requires the extracted value to be convertible to a positive float. | 
**buckets** | **list[str]** | Buckets to create. Bucket values must be convertible to float64s. Extremely large or small numbers are subject to some loss of precision. Only valid for type: histogram. | [optional] 
**count_entry_bytes** | **bool** | If true all log line bytes are counted. Can only be set with matchAll: true and action: add.   Only valid for type: counter. | [optional] 
**description** | **str** | Sets the description for the created metric. | [optional] 
**match_all** | **bool** | If true, all log lines are counted without attempting to match the source to the extracted map. Mutually exclusive with value.   Only valid for type: counter. | [optional] 
**max_idle_duration** | **str** | Label values on metrics are dynamic which can cause exported metrics to go stale. To prevent unbounded cardinality, any metrics not updated within MaxIdleDuration are removed.   Must be greater or equal to 1s. Defaults to 5m. | [optional] 
**prefix** | **str** | Sets the custom prefix name for the metric. Defaults to \&quot;promtail_custom_\&quot;. | [optional] 
**source** | **str** | Key from the extracted data map to use for the metric. Defaults to the metrics name if not present. | [optional] 
**type** | **str** | The metric type to create. Must be one of counter, gauge, histogram. Required. | 
**value** | **str** | Filters down source data and only changes the metric if the targeted value matches the provided string exactly. If not present, all data matches. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


