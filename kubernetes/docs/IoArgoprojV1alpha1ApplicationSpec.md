# IoArgoprojV1alpha1ApplicationSpec

ApplicationSpec represents desired application state. Contains link to repository with application definition and additional parameters link definition revision.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**IoArgoprojV1alpha1ApplicationSpecDestination**](IoArgoprojV1alpha1ApplicationSpecDestination.md) |  | 
**ignore_differences** | [**list[IoArgoprojV1alpha1ApplicationSpecIgnoreDifferences]**](IoArgoprojV1alpha1ApplicationSpecIgnoreDifferences.md) | IgnoreDifferences is a list of resources and their fields which should be ignored during comparison | [optional] 
**info** | [**list[IoArgoprojV1alpha1ApplicationOperationInfo]**](IoArgoprojV1alpha1ApplicationOperationInfo.md) | Info contains a list of information (URLs, email addresses, and plain text) that relates to the application | [optional] 
**project** | **str** | Project is a reference to the project this application belongs to. The empty string means that application belongs to the &#39;default&#39; project. | 
**revision_history_limit** | **int** | RevisionHistoryLimit limits the number of items kept in the application&#39;s revision history, which is used for informational purposes as well as for rollbacks to previous versions. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10. | [optional] 
**source** | [**IoArgoprojV1alpha1ApplicationSpecSource**](IoArgoprojV1alpha1ApplicationSpecSource.md) |  | [optional] 
**sources** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncSources]**](IoArgoprojV1alpha1ApplicationOperationSyncSources.md) | Sources is a reference to the location of the application&#39;s manifests or chart | [optional] 
**sync_policy** | [**IoArgoprojV1alpha1ApplicationSpecSyncPolicy**](IoArgoprojV1alpha1ApplicationSpecSyncPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


