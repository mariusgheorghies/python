# IoCertManagerV1ClusterIssuerSpecSelfSigned

SelfSigned configures this issuer to 'self sign' certificates using the private key used to create the CertificateRequest object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crl_distribution_points** | **list[str]** | The CRL distribution points is an X.509 v3 certificate extension which identifies the location of the CRL from which the revocation of this certificate can be checked. If not set certificate will be issued without CDP. Values are strings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


