# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetrics

Metrics controls the metrics subsystem of the Agent and settings unique to metrics-specific pods that are deployed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitrary_fs_access_through_s_ms** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsArbitraryFSAccessThroughSMs**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsArbitraryFSAccessThroughSMs.md) |  | [optional] 
**enforced_namespace_label** | **str** | EnforcedNamespaceLabel enforces adding a namespace label of origin for each metric that is user-created. The label value is always the namespace of the object that is being created. | [optional] 
**enforced_sample_limit** | **int** | EnforcedSampleLimit defines a global limit on the number of scraped samples that are accepted. This overrides any SampleLimit set per ServiceMonitor and/or PodMonitor. It is meant to be used by admins to enforce the SampleLimit to keep the overall number of samples and series under the desired limit. Note that if a SampleLimit from a ServiceMonitor or PodMonitor is lower, that value is used instead. | [optional] 
**enforced_target_limit** | **int** | EnforcedTargetLimit defines a global limit on the number of scraped targets. This overrides any TargetLimit set per ServiceMonitor and/or PodMonitor. It is meant to be used by admins to enforce the TargetLimit to keep the overall number of targets under the desired limit. Note that if a TargetLimit from a ServiceMonitor or PodMonitor is higher, that value is used instead. | [optional] 
**external_labels** | **dict(str, str)** | ExternalLabels are labels to add to any time series when sending data over remote_write. | [optional] 
**ignore_namespace_selectors** | **bool** | IgnoreNamespaceSelectors, if true, ignores NamespaceSelector settings from the PodMonitor and ServiceMonitor configs, so that they only discover endpoints within their current namespace. | [optional] 
**instance_namespace_selector** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsInstanceNamespaceSelector**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsInstanceNamespaceSelector.md) |  | [optional] 
**instance_selector** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsInstanceSelector**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsInstanceSelector.md) |  | [optional] 
**metrics_external_label_name** | **str** | MetricsExternalLabelName is the name of the external label used to denote Grafana Agent cluster. Defaults to \&quot;cluster.\&quot; The external label is _not_ added when the value is set to the empty string. | [optional] 
**override_honor_labels** | **bool** | OverrideHonorLabels, if true, overrides all configured honor_labels read from ServiceMonitor or PodMonitor and sets them to false. | [optional] 
**override_honor_timestamps** | **bool** | OverrideHonorTimestamps allows global enforcement for honoring timestamps in all scrape configs. | [optional] 
**remote_write** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsRemoteWrite]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsRemoteWrite.md) | RemoteWrite controls default remote_write settings for all instances. If an instance does not provide its own RemoteWrite settings, these will be used instead. | [optional] 
**replica_external_label_name** | **str** | ReplicaExternalLabelName is the name of the metrics external label used to denote the replica name. Defaults to __replica__. The external label is _not_ added when the value is set to the empty string. | [optional] 
**replicas** | **int** | Replicas of each shard to deploy for metrics pods. Number of replicas multiplied by the number of shards is the total number of pods created. | [optional] 
**scrape_interval** | **str** | ScrapeInterval is the time between consecutive scrapes. | [optional] 
**scrape_timeout** | **str** | ScrapeTimeout is the time to wait for a target to respond before marking a scrape as failed. | [optional] 
**shards** | **int** | Shards to distribute targets onto. Number of replicas multiplied by the number of shards is the total number of pods created. Note that scaling down shards does not reshard data onto remaining instances; it must be manually moved. Increasing shards does not reshard data either, but it will continue to be available from the same instances. Sharding is performed on the content of the __address__ target meta-label. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


