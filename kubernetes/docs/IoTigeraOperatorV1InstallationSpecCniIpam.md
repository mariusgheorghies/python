# IoTigeraOperatorV1InstallationSpecCniIpam

IPAM specifies the pod IP address management that will be used in the Calico or Calico Enterprise installation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specifies the IPAM plugin that will be used in the Calico or Calico Enterprise installation. * For CNI Plugin Calico, this field defaults to Calico. * For CNI Plugin GKE, this field defaults to HostLocal. * For CNI Plugin AzureVNET, this field defaults to AzureVNET. * For CNI Plugin AmazonVPC, this field defaults to AmazonVPC.   The IPAM plugin is installed and configured only if the CNI plugin is set to Calico, for all other values of the CNI plugin the plugin binaries and CNI config is a dependency that is expected to be installed separately.   Default: Calico | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


