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
from kubernetes.client.models.v1_load_balancer_ingress import V1LoadBalancerIngress  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1LoadBalancerIngress(unittest.TestCase):
    """V1LoadBalancerIngress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1LoadBalancerIngress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_load_balancer_ingress.V1LoadBalancerIngress()  # noqa: E501
        if include_optional :
            return V1LoadBalancerIngress(
                hostname = '0', 
                ip = '0', 
                ports = [
                    kubernetes.client.models.v1/port_status.v1.PortStatus(
                        error = '0', 
                        port = 56, 
                        protocol = '0', )
                    ]
            )
        else :
            return V1LoadBalancerIngress(
        )

    def testV1LoadBalancerIngress(self):
        """Test V1LoadBalancerIngress"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
