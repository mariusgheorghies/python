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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec import AwsK8sServicesEc2V1alpha1SecurityGroupSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1SecurityGroupSpec(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1SecurityGroupSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1SecurityGroupSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec.AwsK8sServicesEc2V1alpha1SecurityGroupSpec()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1SecurityGroupSpec(
                description = '0', 
                egress_rules = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_egress_rules.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_egressRules(
                        from_port = 56, 
                        ip_protocol = '0', 
                        ip_ranges = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_ip_ranges.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_ipRanges(
                                cidr_ip = '0', 
                                description = '0', )
                            ], 
                        ipv6_ranges = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_ipv6_ranges.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_ipv6Ranges(
                                cidr_i_pv6 = '0', 
                                description = '0', )
                            ], 
                        prefix_list_i_ds = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_prefix_list_i_ds.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_prefixListIDs(
                                description = '0', 
                                prefix_list_id = '0', )
                            ], 
                        to_port = 56, 
                        user_id_group_pairs = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_user_id_group_pairs.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_userIDGroupPairs(
                                description = '0', 
                                group_id = '0', 
                                group_name = '0', 
                                peering_status = '0', 
                                user_id = '0', 
                                vpc_id = '0', 
                                vpc_peering_connection_id = '0', )
                            ], )
                    ], 
                ingress_rules = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_egress_rules.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_egressRules(
                        from_port = 56, 
                        ip_protocol = '0', 
                        ip_ranges = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_ip_ranges.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_ipRanges(
                                cidr_ip = '0', 
                                description = '0', )
                            ], 
                        ipv6_ranges = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_ipv6_ranges.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_ipv6Ranges(
                                cidr_i_pv6 = '0', 
                                description = '0', )
                            ], 
                        prefix_list_i_ds = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_prefix_list_i_ds.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_prefixListIDs(
                                description = '0', 
                                prefix_list_id = '0', )
                            ], 
                        to_port = 56, 
                        user_id_group_pairs = [
                            kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_security_group_spec_user_id_group_pairs.aws_k8s_services_ec2_v1alpha1_SecurityGroup_spec_userIDGroupPairs(
                                description = '0', 
                                group_id = '0', 
                                group_name = '0', 
                                peering_status = '0', 
                                user_id = '0', 
                                vpc_id = '0', 
                                vpc_peering_connection_id = '0', )
                            ], )
                    ], 
                name = '0', 
                tags = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_tags.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_tags(
                        key = '0', 
                        value = '0', )
                    ], 
                vpc_id = '0', 
                vpc_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(
                    from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                        name = '0', ), )
            )
        else :
            return AwsK8sServicesEc2V1alpha1SecurityGroupSpec(
                description = '0',
                name = '0',
        )

    def testAwsK8sServicesEc2V1alpha1SecurityGroupSpec(self):
        """Test AwsK8sServicesEc2V1alpha1SecurityGroupSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
