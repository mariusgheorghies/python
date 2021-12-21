# ComCoreosMonitoringV1PrometheusSpecStorage

Storage spec to specify how storage shall be used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_mount_sub_path** | **bool** | Deprecated: subPath usage will be disabled by default in a future release, this option will become unnecessary. DisableMountSubPath allows to remove any subPath usage in volume mounts. | [optional] 
**empty_dir** | [**ComCoreosMonitoringV1AlertmanagerSpecStorageEmptyDir**](ComCoreosMonitoringV1AlertmanagerSpecStorageEmptyDir.md) |  | [optional] 
**volume_claim_template** | [**ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplate**](ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


