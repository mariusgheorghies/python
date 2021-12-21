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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_machine import IoXK8sClusterInfrastructureV1alpha3AWSMachine  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1alpha3AWSMachine(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1alpha3AWSMachine unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSMachine
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_machine.IoXK8sClusterInfrastructureV1alpha3AWSMachine()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1alpha3AWSMachine(
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
                spec = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec(
                    additional_security_groups = [
                        kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_additional_security_groups.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_additionalSecurityGroups(
                            arn = '0', 
                            filters = [
                                kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_filters.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_filters(
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
                    ami = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_ami.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_ami(
                        arn = '0', 
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
                    instance_type = '0', 
                    network_interfaces = [
                        '0'
                        ], 
                    non_root_volumes = [
                        kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_bastion_non_root_volumes.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_bastion_nonRootVolumes(
                            device_name = '0', 
                            encrypted = True, 
                            encryption_key = '0', 
                            iops = 56, 
                            size = 8, 
                            type = '0', )
                        ], 
                    provider_id = '0', 
                    public_ip = True, 
                    root_volume = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_root_volume.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_rootVolume(
                        device_name = '0', 
                        encrypted = True, 
                        encryption_key = '0', 
                        iops = 56, 
                        size = 8, 
                        type = '0', ), 
                    spot_market_options = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_spot_market_options.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_spotMarketOptions(
                        max_price = '0', ), 
                    ssh_key_name = '0', 
                    subnet = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_spec_subnet.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_spec_subnet(
                        arn = '0', 
                        id = '0', ), 
                    tenancy = 'default', 
                    uncompressed_user_data = True, ), 
                status = kubernetes.client.models.io_x_k8s_cluster_infrastructure_v1alpha3_aws_machine_status.io_x_k8s_cluster_infrastructure_v1alpha3_AWSMachine_status(
                    addresses = [
                        kubernetes.client.models.io_x_k8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_status_bastion_addresses.io_x_k8s_cluster_controlplane_v1alpha3_AWSManagedControlPlane_status_bastion_addresses(
                            address = '0', 
                            type = '0', )
                        ], 
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
                    instance_state = '0', 
                    interruptible = True, 
                    ready = True, )
            )
        else :
            return IoXK8sClusterInfrastructureV1alpha3AWSMachine(
        )

    def testIoXK8sClusterInfrastructureV1alpha3AWSMachine(self):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSMachine"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
