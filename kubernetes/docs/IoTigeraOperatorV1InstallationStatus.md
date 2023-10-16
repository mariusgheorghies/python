# IoTigeraOperatorV1InstallationStatus

Most recently observed state for the Calico or Calico Enterprise installation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computed** | [**IoTigeraOperatorV1InstallationStatusComputed**](IoTigeraOperatorV1InstallationStatusComputed.md) |  | [optional] 
**image_set** | **str** | ImageSet is the name of the ImageSet being used, if there is an ImageSet that is being used. If an ImageSet is not being used then this will not be set. | [optional] 
**mtu** | **int** | MTU is the most recently observed value for pod network MTU. This may be an explicitly configured value, or based on Calico&#39;s native auto-detetion. | [optional] 
**variant** | **str** | Variant is the most recently observed installed variant - one of Calico or TigeraSecureEnterprise | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


