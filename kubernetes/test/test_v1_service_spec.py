# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_service_spec import V1ServiceSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ServiceSpec(unittest.TestCase):
    """V1ServiceSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ServiceSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_service_spec.V1ServiceSpec()  # noqa: E501
        if include_optional :
            return V1ServiceSpec(
                allocate_load_balancer_node_ports = True, 
                cluster_ip = '0', 
                cluster_i_ps = [
                    '0'
                    ], 
                external_i_ps = [
                    '0'
                    ], 
                external_name = '0', 
                external_traffic_policy = '0', 
                health_check_node_port = 56, 
                ip_families = [
                    '0'
                    ], 
                ip_family_policy = '0', 
                load_balancer_ip = '0', 
                load_balancer_source_ranges = [
                    '0'
                    ], 
                ports = [
                    kubernetes.client.models.v1/service_port.v1.ServicePort(
                        app_protocol = '0', 
                        name = '0', 
                        node_port = 56, 
                        port = 56, 
                        protocol = '0', 
                        target_port = kubernetes.client.models.target_port.targetPort(), )
                    ], 
                publish_not_ready_addresses = True, 
                selector = {
                    'key' : '0'
                    }, 
                session_affinity = '0', 
                session_affinity_config = kubernetes.client.models.v1/session_affinity_config.v1.SessionAffinityConfig(
                    kubernetes.client_ip = kubernetes.client.models.v1/kubernetes.client_ip_config.v1.ClientIPConfig(
                        timeout_seconds = 56, ), ), 
                topology_keys = [
                    '0'
                    ], 
                type = '0'
            )
        else :
            return V1ServiceSpec(
        )

    def testV1ServiceSpec(self):
        """Test V1ServiceSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
