# IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudDNS

Use the Google Cloud DNS API to manage DNS01 challenge records.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosted_zone_name** | **str** | HostedZoneName is an optional field that tells cert-manager in which Cloud DNS zone the challenge record has to be created. If left empty cert-manager will automatically choose a zone. | [optional] 
**project** | **str** |  | 
**service_account_secret_ref** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNSAccountSecretRef**](IoCertManagerAcmeV1ChallengeSpecSolverDns01AcmeDNSAccountSecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


