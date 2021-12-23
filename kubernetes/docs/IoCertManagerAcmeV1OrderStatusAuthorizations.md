# IoCertManagerAcmeV1OrderStatusAuthorizations

ACMEAuthorization contains data returned from the ACME server on an authorization that must be completed in order validate a DNS name on an ACME Order resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenges** | [**list[IoCertManagerAcmeV1OrderStatusChallenges]**](IoCertManagerAcmeV1OrderStatusChallenges.md) | Challenges specifies the challenge types offered by the ACME server. One of these challenge types will be selected when validating the DNS name and an appropriate Challenge resource will be created to perform the ACME challenge process. | [optional] 
**identifier** | **str** | Identifier is the DNS name to be validated as part of this authorization | [optional] 
**initial_state** | **str** | InitialState is the initial state of the ACME authorization when first fetched from the ACME server. If an Authorization is already &#39;valid&#39;, the Order controller will not create a Challenge resource for the authorization. This will occur when working with an ACME server that enables &#39;authz reuse&#39; (such as Let&#39;s Encrypt&#39;s production endpoint). If not set and &#39;identifier&#39; is set, the state is assumed to be pending and a Challenge will be created. | [optional] 
**url** | **str** | URL is the URL of the Authorization that must be completed | 
**wildcard** | **bool** | Wildcard will be true if this authorization is for a wildcard DNS name. If this is true, the identifier will be the *non-wildcard* version of the DNS name. For example, if &#39;*.example.com&#39; is the DNS name being validated, this field will be &#39;true&#39; and the &#39;identifier&#39; field will be &#39;example.com&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


