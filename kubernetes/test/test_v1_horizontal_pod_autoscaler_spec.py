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
from kubernetes.client.models.v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1HorizontalPodAutoscalerSpec(unittest.TestCase):
    """V1HorizontalPodAutoscalerSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1HorizontalPodAutoscalerSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_horizontal_pod_autoscaler_spec.V1HorizontalPodAutoscalerSpec()  # noqa: E501
        if include_optional :
            return V1HorizontalPodAutoscalerSpec(
                max_replicas = 56, 
                min_replicas = 56, 
                scale_target_ref = kubernetes.client.models.v1/cross_version_object_reference.v1.CrossVersionObjectReference(
                    api_version = '0', 
                    kind = '0', 
                    name = '0', ), 
                target_cpu_utilization_percentage = 56
            )
        else :
            return V1HorizontalPodAutoscalerSpec(
                max_replicas = 56,
                scale_target_ref = kubernetes.client.models.v1/cross_version_object_reference.v1.CrossVersionObjectReference(
                    api_version = '0', 
                    kind = '0', 
                    name = '0', ),
        )

    def testV1HorizontalPodAutoscalerSpec(self):
        """Test V1HorizontalPodAutoscalerSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
