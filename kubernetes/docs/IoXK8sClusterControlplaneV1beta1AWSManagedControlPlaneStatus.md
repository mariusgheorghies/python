# IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatus

AWSManagedControlPlaneStatus defines the observed state of an Amazon EKS Cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**list[IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusAddons]**](IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusAddons.md) | Addons holds the current status of the EKS addons | [optional] 
**bastion** | [**IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastion**](IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastion.md) |  | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions specifies the cpnditions for the managed control plane | [optional] 
**external_managed_control_plane** | **bool** | ExternalManagedControlPlane indicates to cluster-api that the control plane is managed by an external service such as AKS, EKS, GKE, etc. | [optional] 
**failure_domains** | [**dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains)**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains.md) | FailureDomains specifies a list fo available availability zones that can be used | [optional] 
**failure_message** | **str** | ErrorMessage indicates that there is a terminal problem reconciling the state, and will be set to a descriptive error message. | [optional] 
**identity_provider_status** | [**IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusIdentityProviderStatus**](IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusIdentityProviderStatus.md) |  | [optional] 
**initialized** | **bool** | Initialized denotes whether or not the control plane has the uploaded kubernetes config-map. | [optional] 
**network_status** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetwork**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetwork.md) |  | [optional] 
**oidc_provider** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusOidcProvider**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusOidcProvider.md) |  | [optional] 
**ready** | **bool** | Ready denotes that the AWSManagedControlPlane API Server is ready to receive requests and that the VPC infra is ready. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


