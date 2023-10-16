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
from kubernetes.client.models.v1_endpoint_conditions import V1EndpointConditions  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1EndpointConditions(unittest.TestCase):
    """V1EndpointConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1EndpointConditions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_endpoint_conditions.V1EndpointConditions()  # noqa: E501
        if include_optional :
            return V1EndpointConditions(
                ready = True, 
                serving = True, 
                terminating = True
            )
        else :
            return V1EndpointConditions(
        )

    def testV1EndpointConditions(self):
        """Test V1EndpointConditions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
