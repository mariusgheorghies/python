# IoCertManagerV1ClusterIssuerSpecVenafi

Venafi configures this issuer to sign certificates using a Venafi TPP or Venafi Cloud policy zone.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud** | [**IoCertManagerV1ClusterIssuerSpecVenafiCloud**](IoCertManagerV1ClusterIssuerSpecVenafiCloud.md) |  | [optional] 
**tpp** | [**IoCertManagerV1ClusterIssuerSpecVenafiTpp**](IoCertManagerV1ClusterIssuerSpecVenafiTpp.md) |  | [optional] 
**zone** | **str** | Zone is the Venafi Policy Zone to use for this issuer. All requests made to the Venafi platform will be restricted by the named zone policy. This field is required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


