# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains

FailureDomainSpec is the Schema for Cluster API failure domains. It allows controllers to understand how many failure domains a cluster can optionally span across.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **dict(str, str)** | Attributes is a free form map of attributes an infrastructure provider might use or require. | [optional] 
**control_plane** | **bool** | ControlPlane determines if this failure domain is suitable for use by control plane machines. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


