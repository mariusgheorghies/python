# ComCoreosMonitoringV1AlertmanagerSpecHostPath

HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath --- TODO(jonesdl) We need to restrict who can use host directory mounts and who can/can not mount host directories as read/write.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | 
**type** | **str** | Type for HostPath Volume Defaults to \&quot;\&quot; More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


