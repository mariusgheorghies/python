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
from kubernetes.client.models.io_argoproj_v1alpha1_application_status_resources import IoArgoprojV1alpha1ApplicationStatusResources  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationStatusResources(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationStatusResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationStatusResources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_status_resources.IoArgoprojV1alpha1ApplicationStatusResources()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationStatusResources(
                group = '0', 
                health = kubernetes.client.models.io_argoproj_v1alpha1_application_status_health_1.io_argoproj_v1alpha1_Application_status_health_1(
                    message = '0', 
                    status = '0', ), 
                hook = True, 
                kind = '0', 
                name = '0', 
                namespace = '0', 
                requires_pruning = True, 
                status = '0', 
                sync_wave = 56, 
                version = '0'
            )
        else :
            return IoArgoprojV1alpha1ApplicationStatusResources(
        )

    def testIoArgoprojV1alpha1ApplicationStatusResources(self):
        """Test IoArgoprojV1alpha1ApplicationStatusResources"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
