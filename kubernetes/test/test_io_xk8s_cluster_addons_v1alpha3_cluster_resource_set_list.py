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
from kubernetes.client.models.io_xk8s_cluster_addons_v1alpha3_cluster_resource_set_list import IoXK8sClusterAddonsV1alpha3ClusterResourceSetList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterAddonsV1alpha3ClusterResourceSetList(unittest.TestCase):
    """IoXK8sClusterAddonsV1alpha3ClusterResourceSetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterAddonsV1alpha3ClusterResourceSetList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_addons_v1alpha3_cluster_resource_set_list.IoXK8sClusterAddonsV1alpha3ClusterResourceSetList()  # noqa: E501
        if include_optional :
            return IoXK8sClusterAddonsV1alpha3ClusterResourceSetList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.io/x_k8s/cluster/addons/v1alpha3/cluster_resource_set.io.x-k8s.cluster.addons.v1alpha3.ClusterResourceSet(
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
                        spec = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_spec.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_spec(
                            cluster_selector = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_spec_cluster_selector.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_spec_clusterSelector(
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
                            resources = [
                                kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_spec_resources.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_spec_resources(
                                    kind = 'Secret', 
                                    name = '0', )
                                ], 
                            strategy = 'ApplyOnce', ), 
                        status = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_status.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_status(
                            conditions = [
                                kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_status_conditions.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    severity = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return IoXK8sClusterAddonsV1alpha3ClusterResourceSetList(
                items = [
                    kubernetes.client.models.io/x_k8s/cluster/addons/v1alpha3/cluster_resource_set.io.x-k8s.cluster.addons.v1alpha3.ClusterResourceSet(
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
                        spec = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_spec.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_spec(
                            cluster_selector = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_spec_cluster_selector.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_spec_clusterSelector(
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
                            resources = [
                                kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_spec_resources.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_spec_resources(
                                    kind = 'Secret', 
                                    name = '0', )
                                ], 
                            strategy = 'ApplyOnce', ), 
                        status = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_status.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_status(
                            conditions = [
                                kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_status_conditions.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    severity = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, ), )
                    ],
        )

    def testIoXK8sClusterAddonsV1alpha3ClusterResourceSetList(self):
        """Test IoXK8sClusterAddonsV1alpha3ClusterResourceSetList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
