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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_spec import IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_spec.IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec(
                additional_tags = {
                    'key' : '0'
                    }, 
                ami_type = 'AL2_x86_64', 
                ami_version = '01', 
                availability_zones = [
                    '0'
                    ], 
                disk_size = 56, 
                eks_nodegroup_name = '0', 
                instance_type = '0', 
                labels = {
                    'key' : '0'
                    }, 
                provider_id_list = [
                    '0'
                    ], 
                remote_access = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_spec_remote_access.io_x_k8s_cluster_infrastructure_v1alpha3_AWSManagedMachinePool_spec_remoteAccess(
                    public = True, 
                    source_security_groups = [
                        '0'
                        ], 
                    ssh_key_name = '0', ), 
                role_name = '0', 
                scaling = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_spec_scaling.io_x_k8s_cluster_infrastructure_v1alpha3_AWSManagedMachinePool_spec_scaling(
                    max_size = 56, 
                    min_size = 56, ), 
                subnet_i_ds = [
                    '0'
                    ]
            )
        else :
            return IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec(
        )

    def testIoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec(self):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
