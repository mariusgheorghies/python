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
from kubernetes.client.models.io_xk8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_endpoint_access import IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess(unittest.TestCase):
    """IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_controlplane_v1alpha3_aws_managed_control_plane_spec_endpoint_access.IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess()  # noqa: E501
        if include_optional :
            return IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess(
                private = True, 
                public = True, 
                public_cid_rs = [
                    '0'
                    ]
            )
        else :
            return IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess(
        )

    def testIoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess(self):
        """Test IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
