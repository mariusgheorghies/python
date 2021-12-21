# V1alpha1DNSEndpointSpecEndpoints

Endpoint is a high-level way of a connection between a service and an IP
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_name** | **str** | The hostname of the DNS record | [optional] 
**labels** | **dict(str, str)** | Labels stores labels defined for the Endpoint | [optional] 
**provider_specific** | [**list[V1alpha1DNSEndpointSpecProviderSpecific]**](V1alpha1DNSEndpointSpecProviderSpecific.md) | ProviderSpecific stores provider specific config | [optional] 
**record_ttl** | **int** | TTL for the record | [optional] 
**record_type** | **str** | RecordType type of record, e.g. CNAME, A, SRV, TXT etc | [optional] 
**set_identifier** | **str** | Identifier to distinguish multiple records with the same name and type (e.g. Route53 records with routing policies other than &#39;simple&#39;) | [optional] 
**targets** | **list[str]** | The targets the DNS record points to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


