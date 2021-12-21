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
from kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_webhook_configs import ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs(unittest.TestCase):
    """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_webhook_configs.ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs(
                http_config = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_httpConfig(
                    basic_auth = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config_basic_auth.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_httpConfig_basicAuth(
                        password = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_password.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_password(
                            key = '0', 
                            name = '0', 
                            optional = True, ), 
                        username = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_username.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_username(
                            key = '0', 
                            name = '0', 
                            optional = True, ), ), 
                    bearer_token_secret = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config_bearer_token_secret.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_httpConfig_bearerTokenSecret(
                        key = '0', 
                        name = '0', 
                        optional = True, ), 
                    proxy_url = '0', 
                    tls_config = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config_tls_config.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_httpConfig_tlsConfig(
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
                        server_name = '0', ), ), 
                max_alerts = 0, 
                send_resolved = True, 
                url = '0', 
                url_secret = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_url_secret.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_urlSecret(
                    key = '0', 
                    name = '0', 
                    optional = True, )
            )
        else :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs(
        )

    def testComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs(self):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecWebhookConfigs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
