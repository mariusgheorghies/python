# IoXK8sClusterV1alpha4MachineSpecBootstrap

Bootstrap is a reference to a local struct which encapsulates fields to configure the Machine’s bootstrapping mechanism.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_ref** | [**IoXK8sClusterV1alpha4MachineSpecBootstrapConfigRef**](IoXK8sClusterV1alpha4MachineSpecBootstrapConfigRef.md) |  | [optional] 
**data_secret_name** | **str** | DataSecretName is the name of the secret that stores the bootstrap data script. If nil, the Machine should remain in the Pending state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


