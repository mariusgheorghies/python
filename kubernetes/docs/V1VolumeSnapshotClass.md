# V1VolumeSnapshotClass

VolumeSnapshotClass specifies parameters that a underlying storage system uses when creating a volume snapshot. A specific VolumeSnapshotClass is used by specifying its name in a VolumeSnapshot object. VolumeSnapshotClasses are non-namespaced
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**deletion_policy** | **str** | deletionPolicy determines whether a VolumeSnapshotContent created through the VolumeSnapshotClass should be deleted when its bound VolumeSnapshot is deleted. Supported values are \&quot;Retain\&quot; and \&quot;Delete\&quot;. \&quot;Retain\&quot; means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are kept. \&quot;Delete\&quot; means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are deleted. Required. | 
**driver** | **str** | driver is the name of the storage driver that handles this VolumeSnapshotClass. Required. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**parameters** | **dict(str, str)** | parameters is a key-value map with storage driver specific parameters for creating snapshots. These values are opaque to Kubernetes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


