# V1VolumeSnapshotSpecSource

source specifies where a snapshot will be created from. This field is immutable after creation. Required.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persistent_volume_claim_name** | **str** | persistentVolumeClaimName specifies the name of the PersistentVolumeClaim object representing the volume from which a snapshot should be created. This PVC is assumed to be in the same namespace as the VolumeSnapshot object. This field should be set if the snapshot does not exists, and needs to be created. This field is immutable. | [optional] 
**volume_snapshot_content_name** | **str** | volumeSnapshotContentName specifies the name of a pre-existing VolumeSnapshotContent object representing an existing volume snapshot. This field should be set if the snapshot already exists and only needs a representation in Kubernetes. This field is immutable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


