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
from kubernetes.client.models.v1_pod_failure_policy import V1PodFailurePolicy  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1PodFailurePolicy(unittest.TestCase):
    """V1PodFailurePolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PodFailurePolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_pod_failure_policy.V1PodFailurePolicy()  # noqa: E501
        if include_optional :
            return V1PodFailurePolicy(
                rules = [
                    kubernetes.client.models.v1/pod_failure_policy_rule.v1.PodFailurePolicyRule(
                        action = 'Count', 
                        on_exit_codes = kubernetes.client.models.v1/pod_failure_policy_on_exit_codes_requirement.v1.PodFailurePolicyOnExitCodesRequirement(
                            container_name = '0', 
                            operator = 'In', 
                            values = [
                                56
                                ], ), 
                        on_pod_conditions = [
                            kubernetes.client.models.v1/pod_failure_policy_on_pod_conditions_pattern.v1.PodFailurePolicyOnPodConditionsPattern(
                                status = '0', 
                                type = '0', )
                            ], )
                    ]
            )
        else :
            return V1PodFailurePolicy(
                rules = [
                    kubernetes.client.models.v1/pod_failure_policy_rule.v1.PodFailurePolicyRule(
                        action = 'Count', 
                        on_exit_codes = kubernetes.client.models.v1/pod_failure_policy_on_exit_codes_requirement.v1.PodFailurePolicyOnExitCodesRequirement(
                            container_name = '0', 
                            operator = 'In', 
                            values = [
                                56
                                ], ), 
                        on_pod_conditions = [
                            kubernetes.client.models.v1/pod_failure_policy_on_pod_conditions_pattern.v1.PodFailurePolicyOnPodConditionsPattern(
                                status = '0', 
                                type = '0', )
                            ], )
                    ],
        )

    def testV1PodFailurePolicy(self):
        """Test V1PodFailurePolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
