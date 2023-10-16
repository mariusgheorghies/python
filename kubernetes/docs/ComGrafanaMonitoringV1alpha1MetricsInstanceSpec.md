# ComGrafanaMonitoringV1alpha1MetricsInstanceSpec

Spec holds the specification of the desired behavior for the Metrics instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_scrape_configs** | [**ComGrafanaMonitoringV1alpha1MetricsInstanceSpecAdditionalScrapeConfigs**](ComGrafanaMonitoringV1alpha1MetricsInstanceSpecAdditionalScrapeConfigs.md) |  | [optional] 
**max_wal_time** | **str** | MaxWALTime is the maximum amount of time that series and samples can exist in the WAL before being forcibly deleted. | [optional] 
**min_wal_time** | **str** | MinWALTime is the minimum amount of time that series and samples can exist in the WAL before being considered for deletion. | [optional] 
**pod_monitor_namespace_selector** | [**ComGrafanaMonitoringV1alpha1MetricsInstanceSpecPodMonitorNamespaceSelector**](ComGrafanaMonitoringV1alpha1MetricsInstanceSpecPodMonitorNamespaceSelector.md) |  | [optional] 
**pod_monitor_selector** | [**ComGrafanaMonitoringV1alpha1MetricsInstanceSpecPodMonitorSelector**](ComGrafanaMonitoringV1alpha1MetricsInstanceSpecPodMonitorSelector.md) |  | [optional] 
**probe_namespace_selector** | [**ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector**](ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector.md) |  | [optional] 
**probe_selector** | [**ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeSelector**](ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeSelector.md) |  | [optional] 
**remote_flush_deadline** | **str** | RemoteFlushDeadline is the deadline for flushing data when an instance shuts down. | [optional] 
**remote_write** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsRemoteWrite]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsRemoteWrite.md) | RemoteWrite controls remote_write settings for this instance. | [optional] 
**service_monitor_namespace_selector** | [**ComGrafanaMonitoringV1alpha1MetricsInstanceSpecServiceMonitorNamespaceSelector**](ComGrafanaMonitoringV1alpha1MetricsInstanceSpecServiceMonitorNamespaceSelector.md) |  | [optional] 
**service_monitor_selector** | [**ComGrafanaMonitoringV1alpha1MetricsInstanceSpecServiceMonitorSelector**](ComGrafanaMonitoringV1alpha1MetricsInstanceSpecServiceMonitorSelector.md) |  | [optional] 
**wal_truncate_frequency** | **str** | WALTruncateFrequency specifies how frequently to run the WAL truncation process. Higher values cause the WAL to increase and for old series to stay in the WAL longer, but reduces the chance of data loss when remote_write fails for longer than the given frequency. | [optional] 
**write_stale_on_shutdown** | **bool** | WriteStaleOnShutdown writes staleness markers on shutdown for all series. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


