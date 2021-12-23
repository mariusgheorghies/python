# IoCertManagerV1ClusterIssuerStatusAcme

ACME specific status options. This field should only be set if the Issuer is configured to use an ACME server to issue certificates.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_registered_email** | **str** | LastRegisteredEmail is the email associated with the latest registered ACME account, in order to track changes made to registered account associated with the  Issuer | [optional] 
**uri** | **str** | URI is the unique account identifier, which can also be used to retrieve account details from the CA | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


