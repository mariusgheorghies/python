# IoQuestdbCrdV1alpha1QuestDBSpec

QuestDBSpec defines the desired state of QuestDB
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_cidr** | **list[str]** | Defaults to an empty list, which allows external traffic from all sources. Otherwise, this sets the allowed CIDRs that traffic is allowed to flow to the database | [optional] 
**aws** | [**IoQuestdbCrdV1alpha1QuestDBSpecAws**](IoQuestdbCrdV1alpha1QuestDBSpecAws.md) |  | [optional] 
**config** | **str** | QuestDB config file contents (raw string data) | [optional] 
**container** | [**IoQuestdbCrdV1alpha1QuestDBSpecContainer**](IoQuestdbCrdV1alpha1QuestDBSpecContainer.md) |  | [optional] 
**ilp_auth** | [**IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth**](IoQuestdbCrdV1alpha1QuestDBSpecIlpAuth.md) |  | [optional] 
**maintenance_mode** | **bool** | If set to true, will prevent any additional controller reconciliation from happening. This should be used in cases where you need to make a manual change to a resource, or need to debug the QuestDB&#39;s current state | [optional] 
**stateful_set** | [**IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet**](IoQuestdbCrdV1alpha1QuestDBSpecStatefulSet.md) |  | [optional] 
**stopped** | **bool** | Whether the database is \&quot;paused\&quot; or not.  If true, all nodes, DNS records, and containers will be deleted, but the volume will still remain | [optional] 
**subdomain** | **str** | Desired subdomain to place the ILP, PSQL, and HTTPS DNS records under | [optional] 
**volume** | [**IoQuestdbCrdV1alpha1QuestDBSpecVolume**](IoQuestdbCrdV1alpha1QuestDBSpecVolume.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


