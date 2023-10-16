# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorage

Storage spec to specify how storage will be used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_mount_sub_path** | **bool** | Deprecated: subPath usage will be disabled by default in a future release, this option will become unnecessary. DisableMountSubPath allows to remove any subPath usage in volume mounts. | [optional] 
**empty_dir** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEmptyDir**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEmptyDir.md) |  | [optional] 
**ephemeral** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeral**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeral.md) |  | [optional] 
**volume_claim_template** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplate**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


