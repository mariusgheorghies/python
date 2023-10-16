# ComCoreosMonitoringV1AlertmanagerSpecSecurityContextCapabilities

The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **list[str]** | Added capabilities | [optional] 
**drop** | **list[str]** | Removed capabilities | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


