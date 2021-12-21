# IoXK8sClusterInfrastructureV1alpha3AWSClusterStatus

AWSClusterStatus defines the observed state of AWSCluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bastion** | [**IoXK8sClusterInfrastructureV1alpha3AWSClusterStatusBastion**](IoXK8sClusterInfrastructureV1alpha3AWSClusterStatusBastion.md) |  | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions.md) | Conditions provide observations of the operational state of a Cluster API resource. | [optional] 
**failure_domains** | [**dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains)**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains.md) | FailureDomains is a slice of FailureDomains. | [optional] 
**network** | [**IoXK8sClusterInfrastructureV1alpha3AWSClusterStatusNetwork**](IoXK8sClusterInfrastructureV1alpha3AWSClusterStatusNetwork.md) |  | [optional] 
**ready** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


