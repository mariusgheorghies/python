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
from kubernetes.client.models.v2beta2_hpa_scaling_rules import V2beta2HPAScalingRules  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2beta2HPAScalingRules(unittest.TestCase):
    """V2beta2HPAScalingRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta2HPAScalingRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2beta2_hpa_scaling_rules.V2beta2HPAScalingRules()  # noqa: E501
        if include_optional :
            return V2beta2HPAScalingRules(
                policies = [
                    kubernetes.client.models.v2beta2/hpa_scaling_policy.v2beta2.HPAScalingPolicy(
                        period_seconds = 56, 
                        type = '0', 
                        value = 56, )
                    ], 
                select_policy = '0', 
                stabilization_window_seconds = 56
            )
        else :
            return V2beta2HPAScalingRules(
        )

    def testV2beta2HPAScalingRules(self):
        """Test V2beta2HPAScalingRules"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
