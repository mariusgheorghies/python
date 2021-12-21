# IoCertManagerAcmeV1alpha2ChallengeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authz_url** | **str** | AuthzURL is the URL to the ACME Authorization resource that this challenge is a part of. | 
**dns_name** | **str** | DNSName is the identifier that this challenge is for, e.g. example.com. If the requested DNSName is a &#39;wildcard&#39;, this field MUST be set to the non-wildcard domain, e.g. for &#x60;*.example.com&#x60;, it must be &#x60;example.com&#x60;. | 
**issuer_ref** | [**IoCertManagerAcmeV1alpha2ChallengeSpecIssuerRef**](IoCertManagerAcmeV1alpha2ChallengeSpecIssuerRef.md) |  | 
**key** | **str** | Key is the ACME challenge key for this challenge For HTTP01 challenges, this is the value that must be responded with to complete the HTTP01 challenge in the format: &#x60;&lt;private key JWK thumbprint&gt;.&lt;key from acme server for challenge&gt;&#x60;. For DNS01 challenges, this is the base64 encoded SHA256 sum of the &#x60;&lt;private key JWK thumbprint&gt;.&lt;key from acme server for challenge&gt;&#x60; text that must be set as the TXT record content. | 
**solver** | [**IoCertManagerAcmeV1alpha2ChallengeSpecSolver**](IoCertManagerAcmeV1alpha2ChallengeSpecSolver.md) |  | 
**token** | **str** | Token is the ACME challenge token for this challenge. This is the raw value returned from the ACME server. | 
**type** | **str** | Type is the type of ACME challenge this resource represents. One of \&quot;http-01\&quot; or \&quot;dns-01\&quot;. | 
**url** | **str** | URL is the URL of the ACME Challenge resource for this challenge. This can be used to lookup details about the status of this challenge. | 
**wildcard** | **bool** | Wildcard will be true if this challenge is for a wildcard identifier, for example &#39;*.example.com&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


