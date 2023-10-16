# IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize

Kustomize holds kustomize specific options
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_annotations** | **dict(str, str)** | CommonAnnotations is a list of additional annotations to add to rendered manifests | [optional] 
**common_annotations_envsubst** | **bool** | CommonAnnotationsEnvsubst specifies whether to apply env variables substitution for annotation values | [optional] 
**common_labels** | **dict(str, str)** | CommonLabels is a list of additional labels to add to rendered manifests | [optional] 
**force_common_annotations** | **bool** | ForceCommonAnnotations specifies whether to force applying common annotations to resources for Kustomize apps | [optional] 
**force_common_labels** | **bool** | ForceCommonLabels specifies whether to force applying common labels to resources for Kustomize apps | [optional] 
**images** | **list[str]** | Images is a list of Kustomize image override specifications | [optional] 
**name_prefix** | **str** | NamePrefix is a prefix appended to resources for Kustomize apps | [optional] 
**name_suffix** | **str** | NameSuffix is a suffix appended to resources for Kustomize apps | [optional] 
**namespace** | **str** | Namespace sets the namespace that Kustomize adds to all resources | [optional] 
**replicas** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomizeReplicas]**](IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomizeReplicas.md) | Replicas is a list of Kustomize Replicas override specifications | [optional] 
**version** | **str** | Version controls which version of Kustomize to use for rendering manifests | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


