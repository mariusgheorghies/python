# IoXK8sHncV1alpha2HNCConfigurationStatus

HNCConfigurationStatus defines the observed state of HNC configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoXK8sHncV1alpha2HNCConfigurationStatusConditions]**](IoXK8sHncV1alpha2HNCConfigurationStatusConditions.md) | Conditions describes the errors, if any. If there are any conditions with \&quot;ActivitiesHalted\&quot; reason, this means that HNC cannot function in the affected namespaces. The HierarchyConfiguration object in each of the affected namespaces will have more information. To learn more about conditions, see https://github.com/kubernetes-sigs/hierarchical-namespaces/blob/master/docs/user-guide/concepts.md#admin-conditions. | [optional] 
**resources** | [**list[IoXK8sHncV1alpha2HNCConfigurationStatusResources]**](IoXK8sHncV1alpha2HNCConfigurationStatusResources.md) | Resources indicates the observed synchronization states of the resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


