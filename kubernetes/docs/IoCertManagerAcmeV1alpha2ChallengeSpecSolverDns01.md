# IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01

Configures cert-manager to attempt to complete authorizations by performing the DNS01 challenge flow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acmedns** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNS**](IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNS.md) |  | [optional] 
**akamai** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Akamai**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Akamai.md) |  | [optional] 
**azuredns** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNS**](IoCertManagerAcmeV1ChallengeSpecSolverDns01AzureDNS.md) |  | [optional] 
**clouddns** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS**](IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS.md) |  | [optional] 
**cloudflare** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Cloudflare**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Cloudflare.md) |  | [optional] 
**cname_strategy** | **str** | CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones. | [optional] 
**digitalocean** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Digitalocean**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Digitalocean.md) |  | [optional] 
**rfc2136** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136.md) |  | [optional] 
**route53** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53.md) |  | [optional] 
**webhook** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Webhook**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Webhook.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


