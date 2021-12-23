# IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategyRollingUpdate

Rolling update config params. Present only if RolloutStrategyType = RollingUpdate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_surge** | [**object**](.md) | The maximum number of control planes that can be scheduled above or under the desired number of control planes. Value can be an absolute number 1 or 0. Defaults to 1. Example: when this is set to 1, the control plane can be scaled up immediately when the rolling update starts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


