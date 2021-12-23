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
from kubernetes.client.models.io_xk8s_cluster_v1alpha4_machine_status import IoXK8sClusterV1alpha4MachineStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterV1alpha4MachineStatus(unittest.TestCase):
    """IoXK8sClusterV1alpha4MachineStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterV1alpha4MachineStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_v1alpha4_machine_status.IoXK8sClusterV1alpha4MachineStatus()  # noqa: E501
        if include_optional :
            return IoXK8sClusterV1alpha4MachineStatus(
                addresses = [
                    kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_bastion_addresses.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_bastion_addresses(
                        address = '0', 
                        type = '0', )
                    ], 
                bootstrap_ready = True, 
                conditions = [
                    kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_status_conditions.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_status_conditions(
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
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                node_info = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_machine_status_node_info.io_x_k8s_cluster_v1alpha4_Machine_status_nodeInfo(
                    architecture = '0', 
                    boot_id = '0', 
                    container_runtime_version = '0', 
                    kernel_version = '0', 
                    kube_proxy_version = '0', 
                    kubelet_version = '0', 
                    machine_id = '0', 
                    operating_system = '0', 
                    os_image = '0', 
                    system_uuid = '0', ), 
                node_ref = kubernetes.client.models.io_x_k8s_cluster_v1alpha3_machine_status_node_ref.io_x_k8s_cluster_v1alpha3_Machine_status_nodeRef(
                    api_version = '0', 
                    field_path = '0', 
                    kind = '0', 
                    name = '0', 
                    namespace = '0', 
                    resource_version = '0', 
                    uid = '0', ), 
                observed_generation = 56, 
                phase = '0', 
                version = '0'
            )
        else :
            return IoXK8sClusterV1alpha4MachineStatus(
        )

    def testIoXK8sClusterV1alpha4MachineStatus(self):
        """Test IoXK8sClusterV1alpha4MachineStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
