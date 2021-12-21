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
from kubernetes.client.models.io_xk8s_cluster_v1beta1_machine_health_check_status import IoXK8sClusterV1beta1MachineHealthCheckStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterV1beta1MachineHealthCheckStatus(unittest.TestCase):
    """IoXK8sClusterV1beta1MachineHealthCheckStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterV1beta1MachineHealthCheckStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_v1beta1_machine_health_check_status.IoXK8sClusterV1beta1MachineHealthCheckStatus()  # noqa: E501
        if include_optional :
            return IoXK8sClusterV1beta1MachineHealthCheckStatus(
                conditions = [
                    kubernetes.client.models.io_x_k8s_cluster_addons_v1beta1_cluster_resource_set_status_conditions.io_x_k8s_cluster_addons_v1beta1_ClusterResourceSet_status_conditions(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        severity = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                current_healthy = 0, 
                expected_machines = 0, 
                observed_generation = 56, 
                remediations_allowed = 0, 
                targets = [
                    '0'
                    ]
            )
        else :
            return IoXK8sClusterV1beta1MachineHealthCheckStatus(
        )

    def testIoXK8sClusterV1beta1MachineHealthCheckStatus(self):
        """Test IoXK8sClusterV1beta1MachineHealthCheckStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
