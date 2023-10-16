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
from kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy import OrgProjectcalicoCrdV1GlobalNetworkPolicy  # noqa: E501
from kubernetes.client.rest import ApiException

class TestOrgProjectcalicoCrdV1GlobalNetworkPolicy(unittest.TestCase):
    """OrgProjectcalicoCrdV1GlobalNetworkPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrgProjectcalicoCrdV1GlobalNetworkPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy.OrgProjectcalicoCrdV1GlobalNetworkPolicy()  # noqa: E501
        if include_optional :
            return OrgProjectcalicoCrdV1GlobalNetworkPolicy(
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
                spec = kubernetes.client.models.org_projectcalico_crd_v1_global_network_policy_spec.org_projectcalico_crd_v1_GlobalNetworkPolicy_spec(
                    apply_on_forward = True, 
                    do_not_track = True, 
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
                            ip_version = 56, 
                            not_protocol = kubernetes.client.models.not_protocol.notProtocol(), 
                            protocol = kubernetes.client.models.protocol.protocol(), )
                        ], 
                    namespace_selector = '0', 
                    order = 1.337, 
                    pre_dnat = True, 
                    selector = '0', 
                    service_account_selector = '0', 
                    types = [
                        '0'
                        ], )
            )
        else :
            return OrgProjectcalicoCrdV1GlobalNetworkPolicy(
        )

    def testOrgProjectcalicoCrdV1GlobalNetworkPolicy(self):
        """Test OrgProjectcalicoCrdV1GlobalNetworkPolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
