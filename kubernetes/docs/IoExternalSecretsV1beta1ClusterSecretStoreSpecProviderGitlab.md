# IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderGitlab

Gitlab configures this store to sync secrets using Gitlab Variables provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGitlabAuth**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGitlabAuth.md) |  | 
**environment** | **str** | Environment environment_scope of gitlab CI/CD variables (Please see https://docs.gitlab.com/ee/ci/environments/#create-a-static-environment on how to create environments) | [optional] 
**group_i_ds** | **list[str]** | GroupIDs specify, which gitlab groups to pull secrets from. Group secrets are read from left to right followed by the project variables. | [optional] 
**inherit_from_groups** | **bool** | InheritFromGroups specifies whether parent groups should be discovered and checked for secrets. | [optional] 
**project_id** | **str** | ProjectID specifies a project where secrets are located. | [optional] 
**url** | **str** | URL configures the GitLab instance URL. Defaults to https://gitlab.com/. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


