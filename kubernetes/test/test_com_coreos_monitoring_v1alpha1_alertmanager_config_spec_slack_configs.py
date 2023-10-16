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
from kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_slack_configs import ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs(unittest.TestCase):
    """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_slack_configs.ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs(
                actions = [
                    kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_actions.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_actions(
                        confirm = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_confirm.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_confirm(
                            dismiss_text = '0', 
                            ok_text = '0', 
                            text = '0', 
                            title = '0', ), 
                        name = '0', 
                        style = '0', 
                        text = '0', 
                        type = '0', 
                        url = '0', 
                        value = '0', )
                    ], 
                api_url = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_api_url.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_apiURL(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                callback_id = '0', 
                channel = '0', 
                color = '0', 
                fallback = '0', 
                fields = [
                    kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_fields.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_fields(
                        short = True, 
                        title = '0', 
                        value = '0', )
                    ], 
                footer = '0', 
                http_config = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_httpConfig(
                    authorization = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_http_config_authorization.com_coreos_monitoring_v1alpha1_AlertmanagerConfig_spec_httpConfig_authorization(
                        credentials = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization_credentials.com_coreos_monitoring_v1_PodMonitor_spec_authorization_credentials(
                            key = '0', 
                            name = '0', 
                            optional = True, ), 
                        type = '0', ), 
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
                        server_name = '0', ), ), 
                icon_emoji = '0', 
                icon_url = '0', 
                image_url = '0', 
                link_names = True, 
                mrkdwn_in = [
                    '0'
                    ], 
                pretext = '0', 
                send_resolved = True, 
                short_fields = True, 
                text = '0', 
                thumb_url = '0', 
                title = '0', 
                title_link = '0', 
                username = '0'
            )
        else :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs(
        )

    def testComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs(self):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSlackConfigs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()