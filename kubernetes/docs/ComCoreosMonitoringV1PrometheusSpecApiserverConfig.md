# ComCoreosMonitoringV1PrometheusSpecApiserverConfig

APIServerConfig allows specifying a host and auth methods to access apiserver. If left empty, Prometheus is assumed to run inside of the cluster and will discover API servers automatically and use the pod's CA certificate and bearer token file at /var/run/secrets/kubernetes.io/serviceaccount/.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**ComCoreosMonitoringV1PrometheusSpecApiserverConfigAuthorization**](ComCoreosMonitoringV1PrometheusSpecApiserverConfigAuthorization.md) |  | [optional] 
**basic_auth** | [**ComCoreosMonitoringV1PrometheusSpecApiserverConfigBasicAuth**](ComCoreosMonitoringV1PrometheusSpecApiserverConfigBasicAuth.md) |  | [optional] 
**bearer_token** | **str** | Bearer token for accessing apiserver. | [optional] 
**bearer_token_file** | **str** | File to read bearer token for accessing apiserver. | [optional] 
**host** | **str** | Host of apiserver. A valid string consisting of a hostname or IP followed by an optional port number | 
**tls_config** | [**ComCoreosMonitoringV1PrometheusSpecApiserverConfigTlsConfig**](ComCoreosMonitoringV1PrometheusSpecApiserverConfigTlsConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


