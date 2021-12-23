# ComCoreosMonitoringV1PodMonitorSpecOauth2

OAuth2 for the URL. Only valid in Prometheus versions 2.27.0 and newer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.client_id** | [**ComCoreosMonitoringV1PodMonitorSpecOauth2ClientId**](ComCoreosMonitoringV1PodMonitorSpecOauth2ClientId.md) |  | 
**kubernetes.client_secret** | [**ComCoreosMonitoringV1PodMonitorSpecOauth2ClientSecret**](ComCoreosMonitoringV1PodMonitorSpecOauth2ClientSecret.md) |  | 
**endpoint_params** | **dict(str, str)** | Parameters to append to the token URL | [optional] 
**scopes** | **list[str]** | OAuth2 scopes used for the token request | [optional] 
**token_url** | **str** | The URL to fetch the token from | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


