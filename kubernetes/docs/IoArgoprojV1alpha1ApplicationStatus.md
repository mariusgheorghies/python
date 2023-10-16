# IoArgoprojV1alpha1ApplicationStatus

ApplicationStatus contains status information for the application
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoArgoprojV1alpha1ApplicationStatusConditions]**](IoArgoprojV1alpha1ApplicationStatusConditions.md) | Conditions is a list of currently observed application conditions | [optional] 
**health** | [**IoArgoprojV1alpha1ApplicationStatusHealth**](IoArgoprojV1alpha1ApplicationStatusHealth.md) |  | [optional] 
**history** | [**list[IoArgoprojV1alpha1ApplicationStatusHistory]**](IoArgoprojV1alpha1ApplicationStatusHistory.md) | History contains information about the application&#39;s sync history | [optional] 
**observed_at** | **datetime** | ObservedAt indicates when the application state was updated without querying latest git state Deprecated: controller no longer updates ObservedAt field | [optional] 
**operation_state** | [**IoArgoprojV1alpha1ApplicationStatusOperationState**](IoArgoprojV1alpha1ApplicationStatusOperationState.md) |  | [optional] 
**reconciled_at** | **datetime** | ReconciledAt indicates when the application state was reconciled using the latest git version | [optional] 
**resource_health_source** | **str** | ResourceHealthSource indicates where the resource health status is stored: inline if not set or appTree | [optional] 
**resources** | [**list[IoArgoprojV1alpha1ApplicationStatusResources]**](IoArgoprojV1alpha1ApplicationStatusResources.md) | Resources is a list of Kubernetes resources managed by this application | [optional] 
**source_type** | **str** | SourceType specifies the type of this application | [optional] 
**source_types** | **list[str]** | SourceTypes specifies the type of the sources included in the application | [optional] 
**summary** | [**IoArgoprojV1alpha1ApplicationStatusSummary**](IoArgoprojV1alpha1ApplicationStatusSummary.md) |  | [optional] 
**sync** | [**IoArgoprojV1alpha1ApplicationStatusSync**](IoArgoprojV1alpha1ApplicationStatusSync.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


