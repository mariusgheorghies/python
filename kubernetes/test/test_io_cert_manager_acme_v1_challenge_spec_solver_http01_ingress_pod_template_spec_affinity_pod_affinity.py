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
from kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity import IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity(unittest.TestCase):
    """IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity.IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity(
                preferred_during_scheduling_ignored_during_execution = [
                    kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution(
                        pod_affinity_term = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity_pod_affinity_term.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity_podAffinity_podAffinityTerm(
                            label_selector = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_label_selector.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_labelSelector(
                                match_expressions = [
                                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_label_selector_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_labelSelector_matchExpressions(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_labels = {
                                    'key' : '0'
                                    }, ), 
                            namespace_selector = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity_pod_affinity_term_namespace_selector.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity_podAffinity_podAffinityTerm_namespaceSelector(), 
                            namespaces = [
                                '0'
                                ], 
                            topology_key = '0', ), 
                        weight = 56, )
                    ], 
                required_during_scheduling_ignored_during_execution = [
                    kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity_podAffinity_requiredDuringSchedulingIgnoredDuringExecution(
                        label_selector = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_label_selector.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_labelSelector(
                            match_expressions = [
                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_pod_affinity_pod_affinity_term_label_selector_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_podAffinity_podAffinityTerm_labelSelector_matchExpressions(
                                    key = '0', 
                                    operator = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            match_labels = {
                                'key' : '0'
                                }, ), 
                        namespace_selector = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity_pod_affinity_term_namespace_selector.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity_podAffinity_podAffinityTerm_namespaceSelector(), 
                        namespaces = [
                            '0'
                            ], 
                        topology_key = '0', )
                    ]
            )
        else :
            return IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity(
        )

    def testIoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity(self):
        """Test IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
