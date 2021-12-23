# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecLogging

Logging specifies which EKS Cluster logs should be enabled. Entries for each of the enabled logs will be sent to CloudWatch
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server** | **bool** | APIServer indicates if the Kubernetes API Server log (kube-apiserver) shoulkd be enabled | 
**audit** | **bool** | Audit indicates if the Kubernetes API audit log should be enabled | 
**authenticator** | **bool** | Authenticator indicates if the iam authenticator log should be enabled | 
**controller_manager** | **bool** | ControllerManager indicates if the controller manager (kube-controller-manager) log should be enabled | 
**scheduler** | **bool** | Scheduler indicates if the Kubernetes scheduler (kube-scheduler) log should be enabled | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


