# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes

HostPathMount contains elements describing volumes that are mounted from the host.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_path** | **str** | HostPath is the path in the host that will be mounted inside the pod. | 
**mount_path** | **str** | MountPath is the path inside the pod where hostPath will be mounted. | 
**name** | **str** | Name of the volume inside the pod template. | 
**path_type** | **str** | PathType is the type of the HostPath. | [optional] 
**read_only** | **bool** | ReadOnly controls write access to the volume | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


