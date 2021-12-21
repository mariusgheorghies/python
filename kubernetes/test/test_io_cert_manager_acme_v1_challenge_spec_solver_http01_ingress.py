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
from kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress import IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress(unittest.TestCase):
    """IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress.IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress(
                _class = '0', 
                ingress_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate(
                    metadata = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_ingress_template_metadata.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_ingressTemplate_metadata(
                        annotations = {
                            'key' : '0'
                            }, 
                        labels = {
                            'key' : '0'
                            }, ), ), 
                name = '0', 
                pod_template = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate(
                    metadata = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_metadata.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_metadata(
                        annotations = {
                            'key' : '0'
                            }, 
                        labels = {
                            'key' : '0'
                            }, ), 
                    spec = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec(
                        affinity = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity(
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
                            pod_affinity = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_affinity.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity_podAffinity(), 
                            pod_anti_affinity = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_http01_ingress_pod_template_spec_affinity_pod_anti_affinity.io_cert_manager_acme_v1_Challenge_spec_solver_http01_ingress_podTemplate_spec_affinity_podAntiAffinity(), ), 
                        node_selector = {
                            'key' : '0'
                            }, 
                        priority_class_name = '0', 
                        service_account_name = '0', 
                        tolerations = [
                            kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_tolerations.com_coreos_monitoring_v1_Alertmanager_spec_tolerations(
                                effect = '0', 
                                key = '0', 
                                operator = '0', 
                                toleration_seconds = 56, 
                                value = '0', )
                            ], ), ), 
                service_type = '0'
            )
        else :
            return IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress(
        )

    def testIoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress(self):
        """Test IoCertManagerAcmeV1ChallengeSpecSolverHttp01Ingress"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
