# AwsK8sNetworkingV1alpha1PolicyEndpointSpec

PolicyEndpointSpec defines the desired state of PolicyEndpoint
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egress** | [**list[AwsK8sNetworkingV1alpha1PolicyEndpointSpecEgress]**](AwsK8sNetworkingV1alpha1PolicyEndpointSpecEgress.md) | Egress is the list of egress rules containing resolved network addresses | [optional] 
**ingress** | [**list[AwsK8sNetworkingV1alpha1PolicyEndpointSpecEgress]**](AwsK8sNetworkingV1alpha1PolicyEndpointSpecEgress.md) | Ingress is the list of ingress rules containing resolved network addresses | [optional] 
**pod_isolation** | **list[str]** | PodIsolation specifies whether the pod needs to be isolated for a particular traffic direction Ingress or Egress, or both. If default isolation is not specified, and there are no ingress/egress rules, then the pod is not isolated from the point of view of this policy. This follows the NetworkPolicy spec.PolicyTypes. | [optional] 
**pod_selector** | [**AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelector**](AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelector.md) |  | [optional] 
**pod_selector_endpoints** | [**list[AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorEndpoints]**](AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorEndpoints.md) | PodSelectorEndpoints contains information about the pods matching the podSelector | [optional] 
**policy_ref** | [**AwsK8sNetworkingV1alpha1PolicyEndpointSpecPolicyRef**](AwsK8sNetworkingV1alpha1PolicyEndpointSpecPolicyRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


