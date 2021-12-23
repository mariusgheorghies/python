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
from kubernetes.client.models.v1_probe import V1Probe  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1Probe(unittest.TestCase):
    """V1Probe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Probe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_probe.V1Probe()  # noqa: E501
        if include_optional :
            return V1Probe(
                _exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                    command = [
                        '0'
                        ], ), 
                failure_threshold = 56, 
                http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                    host = '0', 
                    http_headers = [
                        kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                            name = '0', 
                            value = '0', )
                        ], 
                    path = '0', 
                    port = kubernetes.client.models.port.port(), 
                    scheme = '0', ), 
                initial_delay_seconds = 56, 
                period_seconds = 56, 
                success_threshold = 56, 
                tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                    host = '0', 
                    port = kubernetes.client.models.port.port(), ), 
                timeout_seconds = 56
            )
        else :
            return V1Probe(
        )

    def testV1Probe(self):
        """Test V1Probe"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
