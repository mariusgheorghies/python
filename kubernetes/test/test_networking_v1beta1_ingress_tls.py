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
from kubernetes.client.models.networking_v1beta1_ingress_tls import NetworkingV1beta1IngressTLS  # noqa: E501
from kubernetes.client.rest import ApiException

class TestNetworkingV1beta1IngressTLS(unittest.TestCase):
    """NetworkingV1beta1IngressTLS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkingV1beta1IngressTLS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.networking_v1beta1_ingress_tls.NetworkingV1beta1IngressTLS()  # noqa: E501
        if include_optional :
            return NetworkingV1beta1IngressTLS(
                hosts = [
                    '0'
                    ], 
                secret_name = '0'
            )
        else :
            return NetworkingV1beta1IngressTLS(
        )

    def testNetworkingV1beta1IngressTLS(self):
        """Test NetworkingV1beta1IngressTLS"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
