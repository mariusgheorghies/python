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
from kubernetes.client.models.v1alpha1_priority_level_configuration_status import V1alpha1PriorityLevelConfigurationStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha1PriorityLevelConfigurationStatus(unittest.TestCase):
    """V1alpha1PriorityLevelConfigurationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1PriorityLevelConfigurationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha1_priority_level_configuration_status.V1alpha1PriorityLevelConfigurationStatus()  # noqa: E501
        if include_optional :
            return V1alpha1PriorityLevelConfigurationStatus(
                conditions = [
                    kubernetes.client.models.v1alpha1/priority_level_configuration_condition.v1alpha1.PriorityLevelConfigurationCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ]
            )
        else :
            return V1alpha1PriorityLevelConfigurationStatus(
        )

    def testV1alpha1PriorityLevelConfigurationStatus(self):
        """Test V1alpha1PriorityLevelConfigurationStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
