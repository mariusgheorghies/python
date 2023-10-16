# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance import AwsK8sServicesEc2V1alpha1Instance  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1Instance(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1Instance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1Instance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance.AwsK8sServicesEc2V1alpha1Instance()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1Instance(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
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
                            subresource = '0', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '0', 
                    namespace = '0', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
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
                spec = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec.aws_k8s_services_ec2_v1alpha1_Instance_spec(
                    block_device_mappings = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_block_device_mappings.aws_k8s_services_ec2_v1alpha1_Instance_spec_blockDeviceMappings(
                            device_name = '0', 
                            ebs = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_ebs.aws_k8s_services_ec2_v1alpha1_Instance_spec_ebs(
                                delete_on_termination = True, 
                                encrypted = True, 
                                iops = 56, 
                                kms_key_id = '0', 
                                outpost_arn = '0', 
                                snapshot_id = '0', 
                                throughput = 56, 
                                volume_size = 56, 
                                volume_type = '0', ), 
                            no_device = '0', 
                            virtual_name = '0', )
                        ], 
                    capacity_reservation_specification = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_capacity_reservation_specification.aws_k8s_services_ec2_v1alpha1_Instance_spec_capacityReservationSpecification(
                        capacity_reservation_preference = '0', 
                        capacity_reservation_target = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_capacity_reservation_specification_capacity_reservation_target.aws_k8s_services_ec2_v1alpha1_Instance_spec_capacityReservationSpecification_capacityReservationTarget(
                            capacity_reservation_id = '0', 
                            capacity_reservation_resource_group_arn = '0', ), ), 
                    cpu_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_cpu_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_cpuOptions(
                        core_count = 56, 
                        threads_per_core = 56, ), 
                    credit_specification = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_credit_specification.aws_k8s_services_ec2_v1alpha1_Instance_spec_creditSpecification(
                        cpu_credits = '0', ), 
                    disable_api_stop = True, 
                    disable_api_termination = True, 
                    ebs_optimized = True, 
                    elastic_gpu_specification = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_elastic_gpu_specification.aws_k8s_services_ec2_v1alpha1_Instance_spec_elasticGPUSpecification(
                            type_ = '0', )
                        ], 
                    elastic_inference_accelerators = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_elastic_inference_accelerators.aws_k8s_services_ec2_v1alpha1_Instance_spec_elasticInferenceAccelerators(
                            count = 56, 
                            type_ = '0', )
                        ], 
                    enclave_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_enclave_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_enclaveOptions(
                        enabled = True, ), 
                    hibernation_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_hibernation_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_hibernationOptions(
                        configured = True, ), 
                    iam_instance_profile = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_iam_instance_profile.aws_k8s_services_ec2_v1alpha1_Instance_spec_iamInstanceProfile(
                        arn = '0', 
                        name = '0', ), 
                    image_id = '0', 
                    instance_initiated_shutdown_behavior = '0', 
                    instance_market_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_instance_market_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_instanceMarketOptions(
                        market_type = '0', 
                        spot_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_instance_market_options_spot_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_instanceMarketOptions_spotOptions(
                            block_duration_minutes = 56, 
                            instance_interruption_behavior = '0', 
                            max_price = '0', 
                            spot_instance_type = '0', 
                            valid_until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), 
                    instance_type = '0', 
                    ipv6_address_count = 56, 
                    ipv6_addresses = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_ipv6_addresses.aws_k8s_services_ec2_v1alpha1_Instance_spec_ipv6Addresses(
                            ipv6_address = '0', )
                        ], 
                    kernel_id = '0', 
                    key_name = '0', 
                    launch_template = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_launch_template.aws_k8s_services_ec2_v1alpha1_Instance_spec_launchTemplate(
                        launch_template_id = '0', 
                        launch_template_name = '0', 
                        version = '0', ), 
                    license_specifications = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_license_specifications.aws_k8s_services_ec2_v1alpha1_Instance_spec_licenseSpecifications(
                            license_configuration_arn = '0', )
                        ], 
                    maintenance_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_maintenance_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_maintenanceOptions(
                        auto_recovery = '0', ), 
                    max_count = 56, 
                    metadata_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_metadata_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_metadataOptions(
                        http_endpoint = '0', 
                        http_protocol_i_pv6 = '0', 
                        http_put_response_hop_limit = 56, 
                        http_tokens = '0', 
                        instance_metadata_tags = '0', ), 
                    min_count = 56, 
                    monitoring = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_monitoring.aws_k8s_services_ec2_v1alpha1_Instance_spec_monitoring(
                        enabled = True, ), 
                    network_interfaces = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_network_interfaces.aws_k8s_services_ec2_v1alpha1_Instance_spec_networkInterfaces(
                            associate_carrier_ip_address = True, 
                            associate_public_ip_address = True, 
                            delete_on_termination = True, 
                            description = '0', 
                            device_index = 56, 
                            interface_type = '0', 
                            ipv4_prefix_count = 56, 
                            ipv4_prefixes = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_ipv4_prefixes.aws_k8s_services_ec2_v1alpha1_Instance_spec_ipv4Prefixes(
                                    ipv4_prefix = '0', )
                                ], 
                            ipv6_address_count = 56, 
                            ipv6_prefix_count = 56, 
                            ipv6_prefixes = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_ipv6_prefixes.aws_k8s_services_ec2_v1alpha1_Instance_spec_ipv6Prefixes(
                                    ipv6_prefix = '0', )
                                ], 
                            network_card_index = 56, 
                            network_interface_id = '0', 
                            private_ip_address = '0', 
                            private_ip_addresses = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_private_ip_addresses.aws_k8s_services_ec2_v1alpha1_Instance_spec_privateIPAddresses(
                                    primary = True, 
                                    private_ip_address = '0', )
                                ], 
                            secondary_private_ip_address_count = 56, 
                            subnet_id = '0', )
                        ], 
                    placement = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_placement.aws_k8s_services_ec2_v1alpha1_Instance_spec_placement(
                        affinity = '0', 
                        availability_zone = '0', 
                        group_name = '0', 
                        host_id = '0', 
                        host_resource_group_arn = '0', 
                        partition_number = 56, 
                        spread_domain = '0', 
                        tenancy = '0', ), 
                    private_dns_name_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_private_dns_name_options.aws_k8s_services_ec2_v1alpha1_Instance_spec_privateDNSNameOptions(
                        enable_resource_name_dnsaaaa_record = True, 
                        enable_resource_name_dnsa_record = True, 
                        hostname_type = '0', ), 
                    private_ip_address = '0', 
                    ram_disk_id = '0', 
                    security_group_i_ds = [
                        '0'
                        ], 
                    security_groups = [
                        '0'
                        ], 
                    subnet_id = '0', 
                    tags = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_tags.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_tags(
                            key = '0', 
                            value = '0', )
                        ], 
                    user_data = '0', ), 
                status = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status.aws_k8s_services_ec2_v1alpha1_Instance_status(
                    ack_resource_metadata = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_ack_resource_metadata.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_ackResourceMetadata(
                        arn = '0', 
                        owner_account_id = '0', 
                        region = '0', ), 
                    ami_launch_index = 56, 
                    architecture = '0', 
                    boot_mode = '0', 
                    capacity_reservation_id = '0', 
                    conditions = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_conditions.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_conditions(
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], 
                    elastic_gpu_associations = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status_elastic_gpu_associations.aws_k8s_services_ec2_v1alpha1_Instance_status_elasticGPUAssociations(
                            elastic_gpu_association_id = '0', 
                            elastic_gpu_association_state = '0', 
                            elastic_gpu_association_time = '0', 
                            elastic_gpuid = '0', )
                        ], 
                    elastic_inference_accelerator_associations = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status_elastic_inference_accelerator_associations.aws_k8s_services_ec2_v1alpha1_Instance_status_elasticInferenceAcceleratorAssociations(
                            elastic_inference_accelerator_arn = '0', 
                            elastic_inference_accelerator_association_id = '0', 
                            elastic_inference_accelerator_association_state = '0', 
                            elastic_inference_accelerator_association_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    ena_support = True, 
                    hypervisor = '0', 
                    instance_id = '0', 
                    instance_lifecycle = '0', 
                    ipv6_address = '0', 
                    launch_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    licenses = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_spec_license_specifications.aws_k8s_services_ec2_v1alpha1_Instance_spec_licenseSpecifications(
                            license_configuration_arn = '0', )
                        ], 
                    outpost_arn = '0', 
                    platform = '0', 
                    platform_details = '0', 
                    private_dns_name = '0', 
                    product_codes = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status_product_codes.aws_k8s_services_ec2_v1alpha1_Instance_status_productCodes(
                            product_code_id = '0', 
                            product_code_type = '0', )
                        ], 
                    public_dns_name = '0', 
                    public_ip_address = '0', 
                    root_device_name = '0', 
                    root_device_type = '0', 
                    source_dest_check = True, 
                    spot_instance_request_id = '0', 
                    sriov_net_support = '0', 
                    state = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status_state.aws_k8s_services_ec2_v1alpha1_Instance_status_state(
                        code = 56, 
                        name = '0', ), 
                    state_reason = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_instance_status_state_reason.aws_k8s_services_ec2_v1alpha1_Instance_status_stateReason(
                        code = '0', 
                        message = '0', ), 
                    state_transition_reason = '0', 
                    tpm_support = '0', 
                    usage_operation = '0', 
                    usage_operation_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    virtualization_type = '0', 
                    vpc_id = '0', )
            )
        else :
            return AwsK8sServicesEc2V1alpha1Instance(
        )

    def testAwsK8sServicesEc2V1alpha1Instance(self):
        """Test AwsK8sServicesEc2V1alpha1Instance"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
