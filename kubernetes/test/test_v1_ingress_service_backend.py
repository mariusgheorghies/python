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
from kubernetes.client.models.v1_ingress_service_backend import V1IngressServiceBackend  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1IngressServiceBackend(unittest.TestCase):
    """V1IngressServiceBackend unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1IngressServiceBackend
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_ingress_service_backend.V1IngressServiceBackend()  # noqa: E501
        if include_optional :
            return V1IngressServiceBackend(
                name = '0', 
                port = kubernetes.client.models.v1/service_backend_port.v1.ServiceBackendPort(
                    name = '0', 
                    number = 56, )
            )
        else :
            return V1IngressServiceBackend(
                name = '0',
        )

    def testV1IngressServiceBackend(self):
        """Test V1IngressServiceBackend"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
