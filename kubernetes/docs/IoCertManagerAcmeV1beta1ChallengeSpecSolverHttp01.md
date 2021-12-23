# IoCertManagerAcmeV1beta1ChallengeSpecSolverHttp01

Configures cert-manager to attempt to complete authorizations by performing the HTTP01 challenge flow. It is not possible to obtain certificates for wildcard domain names (e.g. `*.example.com`) using the HTTP01 challenge mechanism.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_http_route** | [**IoCertManagerAcmeV1ChallengeSpecSolverHttp01GatewayHTTPRoute**](IoCertManagerAcmeV1ChallengeSpecSolverHttp01GatewayHTTPRoute.md) |  | [optional] 
**ingress** | [**IoCertManagerAcmeV1beta1ChallengeSpecSolverHttp01Ingress**](IoCertManagerAcmeV1beta1ChallengeSpecSolverHttp01Ingress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


