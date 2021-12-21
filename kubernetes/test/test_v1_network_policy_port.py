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
from kubernetes.client.models.v1_network_policy_port import V1NetworkPolicyPort  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1NetworkPolicyPort(unittest.TestCase):
    """V1NetworkPolicyPort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NetworkPolicyPort
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_network_policy_port.V1NetworkPolicyPort()  # noqa: E501
        if include_optional :
            return V1NetworkPolicyPort(
                port = kubernetes.client.models.port.port(), 
                protocol = '0'
            )
        else :
            return V1NetworkPolicyPort(
        )

    def testV1NetworkPolicyPort(self):
        """Test V1NetworkPolicyPort"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
