# IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess

RemoteAccess specifies how machines can be accessed remotely
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public** | **bool** | Public specifies whether to open port 22 to the public internet | [optional] 
**source_security_groups** | **list[str]** | SourceSecurityGroups specifies which security groups are allowed access | [optional] 
**ssh_key_name** | **str** | SSHKeyName specifies which EC2 SSH key can be used to access machines. If left empty, the key from the control plane is used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


