# IoArgoprojV1alpha1AppProjectSpecRoles

ProjectRole represents a role that has access to a project
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description is a description of the role | [optional] 
**groups** | **list[str]** | Groups are a list of OIDC group claims bound to this role | [optional] 
**jwt_tokens** | [**list[IoArgoprojV1alpha1AppProjectSpecJwtTokens]**](IoArgoprojV1alpha1AppProjectSpecJwtTokens.md) | JWTTokens are a list of generated JWT tokens bound to this role | [optional] 
**name** | **str** | Name is a name for this role | 
**policies** | **list[str]** | Policies Stores a list of casbin formatted strings that define access policies for the role in the project | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


