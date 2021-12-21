# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_flow_schema_list import V1beta1FlowSchemaList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1FlowSchemaList(unittest.TestCase):
    """V1beta1FlowSchemaList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1FlowSchemaList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_flow_schema_list.V1beta1FlowSchemaList()  # noqa: E501
        if include_optional :
            return V1beta1FlowSchemaList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.v1beta1/flow_schema.v1beta1.FlowSchema(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.v1beta1/flow_schema_spec.v1beta1.FlowSchemaSpec(
                            distinguisher_method = kubernetes.client.models.v1beta1/flow_distinguisher_method.v1beta1.FlowDistinguisherMethod(
                                type = '0', ), 
                            matching_precedence = 56, 
                            priority_level_configuration = kubernetes.client.models.v1beta1/priority_level_configuration_reference.v1beta1.PriorityLevelConfigurationReference(
                                name = '0', ), 
                            rules = [
                                kubernetes.client.models.v1beta1/policy_rules_with_subjects.v1beta1.PolicyRulesWithSubjects(
                                    non_resource_rules = [
                                        kubernetes.client.models.v1beta1/non_resource_policy_rule.v1beta1.NonResourcePolicyRule(
                                            non_resource_ur_ls = [
                                                '0'
                                                ], 
                                            verbs = [
                                                '0'
                                                ], )
                                        ], 
                                    resource_rules = [
                                        kubernetes.client.models.v1beta1/resource_policy_rule.v1beta1.ResourcePolicyRule(
                                            api_groups = [
                                                '0'
                                                ], 
                                            cluster_scope = True, 
                                            namespaces = [
                                                '0'
                                                ], 
                                            resources = [
                                                '0'
                                                ], 
                                            verbs = [
                                                '0'
                                                ], )
                                        ], 
                                    subjects = [
                                        kubernetes.client.models.flowcontrol/v1beta1/subject.flowcontrol.v1beta1.Subject(
                                            group = kubernetes.client.models.v1beta1/group_subject.v1beta1.GroupSubject(
                                                name = '0', ), 
                                            kind = '0', 
                                            service_account = kubernetes.client.models.v1beta1/service_account_subject.v1beta1.ServiceAccountSubject(
                                                name = '0', 
                                                namespace = '0', ), 
                                            user = kubernetes.client.models.v1beta1/user_subject.v1beta1.UserSubject(
                                                name = '0', ), )
                                        ], )
                                ], ), 
                        status = kubernetes.client.models.v1beta1/flow_schema_status.v1beta1.FlowSchemaStatus(
                            conditions = [
                                kubernetes.client.models.v1beta1/flow_schema_condition.v1beta1.FlowSchemaCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    type = '0', )
                                ], ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V1beta1FlowSchemaList(
                items = [
                    kubernetes.client.models.v1beta1/flow_schema.v1beta1.FlowSchema(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.v1beta1/flow_schema_spec.v1beta1.FlowSchemaSpec(
                            distinguisher_method = kubernetes.client.models.v1beta1/flow_distinguisher_method.v1beta1.FlowDistinguisherMethod(
                                type = '0', ), 
                            matching_precedence = 56, 
                            priority_level_configuration = kubernetes.client.models.v1beta1/priority_level_configuration_reference.v1beta1.PriorityLevelConfigurationReference(
                                name = '0', ), 
                            rules = [
                                kubernetes.client.models.v1beta1/policy_rules_with_subjects.v1beta1.PolicyRulesWithSubjects(
                                    non_resource_rules = [
                                        kubernetes.client.models.v1beta1/non_resource_policy_rule.v1beta1.NonResourcePolicyRule(
                                            non_resource_ur_ls = [
                                                '0'
                                                ], 
                                            verbs = [
                                                '0'
                                                ], )
                                        ], 
                                    resource_rules = [
                                        kubernetes.client.models.v1beta1/resource_policy_rule.v1beta1.ResourcePolicyRule(
                                            api_groups = [
                                                '0'
                                                ], 
                                            cluster_scope = True, 
                                            namespaces = [
                                                '0'
                                                ], 
                                            resources = [
                                                '0'
                                                ], 
                                            verbs = [
                                                '0'
                                                ], )
                                        ], 
                                    subjects = [
                                        kubernetes.client.models.flowcontrol/v1beta1/subject.flowcontrol.v1beta1.Subject(
                                            group = kubernetes.client.models.v1beta1/group_subject.v1beta1.GroupSubject(
                                                name = '0', ), 
                                            kind = '0', 
                                            service_account = kubernetes.client.models.v1beta1/service_account_subject.v1beta1.ServiceAccountSubject(
                                                name = '0', 
                                                namespace = '0', ), 
                                            user = kubernetes.client.models.v1beta1/user_subject.v1beta1.UserSubject(
                                                name = '0', ), )
                                        ], )
                                ], ), 
                        status = kubernetes.client.models.v1beta1/flow_schema_status.v1beta1.FlowSchemaStatus(
                            conditions = [
                                kubernetes.client.models.v1beta1/flow_schema_condition.v1beta1.FlowSchemaCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    type = '0', )
                                ], ), )
                    ],
        )

    def testV1beta1FlowSchemaList(self):
        """Test V1beta1FlowSchemaList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
