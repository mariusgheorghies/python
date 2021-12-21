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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_cluster_list import IoXK8sClusterInfrastructureV1alpha3AWSClusterList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1alpha3AWSClusterList(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1alpha3AWSClusterList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSClusterList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_cluster_list.IoXK8sClusterInfrastructureV1alpha3AWSClusterList()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1alpha3AWSClusterList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.io/x_k8s/cluster/infrastructure/v1alpha3/aws_cluster.io.x-k8s.cluster.infrastructure.v1alpha3.AWSCluster(
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
                        spec = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_spec.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_spec(
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
                            control_plane_load_balancer = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_spec_control_plane_load_balancer.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_spec_controlPlaneLoadBalancer(
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
                            network_spec = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec(
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
                                vpc = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec_vpc.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec_vpc(
                                    availability_zone_selection = 'Ordered', 
                                    availability_zone_usage_limit = 1, 
                                    cidr_block = '0', 
                                    id = '0', 
                                    internet_gateway_id = '0', 
                                    tags = {
                                        'key' : '0'
                                        }, ), ), 
                            region = '0', 
                            ssh_key_name = '0', ), 
                        status = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_status.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_status(
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
                            network = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_status_network.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_status_network(
                                api_server_elb = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_api_server_elb.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_apiServerElb(
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
                                        ], ), 
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
                            ready = True, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return IoXK8sClusterInfrastructureV1alpha3AWSClusterList(
                items = [
                    kubernetes.client.models.io/x_k8s/cluster/infrastructure/v1alpha3/aws_cluster.io.x-k8s.cluster.infrastructure.v1alpha3.AWSCluster(
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
                        spec = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_spec.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_spec(
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
                            control_plane_load_balancer = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_spec_control_plane_load_balancer.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_spec_controlPlaneLoadBalancer(
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
                            network_spec = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec(
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
                                vpc = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_network_spec_vpc.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_spec_networkSpec_vpc(
                                    availability_zone_selection = 'Ordered', 
                                    availability_zone_usage_limit = 1, 
                                    cidr_block = '0', 
                                    id = '0', 
                                    internet_gateway_id = '0', 
                                    tags = {
                                        'key' : '0'
                                        }, ), ), 
                            region = '0', 
                            ssh_key_name = '0', ), 
                        status = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_status.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_status(
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
                            network = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_cluster_status_network.io_x_k8s_cluster_infrastructure_v1alpha3_AWSCluster_status_network(
                                api_server_elb = kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_network_api_server_elb.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_network_apiServerElb(
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
                                        ], ), 
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
                            ready = True, ), )
                    ],
        )

    def testIoXK8sClusterInfrastructureV1alpha3AWSClusterList(self):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSClusterList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
