# IoCertManagerV1alpha2CertificateSpecKeystoresJks

JKS configures options for storing a JKS keystore in the `spec.secretName` Secret resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | **bool** | Create enables JKS keystore creation for the Certificate. If true, a file named &#x60;keystore.jks&#x60; will be created in the target Secret resource, encrypted using the password stored in &#x60;passwordSecretRef&#x60;. The keystore file will only be updated upon re-issuance. | 
**password_secret_ref** | [**IoCertManagerV1CertificateSpecKeystoresJksPasswordSecretRef**](IoCertManagerV1CertificateSpecKeystoresJksPasswordSecretRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


