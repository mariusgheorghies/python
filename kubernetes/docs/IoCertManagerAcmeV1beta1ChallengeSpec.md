# IoCertManagerAcmeV1beta1ChallengeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** | The URL to the ACME Authorization resource that this challenge is a part of. | 
**dns_name** | **str** | dnsName is the identifier that this challenge is for, e.g. example.com. If the requested DNSName is a &#39;wildcard&#39;, this field MUST be set to the non-wildcard domain, e.g. for &#x60;*.example.com&#x60;, it must be &#x60;example.com&#x60;. | 
**issuer_ref** | [**IoCertManagerAcmeV1ChallengeSpecIssuerRef**](IoCertManagerAcmeV1ChallengeSpecIssuerRef.md) |  | 
**key** | **str** | The ACME challenge key for this challenge For HTTP01 challenges, this is the value that must be responded with to complete the HTTP01 challenge in the format: &#x60;&lt;private key JWK thumbprint&gt;.&lt;key from acme server for challenge&gt;&#x60;. For DNS01 challenges, this is the base64 encoded SHA256 sum of the &#x60;&lt;private key JWK thumbprint&gt;.&lt;key from acme server for challenge&gt;&#x60; text that must be set as the TXT record content. | 
**solver** | [**IoCertManagerAcmeV1beta1ChallengeSpecSolver**](IoCertManagerAcmeV1beta1ChallengeSpecSolver.md) |  | 
**token** | **str** | The ACME challenge token for this challenge. This is the raw value returned from the ACME server. | 
**type** | **str** | The type of ACME challenge this resource represents. One of \&quot;HTTP-01\&quot; or \&quot;DNS-01\&quot;. | 
**url** | **str** | The URL of the ACME Challenge resource for this challenge. This can be used to lookup details about the status of this challenge. | 
**wildcard** | **bool** | wildcard will be true if this challenge is for a wildcard identifier, for example &#39;*.example.com&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


