# IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNS

Use the Microsoft Azure DNS API to manage DNS01 challenge records.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.client_id** | **str** | if both this and ClientSecret are left unset MSI will be used | [optional] 
**kubernetes.client_secret_secret_ref** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNSClientSecretSecretRef**](IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNSClientSecretSecretRef.md) |  | [optional] 
**environment** | **str** | name of the Azure environment (default AzurePublicCloud) | [optional] 
**hosted_zone_name** | **str** | name of the DNS zone that should be used | [optional] 
**managed_identity** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNSManagedIdentity**](IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNSManagedIdentity.md) |  | [optional] 
**resource_group_name** | **str** | resource group the DNS zone is located in | 
**subscription_id** | **str** | ID of the Azure subscription | 
**tenant_id** | **str** | when specifying ClientID and ClientSecret then this field is also needed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


