# IoArgoprojV1alpha1ApplicationOperationSyncSource

Source overrides the source definition set in the application. This is typically set in a Rollback operation and is nil during a Sync operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart** | **str** | Chart is a Helm chart name, and must be specified for applications sourced from a Helm repo. | [optional] 
**directory** | [**IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectory**](IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectory.md) |  | [optional] 
**helm** | [**IoArgoprojV1alpha1ApplicationOperationSyncSourceHelm**](IoArgoprojV1alpha1ApplicationOperationSyncSourceHelm.md) |  | [optional] 
**kustomize** | [**IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize**](IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize.md) |  | [optional] 
**path** | **str** | Path is a directory path within the Git repository, and is only valid for applications sourced from Git. | [optional] 
**plugin** | [**IoArgoprojV1alpha1ApplicationOperationSyncSourcePlugin**](IoArgoprojV1alpha1ApplicationOperationSyncSourcePlugin.md) |  | [optional] 
**ref** | **str** | Ref is reference to another source within sources field. This field will not be used if used with a &#x60;source&#x60; tag. | [optional] 
**repo_url** | **str** | RepoURL is the URL to the repository (Git or Helm) that contains the application manifests | 
**target_revision** | **str** | TargetRevision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch. If omitted, will equal to HEAD. In case of Helm, this is a semver tag for the Chart&#39;s version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


