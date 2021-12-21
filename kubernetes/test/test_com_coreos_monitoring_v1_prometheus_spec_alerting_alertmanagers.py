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
from kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_alerting_alertmanagers import ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers(unittest.TestCase):
    """ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_alerting_alertmanagers.ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers(
                api_version = '0', 
                authorization = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_alerting_authorization.com_coreos_monitoring_v1_Prometheus_spec_alerting_authorization(
                    credentials = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization_credentials.com_coreos_monitoring_v1_PodMonitor_spec_authorization_credentials(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    type = '0', ), 
                bearer_token_file = '0', 
                name = '0', 
                namespace = '0', 
                path_prefix = '0', 
                port = kubernetes.client.models.port.port(), 
                scheme = '0', 
                timeout = '0', 
                tls_config = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_alerting_tls_config.com_coreos_monitoring_v1_Prometheus_spec_alerting_tlsConfig(
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
                    cert = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_cert.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_cert(), 
                    cert_file = '0', 
                    insecure_skip_verify = True, 
                    key_file = '0', 
                    key_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_key_secret.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_keySecret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    server_name = '0', )
            )
        else :
            return ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers(
                name = '0',
                namespace = '0',
                port = kubernetes.client.models.port.port(),
        )

    def testComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers(self):
        """Test ComCoreosMonitoringV1PrometheusSpecAlertingAlertmanagers"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
