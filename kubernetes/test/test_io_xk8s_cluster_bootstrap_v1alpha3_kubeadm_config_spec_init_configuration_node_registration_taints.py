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
from kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_init_configuration_node_registration_taints import IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints(unittest.TestCase):
    """IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_kubeadm_config_spec_init_configuration_node_registration_taints.IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints()  # noqa: E501
        if include_optional :
            return IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints(
                effect = '0', 
                key = '0', 
                time_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                value = '0'
            )
        else :
            return IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints(
                effect = '0',
                key = '0',
        )

    def testIoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints(self):
        """Test IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
