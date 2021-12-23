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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1beta1_aws_machine_pool_spec import IoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1beta1_aws_machine_pool_spec.IoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec(
                additional_tags = {
                    'key' : '0'
                    }, 
                availability_zones = [
                    '0'
                    ], 
                aws_launch_template = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_pool_spec_aws_launch_template.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachinePool_spec_awsLaunchTemplate(
                    additional_security_groups = [
                        kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_additional_security_groups.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_additionalSecurityGroups(
                            arn = '0', 
                            filters = [
                                kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_filters.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_filters(
                                    name = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            id = '0', )
                        ], 
                    ami = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_machine_spec_ami.io_x_k8s_cluster_infrastructure_v1alpha4_AWSMachine_spec_ami(
                        eks_lookup_type = 'AmazonLinux', 
                        id = '0', ), 
                    iam_instance_profile = '0', 
                    image_lookup_base_os = '0', 
                    image_lookup_format = '0', 
                    image_lookup_org = '0', 
                    instance_type = '0', 
                    name = '0', 
                    root_volume = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_machine_spec_root_volume.io_x_k8s_cluster_infrastructure_v1alpha4_AWSMachine_spec_rootVolume(
                        device_name = '0', 
                        encrypted = True, 
                        encryption_key = '0', 
                        iops = 56, 
                        size = 8, 
                        throughput = 56, 
                        type = '0', ), 
                    ssh_key_name = '0', 
                    version_number = 56, ), 
                capacity_rebalance = True, 
                default_cool_down = '0', 
                max_size = 1, 
                min_size = 1, 
                mixed_instances_policy = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_pool_spec_mixed_instances_policy.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachinePool_spec_mixedInstancesPolicy(
                    instances_distribution = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_pool_spec_mixed_instances_policy_instances_distribution.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachinePool_spec_mixedInstancesPolicy_instancesDistribution(
                        on_demand_allocation_strategy = 'prioritized', 
                        on_demand_base_capacity = 56, 
                        on_demand_percentage_above_base_capacity = 56, 
                        spot_allocation_strategy = 'lowest-price', ), 
                    overrides = [
                        kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_pool_spec_mixed_instances_policy_overrides.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachinePool_spec_mixedInstancesPolicy_overrides(
                            instance_type = '0', )
                        ], ), 
                provider_id = '0', 
                provider_id_list = [
                    '0'
                    ], 
                refresh_preferences = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_pool_spec_refresh_preferences.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachinePool_spec_refreshPreferences(
                    instance_warmup = 56, 
                    min_healthy_percentage = 56, 
                    strategy = '0', ), 
                subnets = [
                    kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_additional_security_groups.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_additionalSecurityGroups(
                        arn = '0', 
                        filters = [
                            kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_filters.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_filters(
                                name = '0', 
                                values = [
                                    '0'
                                    ], )
                            ], 
                        id = '0', )
                    ]
            )
        else :
            return IoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec(
                aws_launch_template = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_pool_spec_aws_launch_template.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachinePool_spec_awsLaunchTemplate(
                    additional_security_groups = [
                        kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_additional_security_groups.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_additionalSecurityGroups(
                            arn = '0', 
                            filters = [
                                kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_filters.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_filters(
                                    name = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            id = '0', )
                        ], 
                    ami = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_machine_spec_ami.io_x_k8s_cluster_infrastructure_v1alpha4_AWSMachine_spec_ami(
                        eks_lookup_type = 'AmazonLinux', 
                        id = '0', ), 
                    iam_instance_profile = '0', 
                    image_lookup_base_os = '0', 
                    image_lookup_format = '0', 
                    image_lookup_org = '0', 
                    instance_type = '0', 
                    name = '0', 
                    root_volume = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_machine_spec_root_volume.io_x_k8s_cluster_infrastructure_v1alpha4_AWSMachine_spec_rootVolume(
                        device_name = '0', 
                        encrypted = True, 
                        encryption_key = '0', 
                        iops = 56, 
                        size = 8, 
                        throughput = 56, 
                        type = '0', ), 
                    ssh_key_name = '0', 
                    version_number = 56, ),
                max_size = 1,
                min_size = 1,
        )

    def testIoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec(self):
        """Test IoXK8sClusterInfrastructureV1beta1AWSMachinePoolSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
