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
from kubernetes.client.models.extensions_v1beta1_ingress_status import ExtensionsV1beta1IngressStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestExtensionsV1beta1IngressStatus(unittest.TestCase):
    """ExtensionsV1beta1IngressStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1IngressStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.extensions_v1beta1_ingress_status.ExtensionsV1beta1IngressStatus()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1IngressStatus(
                load_balancer = kubernetes.client.models.v1/load_balancer_status.v1.LoadBalancerStatus(
                    ingress = [
                        kubernetes.client.models.v1/load_balancer_ingress.v1.LoadBalancerIngress(
                            hostname = '0', 
                            ip = '0', 
                            ports = [
                                kubernetes.client.models.v1/port_status.v1.PortStatus(
                                    error = '0', 
                                    port = 56, 
                                    protocol = '0', )
                                ], )
                        ], )
            )
        else :
            return ExtensionsV1beta1IngressStatus(
        )

    def testExtensionsV1beta1IngressStatus(self):
        """Test ExtensionsV1beta1IngressStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
