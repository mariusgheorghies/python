# IoXK8sClusterV1alpha3MachineDeploymentSpec

MachineDeploymentSpec defines the desired state of MachineDeployment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | ClusterName is the name of the Cluster this object belongs to. | 
**min_ready_seconds** | **int** | Minimum number of seconds for which a newly created machine should be ready. Defaults to 0 (machine will be considered available as soon as it is ready) | [optional] 
**paused** | **bool** | Indicates that the deployment is paused. | [optional] 
**progress_deadline_seconds** | **int** | The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. | [optional] 
**replicas** | **int** | Number of desired machines. Defaults to 1. This is a pointer to distinguish between explicit zero and not specified. | [optional] 
**revision_history_limit** | **int** | The number of old MachineSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] 
**selector** | [**IoXK8sClusterV1alpha3MachineDeploymentSpecSelector**](IoXK8sClusterV1alpha3MachineDeploymentSpecSelector.md) |  | 
**strategy** | [**IoXK8sClusterV1alpha3MachineDeploymentSpecStrategy**](IoXK8sClusterV1alpha3MachineDeploymentSpecStrategy.md) |  | [optional] 
**template** | [**IoXK8sClusterV1alpha3MachineDeploymentSpecTemplate**](IoXK8sClusterV1alpha3MachineDeploymentSpecTemplate.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


