# IoExternalSecretsV1alpha1PushSecretStatus

PushSecretStatus indicates the history of the status of PushSecret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoExternalSecretsV1alpha1PushSecretStatusConditions]**](IoExternalSecretsV1alpha1PushSecretStatusConditions.md) |  | [optional] 
**refresh_time** | [**object**](.md) | refreshTime is the time and date the external secret was fetched and the target secret updated | [optional] 
**synced_push_secrets** | **dict(str, dict(str, object))** | Synced Push Secrets for later deletion. Matches Secret Stores to PushSecretData that was stored to that secretStore. | [optional] 
**synced_resource_version** | **str** | SyncedResourceVersion keeps track of the last synced version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


