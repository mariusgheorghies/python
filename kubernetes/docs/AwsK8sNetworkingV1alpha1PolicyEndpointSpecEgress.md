# AwsK8sNetworkingV1alpha1PolicyEndpointSpecEgress

EndpointInfo defines the network endpoint information for the policy ingress/egress
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | CIDR is the network address(s) of the endpoint | 
**_except** | **list[str]** | Except is the exceptions to the CIDR ranges mentioned above. | [optional] 
**ports** | [**list[AwsK8sNetworkingV1alpha1PolicyEndpointSpecPorts]**](AwsK8sNetworkingV1alpha1PolicyEndpointSpecPorts.md) | Ports is the list of ports | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


