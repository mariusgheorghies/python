# IoXK8sClusterInfrastructureV1beta1AWSClusterStatus

AWSClusterStatus defines the observed state of AWSCluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bastion** | [**IoXK8sClusterInfrastructureV1beta1AWSClusterStatusBastion**](IoXK8sClusterInfrastructureV1beta1AWSClusterStatusBastion.md) |  | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions provide observations of the operational state of a Cluster API resource. | [optional] 
**failure_domains** | [**dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains)**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains.md) | FailureDomains is a slice of FailureDomains. | [optional] 
**network_status** | [**IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus**](IoXK8sClusterInfrastructureV1alpha4AWSClusterStatusNetworkStatus.md) |  | [optional] 
**ready** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


