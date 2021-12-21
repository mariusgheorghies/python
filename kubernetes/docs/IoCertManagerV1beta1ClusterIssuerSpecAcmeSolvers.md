# IoCertManagerV1beta1ClusterIssuerSpecAcmeSolvers

Configures an issuer to solve challenges using the specified options. Only one of HTTP01 or DNS01 may be provided.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns01** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01**](IoCertManagerAcmeV1ChallengeSpecSolverDns01.md) |  | [optional] 
**http01** | [**IoCertManagerAcmeV1beta1ChallengeSpecSolverHttp01**](IoCertManagerAcmeV1beta1ChallengeSpecSolverHttp01.md) |  | [optional] 
**selector** | [**IoCertManagerAcmeV1ChallengeSpecSolverSelector**](IoCertManagerAcmeV1ChallengeSpecSolverSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


