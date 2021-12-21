# IoCertManagerAcmeV1OrderSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | CommonName is the common name as specified on the DER encoded CSR. If specified, this value must also be present in &#x60;dnsNames&#x60; or &#x60;ipAddresses&#x60;. This field must match the corresponding field on the DER encoded CSR. | [optional] 
**dns_names** | **list[str]** | DNSNames is a list of DNS names that should be included as part of the Order validation process. This field must match the corresponding field on the DER encoded CSR. | [optional] 
**duration** | **str** | Duration is the duration for the not after date for the requested certificate. this is set on order creation as pe the ACME spec. | [optional] 
**ip_addresses** | **list[str]** | IPAddresses is a list of IP addresses that should be included as part of the Order validation process. This field must match the corresponding field on the DER encoded CSR. | [optional] 
**issuer_ref** | [**IoCertManagerAcmeV1OrderSpecIssuerRef**](IoCertManagerAcmeV1OrderSpecIssuerRef.md) |  | 
**request** | **str** | Certificate signing request bytes in DER encoding. This will be used when finalizing the order. This field must be set on the order. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


