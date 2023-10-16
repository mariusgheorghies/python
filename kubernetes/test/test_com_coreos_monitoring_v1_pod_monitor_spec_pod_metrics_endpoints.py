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
from kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_pod_metrics_endpoints import ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints(unittest.TestCase):
    """ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_pod_metrics_endpoints.ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints(
                authorization = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization.com_coreos_monitoring_v1_PodMonitor_spec_authorization(
                    credentials = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization_credentials.com_coreos_monitoring_v1_PodMonitor_spec_authorization_credentials(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    type = '0', ), 
                basic_auth = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth(
                    password = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_password.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_password(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    username = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_username.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_username(
                        key = '0', 
                        name = '0', 
                        optional = True, ), ), 
                bearer_token_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_bearer_token_secret.com_coreos_monitoring_v1_PodMonitor_spec_bearerTokenSecret(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                enable_http2 = True, 
                filter_running = True, 
                follow_redirects = True, 
                honor_labels = True, 
                honor_timestamps = True, 
                interval = 'a', 
                metric_relabelings = [
                    kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_metric_relabelings.com_coreos_monitoring_v1_PodMonitor_spec_metricRelabelings(
                        action = 'replace', 
                        modulus = 56, 
                        regex = '0', 
                        replacement = '0', 
                        separator = '0', 
                        source_labels = [
                            'a'
                            ], 
                        target_label = '0', )
                    ], 
                oauth2 = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2.com_coreos_monitoring_v1_PodMonitor_spec_oauth2(
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
                    token_url = '0', ), 
                params = {
                    'key' : [
                        '0'
                        ]
                    }, 
                path = '0', 
                port = '0', 
                proxy_url = '0', 
                relabelings = [
                    kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_metric_relabelings.com_coreos_monitoring_v1_PodMonitor_spec_metricRelabelings(
                        action = 'replace', 
                        modulus = 56, 
                        regex = '0', 
                        replacement = '0', 
                        separator = '0', 
                        source_labels = [
                            'a'
                            ], 
                        target_label = '0', )
                    ], 
                scheme = '0', 
                scrape_timeout = 'a', 
                target_port = kubernetes.client.models.target_port.targetPort(), 
                tls_config = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig(
                    ca = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_ca.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_ca(
                        config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                            key = '0', 
                            name = '0', 
                            optional = True, ), 
                        secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                            key = '0', 
                            name = '0', 
                            optional = True, ), ), 
                    cert = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_cert.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_cert(), 
                    insecure_skip_verify = True, 
                    key_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_key_secret.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_keySecret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    server_name = '0', )
            )
        else :
            return ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints(
        )

    def testComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints(self):
        """Test ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()