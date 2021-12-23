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
from kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_networking import IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking(unittest.TestCase):
    """IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_cluster_configuration_networking.IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking()  # noqa: E501
        if include_optional :
            return IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking(
                dns_domain = '0', 
                pod_subnet = '0', 
                service_subnet = '0'
            )
        else :
            return IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking(
        )

    def testIoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking(self):
        """Test IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
