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
from kubernetes.client.models.org_projectcalico_crd_v1_host_endpoint_list import OrgProjectcalicoCrdV1HostEndpointList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestOrgProjectcalicoCrdV1HostEndpointList(unittest.TestCase):
    """OrgProjectcalicoCrdV1HostEndpointList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrgProjectcalicoCrdV1HostEndpointList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.org_projectcalico_crd_v1_host_endpoint_list.OrgProjectcalicoCrdV1HostEndpointList()  # noqa: E501
        if include_optional :
            return OrgProjectcalicoCrdV1HostEndpointList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.org/projectcalico/crd/v1/host_endpoint.org.projectcalico.crd.v1.HostEndpoint(
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
                        spec = kubernetes.client.models.org_projectcalico_crd_v1_host_endpoint_spec.org_projectcalico_crd_v1_HostEndpoint_spec(
                            expected_i_ps = [
                                '0'
                                ], 
                            interface_name = '0', 
                            node = '0', 
                            ports = [
                                kubernetes.client.models.org_projectcalico_crd_v1_host_endpoint_spec_ports.org_projectcalico_crd_v1_HostEndpoint_spec_ports(
                                    name = '0', 
                                    port = 56, 
                                    protocol = kubernetes.client.models.protocol.protocol(), )
                                ], 
                            profiles = [
                                '0'
                                ], ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return OrgProjectcalicoCrdV1HostEndpointList(
                items = [
                    kubernetes.client.models.org/projectcalico/crd/v1/host_endpoint.org.projectcalico.crd.v1.HostEndpoint(
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
                        spec = kubernetes.client.models.org_projectcalico_crd_v1_host_endpoint_spec.org_projectcalico_crd_v1_HostEndpoint_spec(
                            expected_i_ps = [
                                '0'
                                ], 
                            interface_name = '0', 
                            node = '0', 
                            ports = [
                                kubernetes.client.models.org_projectcalico_crd_v1_host_endpoint_spec_ports.org_projectcalico_crd_v1_HostEndpoint_spec_ports(
                                    name = '0', 
                                    port = 56, 
                                    protocol = kubernetes.client.models.protocol.protocol(), )
                                ], 
                            profiles = [
                                '0'
                                ], ), )
                    ],
        )

    def testOrgProjectcalicoCrdV1HostEndpointList(self):
        """Test OrgProjectcalicoCrdV1HostEndpointList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
