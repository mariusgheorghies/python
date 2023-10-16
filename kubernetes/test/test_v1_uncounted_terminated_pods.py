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
from kubernetes.client.models.v1_uncounted_terminated_pods import V1UncountedTerminatedPods  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1UncountedTerminatedPods(unittest.TestCase):
    """V1UncountedTerminatedPods unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1UncountedTerminatedPods
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_uncounted_terminated_pods.V1UncountedTerminatedPods()  # noqa: E501
        if include_optional :
            return V1UncountedTerminatedPods(
                failed = [
                    '0'
                    ], 
                succeeded = [
                    '0'
                    ]
            )
        else :
            return V1UncountedTerminatedPods(
        )

    def testV1UncountedTerminatedPods(self):
        """Test V1UncountedTerminatedPods"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
