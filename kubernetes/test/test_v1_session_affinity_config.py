# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_session_affinity_config import V1SessionAffinityConfig  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1SessionAffinityConfig(unittest.TestCase):
    """V1SessionAffinityConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1SessionAffinityConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_session_affinity_config.V1SessionAffinityConfig()  # noqa: E501
        if include_optional :
            return V1SessionAffinityConfig(
                kubernetes.client_ip = kubernetes.client.models.v1/kubernetes.client_ip_config.v1.ClientIPConfig(
                    timeout_seconds = 56, )
            )
        else :
            return V1SessionAffinityConfig(
        )

    def testV1SessionAffinityConfig(self):
        """Test V1SessionAffinityConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
