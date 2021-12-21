# IoCertManagerV1ClusterIssuerSpecAcme

ACME configures this issuer to communicate with a RFC8555 (ACME) server to obtain signed x509 certificates.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_account_key_generation** | **bool** | Enables or disables generating a new ACME account key. If true, the Issuer resource will *not* request a new account but will expect the account key to be supplied via an existing secret. If false, the cert-manager system will generate a new ACME account key for the Issuer. Defaults to false. | [optional] 
**email** | **str** | Email is the email address to be associated with the ACME account. This field is optional, but it is strongly recommended to be set. It will be used to contact you in case of issues with your account or certificates, including expiry notification emails. This field may be updated after the account is initially registered. | [optional] 
**enable_duration_feature** | **bool** | Enables requesting a Not After date on certificates that matches the duration of the certificate. This is not supported by all ACME servers like Let&#39;s Encrypt. If set to true when the ACME server does not support it it will create an error on the Order. Defaults to false. | [optional] 
**external_account_binding** | [**IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding**](IoCertManagerV1ClusterIssuerSpecAcmeExternalAccountBinding.md) |  | [optional] 
**preferred_chain** | **str** | PreferredChain is the chain to use if the ACME server outputs multiple. PreferredChain is no guarantee that this one gets delivered by the ACME endpoint. For example, for Let&#39;s Encrypt&#39;s DST crosssign you would use: \&quot;DST Root CA X3\&quot; or \&quot;ISRG Root X1\&quot; for the newer Let&#39;s Encrypt root CA. This value picks the first certificate bundle in the ACME alternative chains that has a certificate with this value as its issuer&#39;s CN | [optional] 
**private_key_secret_ref** | [**IoCertManagerV1ClusterIssuerSpecAcmePrivateKeySecretRef**](IoCertManagerV1ClusterIssuerSpecAcmePrivateKeySecretRef.md) |  | 
**server** | **str** | Server is the URL used to access the ACME server&#39;s &#39;directory&#39; endpoint. For example, for Let&#39;s Encrypt&#39;s staging endpoint, you would use: \&quot;https://acme-staging-v02.api.letsencrypt.org/directory\&quot;. Only ACME v2 endpoints (i.e. RFC 8555) are supported. | 
**skip_tls_verify** | **bool** | Enables or disables validation of the ACME server TLS certificate. If true, requests to the ACME server will not have their TLS certificate validated (i.e. insecure connections will be allowed). Only enable this option in development environments. The cert-manager system installed roots will be used to verify connections to the ACME server if this is false. Defaults to false. | [optional] 
**solvers** | [**list[IoCertManagerV1ClusterIssuerSpecAcmeSolvers]**](IoCertManagerV1ClusterIssuerSpecAcmeSolvers.md) | Solvers is a list of challenge solvers that will be used to solve ACME challenges for the matching domains. Solver configurations must be provided in order to obtain certificates from an ACME server. For more information, see: https://cert-manager.io/docs/configuration/acme/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


