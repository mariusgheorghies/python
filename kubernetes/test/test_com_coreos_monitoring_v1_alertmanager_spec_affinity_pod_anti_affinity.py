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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_anti_affinity import ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_anti_affinity.ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity(
                preferred_during_scheduling_ignored_during_execution = [
                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                        pod_affinity_term = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm(
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
                            namespace_selector = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_namespace_selector.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_namespaceSelector(), 
                            namespaces = [
                                '0'
                                ], 
                            topology_key = '0', ), 
                        weight = 56, )
                    ], 
                required_during_scheduling_ignored_during_execution = [
                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_requiredDuringSchedulingIgnoredDuringExecution(
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
                        namespace_selector = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_namespace_selector.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_namespaceSelector(), 
                        namespaces = [
                            '0'
                            ], 
                        topology_key = '0', )
                    ]
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAntiAffinity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
