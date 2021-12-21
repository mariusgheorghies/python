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
from kubernetes.client.models.io_xk8s_cluster_addons_v1beta1_cluster_resource_set_binding_list import IoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList(unittest.TestCase):
    """IoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_addons_v1beta1_cluster_resource_set_binding_list.IoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList()  # noqa: E501
        if include_optional :
            return IoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.io/x_k8s/cluster/addons/v1beta1/cluster_resource_set_binding.io.x-k8s.cluster.addons.v1beta1.ClusterResourceSetBinding(
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
                        spec = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_binding_spec.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSetBinding_spec(
                            bindings = [
                                kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_binding_spec_bindings.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSetBinding_spec_bindings(
                                    cluster_resource_set_name = '0', 
                                    resources = [
                                        kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_binding_spec_resources.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSetBinding_spec_resources(
                                            applied = True, 
                                            hash = '0', 
                                            kind = 'Secret', 
                                            last_applied_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            name = '0', )
                                        ], )
                                ], ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return IoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList(
                items = [
                    kubernetes.client.models.io/x_k8s/cluster/addons/v1beta1/cluster_resource_set_binding.io.x-k8s.cluster.addons.v1beta1.ClusterResourceSetBinding(
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
                        spec = kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_binding_spec.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSetBinding_spec(
                            bindings = [
                                kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_binding_spec_bindings.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSetBinding_spec_bindings(
                                    cluster_resource_set_name = '0', 
                                    resources = [
                                        kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_binding_spec_resources.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSetBinding_spec_resources(
                                            applied = True, 
                                            hash = '0', 
                                            kind = 'Secret', 
                                            last_applied_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            name = '0', )
                                        ], )
                                ], ), )
                    ],
        )

    def testIoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList(self):
        """Test IoXK8sClusterAddonsV1beta1ClusterResourceSetBindingList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
