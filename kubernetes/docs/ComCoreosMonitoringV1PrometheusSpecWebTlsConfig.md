# ComCoreosMonitoringV1PrometheusSpecWebTlsConfig

WebTLSConfig defines the TLS parameters for HTTPS.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | [**ComCoreosMonitoringV1PrometheusSpecWebTlsConfigCert**](ComCoreosMonitoringV1PrometheusSpecWebTlsConfigCert.md) |  | 
**cipher_suites** | **list[str]** | List of supported cipher suites for TLS versions up to TLS 1.2. If empty, Go default cipher suites are used. Available cipher suites are documented in the go documentation: https://golang.org/pkg/crypto/tls/#pkg-constants | [optional] 
**kubernetes.client_auth_type** | **str** | Server policy for kubernetes.client authentication. Maps to ClientAuth Policies. For more detail on kubernetes.clientAuth options: https://golang.org/pkg/crypto/tls/#ClientAuthType | [optional] 
**kubernetes.client_ca** | [**ComCoreosMonitoringV1PrometheusSpecWebTlsConfigClientCa**](ComCoreosMonitoringV1PrometheusSpecWebTlsConfigClientCa.md) |  | [optional] 
**curve_preferences** | **list[str]** | Elliptic curves that will be used in an ECDHE handshake, in preference order. Available curves are documented in the go documentation: https://golang.org/pkg/crypto/tls/#CurveID | [optional] 
**key_secret** | [**ComCoreosMonitoringV1PrometheusSpecWebTlsConfigKeySecret**](ComCoreosMonitoringV1PrometheusSpecWebTlsConfigKeySecret.md) |  | 
**max_version** | **str** | Maximum TLS version that is acceptable. Defaults to TLS13. | [optional] 
**min_version** | **str** | Minimum TLS version that is acceptable. Defaults to TLS12. | [optional] 
**prefer_server_cipher_suites** | **bool** | Controls whether the server selects the kubernetes.client&#39;s most preferred cipher suite, or the server&#39;s most preferred cipher suite. If true then the server&#39;s preference, as expressed in the order of elements in cipherSuites, is used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


