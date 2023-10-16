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
from kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network import IoTigeraOperatorV1InstallationSpecCalicoNetwork  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoTigeraOperatorV1InstallationSpecCalicoNetwork(unittest.TestCase):
    """IoTigeraOperatorV1InstallationSpecCalicoNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoTigeraOperatorV1InstallationSpecCalicoNetwork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network.IoTigeraOperatorV1InstallationSpecCalicoNetwork()  # noqa: E501
        if include_optional :
            return IoTigeraOperatorV1InstallationSpecCalicoNetwork(
                bgp = 'Enabled', 
                container_ip_forwarding = 'Enabled', 
                host_ports = 'Enabled', 
                ip_pools = [
                    kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_ip_pools.io_tigera_operator_v1_Installation_spec_calicoNetwork_ipPools(
                        block_size = 56, 
                        cidr = '0', 
                        encapsulation = 'IPIPCrossSubnet', 
                        nat_outgoing = 'Enabled', 
                        node_selector = '0', )
                    ], 
                linux_dataplane = 'Iptables', 
                mtu = 56, 
                multi_interface_mode = 'None', 
                node_address_autodetection_v4 = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_node_address_autodetection_v4.io_tigera_operator_v1_Installation_spec_calicoNetwork_nodeAddressAutodetectionV4(
                    can_reach = '0', 
                    cidrs = [
                        '0'
                        ], 
                    first_found = True, 
                    interface = '0', 
                    skip_interface = '0', ), 
                node_address_autodetection_v6 = kubernetes.client.models.io_tigera_operator_v1_installation_spec_calico_network_node_address_autodetection_v6.io_tigera_operator_v1_Installation_spec_calicoNetwork_nodeAddressAutodetectionV6(
                    can_reach = '0', 
                    cidrs = [
                        '0'
                        ], 
                    first_found = True, 
                    interface = '0', 
                    skip_interface = '0', )
            )
        else :
            return IoTigeraOperatorV1InstallationSpecCalicoNetwork(
        )

    def testIoTigeraOperatorV1InstallationSpecCalicoNetwork(self):
        """Test IoTigeraOperatorV1InstallationSpecCalicoNetwork"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
