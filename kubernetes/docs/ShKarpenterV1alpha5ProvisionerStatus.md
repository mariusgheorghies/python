# ShKarpenterV1alpha5ProvisionerStatus

ProvisionerStatus defines the observed state of Provisioner
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[ShKarpenterV1alpha5ProvisionerStatusConditions]**](ShKarpenterV1alpha5ProvisionerStatusConditions.md) | Conditions is the set of conditions required for this provisioner to scale its target, and indicates whether or not those conditions are met. | [optional] 
**last_scale_time** | **datetime** | LastScaleTime is the last time the Provisioner scaled the number of nodes | [optional] 
**resources** | **dict(str, object)** | Resources is the list of resources that have been provisioned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


