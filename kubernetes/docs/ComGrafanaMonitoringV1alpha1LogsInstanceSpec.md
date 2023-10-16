# ComGrafanaMonitoringV1alpha1LogsInstanceSpec

Spec holds the specification of the desired behavior for the logs instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_scrape_configs** | [**ComGrafanaMonitoringV1alpha1LogsInstanceSpecAdditionalScrapeConfigs**](ComGrafanaMonitoringV1alpha1LogsInstanceSpecAdditionalScrapeConfigs.md) |  | [optional] 
**kubernetes.clients** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsClients]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsClients.md) | Clients controls where logs are written to for this instance. | [optional] 
**pod_logs_namespace_selector** | [**ComGrafanaMonitoringV1alpha1LogsInstanceSpecPodLogsNamespaceSelector**](ComGrafanaMonitoringV1alpha1LogsInstanceSpecPodLogsNamespaceSelector.md) |  | [optional] 
**pod_logs_selector** | [**ComGrafanaMonitoringV1alpha1LogsInstanceSpecPodLogsSelector**](ComGrafanaMonitoringV1alpha1LogsInstanceSpecPodLogsSelector.md) |  | [optional] 
**target_config** | [**ComGrafanaMonitoringV1alpha1LogsInstanceSpecTargetConfig**](ComGrafanaMonitoringV1alpha1LogsInstanceSpecTargetConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


