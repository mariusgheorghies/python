# ComCoreosMonitoringV1AlertmanagerSpecSecurityContext1SeLinuxOptions

The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Level is SELinux level label that applies to the container. | [optional] 
**role** | **str** | Role is a SELinux role label that applies to the container. | [optional] 
**type** | **str** | Type is a SELinux type label that applies to the container. | [optional] 
**user** | **str** | User is a SELinux user label that applies to the container. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


