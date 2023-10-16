# IoArgoprojV1alpha1ApplicationOperationSync

Sync contains parameters for the operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | DryRun specifies to perform a &#x60;kubectl apply --dry-run&#x60; without actually performing the sync | [optional] 
**manifests** | **list[str]** | Manifests is an optional field that overrides sync source with a local directory for development | [optional] 
**prune** | **bool** | Prune specifies to delete resources from the cluster that are no longer tracked in git | [optional] 
**resources** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncResources]**](IoArgoprojV1alpha1ApplicationOperationSyncResources.md) | Resources describes which resources shall be part of the sync | [optional] 
**revision** | **str** | Revision is the revision (Git) or chart version (Helm) which to sync the application to If omitted, will use the revision specified in app spec. | [optional] 
**revisions** | **list[str]** | Revisions is the list of revision (Git) or chart version (Helm) which to sync each source in sources field for the application to If omitted, will use the revision specified in app spec. | [optional] 
**source** | [**IoArgoprojV1alpha1ApplicationOperationSyncSource**](IoArgoprojV1alpha1ApplicationOperationSyncSource.md) |  | [optional] 
**sources** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncSources]**](IoArgoprojV1alpha1ApplicationOperationSyncSources.md) | Sources overrides the source definition set in the application. This is typically set in a Rollback operation and is nil during a Sync operation | [optional] 
**sync_options** | **list[str]** | SyncOptions provide per-sync sync-options, e.g. Validate&#x3D;false | [optional] 
**sync_strategy** | [**IoArgoprojV1alpha1ApplicationOperationSyncSyncStrategy**](IoArgoprojV1alpha1ApplicationOperationSyncSyncStrategy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


