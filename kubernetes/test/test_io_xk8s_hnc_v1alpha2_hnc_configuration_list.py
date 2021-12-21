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
from kubernetes.client.models.io_xk8s_hnc_v1alpha2_hnc_configuration_list import IoXK8sHncV1alpha2HNCConfigurationList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sHncV1alpha2HNCConfigurationList(unittest.TestCase):
    """IoXK8sHncV1alpha2HNCConfigurationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sHncV1alpha2HNCConfigurationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_hnc_v1alpha2_hnc_configuration_list.IoXK8sHncV1alpha2HNCConfigurationList()  # noqa: E501
        if include_optional :
            return IoXK8sHncV1alpha2HNCConfigurationList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.io/x_k8s/hnc/v1alpha2/hnc_configuration.io.x-k8s.hnc.v1alpha2.HNCConfiguration(
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
                        spec = kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_spec.io_x_k8s_hnc_v1alpha2_HNCConfiguration_spec(
                            resources = [
                                kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_spec_resources.io_x_k8s_hnc_v1alpha2_HNCConfiguration_spec_resources(
                                    group = '0', 
                                    mode = 'Propagate', 
                                    resource = '0', )
                                ], ), 
                        status = kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_status.io_x_k8s_hnc_v1alpha2_HNCConfiguration_status(
                            conditions = [
                                kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_status_conditions.io_x_k8s_hnc_v1alpha2_HNCConfiguration_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 0, 
                                    reason = 'a', 
                                    status = 'True', 
                                    type = 'a', )
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
            return IoXK8sHncV1alpha2HNCConfigurationList(
                items = [
                    kubernetes.client.models.io/x_k8s/hnc/v1alpha2/hnc_configuration.io.x-k8s.hnc.v1alpha2.HNCConfiguration(
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
                        spec = kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_spec.io_x_k8s_hnc_v1alpha2_HNCConfiguration_spec(
                            resources = [
                                kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_spec_resources.io_x_k8s_hnc_v1alpha2_HNCConfiguration_spec_resources(
                                    group = '0', 
                                    mode = 'Propagate', 
                                    resource = '0', )
                                ], ), 
                        status = kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_status.io_x_k8s_hnc_v1alpha2_HNCConfiguration_status(
                            conditions = [
                                kubernetes.client.models.io_x_k8s_hnc_v1alpha2_hnc_configuration_status_conditions.io_x_k8s_hnc_v1alpha2_HNCConfiguration_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 0, 
                                    reason = 'a', 
                                    status = 'True', 
                                    type = 'a', )
                                ], ), )
                    ],
        )

    def testIoXK8sHncV1alpha2HNCConfigurationList(self):
        """Test IoXK8sHncV1alpha2HNCConfigurationList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
