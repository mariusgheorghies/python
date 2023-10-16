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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec import AwsK8sServicesEc2V1alpha1NetworkACLSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1NetworkACLSpec(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1NetworkACLSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1NetworkACLSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_network_acl_spec.AwsK8sServicesEc2V1alpha1NetworkACLSpec()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1NetworkACLSpec(
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
                            from = 56, 
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
                vpc_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(
                    from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                        name = '0', ), )
            )
        else :
            return AwsK8sServicesEc2V1alpha1NetworkACLSpec(
        )

    def testAwsK8sServicesEc2V1alpha1NetworkACLSpec(self):
        """Test AwsK8sServicesEc2V1alpha1NetworkACLSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()