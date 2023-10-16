# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecResources1

Resources holds requests and limits for individual pods.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecResourcesClaims]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecResourcesClaims.md) | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.   This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.   This field is immutable. | [optional] 
**limits** | **dict(str, object)** | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 
**requests** | **dict(str, object)** | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


