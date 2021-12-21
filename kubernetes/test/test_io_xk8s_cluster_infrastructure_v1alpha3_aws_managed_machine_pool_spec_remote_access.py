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
from kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_spec_remote_access import IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess(unittest.TestCase):
    """IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_infrastructure_v1alpha3_aws_managed_machine_pool_spec_remote_access.IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess()  # noqa: E501
        if include_optional :
            return IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess(
                public = True, 
                source_security_groups = [
                    '0'
                    ], 
                ssh_key_name = '0'
            )
        else :
            return IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess(
        )

    def testIoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess(self):
        """Test IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
