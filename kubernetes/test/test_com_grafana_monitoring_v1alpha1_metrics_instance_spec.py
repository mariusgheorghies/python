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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec import ComGrafanaMonitoringV1alpha1MetricsInstanceSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1MetricsInstanceSpec(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1MetricsInstanceSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1MetricsInstanceSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec.ComGrafanaMonitoringV1alpha1MetricsInstanceSpec()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1MetricsInstanceSpec(
                additional_scrape_configs = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_additional_scrape_configs.com_grafana_monitoring_v1alpha1_MetricsInstance_spec_additionalScrapeConfigs(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                max_wal_time = '0', 
                min_wal_time = '0', 
                pod_monitor_namespace_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_pod_monitor_namespace_selector.com_grafana_monitoring_v1alpha1_MetricsInstance_spec_podMonitorNamespaceSelector(
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
                pod_monitor_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_pod_monitor_selector.com_grafana_monitoring_v1alpha1_MetricsInstance_spec_podMonitorSelector(
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
                probe_namespace_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_probe_namespace_selector.com_grafana_monitoring_v1alpha1_MetricsInstance_spec_probeNamespaceSelector(
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
                probe_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_probe_selector.com_grafana_monitoring_v1alpha1_MetricsInstance_spec_probeSelector(
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
                remote_flush_deadline = '0', 
                remote_write = [
                    kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_remote_write.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_metrics_remoteWrite(
                        basic_auth = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_basic_auth.com_coreos_monitoring_v1_Prometheus_spec_basicAuth(
                            password = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_password.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_password(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            username = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_username.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_username(
                                key = '0', 
                                name = '0', 
                                optional = True, ), ), 
                        bearer_token = '0', 
                        bearer_token_file = '0', 
                        headers = {
                            'key' : '0'
                            }, 
                        metadata_config = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_metadata_config.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_metrics_metadataConfig(
                            send = True, 
                            send_interval = '0', ), 
                        name = '0', 
                        oauth2 = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_logs_oauth2.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_logs_oauth2(
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
                        proxy_url = '0', 
                        queue_config = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_queue_config.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_metrics_queueConfig(
                            batch_send_deadline = '0', 
                            capacity = 56, 
                            max_backoff = '0', 
                            max_retries = 56, 
                            max_samples_per_send = 56, 
                            max_shards = 56, 
                            min_backoff = '0', 
                            min_shards = 56, 
                            retry_on_rate_limit = True, ), 
                        remote_timeout = '0', 
                        sigv4 = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_sigv4.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_metrics_sigv4(
                            access_key = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_sigv4_access_key.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_metrics_sigv4_accessKey(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            profile = '0', 
                            region = '0', 
                            role_arn = '0', 
                            secret_key = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_sigv4_secret_key.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_metrics_sigv4_secretKey(
                                key = '0', 
                                name = '0', 
                                optional = True, ), ), 
                        tls_config = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_metrics_tls_config.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_metrics_tlsConfig(
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
                            server_name = '0', ), 
                        url = '0', 
                        write_relabel_configs = [
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
                            ], )
                    ], 
                service_monitor_namespace_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_service_monitor_namespace_selector.com_grafana_monitoring_v1alpha1_MetricsInstance_spec_serviceMonitorNamespaceSelector(
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
                service_monitor_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_service_monitor_selector.com_grafana_monitoring_v1alpha1_MetricsInstance_spec_serviceMonitorSelector(
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
                wal_truncate_frequency = '0', 
                write_stale_on_shutdown = True
            )
        else :
            return ComGrafanaMonitoringV1alpha1MetricsInstanceSpec(
        )

    def testComGrafanaMonitoringV1alpha1MetricsInstanceSpec(self):
        """Test ComGrafanaMonitoringV1alpha1MetricsInstanceSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
