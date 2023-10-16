# ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc

GRPC specifies an action involving a GRPC port. This is an alpha field and requires enabling GRPCContainerProbe feature gate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Port number of the gRPC service. Number must be in the range 1 to 65535. | 
**service** | **str** | Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).   If this is not specified, the default behavior is defined by gRPC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

