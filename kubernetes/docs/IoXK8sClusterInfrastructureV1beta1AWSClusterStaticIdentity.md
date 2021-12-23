# IoXK8sClusterInfrastructureV1beta1AWSClusterStaticIdentity

AWSClusterStaticIdentity is the Schema for the awsclusterstaticidentities API It represents a reference to an AWS access key ID and secret access key, stored in a secret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMetaV2**](V1ObjectMetaV2.md) |  | [optional] 
**spec** | [**IoXK8sClusterInfrastructureV1alpha4AWSClusterStaticIdentitySpec**](IoXK8sClusterInfrastructureV1alpha4AWSClusterStaticIdentitySpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


