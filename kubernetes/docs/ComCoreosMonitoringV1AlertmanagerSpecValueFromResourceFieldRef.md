# ComCoreosMonitoringV1AlertmanagerSpecValueFromResourceFieldRef

Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** | Container name: required for volumes, optional for env vars | [optional] 
**divisor** | [**object**](.md) | Specifies the output format of the exposed resources, defaults to \&quot;1\&quot; | [optional] 
**resource** | **str** | Required: resource to select | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


