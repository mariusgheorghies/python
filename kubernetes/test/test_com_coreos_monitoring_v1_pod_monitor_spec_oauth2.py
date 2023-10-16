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
from kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2 import ComCoreosMonitoringV1PodMonitorSpecOauth2  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1PodMonitorSpecOauth2(unittest.TestCase):
    """ComCoreosMonitoringV1PodMonitorSpecOauth2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1PodMonitorSpecOauth2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2.ComCoreosMonitoringV1PodMonitorSpecOauth2()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1PodMonitorSpecOauth2(
                kubernetes.client_id = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId(
                    config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), ), 
                kubernetes.client_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientSecret(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                endpoint_params = {
                    'key' : '0'
                    }, 
                scopes = [
                    '0'
                    ], 
                token_url = '0'
            )
        else :
            return ComCoreosMonitoringV1PodMonitorSpecOauth2(
                kubernetes.client_id = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId(
                    config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), ),
                kubernetes.client_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientSecret(
                    key = '0', 
                    name = '0', 
                    optional = True, ),
                token_url = '0',
        )

    def testComCoreosMonitoringV1PodMonitorSpecOauth2(self):
        """Test ComCoreosMonitoringV1PodMonitorSpecOauth2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()