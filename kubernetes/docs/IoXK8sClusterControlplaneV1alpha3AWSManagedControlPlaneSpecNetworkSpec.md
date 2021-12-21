# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec

NetworkSpec encapsulates all things related to AWS network.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cni** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecCni**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecCni.md) |  | [optional] 
**security_group_overrides** | **dict(str, str)** | SecurityGroupOverrides is an optional set of security groups to use for cluster instances This is optional - if not provided new security groups will be created for the cluster | [optional] 
**subnets** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecSubnets]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecSubnets.md) | Subnets configuration. | [optional] 
**vpc** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecVpc**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecVpc.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


