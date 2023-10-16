# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPersistentVolumeClaim

persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_name** | **str** | claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims | 
**read_only** | **bool** | readOnly Will force the ReadOnly setting in VolumeMounts. Default false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


