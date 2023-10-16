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
from kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_email_configs import ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs(unittest.TestCase):
    """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_email_configs.ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs(
                auth_identity = '0', 
                auth_password = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_auth_password.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_authPassword(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                auth_secret = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_auth_secret.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_authSecret(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                auth_username = '0', 
                _from = '0', 
                headers = [
                    kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_headers.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_headers(
                        key = '0', 
                        value = '0', )
                    ], 
                hello = '0', 
                html = '0', 
                require_tls = True, 
                send_resolved = True, 
                smarthost = '0', 
                text = '0', 
                tls_config = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_tls_config.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_tlsConfig(
                    ca = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_alerting_tls_config_ca.com_coreos_monitoring_v1_Prometheus_spec_alerting_tlsConfig_ca(
                        config_map = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_config_map.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_configMap(
                            key = '0', 
                            name = '0', 
                            optional = True, ), 
                        secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_oauth2_client_id_secret.com_coreos_monitoring_v1_PodMonitor_spec_oauth2_clientId_secret(
                            key = '0', 
                            name = '0', 
                            optional = True, ), ), 
                    cert = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_alerting_tls_config_cert.com_coreos_monitoring_v1_Prometheus_spec_alerting_tlsConfig_cert(), 
                    insecure_skip_verify = True, 
                    key_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_key_secret.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_keySecret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    server_name = '0', ), 
                to = '0'
            )
        else :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs(
        )

    def testComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs(self):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecEmailConfigs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()