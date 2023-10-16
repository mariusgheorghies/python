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
from kubernetes.client.models.org_projectcalico_crd_v1_network_policy_spec import OrgProjectcalicoCrdV1NetworkPolicySpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestOrgProjectcalicoCrdV1NetworkPolicySpec(unittest.TestCase):
    """OrgProjectcalicoCrdV1NetworkPolicySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrgProjectcalicoCrdV1NetworkPolicySpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.org_projectcalico_crd_v1_network_policy_spec.OrgProjectcalicoCrdV1NetworkPolicySpec()  # noqa: E501
        if include_optional :
            return OrgProjectcalicoCrdV1NetworkPolicySpec(
                egress = [
                    kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_egress.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_egress(
                        action = '0', 
                        destination = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_destination.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_destination(
                            namespace_selector = '0', 
                            nets = [
                                '0'
                                ], 
                            not_nets = [
                                '0'
                                ], 
                            not_ports = [
                                None
                                ], 
                            not_selector = '0', 
                            ports = [
                                None
                                ], 
                            selector = '0', 
                            service_accounts = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_destination_service_accounts.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_destination_serviceAccounts(
                                names = [
                                    '0'
                                    ], 
                                selector = '0', ), ), 
                        http = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_http.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_http(
                            methods = [
                                '0'
                                ], 
                            paths = [
                                kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_http_paths.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_http_paths(
                                    exact = '0', 
                                    prefix = '0', )
                                ], ), 
                        icmp = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_icmp.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_icmp(
                            code = 56, 
                            type = 56, ), 
                        ip_version = 56, 
                        metadata = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_metadata.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_metadata(
                            annotations = {
                                'key' : '0'
                                }, ), 
                        not_icmp = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_not_icmp.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_notICMP(
                            code = 56, 
                            type = 56, ), 
                        not_protocol = kubernetes.client.models.not_protocol.notProtocol(), 
                        protocol = kubernetes.client.models.protocol.protocol(), 
                        source = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_source.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_source(
                            namespace_selector = '0', 
                            not_selector = '0', 
                            selector = '0', ), )
                    ], 
                ingress = [
                    kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_egress.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_egress(
                        action = '0', 
                        destination = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_destination.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_destination(
                            namespace_selector = '0', 
                            nets = [
                                '0'
                                ], 
                            not_nets = [
                                '0'
                                ], 
                            not_ports = [
                                None
                                ], 
                            not_selector = '0', 
                            ports = [
                                None
                                ], 
                            selector = '0', 
                            service_accounts = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_destination_service_accounts.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_destination_serviceAccounts(
                                names = [
                                    '0'
                                    ], 
                                selector = '0', ), ), 
                        http = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_http.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_http(
                            methods = [
                                '0'
                                ], 
                            paths = [
                                kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_http_paths.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_http_paths(
                                    exact = '0', 
                                    prefix = '0', )
                                ], ), 
                        icmp = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_icmp.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_icmp(
                            code = 56, 
                            type = 56, ), 
                        ip_version = 56, 
                        metadata = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_metadata.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_metadata(
                            annotations = {
                                'key' : '0'
                                }, ), 
                        not_icmp = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_not_icmp.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_notICMP(
                            code = 56, 
                            type = 56, ), 
                        not_protocol = kubernetes.client.models.not_protocol.notProtocol(), 
                        protocol = kubernetes.client.models.protocol.protocol(), 
                        source = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec_source.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec_source(
                            namespace_selector = '0', 
                            not_selector = '0', 
                            selector = '0', ), )
                    ], 
                order = 1.337, 
                selector = '0', 
                service_account_selector = '0', 
                types = [
                    '0'
                    ]
            )
        else :
            return OrgProjectcalicoCrdV1NetworkPolicySpec(
        )

    def testOrgProjectcalicoCrdV1NetworkPolicySpec(self):
        """Test OrgProjectcalicoCrdV1NetworkPolicySpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()