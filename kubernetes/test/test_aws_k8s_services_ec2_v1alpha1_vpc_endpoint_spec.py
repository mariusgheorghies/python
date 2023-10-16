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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_vpc_endpoint_spec import AwsK8sServicesEc2V1alpha1VPCEndpointSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1VPCEndpointSpec(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1VPCEndpointSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1VPCEndpointSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_vpc_endpoint_spec.AwsK8sServicesEc2V1alpha1VPCEndpointSpec()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1VPCEndpointSpec(
                dns_options = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_vpc_endpoint_spec_dns_options.aws_k8s_services_ec2_v1alpha1_VPCEndpoint_spec_dnsOptions(
                    dns_record_ip_type = '0', ), 
                ip_address_type = '0', 
                policy_document = '0', 
                private_dns_enabled = True, 
                route_table_i_ds = [
                    '0'
                    ], 
                route_table_refs = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(
                        from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                            name = '0', ), )
                    ], 
                security_group_i_ds = [
                    '0'
                    ], 
                security_group_refs = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(
                        from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                            name = '0', ), )
                    ], 
                service_name = '0', 
                subnet_i_ds = [
                    '0'
                    ], 
                subnet_refs = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(
                        from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                            name = '0', ), )
                    ], 
                tags = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_tags.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_tags(
                        key = '0', 
                        value = '0', )
                    ], 
                vpc_endpoint_type = '0', 
                vpc_id = '0', 
                vpc_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(
                    from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                        name = '0', ), )
            )
        else :
            return AwsK8sServicesEc2V1alpha1VPCEndpointSpec(
                service_name = '0',
        )

    def testAwsK8sServicesEc2V1alpha1VPCEndpointSpec(self):
        """Test AwsK8sServicesEc2V1alpha1VPCEndpointSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
