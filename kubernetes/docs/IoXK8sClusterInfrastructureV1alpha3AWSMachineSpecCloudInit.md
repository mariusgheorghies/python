# IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit

CloudInit defines options related to the bootstrapping systems where CloudInit is used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insecure_skip_secrets_manager** | **bool** | InsecureSkipSecretsManager, when set to true will not use AWS Secrets Manager or AWS Systems Manager Parameter Store to ensure privacy of userdata. By default, a cloud-init boothook shell script is prepended to download the userdata from Secrets Manager and additionally delete the secret. | [optional] 
**secret_count** | **int** | SecretCount is the number of secrets used to form the complete secret | [optional] 
**secret_prefix** | **str** | SecretPrefix is the prefix for the secret name. This is stored temporarily, and deleted when the machine registers as a node against the workload cluster. | [optional] 
**secure_secrets_backend** | **str** | SecureSecretsBackend, when set to parameter-store will utilize the AWS Systems Manager Parameter Storage to distribute secrets. By default or with the value of secrets-manager, will use AWS Secrets Manager instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


