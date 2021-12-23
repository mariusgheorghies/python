# IoCertManagerAcmeV1alpha2ChallengeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**presented** | **bool** | Presented will be set to true if the challenge values for this challenge are currently &#39;presented&#39;. This *does not* imply the self check is passing. Only that the values have been &#39;submitted&#39; for the appropriate challenge mechanism (i.e. the DNS01 TXT record has been presented, or the HTTP01 configuration has been configured). | [optional] 
**processing** | **bool** | Processing is used to denote whether this challenge should be processed or not. This field will only be set to true by the &#39;scheduling&#39; component. It will only be set to false by the &#39;challenges&#39; controller, after the challenge has reached a final state or timed out. If this field is set to false, the challenge controller will not take any more action. | [optional] 
**reason** | **str** | Reason contains human readable information on why the Challenge is in the current state. | [optional] 
**state** | **str** | State contains the current &#39;state&#39; of the challenge. If not set, the state of the challenge is unknown. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


