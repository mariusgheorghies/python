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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool import IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool.IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool(
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
                spec = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_spec.io_x_k8s_cluster_infrastructure_v1alpha3_AWSManagedMachinePool_spec(
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
                        ], ), 
                status = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_status.io_x_k8s_cluster_infrastructure_v1alpha3_AWSManagedMachinePool_status(
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
                    ready = True, 
                    replicas = 56, )
            )
        else :
            return IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool(
        )

    def testIoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool(self):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePool"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
