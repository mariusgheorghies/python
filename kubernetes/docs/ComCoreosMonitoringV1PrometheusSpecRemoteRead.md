# ComCoreosMonitoringV1PrometheusSpecRemoteRead

RemoteReadSpec defines the remote_read configuration for prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**ComCoreosMonitoringV1PrometheusSpecAuthorization**](ComCoreosMonitoringV1PrometheusSpecAuthorization.md) |  | [optional] 
**basic_auth** | [**ComCoreosMonitoringV1PrometheusSpecBasicAuth**](ComCoreosMonitoringV1PrometheusSpecBasicAuth.md) |  | [optional] 
**bearer_token** | **str** | Bearer token for remote read. | [optional] 
**bearer_token_file** | **str** | File to read bearer token for remote read. | [optional] 
**headers** | **dict(str, str)** | Custom HTTP headers to be sent along with each remote read request. Be aware that headers that are set by Prometheus itself can&#39;t be overwritten. Only valid in Prometheus versions 2.26.0 and newer. | [optional] 
**name** | **str** | The name of the remote read queue, must be unique if specified. The name is used in metrics and logging in order to differentiate read configurations.  Only valid in Prometheus versions 2.15.0 and newer. | [optional] 
**oauth2** | [**ComCoreosMonitoringV1PodMonitorSpecOauth2**](ComCoreosMonitoringV1PodMonitorSpecOauth2.md) |  | [optional] 
**proxy_url** | **str** | Optional ProxyURL | [optional] 
**read_recent** | **bool** | Whether reads should be made for queries for time ranges that the local storage should have complete data for. | [optional] 
**remote_timeout** | **str** | Timeout for requests to the remote read endpoint. | [optional] 
**required_matchers** | **dict(str, str)** | An optional list of equality matchers which have to be present in a selector to query the remote read endpoint. | [optional] 
**tls_config** | [**ComCoreosMonitoringV1PrometheusSpecTlsConfig**](ComCoreosMonitoringV1PrometheusSpecTlsConfig.md) |  | [optional] 
**url** | **str** | The URL of the endpoint to send samples to. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


