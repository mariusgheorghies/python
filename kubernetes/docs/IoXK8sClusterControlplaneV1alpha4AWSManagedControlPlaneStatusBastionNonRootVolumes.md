# IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionNonRootVolumes

Volume encapsulates the configuration options for the storage device
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Device name | [optional] 
**encrypted** | **bool** | Encrypted is whether the volume should be encrypted or not. | [optional] 
**encryption_key** | **str** | EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller. | [optional] 
**iops** | **int** | IOPS is the number of IOPS requested for the disk. Not applicable to all types. | [optional] 
**size** | **int** | Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater). | 
**throughput** | **int** | Throughput to provision in MiB/s supported for the volume type. Not applicable to all types. | [optional] 
**type** | **str** | Type is the type of the volume (e.g. gp2, io1, etc...). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


