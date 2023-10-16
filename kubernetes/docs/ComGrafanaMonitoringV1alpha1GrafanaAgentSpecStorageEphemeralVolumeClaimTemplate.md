# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplate

Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod.  The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).   An existing PVC with that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.   This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.   Required, must not be nil.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**object**](.md) | May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. | [optional] 
**spec** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpec**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpec.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

