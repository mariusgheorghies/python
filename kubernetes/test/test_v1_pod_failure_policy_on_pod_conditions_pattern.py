# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_pod_failure_policy_on_pod_conditions_pattern import V1PodFailurePolicyOnPodConditionsPattern  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1PodFailurePolicyOnPodConditionsPattern(unittest.TestCase):
    """V1PodFailurePolicyOnPodConditionsPattern unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PodFailurePolicyOnPodConditionsPattern
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_pod_failure_policy_on_pod_conditions_pattern.V1PodFailurePolicyOnPodConditionsPattern()  # noqa: E501
        if include_optional :
            return V1PodFailurePolicyOnPodConditionsPattern(
                status = '0', 
                type = '0'
            )
        else :
            return V1PodFailurePolicyOnPodConditionsPattern(
                status = '0',
                type = '0',
        )

    def testV1PodFailurePolicyOnPodConditionsPattern(self):
        """Test V1PodFailurePolicyOnPodConditionsPattern"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
