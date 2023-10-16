# ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings

RelabelConfig allows dynamic rewriting of the label set, being applied to samples before ingestion. It defines `<metric_relabel_configs>`-section of Prometheus configuration. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to perform based on regex matching. Default is &#39;replace&#39;. uppercase and lowercase actions require Prometheus &gt;&#x3D; 2.36. | [optional] 
**modulus** | **int** | Modulus to take of the hash of the source label values. | [optional] 
**regex** | **str** | Regular expression against which the extracted value is matched. Default is &#39;(.*)&#39; | [optional] 
**replacement** | **str** | Replacement value against which a regex replace is performed if the regular expression matches. Regex capture groups are available. Default is &#39;$1&#39; | [optional] 
**separator** | **str** | Separator placed between concatenated source label values. default is &#39;;&#39;. | [optional] 
**source_labels** | **list[str]** | The source labels select values from existing labels. Their content is concatenated using the configured separator and matched against the configured regular expression for the replace, keep, and drop actions. | [optional] 
**target_label** | **str** | Label to which the resulting value is written in a replace action. It is mandatory for replace actions. Regex capture groups are available. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


