# IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateMetadata

ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | Annotations that should be added to the create ACME HTTP01 solver pods. | [optional] 
**labels** | **dict(str, str)** | Labels that should be added to the created ACME HTTP01 solver pods. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


