# IoCertManagerV1ClusterIssuerSpecVenafiTpp

TPP specifies Trust Protection Platform configuration settings. Only one of TPP or Cloud may be specified.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_bundle** | **str** | CABundle is a PEM encoded TLS certificate to use to verify connections to the TPP instance. If specified, system roots will not be used and the issuing CA for the TPP instance must be verifiable using the provided root. If not specified, the connection will be verified using the cert-manager system root certificates. | [optional] 
**credentials_ref** | [**IoCertManagerV1ClusterIssuerSpecVenafiTppCredentialsRef**](IoCertManagerV1ClusterIssuerSpecVenafiTppCredentialsRef.md) |  | 
**url** | **str** | URL is the base URL for the vedsdk endpoint of the Venafi TPP instance, for example: \&quot;https://tpp.example.com/vedsdk\&quot;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


