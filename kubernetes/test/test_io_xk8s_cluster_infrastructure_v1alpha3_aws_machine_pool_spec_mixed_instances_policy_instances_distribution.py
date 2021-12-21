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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_machine_pool_spec_mixed_instances_policy_instances_distribution import IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_machine_pool_spec_mixed_instances_policy_instances_distribution.IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution(
                on_demand_allocation_strategy = 'prioritized', 
                on_demand_base_capacity = 56, 
                on_demand_percentage_above_base_capacity = 56, 
                spot_allocation_strategy = 'lowest-price'
            )
        else :
            return IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution(
        )

    def testIoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution(self):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
