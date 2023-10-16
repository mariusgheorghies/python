# ComCoreosMonitoringV1PrometheusSpecServiceMonitorSelector

ServiceMonitors to be selected for target discovery. *Deprecated:* if neither this nor podMonitorSelector are specified, configuration is unmanaged.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**list[AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions]**](AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions.md) | matchExpressions is a list of label selector requirements. The requirements are ANDed. | [optional] 
**match_labels** | **dict(str, str)** | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \&quot;key\&quot;, the operator is \&quot;In\&quot;, and the values array contains only \&quot;value\&quot;. The requirements are ANDed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


