# IoCertManagerAcmeV1alpha2ChallengeSpecSolverHttp01Ingress

The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | The ingress class to use when creating Ingress resources to solve ACME challenges that use this challenge solver. Only one of &#39;class&#39; or &#39;name&#39; may be specified. | [optional] 
**ingress_template** | [**IoCertManagerAcmeV1alpha2ChallengeSpecSolverHttp01IngressIngressTemplate**](IoCertManagerAcmeV1alpha2ChallengeSpecSolverHttp01IngressIngressTemplate.md) |  | [optional] 
**name** | **str** | The name of the ingress resource that should have ACME challenge solving routes inserted into it in order to solve HTTP01 challenges. This is typically used in conjunction with ingress controllers like ingress-gce, which maintains a 1:1 mapping between external IPs and ingress resources. | [optional] 
**pod_template** | [**IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplate**](IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplate.md) |  | [optional] 
**service_type** | **str** | Optional service type for Kubernetes solver service. Supported values are NodePort or ClusterIP. If unset, defaults to NodePort. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


