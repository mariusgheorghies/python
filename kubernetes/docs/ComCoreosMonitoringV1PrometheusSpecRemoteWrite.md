# ComCoreosMonitoringV1PrometheusSpecRemoteWrite

RemoteWriteSpec defines the remote_write configuration for prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**ComCoreosMonitoringV1PrometheusSpecAuthorization1**](ComCoreosMonitoringV1PrometheusSpecAuthorization1.md) |  | [optional] 
**basic_auth** | [**ComCoreosMonitoringV1PrometheusSpecBasicAuth**](ComCoreosMonitoringV1PrometheusSpecBasicAuth.md) |  | [optional] 
**bearer_token** | **str** | Bearer token for remote write. | [optional] 
**bearer_token_file** | **str** | File to read bearer token for remote write. | [optional] 
**headers** | **dict(str, str)** | Custom HTTP headers to be sent along with each remote write request. Be aware that headers that are set by Prometheus itself can&#39;t be overwritten. Only valid in Prometheus versions 2.25.0 and newer. | [optional] 
**metadata_config** | [**ComCoreosMonitoringV1PrometheusSpecMetadataConfig**](ComCoreosMonitoringV1PrometheusSpecMetadataConfig.md) |  | [optional] 
**name** | **str** | The name of the remote write queue, must be unique if specified. The name is used in metrics and logging in order to differentiate queues. Only valid in Prometheus versions 2.15.0 and newer. | [optional] 
**oauth2** | [**ComCoreosMonitoringV1PodMonitorSpecOauth2**](ComCoreosMonitoringV1PodMonitorSpecOauth2.md) |  | [optional] 
**proxy_url** | **str** | Optional ProxyURL | [optional] 
**queue_config** | [**ComCoreosMonitoringV1PrometheusSpecQueueConfig**](ComCoreosMonitoringV1PrometheusSpecQueueConfig.md) |  | [optional] 
**remote_timeout** | **str** | Timeout for requests to the remote write endpoint. | [optional] 
**send_exemplars** | **bool** | Enables sending of exemplars over remote write. Note that exemplar-storage itself must be enabled using the enableFeature option for exemplars to be scraped in the first place.  Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**tls_config** | [**ComCoreosMonitoringV1PrometheusSpecTlsConfig1**](ComCoreosMonitoringV1PrometheusSpecTlsConfig1.md) |  | [optional] 
**url** | **str** | The URL of the endpoint to send samples to. | 
**write_relabel_configs** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | The list of remote write relabel configurations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


