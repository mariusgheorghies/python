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
from kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets import ComCoreosMonitoringV1ProbeSpecTargets  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1ProbeSpecTargets(unittest.TestCase):
    """ComCoreosMonitoringV1ProbeSpecTargets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1ProbeSpecTargets
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets.ComCoreosMonitoringV1ProbeSpecTargets()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1ProbeSpecTargets(
                ingress = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress.com_coreos_monitoring_v1_Probe_spec_targets_ingress(
                    namespace_selector = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress_namespace_selector.com_coreos_monitoring_v1_Probe_spec_targets_ingress_namespaceSelector(
                        any = True, 
                        match_names = [
                            '0'
                            ], ), 
                    relabeling_configs = [
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
                    selector = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress_selector.com_coreos_monitoring_v1_Probe_spec_targets_ingress_selector(
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
                            }, ), ), 
                static_config = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_static_config.com_coreos_monitoring_v1_Probe_spec_targets_staticConfig(
                    labels = {
                        'key' : '0'
                        }, 
                    relabeling_configs = [
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
                    static = [
                        '0'
                        ], )
            )
        else :
            return ComCoreosMonitoringV1ProbeSpecTargets(
        )

    def testComCoreosMonitoringV1ProbeSpecTargets(self):
        """Test ComCoreosMonitoringV1ProbeSpecTargets"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()