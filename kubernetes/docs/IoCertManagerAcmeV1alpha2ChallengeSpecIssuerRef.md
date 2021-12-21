# IoCertManagerAcmeV1alpha2ChallengeSpecIssuerRef

IssuerRef references a properly configured ACME-type Issuer which should be used to create this Challenge. If the Issuer does not exist, processing will be retried. If the Issuer is not an 'ACME' Issuer, an error will be returned and the Challenge will be marked as failed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Group of the resource being referred to. | [optional] 
**kind** | **str** | Kind of the resource being referred to. | [optional] 
**name** | **str** | Name of the resource being referred to. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


