# ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers

AlertmanagerEndpoints defines a selection of a single Endpoints object containing alertmanager IPs to fire alerts against.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Version of the Alertmanager API that Prometheus uses to send alerts. It can be \&quot;v1\&quot; or \&quot;v2\&quot;. | [optional] 
**authorization** | [**ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization**](ComCoreosMonitoringV1PrometheusSpecAlertingAuthorization.md) |  | [optional] 
**bearer_token_file** | **str** | BearerTokenFile to read from filesystem to use when authenticating to Alertmanager. | [optional] 
**name** | **str** | Name of Endpoints object in Namespace. | 
**namespace** | **str** | Namespace of Endpoints object. | 
**path_prefix** | **str** | Prefix for the HTTP path alerts are pushed to. | [optional] 
**port** | [**object**](.md) | Port the Alertmanager API is exposed on. | 
**scheme** | **str** | Scheme to use when firing alerts. | [optional] 
**timeout** | **str** | Timeout is a per-target Alertmanager timeout when pushing alerts. | [optional] 
**tls_config** | [**ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfig**](ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


