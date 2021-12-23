# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkSecurityGroups

SecurityGroup defines an AWS security group.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a unique identifier. | 
**ingress_rule** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkIngressRule]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkIngressRule.md) | IngressRules is the inbound rules associated with the security group. | [optional] 
**name** | **str** | Name is the security group name. | 
**tags** | **dict(str, str)** | Tags is a map of tags associated with the security group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


