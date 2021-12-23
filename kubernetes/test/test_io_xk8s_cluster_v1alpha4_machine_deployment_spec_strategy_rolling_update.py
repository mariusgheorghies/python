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
from kubernetes.client.models.io_xk8s_cluster_v1alpha4_machine_deployment_spec_strategy_rolling_update import IoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate(unittest.TestCase):
    """IoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_v1alpha4_machine_deployment_spec_strategy_rolling_update.IoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate()  # noqa: E501
        if include_optional :
            return IoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate(
                delete_policy = 'Random', 
                max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable()
            )
        else :
            return IoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate(
        )

    def testIoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate(self):
        """Test IoXK8sClusterV1alpha4MachineDeploymentSpecStrategyRollingUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
