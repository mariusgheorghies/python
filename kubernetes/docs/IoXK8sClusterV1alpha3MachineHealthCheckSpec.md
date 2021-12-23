# IoXK8sClusterV1alpha3MachineHealthCheckSpec

Specification of machine health check policy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | ClusterName is the name of the Cluster this object belongs to. | 
**max_unhealthy** | [**object**](.md) | Any further remediation is only allowed if at most \&quot;MaxUnhealthy\&quot; machines selected by \&quot;selector\&quot; are not healthy. | [optional] 
**node_startup_timeout** | **str** | Machines older than this duration without a node will be considered to have failed and will be remediated. | [optional] 
**remediation_template** | [**IoXK8sClusterV1alpha3MachineHealthCheckSpecRemediationTemplate**](IoXK8sClusterV1alpha3MachineHealthCheckSpecRemediationTemplate.md) |  | [optional] 
**selector** | [**IoXK8sClusterV1alpha3MachineHealthCheckSpecSelector**](IoXK8sClusterV1alpha3MachineHealthCheckSpecSelector.md) |  | 
**unhealthy_conditions** | [**list[IoXK8sClusterV1alpha3MachineHealthCheckSpecUnhealthyConditions]**](IoXK8sClusterV1alpha3MachineHealthCheckSpecUnhealthyConditions.md) | UnhealthyConditions contains a list of the conditions that determine whether a node is considered unhealthy.  The conditions are combined in a logical OR, i.e. if any of the conditions is met, the node is unhealthy. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


