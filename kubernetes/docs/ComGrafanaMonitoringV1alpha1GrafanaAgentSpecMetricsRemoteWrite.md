# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsRemoteWrite

RemoteWriteSpec defines the remote_write configuration for Prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**ComCoreosMonitoringV1PrometheusSpecBasicAuth**](ComCoreosMonitoringV1PrometheusSpecBasicAuth.md) |  | [optional] 
**bearer_token** | **str** | BearerToken used for remote_write. | [optional] 
**bearer_token_file** | **str** | BearerTokenFile used to read bearer token. | [optional] 
**headers** | **dict(str, str)** | Headers is a set of custom HTTP headers to be sent along with each remote_write request. Be aware that any headers set by Grafana Agent itself can&#39;t be overwritten. | [optional] 
**metadata_config** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsMetadataConfig**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsMetadataConfig.md) |  | [optional] 
**name** | **str** | Name of the remote_write queue. Must be unique if specified. The name is used in metrics and logging in order to differentiate queues. | [optional] 
**oauth2** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsOauth2**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsOauth2.md) |  | [optional] 
**proxy_url** | **str** | ProxyURL to proxy requests through. Optional. | [optional] 
**queue_config** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsQueueConfig**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsQueueConfig.md) |  | [optional] 
**remote_timeout** | **str** | RemoteTimeout is the timeout for requests to the remote_write endpoint. | [optional] 
**sigv4** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4.md) |  | [optional] 
**tls_config** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig.md) |  | [optional] 
**url** | **str** | URL of the endpoint to send samples to. | 
**write_relabel_configs** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | WriteRelabelConfigs holds relabel_configs to relabel samples before they are sent to the remote_write endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


