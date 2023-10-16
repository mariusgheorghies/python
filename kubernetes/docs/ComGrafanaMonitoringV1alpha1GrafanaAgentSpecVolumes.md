# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes

Volume represents a named volume in a pod that may be accessed by any container in the pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_elastic_block_store** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAwsElasticBlockStore**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAwsElasticBlockStore.md) |  | [optional] 
**azure_disk** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAzureDisk**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAzureDisk.md) |  | [optional] 
**azure_file** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAzureFile**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAzureFile.md) |  | [optional] 
**cephfs** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCephfs**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCephfs.md) |  | [optional] 
**cinder** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder.md) |  | [optional] 
**config_map** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecConfigMap**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecConfigMap.md) |  | [optional] 
**csi** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCsi**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCsi.md) |  | [optional] 
**downward_api** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecDownwardAPI**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecDownwardAPI.md) |  | [optional] 
**empty_dir** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecEmptyDir**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecEmptyDir.md) |  | [optional] 
**ephemeral** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecEphemeral**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecEphemeral.md) |  | [optional] 
**fc** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecFc**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecFc.md) |  | [optional] 
**flex_volume** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecFlexVolume**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecFlexVolume.md) |  | [optional] 
**flocker** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecFlocker**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecFlocker.md) |  | [optional] 
**gce_persistent_disk** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk.md) |  | [optional] 
**git_repo** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGitRepo**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGitRepo.md) |  | [optional] 
**glusterfs** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGlusterfs**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGlusterfs.md) |  | [optional] 
**host_path** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecHostPath**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecHostPath.md) |  | [optional] 
**iscsi** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecIscsi**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecIscsi.md) |  | [optional] 
**name** | **str** | name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 
**nfs** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecNfs**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecNfs.md) |  | [optional] 
**persistent_volume_claim** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPersistentVolumeClaim**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPersistentVolumeClaim.md) |  | [optional] 
**photon_persistent_disk** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPhotonPersistentDisk**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPhotonPersistentDisk.md) |  | [optional] 
**portworx_volume** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPortworxVolume**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPortworxVolume.md) |  | [optional] 
**projected** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected.md) |  | [optional] 
**quobyte** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecQuobyte**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecQuobyte.md) |  | [optional] 
**rbd** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbd**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbd.md) |  | [optional] 
**scale_io** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecScaleIO**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecScaleIO.md) |  | [optional] 
**secret** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecSecret**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecSecret.md) |  | [optional] 
**storageos** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageos**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageos.md) |  | [optional] 
**vsphere_volume** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVsphereVolume**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVsphereVolume.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


