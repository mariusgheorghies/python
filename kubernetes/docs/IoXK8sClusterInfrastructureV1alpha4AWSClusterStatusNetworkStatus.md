# IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus

NetworkStatus encapsulates AWS networking resources.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server_elb** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElb**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElb.md) |  | [optional] 
**security_groups** | [**dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkSecurityGroups)**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkSecurityGroups.md) | SecurityGroups is a map from the role/kind of the security group to its unique name, if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


