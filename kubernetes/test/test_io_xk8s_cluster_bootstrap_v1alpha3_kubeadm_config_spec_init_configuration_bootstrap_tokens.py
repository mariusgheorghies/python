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
from kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_init_configuration_bootstrap_tokens import IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens(unittest.TestCase):
    """IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_init_configuration_bootstrap_tokens.IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens()  # noqa: E501
        if include_optional :
            return IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens(
                description = '0', 
                expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                groups = [
                    '0'
                    ], 
                token = '0', 
                ttl = '0', 
                usages = [
                    '0'
                    ]
            )
        else :
            return IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens(
                token = '0',
        )

    def testIoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens(self):
        """Test IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
