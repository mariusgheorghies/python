# IoArgoprojV1alpha1AppProjectSpec

AppProjectSpec is the specification of an AppProject
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_resource_blacklist** | [**list[IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist]**](IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist.md) | ClusterResourceBlacklist contains list of blacklisted cluster level resources | [optional] 
**cluster_resource_whitelist** | [**list[IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist]**](IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist.md) | ClusterResourceWhitelist contains list of whitelisted cluster level resources | [optional] 
**description** | **str** | Description contains optional project description | [optional] 
**destinations** | [**list[IoArgoprojV1alpha1AppProjectSpecDestinations]**](IoArgoprojV1alpha1AppProjectSpecDestinations.md) | Destinations contains list of destinations available for deployment | [optional] 
**namespace_resource_blacklist** | [**list[IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist]**](IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist.md) | NamespaceResourceBlacklist contains list of blacklisted namespace level resources | [optional] 
**namespace_resource_whitelist** | [**list[IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist]**](IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist.md) | NamespaceResourceWhitelist contains list of whitelisted namespace level resources | [optional] 
**orphaned_resources** | [**IoArgoprojV1alpha1AppProjectSpecOrphanedResources**](IoArgoprojV1alpha1AppProjectSpecOrphanedResources.md) |  | [optional] 
**permit_only_project_scoped_clusters** | **bool** | PermitOnlyProjectScopedClusters determines whether destinations can only reference clusters which are project-scoped | [optional] 
**roles** | [**list[IoArgoprojV1alpha1AppProjectSpecRoles]**](IoArgoprojV1alpha1AppProjectSpecRoles.md) | Roles are user defined RBAC roles associated with this project | [optional] 
**signature_keys** | [**list[IoArgoprojV1alpha1AppProjectSpecSignatureKeys]**](IoArgoprojV1alpha1AppProjectSpecSignatureKeys.md) | SignatureKeys contains a list of PGP key IDs that commits in Git must be signed with in order to be allowed for sync | [optional] 
**source_namespaces** | **list[str]** | SourceNamespaces defines the namespaces application resources are allowed to be created in | [optional] 
**source_repos** | **list[str]** | SourceRepos contains list of repository URLs which can be used for deployment | [optional] 
**sync_windows** | [**list[IoArgoprojV1alpha1AppProjectSpecSyncWindows]**](IoArgoprojV1alpha1AppProjectSpecSyncWindows.md) | SyncWindows controls when syncs can be run for apps in this project | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


