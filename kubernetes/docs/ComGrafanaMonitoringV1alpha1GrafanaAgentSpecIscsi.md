# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecIscsi

iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chap_auth_discovery** | **bool** | chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication | [optional] 
**chap_auth_session** | **bool** | chapAuthSession defines whether support iSCSI Session CHAP authentication | [optional] 
**fs_type** | **str** | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi TODO: how do we prevent errors in the filesystem from compromising the machine | [optional] 
**initiator_name** | **str** | initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface &lt;target portal&gt;:&lt;volume name&gt; will be created for the connection. | [optional] 
**iqn** | **str** | iqn is the target iSCSI Qualified Name. | 
**iscsi_interface** | **str** | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to &#39;default&#39; (tcp). | [optional] 
**lun** | **int** | lun represents iSCSI Target Lun number. | 
**portals** | **list[str]** | portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | [optional] 
**read_only** | **bool** | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. | [optional] 
**secret_ref** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecIscsiSecretRef**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecIscsiSecretRef.md) |  | [optional] 
**target_portal** | **str** | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

