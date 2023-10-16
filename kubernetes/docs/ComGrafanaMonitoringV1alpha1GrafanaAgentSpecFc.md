# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecFc

fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. TODO: how do we prevent errors in the filesystem from compromising the machine | [optional] 
**lun** | **int** | lun is Optional: FC target lun number | [optional] 
**read_only** | **bool** | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**target_ww_ns** | **list[str]** | targetWWNs is Optional: FC target worldwide names (WWNs) | [optional] 
**wwids** | **list[str]** | wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

