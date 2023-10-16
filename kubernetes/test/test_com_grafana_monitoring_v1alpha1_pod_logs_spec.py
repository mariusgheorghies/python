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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec import ComGrafanaMonitoringV1alpha1PodLogsSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1PodLogsSpec(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1PodLogsSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1PodLogsSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec.ComGrafanaMonitoringV1alpha1PodLogsSpec()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1PodLogsSpec(
                job_label = '0', 
                namespace_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_namespace_selector.com_grafana_monitoring_v1alpha1_PodLogs_spec_namespaceSelector(
                    any = True, 
                    match_names = [
                        '0'
                        ], ), 
                pipeline_stages = [
                    kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_pipeline_stages.com_grafana_monitoring_v1alpha1_PodLogs_spec_pipelineStages(
                        cri = kubernetes.client.models.cri.cri(), 
                        docker = kubernetes.client.models.docker.docker(), 
                        drop = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_drop.com_grafana_monitoring_v1alpha1_PodLogs_spec_drop(
                            drop_counter_reason = '0', 
                            expression = '0', 
                            longer_than = '0', 
                            older_than = '0', 
                            source = '0', 
                            value = '0', ), 
                        json = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_json.com_grafana_monitoring_v1alpha1_PodLogs_spec_json(
                            expressions = {
                                'key' : '0'
                                }, 
                            source = '0', ), 
                        label_allow = [
                            '0'
                            ], 
                        label_drop = [
                            '0'
                            ], 
                        labels = {
                            'key' : '0'
                            }, 
                        limit = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_limit.com_grafana_monitoring_v1alpha1_PodLogs_spec_limit(
                            burst = 56, 
                            rate = 56, ), 
                        match = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_match.com_grafana_monitoring_v1alpha1_PodLogs_spec_match(
                            action = '0', 
                            drop_counter_reason = '0', 
                            pipeline_name = '0', 
                            selector = '0', 
                            stages = '0', ), 
                        metrics = {
                            'key' : kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_metrics.com_grafana_monitoring_v1alpha1_PodLogs_spec_metrics(
                                action = '0', 
                                buckets = [
                                    '0'
                                    ], 
                                count_entry_bytes = True, 
                                description = '0', 
                                match_all = True, 
                                max_idle_duration = '0', 
                                prefix = '0', 
                                source = '0', 
                                type = '0', 
                                value = '0', )
                            }, 
                        multiline = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_multiline.com_grafana_monitoring_v1alpha1_PodLogs_spec_multiline(
                            first_line = '0', 
                            max_lines = 56, 
                            max_wait_time = '0', ), 
                        output = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_output.com_grafana_monitoring_v1alpha1_PodLogs_spec_output(
                            source = '0', ), 
                        pack = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_pack.com_grafana_monitoring_v1alpha1_PodLogs_spec_pack(
                            ingest_timestamp = True, 
                            labels = [
                                '0'
                                ], ), 
                        regex = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_regex.com_grafana_monitoring_v1alpha1_PodLogs_spec_regex(
                            expression = '0', 
                            source = '0', ), 
                        replace = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_replace.com_grafana_monitoring_v1alpha1_PodLogs_spec_replace(
                            expression = '0', 
                            source = '0', ), 
                        template = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_template.com_grafana_monitoring_v1alpha1_PodLogs_spec_template(
                            source = '0', 
                            template = '0', ), 
                        tenant = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_tenant.com_grafana_monitoring_v1alpha1_PodLogs_spec_tenant(
                            label = '0', 
                            source = '0', 
                            value = '0', ), 
                        timestamp = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_timestamp.com_grafana_monitoring_v1alpha1_PodLogs_spec_timestamp(
                            action_on_failure = '0', 
                            fallback_formats = [
                                '0'
                                ], 
                            format = '0', 
                            location = '0', 
                            source = '0', ), )
                    ], 
                pod_target_labels = [
                    '0'
                    ], 
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
                selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_selector.com_grafana_monitoring_v1alpha1_PodLogs_spec_selector(
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
                        }, )
            )
        else :
            return ComGrafanaMonitoringV1alpha1PodLogsSpec(
                selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_pod_logs_spec_selector.com_grafana_monitoring_v1alpha1_PodLogs_spec_selector(
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

    def testComGrafanaMonitoringV1alpha1PodLogsSpec(self):
        """Test ComGrafanaMonitoringV1alpha1PodLogsSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()