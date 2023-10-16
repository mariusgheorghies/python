# IoCertManagerAcmeV1OrderStatusChallenges

Challenge specifies a challenge offered by the ACME server for an Order. An appropriate Challenge resource can be created to perform the ACME challenge process.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token is the token that must be presented for this challenge. This is used to compute the &#39;key&#39; that must also be presented. | 
**type** | **str** | Type is the type of challenge being offered, e.g. &#39;http-01&#39;, &#39;dns-01&#39;, &#39;tls-sni-01&#39;, etc. This is the raw value retrieved from the ACME server. Only &#39;http-01&#39; and &#39;dns-01&#39; are supported by cert-manager, other values will be ignored. | 
**url** | **str** | URL is the URL of this challenge. It can be used to retrieve additional metadata about the Challenge from the ACME server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


