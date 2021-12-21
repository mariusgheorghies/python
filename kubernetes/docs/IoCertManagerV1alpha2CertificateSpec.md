# IoCertManagerV1alpha2CertificateSpec

Desired state of the Certificate resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | CommonName is a common name to be used on the Certificate. The CommonName should have a length of 64 characters or fewer to avoid generating invalid CSRs. This value is ignored by TLS kubernetes.clients when any subject alt name is set. This is x509 behaviour: https://tools.ietf.org/html/rfc6125#section-6.4.4 | [optional] 
**dns_names** | **list[str]** | DNSNames is a list of DNS subjectAltNames to be set on the Certificate. | [optional] 
**duration** | **str** | The requested &#39;duration&#39; (i.e. lifetime) of the Certificate. This option may be ignored/overridden by some issuer types. If unset this defaults to 90 days. Certificate will be renewed either 2/3 through its duration or &#x60;renewBefore&#x60; period before its expiry, whichever is later. Minimum accepted duration is 1 hour. Value must be in units accepted by Go time.ParseDuration https://golang.org/pkg/time/#ParseDuration | [optional] 
**email_sa_ns** | **list[str]** | EmailSANs is a list of email subjectAltNames to be set on the Certificate. | [optional] 
**encode_usages_in_request** | **bool** | EncodeUsagesInRequest controls whether key usages should be present in the CertificateRequest | [optional] 
**ip_addresses** | **list[str]** | IPAddresses is a list of IP address subjectAltNames to be set on the Certificate. | [optional] 
**is_ca** | **bool** | IsCA will mark this Certificate as valid for certificate signing. This will automatically add the &#x60;cert sign&#x60; usage to the list of &#x60;usages&#x60;. | [optional] 
**issuer_ref** | [**IoCertManagerV1CertificateSpecIssuerRef**](IoCertManagerV1CertificateSpecIssuerRef.md) |  | 
**key_algorithm** | **str** | KeyAlgorithm is the private key algorithm of the corresponding private key for this certificate. If provided, allowed values are either &#x60;rsa&#x60; or &#x60;ecdsa&#x60; If &#x60;keyAlgorithm&#x60; is specified and &#x60;keySize&#x60; is not provided, key size of 256 will be used for &#x60;ecdsa&#x60; key algorithm and key size of 2048 will be used for &#x60;rsa&#x60; key algorithm. | [optional] 
**key_encoding** | **str** | KeyEncoding is the private key cryptography standards (PKCS) for this certificate&#39;s private key to be encoded in. If provided, allowed values are &#x60;pkcs1&#x60; and &#x60;pkcs8&#x60; standing for PKCS#1 and PKCS#8, respectively. If KeyEncoding is not specified, then &#x60;pkcs1&#x60; will be used by default. | [optional] 
**key_size** | **int** | KeySize is the key bit size of the corresponding private key for this certificate. If &#x60;keyAlgorithm&#x60; is set to &#x60;rsa&#x60;, valid values are &#x60;2048&#x60;, &#x60;4096&#x60; or &#x60;8192&#x60;, and will default to &#x60;2048&#x60; if not specified. If &#x60;keyAlgorithm&#x60; is set to &#x60;ecdsa&#x60;, valid values are &#x60;256&#x60;, &#x60;384&#x60; or &#x60;521&#x60;, and will default to &#x60;256&#x60; if not specified. No other values are allowed. | [optional] 
**keystores** | [**IoCertManagerV1alpha2CertificateSpecKeystores**](IoCertManagerV1alpha2CertificateSpecKeystores.md) |  | [optional] 
**organization** | **list[str]** | Organization is a list of organizations to be used on the Certificate. | [optional] 
**private_key** | [**IoCertManagerV1alpha2CertificateSpecPrivateKey**](IoCertManagerV1alpha2CertificateSpecPrivateKey.md) |  | [optional] 
**renew_before** | **str** | How long before the currently issued certificate&#39;s expiry cert-manager should renew the certificate. The default is 2/3 of the issued certificate&#39;s duration. Minimum accepted value is 5 minutes. Value must be in units accepted by Go time.ParseDuration https://golang.org/pkg/time/#ParseDuration | [optional] 
**revision_history_limit** | **int** | revisionHistoryLimit is the maximum number of CertificateRequest revisions that are maintained in the Certificate&#39;s history. Each revision represents a single &#x60;CertificateRequest&#x60; created by this Certificate, either when it was created, renewed, or Spec was changed. Revisions will be removed by oldest first if the number of revisions exceeds this number. If set, revisionHistoryLimit must be a value of &#x60;1&#x60; or greater. If unset (&#x60;nil&#x60;), revisions will not be garbage collected. Default value is &#x60;nil&#x60;. | [optional] 
**secret_name** | **str** | SecretName is the name of the secret resource that will be automatically created and managed by this Certificate resource. It will be populated with a private key and certificate, signed by the denoted issuer. | 
**secret_template** | [**IoCertManagerV1CertificateSpecSecretTemplate**](IoCertManagerV1CertificateSpecSecretTemplate.md) |  | [optional] 
**subject** | [**IoCertManagerV1alpha2CertificateSpecSubject**](IoCertManagerV1alpha2CertificateSpecSubject.md) |  | [optional] 
**uri_sa_ns** | **list[str]** | URISANs is a list of URI subjectAltNames to be set on the Certificate. | [optional] 
**usages** | **list[str]** | Usages is the set of x509 usages that are requested for the certificate. Defaults to &#x60;digital signature&#x60; and &#x60;key encipherment&#x60; if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


