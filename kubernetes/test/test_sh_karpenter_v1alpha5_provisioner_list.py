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
from kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_list import ShKarpenterV1alpha5ProvisionerList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestShKarpenterV1alpha5ProvisionerList(unittest.TestCase):
    """ShKarpenterV1alpha5ProvisionerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ShKarpenterV1alpha5ProvisionerList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_list.ShKarpenterV1alpha5ProvisionerList()  # noqa: E501
        if include_optional :
            return ShKarpenterV1alpha5ProvisionerList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.sh/karpenter/v1alpha5/provisioner.sh.karpenter.v1alpha5.Provisioner(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
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
                                    subresource = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
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
                        spec = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec.sh_karpenter_v1alpha5_Provisioner_spec(
                            kubelet_configuration = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_kubelet_configuration.sh_karpenter_v1alpha5_Provisioner_spec_kubeletConfiguration(
                                cluster_dns = [
                                    '0'
                                    ], 
                                container_runtime = '0', ), 
                            limits = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_limits.sh_karpenter_v1alpha5_Provisioner_spec_limits(
                                resources = {
                                    'key' : None
                                    }, ), 
                            provider = kubernetes.client.models.provider.provider(), 
                            provider_ref = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_provider_ref.sh_karpenter_v1alpha5_Provisioner_spec_providerRef(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), 
                            requirements = [
                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                    key = '0', 
                                    operator = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            startup_taints = [
                                kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_startup_taints.sh_karpenter_v1alpha5_Provisioner_spec_startupTaints(
                                    effect = '0', 
                                    key = '0', 
                                    time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    value = '0', )
                                ], 
                            taints = [
                                kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_startup_taints.sh_karpenter_v1alpha5_Provisioner_spec_startupTaints(
                                    effect = '0', 
                                    key = '0', 
                                    time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    value = '0', )
                                ], 
                            ttl_seconds_after_empty = 56, 
                            ttl_seconds_until_expired = 56, ), 
                        status = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_status.sh_karpenter_v1alpha5_Provisioner_status(
                            conditions = [
                                kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_status_conditions.sh_karpenter_v1alpha5_Provisioner_status_conditions(
                                    last_transition_time = '0', 
                                    message = '0', 
                                    reason = '0', 
                                    severity = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return ShKarpenterV1alpha5ProvisionerList(
                items = [
                    kubernetes.client.models.sh/karpenter/v1alpha5/provisioner.sh.karpenter.v1alpha5.Provisioner(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
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
                                    subresource = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
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
                        spec = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec.sh_karpenter_v1alpha5_Provisioner_spec(
                            kubelet_configuration = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_kubelet_configuration.sh_karpenter_v1alpha5_Provisioner_spec_kubeletConfiguration(
                                cluster_dns = [
                                    '0'
                                    ], 
                                container_runtime = '0', ), 
                            limits = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_limits.sh_karpenter_v1alpha5_Provisioner_spec_limits(
                                resources = {
                                    'key' : None
                                    }, ), 
                            provider = kubernetes.client.models.provider.provider(), 
                            provider_ref = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_provider_ref.sh_karpenter_v1alpha5_Provisioner_spec_providerRef(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), 
                            requirements = [
                                kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_affinity_node_affinity_preference_match_expressions.com_coreos_monitoring_v1_Alertmanager_spec_affinity_nodeAffinity_preference_matchExpressions(
                                    key = '0', 
                                    operator = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            startup_taints = [
                                kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_startup_taints.sh_karpenter_v1alpha5_Provisioner_spec_startupTaints(
                                    effect = '0', 
                                    key = '0', 
                                    time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    value = '0', )
                                ], 
                            taints = [
                                kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_spec_startup_taints.sh_karpenter_v1alpha5_Provisioner_spec_startupTaints(
                                    effect = '0', 
                                    key = '0', 
                                    time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    value = '0', )
                                ], 
                            ttl_seconds_after_empty = 56, 
                            ttl_seconds_until_expired = 56, ), 
                        status = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_status.sh_karpenter_v1alpha5_Provisioner_status(
                            conditions = [
                                kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_status_conditions.sh_karpenter_v1alpha5_Provisioner_status_conditions(
                                    last_transition_time = '0', 
                                    message = '0', 
                                    reason = '0', 
                                    severity = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
        )

    def testShKarpenterV1alpha5ProvisionerList(self):
        """Test ShKarpenterV1alpha5ProvisionerList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
