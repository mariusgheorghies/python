# IoXK8sClusterControlplaneV1beta1KubeadmControlPlaneStatus

KubeadmControlPlaneStatus defines the observed state of KubeadmControlPlane.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the KubeadmControlPlane. | [optional] 
**failure_message** | **str** | ErrorMessage indicates that there is a terminal problem reconciling the state, and will be set to a descriptive error message. | [optional] 
**failure_reason** | **str** | FailureReason indicates that there is a terminal problem reconciling the state, and will be set to a token value suitable for programmatic interpretation. | [optional] 
**initialized** | **bool** | Initialized denotes whether or not the control plane has the uploaded kubeadm-config configmap. | [optional] 
**observed_generation** | **int** | ObservedGeneration is the latest generation observed by the controller. | [optional] 
**ready** | **bool** | Ready denotes that the KubeadmControlPlane API Server is ready to receive requests. | [optional] 
**ready_replicas** | **int** | Total number of fully running and ready control plane machines. | [optional] 
**replicas** | **int** | Total number of non-terminated machines targeted by this control plane (their labels match the selector). | [optional] 
**selector** | **str** | Selector is the label selector in string format to avoid introspection by kubernetes.clients, and is used to provide the CRD-based integration for the scale subresource and additional integrations for things like kubectl describe.. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors | [optional] 
**unavailable_replicas** | **int** | Total number of unavailable machines targeted by this control plane. This is the total number of machines that are still required for the deployment to have 100% available capacity. They may either be machines that are running but not yet ready or machines that still have not been created. | [optional] 
**updated_replicas** | **int** | Total number of non-terminated machines targeted by this control plane that have the desired template spec. | [optional] 
**version** | **str** | Version represents the minimum Kubernetes version for the control plane machines in the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


