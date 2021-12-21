# IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecJoinConfigurationDiscoveryBootstrapToken

BootstrapToken is used to set the options for bootstrap token based discovery BootstrapToken and File are mutually exclusive
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server_endpoint** | **str** | APIServerEndpoint is an IP or domain name to the API server from which info will be fetched. | [optional] 
**ca_cert_hashes** | **list[str]** | CACertHashes specifies a set of public key pins to verify when token-based discovery is used. The root CA found during discovery must match one of these values. Specifying an empty set disables root CA pinning, which can be unsafe. Each hash is specified as \&quot;&lt;type&gt;:&lt;value&gt;\&quot;, where the only currently supported type is \&quot;sha256\&quot;. This is a hex-encoded SHA-256 hash of the Subject Public Key Info (SPKI) object in DER-encoded ASN.1. These hashes can be calculated using, for example, OpenSSL: openssl x509 -pubkey -in ca.crt openssl rsa -pubin -outform der 2&gt;&amp;/dev/null | openssl dgst -sha256 -hex | [optional] 
**token** | **str** | Token is a token used to validate cluster information fetched from the control-plane. | 
**unsafe_skip_ca_verification** | **bool** | UnsafeSkipCAVerification allows token-based discovery without CA verification via CACertHashes. This can weaken the security of kubeadm since other nodes can impersonate the control-plane. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


