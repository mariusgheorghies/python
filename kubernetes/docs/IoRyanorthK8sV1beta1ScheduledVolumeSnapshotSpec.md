# IoRyanorthK8sV1beta1ScheduledVolumeSnapshotSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persistent_volume_claim_name** | **str** | The name of the persistent volume claim snapshots should be taken against. | 
**snapshot_class_name** | **str** | The name of the VolumeSnapshotClass to be used for generating the snapshot. | 
**snapshot_frequency** | [**object**](.md) | How often a snapshot should be created against the persistent volume. Value can be provided as a string (e.g. 30m, 5h, 4d, 1w, etc.) or an integer (interpretted in hours).  | 
**snapshot_labels** | **dict(str, str)** | Labels to include on the VolumeSnapshot objects. | [optional] 
**snapshot_retention** | [**object**](.md) | How long a snapshot should be retained. Value can be provided as a string (e.g. 30m, 5h, 4d, 1w, etc.) or an integer (interpretted in hours). Negative values indicate indefinite retention.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


