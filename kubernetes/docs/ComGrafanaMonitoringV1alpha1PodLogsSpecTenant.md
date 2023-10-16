# ComGrafanaMonitoringV1alpha1PodLogsSpecTenant

Tenant is an action stage that sets the tenant ID for the log entry picking it from a field in the extracted data map. If the field is missing, the default LogsClientSpec.tenantId will be used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Name from labels whose value should be set as tenant ID. Mutually exclusive with source and value. | [optional] 
**source** | **str** | Name from extracted data to use as the tenant ID. Mutually exclusive with label and value. | [optional] 
**value** | **str** | Value to use for the template ID. Useful when this stage is used within a conditional pipeline such as match. Mutually exclusive with label and source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


