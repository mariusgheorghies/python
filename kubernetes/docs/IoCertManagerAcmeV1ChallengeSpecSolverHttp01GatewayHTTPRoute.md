# IoCertManagerAcmeV1ChallengeSpecSolverHttp01GatewayHTTPRoute

The Gateway API is a sig-network community API that models service networking in Kubernetes (https://gateway-api.sigs.k8s.io/). The Gateway solver will create HTTPRoutes with the specified labels in the same namespace as the challenge. This solver is experimental, and fields / behaviour may change in the future.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **dict(str, str)** | The labels that cert-manager will use when creating the temporary HTTPRoute needed for solving the HTTP-01 challenge. These labels must match the label selector of at least one Gateway. | [optional] 
**service_type** | **str** | Optional service type for Kubernetes solver service. Supported values are NodePort or ClusterIP. If unset, defaults to NodePort. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


