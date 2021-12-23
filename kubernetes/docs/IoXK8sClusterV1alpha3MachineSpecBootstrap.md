# IoXK8sClusterV1alpha3MachineSpecBootstrap

Bootstrap is a reference to a local struct which encapsulates fields to configure the Machine’s bootstrapping mechanism.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_ref** | [**IoXK8sClusterV1alpha3MachineSpecBootstrapConfigRef**](IoXK8sClusterV1alpha3MachineSpecBootstrapConfigRef.md) |  | [optional] 
**data** | **str** | Data contains the bootstrap data, such as cloud-init details scripts. If nil, the Machine should remain in the Pending state.   Deprecated: Switch to DataSecretName. | [optional] 
**data_secret_name** | **str** | DataSecretName is the name of the secret that stores the bootstrap data script. If nil, the Machine should remain in the Pending state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


