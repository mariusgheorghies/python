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
from kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions import AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions(unittest.TestCase):
    """AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions.AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions()  # noqa: E501
        if include_optional :
            return AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions(
                key = '0', 
                operator = '0', 
                values = [
                    '0'
                    ]
            )
        else :
            return AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions(
                key = '0',
                operator = '0',
        )

    def testAwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions(self):
        """Test AwsK8sNetworkingV1alpha1PolicyEndpointSpecPodSelectorMatchExpressions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()