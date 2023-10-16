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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl import AwsK8sServicesEc2V1alpha1NetworkACL  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1NetworkACL(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1NetworkACL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1NetworkACL
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl.AwsK8sServicesEc2V1alpha1NetworkACL()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1NetworkACL(
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
                spec = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec.aws_k8s_services_ec2_v1alpha1_NetworkACL_spec(
                    associations = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec_associations.aws_k8s_services_ec2_v1alpha1_NetworkACL_spec_associations(
                            network_acl_association_id = '0', 
                            network_aclid = '0', 
                            subnet_id = '0', 
                            subnet_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec_subnet_ref.aws_k8s_services_ec2_v1alpha1_NetworkACL_spec_subnetRef(
                                from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                                    name = '0', ), ), )
                        ], 
                    entries = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec_entries.aws_k8s_services_ec2_v1alpha1_NetworkACL_spec_entries(
                            cidr_block = '0', 
                            egress = True, 
                            icmp_type_code = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec_icmp_type_code.aws_k8s_services_ec2_v1alpha1_NetworkACL_spec_icmpTypeCode(
                                code = 56, 
                                type_ = 56, ), 
                            ipv6_cidr_block = '0', 
                            port_range = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec_port_range.aws_k8s_services_ec2_v1alpha1_NetworkACL_spec_portRange(
                                to = 56, ), 
                            protocol = '0', 
                            rule_action = '0', 
                            rule_number = 56, )
                        ], 
                    tags = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_tags.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_tags(
                            key = '0', 
                            value = '0', )
                        ], 
                    vpc_id = '0', 
                    vpc_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(), ), 
                status = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_status.aws_k8s_services_ec2_v1alpha1_NetworkACL_status(
                    ack_resource_metadata = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_ack_resource_metadata.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_ackResourceMetadata(
                        arn = '0', 
                        owner_account_id = '0', 
                        region = '0', ), 
                    conditions = [
                        kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_conditions.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_conditions(
                            last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], 
                    id = '0', 
                    is_default = True, 
                    owner_id = '0', )
            )
        else :
            return AwsK8sServicesEc2V1alpha1NetworkACL(
        )

    def testAwsK8sServicesEc2V1alpha1NetworkACL(self):
        """Test AwsK8sServicesEc2V1alpha1NetworkACL"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
