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
from kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config_tls_config import ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig(unittest.TestCase):
    """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config_tls_config.ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig(
                ca = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_ca.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_ca(
                    config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), ), 
                cert = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_cert.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_cert(
                    config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), ), 
                insecure_skip_verify = True, 
                key_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_key_secret.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_keySecret(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                server_name = '0'
            )
        else :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig(
        )

    def testComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig(self):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
