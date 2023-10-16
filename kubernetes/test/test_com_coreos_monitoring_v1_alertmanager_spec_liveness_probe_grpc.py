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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_liveness_probe_grpc import ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_liveness_probe_grpc.ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc(
                port = 56, 
                service = '0'
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc(
                port = 56,
        )

    def testComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLivenessProbeGrpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
