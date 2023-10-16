# IoArgoprojV1alpha1ApplicationSpecSyncPolicyAutomated

Automated will keep an application synced to the target revision
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_empty** | **bool** | AllowEmpty allows apps have zero live resources (default: false) | [optional] 
**prune** | **bool** | Prune specifies whether to delete resources from the cluster that are not found in the sources anymore as part of automated sync (default: false) | [optional] 
**self_heal** | **bool** | SelfHeal specifes whether to revert resources back to their desired state upon modification in the cluster (default: false) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


