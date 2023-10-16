# OrgProjectcalicoCrdV1BGPConfigurationSpecPrefixAdvertisements

PrefixAdvertisement configures advertisement properties for the specified CIDR.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | CIDR for which properties should be advertised. | [optional] 
**communities** | **list[str]** | Communities can be list of either community names already defined in &#x60;Specs.Communities&#x60; or community value of format &#x60;aa:nn&#x60; or &#x60;aa:nn:mm&#x60;. For standard community use &#x60;aa:nn&#x60; format, where &#x60;aa&#x60; and &#x60;nn&#x60; are 16 bit number. For large community use &#x60;aa:nn:mm&#x60; format, where &#x60;aa&#x60;, &#x60;nn&#x60; and &#x60;mm&#x60; are 32 bit number. Where,&#x60;aa&#x60; is an AS Number, &#x60;nn&#x60; and &#x60;mm&#x60; are per-AS identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


