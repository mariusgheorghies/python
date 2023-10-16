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
from kubernetes.client.models.v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1DaemonSetUpdateStrategy(unittest.TestCase):
    """V1DaemonSetUpdateStrategy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DaemonSetUpdateStrategy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_daemon_set_update_strategy.V1DaemonSetUpdateStrategy()  # noqa: E501
        if include_optional :
            return V1DaemonSetUpdateStrategy(
                rolling_update = kubernetes.client.models.v1/rolling_update_daemon_set.v1.RollingUpdateDaemonSet(
                    max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                type = 'OnDelete'
            )
        else :
            return V1DaemonSetUpdateStrategy(
        )

    def testV1DaemonSetUpdateStrategy(self):
        """Test V1DaemonSetUpdateStrategy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
