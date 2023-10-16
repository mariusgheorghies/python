# IoCertManagerV1CertificateSpec

Desired state of the Certificate resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_output_formats** | [**list[IoCertManagerV1CertificateSpecAdditionalOutputFormats]**](IoCertManagerV1CertificateSpecAdditionalOutputFormats.md) | AdditionalOutputFormats defines extra output formats of the private key and signed certificate chain to be written to this Certificate&#39;s target Secret. This is an Alpha Feature and is only enabled with the &#x60;--feature-gates&#x3D;AdditionalCertificateOutputFormats&#x3D;true&#x60; option. | [optional] 
**common_name** | **str** | CommonName is a common name to be used on the Certificate. The CommonName should have a length of 64 characters or fewer to avoid generating invalid CSRs. This value is ignored by TLS kubernetes.clients when any subject alt name is set. This is x509 behaviour: https://tools.ietf.org/html/rfc6125#section-6.4.4 | [optional] 
**dns_names** | **list[str]** | DNSNames is a list of DNS subjectAltNames to be set on the Certificate. | [optional] 
**duration** | **str** | The requested &#39;duration&#39; (i.e. lifetime) of the Certificate. This option may be ignored/overridden by some issuer types. If unset this defaults to 90 days. Certificate will be renewed either 2/3 through its duration or &#x60;renewBefore&#x60; period before its expiry, whichever is later. Minimum accepted duration is 1 hour. Value must be in units accepted by Go time.ParseDuration https://golang.org/pkg/time/#ParseDuration | [optional] 
**email_addresses** | **list[str]** | EmailAddresses is a list of email subjectAltNames to be set on the Certificate. | [optional] 
**encode_usages_in_request** | **bool** | EncodeUsagesInRequest controls whether key usages should be present in the CertificateRequest | [optional] 
**ip_addresses** | **list[str]** | IPAddresses is a list of IP address subjectAltNames to be set on the Certificate. | [optional] 
**is_ca** | **bool** | IsCA will mark this Certificate as valid for certificate signing. This will automatically add the &#x60;cert sign&#x60; usage to the list of &#x60;usages&#x60;. | [optional] 
**issuer_ref** | [**IoCertManagerV1CertificateSpecIssuerRef**](IoCertManagerV1CertificateSpecIssuerRef.md) |  | 
**keystores** | [**IoCertManagerV1CertificateSpecKeystores**](IoCertManagerV1CertificateSpecKeystores.md) |  | [optional] 
**private_key** | [**IoCertManagerV1CertificateSpecPrivateKey**](IoCertManagerV1CertificateSpecPrivateKey.md) |  | [optional] 
**renew_before** | **str** | How long before the currently issued certificate&#39;s expiry cert-manager should renew the certificate. The default is 2/3 of the issued certificate&#39;s duration. Minimum accepted value is 5 minutes. Value must be in units accepted by Go time.ParseDuration https://golang.org/pkg/time/#ParseDuration | [optional] 
**revision_history_limit** | **int** | revisionHistoryLimit is the maximum number of CertificateRequest revisions that are maintained in the Certificate&#39;s history. Each revision represents a single &#x60;CertificateRequest&#x60; created by this Certificate, either when it was created, renewed, or Spec was changed. Revisions will be removed by oldest first if the number of revisions exceeds this number. If set, revisionHistoryLimit must be a value of &#x60;1&#x60; or greater. If unset (&#x60;nil&#x60;), revisions will not be garbage collected. Default value is &#x60;nil&#x60;. | [optional] 
**secret_name** | **str** | SecretName is the name of the secret resource that will be automatically created and managed by this Certificate resource. It will be populated with a private key and certificate, signed by the denoted issuer. | 
**secret_template** | [**IoCertManagerV1CertificateSpecSecretTemplate**](IoCertManagerV1CertificateSpecSecretTemplate.md) |  | [optional] 
**subject** | [**IoCertManagerV1CertificateSpecSubject**](IoCertManagerV1CertificateSpecSubject.md) |  | [optional] 
**uris** | **list[str]** | URIs is a list of URI subjectAltNames to be set on the Certificate. | [optional] 
**usages** | **list[str]** | Usages is the set of x509 usages that are requested for the certificate. Defaults to &#x60;digital signature&#x60; and &#x60;key encipherment&#x60; if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


