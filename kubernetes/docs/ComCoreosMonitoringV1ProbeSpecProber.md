# ComCoreosMonitoringV1ProbeSpecProber

Specification for the prober to use for probing targets. The prober.URL parameter is required. Targets cannot be probed if left empty.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to collect metrics from. Defaults to &#x60;/probe&#x60;. | [optional] 
**proxy_url** | **str** | Optional ProxyURL. | [optional] 
**scheme** | **str** | HTTP scheme to use for scraping. Defaults to &#x60;http&#x60;. | [optional] 
**url** | **str** | Mandatory URL of the prober. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


