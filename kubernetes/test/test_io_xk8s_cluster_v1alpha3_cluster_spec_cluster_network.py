# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.io_xk8s_cluster_v1alpha3_cluster_spec_cluster_network import IoXK8sClusterV1alpha3ClusterSpecClusterNetwork  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterV1alpha3ClusterSpecClusterNetwork(unittest.TestCase):
    """IoXK8sClusterV1alpha3ClusterSpecClusterNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterV1alpha3ClusterSpecClusterNetwork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_v1alpha3_cluster_spec_cluster_network.IoXK8sClusterV1alpha3ClusterSpecClusterNetwork()  # noqa: E501
        if include_optional :
            return IoXK8sClusterV1alpha3ClusterSpecClusterNetwork(
                api_server_port = 56, 
                pods = kubernetes.client.models.io_x_k8s_cluster_v1alpha3_cluster_spec_cluster_network_pods.io_x_k8s_cluster_v1alpha3_Cluster_spec_clusterNetwork_pods(
                    cidr_blocks = [
                        '0'
                        ], ), 
                service_domain = '0', 
                services = kubernetes.client.models.io_x_k8s_cluster_v1alpha3_cluster_spec_cluster_network_services.io_x_k8s_cluster_v1alpha3_Cluster_spec_clusterNetwork_services(
                    cidr_blocks = [
                        '0'
                        ], )
            )
        else :
            return IoXK8sClusterV1alpha3ClusterSpecClusterNetwork(
        )

    def testIoXK8sClusterV1alpha3ClusterSpecClusterNetwork(self):
        """Test IoXK8sClusterV1alpha3ClusterSpecClusterNetwork"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
