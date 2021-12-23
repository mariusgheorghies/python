# IoXK8sClusterV1beta1MachinePool

MachinePool is the Schema for the machinepools API.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMetaV2**](V1ObjectMetaV2.md) |  | [optional] 
**spec** | [**IoXK8sClusterV1alpha4MachinePoolSpec**](IoXK8sClusterV1alpha4MachinePoolSpec.md) |  | [optional] 
**status** | [**IoXK8sClusterV1beta1MachinePoolStatus**](IoXK8sClusterV1beta1MachinePoolStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


