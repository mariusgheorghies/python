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
from kubernetes.client.models.io_xk8s_cluster_v1alpha4_cluster_class_spec import IoXK8sClusterV1alpha4ClusterClassSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterV1alpha4ClusterClassSpec(unittest.TestCase):
    """IoXK8sClusterV1alpha4ClusterClassSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterV1alpha4ClusterClassSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_v1alpha4_cluster_class_spec.IoXK8sClusterV1alpha4ClusterClassSpec()  # noqa: E501
        if include_optional :
            return IoXK8sClusterV1alpha4ClusterClassSpec(
                control_plane = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane(
                    machine_infrastructure = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane_machine_infrastructure.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane_machineInfrastructure(
                        ref = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane_machine_infrastructure_ref.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane_machineInfrastructure_ref(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), ), 
                    metadata = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane_metadata.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane_metadata(
                        annotations = {
                            'key' : '0'
                            }, 
                        labels = {
                            'key' : '0'
                            }, ), 
                    ref = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane_machine_infrastructure_ref.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane_machineInfrastructure_ref(
                        api_version = '0', 
                        field_path = '0', 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', ), ), 
                infrastructure = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_infrastructure.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_infrastructure(
                    ref = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane_machine_infrastructure_ref.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane_machineInfrastructure_ref(
                        api_version = '0', 
                        field_path = '0', 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', 
                        resource_version = '0', 
                        uid = '0', ), ), 
                workers = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_workers.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_workers(
                    machine_deployments = [
                        kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_workers_machine_deployments.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_workers_machineDeployments(
                            class = '0', 
                            template = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_workers_template.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_workers_template(
                                bootstrap = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_workers_template_bootstrap.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_workers_template_bootstrap(
                                    ref = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane_machine_infrastructure_ref.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane_machineInfrastructure_ref(
                                        api_version = '0', 
                                        field_path = '0', 
                                        kind = '0', 
                                        name = '0', 
                                        namespace = '0', 
                                        resource_version = '0', 
                                        uid = '0', ), ), 
                                infrastructure = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_workers_template_infrastructure.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_workers_template_infrastructure(
                                    ref = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_control_plane_machine_infrastructure_ref.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_controlPlane_machineInfrastructure_ref(
                                        api_version = '0', 
                                        field_path = '0', 
                                        kind = '0', 
                                        name = '0', 
                                        namespace = '0', 
                                        resource_version = '0', 
                                        uid = '0', ), ), 
                                metadata = kubernetes.client.models.io_x_k8s_cluster_v1alpha4_cluster_class_spec_workers_template_metadata.io_x_k8s_cluster_v1alpha4_ClusterClass_spec_workers_template_metadata(
                                    annotations = {
                                        'key' : '0'
                                        }, 
                                    labels = {
                                        'key' : '0'
                                        }, ), ), )
                        ], )
            )
        else :
            return IoXK8sClusterV1alpha4ClusterClassSpec(
        )

    def testIoXK8sClusterV1alpha4ClusterClassSpec(self):
        """Test IoXK8sClusterV1alpha4ClusterClassSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
