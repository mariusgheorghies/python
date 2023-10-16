# IoTigeraOperatorV1InstallationSpecCni

CNI specifies the CNI that will be used by this installation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipam** | [**IoTigeraOperatorV1InstallationSpecCniIpam**](IoTigeraOperatorV1InstallationSpecCniIpam.md) |  | [optional] 
**type** | **str** | Specifies the CNI plugin that will be used in the Calico or Calico Enterprise installation. * For KubernetesProvider GKE, this field defaults to GKE. * For KubernetesProvider AKS, this field defaults to AzureVNET. * For KubernetesProvider EKS, this field defaults to AmazonVPC. * If aws-node daemonset exists in kube-system when the Installation resource is created, this field defaults to AmazonVPC. * For all other cases this field defaults to Calico.   For the value Calico, the CNI plugin binaries and CNI config will be installed as part of deployment, for all other values the CNI plugin binaries and CNI config is a dependency that is expected to be installed separately.   Default: Calico | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


