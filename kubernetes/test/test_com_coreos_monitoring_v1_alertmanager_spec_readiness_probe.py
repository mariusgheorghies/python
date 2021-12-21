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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_readiness_probe import ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecReadinessProbe(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_readiness_probe.ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe(
                _exec = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_exec.com_coreos_monitoring_v1_Alertmanager_spec_lifecycle_postStart_exec(
                    command = [
                        '0'
                        ], ), 
                failure_threshold = 56, 
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
                tcp_socket = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_tcp_socket.com_coreos_monitoring_v1_Alertmanager_spec_lifecycle_postStart_tcpSocket(
                    host = '0', 
                    port = kubernetes.client.models.port.port(), ), 
                timeout_seconds = 56
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecReadinessProbe(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
