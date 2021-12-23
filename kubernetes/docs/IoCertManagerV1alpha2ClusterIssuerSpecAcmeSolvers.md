# IoCertManagerV1alpha2ClusterIssuerSpecAcmeSolvers

Configures an issuer to solve challenges using the specified options. Only one of HTTP01 or DNS01 may be provided.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns01** | [**IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01**](IoCertManagerAcmeV1alpha2ChallengeSpecSolverDns01.md) |  | [optional] 
**http01** | [**IoCertManagerAcmeV1alpha2ChallengeSpecSolverHttp01**](IoCertManagerAcmeV1alpha2ChallengeSpecSolverHttp01.md) |  | [optional] 
**selector** | [**IoCertManagerAcmeV1ChallengeSpecSolverSelector**](IoCertManagerAcmeV1ChallengeSpecSolverSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


