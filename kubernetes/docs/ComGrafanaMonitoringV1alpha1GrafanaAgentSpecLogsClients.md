# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsClients

LogsClientSpec defines the kubernetes.client integration for logs, indicating which Loki server to send logs to.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backoff_config** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBackoffConfig**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBackoffConfig.md) |  | [optional] 
**basic_auth** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth.md) |  | [optional] 
**batch_size** | **int** | Maximum batch size (in bytes) of logs to accumulate before sending the batch to Loki. | [optional] 
**batch_wait** | **str** | Maximum amount of time to wait before sending a batch, even if that batch isn&#39;t full. | [optional] 
**bearer_token** | **str** | BearerToken used for remote_write. | [optional] 
**bearer_token_file** | **str** | BearerTokenFile used to read bearer token. | [optional] 
**external_labels** | **dict(str, str)** | ExternalLabels are labels to add to any time series when sending data to Loki. | [optional] 
**oauth2** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsOauth2**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsOauth2.md) |  | [optional] 
**proxy_url** | **str** | ProxyURL to proxy requests through. Optional. | [optional] 
**tenant_id** | **str** | Tenant ID used by default to push logs to Loki. If omitted assumes remote Loki is running in single-tenant mode or an authentication layer is used to inject an X-Scope-OrgID header. | [optional] 
**timeout** | **str** | Maximum time to wait for a server to respond to a request. | [optional] 
**tls_config** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsTlsConfig**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsTlsConfig.md) |  | [optional] 
**url** | **str** | URL is the URL where Loki is listening. Must be a full HTTP URL, including protocol. Required. Example: https://logs-prod-us-central1.grafana.net/loki/api/v1/push. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


