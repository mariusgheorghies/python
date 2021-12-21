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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1beta1_aws_machine_spec import IoXK8sClusterInfrastructureV1beta1AWSMachineSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1beta1AWSMachineSpec(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1beta1AWSMachineSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1beta1AWSMachineSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1beta1_aws_machine_spec.IoXK8sClusterInfrastructureV1beta1AWSMachineSpec()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1beta1AWSMachineSpec(
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
                additional_tags = {
                    'key' : '0'
                    }, 
                ami = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_machine_spec_ami.io_x_k8s_cluster_infrastructure_v1alpha4_AWSMachine_spec_ami(
                    eks_lookup_type = 'AmazonLinux', 
                    id = '0', ), 
                cloud_init = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_cloud_init.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_cloudInit(
                    insecure_skip_secrets_manager = True, 
                    secret_count = 56, 
                    secret_prefix = '0', 
                    secure_secrets_backend = 'secrets-manager', ), 
                failure_domain = '0', 
                iam_instance_profile = '0', 
                image_lookup_base_os = '0', 
                image_lookup_format = '0', 
                image_lookup_org = '0', 
                instance_id = '0', 
                instance_type = '01', 
                network_interfaces = [
                    '0'
                    ], 
                non_root_volumes = [
                    kubernetes.client.models.io_x_k8s_cluster_controlplane_v1beta1_aws_managed_control_plane_status_bastion_non_root_volumes.io_x_k8s_cluster_controlplane_v1beta1_AWSManagedControlPlane_status_bastion_nonRootVolumes(
                        device_name = '0', 
                        encrypted = True, 
                        encryption_key = '0', 
                        iops = 56, 
                        size = 8, 
                        throughput = 56, 
                        type = '0', )
                    ], 
                provider_id = '0', 
                public_ip = True, 
                root_volume = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha4_aws_machine_spec_root_volume.io_x_k8s_cluster_infrastructure_v1alpha4_AWSMachine_spec_rootVolume(
                    device_name = '0', 
                    encrypted = True, 
                    encryption_key = '0', 
                    iops = 56, 
                    size = 8, 
                    throughput = 56, 
                    type = '0', ), 
                spot_market_options = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_spot_market_options.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_spotMarketOptions(
                    max_price = '0', ), 
                ssh_key_name = '0', 
                subnet = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_subnet.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_subnet(
                    arn = '0', 
                    filters = [
                        kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1beta1_aws_machine_spec_filters.io_x_k8s_cluster_infrastructure_v1beta1_AWSMachine_spec_filters(
                            name = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    id = '0', ), 
                tenancy = 'default', 
                uncompressed_user_data = True
            )
        else :
            return IoXK8sClusterInfrastructureV1beta1AWSMachineSpec(
                instance_type = '01',
        )

    def testIoXK8sClusterInfrastructureV1beta1AWSMachineSpec(self):
        """Test IoXK8sClusterInfrastructureV1beta1AWSMachineSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
