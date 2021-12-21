# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecUsers

User defines the input for a generated user in cloud-init.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gecos** | **str** | Gecos specifies the gecos to use for the user | [optional] 
**groups** | **str** | Groups specifies the additional groups for the user | [optional] 
**home_dir** | **str** | HomeDir specifies the home directory to use for the user | [optional] 
**inactive** | **bool** | Inactive specifies whether to mark the user as inactive | [optional] 
**lock_password** | **bool** | LockPassword specifies if password login should be disabled | [optional] 
**name** | **str** | Name specifies the user name | 
**passwd** | **str** | Passwd specifies a hashed password for the user | [optional] 
**primary_group** | **str** | PrimaryGroup specifies the primary group for the user | [optional] 
**shell** | **str** | Shell specifies the user&#39;s shell | [optional] 
**ssh_authorized_keys** | **list[str]** | SSHAuthorizedKeys specifies a list of ssh authorized keys for the user | [optional] 
**sudo** | **str** | Sudo specifies a sudo role for the user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


