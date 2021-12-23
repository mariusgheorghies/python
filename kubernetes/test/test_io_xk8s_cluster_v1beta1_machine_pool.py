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
from kubernetes.client.models.io_xk8s_cluster_v1beta1_machine_pool import IoXK8sClusterV1beta1MachinePool  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterV1beta1MachinePool(unittest.TestCase):
    """IoXK8sClusterV1beta1MachinePool unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterV1beta1MachinePool
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_v1beta1_machine_pool.IoXK8sClusterV1beta1MachinePool()  # noqa: E501
        if include_optional :
            return IoXK8sClusterV1beta1MachinePool(
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
                spec = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_machine_pool_spec.io_x_k8s_cluster_v1alpha4_MachinePool_spec(
                    cluster_name = '0', 
                    failure_domains = [
                        '0'
                        ], 
                    min_ready_seconds = 56, 
                    provider_id_list = [
                        '0'
                        ], 
                    replicas = 56, 
                    template = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_machine_deployment_spec_template.io_x_k8s_cluster_v1alpha4_MachineDeployment_spec_template(
                        metadata = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha4_kubeadm_control_plane_spec_machine_template_metadata.io_x_k8s_cluster_controlplane_v1alpha4_KubeadmControlPlane_spec_machineTemplate_metadata(
                            annotations = {
                                'key' : '0'
                                }, 
                            labels = {
                                'key' : '0'
                                }, ), 
                        spec = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_machine_deployment_spec_template_spec.io_x_k8s_cluster_v1alpha4_MachineDeployment_spec_template_spec(
                            bootstrap = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_machine_spec_bootstrap.io_x_k8s_cluster_v1alpha4_Machine_spec_bootstrap(
                                config_ref = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_machine_spec_bootstrap_config_ref.io_x_k8s_cluster_v1alpha4_Machine_spec_bootstrap_configRef(
                                    api_version = '0', 
                                    field_path = '0', 
                                    kind = '0', 
                                    name = '0', 
                                    namespace = '0', 
                                    resource_version = '0', 
                                    uid = '0', ), 
                                data_secret_name = '0', ), 
                            cluster_name = '0', 
                            failure_domain = '0', 
                            infrastructure_ref = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha4_kubeadm_control_plane_spec_machine_template_infrastructure_ref.io_x_k8s_cluster_controlplane_v1alpha4_KubeadmControlPlane_spec_machineTemplate_infrastructureRef(
                                api_version = '0', 
                                field_path = '0', 
                                kind = '0', 
                                name = '0', 
                                namespace = '0', 
                                resource_version = '0', 
                                uid = '0', ), 
                            node_drain_timeout = '0', 
                            provider_id = '0', 
                            version = '0', ), ), ), 
                status = kubernetes.client.models.io_x_k8s_cluster_v1beta1_machine_pool_status.io_x_k8s_cluster_v1beta1_MachinePool_status(
                    available_replicas = 56, 
                    bootstrap_ready = True, 
                    conditions = [
                        kubernetes.client.models.io_x_k8s_cluster_addons_v1beta1_cluster_resource_set_status_conditions.io_x_k8s_cluster_addons_v1beta1_ClusterResourceSet_status_conditions(
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '0', 
                            reason = '0', 
                            severity = '0', 
                            status = '0', 
                            type = '0', )
                        ], 
                    failure_message = '0', 
                    failure_reason = '0', 
                    infrastructure_ready = True, 
                    node_refs = [
                        kubernetes.client.models.io_x_k8s_cluster_v1alpha3_machine_pool_status_node_refs.io_x_k8s_cluster_v1alpha3_MachinePool_status_nodeRefs(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', )
                        ], 
                    observed_generation = 56, 
                    phase = '0', 
                    ready_replicas = 56, 
                    replicas = 56, 
                    unavailable_replicas = 56, )
            )
        else :
            return IoXK8sClusterV1beta1MachinePool(
        )

    def testIoXK8sClusterV1beta1MachinePool(self):
        """Test IoXK8sClusterV1beta1MachinePool"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
