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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha4_aws_cluster_status import IoXK8sClusterInfrastructureV1alpha4AWSClusterStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1alpha4AWSClusterStatus(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1alpha4AWSClusterStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1alpha4AWSClusterStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha4_aws_cluster_status.IoXK8sClusterInfrastructureV1alpha4AWSClusterStatus()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1alpha4AWSClusterStatus(
                bastion = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_cluster_status_bastion.io_x_k8s_cluster_infrastructure_v1alpha4_AWSCluster_status_bastion(
                    addresses = [
                        kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_bastion_addresses.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_bastion_addresses(
                            address = '0', 
                            type = '0', )
                        ], 
                    availability_zone = '0', 
                    ebs_optimized = True, 
                    ena_support = True, 
                    iam_profile = '0', 
                    id = '0', 
                    image_id = '0', 
                    instance_state = '0', 
                    network_interfaces = [
                        '0'
                        ], 
                    non_root_volumes = [
                        kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha4_aws_managed_control_plane_status_bastion_non_root_volumes.io_x_k8s_cluster_controlplane_v1alpha4_AWSManagedControlPlane_status_bastion_nonRootVolumes(
                            device_name = '0', 
                            encrypted = True, 
                            encryption_key = '0', 
                            iops = 56, 
                            size = 8, 
                            throughput = 56, 
                            type = '0', )
                        ], 
                    private_ip = '0', 
                    public_ip = '0', 
                    root_volume = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha4_aws_managed_control_plane_status_bastion_root_volume.io_x_k8s_cluster_controlplane_v1alpha4_AWSManagedControlPlane_status_bastion_rootVolume(
                        device_name = '0', 
                        encrypted = True, 
                        encryption_key = '0', 
                        iops = 56, 
                        size = 8, 
                        throughput = 56, 
                        type = '0', ), 
                    security_group_ids = [
                        '0'
                        ], 
                    spot_market_options = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_bastion_spot_market_options.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_bastion_spotMarketOptions(
                        max_price = '0', ), 
                    ssh_key_name = '0', 
                    subnet_id = '0', 
                    tags = {
                        'key' : '0'
                        }, 
                    tenancy = '0', 
                    type = '0', 
                    user_data = '0', 
                    volume_i_ds = [
                        '0'
                        ], ), 
                conditions = [
                    kubernetes.client.models.io_x_k8s_cluster_addons_v1alpha3_cluster_resource_set_status_conditions.io_x_k8s_cluster_addons_v1alpha3_ClusterResourceSet_status_conditions(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        severity = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                failure_domains = {
                    'key' : kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_failure_domains.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_failureDomains(
                        attributes = {
                            'key' : '0'
                            }, 
                        control_plane = True, )
                    }, 
                network_status = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_cluster_status_network_status.io_x_k8s_cluster_infrastructure_v1alpha4_AWSCluster_status_networkStatus(
                    api_server_elb = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_api_server_elb.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_apiServerElb(
                        attributes = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_api_server_elb_attributes.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_apiServerElb_attributes(
                            cross_zone_load_balancing = True, 
                            idle_timeout = 56, ), 
                        availability_zones = [
                            '0'
                            ], 
                        dns_name = '0', 
                        health_checks = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_api_server_elb_health_checks.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_apiServerElb_healthChecks(
                            healthy_threshold = 56, 
                            interval = 56, 
                            target = '0', 
                            timeout = 56, 
                            unhealthy_threshold = 56, ), 
                        listeners = [
                            kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_api_server_elb_listeners.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_apiServerElb_listeners(
                                instance_port = 56, 
                                instance_protocol = '0', 
                                port = 56, 
                                protocol = '0', )
                            ], 
                        name = '0', 
                        scheme = '0', 
                        security_group_ids = [
                            '0'
                            ], 
                        subnet_ids = [
                            '0'
                            ], 
                        tags = {
                            'key' : '0'
                            }, ), 
                    security_groups = {
                        'key' : kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_security_groups.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_securityGroups(
                            id = '0', 
                            ingress_rule = [
                                kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_ingress_rule.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_ingressRule(
                                    cidr_blocks = [
                                        '0'
                                        ], 
                                    description = '0', 
                                    from_port = 56, 
                                    protocol = '0', 
                                    source_security_group_ids = [
                                        '0'
                                        ], 
                                    to_port = 56, )
                                ], 
                            name = '0', )
                        }, ), 
                ready = True
            )
        else :
            return IoXK8sClusterInfrastructureV1alpha4AWSClusterStatus(
                ready = True,
        )

    def testIoXK8sClusterInfrastructureV1alpha4AWSClusterStatus(self):
        """Test IoXK8sClusterInfrastructureV1alpha4AWSClusterStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
