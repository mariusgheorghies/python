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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_tls_config import ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_tls_config.ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig(
                ca = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_ca.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_ca(
                    config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), ), 
                ca_file = '0', 
                cert = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_cert.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_cert(
                    config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), ), 
                cert_file = '0', 
                insecure_skip_verify = True, 
                key_file = '0', 
                key_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_key_secret.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_keySecret(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                server_name = '0'
            )
        else :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig(
        )

    def testComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig(self):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsTlsConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
