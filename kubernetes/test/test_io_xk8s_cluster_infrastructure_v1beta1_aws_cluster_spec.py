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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1beta1_aws_cluster_spec import IoXK8sClusterInfrastructureV1beta1AWSClusterSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1beta1AWSClusterSpec(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1beta1AWSClusterSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1beta1AWSClusterSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1beta1_aws_cluster_spec.IoXK8sClusterInfrastructureV1beta1AWSClusterSpec()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1beta1AWSClusterSpec(
                additional_tags = {
                    'key' : '0'
                    }, 
                bastion = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_bastion.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_bastion(
                    allowed_cidr_blocks = [
                        '0'
                        ], 
                    ami = '0', 
                    disable_ingress_rules = True, 
                    enabled = True, 
                    instance_type = '0', ), 
                control_plane_endpoint = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_control_plane_endpoint.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_controlPlaneEndpoint(
                    host = '0', 
                    port = 56, ), 
                control_plane_load_balancer = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_cluster_spec_control_plane_load_balancer.io_x_k8s_cluster_infrastructure_v1beta1_AWSCluster_spec_controlPlaneLoadBalancer(
                    additional_security_groups = [
                        '0'
                        ], 
                    cross_zone_load_balancing = True, 
                    scheme = 'internet-facing', 
                    subnets = [
                        '0'
                        ], ), 
                identity_ref = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_spec_identity_ref.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_spec_identityRef(
                    kind = 'AWSClusterControllerIdentity', 
                    name = '0', ), 
                image_lookup_base_os = '0', 
                image_lookup_format = '0', 
                image_lookup_org = '0', 
                network = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec(
                    cni = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec_cni.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec_cni(
                        cni_ingress_rules = [
                            kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec_cni_cni_ingress_rules.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec_cni_cniIngressRules(
                                description = '0', 
                                from_port = 56, 
                                protocol = '0', 
                                to_port = 56, )
                            ], ), 
                    security_group_overrides = {
                        'key' : '0'
                        }, 
                    subnets = [
                        kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec_subnets.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec_subnets(
                            availability_zone = '0', 
                            cidr_block = '0', 
                            id = '0', 
                            is_public = True, 
                            nat_gateway_id = '0', 
                            route_table_id = '0', 
                            tags = {
                                'key' : '0'
                                }, )
                        ], 
                    vpc = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec_vpc.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec_vpc(
                        availability_zone_selection = 'Ordered', 
                        availability_zone_usage_limit = 1, 
                        cidr_block = '0', 
                        id = '0', 
                        internet_gateway_id = '0', ), ), 
                region = '0', 
                ssh_key_name = '0'
            )
        else :
            return IoXK8sClusterInfrastructureV1beta1AWSClusterSpec(
        )

    def testIoXK8sClusterInfrastructureV1beta1AWSClusterSpec(self):
        """Test IoXK8sClusterInfrastructureV1beta1AWSClusterSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
