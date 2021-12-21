# IoCertManagerV1alpha2CertificateRequestSpec

Desired state of the CertificateRequest resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | The PEM-encoded x509 certificate signing request to be submitted to the CA for signing. | 
**duration** | **str** | The requested &#39;duration&#39; (i.e. lifetime) of the Certificate. This option may be ignored/overridden by some issuer types. | [optional] 
**extra** | **dict(str, list[str])** | Extra contains extra attributes of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable. | [optional] 
**groups** | **list[str]** | Groups contains group membership of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable. | [optional] 
**is_ca** | **bool** | IsCA will request to mark the certificate as valid for certificate signing when submitting to the issuer. This will automatically add the &#x60;cert sign&#x60; usage to the list of &#x60;usages&#x60;. | [optional] 
**issuer_ref** | [**IoCertManagerV1CertificateRequestSpecIssuerRef**](IoCertManagerV1CertificateRequestSpecIssuerRef.md) |  | 
**uid** | **str** | UID contains the uid of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable. | [optional] 
**usages** | **list[str]** | Usages is the set of x509 usages that are requested for the certificate. Defaults to &#x60;digital signature&#x60; and &#x60;key encipherment&#x60; if not specified. | [optional] 
**username** | **str** | Username contains the name of the user that created the CertificateRequest. Populated by the cert-manager webhook on creation and immutable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


