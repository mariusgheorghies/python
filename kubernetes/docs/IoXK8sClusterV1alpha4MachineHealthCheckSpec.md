# IoXK8sClusterV1alpha4MachineHealthCheckSpec

Specification of machine health check policy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | ClusterName is the name of the Cluster this object belongs to. | 
**max_unhealthy** | [**object**](.md) | Any further remediation is only allowed if at most \&quot;MaxUnhealthy\&quot; machines selected by \&quot;selector\&quot; are not healthy. | [optional] 
**node_startup_timeout** | **str** | Machines older than this duration without a node will be considered to have failed and will be remediated. If not set, this value is defaulted to 10 minutes. If you wish to disable this feature, set the value explicitly to 0. | [optional] 
**remediation_template** | [**IoXK8sClusterV1alpha3MachineHealthCheckSpecRemediationTemplate**](IoXK8sClusterV1alpha3MachineHealthCheckSpecRemediationTemplate.md) |  | [optional] 
**selector** | [**IoXK8sClusterV1alpha3MachineHealthCheckSpecSelector**](IoXK8sClusterV1alpha3MachineHealthCheckSpecSelector.md) |  | 
**unhealthy_conditions** | [**list[IoXK8sClusterV1alpha3MachineHealthCheckSpecUnhealthyConditions]**](IoXK8sClusterV1alpha3MachineHealthCheckSpecUnhealthyConditions.md) | UnhealthyConditions contains a list of the conditions that determine whether a node is considered unhealthy.  The conditions are combined in a logical OR, i.e. if any of the conditions is met, the node is unhealthy. | 
**unhealthy_range** | **str** | Any further remediation is only allowed if the number of machines selected by \&quot;selector\&quot; as not healthy is within the range of \&quot;UnhealthyRange\&quot;. Takes precedence over MaxUnhealthy. Eg. \&quot;[3-5]\&quot; - This means that remediation will be allowed only when: (a) there are at least 3 unhealthy machines (and) (b) there are at most 5 unhealthy machines | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


