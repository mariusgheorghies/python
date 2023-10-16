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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity import ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity.ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity(
                node_affinity = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity(
                    preferred_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                            preference = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference(
                                match_expressions = [
                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_fields = [
                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                        key = '0', 
                                        operator = '0', )
                                    ], ), 
                            weight = 56, )
                        ], 
                    required_during_scheduling_ignored_during_execution = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                        node_selector_terms = [
                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_requiredDuringSchedulingIgnoredDuringExecution_nodeSelectorTerms()
                            ], ), ), 
                pod_affinity = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity(
                    preferred_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                            pod_affinity_term = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_pod_affinity_term.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_podAffinityTerm(
                                label_selector = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_label_selector.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_labelSelector(
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
                                namespace_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_pod_affinity_term_namespace_selector.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_podAffinityTerm_namespaceSelector(), 
                                namespaces = [
                                    '0'
                                    ], 
                                topology_key = '0', ), 
                            weight = 56, )
                        ], 
                    required_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                            topology_key = '0', )
                        ], ), 
                pod_anti_affinity = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_anti_affinity.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAntiAffinity(
                    preferred_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                            pod_affinity_term = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_pod_affinity_term.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_podAffinityTerm(
                                label_selector = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_label_selector.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_labelSelector(
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
                                namespace_selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_pod_affinity_term_namespace_selector.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_podAffinityTerm_namespaceSelector(), 
                                namespaces = [
                                    '0'
                                    ], 
                                topology_key = '0', ), 
                            weight = 56, )
                        ], 
                    required_during_scheduling_ignored_during_execution = [
                        kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_affinity_podAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                            topology_key = '0', )
                        ], )
            )
        else :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity(
        )

    def testComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity(self):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
