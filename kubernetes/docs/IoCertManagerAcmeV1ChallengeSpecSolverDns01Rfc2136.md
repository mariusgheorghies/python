# IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136

Use RFC2136 (\"Dynamic Updates in the Domain Name System\") (https://datatracker.ietf.org/doc/rfc2136/) to manage DNS01 challenge records.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nameserver** | **str** | The IP address or hostname of an authoritative DNS server supporting RFC2136 in the form host:port. If the host is an IPv6 address it must be enclosed in square brackets (e.g [2001:db8::1]) ; port is optional. This field is required. | 
**tsig_algorithm** | **str** | The TSIG Algorithm configured in the DNS supporting RFC2136. Used only when &#x60;&#x60;tsigSecretSecretRef&#x60;&#x60; and &#x60;&#x60;tsigKeyName&#x60;&#x60; are defined. Supported values are (case-insensitive): &#x60;&#x60;HMACMD5&#x60;&#x60; (default), &#x60;&#x60;HMACSHA1&#x60;&#x60;, &#x60;&#x60;HMACSHA256&#x60;&#x60; or &#x60;&#x60;HMACSHA512&#x60;&#x60;. | [optional] 
**tsig_key_name** | **str** | The TSIG Key name configured in the DNS. If &#x60;&#x60;tsigSecretSecretRef&#x60;&#x60; is defined, this field is required. | [optional] 
**tsig_secret_secret_ref** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


