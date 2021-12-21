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
from kubernetes.client.models.v1alpha1_priority_level_configuration_spec import V1alpha1PriorityLevelConfigurationSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha1PriorityLevelConfigurationSpec(unittest.TestCase):
    """V1alpha1PriorityLevelConfigurationSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1PriorityLevelConfigurationSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha1_priority_level_configuration_spec.V1alpha1PriorityLevelConfigurationSpec()  # noqa: E501
        if include_optional :
            return V1alpha1PriorityLevelConfigurationSpec(
                limited = kubernetes.client.models.v1alpha1/limited_priority_level_configuration.v1alpha1.LimitedPriorityLevelConfiguration(
                    assured_concurrency_shares = 56, 
                    limit_response = kubernetes.client.models.v1alpha1/limit_response.v1alpha1.LimitResponse(
                        queuing = kubernetes.client.models.v1alpha1/queuing_configuration.v1alpha1.QueuingConfiguration(
                            hand_size = 56, 
                            queue_length_limit = 56, 
                            queues = 56, ), 
                        type = '0', ), ), 
                type = '0'
            )
        else :
            return V1alpha1PriorityLevelConfigurationSpec(
                type = '0',
        )

    def testV1alpha1PriorityLevelConfigurationSpec(self):
        """Test V1alpha1PriorityLevelConfigurationSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
