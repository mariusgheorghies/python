# IoCertManagerAcmeV1OrderStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizations** | [**list[IoCertManagerAcmeV1OrderStatusAuthorizations]**](IoCertManagerAcmeV1OrderStatusAuthorizations.md) | Authorizations contains data returned from the ACME server on what authorizations must be completed in order to validate the DNS names specified on the Order. | [optional] 
**certificate** | **str** | Certificate is a copy of the PEM encoded certificate for this Order. This field will be populated after the order has been successfully finalized with the ACME server, and the order has transitioned to the &#39;valid&#39; state. | [optional] 
**failure_time** | **datetime** | FailureTime stores the time that this order failed. This is used to influence garbage collection and back-off. | [optional] 
**finalize_url** | **str** | FinalizeURL of the Order. This is used to obtain certificates for this order once it has been completed. | [optional] 
**reason** | **str** | Reason optionally provides more information about a why the order is in the current state. | [optional] 
**state** | **str** | State contains the current state of this Order resource. States &#39;success&#39; and &#39;expired&#39; are &#39;final&#39; | [optional] 
**url** | **str** | URL of the Order. This will initially be empty when the resource is first created. The Order controller will populate this field when the Order is first processed. This field will be immutable after it is initially set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


