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
from kubernetes.client.models.com_coreos_monitoring_v1_probe_list import ComCoreosMonitoringV1ProbeList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1ProbeList(unittest.TestCase):
    """ComCoreosMonitoringV1ProbeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1ProbeList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_probe_list.ComCoreosMonitoringV1ProbeList()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1ProbeList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.com/coreos/monitoring/v1/probe.com.coreos.monitoring.v1.Probe(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta_v2.v1.ObjectMeta_v2(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference_v2.v1.OwnerReference_v2(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec.com_coreos_monitoring_v1_Probe_spec(
                            interval = '0', 
                            job_name = '0', 
                            module = '0', 
                            prober = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_prober.com_coreos_monitoring_v1_Probe_spec_prober(
                                path = '0', 
                                scheme = '0', 
                                url = '0', ), 
                            scrape_timeout = '0', 
                            targets = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets.com_coreos_monitoring_v1_Probe_spec_targets(
                                ingress = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress.com_coreos_monitoring_v1_Probe_spec_targets_ingress(
                                    namespace_selector = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress_namespace_selector.com_coreos_monitoring_v1_Probe_spec_targets_ingress_namespaceSelector(
                                        any = True, 
                                        match_names = [
                                            '0'
                                            ], ), 
                                    relabeling_configs = [
                                        kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_metric_relabelings.com_coreos_monitoring_v1_PodMonitor_spec_metricRelabelings(
                                            action = '0', 
                                            modulus = 56, 
                                            regex = '0', 
                                            replacement = '0', 
                                            separator = '0', 
                                            source_labels = [
                                                '0'
                                                ], 
                                            target_label = '0', )
                                        ], 
                                    selector = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress_selector.com_coreos_monitoring_v1_Probe_spec_targets_ingress_selector(
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
                                            }, ), ), 
                                static_config = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_static_config.com_coreos_monitoring_v1_Probe_spec_targets_staticConfig(
                                    static = [
                                        '0'
                                        ], ), ), ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return ComCoreosMonitoringV1ProbeList(
                items = [
                    kubernetes.client.models.com/coreos/monitoring/v1/probe.com.coreos.monitoring.v1.Probe(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta_v2.v1.ObjectMeta_v2(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference_v2.v1.OwnerReference_v2(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec.com_coreos_monitoring_v1_Probe_spec(
                            interval = '0', 
                            job_name = '0', 
                            module = '0', 
                            prober = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_prober.com_coreos_monitoring_v1_Probe_spec_prober(
                                path = '0', 
                                scheme = '0', 
                                url = '0', ), 
                            scrape_timeout = '0', 
                            targets = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets.com_coreos_monitoring_v1_Probe_spec_targets(
                                ingress = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress.com_coreos_monitoring_v1_Probe_spec_targets_ingress(
                                    namespace_selector = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress_namespace_selector.com_coreos_monitoring_v1_Probe_spec_targets_ingress_namespaceSelector(
                                        any = True, 
                                        match_names = [
                                            '0'
                                            ], ), 
                                    relabeling_configs = [
                                        kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_metric_relabelings.com_coreos_monitoring_v1_PodMonitor_spec_metricRelabelings(
                                            action = '0', 
                                            modulus = 56, 
                                            regex = '0', 
                                            replacement = '0', 
                                            separator = '0', 
                                            source_labels = [
                                                '0'
                                                ], 
                                            target_label = '0', )
                                        ], 
                                    selector = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_ingress_selector.com_coreos_monitoring_v1_Probe_spec_targets_ingress_selector(
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
                                            }, ), ), 
                                static_config = kubernetes.client.models.com_coreos_monitoring_v1_probe_spec_targets_static_config.com_coreos_monitoring_v1_Probe_spec_targets_staticConfig(
                                    static = [
                                        '0'
                                        ], ), ), ), )
                    ],
        )

    def testComCoreosMonitoringV1ProbeList(self):
        """Test ComCoreosMonitoringV1ProbeList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
