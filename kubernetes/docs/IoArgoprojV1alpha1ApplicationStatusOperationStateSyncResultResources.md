# IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources

ResourceResult holds the operation result details of a specific resource
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Group specifies the API group of the resource | 
**hook_phase** | **str** | HookPhase contains the state of any operation associated with this resource OR hook This can also contain values for non-hook resources. | [optional] 
**hook_type** | **str** | HookType specifies the type of the hook. Empty for non-hook resources | [optional] 
**kind** | **str** | Kind specifies the API kind of the resource | 
**message** | **str** | Message contains an informational or error message for the last sync OR operation | [optional] 
**name** | **str** | Name specifies the name of the resource | 
**namespace** | **str** | Namespace specifies the target namespace of the resource | 
**status** | **str** | Status holds the final result of the sync. Will be empty if the resources is yet to be applied/pruned and is always zero-value for hooks | [optional] 
**sync_phase** | **str** | SyncPhase indicates the particular phase of the sync that this result was acquired in | [optional] 
**version** | **str** | Version specifies the API version of the resource | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


