# IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding

ExternalAccountBinding is a reference to a CA external account of the ACME server. If set, upon registration cert-manager will attempt to associate the given external account credentials with the registered ACME account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_algorithm** | **str** | Deprecated: keyAlgorithm field exists for historical compatibility reasons and should not be used. The algorithm is now hardcoded to HS256 in golang/x/crypto/acme. | [optional] 
**key_id** | **str** | keyID is the ID of the CA key that the External Account is bound to. | 
**key_secret_ref** | [**IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef**](IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


