# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess

Endpoints specifies access to this cluster's control plane endpoints
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | **bool** | Private points VPC-internal control plane access to the private endpoint | [optional] 
**public** | **bool** | Public controls whether control plane endpoints are publicly accessible | [optional] 
**public_cid_rs** | **list[str]** | PublicCIDRs specifies which blocks can access the public endpoint | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


