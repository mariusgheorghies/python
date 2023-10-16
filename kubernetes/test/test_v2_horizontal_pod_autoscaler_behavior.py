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
from kubernetes.client.models.v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2HorizontalPodAutoscalerBehavior(unittest.TestCase):
    """V2HorizontalPodAutoscalerBehavior unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2HorizontalPodAutoscalerBehavior
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2_horizontal_pod_autoscaler_behavior.V2HorizontalPodAutoscalerBehavior()  # noqa: E501
        if include_optional :
            return V2HorizontalPodAutoscalerBehavior(
                scale_down = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                    policies = [
                        kubernetes.client.models.v2/hpa_scaling_policy.v2.HPAScalingPolicy(
                            period_seconds = 56, 
                            type = '0', 
                            value = 56, )
                        ], 
                    select_policy = '0', 
                    stabilization_window_seconds = 56, ), 
                scale_up = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                    policies = [
                        kubernetes.client.models.v2/hpa_scaling_policy.v2.HPAScalingPolicy(
                            period_seconds = 56, 
                            type = '0', 
                            value = 56, )
                        ], 
                    select_policy = '0', 
                    stabilization_window_seconds = 56, )
            )
        else :
            return V2HorizontalPodAutoscalerBehavior(
        )

    def testV2HorizontalPodAutoscalerBehavior(self):
        """Test V2HorizontalPodAutoscalerBehavior"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
