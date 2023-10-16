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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_elastic_ip_address_spec import AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1ElasticIPAddressSpec(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_elastic_ip_address_spec.AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec(
                address = '0', 
                customer_owned_i_pv4_pool = '0', 
                network_border_group = '0', 
                public_i_pv4_pool = '0', 
                tags = [
                    kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_tags.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_tags(
                        key = '0', 
                        value = '0', )
                    ]
            )
        else :
            return AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec(
        )

    def testAwsK8sServicesEc2V1alpha1ElasticIPAddressSpec(self):
        """Test AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()