# IoCertManagerV1ClusterIssuerSpecAcmeSolvers

An ACMEChallengeSolver describes how to solve ACME challenges for the issuer it is part of. A selector may be provided to use different solving strategies for different DNS names. Only one of HTTP01 or DNS01 must be provided.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns01** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01**](IoCertManagerAcmeV1ChallengeSpecSolverDns01.md) |  | [optional] 
**http01** | [**IoCertManagerAcmeV1ChallengeSpecSolverHttp01**](IoCertManagerAcmeV1ChallengeSpecSolverHttp01.md) |  | [optional] 
**selector** | [**IoCertManagerAcmeV1ChallengeSpecSolverSelector**](IoCertManagerAcmeV1ChallengeSpecSolverSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


