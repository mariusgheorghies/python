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
from kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_list import AwsK8sServicesEc2V1alpha1RouteTableList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sServicesEc2V1alpha1RouteTableList(unittest.TestCase):
    """AwsK8sServicesEc2V1alpha1RouteTableList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sServicesEc2V1alpha1RouteTableList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_list.AwsK8sServicesEc2V1alpha1RouteTableList()  # noqa: E501
        if include_optional :
            return AwsK8sServicesEc2V1alpha1RouteTableList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.aws/k8s/services/ec2/v1alpha1/route_table.aws.k8s.services.ec2.v1alpha1.RouteTable(
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
                        spec = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec.aws_k8s_services_ec2_v1alpha1_RouteTable_spec(
                            routes = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_routes.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_routes(
                                    carrier_gateway_id = '0', 
                                    core_network_arn = '0', 
                                    destination_cidr_block = '0', 
                                    destination_i_pv6_cidr_block = '0', 
                                    destination_prefix_list_id = '0', 
                                    egress_only_internet_gateway_id = '0', 
                                    gateway_id = '0', 
                                    gateway_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_gateway_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_gatewayRef(
                                        from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                                            name = '0', ), ), 
                                    instance_id = '0', 
                                    local_gateway_id = '0', 
                                    nat_gateway_id = '0', 
                                    nat_gateway_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_nat_gateway_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_natGatewayRef(), 
                                    network_interface_id = '0', 
                                    transit_gateway_id = '0', 
                                    transit_gateway_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_transit_gateway_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_transitGatewayRef(), 
                                    vpc_endpoint_id = '0', 
                                    vpc_endpoint_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_vpc_endpoint_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_vpcEndpointRef(), 
                                    vpc_peering_connection_id = '0', )
                                ], 
                            tags = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_tags.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_tags(
                                    key = '0', 
                                    value = '0', )
                                ], 
                            vpc_id = '0', 
                            vpc_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(), ), 
                        status = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status.aws_k8s_services_ec2_v1alpha1_RouteTable_status(
                            ack_resource_metadata = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_ack_resource_metadata.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_ackResourceMetadata(
                                arn = '0', 
                                owner_account_id = '0', 
                                region = '0', ), 
                            associations = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_associations.aws_k8s_services_ec2_v1alpha1_RouteTable_status_associations(
                                    association_state = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_association_state.aws_k8s_services_ec2_v1alpha1_RouteTable_status_associationState(
                                        state = '0', 
                                        status_message = '0', ), 
                                    gateway_id = '0', 
                                    main = True, 
                                    route_table_association_id = '0', 
                                    route_table_id = '0', 
                                    subnet_id = '0', )
                                ], 
                            conditions = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_conditions.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            owner_id = '0', 
                            propagating_vg_ws = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_propagating_vg_ws.aws_k8s_services_ec2_v1alpha1_RouteTable_status_propagatingVGWs(
                                    gateway_id = '0', )
                                ], 
                            route_statuses = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_route_statuses.aws_k8s_services_ec2_v1alpha1_RouteTable_status_routeStatuses(
                                    carrier_gateway_id = '0', 
                                    core_network_arn = '0', 
                                    destination_cidr_block = '0', 
                                    destination_i_pv6_cidr_block = '0', 
                                    destination_prefix_list_id = '0', 
                                    egress_only_internet_gateway_id = '0', 
                                    gateway_id = '0', 
                                    instance_id = '0', 
                                    instance_owner_id = '0', 
                                    local_gateway_id = '0', 
                                    nat_gateway_id = '0', 
                                    network_interface_id = '0', 
                                    origin = '0', 
                                    state = '0', 
                                    transit_gateway_id = '0', 
                                    vpc_peering_connection_id = '0', )
                                ], 
                            route_table_id = '0', ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return AwsK8sServicesEc2V1alpha1RouteTableList(
                items = [
                    kubernetes.client.models.aws/k8s/services/ec2/v1alpha1/route_table.aws.k8s.services.ec2.v1alpha1.RouteTable(
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
                        spec = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec.aws_k8s_services_ec2_v1alpha1_RouteTable_spec(
                            routes = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_routes.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_routes(
                                    carrier_gateway_id = '0', 
                                    core_network_arn = '0', 
                                    destination_cidr_block = '0', 
                                    destination_i_pv6_cidr_block = '0', 
                                    destination_prefix_list_id = '0', 
                                    egress_only_internet_gateway_id = '0', 
                                    gateway_id = '0', 
                                    gateway_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_gateway_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_gatewayRef(
                                        from = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_from.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_from(
                                            name = '0', ), ), 
                                    instance_id = '0', 
                                    local_gateway_id = '0', 
                                    nat_gateway_id = '0', 
                                    nat_gateway_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_nat_gateway_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_natGatewayRef(), 
                                    network_interface_id = '0', 
                                    transit_gateway_id = '0', 
                                    transit_gateway_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_transit_gateway_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_transitGatewayRef(), 
                                    vpc_endpoint_id = '0', 
                                    vpc_endpoint_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_spec_vpc_endpoint_ref.aws_k8s_services_ec2_v1alpha1_RouteTable_spec_vpcEndpointRef(), 
                                    vpc_peering_connection_id = '0', )
                                ], 
                            tags = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_tags.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_tags(
                                    key = '0', 
                                    value = '0', )
                                ], 
                            vpc_id = '0', 
                            vpc_ref = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_spec_vpc_refs.aws_k8s_services_ec2_v1alpha1_DHCPOptions_spec_vpcRefs(), ), 
                        status = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status.aws_k8s_services_ec2_v1alpha1_RouteTable_status(
                            ack_resource_metadata = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_ack_resource_metadata.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_ackResourceMetadata(
                                arn = '0', 
                                owner_account_id = '0', 
                                region = '0', ), 
                            associations = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_associations.aws_k8s_services_ec2_v1alpha1_RouteTable_status_associations(
                                    association_state = kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_association_state.aws_k8s_services_ec2_v1alpha1_RouteTable_status_associationState(
                                        state = '0', 
                                        status_message = '0', ), 
                                    gateway_id = '0', 
                                    main = True, 
                                    route_table_association_id = '0', 
                                    route_table_id = '0', 
                                    subnet_id = '0', )
                                ], 
                            conditions = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_dhcp_options_status_conditions.aws_k8s_services_ec2_v1alpha1_DHCPOptions_status_conditions(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            owner_id = '0', 
                            propagating_vg_ws = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_propagating_vg_ws.aws_k8s_services_ec2_v1alpha1_RouteTable_status_propagatingVGWs(
                                    gateway_id = '0', )
                                ], 
                            route_statuses = [
                                kubernetes.client.models.aws_k8s_services_ec2_v1alpha1_route_table_status_route_statuses.aws_k8s_services_ec2_v1alpha1_RouteTable_status_routeStatuses(
                                    carrier_gateway_id = '0', 
                                    core_network_arn = '0', 
                                    destination_cidr_block = '0', 
                                    destination_i_pv6_cidr_block = '0', 
                                    destination_prefix_list_id = '0', 
                                    egress_only_internet_gateway_id = '0', 
                                    gateway_id = '0', 
                                    instance_id = '0', 
                                    instance_owner_id = '0', 
                                    local_gateway_id = '0', 
                                    nat_gateway_id = '0', 
                                    network_interface_id = '0', 
                                    origin = '0', 
                                    state = '0', 
                                    transit_gateway_id = '0', 
                                    vpc_peering_connection_id = '0', )
                                ], 
                            route_table_id = '0', ), )
                    ],
        )

    def testAwsK8sServicesEc2V1alpha1RouteTableList(self):
        """Test AwsK8sServicesEc2V1alpha1RouteTableList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()