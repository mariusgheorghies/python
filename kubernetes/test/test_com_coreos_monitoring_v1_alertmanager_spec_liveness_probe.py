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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_liveness_probe import ComCoreosMonitoringV1AlertmanagerSpecLivenessProbe  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecLivenessProbe(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecLivenessProbe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLivenessProbe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_liveness_probe.ComCoreosMonitoringV1AlertmanagerSpecLivenessProbe()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecLivenessProbe(
                _exec = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_exec.com_coreos_monitoring_v1_Alertmanager_spec_lifecycle_postStart_exec(
                    command = [
                        '0'
                        ], ), 
                failure_threshold = 56, 
                grpc = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_liveness_probe_grpc.com_coreos_monitoring_v1_Alertmanager_spec_livenessProbe_grpc(
                    port = 56, 
                    service = '0', ), 
                http_get = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_http_get.com_coreos_monitoring_v1_Alertmanager_spec_lifecycle_postStart_httpGet(
                    host = '0', 
                    http_headers = [
                        kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_http_get_http_headers.com_coreos_monitoring_v1_Alertmanager_spec_lifecycle_postStart_httpGet_httpHeaders(
                            name = '0', 
                            value = '0', )
                        ], 
                    path = '0', 
                    port = kubernetes.client.models.port.port(), 
                    scheme = '0', ), 
                initial_delay_seconds = 56, 
                period_seconds = 56, 
                success_threshold = 56, 
                tcp_socket = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_liveness_probe_tcp_socket.com_coreos_monitoring_v1_Alertmanager_spec_livenessProbe_tcpSocket(
                    host = '0', 
                    port = kubernetes.client.models.port.port(), ), 
                termination_grace_period_seconds = 56, 
                timeout_seconds = 56
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecLivenessProbe(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecLivenessProbe(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLivenessProbe"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
