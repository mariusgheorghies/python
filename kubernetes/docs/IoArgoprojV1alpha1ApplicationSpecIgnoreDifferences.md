# IoArgoprojV1alpha1ApplicationSpecIgnoreDifferences

ResourceIgnoreDifferences contains resource filter and list of json paths which should be ignored during comparison with live state.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | [optional] 
**jq_path_expressions** | **list[str]** |  | [optional] 
**json_pointers** | **list[str]** |  | [optional] 
**kind** | **str** |  | 
**managed_fields_managers** | **list[str]** | ManagedFieldsManagers is a list of trusted managers. Fields mutated by those managers will take precedence over the desired state defined in the SCM and won&#39;t be displayed in diffs | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


