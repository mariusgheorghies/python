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
from kubernetes.client.models.com_coreos_monitoring_v1_thanos_ruler_status import ComCoreosMonitoringV1ThanosRulerStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1ThanosRulerStatus(unittest.TestCase):
    """ComCoreosMonitoringV1ThanosRulerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1ThanosRulerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_thanos_ruler_status.ComCoreosMonitoringV1ThanosRulerStatus()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1ThanosRulerStatus(
                available_replicas = 56, 
                paused = True, 
                replicas = 56, 
                unavailable_replicas = 56, 
                updated_replicas = 56
            )
        else :
            return ComCoreosMonitoringV1ThanosRulerStatus(
                available_replicas = 56,
                paused = True,
                replicas = 56,
                unavailable_replicas = 56,
                updated_replicas = 56,
        )

    def testComCoreosMonitoringV1ThanosRulerStatus(self):
        """Test ComCoreosMonitoringV1ThanosRulerStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
