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
from kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec import ComCoreosMonitoringV1ServiceMonitorSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1ServiceMonitorSpec(unittest.TestCase):
    """ComCoreosMonitoringV1ServiceMonitorSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1ServiceMonitorSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec.ComCoreosMonitoringV1ServiceMonitorSpec()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1ServiceMonitorSpec(
                attach_metadata = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_attach_metadata.com_coreos_monitoring_v1_ServiceMonitor_spec_attachMetadata(
                    node = True, ), 
                endpoints = [
                    kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_endpoints.com_coreos_monitoring_v1_ServiceMonitor_spec_endpoints(
                        authorization = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization.com_coreos_monitoring_v1_PodMonitor_spec_authorization(
                            credentials = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization_credentials.com_coreos_monitoring_v1_PodMonitor_spec_authorization_credentials(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            type = '0', ), 
                        basic_auth = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_basic_auth.com_coreos_monitoring_v1_ServiceMonitor_spec_basicAuth(
                            password = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_password.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_password(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            username = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_username.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_username(
                                key = '0', 
                                name = '0', 
                                optional = True, ), ), 
                        bearer_token_file = '0', 
                        bearer_token_secret = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_bearer_token_secret.com_coreos_monitoring_v1_ServiceMonitor_spec_bearerTokenSecret(
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
                                target_label = '0', )
                            ], 
                        scheme = '0', 
                        scrape_timeout = 'a', 
                        target_port = kubernetes.client.models.target_port.targetPort(), 
                        tls_config = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_tls_config.com_coreos_monitoring_v1_ServiceMonitor_spec_tlsConfig(
                            ca = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_ca.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_ca(), 
                            ca_file = '0', 
                            cert = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_cert.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_cert(), 
                            cert_file = '0', 
                            insecure_skip_verify = True, 
                            key_file = '0', 
                            key_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_key_secret.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_keySecret(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            server_name = '0', ), )
                    ], 
                job_label = '0', 
                label_limit = 56, 
                label_name_length_limit = 56, 
                label_value_length_limit = 56, 
                namespace_selector = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_namespace_selector.com_coreos_monitoring_v1_ServiceMonitor_spec_namespaceSelector(
                    any = True, 
                    match_names = [
                        '0'
                        ], ), 
                pod_target_labels = [
                    '0'
                    ], 
                sample_limit = 56, 
                selector = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_selector.com_coreos_monitoring_v1_ServiceMonitor_spec_selector(
                    match_expressions = [
                        kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelector_matchExpressions(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                target_labels = [
                    '0'
                    ], 
                target_limit = 56
            )
        else :
            return ComCoreosMonitoringV1ServiceMonitorSpec(
                endpoints = [
                    kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_endpoints.com_coreos_monitoring_v1_ServiceMonitor_spec_endpoints(
                        authorization = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization.com_coreos_monitoring_v1_PodMonitor_spec_authorization(
                            credentials = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization_credentials.com_coreos_monitoring_v1_PodMonitor_spec_authorization_credentials(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            type = '0', ), 
                        basic_auth = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_basic_auth.com_coreos_monitoring_v1_ServiceMonitor_spec_basicAuth(
                            password = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_password.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_password(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            username = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_username.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_username(
                                key = '0', 
                                name = '0', 
                                optional = True, ), ), 
                        bearer_token_file = '0', 
                        bearer_token_secret = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_bearer_token_secret.com_coreos_monitoring_v1_ServiceMonitor_spec_bearerTokenSecret(
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
                                target_label = '0', )
                            ], 
                        scheme = '0', 
                        scrape_timeout = 'a', 
                        target_port = kubernetes.client.models.target_port.targetPort(), 
                        tls_config = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_tls_config.com_coreos_monitoring_v1_ServiceMonitor_spec_tlsConfig(
                            ca = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_ca.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_ca(), 
                            ca_file = '0', 
                            cert = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_cert.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_cert(), 
                            cert_file = '0', 
                            insecure_skip_verify = True, 
                            key_file = '0', 
                            key_secret = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_tls_config_key_secret.com_coreos_monitoring_v1_PodMonitor_spec_tlsConfig_keySecret(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            server_name = '0', ), )
                    ],
                selector = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_selector.com_coreos_monitoring_v1_ServiceMonitor_spec_selector(
                    match_expressions = [
                        kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelector_matchExpressions(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ),
        )

    def testComCoreosMonitoringV1ServiceMonitorSpec(self):
        """Test ComCoreosMonitoringV1ServiceMonitorSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()