# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1alpha1_priority_level_configuration import V1alpha1PriorityLevelConfiguration  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha1PriorityLevelConfiguration(unittest.TestCase):
    """V1alpha1PriorityLevelConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1PriorityLevelConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha1_priority_level_configuration.V1alpha1PriorityLevelConfiguration()  # noqa: E501
        if include_optional :
            return V1alpha1PriorityLevelConfiguration(
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
                spec = kubernetes.client.models.v1alpha1/priority_level_configuration_spec.v1alpha1.PriorityLevelConfigurationSpec(
                    limited = kubernetes.client.models.v1alpha1/limited_priority_level_configuration.v1alpha1.LimitedPriorityLevelConfiguration(
                        assured_concurrency_shares = 56, 
                        limit_response = kubernetes.client.models.v1alpha1/limit_response.v1alpha1.LimitResponse(
                            queuing = kubernetes.client.models.v1alpha1/queuing_configuration.v1alpha1.QueuingConfiguration(
                                hand_size = 56, 
                                queue_length_limit = 56, 
                                queues = 56, ), 
                            type = '0', ), ), 
                    type = '0', ), 
                status = kubernetes.client.models.v1alpha1/priority_level_configuration_status.v1alpha1.PriorityLevelConfigurationStatus(
                    conditions = [
                        kubernetes.client.models.v1alpha1/priority_level_configuration_condition.v1alpha1.PriorityLevelConfigurationCondition(
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], )
            )
        else :
            return V1alpha1PriorityLevelConfiguration(
        )

    def testV1alpha1PriorityLevelConfiguration(self):
        """Test V1alpha1PriorityLevelConfiguration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
