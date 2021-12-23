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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_pre_stop import ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_pre_stop.ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop(
                _exec = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_exec.com_coreos_monitoring_v1_Alertmanager_spec_lifecycle_postStart_exec(
                    command = [
                        '0'
                        ], ), 
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
                tcp_socket = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_tcp_socket.com_coreos_monitoring_v1_Alertmanager_spec_lifecycle_postStart_tcpSocket(
                    host = '0', 
                    port = kubernetes.client.models.port.port(), )
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
