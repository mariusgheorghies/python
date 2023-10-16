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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral import ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral.ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral(
                volume_claim_template = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral_volume_claim_template.com_coreos_monitoring_v1_Alertmanager_spec_storage_ephemeral_volumeClaimTemplate(
                    metadata = kubernetes.client.models.metadata.metadata(), 
                    spec = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral_volume_claim_template_spec.com_coreos_monitoring_v1_Alertmanager_spec_storage_ephemeral_volumeClaimTemplate_spec(
                        access_modes = [
                            '0'
                            ], 
                        data_source = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral_volume_claim_template_spec_data_source.com_coreos_monitoring_v1_Alertmanager_spec_storage_ephemeral_volumeClaimTemplate_spec_dataSource(
                            api_group = '0', 
                            kind = '0', 
                            name = '0', ), 
                        data_source_ref = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral_volume_claim_template_spec_data_source_ref.com_coreos_monitoring_v1_Alertmanager_spec_storage_ephemeral_volumeClaimTemplate_spec_dataSourceRef(
                            api_group = '0', 
                            kind = '0', 
                            name = '0', ), 
                        resources = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral_volume_claim_template_spec_resources.com_coreos_monitoring_v1_Alertmanager_spec_storage_ephemeral_volumeClaimTemplate_spec_resources(
                            limits = {
                                'key' : None
                                }, 
                            requests = {
                                'key' : None
                                }, ), 
                        selector = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_ephemeral_volume_claim_template_spec_selector.com_coreos_monitoring_v1_Alertmanager_spec_storage_ephemeral_volumeClaimTemplate_spec_selector(
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
                        storage_class_name = '0', 
                        volume_mode = '0', 
                        volume_name = '0', ), )
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeral"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
